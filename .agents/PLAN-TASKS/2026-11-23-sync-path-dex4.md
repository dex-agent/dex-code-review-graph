---
dex_contract: spt
version: 3
status: 'EM_EXECUCAO'
owner: 'sessao:zcode (CRG)'
date: '2026-11-23'
workspace: 'C:/CodexProjetos/code-review-graph'
abertura:
  contexto: 'Medido em 2026-11-23: o PATH roda copia congelada (uv tool) do wheel construido em b45272a9 as 15:54; o PR #6 entrou na main as 17:47 (merge fd2fb339, parser em d3771a6b). O parser instalado e identico ao de 6b48d125, com 0 ocorrencias de _js_effect_fn_; o da main tem 6. Nenhum processo do CRG ativo. dist/ guarda o wheel dex.3 para rollback. Fontes vivas: recibos CRG-240DEX-PATH-20261116 e Trilho 2026-11-23-versao-uma-fonte'
  ferramentas: 'tools/release_version.py (dono dos 13 carimbos), suite packaging opt-in (tests/test_packaging.py), uv (build e tool install), tests/test_js_wrapped_functions.py, dex-pendencias (ledger), chama-o-vigia (CI), dex-fechamento-projeto-atualizado (fiscal)'
  mentor: 'nao convocado: sem duvida de API; o caminho da troca vem dos recibos da casa'
origin: 'Pergunta do dono em 2026-11-23 ao ver que o PATH nao tem a feature do PR #6: "por que? nao deveria estar sincronizado?". Quiz sem resposta; recomendada seguida pela regra de silencio (INTERROGAR-ESGOTOU-PESQUISAR-NAO-ADIVINHAR)'
goal:
  id: 'sync-path-dex4-20261123'
  title: 'PATH sincronizado com a main: 2.4.0+dex.4 com a indexacao de Effect.fn'
  objective: 'O executavel do PATH executa o codigo da main: bump para 2.4.0+dex.4 nos 13 carimbos, wheel construido do commit do bump, instalacao com recibo e rollback, prova funcional na copia instalada, indice do repo reconstruido e consumidores conferidos'
context: 'A copia do PATH e um wheel congelado; o PR #6 mudou o parser depois do ultimo wheel'
problem: 'A ferramenta do PATH esta atras da main: a indexacao de Effect.fn existe no codigo e nao no executavel que as janelas usam'
decision: 'Bump para dex.4, porque comportamento novo do parser nao entra sob o mesmo nome de versao; wheel do commit do bump; troca do PATH com recibo e rollback como em 16/11; prova pela copia instalada, nao pelo codigo do repo; sem tag (dex.2 e dex.3 nao tem)'
scope:
  include:
    - 'bump 2.4.0+dex.4 nos 13 carimbos, fechando a entrada Unreleased do Effect.fn no FEATURES e no CHANGELOG'
    - 'wheel construido do HEAD depois do commit do bump, com sha256 no recibo'
    - 'instalacao no PATH com uv tool install --force, recibo e rotas de rollback'
    - 'prova funcional rodando tests/test_js_wrapped_functions.py contra a copia instalada'
    - 'rebuild do indice do proprio repo com o executavel novo'
    - 'gate de consumidores: duas skills que ensinam o CRG conferidas; skill stale vira item no TRACKER do registry'
    - 'pendencia CRG-WHEEL-PATH-SEM-EFFECT-FN-20261123 consumida pelo CLI'
  exclude:
    - 'criar tag git para dex.4'
    - 'editar pacote de skill no registry: fica para o corte da Governanta'
    - 'rebuild de indices de outros repos que usam o CRG: cada dono roda code-review-graph build quando precisar da feature'
    - 'apagar a venv .venv-240dex ou os 2,2 GB de residuo derivado (PENDENTES CRG-RESIDUO-FORA-DO-REPO-20261123)'
requirements:
  - id: REQ-01
    statement: 'O repo declara 2.4.0+dex.4 de forma consistente'
    criteria:
      - id: C-01
        statement: 'os 13 carimbos de versao iguais'
      - id: C-02
        statement: 'testes de documentacao e de Effect.fn verdes no repo'
  - id: REQ-02
    statement: 'O executavel do PATH e o codigo da main'
    criteria:
      - id: C-03
        statement: 'wheel 2.4.0+dex.4 construido do HEAD com a feature no parser'
      - id: C-04
        statement: 'PATH em 2.4.0+dex.4, doctor sem problema e parser instalado com a feature'
      - id: C-05
        statement: 'testes do Effect.fn passam contra a copia instalada e o indice do repo foi reconstruido pelo executavel novo'
  - id: REQ-03
    statement: 'A troca tem rastro e nao deixou consumidor para tras'
    criteria:
      - id: C-06
        statement: 'recibo com sha256, rotas de rollback e conferencia dos consumidores gravados'
      - id: C-07
        statement: 'pendencia consumida pelo CLI e ledger valido'
      - id: C-08
        statement: 'main publicada, CI verde no HEAD e fiscal sem vermelho'
plan:
  - 'A-01 bump 2.4.0+dex.4'
  - 'A-02 commit do bump e wheel do HEAD'
  - 'A-03 troca do PATH com rollback guardado'
  - 'A-04 prova na copia instalada e rebuild do indice'
  - 'A-05 consumidores, ledger, publicacao, CI e fiscal'
tasks:
  - id: A-01
    action: 'Subir os 13 carimbos para 2.4.0+dex.4 e fechar a entrada Unreleased do Effect.fn'
    covers: [REQ-01]
    done_when: [C-01, C-02]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'python -B tools/release_version.py --check'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: '.venv/Scripts/python.exe -B -m pytest tests/test_documentation.py tests/test_js_wrapped_functions.py -q -p no:cacheprovider'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Commitar o bump sozinho e construir o wheel a partir do HEAD'
    covers: [REQ-02]
    done_when: [C-03]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'test -s dist/code_review_graph-2.4.0+dex.4-py3-none-any.whl && unzip -p dist/code_review_graph-2.4.0+dex.4-py3-none-any.whl code_review_graph/parser.py | rg -q "_js_effect_fn_"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Instalar o wheel no PATH, guardar o wheel anterior e registrar as rotas de rollback'
    covers: [REQ-02]
    done_when: [C-04]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'code-review-graph --version | rg -q -F "2.4.0+dex.4" && code-review-graph doctor > /dev/null && rg -q -F "_js_effect_fn_" "$USERPROFILE/AppData/Roaming/uv/tools/code-review-graph/Lib/site-packages/code_review_graph/parser.py"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Rodar os testes do Effect.fn contra a copia instalada e reconstruir o indice do repo'
    covers: [REQ-02]
    done_when: [C-05]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-05
        proves: [C-05]
        method: command
        procedure: 'T=$(mktemp -d) && printf "[pytest]\n" > "$T/pytest.ini" && PYTHONPATH="$USERPROFILE/AppData/Roaming/uv/tools/code-review-graph/Lib/site-packages" .venv/Scripts/python.exe -P -B -c "import code_review_graph as m; assert \"Roaming/uv/tools\" in m.__file__.replace(chr(92), \"/\"), m.__file__" && PYTHONPATH="$USERPROFILE/AppData/Roaming/uv/tools/code-review-graph/Lib/site-packages" .venv/Scripts/python.exe -P -B -m pytest -c "$T/pytest.ini" --rootdir "$T" --confcutdir "$T" "$PWD/tests/test_js_wrapped_functions.py" --import-mode=importlib -p no:cacheprovider -q && rm -rf "$T" && code-review-graph doctor > /dev/null'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-05
    action: 'Conferir os consumidores, consumir a pendencia pelo CLI, gravar o recibo, publicar e rodar o fiscal'
    covers: [REQ-03]
    done_when: [C-06, C-07, C-08]
    depends_on: [A-04]
    evidence_requirements:
      - id: ER-06
        proves: [C-06]
        method: command
        procedure: 'test -s .agents/receipts/CRG-PATH-DEX4-20261123/INDEX.md'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-07
        proves: [C-07]
        method: command
        procedure: 'python -B "$USERPROFILE/.agents/skills/dex-pendencias/scripts/pendencias.py" --arquivo .agents/PENDENTES.md --valida'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-08
        proves: [C-08]
        method: command
        procedure: 'test -z "$(git status --porcelain)" && git fetch -q origin main && test "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-09
        proves: [C-08]
        method: command
        procedure: 'gh run list -R dex-agent/dex-code-review-graph --commit "$(git rev-parse HEAD)" --json conclusion --jq ".[].conclusion" | rg -q "^success$"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-10
        proves: [C-08]
        method: command
        procedure: 'python -B "$USERPROFILE/.agents/skills/dex-fechamento-projeto-atualizado/scripts/scan-fechamento.py" --repo C:/CodexProjetos/code-review-graph --out - > /dev/null'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'release_version.py --check exit 0 no HEAD publicado'
  - 'parser instalado no PATH identico ao do HEAD, com fim de linha normalizado'
  - 'testes do Effect.fn verdes contra a copia instalada, com a origem da importacao conferida (RED de abertura: 3 falhas na copia dex.3)'
  - 'rollback viavel: wheel dex.3 preservado e rota registrada'
risks:
  - 'o executavel do PATH e compartilhado por todas as janelas: mitigacao = trocar sem processo do CRG ativo, preservar o wheel dex.3 e registrar as rotas de rollback'
  - 'indice construido antes do PR #6 nao enxerga Effect.fn com update: mitigacao = rebuild do indice do repo e aviso no recibo'
  - 'bump parcial deixa a main vermelha (tres ocorrencias anteriores): mitigacao = release_version.py --check antes do commit, no hook e no CI'
uncertainties:
  - 'a suite packaging e opt-in e pode demorar; se falhar por ambiente Windows, o resultado fica como ressalva e a prova fica no wheel explicito'
  - 'skills do registry que citam dex.3 como versao atual ficam uma versao atras depois do bump; o conserto do pacote e corte da Governanta e fica como item'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'python -B tools/release_version.py --check'
  - 'python -B "$USERPROFILE/.agents/skills/dex-fechamento-projeto-atualizado/scripts/scan-fechamento.py" --repo C:/CodexProjetos/code-review-graph'
execution_prompt: |
  /GOAL Executar o Trilho .agents/PLAN-TASKS/2026-11-23-sync-path-dex4.md no workspace C:/CodexProjetos/code-review-graph: fases A-01 a A-05 sem parar entre fases — bump para 2.4.0+dex.4 nos 13 carimbos, commit do bump, wheel do HEAD, troca do PATH com rollback, prova na copia instalada, rebuild do indice, gate de consumidores, ledger, publicacao, CI e fiscal; verdict no fim.
---

# Sincronizar o PATH com a main: 2.4.0+dex.4

## Checklist visual
- [x] A-01 — bump 2.4.0+dex.4
- [x] A-02 — commit do bump e wheel do HEAD
- [x] A-03 — troca do PATH com rollback guardado
- [x] A-04 — prova na cópia instalada e rebuild do índice
- [ ] A-05 — consumidores, ledger, publicação, CI e fiscal

Recibos: `.agents/receipts/CRG-PATH-DEX4-20261123/`.
