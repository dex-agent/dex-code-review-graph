"""Exercise the CRG CLI across two PHP name-resolution boundaries."""

import argparse
import hashlib
import importlib.util
import json
import os
import tempfile
from contextlib import closing
from pathlib import Path
from sqlite3 import connect

ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "crg_fixture",
    ROOT.parent / "crg-phpunit-adversarial/graph/probe.py",
)
fixture = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fixture)
METHOD = "testItAdds"


def read_graph(repo):
    test = f"{repo / 'tests/CalculatorTest.php'}::CalculatorTest.{METHOD}"
    with closing(
        connect((repo / ".code-review-graph/graph.db").as_uri() + "?mode=ro", uri=True)
    ) as db:
        rows = db.execute(
            "SELECT kind,source_qualified,target_qualified,line FROM edges "
            "WHERE (kind='CALLS' AND source_qualified=?) "
            "OR (kind='TESTED_BY' AND target_qualified=?) ORDER BY kind,line,2,3",
            (test, test),
        ).fetchall()
    return [
        {
            "kind": kind,
            "destination": (target if kind == "CALLS" else source)
            .removeprefix(str(repo) + os.sep)
            .replace(os.sep, "/"),
            "line": line,
        }
        for kind, source, target, line in rows
    ]


def observe(repo):
    status = json.loads(fixture.cli(repo, "status", "--json"))
    head = fixture.invoke(repo, "git", "rev-parse", "HEAD")
    assert status["built_at_commit"] == status["current_sha"] == head
    data = fixture.result(repo, METHOD)
    assert data["kind"] == "Test" and data["is_test"]
    return {
        "git_head": head,
        "edges": read_graph(repo),
        "Shipping": data["Shipping"],
        "Payments": data["Payments"],
    }


def run_scenario(repo, composer):
    test = fixture.fixture(repo, METHOD, payments_present=False)
    if composer:
        source = test.read_text(encoding="utf-8").replace(
            "use PHPUnit",
            r"use App\Shipping\Calculator as ShippingCalculator;" + "\nuse PHPUnit",
        )
        test.write_text(source, encoding="utf-8")
        (repo / "composer.json").write_text(
            json.dumps({"autoload": {"psr-4": {"App\\": "src/"}}}),
            encoding="utf-8",
        )
        fixture.invoke(repo, "git", "add", "composer.json")
        fixture.commit(repo, "add separate Composer import")
    initial_build = fixture.cli(repo, "build", "--skip-flows")
    missing = observe(repo)
    test_sha = hashlib.sha256(test.read_bytes()).hexdigest()
    fixture.calculator(repo, "Payments")
    fixture.commit(repo, "add the imported class")
    changed = fixture.invoke(repo, "git", "diff", "--name-only", missing["git_head"], "HEAD")
    assert changed == "src/Payments/Calculator.php", changed
    update = fixture.cli(repo, "update", "--skip-flows")
    assert update.startswith("Incremental: "), update
    added = observe(repo)
    repeated = fixture.cli(repo, "update", "--skip-flows")
    repeated_state = observe(repo)
    rebuild = fixture.cli(repo, "build", "--skip-flows")
    rebuilt = observe(repo)
    assert added["git_head"] == repeated_state["git_head"] == rebuilt["git_head"]
    assert hashlib.sha256(test.read_bytes()).hexdigest() == test_sha
    return {
        "changed": changed,
        "test_sha256": test_sha,
        "build": initial_build,
        "update": update,
        "repeat_update": repeated,
        "rebuild": rebuild,
        "missing": missing,
        "added": added,
        "repeated": repeated_state,
        "rebuilt": rebuilt,
    }


def verify(scenario):
    findings = []
    expected_query = [{"name": METHOD, "indirect": False, "inferred_by": None}]
    for stage in ("missing", "added", "repeated", "rebuilt"):
        state = scenario[stage]
        wrong = [edge for edge in state["edges"] if edge["destination"].startswith("src/Shipping/")]
        if wrong or state["Shipping"]["tests"]:
            findings.append(f"{stage}: Shipping received CALLS/TESTED_BY or a query result")
        if stage == "missing":
            continue
        cls = "src/Payments/Calculator.php::Calculator"
        right = [
            (edge["kind"], edge["destination"])
            for edge in state["edges"]
            if edge["destination"] in (cls, f"{cls}.add")
        ]
        expected = [
            (kind, target) for kind in ("CALLS", "TESTED_BY") for target in (cls, f"{cls}.add")
        ]
        if right != expected or state["Payments"]["tests"] != expected_query:
            findings.append(
                f"{stage}: missing constructor or direct method association for Payments"
            )
    if scenario["added"] != scenario["repeated"] or scenario["added"] != scenario["rebuilt"]:
        findings.append("updated, repeated and rebuilt snapshots differ")
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, required=True)
    opts = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="crg-x6m-") as temp:
        work = Path(temp)
        fixture.ENV["CRG_HOME"] = str(work / "crg-home")
        rows = {}
        for label, composer in (("scoped", False), ("composer_alias", True)):
            repo = work / label
            repo.mkdir()
            data = run_scenario(repo, composer)
            rows[label] = {"findings": verify(data), **data}
    exit_code = int(any(row["findings"] for row in rows.values()))
    opts.receipt.write_text(
        json.dumps(
            {
                "exit_code": exit_code,
                "workspace_revision": fixture.invoke(ROOT, "git", "rev-parse", "HEAD"),
                "module_sha256": {
                    name: hashlib.sha256(
                        (fixture.ROOT / "code_review_graph" / name).read_bytes(),
                    ).hexdigest()
                    for name in ("parser.py", "scoped_resolver.py")
                },
                "executable": fixture.CLI.name,
                "scenarios": rows,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    for label, row in rows.items():
        print(label, row["findings"] or "ok")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
