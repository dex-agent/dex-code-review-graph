---
dex_contract: spt
version: 3
status: 'CONCLUIDO_COM_RESSALVAS'
owner: 'sprinter'
date: '2026-11-09'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO do dono para executar o corte forget do crg-iu1'
goal:
  id: 'crg-iu1-forget-20261109'
  title: 'Seleção exata do forget no Windows'
  objective: 'Corrigir a seleção de pasta literal no forget e comprovar a remoção exata na CLI, no SQLite e na CI Windows e Ubuntu'
context: 'O corte Julia deixou oito falhas Windows, três de fixtures do forget. A CLI já reproduziu uma falha separada de produto.'
problem: 'Uma grafia equivalente da pasta no Windows pode deixar todo o alvo no SQLite.'
decision: 'Preservar o RED público, portar fixtures, corrigir a seleção literal e publicar a regressão na CI existente.'
scope:
  include:
    - 'Matcher forget, fixtures e regressão, job CI Windows, recibos, Trilho, mapas e continuidade.'
  exclude:
    - 'Índice persistente, refatoração da remoção, mudança do contrato de glob, correções dos outros cinco IDs.'
requirements:
  - id: REQ-01
    statement: 'Preservar o RED de produto'
    criteria:
      - id: C-01
        statement: 'O recibo RED registra zero alvos na CLI com PKG apontando para pkg'
  - id: REQ-02
    statement: 'Portar as três fixtures'
    criteria:
      - id: C-02
        statement: 'Os três testes de caminhos nativos passam antes da correção do seletor'
  - id: REQ-03
    statement: 'Corrigir e revisar a seleção de pasta literal'
    criteria:
      - id: C-03
        statement: 'A prova pública da seleção exata passa no executável'
  - id: REQ-04
    statement: 'Validar CI publicada no SHA de produto'
    criteria:
      - id: C-04
        statement: 'A CI do SHA corrigido comprova o módulo em Windows e Ubuntu'
  - id: REQ-05
    statement: 'Registrar saldo e continuidade'
    criteria:
      - id: C-05
        statement: 'O registro de fechamento do corte é recuperável pelo bead'
plan:
  - 'RED público, fixtures nativas, correção e revisão, prova na CI, continuidade e veredito.'
tasks:
  - id: A-01
    action: 'Preservar o RED de produto'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Executar o caso público com a CLI anterior e validar o recibo contra o conjunto de quatro arquivos no SQLite.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Portar as três fixtures'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Rodar pytest para os três IDs de seleção, preservando o RED de produto.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Corrigir e revisar a seleção de pasta literal'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Rodar o caso público com a CLI corrigida, verificando dry-run, remoção SQLite, pasta vizinha, fontes no disco e contraprova de pastas distintas.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Validar CI publicada no SHA de produto'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Publicar no remoto privado e observar os jobs por SHA, com evidência da execução de test_forget.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-05
    action: 'Registrar saldo e continuidade'
    covers: [REQ-05]
    done_when: [C-05]
    depends_on: [A-04]
    evidence_requirements:
      - id: ER-05
        proves: [C-05]
        method: command
        procedure: 'Conferir checklist, mapas, estado vivo, saldo e referências no Trilho antes do veredito.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Checklist visual integral, veredito oficial, Git e Dolt publicados e estado vivo atualizado.'
risks:
  - 'Uma comparação cega por caixa pode remover pastas distintas. Preservar identidade do filesystem e chaves SQLite.'
uncertainties:
  - 'As conclusões da CI e o saldo Windows serão medidos no SHA publicado.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'Executável forget, SQLite, pytest, ruff, git diff --check e leitura dos jobs GitHub por SHA.'
execution_prompt: |
  /GOAL
  Execute .agents/PLAN-TASKS/2026-11-09-crg-iu1-forget.md no workspace C:\CodexProjetos\code-review-graph até o veredito.
---

# Seleção exata do forget no Windows

Tipo: SPEC-PLAN-TASKs

Aplicar Pragmático e Oráculo Clean Code. Fiscal vivo: Chato com Investigador Socrático e Dex Anti-Autossabotagem em VIGIA ON. Dono técnico: mantenedor CRG.

## Checklist visual

- [x] A-01 Preservar o RED de produto · [CLI e SQLite](../receipts/crg-iu1-forget/red.json) · `evd_20261109210628203_0454_0009`
- [x] A-02 Portar as três fixtures · [Pytest](../receipts/crg-iu1-forget/fixtures.xml) · `9e431bc` · `evd_20261109210628255_0455_0011`
- [x] A-03 Corrigir e revisar a seleção de pasta literal · [Windows](../receipts/crg-iu1-forget/green-windows.json) · [Ubuntu](../receipts/crg-iu1-forget/green-ubuntu.json) · `aca7f74` · `evd_20261109210653231_0456_0013`
- [x] A-04 Validar CI publicada no SHA de produto · [Run 42699224753](https://github.com/dex-agent/dex-code-review-graph/actions/runs/42699224753) · [Saldo por ID](../receipts/crg-iu1-forget/comparison.json) · `evd_20261109211041245_0467_0027`
- [x] A-05 Registrar saldo e continuidade · [Mapas](../MAPAS/INDEX.md) · `bd show crg-iu1` · [Validação da memória](../receipts/crg-iu1-forget/memory-validation.json)

## Validação e retomada

Preflight sem achados, SPT v3 elegível e revisão causal apta. A prova de cada task vem do executável, do Pytest, da CI ou da conferência do estado persistido conforme a cadeia de requisitos acima. Flow `flow_20261109210335862_0447_0001`.

O acesso à CI foi confirmado pelo Gerenciador de Credenciais do Git. O run anterior em `6d1c5df` registrou `KeyboardInterrupt` no Ubuntu 3.13. O SHA de produto passou nos nove jobs. O teste de identidade confirmou a preservação de `pkg_extra` e de `pkg` quando `PKG` é outra pasta.

O saldo integral do Windows caiu de oito para cinco IDs, sem novos. O mantenedor do CRG retoma `test_explicit_repo_without_markers_errors_cleanly` antes do próximo release Windows. [Recibo de veredito](../receipts/crg-iu1-forget/verdict.json).

