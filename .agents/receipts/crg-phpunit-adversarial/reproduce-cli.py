import io
import json
import os
import sqlite3
import subprocess
import tarfile
import tempfile
from contextlib import closing
from pathlib import Path

root = Path.cwd()
exe = root / ".venv/Scripts/code-review-graph.exe"
python = root / ".venv/Scripts/python.exe"
out = root / ".agents/receipts/crg-phpunit-adversarial"
base = "c3682acb70bfcd15c024a27f60833ac54453db30"
fix = "92fdfe052c2d97755659d1c81a3a1593e204c1c6"

def run(*args, cwd=root, env=None):
    proc = subprocess.run(args, cwd=cwd, env=env, text=True, encoding="utf-8", errors="replace", capture_output=True, check=True)
    return proc.stdout

def scan(project, relative, code):
    (project / relative).parent.mkdir(parents=True)
    (project / relative).write_text(code, encoding="utf-8")
    run("git","init","-q",cwd=project)

cases = [
    ("src_neutro","neutral","src/Example.php"),
    ("sufixo_contest","neutral","contest/Example.php"),
    ("ancestral_tests","tests/checkout","src/Example.php"),
    ("tests_real","neutral","tests/Example.php"),
]
source = "<?php namespace App; class Example { public function add($a, $b) {return $a + $b;} public function testProductionHelper() { $x = new Example(); return $x->add(1,2); } }"
rows = []
with tempfile.TemporaryDirectory(prefix="crg-adv-cli-") as temporary:
    work = Path(temporary)
    for label, sha in [("baseline",base),("fix",fix)]:
        snapshot = work / f"snapshot-{label}"
        snapshot.mkdir()
        code = subprocess.check_output(["git","archive",sha,"code_review_graph"],cwd=root)
        with tarfile.open(fileobj=io.BytesIO(code)) as archive:
            archive.extractall(snapshot, filter="data")
        env = os.environ | {"PYTHONPATH":str(snapshot),"PYTHONUTF8":"1","CRG_HOME":str(work/"crg-home")}
        module = Path(run(python,"-c","import code_review_graph.parser as p; print(p.__file__)",cwd=snapshot,env=env).strip())
        assert module.is_relative_to(snapshot), module
        for key, project_path, relative in cases:
            project = work / label / key / project_path
            scan(project,relative,source)
            run(exe,"build","--repo",str(project),env=env)
            target = str(project/relative)+"::Example.add"
            payload=json.loads(run(exe,"query","tests_for",target,"--repo",str(project),env=env))
            with closing(sqlite3.connect(project/".code-review-graph/graph.db")) as db:
                kind,flag=db.execute("SELECT kind,is_test FROM nodes WHERE name='testProductionHelper'").fetchone()
                edges=db.execute("SELECT count(*) FROM edges WHERE kind='TESTED_BY' AND source_qualified=?",(target,)).fetchone()[0]
            results=[{"name": row["name"], "indirect": row["indirect"]} for row in payload["results"]]
            rows.append({"revision":sha,"variant":key,"path_relative":relative,"kind":kind,"is_test":flag,"tested_by_edges":edges,"query_results":results})
observed = [(r["kind"],r["tested_by_edges"]) for r in rows]
assert observed == [("Function",0)]*5 + [("Test",1)]*3, observed
(out/"ab-cli.json").write_text(json.dumps({"executable":"code-review-graph.exe","fixture":source,"results":rows},indent=2)+"\n",encoding="utf-8")
print(json.dumps(rows))
