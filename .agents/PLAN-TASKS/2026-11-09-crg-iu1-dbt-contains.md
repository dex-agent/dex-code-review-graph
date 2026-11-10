---
dex_contract: spt
version: 3
status: 'CONCLUIDO_COM_RESSALVAS'
owner: 'sprinter'
date: '2026-11-09'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO integral do dono para o caso dbt recomendado no handoff de crg-iu1'
goal:
  id: 'crg-iu1-dbt-contains-20261109'
  title: 'Identidade da aresta CONTAINS no dbt'
  objective: 'Distinguir e corrigir a expectativa não portátil de CONTAINS no teste dbt com prova de identidade no SQLite'
context: 'A suíte Windows tem quatro IDs conhecidos. O primeiro é test_contains_edge.'
problem: 'O teste espera uma string POSIX em um caminho formatado pelo sistema anfitrião.'
decision: 'Preservar o RED e verificar os endpoints pela CLI e SQLite antes de corrigir a expectativa.'
scope:
  include:
    - 'Fixture dbt, resolução da aresta em índice descartável, seleção dbt na CI Windows e fechamento.'
  exclude:
    - 'Outros três IDs históricos, reforma transversal de IDs e índice persistente habitual.'
requirements:
  - id: REQ-01
    statement: 'Preservar a diferença Windows e Ubuntu antes da edição'
    criteria:
      - id: C-01
        statement: 'O recibo do baseline distingue a expectativa literal do vínculo exato no SQLite'
  - id: REQ-02
    statement: 'Usar a representação nativa para verificar os endpoints dbt'
    criteria:
      - id: C-02
        statement: 'O módulo dbt passa nos dois sistemas com verificação do destino persistido'
  - id: REQ-03
    statement: 'Provar a cobertura Windows na CI publicada'
    criteria:
      - id: C-03
        statement: 'A CI do SHA publicado aprova a matriz com o módulo dbt no runner Windows'
  - id: REQ-04
    statement: 'Fechar o corte com provas recuperáveis'
    criteria:
      - id: C-04
        statement: 'O recibo de fechamento confirma o checklist e os registros publicados'
plan:
  - 'Caracterizar a aresta no baseline'
  - 'Corrigir a expectativa dbt'
  - 'Validar o SHA publicado'
  - 'Reconciliar continuidade'
tasks:
  - id: A-01
    action: 'Caracterizar a aresta no baseline'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Executar pytest tests/test_dbt_parser.py nos dois sistemas e conferir o vínculo File para Class no banco criado pela CLI descartável.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Corrigir a expectativa dbt'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Executar pytest tests/test_dbt_parser.py em Windows e Ubuntu após a edição. Confirmar que o teste consulta o destino persistido.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Validar o SHA publicado'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Conferir gh run view pelo SHA, o log do módulo Windows e a diferença de falhas locais por ID.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Reconciliar continuidade'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Conferir checklist, memória, bead, continuidade e hashes no workspace. Registrar veredito e checkout.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Checklist completo, veredito PPIRTV, continuidade, Git e Dolt publicados.'
risks:
  - 'Normalizar texto no teste pode esconder referência órfã. Confronte os IDs exatos de aresta e nós.'
uncertainties:
  - 'A prova isolada distingue falha de apresentação de inconsistência de grafo.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'pytest tests/test_dbt_parser.py; leitura SQLite em modo ro; gh run view pelo SHA.'
execution_prompt: |
  /GOAL
  Execute .agents/PLAN-TASKS/2026-11-09-crg-iu1-dbt-contains.md em C:\CodexProjetos\code-review-graph até o veredito.
---

# Identidade da aresta CONTAINS no dbt

Tipo: SPEC-PLAN-TASKs

Owner mantenedor CRG. Oráculo Refatoração comanda o recorte. Chato verifica se a prova detecta uma aresta órfã. Ponytail fiscaliza o diff. Vigia ON confere o limite do corte. Fonte dos quality_gates: ppirtv-workflow/PATTERNS.md e receita local de manutenção iterativa.

## SPEC

- Fixar a diferença do baseline com teste Windows e Ubuntu antes da edição.
- Validar aresta, nó arquivo e nó modelo por IDs exatos no banco produzido pelo executável instalado.
- Se o produto estiver coerente, limitar o diff ao teste dbt e à cobertura Windows. Se a prova refutar isso, devolver ao planejamento com a evidência.

## PLAN

A-01 discrimina a causa, A-02 corrige o teste, A-03 verifica a publicação e A-04 reconcilia o estado vivo. Rollback por revert do commit de teste/CI.

## Checklist visual

- [x] A-01 [AÇÃO] Caracterizar a aresta no baseline | owner: mantenedor CRG | when: após goal_start | evidence: [Windows](../receipts/crg-iu1-dbt-contains/baseline-windows.json), [Ubuntu](../receipts/crg-iu1-dbt-contains/baseline-ubuntu.json), `evd_20261110001009022_0516_0011` | source: crg-iu1
- [x] A-02 [AÇÃO] Corrigir a expectativa dbt | owner: mantenedor CRG | when: após A-01 | evidence: [Windows](../receipts/crg-iu1-dbt-contains/green-windows.xml), [Ubuntu](../receipts/crg-iu1-dbt-contains/green-ubuntu.xml), `evd_20261110001014807_0517_0013` | source: crg-iu1
- [x] A-03 [AÇÃO] Validar o SHA publicado | owner: mantenedor CRG | when: após A-02 | evidence: [CI](../receipts/crg-iu1-dbt-contains/ci.json), [Windows 9/9 dbt](../receipts/crg-iu1-dbt-contains/ci-windows-dbt.txt), `evd_20261110001555200_0529_0028` | source: crg-iu1
- [x] A-04 [AÇÃO] Reconciliar continuidade | owner: mantenedor CRG | when: após A-03 | evidence: [conferência do fechamento](../receipts/crg-iu1-dbt-contains/handoff.json), [veredito](../receipts/crg-iu1-dbt-contains/verdict.json) | source: crg-iu1

## Revisão de entrada

Preflight com zero achados, SPT v3 válido e elegível. `runtime_semantics_scope: static_referential_integrity`. `causal_semantics_reviewed: true`. `goal_start_readiness: ready`. Revisão A–E apta, sem achado bloqueante.

- A-01 → REQ-01 → C-01 → ER-01. Pytest produz o resultado do baseline. Um leitor SQLite separado comprova os dois endpoints da aresta. O recibo só é aceito se ambas as observações forem obtidas.
- A-02 → REQ-02 → C-02 → ER-02. Pytest executa a fixture corrigida nos dois sistemas. A fixture usa o caminho nativo de entrada e resolve o destino persistido pelo ID bruto da aresta.
- A-03 → REQ-03 → C-03 → ER-03. Git fornece o SHA publicado, Actions fornece o resultado e o JUnit identifica cada falha. A CI prova cobertura da fixture apenas se o log Windows mostrar o módulo executado.
- A-04 → REQ-04 → C-04 → ER-04. O executor confere os artefatos e o bead reaberto após o push, registra seus hashes e só então chama o veredito. O checkout confirma o estado terminal.

Chato e Vigia: um teste que troca separadores dos dois lados pode esconder uma aresta órfã. Compare a identidade exata e aponte para o nó existente. Se o baseline provar isso, a camada de produção fica fora do recorte.

Oráculo, edição ptbr-2019-2ed. A rota `refactoring-fowler-rich/chapters/04-testes.md` sugeriu caracterização para a expectativa frágil. O capítulo 1, seção Primeiro passo na refatoração, confirma a necessidade de testes automatizados antes da mudança. A página 25 do PDF foi reaberta, a partir da extração `range_0001_0060.md`. PDF SHA-256 `2e85bb71faa1e7865720042317b918e38c2acc1f63540ca52ae6756d5ab0ac79`. A decisão sobre a identidade dbt depende da prova do CRG.

## Fechamento

Flow `flow_20261110000815041_0508_0001`. Windows falhava apenas na expectativa POSIX do teste dbt. CLI e SQLite confirmaram a aresta com os dois nós existentes antes da alteração. `b02a4ba` ajustou a fixture, a verificação do vínculo persistido e a seleção Windows. O módulo passou 9/9 em cada sistema e a CI passou 9/9 jobs. A suíte Windows integral perdeu um ID e mantém três históricos, sem IDs novos.

Mapas históricos, memória validada L1↔L2 e bead atualizado no Dolt. Antes do próximo release Windows, o mantenedor retoma pelo caso HCL com a comparação dos IDs brutos das referências.

