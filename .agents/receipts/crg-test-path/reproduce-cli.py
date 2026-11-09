"""Compare the Windows CLI and its SQLite graph on isolated Git repos."""

import hashlib
import io
import json
import os
import sqlite3
import subprocess
import tarfile
import tempfile
from contextlib import closing
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EXE = ROOT / ".venv/Scripts/code-review-graph.exe"
PYTHON = ROOT / ".venv/Scripts/python.exe"
BASELINE = "b28fcd4583db157ff1d9f907efdf316f841c039d"
PHP = """<?php
class Example {
    public function add($a, $b) { return $a + $b; }
    public function testProductionHelper() { $x = new Example(); return $x->add(1, 2); }
}
"""
TS = """function add(a: number, b: number) { return a + b; }
describe("behavior", () => { add(1, 2); });
"""
CASES = [
    ("php-suffix", "checkout", "contest/Example.php", True, False),
    ("php-ancestor", "tests/checkout", "src/Example.php", True, False),
    ("php-real-tests", "checkout", "tests/Example.php", True, True),
    ("php-neutral", "checkout", "src/Example.php", False, False),
    ("ts-suffix", "checkout", "contest/Example.ts", True, False),
    ("ts-ancestor", "tests/checkout", "src/Example.ts", True, False),
    ("ts-root-jest", "checkout", "__tests__/Example.ts", True, True),
]


def run(*args, cwd=ROOT, env=None):
    process = subprocess.run(
        args, cwd=cwd, env=env, encoding="utf-8", errors="replace", capture_output=True,
    )
    if process.returncode != 0:
        raise RuntimeError(f"{args[0]} exited {process.returncode}: {process.stderr}")
    return process.stdout


def probe(project, relative, expected, module_root, env):
    path = project / relative
    path.parent.mkdir(parents=True)
    php = path.suffix == ".php"
    source = PHP if php else TS
    path.write_text(source, encoding="utf-8", newline="\n")
    run("git", "init", "-q", cwd=project)
    run(EXE, "build", "--repo", project, cwd=module_root, env=env)
    target = f"{path}::{'Example.add' if php else 'add'}"
    test = f"{path}::{'Example.testProductionHelper' if php else 'describe:behavior@L2'}"
    payload = json.loads(run(
        EXE, "query", "tests_for", target, "--repo", project, cwd=module_root, env=env,
    ))
    with closing(sqlite3.connect(project / ".code-review-graph/graph.db")) as db:
        nodes = db.execute(
            "SELECT kind,is_test,file_path FROM nodes WHERE qualified_name=?", (test,),
        ).fetchall()
        edges = db.execute(
            "SELECT target_qualified FROM edges WHERE kind='TESTED_BY' AND source_qualified=?",
            (target,),
        ).fetchall()
    assert nodes == (
        [("Test", 1, str(path))] if expected else [("Function", 0, str(path))] if php else []
    ), (relative, nodes)
    assert edges == ([(test,)] if expected else []), (relative, edges)
    results = [{"name": row["name"], "indirect": row["indirect"]} for row in payload["results"]]
    assert len(results) == int(expected), (relative, results)
    if expected:
        assert results[0]["indirect"] is False, (relative, results)
    return {
        "relative_path": relative,
        "git_checkout": project.name,
        "native_identity_verified": True,
        "nodes": [{"kind": kind, "is_test": bool(flag)} for kind, flag, _ in nodes],
        "tested_by": [edge[0].rsplit("::", 1)[-1] for edge in edges],
        "query_results": results,
        "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
    }


def main():
    with tempfile.TemporaryDirectory(prefix="crg-test-path-") as temporary:
        work = Path(temporary)
        snapshot = work / "baseline"
        snapshot.mkdir()
        code = subprocess.check_output(["git", "archive", BASELINE, "code_review_graph"], cwd=ROOT)
        with tarfile.open(fileobj=io.BytesIO(code)) as archive:
            archive.extractall(snapshot, filter="data")
        rows = {}
        for label, module_root, expectation in (("baseline", snapshot, 3), ("fixed", ROOT, 4)):
            env = os.environ | {
                "PYTHONPATH": str(module_root),
                "PYTHONUTF8": "1",
                "CRG_HOME": str(work / label / "crg-home"),
            }
            module = run(
                PYTHON, "-c", "import code_review_graph.parser as p; print(p.__file__)",
                cwd=module_root, env=env,
            )
            assert Path(module.strip()).is_relative_to(module_root), module
            rows[label] = {
                case[0]: probe(
                    work / label / case[0] / case[1], case[2], case[expectation], module_root, env,
                )
                for case in CASES
            }
        result = {
            "exit_code": 0,
            "baseline": BASELINE,
            "parser_sha256": hashlib.sha256((ROOT / "code_review_graph/parser.py").read_bytes()).hexdigest(),
            "executable": EXE.name,
            "fixtures": {"php": PHP, "ts": TS},
            "results": rows,
        }
        Path(__file__).with_name("cli.json").write_text(
            json.dumps(result, indent=2) + "\n", encoding="utf-8",
        )
        print(f"{len(CASES)} casos x 2 revisões: CLI e SQLite concordam")


if __name__ == "__main__":
    main()
