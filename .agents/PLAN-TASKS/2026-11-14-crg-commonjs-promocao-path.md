---
dex_contract: spt
version: 3
status: 'RASCUNHO'
owner: 'sprinter / mantenedor CRG'
date: '2026-11-14'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'GO do usuário após o veredito do crg-6bf.'
goal:
  id: 'crg-commonjs-promocao-path-20261114'
  title: 'Promover testes CommonJS à CLI habitual'
  objective: 'Promover o wheel validado do CRG e provar TESTED_BY direto de install pela CLI do PATH em banco descartável.'
context: 'A versão 2.3.7 tem dois wheels de hashes diferentes. O candidato foi testado em índice descartável.'
problem: 'O executável habitual ainda roda o parser anterior à correção lexical.'
decision: 'Promover exatamente o wheel validado, ensaiar rollback antes e verificar o comportamento pelo PATH.'
scope:
  include:
    - 'Instalação local uv, prova isolada, mapas e consulta ao grafo rico SOLID.'
  exclude:
    - 'Push, alterações no código e banco persistente do Dex WhatsApp, mudanças na política de tests_for.'
requirements:
  - id: REQ-01
    statement: 'Confirmar artefatos e ensaiar rollback'
    criteria:
      - id: C-01
        statement: 'O wheel anterior reinstalado offline reproduz o parser e as versões anteriores em sandbox.'
  - id: REQ-02
    statement: 'Promover com a CLI livre'
    criteria:
      - id: C-02
        statement: 'Os hashes instalados correspondem ao wheel validado e as dependências conservam suas versões.'
  - id: REQ-03
    statement: 'Provar pelo PATH'
    criteria:
      - id: C-03
        statement: 'CLI do PATH e SQLite concordam em um TESTED_BY direto de install no snapshot Git descartável.'
  - id: REQ-04
    statement: 'Fechar o Trilho'
    criteria:
      - id: C-04
        statement: 'As provas, mapas e o parecer SOLID permitem retomar o corte de modo verificável.'
plan:
  - 'Confirmar artefatos e ensaiar rollback'
  - 'Promover com a CLI livre'
  - 'Provar pelo PATH'
  - 'Fechar o Trilho'
tasks:
  - id: A-01
    action: 'Confirmar artefatos e ensaiar rollback'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Inventariar a instalação, verificar hashes e provar rollback com executável em diretórios isolados.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-02
    action: 'Promover com a CLI livre'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Verificar disponibilidade de ambos os launchers e instalar offline com constraints; restaurar versão anterior se falhar.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-03
    action: 'Provar pelo PATH'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Construir banco novo pelo PATH, conferir HEAD e cruzar tests_for e os IDs SQL.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-04
    action: 'Fechar o Trilho'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Atualizar mapas locais, rodar fiscal e registrar veredito oficial.'
        expectation:
          kind: boolean_assertion
          expected: true
closure_gates:
  - 'Checklist 100 por cento e goal_verdict registrado.'
risks:
  - 'Lock Windows de serve ou daemon; não matar processos. Preservar wheel e configuração anterior.'
uncertainties:
  - 'O banco persistente pode guardar o mesmo HEAD com parser anterior; medi-lo sem mutar.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'Comparar SHA256 dos wheels e dos parsers, as distribuições uv, Git e as arestas SQLite.'
execution_prompt: |
  /GOAL
  Execute este Trilho até o veredito, com instalação reversível, sem push.
---

# Promoção da CLI CommonJS ao PATH

- [x] A-01 — Confirmar artefatos e ensaiar rollback. [Evidência](../receipts/crg-commonjs-path-20261114/backup.json).
- [x] A-02 — Promover com a CLI livre. [Evidência](../receipts/crg-commonjs-path-20261114/promotion.json).
- [x] A-03 — Provar pelo PATH. [Evidência](../receipts/crg-commonjs-path-20261114/acceptance.json).
- [x] A-04 — Fechar o Trilho. [Evidência](../receipts/crg-commonjs-path-20261114/INDEX.md).
