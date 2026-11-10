"""Check the exact HCL fixture before and after CLI persistence."""

import ast
import json
import os
import sqlite3
import subprocess
import sysconfig
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory

from code_review_graph.parser import CodeParser

module = ast.parse(Path("tests/test_hcl_parser.py").read_text(encoding="utf-8"))
test = next(
    node for node in module.body
    if isinstance(node, ast.FunctionDef)
    and node.name == "test_for_expression_references_are_emitted_for_local_binding"
)
source = next(
    ast.literal_eval(node.value) for node in test.body
    if isinstance(node, ast.Assign)
    and isinstance(node.targets[0], ast.Name)
    and node.targets[0].id == "source"
)
relative = Path("infra/locals.tf")
names = {"var.items", "var.enabled"}
_, edges = CodeParser().parse_bytes(relative, source)
raw = [(edge.source, edge.target) for edge in edges if edge.kind == "REFERENCES"]
assert len(raw) == 2
assert set(raw) == {(f"{relative}::local.selected", f"{relative}::{name}") for name in names}
old_filter_matches = sum(s == "infra/locals.tf::local.selected" for s, _ in raw)
assert old_filter_matches == (0 if os.name == "nt" else 2)

with TemporaryDirectory(prefix="crg-hcl-") as scratch:
    root = Path(scratch) / "repo"
    path = root / relative
    path.parent.mkdir(parents=True)
    path.write_bytes(source)
    env = dict(os.environ, CRG_HOME=str(Path(scratch) / "state"))
    env.pop("CRG_DATA_DIR", None)
    env.pop("CRG_REPO_ROOT", None)
    cli = Path(sysconfig.get_path("scripts")) / (
        "code-review-graph.exe" if os.name == "nt" else "code-review-graph"
    )
    result = subprocess.run(
        [str(cli), "build", "--repo", str(root)], env=env,
        capture_output=True, encoding="utf-8", timeout=60,
    )
    assert result.returncode == 0, result.stderr
    db = root / ".code-review-graph" / "graph.db"
    with closing(sqlite3.connect(db.as_uri() + "?mode=ro", uri=True)) as conn:
        rows = conn.execute(
            """SELECT e.source_qualified, e.target_qualified, s.name, t.name
               FROM edges e
               LEFT JOIN nodes s ON s.qualified_name = e.source_qualified
               LEFT JOIN nodes t ON t.qualified_name = e.target_qualified
               WHERE e.kind = 'REFERENCES' AND e.source_qualified = ?
               ORDER BY e.target_qualified""",
            (f"{path}::local.selected",),
        ).fetchall()
    assert len(rows) == 2
    assert set(rows) == {
        (f"{path}::local.selected", f"{path}::{name}", "local.selected", name)
        for name in names
    }
    print(json.dumps({
        "platform": os.name,
        "raw_references": raw,
        "old_source_filter_matches": old_filter_matches,
        "cli_build_exit": result.returncode,
        "sqlite_endpoint_symbols": [row[2:] for row in rows],
    }, indent=2))
