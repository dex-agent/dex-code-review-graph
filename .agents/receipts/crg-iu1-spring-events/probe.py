"""Verify Spring event endpoints in a disposable index built by the CLI."""

import json
import os
import runpy
import sqlite3
import subprocess
import sysconfig
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory

fixture = runpy.run_path("tests/test_spring_events.py")["_write_event_package"]
packages = ("alpha", "beta")

with TemporaryDirectory(prefix="crg-spring-") as scratch:
    root = Path(scratch) / "repo"
    paths = {package: fixture(root, package)[1:] for package in packages}
    env = dict(os.environ, CRG_HOME=str(Path(scratch) / "state"))
    env.pop("CRG_DATA_DIR", None)
    env.pop("CRG_REPO_ROOT", None)
    executable = "code-review-graph.exe" if os.name == "nt" else "code-review-graph"
    cli = Path(sysconfig.get_path("scripts")) / executable
    subprocess.run(
        [str(cli), "build", "--repo", str(root)],
        env=env, check=True, capture_output=True, timeout=60,
    )
    db = root / ".code-review-graph" / "graph.db"
    with closing(sqlite3.connect(db.as_uri() + "?mode=ro", uri=True)) as conn:
        conn.row_factory = sqlite3.Row
        rows = [
            dict(row)
            for row in conn.execute(
                """SELECT e.source_qualified, e.target_qualified,
                          s.id AS source_id, t.id AS target_id,
                          s.kind AS source_kind, t.kind AS target_kind,
                          json_extract(e.extra, '$.event_type') AS event_type
                   FROM edges e
                   LEFT JOIN nodes s ON s.qualified_name = e.source_qualified
                   LEFT JOIN nodes t ON t.qualified_name = e.target_qualified
                   WHERE e.kind = 'CALLS'
                     AND json_extract(e.extra, '$.spring_event_resolved') = 1
                   ORDER BY event_type"""
            )
        ]
    expected = {
        (f"{publisher}::Publisher.publish", f"{listener}::Listener.on", f"{package}.SharedEvent")
        for package, (publisher, listener) in paths.items()
    }
    actual = {(row["source_qualified"], row["target_qualified"], row["event_type"]) for row in rows}
    assert len(rows) == 2 and actual == expected
    assert all(
        row["source_id"] is not None and row["target_id"] is not None
        and row["source_kind"] == row["target_kind"] == "Function"
        for row in rows
    )
    old_filter_matches = sum(
        any(
            f"/{package}/" in row["source_qualified"]
            and f"/{package}/" in row["target_qualified"]
            for package in packages
        )
        for row in rows
    )
    assert old_filter_matches == (0 if os.name == "nt" else 2)
    print(json.dumps({
        "platform": os.name, "cli_build_exit": 0, "old_filter_matches": old_filter_matches,
        "expected_pairs": 2, "cross_links": 0, "orphan_endpoints": 0, "rows": rows,
    }, indent=2))
