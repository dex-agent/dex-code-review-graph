---
dex_contract: spt
version: 3
status: 'EM_EXECUCAO'
owner: 'mantenedor CRG'
date: '2026-11-25'
workspace: 'C:/CodexProjetos/code-review-graph'
abertura:
  contexto: 'Auditoria em f55e4ff2 confirmou mutação em status, índice obsoleto e cinco asserções CommonJS incompatíveis com Windows.'
  ferramentas: 'CLI CRG, pytest, Git, gh e Toolsbook local.'
  mentor: 'SQLite, abertura mode=ro consultada durante a auditoria.'
origin: 'Pedido para corrigir os achados e enviar PR.'
goal:
  id: 'crg-status-e-commonjs-20261125'
  title: 'Corrigir status e testes CommonJS'
  objective: 'Preservar o banco em status, corrigir a regressão de testes Windows e atualizar o índice local.'
context: 'O status migrou um banco v9 e preservou a revisão antiga do grafo.'
problem: 'Consultar status pode alterar o banco e testes usam a representação de caminho errada.'
decision: 'Abrir status em leitura, consolidar expectativas POSIX e reconstruir o índice local com backup.'
scope:
  include: ['CLI status, testes CommonJS, documentação e índice local']
  exclude: ['Novas instalações paralelas, mudanças em índices de outros repos e publicação de release']
requirements:
  - id: REQ-01
    statement: 'Corrigir os achados verificados no CRG.'
    criteria:
      - id: C-01
        statement: 'Testes provam status sem alteração de banco legado e expectativas Windows no CommonJS.'
plan:
  - 'Reproduzir e corrigir as duas falhas em testes.'
  - 'Atualizar e verificar o índice local após backup.'
  - 'Publicar a branch e abrir PR.'
tasks:
  - id: A-01
    action: 'Corrigir a abertura de status e as expectativas Windows.'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'python -m pytest tests/test_cli_reconciliation.py tests/test_commonjs_imports.py -q'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Testes focais, doctor e leitura da publicação.'
risks:
  - 'Atualização do índice local exige cópia verificável antes do build.'
uncertainties:
  - 'O estado da autenticação Git e GitHub pode divergir.'
gates:
  - 'Preflight do formato v3 e testes da correção.'
validation:
  - 'python -m pytest tests/test_cli_reconciliation.py tests/test_commonjs_imports.py -q'
execution_prompt: |
  /GOAL
  Executar este Trilho em C:/CodexProjetos/code-review-graph.
---

# Status somente leitura e testes CommonJS
