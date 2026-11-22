---
dex_contract: spt
version: 3
status: 'ATIVO'
owner: 'paula-planeja-spt'
date: '2026-11-21'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO do dono via $oraculo-pragmatico (GO PADRAO, quiz sem resposta a tempo — seguiu pelo recomendado) para pagar ISSUE-LOCAL-0006 apontada pela janela dona do dex-memoria no corte 0.1.20'
goal:
  id: 'issue0006-winerror2-spawn-npm-windows'
  title: 'merge-check executa suíte npm no Windows (nunca WinError 2 por spawn)'
  objective: 'Resolver o executável da suíte por plataforma no chokepoint _run_suite e provar com RED→GREEN que merge-check -- npm test devolve veredito 0/1 no Windows'
context: 'repo code-review-graph (fork casa 2.4.0+dex.1, main f91c021e == origin, CI 22/22 verde); ISSUE-LOCAL-0006 aberta pela sessão dex-memoria (corte 0.1.20, issues #28/#29): merge-check com suíte npm no Windows devolve execution_error WinError 2; consumidor real: hook pre-merge-commit do dex-memoria (via 3-fases) e a frota'
problem: 'merge_check.py:90 spawna a suíte como lista crua (["npm","test"]) sem resolver executável por plataforma — no Windows npm é npm.cmd e CreateProcess dá FileNotFoundError (WinError 2), capturado como execution_error exit 2 em check_merge l.177'
decision: 'Resolver o executável no chokepoint _run_suite com shutil.which (PATH+PATHEXT) antes do spawn, cobrindo a classe de comando-sem-extensão; teste unitário novo + RED→GREEN Windows real + regressão de ponta-a-ponta no dex-memoria com CRG real (sem stub)'
scope:
  include:
    - 'cura em code_review_graph/merge_check.py (_run_suite resolve executável via shutil.which)'
    - 'teste unitário novo em tests/test_merge_check.py (resolução de comando por plataforma)'
    - 'RED→GREEN com Windows real em laboratório descartável (.agents/EVIDENCIAS/2026-11-21-issue0006/)'
    - 'suíte pytest do repo + commit + release do fork (wheel 2.4.0+dex.2) pelos gates da casa'
    - 'regressão no dex-memoria: lab-green-auto com CRG REAL na via-d'
    - 'fechar ISSUE-LOCAL-0006 dos TRACKERs dos dois repos + ficha MERGE-CHECK do dex-memoria'
  exclude:
    - 'spawn tail -f do daemon_cli.py:358 (irmão interativo não-suíte; nota no item 0006, fora deste corte)'
    - 'refatoração do pipeline de checkouts descartáveis do merge-check'
    - 'política de release/publish.yml do fork (mantida como está: disabled)'
requirements:
  - id: REQ-01
    statement: 'O comportamento defeituoso atual está provado por evidência executável ANTES da cura (RED)'
    criteria:
      - id: C-01
        statement: 'Laboratório Windows real: merge-check -- npm test devolve exit 2 com WinError 2 no error (RED0006_CONFIRMADO em log)'
  - id: REQ-02
    statement: 'Suíte com executável de plataforma roda e devolve veredito no Windows (cura)'
    criteria:
      - id: C-02
        statement: 'Mesmo laboratório com cura: merge-check -- npm test devolve exit 0 com suíte npm verde'
      - id: C-03
        statement: 'Laboratório com cura: merge-check com suíte npm vermelha (exit 1) devolve outcome regression exit 1'
      - id: C-04
        statement: 'Suíte pytest do repo verde com o teste unitário novo de resolução de comando incluído'
  - id: REQ-03
    statement: 'Circuito fechado no consumidor (dex-memoria) com CRG real'
    criteria:
      - id: C-05
        statement: 'lab-green-auto.sh do dex-memoria adaptado com CRG REAL (sem stub) na via-d executa merge-check de verdade e os casos vermelho/são mantêm os vereditos'
  - id: REQ-04
    statement: 'Trilha e fechamento completos'
    criteria:
      - id: C-06
        statement: 'ISSUE-LOCAL-0006 integrado nos TRACKERs dos dois repos + commit/push/release do fork + ficha MERGE-CHECK do dex-memoria atualizada'
plan:
  - 'Trilho do MOLDE + preflight achados=0'
  - 'A-01: RED Windows real (lab-issue0006-red.sh)'
  - 'A-02: cura no chokepoint _run_suite (shutil.which) + teste unitário + GREEN (lab-issue0006-green.sh) + suíte pytest'
  - 'A-03: release do fork (wheel 2.4.0+dex.2 promovido ao PATH) + TRACKERs'
  - 'A-04: regressão dex-memoria com CRG real + ficha MERGE-CHECK + verdict'
tasks:
  - id: A-01
    action: 'Provar RED com Windows real: repo git dummy com package.json, merge-check -- npm test capturando exit e error (espera exit 2 + WinError 2)'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'bash .agents/EVIDENCIAS/2026-11-21-issue0006/lab-issue0006-red.sh — monta repo dummy com 3 commits, roda code-review-graph merge-check -- npm test e asserta exit=2 com WinError 2 no relatório; sai 0 imprimindo RED0006_CONFIRMADO'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Curar _run_suite: resolver executável via shutil.which antes do subprocess.run; teste unitário novo; GREEN com suíte npm verde e vermelha; suíte pytest do repo'
    covers: [REQ-02]
    done_when: [C-02, C-03, C-04]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02, C-03]
        method: command
        procedure: 'bash .agents/EVIDENCIAS/2026-11-21-issue0006/lab-issue0006-green.sh — mesmo laboratório com cura: caso verde exit 0 (outcome passed) e caso vermelho exit 1 (outcome regression); sai 0 imprimindo GREEN0006_OK'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-03
        proves: [C-04]
        method: command
        procedure: 'python -m pytest tests/test_merge_check.py -q (e suíte focal do repo conforme CI) — exit 0 com o teste novo de resolução incluído'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Release do fork: commit da cura, wheel 2.4.0+dex.2 construído e promovido ao PATH (padrão do Trilho crg-240dex-path-troca), push, TRACKERs 0006 integrados'
    covers: [REQ-04]
    done_when: [C-06]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-04
        proves: [C-06]
        method: command
        procedure: 'git log -1 + code-review-graph --version (2.4.0+dex.2 no PATH) + rg ISSUE-LOCAL-0006 nos TRACKERs dos dois repos com status integrado'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Regressão de ponta-a-ponta no dex-memoria: lab-green-auto com CRG REAL na via-d + ficha MERGE-CHECK sem E-SE WinError + verdict neste Trilho + memórias do bloco'
    covers: [REQ-03, REQ-04]
    done_when: [C-05, C-06]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-05
        proves: [C-05]
        method: command
        procedure: 'bash .agents/EVIDENCIAS/2026-11-21-issue28-29/lab-green-real-crg.sh (dex-memoria) — merge automático com suíte CRG REAL executada (log do merge-check com commits base/ours/theirs) e vereditos mantidos; sai 0 imprimindo GREEN-REAL-CRG_OK'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-06
        proves: [C-06]
        method: command
        procedure: 'rg -n "goal_verdict" neste Trilho com verdict e checklist 100% + node preflight.mjs no Trilho final (status CONCLUIDO) exit 0'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'preflight spt-kit exit 0 achados=0 antes da execução'
  - 'RED antes da cura; GREEN com Windows real; suíte pytest verde'
  - 'regressão dex-memoria com CRG real antes de fechar o TRACKER'
  - 'memórias do bloco (auto + espelho dex) + áudio Bruninha se avanço substancial'
risks:
  - 'shutil.which pode não achar npm em PATH de shell unix (Git Bash) quando o CRG roda de dentro do hook — mitigação: o hook roda com PATH herdado do git (Windows PATH, com npm.cmd presente); teste GREEN usa o mesmo ambiente do consumidor'
  - 'suíte pytest completa do repo pode ter jobs que dependem de browser/opcionais — mitigação: rodar a suíte focada (tests/test_merge_check.py + conjunto que o CI executa localmente viável); declarar o que rodou'
  - 'promover wheel ao PATH pode conflitar com a instalação uv atual — mitigação: seguir o padrão do Trilho crg-240dex-path-troca (receipt + rollback)'
uncertainties:
  - 'Formato exato do release do fork (wheel promovido ao PATH .local/bin versus uv tool install) — decidido pelo padrão do Trilho crg-240dex-path-troca ao abrir o A-03; se ambos viáveis, escolher o do Trilho anterior'
  - 'Gates do repo code-review-graph (beads/bd + TRACKER + pre-commits) podem exigir passos adicionais ao commit — lidos no A-03 antes do commit'
gates:
  - 'spt_validate valid=true antes de goal_start; com MCP ausente, preflight.mjs exit 0 achados=0 + validação semântica local com evidência registrada (SPT-VALIDATE-FAIL-NAO-PARA)'
validation:
  - 'node C:/CodexProjetos/dex-PPIRTV/spt-kit/preflight.mjs .agents/PLAN-TASKS/2026-11-21-issue0006-winerror2-spawn-npm.md (exit 0)'
  - 'bash .agents/EVIDENCIAS/2026-11-21-issue0006/lab-issue0006-red.sh (RED) ANTES da cura'
  - 'bash .agents/EVIDENCIAS/2026-11-21-issue0006/lab-issue0006-green.sh + python -m pytest tests/test_merge_check.py -q APOS a cura'
  - 'bash .agents/EVIDENCIAS/2026-11-21-issue28-29/lab-green-real-crg.sh (dex-memoria, CRG real)'
execution_prompt: |
  /GOAL
  Executar o Trilho .agents/PLAN-TASKS/2026-11-21-issue0006-winerror2-spawn-npm.md no workspace C:\CodexProjetos\code-review-graph na ordem A-01..A-04: provar RED WinError 2 com Windows real, curar o spawn no chokepoint _run_suite, GREEN + suíte + release do fork, regressão de ponta-a-ponta no dex-memoria com CRG real e verdict com evidências.
---

# ISSUE-LOCAL-0006 — merge-check Windows: WinError 2 no spawn da suíte npm

**Tipo:** SPEC-PLAN-TASKs · **Owner:** paula-planeja-spt (Trilho) / sessão (execução)
**Origem:** GO do dono via `$oraculo-pragmatico` (quiz sem resposta a tempo — seguiu pelo recomendado, emenda GO 2026-11-16).
**Status:** ATIVO · **Data:** 2026-11-21 · **Fonte dos quality_gates:** `agent-ops/secrets-scan` (release/push) + universal.

## SPEC

Causa-raiz na fonte: `code_review_graph/merge_check.py:90-92` spawna a suíte como lista crua; no Windows `npm` é `npm.cmd` → `FileNotFoundError` (WinError 2) → capturado como `execution_error` exit 2 (`check_merge` l.177) — a via 3-fases do gate do dex-memoria não entrega veredito na plataforma principal. Chokepoint: TODAS as suítes do merge-check passam por `_run_suite`; irmão não-suíte (`daemon_cli.py:358` `tail -f`) declarado fora do corte.

## TASKs (checklist visual)

### A-01 · RED Windows real (C-01)
- [ ] Lab dummy com 3 commits + package.json (suíte npm)
- [ ] merge-check -- npm test → exit 2 + WinError 2 (RED0006_CONFIRMADO)

### A-02 · Cura chokepoint + testes (C-02, C-03, C-04)
- [ ] _run_suite resolve executável (shutil.which: PATH+PATHEXT)
- [ ] Teste unitário novo de resolução de comando
- [ ] GREEN: verde exit 0 (passed) / vermelho exit 1 (regression) (GREEN0006_OK)
- [ ] pytest tests/test_merge_check.py verde

### A-03 · Release do fork + TRACKERs (C-06)
- [ ] Commit + wheel 2.4.0+dex.2 promovido ao PATH (padrão crg-240dex-path-troca)
- [ ] ISSUE-LOCAL-0006 integrado nos TRACKERs dos 2 repos

### A-04 · Regressão consumidor + verdict (C-05, ER-06)
- [ ] dex-memoria: lab-green-real-crg.sh com CRG REAL na via-d (GREEN-REAL-CRG_OK)
- [ ] Ficha MERGE-CHECK sem E-SE WinError
- [ ] goal_verdict + memórias + áudio Bruninha

## goal_verdict

(A registrar em A-04.)
