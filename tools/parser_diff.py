#!/usr/bin/env python
"""Diff what a CRG checkout's parser produces, file by file.

``dump`` records the nodes and edges ONE checkout's parser extracts from
labelled JS/TS corpora; ``cmp`` compares two dumps and reports what moved.
It proves that a parser change only touches what it claims to touch: the PR #6
review compared ``main`` and the PR over 160 files of six corpora and found
+37 nodes in 20 files of one label and nothing in the other five.

``tests/test_real_repo_corpus.py`` compares twelve aggregate properties of
eight pinned public repositories (it needs a clone and the network). This tool
compares nodes and edges per file, in any local folder, offline.

    python -B tools/parser_diff.py dump <crg_root> <out.json> <label>=<corpus_dir> [...]
    python -B tools/parser_diff.py cmp <base.json> <candidate.json> [<label> ...] \
        [--json] [--expect-identical <label>[,<label>...]]

``dump`` imports ``code_review_graph`` from the given root, so run it without
``-I``: isolated mode drops the tree-sitter language packs and the parser
returns nothing in silence.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

CONTRACT = "crg.parser_diff.v1"
SOURCE_EXTENSIONS = {".ts", ".tsx", ".mts", ".cts", ".js", ".jsx", ".mjs", ".cjs"}
SKIPPED_DIRS = {"node_modules", ".git"}
COUNTERS = (
    "files", "identical", "changed", "same_error", "error_changed", "only_one_side",
    "errors", "nodes_added", "nodes_removed", "edges_added", "edges_removed",
)
UNLISTED_KINDS = ("identical", "same_error")
SAMPLE_LIMIT = 6
FULL_LIMIT = 200
EDGES_SHOWN = 4


def iter_source_files(corpus: Path):
    """Yield the JS/TS files of *corpus* in a stable order."""
    for dirpath, dirnames, filenames in os.walk(corpus):
        dirnames[:] = sorted(name for name in dirnames if name not in SKIPPED_DIRS)
        for filename in sorted(filenames):
            if Path(filename).suffix in SOURCE_EXTENSIONS:
                yield Path(dirpath) / filename


def dump_file(parser, path: Path) -> dict:
    """Return the nodes and edges *parser* extracts from *path*, sorted."""
    try:
        nodes, edges = parser.parse_file(path)
        return {
            "nodes": sorted(
                [node.kind, node.name, node.line_start, node.line_end] for node in nodes
            ),
            "edges": sorted(
                [edge.kind, edge.source, edge.target, edge.line] for edge in edges
            ),
        }
    except Exception as error:  # a parse failure is data for the diff, not a crash
        return {"error": f"{type(error).__name__}: {str(error)[:160]}"}


def dump_corpus(parser, corpus: Path) -> tuple[dict, dict]:
    """Dump every source file of *corpus*; return the files and their stats."""
    files, stats = {}, {"path": str(corpus), "seen": 0, "errors": 0}
    for path in iter_source_files(corpus):
        stats["seen"] += 1
        entry = dump_file(parser, path)
        stats["errors"] += "error" in entry
        files[path.relative_to(corpus).as_posix()] = entry
    return files, stats


def load_parser(repo_root: Path):
    """Import ``code_review_graph`` from *repo_root*; return its parser and file."""
    sys.path.insert(0, str(repo_root))
    try:
        import code_review_graph
    except ImportError as error:
        raise ImportError(
            f"cannot import code_review_graph from {repo_root} ({error}); run without -I"
        ) from error
    package_parent = Path(code_review_graph.__file__).resolve().parent.parent
    if package_parent != repo_root:
        raise ImportError(f"package resolved to {package_parent}, expected {repo_root}")
    from code_review_graph.parser import CodeParser

    parser_file = Path(sys.modules["code_review_graph.parser"].__file__).resolve()
    if not parser_file.is_relative_to(repo_root):
        raise ImportError(f"parser module came from {parser_file}")
    return CodeParser(), parser_file


def parse_corpora(arguments: list[str]) -> list[tuple[str, Path]]:
    """Turn ``label=directory`` arguments into (label, directory) pairs."""
    corpora = []
    for argument in arguments:
        label, separator, raw = argument.partition("=")
        if not (label and separator and raw):
            raise ValueError(f"expected <label>=<corpus_dir>, got {argument!r}")
        corpora.append((label, Path(raw).resolve()))
    return corpora


def dump(repo_root: Path, out_path: Path, corpora: list[tuple[str, Path]]) -> dict:
    """Write the dump of *corpora* to *out_path*; return the summary."""
    parser, parser_file = load_parser(repo_root)
    files, labels, started = {}, {}, time.time()
    for label, corpus in corpora:
        if not corpus.is_dir():
            labels[label] = {"path": str(corpus), "missing": True}
            continue
        dumped, labels[label] = dump_corpus(parser, corpus)
        files.update({f"{label}\t{name}": entry for name, entry in dumped.items()})
    content = {"parser_file": str(parser_file), "labels": labels, "files": files}
    out_path.write_text(json.dumps(content, ensure_ascii=False), encoding="utf-8")
    return {
        "parser": str(parser_file),
        "files": len(files),
        "nodes": sum(len(entry.get("nodes", ())) for entry in files.values()),
        "labels": labels,
        "seconds": round(time.time() - started, 1),
    }


def _moved(old: list, new: list) -> tuple[list, list]:
    """Return (added, removed) between two dumps of one file, as sorted lists."""
    old_set, new_set = {tuple(item) for item in old}, {tuple(item) for item in new}
    added = [list(item) for item in sorted(new_set - old_set)]
    removed = [list(item) for item in sorted(old_set - new_set)]
    return added, removed


def _classify_error(base: dict, candidate: dict) -> tuple[str, dict]:
    """Return (kind, change) for a file that failed to parse on at least one side."""
    if base == candidate:
        return "same_error", {}
    return "error_changed", {"base": base, "candidate": candidate}


def _classify(base: dict | None, candidate: dict | None) -> tuple[str, dict]:
    """Return (kind, change) for one file across two dumps."""
    if base is None or candidate is None:
        return "only_one_side", {"side": "candidate" if base is None else "base"}
    if "error" in base or "error" in candidate:
        return _classify_error(base, candidate)
    added_nodes, removed_nodes = _moved(base["nodes"], candidate["nodes"])
    added_edges, removed_edges = _moved(base["edges"], candidate["edges"])
    if not (added_nodes or removed_nodes or added_edges or removed_edges):
        return "identical", {}
    return "changed", {
        "nodes_added": added_nodes, "nodes_removed": removed_nodes,
        "edges_added": added_edges, "edges_removed": removed_edges,
    }


def _record(report: dict, name: str, kind: str, change: dict) -> None:
    """Count one classified file in its label's report."""
    report["files"] += 1
    report[kind] += 1
    if kind in ("same_error", "error_changed"):
        report["errors"] += 1
    for moved in ("nodes", "edges"):
        for side in ("added", "removed"):
            report[f"{moved}_{side}"] += len(change.get(f"{moved}_{side}", ()))
    if kind not in UNLISTED_KINDS:
        report["changed_files"].append({"file": name, "kind": kind, **change})


def compare(base: dict, candidate: dict) -> list[dict]:
    """Compare two dumps (their ``files`` mappings); return one report per label."""
    reports: dict[str, dict] = {}
    for key in sorted(set(base["files"]) | set(candidate["files"])):
        label, _, name = key.partition("\t")
        report = reports.setdefault(
            label, {"label": label, "changed_files": [], **{counter: 0 for counter in COUNTERS}},
        )
        kind, change = _classify(base["files"].get(key), candidate["files"].get(key))
        _record(report, name, kind, change)
    return [reports[label] for label in sorted(reports)]


def summary_line(report: dict) -> str:
    """One line per label: what moved in that corpus."""
    return (
        f"[{report['label']}] files={report['files']} identical={report['identical']} "
        f"changed={report['changed']} nodes +{report['nodes_added']}/-{report['nodes_removed']} "
        f"edges +{report['edges_added']}/-{report['edges_removed']} errors={report['errors']} "
        f"error_changed={report['error_changed']} only_one_side={report['only_one_side']}"
    )


def _format_change(change: dict) -> list[str]:
    kind, name = change["kind"], change["file"]
    if kind == "error_changed":
        return [f"    {name}: error changed: {change['base']} -> {change['candidate']}"]
    if kind == "only_one_side":
        return [f"    {name}: ONLY IN {change['side']}"]
    added = sorted(f"{edge[0]} {edge[1]} -> {edge[2]}" for edge in change["edges_added"])
    removed = sorted(f"{edge[0]} {edge[1]} -> {edge[2]}" for edge in change["edges_removed"])
    lines = [
        f"    {name}: nodes +{change['nodes_added']} -{change['nodes_removed']}"
        f" | edges +{len(added)} -{len(removed)}"
    ]
    lines += [f"        edge- {edge}" for edge in removed[:EDGES_SHOWN]]
    lines += [f"        edge+ {edge}" for edge in added[:EDGES_SHOWN]]
    return lines


def format_report(report: dict, full: bool = False) -> list[str]:
    """Human-readable lines of one label's report; *full* lists every change."""
    limit = FULL_LIMIT if full else SAMPLE_LIMIT
    lines = [summary_line(report)]
    for change in report["changed_files"][:limit]:
        lines.extend(_format_change(change))
    hidden = len(report["changed_files"]) - limit
    if hidden > 0:
        lines.append(f"    (+{hidden} changed files not listed; pass the label to list them all)")
    return lines


def unexpected(reports: list[dict], labels: list[str]) -> list[str]:
    """Return the problems in the labels that had to stay identical."""
    by_label = {report["label"]: report for report in reports}
    problems = []
    for label in labels:
        report = by_label.get(label)
        if report is None:
            problems.append(f"[{label}] label missing from the dumps")
        elif report["files"] != report["identical"] + report["same_error"]:
            problems.append(summary_line(report))
    return problems


def _schema() -> int:
    print(json.dumps({
        "contract": CONTRACT,
        "dump_file": {
            "parser_file": "parser that produced the dump",
            "labels": {
                "<label>": {
                    "path": "corpus folder",
                    "seen": "source files found",
                    "errors": "files the parser could not read",
                    "missing": "true when the folder does not exist",
                },
            },
            "files": {
                "<label>\\t<relative path>": {
                    "nodes": "[kind, name, line_start, line_end], sorted",
                    "edges": "[kind, source, target, line], sorted",
                    "error": "instead of nodes and edges, when the parser failed",
                },
            },
        },
        "report": "one per label: label, files, identical, changed, same_error, "
                  "error_changed, only_one_side, errors, nodes_added, nodes_removed, "
                  "edges_added, edges_removed, changed_files[]",
        "commands": {
            "dump": "<crg_root> <out.json> <label>=<corpus_dir> [...]",
            "cmp": "<base.json> <candidate.json> [<label> ...] [--json] "
                   "[--expect-identical <label>[,<label>...]]",
        },
        "requires": "dump imports code_review_graph from the given root: run it without -I",
        "exit_codes": {
            "0": "no problem",
            "1": "cmp: a label of --expect-identical moved or is missing from the dumps",
            "2": "invalid usage, tree not importable or dump unreadable",
        },
    }, ensure_ascii=False, indent=1))
    return 0


def _usage() -> int:
    run = "python -B tools/parser_diff.py"
    print(f"{run} dump <crg_root> base.json app=/path/corpus probes=/path/probes")
    print(f"{run} dump <other_crg_root> candidate.json app=/path/corpus probes=/path/probes")
    print(f"{run} cmp base.json candidate.json --expect-identical app")
    print(f"{run} cmp base.json candidate.json probes --json")
    return 0


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="parser_diff.py",
        description="Diff what a CRG checkout's parser produces, file by file.",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    dump_command = commands.add_parser("dump", help="record one checkout's parser output")
    dump_command.add_argument("repo_root", help="root of the CRG checkout whose parser is used")
    dump_command.add_argument("out", help="JSON file to write")
    dump_command.add_argument("corpora", nargs="+", metavar="label=dir", help="corpus folder")
    cmp_command = commands.add_parser("cmp", help="compare two dumps")
    cmp_command.add_argument("base")
    cmp_command.add_argument("candidate")
    cmp_command.add_argument("full", nargs="*", metavar="label", help="labels to list in full")
    cmp_command.add_argument("--json", action="store_true", help="print the reports as JSON")
    cmp_command.add_argument(
        "--expect-identical", default="", metavar="label[,label]",
        help="labels that must not move; any change in them exits 1",
    )
    return parser.parse_args(argv)


def _run_dump(args: argparse.Namespace) -> int:
    try:
        corpora = parse_corpora(args.corpora)
        summary = dump(Path(args.repo_root).resolve(), Path(args.out), corpora)
    except (ImportError, OSError, ValueError) as error:
        print(f"abort: {error}", file=sys.stderr)
        return 2
    print(json.dumps(summary, ensure_ascii=False))
    return 0


def _read_dump(path: str) -> dict:
    """Return the parsed content of a dump file."""
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _run_cmp(args: argparse.Namespace) -> int:
    try:
        base, candidate = _read_dump(args.base), _read_dump(args.candidate)
        reports = compare(base, candidate)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(f"abort: unreadable dump ({type(error).__name__}: {error})", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps({"contract": CONTRACT, "reports": reports}, ensure_ascii=False))
    else:
        for report in reports:
            print("\n".join(format_report(report, report["label"] in args.full)))
    labels = [label for label in args.expect_identical.split(",") if label]
    problems = unexpected(reports, labels)
    for problem in problems:
        print(f"UNEXPECTED: {problem}", file=sys.stderr)
    return 1 if problems else 0


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--schema" in argv:
        return _schema()
    if "--usage" in argv:
        return _usage()
    args = _parse_args(argv)
    return _run_dump(args) if args.command == "dump" else _run_cmp(args)


if __name__ == "__main__":
    sys.exit(main())
