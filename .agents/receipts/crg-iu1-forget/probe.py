"""Exercise the installed CRG executable against a disposable Git/SQLite index."""

import argparse
import json
import os
import sqlite3
import subprocess
import tempfile
from contextlib import closing
from pathlib import Path


FILES = ["main.py", "pkg/auth.py", "pkg/views.py", "pkg_extra/keep.py"]


def run(executable: Path, expected: str) -> dict:
    with tempfile.TemporaryDirectory(prefix="crg-forget-") as scratch:
        repo = Path(scratch) / "repo"
        repo.mkdir()
        data = Path(scratch) / "data"
        paths = FILES.copy()
        if os.name != "nt":
            paths.append("PKG/other.py")
        for name in paths:
            file = repo / name
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text(f"def {file.stem}():\n    return 1\n", encoding="utf-8")
        subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
        subprocess.run(["git", "add", "."], cwd=repo, check=True)
        same_directory = (repo / "pkg").samefile(repo / "PKG")
        assert same_directory == (os.name == "nt"), same_directory

        def cli(action, *args):
            return subprocess.run(
                [str(executable), action, "--repo", str(repo), "--data-dir", str(data), *args],
                cwd=repo,
                check=True,
                capture_output=True,
                encoding="utf-8",
                env={**os.environ, "PYTHONIOENCODING": "utf-8"},
            ).stdout.strip()

        def indexed_files():
            with closing(sqlite3.connect((data / "graph.db").as_uri() + "?mode=ro", uri=True)) as conn:
                return sorted(
                    Path(row[0]).relative_to(repo).as_posix()
                    for row in conn.execute("SELECT file_path FROM nodes WHERE kind='File'")
                )

        build = cli("build")
        before = indexed_files()
        assert before == sorted(paths), before
        dry_run = cli("forget", "--dry-run", "PKG")
        assert indexed_files() == before
        preview = sorted(
            line.strip().replace("\\", "/")
            for line in dry_run.splitlines()
            if line.startswith("  ")
        )
        removal = cli("forget", "PKG")
        after = indexed_files()
        targets = ["pkg/auth.py", "pkg/views.py"] if same_directory else ["PKG/other.py"]
        if expected == "red":
            assert same_directory and preview == [] and after == before, (preview, after)
            assert "No parsed files matched" in removal, removal
        else:
            assert preview == targets, preview
            assert after == sorted(set(before) - set(targets)), after
        assert all((repo / name).is_file() for name in paths)
        return {
            "mode": expected,
            "platform": os.name,
            "build": build,
            "same_directory": same_directory,
            "before": before,
            "dry_run": dry_run,
            "preview": preview,
            "removal": removal,
            "after": after,
            "all_sources_exist": True,
        }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("executable", type=Path)
    parser.add_argument("expected", choices=["red", "green"])
    args = parser.parse_args()
    result = run(args.executable.resolve(strict=True), args.expected)
    print(json.dumps(result, indent=2))
