---
dex_contract: spt
version: 3
status: 'CONCLUIDO_COM_RESSALVAS'
owner: 'sprinter'
date: '2026-11-09'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO integral do dono para a recomendação da raiz externa em crg-iu1'
goal:
  id: 'crg-iu1-raiz-externa-20261109'
  title: 'Identidade da raiz com índice externo'
  objective: 'Alinhar build e search na identidade da raiz de projeto sem VCS com índice externo'
context: 'A CLI reconhece build sem VCS local e com Git externo, porém o caso combinado falha. Um teste negativo herdado encontra marcador real no ancestral da fixture.'
problem: 'A localização de armazenamento participa acidentalmente do reconhecimento da raiz.'
decision: 'Reusar o vínculo exato persistido de data-dir no reconhecimento de raiz e isolar a fixture.'
scope:
  include:
    - 'Resolvedor explícito, validador compartilhado, fixtures, CI, mapas e fechamento do corte.'
  exclude:
    - 'Índice persistente, novas flags, outras famílias Windows, migração de storage e comportamento automático sem --repo.'
requirements:
  - id: REQ-01
    statement: 'Preservar o RED de produto'
    criteria:
      - id: C-01
        statement: 'A prova de baseline identifica zero arquivos no índice externo do projeto sem VCS'
  - id: REQ-02
    statement: 'Isolar a fixture herdada'
    criteria:
      - id: C-02
        statement: 'A classe de resolução explícita passa com a fixture isolada antes do fix produtivo'
  - id: REQ-03
    statement: 'Corrigir a regra comum de raiz'
    criteria:
      - id: C-03
        statement: 'O executável retorna o símbolo do projeto sem VCS registrado com índice externo'
  - id: REQ-04
    statement: 'Validar a CI do SHA publicado'
    criteria:
      - id: C-04
        statement: 'A execução de CI do SHA corrigido demonstra os controles de raiz em Windows e Ubuntu'
  - id: REQ-05
    statement: 'Reconciliar continuidade e fechamento'
    criteria:
      - id: C-05
        statement: 'O handoff recupera o saldo do corte com evidências vinculadas'
plan:
  - 'Preservar RED, isolar fixture, corrigir e revisar, provar CI e suite, fechar continuidade.'
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
        procedure: 'Rodar a prova do executável com expectativa red e inspecionar a contagem SQLite no banco isolado.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Isolar a fixture herdada'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Rodar pytest tests/test_cli.py::TestGraphToolExplicitRepoResolution e guardar JUnit.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Corrigir a regra comum de raiz'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Rodar a prova green com dois projetos distintos e conferir os arquivos no SQLite, a busca, o controle sem raiz e o monorepo.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Validar a CI do SHA publicado'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Publicar a revisão privada, conferir os jobs GitHub por SHA e comparar os IDs da suíte Windows com o corte forget.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-05
    action: 'Reconciliar continuidade e fechamento'
    covers: [REQ-05]
    done_when: [C-05]
    depends_on: [A-04]
    evidence_requirements:
      - id: ER-05
        proves: [C-05]
        method: command
        procedure: 'Conferir checklist, mapas, continuidade, bead e referências para registrar o veredito.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Checklist 5/5, goal_verdict, checkout, memória revisada, mapas, Git e Dolt publicados.'
risks:
  - 'Um data-dir global não autoriza uma raiz arbitrária. Exigir vínculo exato registrado e preservar marcadores ancestrais legítimos.'
uncertainties:
  - 'O saldo de regressão e a CI serão medidos no SHA publicado.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'Prova CLI e SQLite, pytest, ruff, git diff --check e gh run view no SHA.'
execution_prompt: |
  /GOAL
  Execute .agents/PLAN-TASKS/2026-11-09-crg-iu1-raiz-externa.md no workspace C:\CodexProjetos\code-review-graph até o veredito.
---

# Identidade da raiz com índice externo

Tipo: SPEC-PLAN-TASKs

Owner mantenedor CRG. GO do dono. Ponytail comanda o menor diff, Chato fiscaliza a fronteira e Vigia confronta limites sem evidência. Fonte dos quality_gates: ppirtv-workflow/PATTERNS.md, ppirtv-flow-base e receita local de manutenção iterativa. Origem técnica: CRG-RAIZ-INDICE-EXTERNO.

## SPEC e ordem

A raiz registrada deve vencer pela identidade do caminho. Diretório de armazenamento global e marcador do sistema anfitrião não equivalem a registro exato do projeto. O controle de monorepo preserva a resolução mais próxima. Primeiro o RED, depois fixture, produto, CI e fechamento. Rollback por revert dos commits de produto, preservando o RED.

## Checklist visual

- [x] A-01 Preservar o RED de produto | owner: mantenedor CRG | [prova CLI/SQLite](../receipts/crg-iu1-raiz-externa/red.json) | `evd_20261109230030938_0481_0009`
- [x] A-02 Isolar a fixture herdada | owner: mantenedor CRG | [Pytest](../receipts/crg-iu1-raiz-externa/fixture.xml) | `d3664f7` | `evd_20261109230030998_0482_0011`
- [x] A-03 Corrigir a regra comum de raiz | owner: mantenedor CRG | [prova do executável e SQLite](../receipts/crg-iu1-raiz-externa/green.json) | `f145ca8` | `evd_20261109230756147_0495_0029`
- [x] A-04 Validar a CI do SHA publicado | owner: mantenedor CRG | [CI 9/9](../receipts/crg-iu1-raiz-externa/ci.json) | [Windows 5/5](../receipts/crg-iu1-raiz-externa/ci-windows-root.txt) | `61ff0da` | `evd_20261109231124476_0496_0031`
- [x] A-05 Reconciliar continuidade e fechamento | owner: mantenedor CRG | [continuidade e provas](../receipts/crg-iu1-raiz-externa/handoff.json) | [veredito oficial](../receipts/crg-iu1-raiz-externa/verdict.json)

## Validação prévia

Preflight sem achados e validação oficial v3 elegível. Integridade referencial do runtime é estática. As cinco cadeias foram revisadas em separado e a revisão A–E ficou apta antes do goal_start.

- A-01 usa os códigos de saída e o conteúdo SQLite, observados fora do processo da CLI.
- A-02 usa o JUnit anterior ao fix produtivo e o commit isolado.
- A-03 usa subprocessos com a entrada pública, um SQLite aberto em modo somente leitura e controles que distinguem pai e filho.
- A-04 usa o SHA publicado e os logs de jobs, além da diferença de IDs da suíte Windows.
- A-05 verifica os arquivos reabertos, seus hashes, o bead e os vínculos de memória antes do veredito.

Flow `flow_20261109225741604_0474_0001`.

## Fechamento

O RED de produto mostrou vínculo exato registrado, build e search com exit 1 e zero arquivos no SQLite. A correção `f145ca8` passou na CLI e no banco descartável. Na primeira CI Windows, o harness achou o executável no caminho errado. A varredura encontrou três ocorrências, corrigidas em `61ff0da` pelo diretório de scripts do próprio interpretador. A CI seguinte passou 9/9 e o Windows integral ficou com quatro falhas históricas, sem novos IDs.

O bead `crg-iu1` foi atualizado e publicado no Dolt. O mantenedor começa pelo teste de aresta `CONTAINS` do dbt antes do próximo release Windows. A memória do launcher foi validada de L1 a L2. Os mapas registram capacidades, decisões e relações do corte.

