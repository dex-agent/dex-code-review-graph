import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import tempfile
import zipfile
from collections import Counter
from pathlib import Path

report_dir, origin, exe, wheel = map(lambda value: Path(value).resolve(), sys.argv[1:])
report_dir.mkdir(parents=True, exist_ok=True)
run = Path(tempfile.mkdtemp(prefix="crg-cjs-e2e-"))
env = {**os.environ, "CRG_HOME": str(run / "registry"), "PYTHONUTF8": "1"}
commands = []


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args], encoding="utf-8").splitlines()


def commit(repo, message, *paths):
    git(repo, "-c", "core.autocrlf=false", "add", "--", *paths)
    git(repo, "-c", "core.hooksPath=NUL", "-c", "commit.gpgSign=false",
        "-c", "user.name=CRG E2E", "-c", "user.email=fixture@example.invalid", "commit", "-qm", message)
    return git(repo, "rev-parse", "HEAD")[0]


def cli(label, repo, *args, result_json=False):
    result = subprocess.run([str(exe), *args, "--repo", str(repo)], cwd=repo, env=env,
                            encoding="utf-8", errors="replace", capture_output=True)
    commands.append({"step": label, "args": list(args), "exit": result.returncode})
    (report_dir / f"{label}.out").write_text(result.stdout, encoding="utf-8")
    if result.stderr:
        (report_dir / f"{label}.err").write_text(result.stderr, encoding="utf-8")
    result.check_returncode()
    return json.loads(result.stdout) if result_json else result.stdout


def db_snapshot(index):
    db = index / "graph.db"
    with sqlite3.connect(db.as_uri() + "?mode=ro", uri=True) as connection:
        nodes = connection.execute(
            "SELECT kind,qualified_name,file_path,language,line_start,line_end FROM nodes"
        ).fetchall()
        edges = connection.execute(
            "SELECT kind,source_qualified,target_qualified,file_path,line FROM edges"
        ).fetchall()
    return Counter(nodes), Counter(edges)


def build(label, repo, index):
    cli(f"{label}-build", repo, "build", "--data-dir", str(index))
    result = cli(f"{label}-status", repo, "status", "--data-dir", str(index), "--json", result_json=True)
    assert result["built_at_commit"] == result["current_sha"] == git(repo, "rev-parse", "HEAD")[0]
    return result


proof = json.loads((report_dir.parent / "crg-cjs-20261113/proof.json").read_text(encoding="utf-8"))
assert sha(wheel) == proof["wheel_sha256"]
assert sha(exe) == proof["candidate_exe_sha256"]
parser = exe.parent.parent / "candidate-tools/code-review-graph/Lib/site-packages/code_review_graph/parser.py"
with zipfile.ZipFile(wheel) as artifact:
    parser_sha = hashlib.sha256(artifact.read("code_review_graph/parser.py")).hexdigest()
assert parser_sha == sha(parser) == proof["source_parser_sha256"]

corpus = run / "corpus"
corpus.mkdir()
source_head = git(origin, "rev-parse", "HEAD")[0]
source_before = git(origin, "status", "--porcelain=v1")
paths = set(git(origin, "ls-files", "--", "*.cjs"))
assert len(paths) == 19 and paths == set(proof["covered_corpus_files"])
hashes = {}
for name in sorted(paths):
    src, dst = origin / name, corpus / name
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(src.read_bytes())
    hashes[name] = sha(src)
    assert hashes[name] == sha(dst)
sentinel = ".agents/receipts/stage/core.cjs"
(corpus / sentinel).parent.mkdir(parents=True)
(corpus / sentinel).write_text("module.exports.fake = () => 0;\n", encoding="utf-8")
(corpus / ".code-review-graphignore").write_text("/.agents/**\n", encoding="utf-8")
git(corpus, "init", "-q")
commit(corpus, "Set up disposable CommonJS corpus", *sorted(paths), sentinel, ".code-review-graphignore")
assert sentinel in git(corpus, "ls-files", "--", "*.cjs")
expected_imports = set()
for name in paths:
    for match in re.finditer(r"""\brequire\s*\(\s*(['"])(\.[^'"]+\.cjs)\1\s*\)""",
                            (corpus / name).read_text(encoding="utf-8")):
        target = ((corpus / name).parent / match[2]).resolve()
        if target.is_relative_to(corpus) and target.relative_to(corpus).as_posix() in paths:
            expected_imports.add((name, target.relative_to(corpus).as_posix()))
ci = run / "corpus-index"
cs = build("corpus", corpus, ci)
query = cli("corpus-imports", corpus, "query", "imports_of", "src/coordinator.cjs", result_json=True)
nodes, edges = db_snapshot(ci)
assert cs["files"] == 19
assert {Path(path).relative_to(corpus).as_posix() for kind, _, path, lang, *_ in nodes
        if kind == "File" and lang == "javascript"} == paths
assert not any(".agents" in Path(path).parts for _, _, path, *_ in nodes)
actual_imports = {(Path(a).relative_to(corpus).as_posix(), Path(b).relative_to(corpus).as_posix())
                  for kind, a, b, _, _ in edges if kind == "IMPORTS_FROM"
                  and Path(a).is_relative_to(corpus) and Path(b).is_relative_to(corpus)}
assert actual_imports == expected_imports and len(actual_imports) == 24
assert query["status"] == "ok"
assert {Path(r["import_target"]).relative_to(corpus).as_posix() for r in query["results"]} == {
    target for source, target in expected_imports if source == "src/coordinator.cjs"}
assert ("REFERENCES", str(corpus / "src/coordinator.cjs"), str(corpus / "src/coordinator.cjs")+"::resolve",
        str(corpus / "src/coordinator.cjs"), 17) in edges

fixture = run / "fixture"
fixture.mkdir()
initial = {
    "package.json": '{"type":"module"}\n',
    "dep.cjs": "function run() { return 7; }\nmodule.exports = { run };\n",
    "missing.js": "export function ghost() { return 0; }\n",
    "app.cjs": "const { run } = require('./dep.cjs');\n"
               "const unresolved = require('./dep');\n"
               "const { ghost } = require('./missing.cjs');\n"
               "module.exports.start = () => run();\n"
               "module.exports.never = () => ghost();\n",
}
for name, body in initial.items():
    (fixture / name).write_text(body, encoding="utf-8", newline="\n")
git(fixture, "init", "-q")
base = commit(fixture, "Initial CommonJS graph", *initial)
fi = run / "fixture-index"
build("fixture", fixture, fi)
imports = cli("fixture-imports", fixture, "query", "imports_of", "app.cjs", result_json=True)
assert imports["status"] == "ok"
assert {r["import_target"] for r in imports["results"]} == {str(fixture / "dep.cjs"), "./dep", "./missing.cjs"}

app = fixture / "app.cjs"
app.write_text(initial["app.cjs"].replace("() => run();", "() => run() + 1;"), encoding="utf-8", newline="\n")
head = commit(fixture, "Change one CommonJS function", "app.cjs")
changed = git(fixture, "diff", "--name-only", base, head)
diff = git(fixture, "diff", "--unified=0", base, head, "--", "app.cjs")
assert changed == ["app.cjs"] and len([line for line in diff if line.startswith("@@")]) == 1
hunk = next(line for line in diff if line.startswith("@@"))
assert re.match(r"@@ -4(?:,1)? \+4(?:,1)? @@", hunk), hunk
cli("fixture-update", fixture, "update", "--data-dir", str(fi))
status = cli("fixture-updated-status", fixture, "status", "--data-dir", str(fi), "--json", result_json=True)
assert status["current_sha"] == status["built_at_commit"] == head
qn = str(fixture / "dep.cjs") + "::run"
callers = cli("fixture-callers", fixture, "query", "callers_of", qn, result_json=True)
assert callers["status"] == "ok"
assert {r["qualified_name"] for r in callers["results"]} == {str(app) + "::module.exports.start"}
analysis = {}
for scope in ("app.cjs", "dep.cjs"):
    result = cli(f"diff-{scope}", fixture, "detect-changes", "--base", base, "--files", scope, result_json=True)
    analysis[scope] = [(n["name"], Path(n["file_path"]).name, n["line_start"], n["line_end"])
                       for n in result["changed_functions"]]
assert analysis["app.cjs"] == [("module.exports.start", "app.cjs", 4, 4)], analysis
assert analysis["dep.cjs"] == []
before_repeat = db_snapshot(fi)
assert ("CALLS", str(app) + "::module.exports.start", qn, str(app), 4) in before_repeat[1]
assert not any(kind == "CALLS" and target == str(fixture / "missing.js")+"::ghost"
               for kind, _, target, _, _ in before_repeat[1])
cli("fixture-repeat-update", fixture, "update", "--data-dir", str(fi))
assert db_snapshot(fi) == before_repeat
assert git(origin, "rev-parse", "HEAD") == [source_head] and git(origin, "status", "--porcelain=v1") == source_before
assert all(sha(origin / name) == value for name, value in hashes.items())
receipt = {
    "result": "passed", "origin_head": source_head, "snapshot_head": cs["built_at_commit"],
    "wheel_sha256": sha(wheel), "parser_sha256": parser_sha, "launcher_sha256": sha(exe),
    "inventory_sha256": hashes, "covered_paths": sorted(paths), "staging_nodes": 0,
    "import_pairs": sorted(actual_imports), "changed_paths": changed, "git_hunk": hunk,
    "fixture_git_base": base, "fixture_git_head": head, "changed_functions": analysis,
    "unresolved_imports": ["./dep", "./missing.cjs"], "false_calls_to_js_homonym": 0,
    "repeat_same_nodes_edges": True, "commands": commands,
}
(report_dir / "proof.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(f"E2E passed: {len(paths)} paths, {len(actual_imports)} pairs, {len(commands)} CLI commands. Isolated indexes: {run}")
