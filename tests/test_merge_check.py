from __future__ import annotations

import json
import os
import subprocess
import sys

import pytest


def cli():
    launcher = os.environ.get("CRG_TEST_MERGE_CHECK_LAUNCHER")
    return [launcher] if launcher else [sys.executable, "-m", "code_review_graph"]


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()


def commit(repo, message):
    git(repo, "add", ".")
    git(repo, "commit", "-qm", message)
    return git(repo, "rev-parse", "HEAD")


@pytest.fixture
def history(tmp_path):
    repo = tmp_path / "project"
    repo.mkdir()
    git(repo, "init", "-q")
    git(repo, "config", "user.name", "Test")
    git(repo, "config", "user.email", "test@example.invalid")
    git(repo, "config", "core.hooksPath", os.devnull)
    (repo / "policy.py").write_text("def admits(x):\n    return x <= 5\n", encoding="utf-8")
    (repo / "sample.py").write_text("def amount():\n    return 4\n", encoding="utf-8")
    (repo / "other.py").write_text("def label():\n    return 'old'\n", encoding="utf-8")
    (repo / "tests").mkdir()
    (repo / "tests/test_boundary.py").write_text(
        "import sys\nfrom policy import admits\nfrom sample import amount\n\n"
        "def test_boundary():\n    assert admits(amount())\n\n"
        "if __name__ == '__main__':\n    try:\n        test_boundary()\n"
        "    except AssertionError:\n"
        "        print('boundary assertion failed')\n        sys.exit(17)\n",
        encoding="utf-8",
    )
    base = commit(repo, "base")
    (repo / "policy.py").write_text("def admits(x):\n    return x < 5\n", encoding="utf-8")
    ours = commit(repo, "strict limit")
    git(repo, "checkout", "-q", "--detach", base)
    (repo / "sample.py").write_text("def amount():\n    return 5\n", encoding="utf-8")
    semantic = commit(repo, "use boundary value")
    git(repo, "checkout", "-q", "--detach", base)
    (repo / "policy.py").write_text("def admits(x):\n    return x <= 7\n", encoding="utf-8")
    textual = commit(repo, "looser limit")
    git(repo, "checkout", "-q", "--detach", base)
    (repo / "other.py").write_text("def label():\n    return 'new'\n", encoding="utf-8")
    passing = commit(repo, "change separate label")
    git(repo, "checkout", "-q", "--detach", base)
    (repo / "sample.py").write_text("def amount():\n    return 6\n", encoding="utf-8")
    failing = commit(repo, "break before merge")
    (repo / "untracked.txt").write_text("preserve", encoding="utf-8")
    (repo / "other.py").write_text("staged delta", encoding="utf-8")
    git(repo, "add", "other.py")
    (repo / "other.py").write_text("unstaged delta", encoding="utf-8")
    return repo, base, ours, {"semantic": semantic, "textual": textual,
                             "passing": passing, "failing": failing}


def invoke(repo, base, ours, theirs, command, env=None):
    return subprocess.run(
        [*cli(), "merge-check", "--repo", str(repo),
         "--base", base, "--ours", ours, "--theirs", theirs, "--test-failure-exit", "17",
         "--", *command],
        capture_output=True, env=env,
    )


SUITE = [sys.executable, "-B", "-c",
         "import runpy; runpy.run_path('tests/test_boundary.py',run_name='__main__')"]


@pytest.mark.parametrize(("case", "expected", "code"), [
    ("textual", "text_conflict", 1),
    ("semantic", "regression", 1),
    ("passing", "passed", 0),
    ("failing", "execution_error", 2),
])
def test_merge_check(history, case, expected, code, tmp_path):
    repo, base, ours, branches = history
    state = [git(repo, *args) for args in (
        ("status", "--porcelain"), ("diff", "--binary"), ("diff", "--cached", "--binary"),
        ("for-each-ref",), ("rev-parse", "HEAD"), ("count-objects",),
    )]
    usual_index = tmp_path / "usual-index"
    usual_index.mkdir()
    marker = usual_index / "graph.db"
    marker.write_bytes(b"unrelated graph")
    env = dict(os.environ, CRG_DATA_DIR=str(usual_index), GIT_INDEX_FILE=str(repo / ".git/index"))
    result = invoke(repo, base, ours, branches[case], SUITE, env)
    assert result.returncode == code, result.stderr.decode(errors="replace")
    data = json.loads(result.stdout)
    assert data["outcome"] == expected
    assert data["commits"] == {"base": base, "ours": ours, "theirs": branches[case]}
    if case == "textual":
        assert data["merge"]["exit_code"] == 1
        assert "policy.py" in data["merge"]["messages"]
        assert data["suite"]["runs"] == {}
    if case == "semantic":
        assert data["merge"]["exit_code"] == 0
        assert data["graph"]["test_gaps"] == []
        assert any(item["name"] == "test_boundary" for item in data["graph"]["test_candidates"])
        runs = data["suite"]["runs"]
        assert {key: row["exit_code"] for key, row in runs.items()} == {
            "base": 0, "ours": 0, "theirs": 0, "merged": 17,
        }
        assert "boundary assertion failed" in runs["merged"]["stdout"]
    if case == "passing":
        assert data["graph"]["coverage"] == "incomplete"
        assert {row["exit_code"] for row in data["suite"]["runs"].values()} == {0}
    if case == "failing":
        assert data["suite"]["runs"]["theirs"]["exit_code"] == 17
        assert "merged" not in data["suite"]["runs"]
    assert marker.read_bytes() == b"unrelated graph"
    assert state == [git(repo, *args) for args in (
        ("status", "--porcelain"), ("diff", "--binary"), ("diff", "--cached", "--binary"),
        ("for-each-ref",), ("rev-parse", "HEAD"), ("count-objects",),
    )]


def test_invalid_ref_and_spawn_failure(history):
    repo, base, ours, branches = history
    for test_base, command in [
        ("wrong-base", SUITE),
        (branches["textual"], SUITE),
        (base, [str(repo / "missing-command")]),
        (base, []),
    ]:
        result = invoke(repo, test_base, ours, branches["passing"], command)
        assert result.returncode == 2, result.stderr.decode(errors="replace")
        assert json.loads(result.stdout)["outcome"] == "execution_error"


def test_repeat_and_isolate_suite_checkouts(history, tmp_path):
    repo, base, ours, branches = history
    command = [
        sys.executable, "-B", "-c",
        "from pathlib import Path; f=Path('generated'); assert not f.exists(); f.touch()",
    ]
    temp_dir = tmp_path / "scratch"
    temp_dir.mkdir()
    env = dict(os.environ, TMP=str(temp_dir), TEMP=str(temp_dir), TMPDIR=str(temp_dir))
    for _ in range(2):
        result = invoke(repo, base, ours, branches["passing"], command, env)
        assert result.returncode == 0, result.stdout.decode(errors="replace")
        assert len(json.loads(result.stdout)["suite"]["runs"]) == 4
        assert list(temp_dir.iterdir()) == []
    assert not (repo / "generated").exists()


def test_detect_brief_legacy_encoding(history, tmp_path):
    repo, base, ours, _ = history
    git(repo, "checkout", "--force", "--detach", ours)
    env = dict(
        os.environ, CRG_HOME=str(tmp_path / "registry"), CRG_DATA_DIR=str(tmp_path / "index"),
        PYTHONIOENCODING="cp1252",
    )
    command = cli()
    subprocess.run(
        [*command, "build", "--repo", str(repo)], env=env, check=True, capture_output=True,
    )
    result = subprocess.run(
        [*command, "detect-changes", "--repo", str(repo), "--base", base, "--brief"],
        env=env, capture_output=True,
    )
    assert result.returncode == 0, result.stderr.decode(errors="replace")
    assert "Token Savings" in result.stdout.decode("utf-8")
