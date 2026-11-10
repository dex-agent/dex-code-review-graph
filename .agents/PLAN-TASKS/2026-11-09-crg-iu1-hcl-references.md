---
dex_contract: spt
version: 3
status: 'CONCLUIDO_COM_RESSALVAS'
owner: 'sprinter'
date: '2026-11-09'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO integral do dono para o próximo corte do crg-iu1'
goal:
  id: 'crg-iu1-hcl-references-20261109'
  title: 'Referências HCL com caminhos nativos'
  objective: 'Corrigir a expectativa nativa do teste HCL e provar a cobertura Windows sem alterar a identidade das arestas'
context: 'O corte dbt encerrou com três IDs históricos na suíte Windows. HCL é o primeiro.'
problem: 'O filtro de origem do teste HCL usa literal POSIX e devolve conjunto vazio no Windows.'
decision: 'Preservar a identidade nativa e ajustar a expectativa somente após provar os endpoints.'
scope:
  include:
    - 'Teste HCL, CI Windows, prova em SQLite descartável e fechamento.'
  exclude:
    - 'Parser de produção, índice habitual, Spring e uninstall.'
requirements:
  - id: REQ-01
    statement: 'Discriminar a causa no baseline'
    criteria:
      - id: C-01
        statement: 'O recibo basal distingue falha da expectativa Windows de ausência de referências'
  - id: REQ-02
    statement: 'Usar o Path da fixture para a identidade esperada'
    criteria:
      - id: C-02
        statement: 'O módulo HCL passa nos dois sistemas com o conjunto exato de referências'
  - id: REQ-03
    statement: 'Provar seleção Windows e saldo de regressão'
    criteria:
      - id: C-03
        statement: 'O SHA publicado passa na CI com execução explícita do módulo HCL no Windows'
  - id: REQ-04
    statement: 'Vincular artefatos e estado do projeto'
    criteria:
      - id: C-04
        statement: 'O recibo de fechamento confirma checklist completo e continuidade publicada'
plan:
  - 'Preservar o RED HCL'
  - 'Corrigir a expectativa e incluir HCL na CI'
  - 'Verificar o SHA publicado'
  - 'Fechar o corte e a continuidade'
tasks:
  - id: A-01
    action: 'Preservar o RED HCL'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Rodar pytest tests/test_hcl_parser.py em Windows e Ubuntu. Executar a CLI em projeto descartável e conferir a junção de origem e destino no SQLite pelos IDs brutos.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Corrigir a expectativa e incluir HCL na CI'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Rodar pytest tests/test_hcl_parser.py em Windows e Ubuntu após a edição. Conferir git diff e ruff.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Verificar o SHA publicado'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Conferir gh run view pelo SHA e o log do passo HCL. Comparar IDs da suíte integral Windows com o baseline dbt.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Fechar o corte e a continuidade'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Conferir checklist-lint, preflight, mapas, bead e referências. Registrar veredito e checkout.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Checklist 4/4, Git e Dolt publicados, mapas reconciliados, veredito oficial e checkout.'
risks:
  - 'Normalizar as duas pontas pode ocultar uma aresta órfã. Exigir igualdade de IDs originais.'
uncertainties:
  - 'Confirmar saldo da suíte Windows e seleção real da CI no SHA corrigido.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'pytest tests/test_hcl_parser.py, CLI build descartável, SQLite somente leitura, ruff e gh run view.'
execution_prompt: |
  /GOAL
  Execute .agents/PLAN-TASKS/2026-11-09-crg-iu1-hcl-references.md em C:\CodexProjetos\code-review-graph até o veredito.
---

# Referências HCL com caminhos nativos

Tipo: SPEC-PLAN-TASKs

Owner mantenedor CRG. Oráculo Clean Code no comando, Sprinter no planejamento, Clara na projeção, Chato e Vigia na fiscalização e Ponytail no escopo. Fonte dos quality_gates: ppirtv-workflow/PATTERNS.md, ppirtv-flow-base e receita local de manutenção iterativa.

## SPEC

- Preservar o RED e usar a mesma entrada no parser e no executável.
- Verificar os dois vínculos de `local.selected` pelos IDs exatos em cada SQLite, sem normalização dos endpoints.
- Derivar a expectativa do `Path` da fixture e incluir o módulo no job Windows. Reverter o commit de teste e CI se necessário.

## Checklist visual

- [x] A-01 [AÇÃO] Preservar o RED HCL | owner: mantenedor CRG | when: após goal_start | evidence: [RED](../receipts/crg-iu1-hcl-references/red-windows.txt), [SQLite Windows](../receipts/crg-iu1-hcl-references/baseline-windows.json), [SQLite Ubuntu](../receipts/crg-iu1-hcl-references/baseline-ubuntu.json), `evd_20261110002527733_0544_0047` | source: crg-iu1
- [x] A-02 [AÇÃO] Corrigir a expectativa e incluir HCL na CI | owner: mantenedor CRG | when: após A-01 | evidence: [Windows](../receipts/crg-iu1-hcl-references/green-windows.xml), [Ubuntu](../receipts/crg-iu1-hcl-references/green-ubuntu.xml), `evd_20261110002559240_0545_0049` | source: crg-iu1
- [x] A-03 [AÇÃO] Verificar o SHA publicado | owner: mantenedor CRG | when: após A-02 | evidence: [CI](../receipts/crg-iu1-hcl-references/ci.json), [HCL Windows](../receipts/crg-iu1-hcl-references/ci-windows-hcl.txt), [saldo por ID](../receipts/crg-iu1-hcl-references/comparison.json), `evd_20261110003055798_0557_0064` | source: crg-iu1
- [x] A-04 [AÇÃO] Fechar o corte e a continuidade | owner: mantenedor CRG | when: após A-03 | evidence: [handoff](../receipts/crg-iu1-hcl-references/handoff.json), [veredito](../receipts/crg-iu1-hcl-references/verdict.json) | source: crg-iu1

## Revisão antes do GOAL

Estrutura v3 passou com zero achados. `runtime_semantics_scope: static_referential_integrity`. `structural_status: pass`. `causal_semantics_reviewed: true`. `semantic_status: pass`. `goal_start_readiness: ready`.

- A-01 → REQ-01 → C-01 → ER-01. O pytest registra o ID que falha, e a sonda reproduz o filtro antigo e o vínculo bruto em um banco criado pela CLI. Exit 0 do conjunto significa RED esperado e dois endpoints resolvidos em cada ambiente, sem confundir a falha esperada com erro de execução.
- A-02 → REQ-02 → C-02 → ER-02. Os dois JUnit observam a igualdade exata do conjunto e os controles do módulo. O diff e o lint verificam o recorte.
- A-03 → REQ-03 → C-03 → ER-03. O Git fornece o SHA, Actions confirma a seleção e o resultado Windows, e a diferença do JUnit integral identifica cada falha.
- A-04 → REQ-04 → C-04 → ER-04. O executor confere contagem, hashes, bead após Dolt e mapas. A prova antecede o veredito, e o checkout confirma a transição terminal.

Revisão A–E apta. O path canônico e o índice existem, os vínculos não têm órfãos, os critérios separam os ambientes, as fontes de prova são reproduzíveis e os comandos não dependem da consulta `references_to` na CLI. Chato: se houver uma aresta extra, a igualdade do conjunto deve falhar. Ponytail: usar o `Path` já existente na fixture, sem helper. Vigia: a evidência da execução, e não a plataforma por si, determina o escopo.

Oráculo: superfície promovida `clean-code`, rota `CC-TESTE-LIMPO`. Confirmado documental em Clean Code, en-2008, “Clean Tests”, p. 124, e T5, p. 314, páginas 155 e 345 do PDF preservado. SHA-256 `61949fc2bc46431fb6cc7a71a472ce4dbfbcec7a2277f538e8d7ae9722c5618e`. A evidência da fixture decide a aplicação local.

## Fechamento

Fluxo `flow_20261110002445162_0537_0039`. Produto `d6336d2` publicado. CI 9/9, com 3/3 HCL no runner Windows. A suíte integral Windows perdeu apenas o ID HCL, sem introduzir IDs de falha. A investigação usou índices descartáveis.

Bead `crg-iu1` publicado no Dolt e mantido em andamento pelos casos Spring e uninstall. Antes do próximo release Windows, o mantenedor reproduz o caso Spring nos dois sistemas e compara os endpoints `CALLS` no SQLite, com zero ligações cruzadas.

