"""Characterize dbt graph identity through the installed CLI and SQLite."""

import json
import os
import sqlite3
import subprocess
import sysconfig
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory

from code_review_graph.parser import CodeParser

source = b"select * from {{ ref('stg_orders') }}\n"
model_path = Path("models/staging/fct_orders.sql")
nodes, edges = CodeParser().parse_bytes(model_path, source)
model = next(n for n in nodes if n.extra.get("sql_kind") == "dbt_model")
model_edge, = (e for e in edges if e.kind == "CONTAINS")
assert model_edge.source == model.file_path == str(model_path)
assert model_edge.target == f"{model.file_path}::{model.name}"

with TemporaryDirectory(prefix="crg-dbt-") as scratch:
    root = Path(scratch) / "repo"
    sql_file = root / model_path
    sql_file.parent.mkdir(parents=True)
    sql_file.write_bytes(source)
    (root / "dbt_project.yml").write_text("name: analytics\nconfig-version: 2\n", encoding="utf-8")
    env = dict(os.environ, CRG_HOME=str(Path(scratch) / "state"))
    env.pop("CRG_REPO_ROOT", None)
    env.pop("CRG_DATA_DIR", None)
    executable = Path(sysconfig.get_path("scripts")) / (
        "code-review-graph.exe" if os.name == "nt" else "code-review-graph"
    )
    result = subprocess.run(
        [str(executable), "build", "--repo", str(root)],
        capture_output=True, text=True, encoding="utf-8", env=env, timeout=90, check=True,
    )
    db = root / ".code-review-graph" / "graph.db"
    with closing(sqlite3.connect(db.as_uri() + "?mode=ro", uri=True)) as conn:
        persisted = conn.execute(
            """SELECT e.source_qualified, e.target_qualified, s.kind, t.kind, t.name
               FROM edges e
               LEFT JOIN nodes s ON s.qualified_name=e.source_qualified
               LEFT JOIN nodes t ON t.qualified_name=e.target_qualified
               WHERE e.kind='CONTAINS' AND e.source_qualified=?""",
            (str(sql_file),),
        ).fetchall()
    assert persisted == [(str(sql_file), f"{sql_file}::fct_orders", "File", "Class", "fct_orders")]
    print(json.dumps({
        "platform": os.name,
        "cli_build_exit": result.returncode,
        "parser": {
            "source": model_edge.source,
            "target": model_edge.target,
            "matches_old_literal": model_edge.target == "models/staging/fct_orders.sql::fct_orders",
        },
        "sqlite": {
            "endpoint_kinds": [persisted[0][2], persisted[0][3]],
            "model": persisted[0][4],
            "exact_identity_join_count": len(persisted),
        },
    }, indent=2))
