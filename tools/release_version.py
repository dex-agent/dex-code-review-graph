"""release_version.py — the one owner of "the version is written down the same everywhere".

A release moves the version in a dozen files (docs/RELEASING.md, step 2). When
one is left behind, CI fails three tests and ``doctor`` reports the installed
copy as older than itself: the CLI prints the built metadata (2.4.0+dex.3)
against ``__version__ = "2.4.0+dex.1"`` in the same install. This module holds
the list of those files and the rule that checks them. ``tests/test_documentation.py``,
``tests/test_packaging.py`` and ``tools/playbook/hooks/pre-commit`` all call it,
so none of them keeps a copy.

    python -B tools/release_version.py                        # report, exit 0
    python -B tools/release_version.py --check                # exit 1 when a file disagrees
    python -B tools/release_version.py --check --from-index   # judge the next commit
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

#: The declared version: what gets built into the distribution's metadata.
PYPROJECT = "pyproject.toml"
PYPROJECT_VERSION = r'^version\s*=\s*"([^"]+)"$'

#: Where the copy-paste Action pin lives: the README and its translations.
README_FILES = (
    "README.md",
    "README.hi-IN.md",
    "README.ja-JP.md",
    "README.ko-KR.md",
    "README.zh-CN.md",
)
ACTION_PIN_FILES = README_FILES + ("docs/GITHUB_ACTION.md",)

#: The same version, assigned by hand in other files: (file, first group is it).
INIT_VERSION = r'^__version__\s*=\s*"([^"]+)"$'
LOCK_VERSION = r'^name\s*=\s*"code-review-graph"\r?\nversion\s*=\s*"([^"]+)"$'
VERSION_ASSIGNMENTS = (
    ("code_review_graph/__init__.py", INIT_VERSION),
    ("uv.lock", LOCK_VERSION),
)

#: Prose and forms that must quote it: (file, sentence with ``{version}``).
VERSION_SENTENCES = (
    ("docs/USAGE.md", "Applies to code-review-graph {version}."),
    ("docs/FEATURES.md", "## v{version} (Current)"),
    ("CHANGELOG.md", "## [{version}] - "),
    (".github/ISSUE_TEMPLATE/bug_report.yml", 'placeholder: "{version}"'),
)

#: Every file a release moves, derived from the rules above.
STAMP_FILES = (
    PYPROJECT,
    *(name for name, _ in VERSION_ASSIGNMENTS),
    *ACTION_PIN_FILES,
    *(name for name, _ in VERSION_SENTENCES),
)

#: Repo-relative path -> file text. Everything below takes this instead of a
#: root, so a test can pass a dict and the pre-commit hook the git index.
Reader = Callable[[str], str]

ACTION_PIN = re.compile(r"tirth8205/code-review-graph@v([0-9][^\s]*)")

SCHEMA = {
    "contract": "crg.release_version.v1",
    "reference": PYPROJECT,
    "stamps": list(STAMP_FILES),
    "flags": {
        "--check": "exit 1 instead of 0 when any stamp disagrees",
        "--from-index": "read the git index (the next commit) instead of the working tree",
    },
    "exit_codes": {
        "0": "every stamp agrees, or report mode",
        "1": "at least one stamp disagrees (--check)",
        "2": "a stamp could not be read",
    },
}

USAGE = """\
# After editing the version by hand: which files were left behind?
python -B tools/release_version.py

# As a gate (CI, scripts): exit 1 when any stamp disagrees
python -B tools/release_version.py --check

# What the next commit will contain (the pre-commit hook does this)
python -B tools/release_version.py --check --from-index

# From Python: load the module with importlib.util.spec_from_file_location and
# call release_version_mismatches(read). ``read`` maps a repo-relative path to
# the file text: read_working_tree(root), read_git_index(), or a dict.
# tests/test_documentation.py shows the dict form and the index form.
"""


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


def assigned_version(text: str, pattern: str) -> str | None:
    """The version that ``pattern``'s first group captures in ``text``, or None."""
    match = re.search(pattern, text, re.MULTILINE)
    return match.group(1) if match else None


def _assignment_problems(read: Reader, declared: str) -> list[str]:
    """Files that state the version as one assignment."""
    problems = []
    for name, pattern in VERSION_ASSIGNMENTS:
        found = assigned_version(read(name), pattern)
        if found != declared:
            problems.append(f"{name} says {found or 'nothing'}; {PYPROJECT} says {declared}")
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
    for name, sentence in VERSION_SENTENCES:
        text = sentence.format(version=declared)
        if text not in read(name):
            problems.append(f"{name} does not say {text!r}")
    current = read("docs/FEATURES.md").count("(Current)")
    if current != 1:
        problems.append(
            f"docs/FEATURES.md marks {current} headings (Current); expected exactly one"
        )
    return problems


def release_version_mismatches(read: Reader) -> list[str]:
    """Every place a release moves the version, against ``pyproject.toml``.

    ``pyproject.toml`` is the reference because it is what gets built into the
    distribution's metadata, which is what ``code-review-graph --version``
    prints. An empty list means every file agrees.
    """
    declared = assigned_version(read(PYPROJECT), PYPROJECT_VERSION)
    if declared is None:
        return [f'{PYPROJECT} has no version = "..." line']
    return [
        *_assignment_problems(read, declared),
        *_pin_problems(read, declared),
        *_sentence_problems(read, declared),
    ]


def _report(read: Reader, gate: bool) -> int:
    """Check ``read``'s files, print what disagrees and answer the exit code."""
    try:
        problems = release_version_mismatches(read)
    except (OSError, LookupError) as exc:
        print(f"release version: cannot read a stamp: {exc}", file=sys.stderr)
        return 2
    if not problems:
        print("The version is the same in every file a release moves.")
        return 0
    print(
        "The version is not the same in every file a release moves (docs/RELEASING.md, step 2):",
        file=sys.stderr,
    )
    for problem in problems:
        print(f"  - {problem}", file=sys.stderr)
    return 1 if gate else 0


def _parse_args(argv: list[str]) -> argparse.Namespace:
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
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if "--schema" in argv:
        print(json.dumps(SCHEMA, indent=2))
        return 0
    if "--usage" in argv:
        print(USAGE)
        return 0
    args = _parse_args(argv)
    read = read_git_index() if args.from_index else read_working_tree(Path.cwd())
    return _report(read, args.check)


if __name__ == "__main__":
    sys.exit(main())
