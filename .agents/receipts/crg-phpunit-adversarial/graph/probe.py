"""Reproduce three PHPUnit graph review findings using isolated repositories."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest.mock import patch

from code_review_graph import parser
from code_review_graph.graph import GraphStore
from code_review_graph.tools.build import build_or_update_graph


ROOT = Path(__file__).resolve().parents[4]
CLI = ROOT / ".venv/Scripts/code-review-graph.exe"
ENV = dict(os.environ, PYTHONIOENCODING="utf-8", CRG_SERIAL_PARSE="1")


def invoke(root: Path, *args: str | Path) -> str:
    result = subprocess.run(
        [str(arg) for arg in args],
        cwd=root,
        env=ENV,
        capture_output=True,
        encoding="utf-8",
        check=True,
    )
    return result.stdout.strip()


def cli(root: Path, *args: str) -> str:
    return invoke(root, CLI, *args, "--repo", root)


def commit(root: Path, message: str) -> None:
    invoke(root, "git", "add", "src", "tests")
    invoke(
        root, "git", "-c", "user.email=fixture@example.invalid", "-c",
        "user.name=Fixture", "commit", "-qm", message,
    )


def calculator(root: Path, namespace: str) -> None:
    source = root / "src" / namespace / "Calculator.php"
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text(
        "<?php\nnamespace App\\" + namespace
        + ";\nclass Calculator {\npublic function add(): int { return 1; }\n}\n",
        encoding="utf-8",
    )


def fixture(root: Path, method: str, payments_present: bool) -> Path:
    invoke(root, "git", "init", "-q")
    (root / "tests").mkdir()
    calculator(root, "Shipping")
    if payments_present:
        calculator(root, "Payments")
    test = root / "tests/CalculatorTest.php"
    test.write_text(
        r"""<?php
namespace App\Tests;
use App\Payments\Calculator;
use PHPUnit\Framework\TestCase;
class CalculatorTest extends TestCase {
public function METHOD(): void {
    $calc = new Calculator();
    $this->assertSame(1, $calc->add());
}
}
""".replace("METHOD", method),
        encoding="utf-8",
    )
    commit(root, "baseline fixture")
    return test


def result(root: Path, method: str) -> dict:
    with GraphStore(root / ".code-review-graph/graph.db") as store:
        node = store._conn.execute(
            "SELECT kind, is_test, qualified_name FROM nodes WHERE name = ?",
            (method,),
        ).fetchone()
        report = {"kind": node["kind"], "is_test": bool(node["is_test"])}
        for kind, source, target in (
            ("CALLS", "target_qualified", "source_qualified"),
            ("TESTED_BY", "source_qualified", "target_qualified"),
        ):
            rows = store._conn.execute(
                f"SELECT {source}, extra FROM edges WHERE kind = ? AND {target} = ? "
                f"AND {source} LIKE '%Calculator.add'",
                (kind, node["qualified_name"]),
            ).fetchall()
            report[kind] = [
                {
                    "method": row[0].replace(str(root) + os.sep, "").replace(os.sep, "/"),
                    "resolver": json.loads(row[1] or "{}").get("scoped_via"),
                }
                for row in rows
            ]
        for domain in ("Payments", "Shipping"):
            target = str(root / "src" / domain / "Calculator.php") + "::Calculator.add"
            output = json.loads(cli(root, "query", "tests_for", target))
            report[domain] = {
                "status": output["status"],
                "tests": [
                    {key: item.get(key) for key in ("name", "indirect", "inferred_by")}
                    for item in output.get("results", [])
                ],
            }
        status = json.loads(cli(root, "status", "--json"))
        report["build_matches_head"] = status["built_at_commit"] == status["current_sha"]
    return report


def old_test_file(path: str) -> bool:
    # Exact predicate from the parent of 92fdfe0.
    return any(pattern.search(path) for pattern in parser._TEST_FILE_PATTERNS)


def upgrade_and_naming() -> dict:
    method = "testAdd"
    with tempfile.TemporaryDirectory(prefix="crg-phpunit-review-") as temp:
        root = Path(temp)
        source = fixture(root, method, payments_present=True)
        with patch.object(parser, "_is_test_file", old_test_file):
            old = build_or_update_graph(
                repo_root=str(root), full_rebuild=True, postprocess="minimal",
            )
            assert not old["errors"], old
        baseline = result(root, method)
        (root / "src/Unrelated.php").write_text(
            "<?php function unrelated() {}", encoding="utf-8",
        )
        commit(root, "unrelated PHP file")
        update = cli(root, "update", "--skip-flows")
        stale = result(root, method)
        with source.open("a", encoding="utf-8") as stream:
            stream.write("\n// touch the test contents")
        edited_update = cli(root, "update", "--skip-flows")
        edited = result(root, method)
        rebuild = cli(root, "build", "--skip-flows")
        rebuilt = result(root, method)
        assert baseline["kind"] == stale["kind"] == "Function"
        assert not stale["TESTED_BY"] and stale["build_matches_head"]
        assert stale["Payments"]["tests"] == []
        assert edited == rebuilt
        assert rebuilt["kind"] == "Test" and rebuilt["is_test"]
        assert rebuilt["TESTED_BY"] == [
            {"method": "src/Payments/Calculator.php::Calculator.add", "resolver": "import"},
        ]
        assert rebuilt["Payments"]["tests"] == [
            {"name": method, "indirect": False, "inferred_by": None},
        ]
        assert rebuilt["Shipping"]["tests"] == [
            {"name": method, "indirect": False, "inferred_by": "naming_convention"},
        ]
        return {
            "baseline": baseline, "update_cli": update, "stale": stale,
            "edit_cli": edited_update, "edited": edited,
            "rebuild_cli": rebuild, "rebuilt": rebuilt,
        }


def sticky_homonym() -> dict:
    method = "testItAdds"
    with tempfile.TemporaryDirectory(prefix="crg-phpunit-review-") as temp:
        root = Path(temp)
        fixture(root, method, payments_present=False)
        first_build = cli(root, "build", "--skip-flows")
        initial = result(root, method)
        calculator(root, "Payments")
        commit(root, "add actual imported implementation")
        update = cli(root, "update", "--skip-flows")
        incremental = result(root, method)
        rebuild = cli(root, "build", "--skip-flows")
        rebuilt = result(root, method)
        wrong_edge = [
            {"method": "src/Shipping/Calculator.php::Calculator.add", "resolver": "single_match"},
        ]
        assert initial["TESTED_BY"] == incremental["TESTED_BY"] == wrong_edge
        assert initial["CALLS"] == incremental["CALLS"] == wrong_edge
        assert incremental["build_matches_head"] and incremental["Payments"]["tests"] == []
        assert incremental["Shipping"]["tests"] == [
            {"name": method, "indirect": False, "inferred_by": None},
        ]
        assert rebuilt["CALLS"] == rebuilt["TESTED_BY"] == [
            {"method": "src/Payments/Calculator.php::Calculator.add", "resolver": "import"},
        ]
        assert rebuilt["Shipping"]["tests"] == []
        assert rebuilt["Payments"]["tests"] == [
            {"name": method, "indirect": False, "inferred_by": None},
        ]
        return {
            "first_build_cli": first_build, "initial": initial, "update_cli": update,
            "incremental": incremental, "rebuild_cli": rebuild, "rebuilt": rebuilt,
        }


def main() -> None:
    assert os.name == "nt", "This probe requires native Windows paths."
    print(json.dumps({
        "workspace_head": invoke(ROOT, "git", "rev-parse", "HEAD"),
        "python": sys.version.split()[0],
        "upgrade_and_naming": upgrade_and_naming(),
        "sticky_homonym": sticky_homonym(),
    }, indent=2))


if __name__ == "__main__":
    main()
