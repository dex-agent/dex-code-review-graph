"""Check an explicit three-way merge in disposable Git repositories."""

from __future__ import annotations

import os
import shutil
import sqlite3
import subprocess
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from .changes import analyze_changes
from .graph import GraphStore, node_to_dict
from .incremental import _decode_name_status_paths, full_build
from .tools.build import _run_postprocess

EXIT_CODES = {"passed": 0, "text_conflict": 1, "regression": 1, "execution_error": 2}


def resolve_suite_command(command: list[str]) -> list[str]:
    """Resolve the suite executable via PATH (Windows: also PATHEXT .cmd/.bat).

    On Windows, spawning ``["npm", "test"]`` fails with WinError 2 because the
    real executable is ``npm.cmd`` (ISSUE-LOCAL-0006). Paths containing a
    directory separator are left untouched: they are resolved by the caller
    relative to the suite checkout, not to this process.
    """
    name = command[0]
    if os.sep in name or (os.altsep and os.altsep in name):
        return command
    executable = shutil.which(name)
    if executable:
        return [executable, *command[1:]]
    return command


def _git(repo, env, *args, check=True):
    return subprocess.run(
        ["git", "-C", str(repo), *map(str, args)],
        env=env,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        check=check,
    )


def _text(data: bytes) -> str:
    return data.decode("utf-8", errors="replace")


@contextmanager
def _isolated_graph_git(env: dict[str, str]) -> Iterator[None]:
    # The existing graph builder and diff helpers launch Git with the process environment.
    original = {key: value for key, value in os.environ.items() if key.upper().startswith("GIT_")}
    for key in original:
        del os.environ[key]
    git_env = {key: value for key, value in env.items() if key.startswith("GIT_")}
    os.environ.update(git_env)
    try:
        yield
    finally:
        for key in git_env:
            del os.environ[key]
        os.environ.update(original)


def _inspect_merge(repo: Path, database: Path, base: str, files: list[str]) -> dict:
    with GraphStore(database) as store:
        build = full_build(repo, store, recurse_submodules=False)
        warnings = _run_postprocess(store, build, "full", full_rebuild=True)
        analysis = analyze_changes(store, files, repo_root=str(repo), base=base)
        paths = [str(repo / path) for path in files]
        unindexed = [path for path in files if not store.get_nodes_by_file(str(repo / path))]
        impact = store.get_impact_radius(paths)
        candidates = {}
        for node in impact["changed_nodes"] + impact["impacted_nodes"]:
            if node.is_test:
                candidate = node_to_dict(node)
                candidate["file_path"] = Path(node.file_path).relative_to(repo).as_posix()
                candidate.pop("id", None)
                candidate["qualified_name"] = node.qualified_name.removeprefix(str(repo) + os.sep)
                candidates[node.qualified_name] = candidate
    partial = bool(unindexed or build["errors"] or warnings or analysis["test_gaps"]
                   or analysis["functions_truncated"] or impact["truncated"])
    return {
        "coverage": "incomplete" if partial else "no_graph_gaps_reported",
        "changed_files": files,
        "unindexed_files": unindexed,
        "build_errors": build["errors"],
        "build_warnings": warnings,
        "analysis_truncated": analysis["functions_truncated"] or impact["truncated"],
        "risk_score": analysis["risk_score"],
        "affected_flows": analysis["affected_flows"],
        "impacted_files": sorted(Path(path).relative_to(repo).as_posix()
                                 for path in impact["impacted_files"]),
        "test_gaps": analysis["test_gaps"],
        "test_candidates": list(candidates.values()),
    }


def _run_suite(root, objects, commits, command, failure_exit, env, report) -> str:
    command = resolve_suite_command(command)
    for name, commit in commits.items():
        checkout = root / f"suite-{name}"
        _git(root, env, "clone", "--shared", "--quiet", "--no-checkout", objects, checkout)
        _git(checkout, env, "checkout", "--quiet", "--detach", commit)
        result = subprocess.run(
            command, cwd=checkout, env=env, stdin=subprocess.DEVNULL, capture_output=True,
        )
        report[name] = {
            "exit_code": result.returncode,
            "stdout": _text(result.stdout),
            "stderr": _text(result.stderr),
        }
        if result.returncode == 0:
            continue
        if name == "merged" and result.returncode == failure_exit:
            return "regression"
        raise ValueError(f"Suite {name} exited with {result.returncode}.")
    return "passed"


def _check(root, source, refs, command, failure_exit, env, report) -> str:
    commits = {
        name: _text(_git(source, env, "rev-parse", "--verify", "--end-of-options",
                         f"{ref}^{{commit}}").stdout).strip()
        for name, ref in refs.items()
    }
    report["commits"] = commits
    base, ours, theirs = (commits[name] for name in ("base", "ours", "theirs"))
    objects = root / "merge"
    objects.mkdir()
    object_format = _text(_git(source, env, "rev-parse", "--show-object-format").stdout).strip()
    _git(objects, env, "init", "--quiet", f"--object-format={object_format}")
    _git(objects, env, "fetch", "--quiet", "--no-tags", "--no-write-fetch-head",
         source, *dict.fromkeys(commits.values()))
    for tip in (ours, theirs):
        ancestry = _git(objects, env, "merge-base", "--is-ancestor", base, tip, check=False)
        if ancestry.returncode == 1:
            raise ValueError("The base must be an ancestor of both commits.")
        ancestry.check_returncode()
    merge = _git(objects, env, "merge-tree", "--write-tree", f"--merge-base={base}",
                 ours, theirs, check=False)
    report["merge"] = {"exit_code": merge.returncode, "messages": _text(merge.stdout)}
    if merge.returncode == 1:
        return "text_conflict"
    merge.check_returncode()
    tree = _text(merge.stdout).strip()
    merged = _text(_git(
        objects, env, "-c", "user.name=CRG merge-check",
        "-c", "user.email=merge-check@example.invalid",
        "-c", "commit.gpgSign=false", "commit-tree", tree, "-p", ours, "-p", theirs,
        "-m", "CRG disposable merge-check",
    ).stdout).strip()
    report["merge"].update(tree=tree, commit=merged)
    _git(objects, env, "checkout", "--quiet", "--detach", merged)
    files = _decode_name_status_paths(
        _git(objects, env, "diff", "--name-status", "-z", base, merged, "--").stdout,
    )
    try:
        with _isolated_graph_git(env):
            report["graph"] = _inspect_merge(objects, root / "graph.db", base, files)
    except (OSError, sqlite3.Error) as exc:
        report["graph"] = {"coverage": "incomplete", "error": str(exc), "changed_files": files}
    return _run_suite(root, objects, {**commits, "merged": merged}, command, failure_exit,
                      env, report["suite"]["runs"])


def check_merge(
    source: Path, base: str, ours: str, theirs: str, command: list[str], failure_exit: int,
) -> dict:
    """Compare test outcomes for the base, both parents and the merged tree."""
    report = {"outcome": "execution_error", "merge": None, "graph": None,
              "suite": {"command": command, "failure_exit": failure_exit, "runs": {}}}
    try:
        if not command or not 1 <= failure_exit <= 255:
            raise ValueError("Supply a suite after -- and a test failure exit code from 1 to 255.")
        with tempfile.TemporaryDirectory(prefix="crg-merge-") as scratch:
            root = Path(scratch).resolve()
            env = {name: value for name, value in os.environ.items()
                   if not name.upper().startswith("GIT_")}
            env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1",
                       GIT_ATTR_NOSYSTEM="1", GIT_TERMINAL_PROMPT="0",
                       GIT_CONFIG_COUNT="1", GIT_CONFIG_KEY_0="core.hooksPath",
                       GIT_CONFIG_VALUE_0=os.devnull, CRG_DATA_DIR=str(root / "data"),
                       CRG_HOME=str(root / "registry"), PYTHONIOENCODING="utf-8")
            refs = {"base": base, "ours": ours, "theirs": theirs}
            report["outcome"] = _check(
                root, source.resolve(), refs, command, failure_exit, env, report,
            )
    except subprocess.CalledProcessError as exc:
        report["outcome"] = "execution_error"
        report["error"] = f"{exc.cmd[3]} exited with {exc.returncode}: {_text(exc.stderr).strip()}"
    except (OSError, ValueError, sqlite3.Error) as exc:
        report["outcome"] = "execution_error"
        report["error"] = str(exc)
    return report
