"""Prove the difference between Git freshness and parser freshness on Windows."""

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
OLD = "c3682acb70bfcd15c024a27f60833ac54453db30"
CURRENT = "5ec476253c5052fe3227ea1750f51657190cc5dd"
OUT = Path(__file__).resolve().parent
TARGET_FILE = Path("src/Calculator.php")
TEST_FILE = Path("tests/CalculatorTest.php")
UNRELATED = Path("src/Unrelated.php")
TEST_METHOD = "CalculatorTest.testAdd"
TARGET_METHOD = "Calculator.add"


def run(*args, cwd, env):
    result = subprocess.run(
        [str(arg) for arg in args],
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode:
        raise RuntimeError(f"{args[0]} exited {result.returncode}: {result.stderr}")
    return result.stdout.strip()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name, payload):
    (OUT / f"{name}.json").write_text(
        json.dumps({"exit_code": 0, **payload}, indent=2) + "\n",
        encoding="utf-8",
    )


def snapshot(revision, work, env):
    directory = work / revision[:7]
    directory.mkdir()
    archive = subprocess.check_output(["git", "archive", revision, "code_review_graph"], cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(directory, filter="data")
    isolated_env = env | {"PYTHONPATH": str(directory)}
    source = Path(
        run(
            PYTHON,
            "-c",
            "import code_review_graph.parser as p; print(p.__file__)",
            cwd=directory,
            env=isolated_env,
        )
    )
    assert source == directory / "code_review_graph/parser.py", source
    return directory, isolated_env, {"git": revision, "parser_sha256": digest(source)}


def sqlite_state(db_path, repo):
    test_path = repo / TEST_FILE
    target_path = repo / TARGET_FILE
    qualified_test = f"{test_path}::{TEST_METHOD}"
    qualified_target = f"{target_path}::{TARGET_METHOD}"
    with closing(sqlite3.connect(db_path.as_uri() + "?mode=ro", uri=True)) as db:
        db.row_factory = sqlite3.Row
        integrity = [row[0] for row in db.execute("PRAGMA integrity_check")]
        assert integrity == ["ok"], integrity
        sha = db.execute("SELECT value FROM metadata WHERE key='git_head_sha'").fetchone()[0]
        rows = db.execute(
            "SELECT kind,is_test,file_path,qualified_name,line_start,line_end FROM nodes "
            "WHERE qualified_name IN (?, ?, ?) ORDER BY qualified_name",
            (str(test_path), qualified_target, qualified_test),
        ).fetchall()
        edges = db.execute(
            "SELECT source_qualified,target_qualified FROM edges WHERE kind='TESTED_BY' "
            "AND source_qualified=? AND target_qualified=?",
            (qualified_target, qualified_test),
        ).fetchall()
    assert {row["qualified_name"] for row in rows} == {
        str(test_path),
        qualified_test,
        qualified_target,
    }
    nodes = [
        {
            **dict(row),
            "file_path": Path(row["file_path"]).relative_to(repo).as_posix(),
            "qualified_name": row["qualified_name"]
            .removeprefix(str(repo) + os.sep)
            .replace(os.sep, "/"),
            "is_test": bool(row["is_test"]),
        }
        for row in rows
    ]
    tested_by = [
        [value.removeprefix(str(repo) + os.sep).replace(os.sep, "/") for value in edge]
        for edge in edges
    ]
    return {
        "integrity_check": integrity[0],
        "git_head_sha": sha,
        "nodes": nodes,
        "TESTED_BY": tested_by,
    }


def main():
    with tempfile.TemporaryDirectory(prefix="crg-k4q-") as temp:
        work = Path(temp).resolve()
        repo = work / "fixture"
        repo.mkdir()
        env = os.environ | {
            "CRG_HOME": str(work / "crg-home"),
            "PYTHONUTF8": "1",
            "CRG_SERIAL_PARSE": "1",
        }
        old = snapshot(OLD, work, env)
        current = snapshot(CURRENT, work, env)
        assert old[2]["parser_sha256"] != current[2]["parser_sha256"]
        db_path = repo / ".code-review-graph/graph.db"

        def git(*args):
            return run("git", *args, cwd=repo, env=env)

        def cli(version, *args):
            return run(EXE, *args, "--repo", repo, cwd=version[0], env=version[1])

        def observe(version):
            status = json.loads(cli(version, "status", "--json"))
            query = json.loads(
                cli(version, "query", "tests_for", f"{repo / TARGET_FILE}::{TARGET_METHOD}")
            )
            assert query["status"] == "ok", query
            sql = sqlite_state(db_path, repo)
            head = git("rev-parse", "HEAD")
            assert status["built_at_commit"] == status["current_sha"] == head == sql["git_head_sha"]
            results = [
                {k: row.get(k) for k in ("name", "indirect", "inferred_by")}
                for row in query["results"]
            ]
            return {"git_head": head, "status": status, "sqlite": sql, "tests_for": results}

        def assert_classification(state, expected):
            method = next(
                node
                for node in state["sqlite"]["nodes"]
                if node["qualified_name"].endswith(f"::{TEST_METHOD}")
            )
            assert (method["kind"], method["is_test"]) == (
                ("Test", True) if expected else ("Function", False)
            )
            edge = [
                f"{TARGET_FILE.as_posix()}::{TARGET_METHOD}",
                f"{TEST_FILE.as_posix()}::{TEST_METHOD}",
            ]
            assert state["sqlite"]["TESTED_BY"] == ([edge] if expected else []), state
            direct = [{"name": "testAdd", "indirect": False, "inferred_by": None}]
            assert state["tests_for"] == (direct if expected else []), state

        git("init", "-q")
        (repo / "src").mkdir()
        (repo / "tests").mkdir()
        (repo / TARGET_FILE).write_text(
            "<?php namespace App; class Calculator { public function add() { return 1; } }\n",
            encoding="utf-8",
        )
        (repo / TEST_FILE).write_text(
            r"""<?php
namespace App\Tests;
use App\Calculator;
use PHPUnit\Framework\TestCase;
class CalculatorTest extends TestCase {
    public function testAdd(): void {
        $calc = new Calculator();
        $this->assertSame(1, $calc->add());
    }
}
""",
            encoding="utf-8",
        )
        (repo / UNRELATED).write_text(
            "<?php function unrelated() { return 1; }\n", encoding="utf-8"
        )
        git("add", "--", "src", "tests")
        git(
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "baseline",
        )
        source_hashes = {path.as_posix(): digest(repo / path) for path in (TARGET_FILE, TEST_FILE)}

        build_old = cli(old, "build", "--skip-flows")
        baseline = observe(old)
        assert_classification(baseline, False)
        save(
            "baseline",
            {
                "module": old[2],
                "executable": EXE.name,
                "build": build_old,
                "php_source_sha256": source_hashes,
                **baseline,
            },
        )

        (repo / UNRELATED).write_text(
            "<?php function unrelated() { return 2; }\n", encoding="utf-8"
        )
        git("add", "--", UNRELATED)
        git(
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "unrelated",
        )
        changed = git("diff", "--name-only", baseline["git_head"], "HEAD").splitlines()
        assert changed == [UNRELATED.as_posix()], changed
        update_cli = cli(current, "update", "--skip-flows")
        assert update_cli.startswith("Incremental: 1 files updated,"), update_cli
        updated = observe(current)
        assert_classification(updated, False)
        assert updated["git_head"] != baseline["git_head"]
        assert updated["sqlite"]["nodes"] == baseline["sqlite"]["nodes"]
        assert all(
            digest(repo / path) == source_hashes[path.as_posix()]
            for path in (TARGET_FILE, TEST_FILE)
        )
        save(
            "update",
            {
                "module": current[2],
                "update": update_cli,
                "git_changed_files": changed,
                "php_source_sha256": source_hashes,
                **updated,
            },
        )

        backup_dir = Path(tempfile.mkdtemp(prefix="backup-", dir=OUT))
        backup = backup_dir / "index-before-rebuild.sqlite3"
        with closing(sqlite3.connect(db_path.as_uri() + "?mode=ro", uri=True)) as source:
            with closing(sqlite3.connect(backup)) as destination:
                source.backup(destination)
        backup_state = sqlite_state(backup, repo)
        assert backup_state == updated["sqlite"]
        backup_hash = digest(backup)
        save(
            "backup",
            {
                "path_local": backup.relative_to(OUT).as_posix(),
                "sha256": backup_hash,
                "size_bytes": backup.stat().st_size,
                "sqlite": backup_state,
            },
        )

        rebuild_cli = cli(current, "build", "--skip-flows")
        rebuilt = observe(current)
        assert_classification(rebuilt, True)
        assert rebuilt["git_head"] == updated["git_head"]
        assert all(
            digest(repo / path) == source_hashes[path.as_posix()]
            for path in (TARGET_FILE, TEST_FILE)
        )
        assert sqlite_state(backup, repo) == backup_state and digest(backup) == backup_hash
        save(
            "rebuild",
            {
                "module": current[2],
                "build": rebuild_cli,
                "php_source_sha256": source_hashes,
                "backup_sha256_after_rebuild": backup_hash,
                **rebuilt,
            },
        )
    print("4/4: baseline, update, backup read-only e rebuild verificados")


if __name__ == "__main__":
    main()
