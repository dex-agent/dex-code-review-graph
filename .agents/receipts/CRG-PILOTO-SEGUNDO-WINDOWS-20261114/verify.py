"""Verify the promoted CRG wheel against a clean Dex WhatsApp commit on Windows."""

import argparse
import hashlib
import json
import os
import platform
import shutil
import sqlite3
import subprocess
import zipfile
from contextlib import closing
from pathlib import Path

WHEEL = "code_review_graph-2.3.7-py3-none-any.whl"
WHEEL_SHA = "7f2f9b60802b253739c6851ee7d84e3b970a5cd9636eab800e831f72b7e051a0"
PARSER_SHA = "2ca0223c0ef234be3fc4558fb0453c1445b188250d2431a54aac585b50a30115"
HEAD = "eb7d95b11b29fa02384323b9e6bae063a40493dc"
PARSER = "code_review_graph/parser.py"


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def run(*args, env, cwd=None, log=None, check=True):
    command = [str(arg) for arg in args]
    result = subprocess.run(command, env=env, cwd=cwd, capture_output=True)
    if log:
        log.write_bytes(result.stdout + result.stderr)
    if check and result.returncode:
        raise SystemExit(f"{command} -> {result.returncode}: {result.stderr.decode(errors='replace')}")
    return result


def save(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True, help="New directory for checkout, index and receipts")
    parser.add_argument("--rehearsal", action="store_true", help="Use the existing PATH install on the original host")
    args = parser.parse_args()
    hostname = platform.node()
    require(platform.system() == "Windows", "Este piloto exige Windows.")
    require(hostname, "Nome do Windows indisponível.")
    require(args.rehearsal or hostname.split(".")[0].casefold() != "predator",
            "PREDATOR é o host original. Use --rehearsal para um ensaio local.")

    package = Path(__file__).resolve().parent
    wheel = package / WHEEL
    require(sha(wheel) == WHEEL_SHA, "SHA-256 do wheel divergente.")
    with zipfile.ZipFile(wheel) as archive:
        require(hashlib.sha256(archive.read(PARSER)).hexdigest() == PARSER_SHA,
                "Parser dentro do wheel divergente.")

    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    env = dict(os.environ, PYTHONUTF8="1", CRG_HOME=str(out / "registry"),
               CRG_DATA_DIR=str(out / "index"), GIT_TERMINAL_PROMPT="0")
    corpus = out / "dex-whatsapp"
    run("git", "clone", "--no-checkout", package / "dex-whatsapp.bundle", corpus, env=env)

    def git(*command):
        return run("git", "-C", corpus, *command, env=env).stdout.decode("utf-8")

    git("-c", "core.hooksPath=NUL", "-c", "core.autocrlf=false", "checkout", "--detach", HEAD)
    require(git("rev-parse", "HEAD").strip() == HEAD and not git("status", "--porcelain"),
            "Checkout inicial divergente ou sujo.")
    uv = shutil.which("uv.exe")
    node = shutil.which("node.exe")
    require(uv and node, "Instale uv e Node 22+ no PATH do host de piloto.")
    node_version = run(node, "--version", env=env).stdout.decode("utf-8").strip()
    require(int(node_version.split(".")[0].lstrip("v")) >= 22, "A suíte requer Node 22+.")
    if not args.rehearsal:
        bin_dir = out / "bin"
        env.update(UV_TOOL_DIR=str(out / "tools"), UV_TOOL_BIN_DIR=str(bin_dir),
                   PATH=str(bin_dir) + os.pathsep + env["PATH"])
        run(uv, "tool", "install", "--no-config", "--python", "3.13", "--constraints",
            package / "constraints.txt", "--with", "google-genai", f"{wheel}[all]",
            env=env, log=out / "install.log")

    launcher = shutil.which("code-review-graph.exe", path=env["PATH"])
    require(launcher, "code-review-graph.exe indisponível no PATH.")
    launcher = Path(launcher).resolve()
    tool_path = Path(run(uv, "tool", "dir", env=env).stdout.decode("utf-8").strip())
    bin_path = Path(run(uv, "tool", "dir", "--bin", env=env).stdout.decode("utf-8").strip())
    require(launcher.parent == bin_path.resolve(), "O PATH resolveu um launcher de outro ambiente.")
    installed_parser = tool_path / "code-review-graph" / "Lib/site-packages" / PARSER
    require(sha(installed_parser) == PARSER_SHA, "O parser da CLI efetiva diverge do wheel.")

    def crg(*command, log=None):
        return run(launcher, *command, "--repo", corpus, env=env, log=log).stdout

    database = out / "index/graph.db"
    require(not database.exists(), "O índice descartável já existe.")
    crg("build", log=out / "build.log")
    status = json.loads(crg("status", "--json"))
    require(status["built_at_commit"] == status["current_sha"] == HEAD, "SHA do índice divergente.")
    install = f"{corpus / 'scripts/install.cjs'}::install"
    test = str(corpus / "tests/distribution.test.cjs")
    query = json.loads(crg("query", "tests_for", install))
    require(query["status"] == "ok", "A consulta tests_for falhou.")
    direct = [row["qualified_name"] for row in query["results"] if row["indirect"] is False]
    with closing(sqlite3.connect(database.as_uri() + "?mode=ro", uri=True)) as db:
        integrity = db.execute("PRAGMA quick_check").fetchall()
        files = {Path(row[0]).relative_to(corpus).as_posix() for row in db.execute(
            "SELECT file_path FROM nodes WHERE kind = 'File' AND file_path LIKE '%.cjs'"
        )}
        edges = db.execute(
            """SELECT e.target_qualified, t.file_path, e.line
               FROM edges e JOIN nodes t ON e.target_qualified = t.qualified_name
               WHERE e.kind = 'TESTED_BY' AND e.source_qualified = ? AND t.kind = 'Test'""",
            (install,),
        ).fetchall()
    tracked = set(git("ls-files", "-z", "--", "*.cjs").rstrip("\0").split("\0"))
    require(integrity == [("ok",)], f"quick_check falhou: {integrity}")
    require(files == tracked and len(tracked) == 21,
            f"Inventário .cjs divergente: faltam {tracked - files}, sobram {files - tracked}.")
    require(len(edges) == 1, f"Esperada uma aresta direta, obtidas {len(edges)}.")
    target, test_file, line = edges[0]
    require(direct == [target] and test_file == test and line == 4 and
            "I.install(" in git("show", "HEAD:tests/distribution.test.cjs").splitlines()[line - 1],
            "CLI, SQLite e código divergiram na associação direta com o teste.")
    require(not git("status", "--porcelain"), "O build do índice alterou o checkout.")
    identity = {"host": hostname, "windows": platform.version(), "rehearsal": args.rehearsal, "git_head": HEAD}
    save(out / "graph.json", {
        **identity, "wheel_sha256": WHEEL_SHA, "parser_sha256": PARSER_SHA,
        "launcher": str(launcher), "launcher_sha256": sha(launcher), "quick_check": integrity,
        "index": str(database), "status": status, "git_cjs": sorted(tracked), "sqlite_cjs": sorted(files),
        "tested_by_cli": direct, "tested_by_sql": {"source": install, "target": target, "line": line},
    })

    suite = run(node, "scripts/test.cjs", env=env, cwd=corpus, log=out / "suite.txt", check=False)
    clean = git("rev-parse", "HEAD").strip() == HEAD and not git("status", "--porcelain")
    counts = {}
    for line in suite.stdout.decode("utf-8", errors="replace").splitlines():
        label, _, count = line.removeprefix("ℹ ").removeprefix("# ").partition(" ")
        if label in {"tests", "pass", "fail", "skipped"} and count.isascii() and count.isdecimal():
            counts[label] = int(count)
    save(out / "suite.json", {
        **identity, "node": node_version, "exit_code": suite.returncode, "checkout_clean": clean,
        "counts": counts, "log": "suite.txt",
    })
    require(suite.returncode == 0 and clean and counts.get("tests", 0) > 0 and counts.get("fail") == 0,
            "A suíte ou a checagem final do checkout falhou.")
    print(out)


if __name__ == "__main__":
    main()

