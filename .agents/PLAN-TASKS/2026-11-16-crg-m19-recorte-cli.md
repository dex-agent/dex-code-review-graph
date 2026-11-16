---
dex_contract: spt
version: 3
status: 'RASCUNHO'
owner: 'sprinter'
date: '2026-11-16'
workspace: 'C:/Users/crsan/.codex/worktrees/crg-combinado-240/code-review-graph'
origin: 'GO do Carlos para crg-m19 sobre o main online.'
goal:
  id: 'crg-m19-recorte-cli-20261116'
  title: 'Corrigir recorte da CLI'
  objective: 'Corrigir o recorte de detect-changes --files e provar os tres casos de crg-m19 pelo executavel com indice novo.'
context: 'Base origin/main 54efb64c e executavel 2.4.0+dex.1.'
problem: 'Faixas globais incluem simbolos de arquivos excluidos pelo filtro da CLI.'
decision: 'Aplicar os caminhos normalizados do recorte a faixas novas e delecoes no analisador compartilhado.'
scope:
  include:
    - 'changes.py, regressao executavel, receipt RED e GREEN e fechamento no Git.'
  exclude:
    - 'Alterar o executavel habitual, seu PATH, o esquema ou indices persistentes.'
requirements:
  - id: REQ-01
    statement: 'Preservar a reproducao anterior a correcao.'
    criteria:
      - id: C-01
        statement: 'O pytest focado retorna exit 1 por divergencia observada no JSON.'
  - id: REQ-02
    statement: 'Aplicar o recorte ao diff na CLI em indice novo.'
    criteria:
      - id: C-02
        statement: 'A CLI retorna apenas o simbolo alterado de A quando A e B mudam.'
      - id: C-03
        statement: 'A CLI retorna zero simbolos no recorte sem diff.'
      - id: C-04
        statement: 'A CLI retorna zero delecoes de um arquivo fora do recorte.'
  - id: REQ-03
    statement: 'Verificar os consumidores do analisador.'
    criteria:
      - id: C-05
        statement: 'A suite focada de mudancas e CLI termina com exit 0.'
plan:
  - 'Rodar regressao antes de alterar changes.py e guardar a saida.'
  - 'Restringir as faixas de cada lado do diff no analisador.'
  - 'Validar executavel do wheel em venv descartavel e revisar diff.'
tasks:
  - id: A-01
    action: 'Estender o E2E existente com delecao pura fora do recorte e preservar RED.'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'python -m pytest -q -s tests/test_cli.py -k detect_changes_file_scope com wheel valido anterior a mudanca.'
        expectation:
          kind: command_exit
          expected_exit_code: 1
  - id: A-02
    action: 'Corrigir o analisador e provar os tres recortes no executavel instalado do wheel corrigido em venv descartavel.'
    covers: [REQ-02]
    done_when: [C-02, C-03, C-04]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02, C-03, C-04]
        method: command
        procedure: 'python -m pytest -q -s tests/test_cli.py -k detect_changes_file_scope com wheel corrigido.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Executar a suite focada, revisar o diff e registrar o resultado.'
    covers: [REQ-03]
    done_when: [C-05]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-05]
        method: command
        procedure: 'python -m pytest -q tests/test_cli.py tests/test_changes.py tests/test_merge_check.py'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Atualizar bead crg-m19, registrar receipt, versionar e verificar destino privado.'
risks:
  - 'Faixas vazias apos filtro nao devem acionar reanalise de arquivo inteiro.'
uncertainties:
  - 'A suite ampla de Windows tem falhas historicas; o aceite usa testes focados.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
  - 'Revisao semantica e lapidacao com spt-revisor e Ponytail antes do RED.'
validation:
  - 'git diff --check'
  - 'Conferir logs RED e GREEN contra o diff Git da fixture.'
execution_prompt: |
  /GOAL
  Execute o trilho crg-m19-recorte-cli-20261116 na ordem das dependencias.
---

# crg-m19 — Recorte da CLI

Execução concluída. O YAML preserva o contrato validado no início do flow.

- [x] A-01 — RED executável: 4 falhas de recorte, 2 controles verdes.
- [x] A-02 — Wheel corrigido: 6/6 cenários em bancos novos.
- [x] A-03 — Suíte focada: 99/99. Diff revisado nos cinco chamadores.

[Provas RED, GREEN e suíte](../receipts/CRG-M19-20261116/INDEX.md).
