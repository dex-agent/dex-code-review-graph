---
dex_contract: spt
version: 3
status: 'CONCLUIDO_COM_RESSALVAS'
owner: 'sprinter'
date: '2026-11-08'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO do dono para o recorte PHPUnit de crg-iu1'
goal:
  id: 'crg-phpunit-windows-2026-11-08'
  title: 'PHPUnit direto no Windows'
  objective: 'Classificar PHPUnit no Windows e provar a associacao direta pela CLI'
context: 'CLI principal no repo privado Dex. Baseline com 27 falhas Windows em c3682ac'
problem: 'Um metodo PHPUnit camelCase em tests com separador nativo e classificado como Function'
decision: 'Normalizar separador nativo apenas na classificacao de arquivo de teste'
scope:
  include:
    - 'code_review_graph/parser.py'
    - 'tests/test_php_scoped_calls.py'
    - '.github/workflows/ci.yml'
    - '.agents/PLAN-TASKS'
    - 'Continuidade local e receipts crg-phpunit-windows'
  exclude:
    - 'Outras familias do bead, migracao de paths SQLite e rebuild do indice persistente'
requirements:
  - id: REQ-01
    statement: 'O caso PHPUnit falha no checkout base do Windows'
    criteria:
      - id: C-01
        statement: 'O caso PHPUnit falha no checkout base do Windows'
  - id: REQ-02
    statement: 'A regressao focada de PHPUnit passa no Windows'
    criteria:
      - id: C-02
        statement: 'A regressao focada de PHPUnit passa no Windows'
  - id: REQ-03
    statement: 'A consulta CLI devolve o teste PHPUnit como direto'
    criteria:
      - id: C-03
        statement: 'A consulta CLI devolve o teste PHPUnit como direto'
  - id: REQ-04
    statement: 'A comparacao focada confirma o delta de falhas previsto'
    criteria:
      - id: C-04
        statement: 'A comparacao focada confirma o delta de falhas previsto'
plan:
  - 'Reproduzir o falso negativo no executavel e nos testes PHPUnit'
  - 'Corrigir o detector comum e habilitar os tres casos na etapa Windows da CI'
  - 'Construir grafo isolado e consultar a associacao com o executavel'
  - 'Comparar os 27 IDs do baseline e verificar o diff final'
tasks:
  - id: A-01
    action: 'Reproduzir o falso negativo no executavel e nos testes PHPUnit'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Executar os tres IDs PHPUnit existentes via pytest e confirmar as falhas por ID no red.json'
        expectation:
          kind: command_exit
          expected_exit_code: 1
  - id: A-02
    action: 'Corrigir o detector comum e habilitar os tres casos na etapa Windows da CI'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Executar os tres IDs PHPUnit com o controle negativo na fixture e guardar exit do pytest no green.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Construir grafo isolado e consultar a associacao com o executavel'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Executar build e query tests_for com code-review-graph.exe na fixture PHP e verificar TESTED_BY e indirect=false no cli.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Comparar os 27 IDs do baseline e verificar o diff final'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Executar via pytest os 27 IDs do receipt historico e verificar a diferenca de conjuntos no comparison.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Atualizar continuidade e beads, guardar evidencias, publicar no origin privado e registrar verdict.'
risks:
  - 'Detector compartilhado pode mudar classificacao. Usar controle negativo e comparar falhas por ID.'
uncertainties:
  - 'Suíte Windows integral segue aberta no bead ate reconciliar o restante.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - '.venv/Scripts/python.exe -m pytest -q tests/test_php_scoped_calls.py tests/test_multilang.py::TestPHPTestAnnotations'
execution_prompt: |
  /GOAL
  Execute .agents/PLAN-TASKS/2026-11-08-crg-phpunit-windows.md em C:\CodexProjetos\code-review-graph na ordem, com verdict oficial.
---

# PHPUnit direto no Windows

Tipo: SPEC-PLAN-TASKs

## SPEC e PLAN

Owner de planejamento Sprinter, execução pelo mantenedor CRG. Oráculo Clean Code usa o repertório promovido e a edição EN 2008, capítulos 9, 12 e 17. O Chato cobra caso negativo e separa identidade de caminho da classificação. Ponytail concentra a mudança no detector existente. Fonte dos quality_gates: princípios da casa e universal_gates do manifesto de domínios.

Revisão causal e revisão A–E: apto. A-01 usa pytest como observador do RED no baseline e registra também a consulta CLI antes do patch. A-02 tem exit pytest com controle negativo e readback dos três IDs no YAML da CI. A-03 compara saída do executável e aresta SQLite, com fixture temporária nova. A-04 compara por identidade com o receipt histórico e falha se um ID novo ou uma regressão esperada divergir. As saídas serão vinculadas por hash. Estrutura e referências são responsabilidade do runtime, causalidade do revisor. causal_semantics_reviewed=true, goal_start_readiness=ready.

## Checklist visual

- [x] A-01 [AÇÃO] Reproduzir o falso negativo no executavel e nos testes PHPUnit | owner: mantenedor CRG | when: após goal_start | source: ER-01 | evidence: [resultado](../receipts/crg-phpunit-windows/summary.json), `evd_20261109005054571_0252_0182`
- [x] A-02 [AÇÃO] Corrigir o detector comum e habilitar os tres casos na etapa Windows da CI | owner: mantenedor CRG | when: depois de A-01 | source: ER-02 | evidence: [resultado](../receipts/crg-phpunit-windows/summary.json), `evd_20261109005117651_0253_0184`
- [x] A-03 [AÇÃO] Construir grafo isolado e consultar a associacao com o executavel | owner: mantenedor CRG | when: depois de A-02 | source: ER-03 | evidence: [resultado](../receipts/crg-phpunit-windows/summary.json), `evd_20261109005127093_0254_0186`
- [x] A-04 [AÇÃO] Comparar os 27 IDs do baseline e verificar o diff final | owner: mantenedor CRG | when: depois de A-03 | source: ER-04 | evidence: [resultado](../receipts/crg-phpunit-windows/summary.json), `evd_20261109005142614_0255_0188`

## Resultados

- Produto `92fdfe0`, RED no baseline `c3682ac`. A CLI passou de zero para uma associação direta. O método comum em `src` continuou Function.
- Suíte completa Windows 3.13.13: 2287 passaram, 24 falhas conhecidas, 12 skips e 2 xpasses. Exatamente 3 IDs removidos e zero novos.
- Seleção Windows da CI reproduzida localmente com Python 3.12.11: 511 passaram e 10 skips. Ruff passou no diff Python.
- Flow `flow_20261109004949066_0244_0172`, revisão `evd_20261109005242625_0261_0196`. [Mapas do corte](../MAPAS/INDEX.md) e [recibo](../receipts/crg-phpunit-windows/summary.json).

## Estacionamento

O mantenedor retoma as demais falhas em crg-iu1 antes do próximo release Windows. O índice persistente será tratado em um corte próprio.

## Veredito

**Pronto com ressalvas**, `vrd_20261109005555936_0268_0205`. Flow `flow_20261109004949066_0244_0172` completo e checklist 4/4. A suíte integral Windows tem 24 falhas preexistentes no bead `crg-iu1`. A etapa Windows foi reproduzida localmente em Python 3.12.
