"""release_version.py — the one owner of "the version is written down the same everywhere".

A release moves the version in a dozen files (docs/RELEASING.md, step 2). When
one is left behind, CI fails three tests and ``doctor`` reports the installed
copy as older than itself: the CLI prints the built metadata (2.4.0+dex.3)
against ``__version__ = "2.4.0+dex.1"`` in the same install. This module holds
the list of those files and the rule that checks them. ``tests/test_documentation.py``
and ``tools/playbook/hooks/pre-commit`` both call it, so neither keeps a copy.

    python -B tools/release_version.py                        # report, exit 0
    python -B tools/release_version.py --check                # exit 1 when a file disagrees
    python -B tools/release_version.py --check --from-index   # judge the next commit
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

#: Where the copy-paste Action pin lives: the README and its translations.
README_FILES = (
    "README.md",
    "README.hi-IN.md",
    "README.ja-JP.md",
    "README.ko-KR.md",
    "README.zh-CN.md",
)
ACTION_PIN_FILES = README_FILES + ("docs/GITHUB_ACTION.md",)

#: Repo-relative path -> file text. Everything below takes this instead of a
#: root, so a test can pass a dict and the pre-commit hook the git index.
Reader = Callable[[str], str]

ACTION_PIN = re.compile(r"tirth8205/code-review-graph@v([0-9][^\s]*)")


def read_working_tree(root: Path) -> Reader:
    return lambda name: (root / name).read_text(encoding="utf-8")


def read_git_index() -> Reader:
    """What the next commit will contain, which is not always what is on disk."""

    def read(name: str) -> str:
        blob = subprocess.run(["git", "show", f":{name}"], capture_output=True, check=False)
        if blob.returncode != 0:
            raise LookupError(f"{name} is not in the git index")
        return blob.stdout.decode("utf-8").replace("\r\n", "\n")

    return read


def _capture(text: str, pattern: str) -> str | None:
    match = re.search(pattern, text, re.MULTILINE)
    return match.group(1) if match else None


def _literal_problems(read: Reader, declared: str) -> list[str]:
    """Files that state the version as one assignment."""
    problems = []
    for name, pattern in (
        ("code_review_graph/__init__.py", r'^__version__ = "([^"]+)"$'),
        ("uv.lock", r'^name = "code-review-graph"\nversion = "([^"]+)"$'),
    ):
        found = _capture(read(name), pattern)
        if found != declared:
            problems.append(f"{name} says {found or 'nothing'}; pyproject.toml says {declared}")
    return problems


def _pin_problems(read: Reader, declared: str) -> list[str]:
    """Files that pin the GitHub Action at a release tag."""
    problems = []
    for name in ACTION_PIN_FILES:
        pins = set(ACTION_PIN.findall(read(name)))
        if pins != {declared}:
            problems.append(f"{name} pins the Action at {sorted(pins)}; expected v{declared}")
    return problems


def _sentence_problems(read: Reader, declared: str) -> list[str]:
    """Prose and forms that quote the version."""
    problems = []
    for name, text in (
        ("docs/USAGE.md", f"Applies to code-review-graph {declared}."),
        ("docs/FEATURES.md", f"## v{declared} (Current)"),
        ("CHANGELOG.md", f"## [{declared}] - "),
        (".github/ISSUE_TEMPLATE/bug_report.yml", f'placeholder: "{declared}"'),
    ):
        if text not in read(name):
            problems.append(f"{name} does not say {text!r}")
    if read("docs/FEATURES.md").count("(Current)") != 1:
        problems.append("docs/FEATURES.md marks more than one heading (Current)")
    return problems


def release_version_mismatches(read: Reader) -> list[str]:
    """Every place a release moves the version, against ``pyproject.toml``.

    ``pyproject.toml`` is the reference because it is what gets built into the
    distribution's metadata, which is what ``code-review-graph --version``
    prints. An empty list means every file agrees.
    """
    declared = _capture(read("pyproject.toml"), r'^version = "([^"]+)"$')
    if declared is None:
        return ['pyproject.toml has no version = "..." line']
    return [
        *_literal_problems(read, declared),
        *_pin_problems(read, declared),
        *_sentence_problems(read, declared),
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check that the version is the same in every file a release moves."
    )
    parser.add_argument(
        "--check", action="store_true", help="exit 1 when any file disagrees with pyproject.toml"
    )
    parser.add_argument(
        "--from-index",
        action="store_true",
        help="read the git index (the next commit) instead of the working tree",
    )
    args = parser.parse_args(argv)
    try:
        read = read_git_index() if args.from_index else read_working_tree(Path.cwd())
        problems = release_version_mismatches(read)
    except (OSError, LookupError) as exc:
        print(f"release version: cannot read a stamp: {exc}", file=sys.stderr)
        return 2
    if problems:
        print(
            "The version is not the same in every file a release moves "
            "(docs/RELEASING.md, step 2):",
            file=sys.stderr,
        )
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
    else:
        print("The version is the same in every file a release moves.")
    return 1 if problems and args.check else 0


if __name__ == "__main__":
    sys.exit(main())
