"""Regression checks for user-facing command examples."""

import importlib.util
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]

# One owner for "which files carry the Action pin" and for the rule that the
# version is the same in each of them: the pre-commit hook calls the same module.
_spec = importlib.util.spec_from_file_location(
    "release_version", ROOT / "tools" / "release_version.py"
)
assert _spec is not None and _spec.loader is not None
release_version = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(release_version)
README_FILES = release_version.README_FILES
OPTIONAL_GROUPS = (
    "embeddings",
    "google-embeddings",
    "communities",
    "enrichment",
    "eval",
    "wiki",
    "all",
)
USER_DOC_FILES = README_FILES + (
    "docs/COMMANDS.md",
    "docs/FAQ.md",
    "docs/USAGE.md",
    "code_review_graph/docs/LLM-OPTIMIZED-REFERENCE.md",
    "docs/TROUBLESHOOTING.md",
)


def test_pip_extra_examples_use_cross_shell_double_quotes():
    """Extras must survive zsh globbing without breaking Windows cmd.exe."""
    for readme_name in README_FILES:
        content = (ROOT / readme_name).read_text(encoding="utf-8")
        for group in OPTIONAL_GROUPS:
            command = f'pip install "code-review-graph[{group}]"'
            assert command in content, f"{readme_name} is missing {command}"


def test_current_user_docs_have_no_unquoted_pip_extras():
    pattern = re.compile(r"pip install code-review-graph\[[A-Za-z0-9-]+\]")
    for doc_name in USER_DOC_FILES:
        content = (ROOT / doc_name).read_text(encoding="utf-8")
        assert pattern.search(content) is None, f"unquoted pip extras in {doc_name}"


def test_github_action_references_use_current_supported_majors():
    """Keep active workflows and copy-paste examples on supported majors."""
    files = [
        ROOT / "action.yml",
        ROOT / "README.md",
        ROOT / "docs/GITHUB_ACTION.md",
        *(ROOT / ".github/workflows").glob("*.yml"),
    ]
    expected_majors = {"checkout": "7", "cache": "6"}
    for path in files:
        content = path.read_text(encoding="utf-8")
        for action, expected in expected_majors.items():
            for actual in re.findall(rf"actions/{action}@v(\d+)", content):
                assert actual == expected, (
                    f"{path.relative_to(ROOT)} uses actions/{action}@v{actual}; "
                    f"expected v{expected}"
                )


def test_codebuddy_install_docs_cover_project_artifacts():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    usage = (ROOT / "docs/USAGE.md").read_text(encoding="utf-8")

    assert "install --platform codebuddy" in readme
    for artifact in (
        ".mcp.json",
        "CODEBUDDY.md",
        ".codebuddy/settings.json",
        ".codebuddy/skills/<name>/SKILL.md",
    ):
        assert artifact in usage


def test_zed_remote_setup_docs_explain_local_checkout_workaround():
    """Keep the host/config mismatch from #828 discoverable from the platform list."""
    troubleshooting = (ROOT / "docs/TROUBLESHOOTING.md").read_text(encoding="utf-8")
    usage = (ROOT / "docs/USAGE.md").read_text(encoding="utf-8")

    heading = "### 6. Zed native agent cannot see MCP in an SSH project"
    assert heading in troubleshooting
    section = troubleshooting.split(heading, 1)[1].split("\n---", 1)[0]
    for detail in (
        "context_servers",
        "user-level settings",
        "remote host",
        "local checkout",
        "cwd",
        "code-review-graph install --platform zed",
        "code-review-graph build",
        "https://github.com/tirth8205/code-review-graph/issues/828",
    ):
        assert detail in section, f"Zed troubleshooting is missing {detail}"
    assert "TROUBLESHOOTING.md#6-zed-native-agent-cannot-see-mcp-in-an-ssh-project" in usage


def test_schema_version_is_current_everywhere_it_is_written_down():
    """The places CI's schema-sync job does not reach.

    schema-sync compares ``migrations.py`` against the VS Code extension only.
    The schema version is also written down in prose that ships — ``docs/`` is
    in the sdist — and in the Action's cache key, and each of those drifted
    behind the migrations at least once.
    """
    from code_review_graph.migrations import LATEST_VERSION

    schema_doc = (ROOT / "docs/schema.md").read_text(encoding="utf-8")
    assert f"The current schema version is {LATEST_VERSION}," in schema_doc, (
        f"docs/schema.md does not state schema version {LATEST_VERSION}"
    )
    assert f"| {LATEST_VERSION} |" in schema_doc, (
        f"docs/schema.md has no migration table row for v{LATEST_VERSION}"
    )

    troubleshooting = (ROOT / "docs/TROUBLESHOOTING.md").read_text(encoding="utf-8")
    assert f"this build understands v{LATEST_VERSION})" in troubleshooting, (
        "the sample newer-database error in docs/TROUBLESHOOTING.md names a "
        f"version other than v{LATEST_VERSION}"
    )

    for name in ("action.yml", "docs/GITHUB_ACTION.md"):
        content = (ROOT / name).read_text(encoding="utf-8")
        segments = set(re.findall(r"schema(\d+)", content))
        assert segments == {str(LATEST_VERSION)}, (
            f"{name} names cache schema segment(s) {sorted(segments)}; "
            f"expected only schema{LATEST_VERSION}"
        )

def test_codex_install_docs_cover_global_skill_and_runtime_scope():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    usage = (ROOT / "docs/USAGE.md").read_text(encoding="utf-8")
    for content in (readme, usage):
        assert "$CODEX_HOME" in content
        assert "skills/code-review-graph" in content
        assert "WSL" in content or "Windows" in content
        assert "read-only CLI" in content


def test_release_version_is_current_everywhere_it_is_written_down():
    """The package version, in every place a release has to move it.

    A release bumps ``pyproject.toml`` and ``__version__``; the copy-paste
    Action pins, the user guide, the feature list, the changelog heading, the
    bug-report form and the lock file each have to move with them, and the
    form had asked for 2.3.5 through four releases. The list of places lives
    in ``tools/release_version.py``; the pre-commit hook runs the same check.
    """
    problems = release_version.release_version_mismatches(
        release_version.read_working_tree(ROOT)
    )
    assert problems == []


def _stamped_files(version: str) -> dict[str, str]:
    """Every file a release moves, all saying ``version``."""
    files = {
        "pyproject.toml": f'[project]\nname = "code-review-graph"\nversion = "{version}"\n',
        "code_review_graph/__init__.py": f'"""Code Review Graph."""\n\n__version__ = "{version}"\n',
        "uv.lock": (
            'version = 1\n\n[[package]]\nname = "code-review-graph"\n'
            f'version = "{version}"\nsource = {{ editable = "." }}\n'
        ),
        "docs/USAGE.md": f"# Usage\n\nApplies to code-review-graph {version}.\n",
        "docs/FEATURES.md": (
            f"# Features\n\n## v{version} (Current)\n\n- Highlights.\n\n## v1.0.0\n- Old.\n"
        ),
        "CHANGELOG.md": (
            f"# Changelog\n\n## [Unreleased]\n\n## [{version}] - 2026-01-01\n\n- Notes.\n"
        ),
        ".github/ISSUE_TEMPLATE/bug_report.yml": (
            "body:\n  - type: input\n    attributes:\n" f'      placeholder: "{version}"\n'
        ),
    }
    for name in release_version.ACTION_PIN_FILES:
        files[name] = f"      - uses: tirth8205/code-review-graph@v{version}\n"
    return files


def _moved(files: dict[str, str], name: str, old: str, new: str) -> dict[str, str]:
    """``files`` with the version moved from ``old`` to ``new`` in ``name`` only."""
    return {**files, name: files[name].replace(old, new)}


def _problems(files: dict[str, str]) -> list[str]:
    return release_version.release_version_mismatches(files.__getitem__)


def test_release_version_check_stays_quiet_on_a_synchronized_tree():
    """The negative control: nothing to report when every file agrees."""
    assert _problems(_stamped_files("9.9.9+dex.7")) == []


def test_release_version_check_reports_a_pyproject_without_a_version():
    files = {
        **_stamped_files("2.4.0+dex.1"),
        "pyproject.toml": '[project]\nname = "code-review-graph"\n',
    }
    assert _problems(files) == ['pyproject.toml has no version = "..." line']


def test_release_version_check_catches_a_bump_that_moved_only_pyproject():
    """6aa3cb23 (2026-11-21) and f86f9920 (2026-11-22): ``pyproject.toml`` moved alone."""
    stale = _stamped_files("2.4.0+dex.1")
    problems = _problems(_moved(stale, "pyproject.toml", "2.4.0+dex.1", "2.4.0+dex.3"))
    left_behind = (
        "code_review_graph/__init__.py",
        "README.md",
        "docs/GITHUB_ACTION.md",
        "docs/USAGE.md",
        "docs/FEATURES.md",
        "CHANGELOG.md",
        ".github/ISSUE_TEMPLATE/bug_report.yml",
        "uv.lock",
    )
    assert problems, "a bump that moved only pyproject.toml was not reported"
    for name in left_behind:
        assert any(problem.startswith(f"{name} ") for problem in problems), (
            f"{name} was left behind and not reported: {problems}"
        )
    assert not any(problem.startswith("pyproject.toml ") for problem in problems), problems


def test_release_version_check_catches_a_bump_that_moved_only_the_package_literal():
    """The mirror image: ``__version__`` moved, the built metadata left behind."""
    files = _stamped_files("2.4.0+dex.2")
    moved = _moved(
        files, "code_review_graph/__init__.py", "2.4.0+dex.2", "2.4.0+dex.3"
    )
    problems = _problems(moved)
    assert len(problems) == 1, problems
    assert problems[0].startswith("code_review_graph/__init__.py ")


@pytest.mark.parametrize("name", release_version.ACTION_PIN_FILES)
def test_release_version_check_catches_one_pin_file_left_behind(name: str):
    """Every translation counts: one stale pin is reported, and only that one."""
    stale = _stamped_files("2.4.0+dex.1")
    problems = _problems(_moved(stale, name, "2.4.0+dex.1", "2.4.0+dex.2"))
    assert len(problems) == 1, problems
    assert problems[0].startswith(f"{name} ")


def test_release_version_check_catches_two_current_headings_in_the_feature_list():
    """A new ``(Current)`` heading added without taking the mark off the old one."""
    files = _stamped_files("2.4.0+dex.1")
    features = files["docs/FEATURES.md"].replace("## v1.0.0", "## v1.0.0 (Current)")
    problems = _problems({**files, "docs/FEATURES.md": features})
    assert problems == ["docs/FEATURES.md marks more than one heading (Current)"]


def test_release_version_check_catches_a_lock_file_left_at_the_old_version():
    """uv.lock said 2.4.0 through three house bumps; no test read it until 2026-11-23."""
    files = _stamped_files("2.4.0+dex.3")
    problems = _problems(_moved(files, "uv.lock", "2.4.0+dex.3", "2.4.0"))
    assert len(problems) == 1, problems
    assert problems[0].startswith("uv.lock ")


def test_releasing_doc_names_every_file_a_release_moves():
    """docs/RELEASING.md is the release checklist (crg-4eb.3). It must name
    each file the version check above reads, and be reachable from the
    contributor guide and the docs index."""
    releasing = (ROOT / "docs/RELEASING.md").read_text(encoding="utf-8")
    for name in (
        "pyproject.toml",
        "code_review_graph/__init__.py",
        "uv.lock",
        "CHANGELOG.md",
        "docs/FEATURES.md",
        "docs/USAGE.md",
        "docs/GITHUB_ACTION.md",
        "README.md",
        ".github/ISSUE_TEMPLATE/bug_report.yml",
    ):
        assert f"`{name}`" in releasing, f"docs/RELEASING.md does not name {name}"
    assert "(docs/RELEASING.md)" in (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    assert "(RELEASING.md)" in (ROOT / "docs/INDEX.md").read_text(encoding="utf-8")
