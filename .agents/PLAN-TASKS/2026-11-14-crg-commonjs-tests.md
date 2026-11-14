---
dex_contract: spt
version: 3
status: 'RASCUNHO'
owner: 'sprinter / mantenedor CRG'
date: '2026-11-14'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'GO do dono após o diagnóstico do diff real do Dex WhatsApp.'
goal:
  id: 'crg-commonjs-tests-2026-11-14'
  title: 'Reconhecer testes CommonJS'
  objective: 'Corrigir testes CommonJS e comprovar TESTED_BY direto de install no diff real do Dex WhatsApp.'
context: 'Bead crg-6bf e itens locais 0001 e 0002. Consumidor scripts/install.cjs no Dex WhatsApp.'
problem: 'A classificação de arquivo e o reconhecimento lexical omitem nós Test e a associação direta.'
decision: 'Preservar dois REDs e provar a correção na CLI instalada em ambiente isolado.'
scope:
  include:
    - 'Parser CommonJS, regressões, prova isolada do diff e mapas locais.'
  exclude:
    - 'Push, alteração da CLI habitual ou do banco persistente, alteração da política de tests_for.'
requirements:
  - id: REQ-01
    statement: 'Preservar os dois REDs'
    criteria:
      - id: C-01
        statement: 'A prova RED identifica a falha de classificação e a falha do alias.'
  - id: REQ-02
    statement: 'Corrigir o parser e respeitar a sombra'
    criteria:
      - id: C-02
        statement: 'Os dois casos corrigidos e os controles lexicais passam.'
  - id: REQ-03
    statement: 'Validar na CLI e no SQLite'
    criteria:
      - id: C-03
        statement: 'TESTED_BY direto para install e seleção por arquivo concordam com Git.'
plan:
  - 'Adicionar regressões e executar antes da correção.'
  - 'Corrigir classificação e vínculo lexical e verificar regressões.'
  - 'Rodar o wheel isolado, confrontar SQLite, CLI e Git e registrar mapas e fechamento.'
tasks:
  - id: A-01
    action: 'Adicionar regressões e executar antes da correção.'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Rodar pytest nos dois casos focais contra o parser original e registrar as falhas por caso.'
        expectation:
          kind: command_exit
          expected_exit_code: 1
  - id: A-02
    action: 'Corrigir classificação e vínculo lexical e verificar regressões.'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Rodar python -m pytest tests/test_commonjs_imports.py e guardar a saída.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Rodar o wheel isolado, confrontar SQLite, CLI e Git e registrar mapas e fechamento.'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Comparar os IDs e caminhos da consulta tests_for e do SQLite e conferir verify e o controle vazio contra git diff.'
        expectation:
          kind: boolean_assertion
          expected: true
closure_gates:
  - 'Checklist completo, revisão atestada e goal_verdict registrado. Mapas e fechamento local atualizados.'
risks:
  - 'Inferir teste por nome pode gerar falso TESTED_BY. Cobrir vínculo real e sombra.'
uncertainties:
  - 'O resultado de tests_for verify é medido separadamente da associação direta de install.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'pytest, CLI isolada, consulta SQLite read-only e git diff --check.'
execution_prompt: |
  /GOAL
  Execute este Trilho no workspace C:/CodexProjetos/code-review-graph.
---

# Reconhecer testes CommonJS

Tipo SPEC-PLAN-TASKs · crg-6bf

- [x] A-01 — Dois REDs observados antes da correção. [Saída original](../receipts/crg-commonjs-tests-20261114/red.txt).
- [x] A-02 — Suíte focal verde e controles de sombra. [Saída final](../receipts/crg-commonjs-tests-20261114/green.txt).
- [x] A-03 — CLI e SQLite isolados, diff Git, revisão, mapas e fechamento. [Prova](../receipts/crg-commonjs-tests-20261114/proof.json) · [Mapas](../MAPAS/INDEX.md).
