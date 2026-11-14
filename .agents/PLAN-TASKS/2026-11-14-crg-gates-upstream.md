---
dex_contract: spt
version: 3
status: 'RASCUNHO'
owner: 'sprinter / mantenedor CRG'
date: '2026-11-14'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'Encaminhamento de Carlos CRG-GATES-UPSTREAM-20261114 após o veredito do piloto anterior.'
goal:
  id: 'crg-gates-upstream-20261114'
  title: 'Comparar upstream e verificar merges com CRG e suíte declarada'
  objective: 'Decidir o aproveitamento da versão 2.4.0 por prova isolada e verificar conflitos de integração pela CLI da casa.'
context: 'A edição da casa permanece principal. O piloto de portabilidade tem fluxo próprio e permanece bloqueado por acesso.'
problem: 'Grafo e merge textual podem parecer verdes enquanto o resultado combinado falha nos testes.'
decision: 'Usar wheels verificados em bancos novos e simular merge com base e commits explícitos em clone descartável.'
scope:
  include:
    - 'Comparação isolada, implementação CLI local, testes sintéticos e evidência.'
  exclude:
    - 'PATH, banco habitual, MCP, CI, remoto, push e deltas preexistentes.'
requirements:
  - id: REQ-01
    statement: 'Comparar wheels no mesmo Windows e checkout'
    criteria:
      - id: C-01
        statement: 'SHA-256, bancos efetivamente abertos, HEAD, inventário, vínculos, cobertura, HTML e saída CP1252 registrados.'
  - id: REQ-02
    statement: 'Implementar o fluxo CLI de merge isolado'
    criteria:
      - id: C-02
        statement: 'Git classifica conflito textual e CRG identifica impacto e testes candidatos em cópia descartável.'
  - id: REQ-03
    statement: 'Provar os resultados e registrar decisão'
    criteria:
      - id: C-03
        statement: 'Conflito textual, interação semântica, controle limpo e falhas de entrada ou execução são exercitados pela CLI.'
plan:
  - 'Comparar wheels no mesmo Windows e checkout'
  - 'Implementar o fluxo CLI de merge isolado'
  - 'Provar os resultados e registrar decisão'
tasks:
  - id: A-01
    action: 'Comparar wheels no mesmo Windows e checkout'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'SHA-256, bancos efetivamente abertos, HEAD, inventário, vínculos, cobertura, HTML e saída CP1252 registrados.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-02
    action: 'Implementar o fluxo CLI de merge isolado'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Git classifica conflito textual e CRG identifica impacto e testes candidatos em cópia descartável.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-03
    action: 'Provar os resultados e registrar decisão'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Conflito textual, interação semântica, controle limpo e falhas de entrada ou execução são exercitados pela CLI.'
        expectation:
          kind: boolean_assertion
          expected: true
closure_gates:
  - 'Suite real separada do sinal do grafo; veredito e decisão locais, sem push.'
risks:
  - 'A 2.4.0 migra o schema ao abrir um banco. Use apenas clone e DB novos.'
uncertainties:
  - 'A comparação recorta o corpus em um HEAD fixado e fixtures específicas.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'pytest tests/test_merge_check.py e recibo comparativo dos executáveis em Windows.'
execution_prompt: |
  /GOAL
  Execute a comparação e o merge-check no escopo autorizado do Trilho.
---

# CRG-GATES-UPSTREAM-20261114

- [x] A-01 — Comparar os wheels. [Bancos novos e dependências equiparadas](../receipts/CRG-GATES-UPSTREAM-20261114/comparison-matched.json).
- [x] A-02 — Implementar o fluxo isolado. [Módulo e contrato](../../code_review_graph/merge_check.py).
- [x] A-03 — Provar casos e registrar decisão. [Laudo](../receipts/CRG-GATES-UPSTREAM-20261114/INDEX.md) e [suíte do wheel](../receipts/CRG-GATES-UPSTREAM-20261114/wheel-tests.xml).
