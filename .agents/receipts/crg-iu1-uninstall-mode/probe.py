"""Exercise the uninstall fixture on the native filesystem."""

import json
import os
import platform
import runpy
import stat
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from code_review_graph import uninstall


def mode(path):
    return stat.S_IMODE(path.stat().st_mode)


with TemporaryDirectory(prefix="crg-uninstall-mode-") as scratch:
    root = Path(scratch)
    repo, home = root / "repo", root / "home"
    (repo / ".git" / "hooks").mkdir(parents=True)
    home.mkdir()
    config = repo / ".mcp.json"

    with patch.object(Path, "home", lambda: home):
        if sys.argv[1:] == ["--negative"]:
            test = runpy.run_path("tests/test_uninstall.py")[
                "test_atomic_config_replace_preserves_file_mode"
            ]
            replace = os.replace
            observed = []

            def change_mode_after_replace(src, dst):
                replace(src, dst)
                if Path(dst) == config:
                    before = mode(config)
                    config.chmod(0o444)
                    observed.extend((before, mode(config)))

            try:
                with patch.object(uninstall.os, "replace", change_mode_after_replace):
                    test(repo, home)
            except AssertionError as exc:
                tb = exc.__traceback__
                while tb.tb_next:
                    tb = tb.tb_next
                lines = Path(tb.tb_frame.f_code.co_filename).read_text(encoding="utf-8").splitlines()
                assert "== original_mode" in lines[tb.tb_lineno - 1]
                assert len(observed) == 2 and observed[0] != observed[1]
                print(json.dumps({
                    "platform": platform.system(),
                    "mutated_mode": [oct(value) for value in observed],
                    "assertion_line": tb.tb_lineno,
                    "rejected": True,
                }))
            else:
                raise AssertionError("Mode mutation was accepted")
            finally:
                if config.exists():
                    config.chmod(0o600)
        else:
            config.write_text(
                json.dumps({"mcpServers": {"code-review-graph": {}, "other": {"command": "mine"}}}),
                encoding="utf-8",
            )
            initial = mode(config)
            config.chmod(0o640)
            before = mode(config)
            report = uninstall.run(repo=repo, keep_data=True, keep_user_configs=True)
            after = mode(config)
            remaining = json.loads(config.read_text(encoding="utf-8"))
            leftovers = list(repo.glob(f".{config.name}.*.tmp"))
            assert before == after and not report.errors and not leftovers
            assert before == (0o666 if os.name == "nt" else 0o640)
            assert remaining == {"mcpServers": {"other": {"command": "mine"}}}
            print(json.dumps({
                "platform": platform.system(),
                "python": platform.python_version(),
                "requested": "0o640",
                "initial": oct(initial),
                "after_chmod": oct(before),
                "after_uninstall": oct(after),
                "report_errors": len(report.errors),
                "temporary_left": len(leftovers),
                "remaining": remaining,
            }, indent=2))
