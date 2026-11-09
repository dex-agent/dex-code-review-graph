"""Reproduce Windows TS test edges caused by the PHPUnit path-normalization delta."""

import ast
import json
import os
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from code_review_graph import parser
from code_review_graph.graph import GraphStore
from code_review_graph.incremental import full_build
from code_review_graph.tools.query import query_graph


def git(*args):
    return subprocess.check_output(["git", *args], text=True).strip()


def baseline_detector(revision):
    tree = ast.parse(git("show", f"{revision}:code_review_graph/parser.py"))
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef)
                    and node.name == "_is_test_file")
    namespace = {"_TEST_FILE_PATTERNS": parser._TEST_FILE_PATTERNS}
    exec(compile(ast.Module(body=[function], type_ignores=[]), "<git-baseline>", "exec"),
         namespace)
    return namespace["_is_test_file"]


def probe(repo, source):
    path = repo / "src" / "view.ts"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(source, encoding="utf-8")
    db = repo / ".code-review-graph" / "graph.db"
    db.parent.mkdir(exist_ok=True)
    with GraphStore(db) as store:
        build = full_build(repo, store)
        assert not build["errors"], build
        target = str(path) + "::sum"
        result = query_graph("tests_for", target, repo_root=str(repo))
        assert result["status"] == "ok", result
        classified = store._conn.execute(
            "SELECT kind, name, is_test FROM nodes WHERE name LIKE 'describe%' "
            "ORDER BY name"
        ).fetchall()
        return {
            "classifications": [dict(row) for row in classified],
            "tests_for_sum": [
                {"name": row["name"], "indirect": row["indirect"]}
                for row in result["results"]
            ],
        }


def main():
    assert os.name == "nt", "This A/B targets native Windows paths."
    before_revision = git("rev-parse", "92fdfe0^")
    after_revision = git("rev-parse", "92fdfe0")
    parser_path = "code_review_graph/parser.py"
    assert git("hash-object", parser_path) == git("rev-parse", f"{after_revision}:{parser_path}")
    source = """export function sum(a: number, b: number) { return a+b; }
export function describe(label: string, fn: () => void) { fn(); }
describe("production callback", () => sum(1,2));
"""
    current = parser._is_test_file
    baseline = baseline_detector(before_revision)
    observed = {}
    try:
        with TemporaryDirectory(prefix="crg-review-ts-") as temporary:
            for layout in ("plain", "contest", "tests/app"):
                checkout = Path(temporary) / layout
                parser._is_test_file = baseline
                before = probe(checkout, source)
                parser._is_test_file = current
                after = probe(checkout, source)
                assert before["tests_for_sum"] == []
                assert after["tests_for_sum"] == ([] if layout == "plain" else [
                    {"name": "describe:production callback@L3", "indirect": False}
                ])
                observed[layout + "/src/view.ts"] = {"before": before, "after": after}
    finally:
        parser._is_test_file = current
    print(json.dumps({
        "baseline_detector_revision": before_revision,
        "current_parser_revision": after_revision,
        "platform": sys.platform,
        "python": sys.version.split()[0],
        "cases": observed,
    }, indent=2))


if __name__ == "__main__":
    main()
