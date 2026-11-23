"""Tests for tools/parser_diff.py: what a parser change moved, file by file."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "tools" / "parser_diff.py"

_spec = importlib.util.spec_from_file_location("parser_diff", TOOL)
parser_diff = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(parser_diff)


def _entry(*names, edges=()):
    return {
        "nodes": [["Function", name, 1, 2] for name in names],
        "edges": [list(edge) for edge in edges],
    }


def _dump(files):
    return {"parser_file": "unused", "labels": {}, "files": files}


def _run(*arguments):
    return subprocess.run(
        [sys.executable, "-B", str(TOOL), *map(str, arguments)],
        capture_output=True, text=True, encoding="utf-8",
    )


class TestCompare:
    def test_identical_files_are_counted_and_not_listed(self):
        files = {"app\ta.js": _entry("load"), "app\tb.js": _entry("save")}
        (report,) = parser_diff.compare(_dump(files), _dump(files))
        assert report["files"] == report["identical"] == 2
        assert report["changed_files"] == []

    def test_added_and_removed_nodes_and_edges_are_counted(self):
        base = {"app\ta.js": _entry("load", "gone", edges=[("CALLS", "load", "gone", 3)])}
        candidate = {"app\ta.js": _entry("load", "new")}
        (report,) = parser_diff.compare(_dump(base), _dump(candidate))
        assert (report["nodes_added"], report["nodes_removed"]) == (1, 1)
        assert (report["edges_added"], report["edges_removed"]) == (0, 1)
        (change,) = report["changed_files"]
        assert (change["file"], change["kind"]) == ("a.js", "changed")
        assert change["nodes_added"] == [["Function", "new", 1, 2]]
        assert change["edges_removed"] == [["CALLS", "load", "gone", 3]]

    def test_order_inside_one_dump_does_not_count_as_a_change(self):
        base = {"app\ta.js": _entry("load", "save")}
        candidate = {"app\ta.js": _entry("save", "load")}
        (report,) = parser_diff.compare(_dump(base), _dump(candidate))
        assert report["identical"] == 1

    def test_file_on_one_side_only_and_changed_error_are_reported(self):
        base = {"app\ta.js": {"error": "SyntaxError: x"}, "app\tb.js": _entry("b")}
        candidate = {"app\ta.js": {"error": "SyntaxError: y"}, "app\tc.js": _entry("c")}
        (report,) = parser_diff.compare(_dump(base), _dump(candidate))
        assert (report["error_changed"], report["only_one_side"]) == (1, 2)
        assert [change["kind"] for change in report["changed_files"]] == [
            "error_changed", "only_one_side", "only_one_side",
        ]
        assert [change["side"] for change in report["changed_files"][1:]] == [
            "base", "candidate",
        ]

    def test_the_same_parse_error_on_both_sides_is_not_a_change(self):
        files = {"app\ta.js": {"error": "SyntaxError: x"}}
        (report,) = parser_diff.compare(_dump(files), _dump(files))
        assert (report["errors"], report["same_error"]) == (1, 1)
        assert report["changed_files"] == []

    def test_reports_are_split_by_label(self):
        files = {"two\ta.js": _entry("a"), "one\ta.js": _entry("a")}
        reports = parser_diff.compare(_dump(files), _dump(files))
        assert [report["label"] for report in reports] == ["one", "two"]

    def test_expected_identical_label_fails_on_any_movement_or_absence(self):
        clean = _dump({"app\ta.js": _entry("a")})
        (moved_report,) = parser_diff.compare(clean, _dump({"app\ta.js": _entry("a", "b")}))
        assert parser_diff.unexpected([moved_report], ["app"]) == [
            parser_diff.summary_line(moved_report),
        ]
        assert parser_diff.unexpected([moved_report], ["other"]) == [
            "[other] label missing from the dumps",
        ]
        assert parser_diff.unexpected(parser_diff.compare(clean, clean), ["app"]) == []


class TestLoadParser:
    def test_a_tree_that_resolves_to_another_checkout_is_refused(self, tmp_path):
        # The package is already imported, so asking for another root is refused
        # instead of silently dumping the already-loaded parser.
        importlib.import_module("code_review_graph")
        with pytest.raises(ImportError, match="resolved to"):
            parser_diff.load_parser(tmp_path)

    def test_corpora_arguments_need_a_label_and_a_folder(self):
        assert parser_diff.parse_corpora(["app=/tmp/a"]) == [("app", Path("/tmp/a").resolve())]
        with pytest.raises(ValueError, match=r"expected <label>=<corpus_dir>"):
            parser_diff.parse_corpora(["/tmp/a"])


class TestCommandLine:
    def test_triad_help_schema_and_usage(self, tmp_path):
        for flag, check in (
            ("--help", lambda out: "dump" in out and "cmp" in out),
            ("--schema", lambda out: json.loads(out)["contract"] == "crg.parser_diff.v1"),
            ("--usage", lambda out: "dump" in out and "--expect-identical" in out),
        ):
            completed = _run(flag)
            assert completed.returncode == 0, completed.stderr
            assert check(completed.stdout)
        assert list(tmp_path.iterdir()) == []

    def _dump(self, corpus, out):
        completed = _run("dump", ROOT, out, f"corpus={corpus}")
        assert completed.returncode == 0, completed.stderr
        return json.loads(completed.stdout)

    def test_dump_then_cmp_shows_exactly_what_the_corpus_change_moved(self, tmp_path):
        # One corpus folder, dumped twice: the real use is the same corpora
        # read by two checkouts, and absolute paths are part of node names.
        corpus, dumps = tmp_path / "corpus", tmp_path / "dumps"
        for folder in (corpus, dumps):
            folder.mkdir()
        (corpus / "a.js").write_text("function load() { return 1; }\n", encoding="utf-8")
        # A dependency folder is not part of the corpus.
        (corpus / "node_modules").mkdir()
        (corpus / "node_modules" / "dep.js").write_text("function skipped() {}\n", encoding="utf-8")

        first = self._dump(corpus, dumps / "base.json")
        (corpus / "a.js").write_text(
            "function load() { return 1; }\nfunction save() { return load(); }\n",
            encoding="utf-8",
        )
        second = self._dump(corpus, dumps / "candidate.json")
        assert first["files"] == second["files"] == 1
        assert second["nodes"] - first["nodes"] == 1
        assert Path(first["parser"]).is_relative_to(ROOT)

        unchanged = _run(
            "cmp", dumps / "base.json", dumps / "base.json", "--expect-identical", "corpus",
        )
        assert (unchanged.returncode, "identical=1 changed=0") == (0, "identical=1 changed=0")

        text = _run("cmp", dumps / "base.json", dumps / "candidate.json")
        assert text.returncode == 0, text.stderr
        assert "[corpus] files=1 identical=0 changed=1" in text.stdout

        gate = _run(
            "cmp", dumps / "base.json", dumps / "candidate.json", "--expect-identical", "corpus",
        )
        assert gate.returncode == 1
        assert "UNEXPECTED: [corpus]" in gate.stderr

        as_json = _run("cmp", dumps / "base.json", dumps / "candidate.json", "--json")
        (report,) = json.loads(as_json.stdout)["reports"]
        (change,) = report["changed_files"]
        # save is the one function that appeared; nothing was removed. The File
        # node is listed again only because the file grew by a line.
        assert change["file"] == "a.js"
        assert [n for n in change["nodes_added"] if n[0] == "Function"] == [
            ["Function", "save", 2, 2],
        ]
        assert [n for n in change["nodes_removed"] if n[0] != "File"] == []

    def test_missing_corpus_folder_is_recorded_not_fatal(self, tmp_path):
        summary = self._dump(tmp_path / "absent", tmp_path / "out.json")
        assert summary["labels"]["corpus"]["missing"] is True
        assert json.loads((tmp_path / "out.json").read_text(encoding="utf-8"))["files"] == {}

    def test_invalid_usage_exits_2_with_the_reason(self, tmp_path):
        bad_label = _run("dump", ROOT, tmp_path / "out.json", "no-equal-sign")
        assert bad_label.returncode == 2
        assert "expected <label>=<corpus_dir>" in bad_label.stderr

        # A root that does not hold the package is refused. Which message comes
        # out depends on whether the package is also installed, so only the
        # refusal and the offending root are asserted.
        no_package = _run("dump", tmp_path, tmp_path / "out.json", f"app={tmp_path}")
        assert no_package.returncode == 2
        assert no_package.stderr.startswith("abort:") and str(tmp_path) in no_package.stderr

        not_a_dump = tmp_path / "not-a-dump.json"
        not_a_dump.write_text("{}", encoding="utf-8")
        unreadable = _run("cmp", not_a_dump, not_a_dump)
        assert (unreadable.returncode, "unreadable dump" in unreadable.stderr) == (2, True)
