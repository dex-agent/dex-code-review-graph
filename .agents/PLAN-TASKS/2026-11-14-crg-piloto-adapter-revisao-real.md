---
dex_contract: spt
version: 3
status: 'CONCLUIDO'
owner: 'sprinter / mantenedor CRG'
date: '2026-11-14'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'GO do dono 2026-11-14 aceitando recomendacao do oraculo-solid: piloto do adapter CRG com canario oraculado primeiro.'
goal:
  id: 'crg-piloto-adapter-revisao-real-20261114'
  title: 'Pilotar o adapter do CRG em revisao real'
  objective: 'Provar o wheel candidato 8fd3127c em consumo real com canario oraculado no Dex WhatsApp eb7d95b e revisao medida de diff real 5356307, em ambiente isolado, com laudo de metricas.'
context: 'Kit run1 validado (3 fases verdes + releitura); bundle dex-whatsapp sha256 a9d44a88 conferido no disco em C:/CodexProjetos/code-review-graph/.agents/receipts/CRG-PILOTO-SEGUNDO-WINDOWS-20261114/package/dex-whatsapp.bundle; venv candidate em C:/CodexProjetos/crg-2w-execucao/run1/candidate (CLI em Scripts/code-review-graph.exe); reuso master_maximus: grafo_gate e normalize_name; restricoes confirmadas: prewarm incondicional no Windows, callers_of cego a tests/, FTS falso-negativo em ofuscado.'
problem: 'A prova faltante da adocao e o consumidor real: suite verde com cliente ideal nao destrava a revisao real.'
decision: 'Pilotar em duas etapas oraculadas: canario Dex WhatsApp 21/21 via bundle e revisao do commit real 5356307 com gabarito conhecido para medir TP/FP/FN.'
scope:
  include:
    - 'Clone descartavel do bundle dex-whatsapp no HEAD eb7d95b fora do repo'
    - 'Indice CRG descartavel construido pela venv candidate do run1'
    - 'Canario 21/21 e TESTED_BY direto conferido na CLI e no SQLite'
    - 'Revisao CRG do diff 5356307 com TP/FP/FN contra gabarito'
    - 'Medicoes Windows: cache HF antes/depois, tempo de startup e de build'
    - 'Laudo com metricas e analise de reuso das tools master_maximus'
  exclude:
    - 'Instalacao habitual, PATH, MCP e indices existentes'
    - 'Push, publicacao ou envio de arquivos'
    - 'Alterar o wheel candidato ou o codigo do CRG'
    - 'Promocao a instalacao permanente (decisao posterior do dono)'
requirements:
  - id: REQ-01
    statement: 'Canario oraculado no Dex WhatsApp eb7d95b'
    criteria:
      - id: C-01
        statement: 'Indice novo no clone eb7d95b com 21/21 testes aprovados, TESTED_BY direto scripts para distribution.test.cjs:4 conferido na CLI e no SQLite e built_at_commit igual ao HEAD.'
  - id: REQ-02
    statement: 'Revisao real medida com gabarito'
    criteria:
      - id: C-02
        statement: 'detect-changes, impact e tests_for sobre o diff 5356307 executados com TP, FP e FN calculados contra o gabarito das funcoes realmente alteradas.'
  - id: REQ-03
    statement: 'Ambiente isolado com egress zero'
    criteria:
      - id: C-03
        statement: 'Clone e indices em diretorios descartaveis fora do repo, cache HF identico antes/depois e instalacao habitual intocada.'
  - id: REQ-04
    statement: 'Laudo com metricas e reuso'
    criteria:
      - id: C-04
        statement: 'Laudo em .agents/receipts/CRG-PILOTO-ADAPTER-20261114/ com 21/21, TP/FP/FN, tempos, egress e analise de reuso grafo_gate/normalize_name registrada e localizavel por rg.'
plan:
  - 'Preparar ambiente isolado e clonar o bundle em eb7d95b'
  - 'Executar canario oraculado com indice descartavel'
  - 'Executar revisao real do commit 5356307 com gabarito'
  - 'Consolidar laudo, metricas e analise de reuso'
tasks:
  - id: A-01
    action: 'Preparar ambiente isolado e clonar o bundle em eb7d95b'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-03]
        method: command
        procedure: 'git clone do bundle em diretorio descartavel; checkout eb7d95b; conferir sentence-transformers ausente na venv candidate; snapshot do cache HF antes e depois do bloco'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Executar canario oraculado Dex WhatsApp com indice descartavel'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-01]
        method: command
        procedure: 'build com CRG_DATA_DIR descartavel via CLI candidate; node --test esperando 21/21; query tests_for na CLI e no SQLite; status com current_sha==built_at_commit==eb7d95b'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Executar revisao real do diff 5356307 com gabarito'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-03
        proves: [C-02]
        method: command
        procedure: 'detect-changes HEAD~1..HEAD no repo CRG via CLI candidate; impact e tests_for nas funcoes do gabarito; calcular TP/FP/FN contra gabarito derivado do git diff'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Consolidar laudo com metricas e analise de reuso'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-02, A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'gravar laudo com numeros medidos em .agents/receipts/CRG-PILOTO-ADAPTER-20261114/LAUDO.md e conferir rg das metricas no arquivo'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Laudo indexado em receipts com INDEX.md; PLAN-TASKS/INDEX.md e ACTIVE.md atualizados; nenhuma superficie habitual tocada.'
risks:
  - 'Prewarm incondicional no Windows: mitigacao com venv sem sentence-transformers e conferencia de cache HF antes/depois.'
  - 'callers_of cego a tests/: nao concluir codigo morto sem cruzar rg no plano de revisao.'
  - 'FTS falso-negativo em nome ofuscado: zero hit nao prova ausencia.'
uncertainties:
  - 'Expectativa 21/21 herdada do LEIA-ME do primeiro host; se o bundle divergir do HEAD ensaiado, registra-se finding sem bloquear o piloto.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes do goal_start.'
validation:
  - 'node C:/CodexProjetos/dex-PPIRTV/spt-kit/preflight.mjs <este trilho>; validacao semantica dex-ppirtv-validate-spt; comandos do canario e da revisao com exit 0.'
execution_prompt: |
  /GOAL
  Retomar em C:/CodexProjetos/code-review-graph.
  Execute 100% do SPT ativo .agents/PLAN-TASKS/2026-11-14-crg-piloto-adapter-revisao-real.md
  Objetivo: pilotar o adapter do CRG em revisao real com canario oraculado e laudo de metricas.
---

# Piloto do adapter do CRG em revisao real

Tipo: SPEC-PLAN-TASKs · status: RASCUNHO até validar · owner: sprinter / mantenedor CRG
Origem: GO do dono 2026-11-14 (recomendação oraculo-solid, selos l.7146/l.2377/l.2378/l.11402/l.5848).

## Checklist visual (Clara — [x] só com evidência)

- [x] A-01 [AÇÃO] Ambiente isolado + clone eb7d95b | owner: sessão | when: agora | source: ER-01
  - [x] C-03 [CRITÉRIO] dirs descartáveis, cache HF antes/depois iguais (89=89), habitual intocada | evidence: ER-01; LAUDO.md §A-01 | source: REQ-03
- [x] A-02 [AÇÃO] Canário Dex WhatsApp | owner: sessão | when: após A-01 | source: ER-02
  - [x] C-01 [CRITÉRIO] suíte 73/73 (rehearsal 72/72; "21/21" do LEIA-ME era número defasado — finding registrado) + TESTED_BY direto :4 (CLI e SQLite idênticos) + HEAD==built_at eb7d95b | evidence: ER-02; LAUDO.md §A-02 | source: REQ-01
- [x] A-03 [AÇÃO] Revisão real diff 5356307 | owner: sessão | when: após A-01 | source: ER-03
  - [x] C-02 [CRITÉRIO] TP=32/FN=3→0 real/FP=1→0 real (classificados com evidência do diff); precisão/recall efetivos 100% | evidence: ER-03; LAUDO.md §A-03 | source: REQ-02
- [x] A-04 [AÇÃO] Laudo + reuso | owner: sessão | when: após A-02+A-03 | source: ER-04
  - [x] C-04 [CRITÉRIO] LAUDO.md em receipts com 21→73, TP/FP/FN, tempos (3s/10s), egress (89=89) + reuso grafo_gate/normalize_name | evidence: ER-04; LAUDO.md §A-04 | source: REQ-04

## Riscos vivos
- R-01 prewarm embeddings (mitigado: venv sem extra + cache check)
- R-02 callers_of cego a tests/ (método: cruzar rg)
- R-03 FTS falso-negativo em ofuscado (método: zero hit ≠ ausência)

## Fora do corte [OUT]
- X-01 promoção a instalação permanente (decisão do dono com o laudo na mão)
- X-02 openras dos 502 nós CHAVE* com coluna clean_name (upstream master_maximus)

## Cooperadores materiais
Chato (fiscal vivo) · oraculo-solid (comando) · grafo_gate.py e normalize_name (reuso master_maximus, sessão sess_8a7ea947).

## /GOAL
Ver execution_prompt do front matter.
