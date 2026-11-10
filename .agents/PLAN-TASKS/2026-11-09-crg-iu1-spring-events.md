---
dex_contract: spt
version: 3
status: 'CONCLUIDO_COM_RESSALVAS'
owner: 'sprinter'
date: '2026-11-09'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO integral do dono sobre a recomendação do Oráculo Pragmático para Spring'
goal:
  id: 'crg-iu1-spring-events-20261109'
  title: 'Pares exatos de eventos Spring na CI Windows'
  objective: 'Provar os dois pares Spring pelos endpoints nativos e eliminar o falso RED Windows com cobertura na CI'
context: 'crg-iu1 segue em andamento após o corte HCL, com Spring e uninstall no saldo Windows.'
problem: 'A asserção de Spring filtra separadores POSIX e aceita dois pares internos ao mesmo pacote.'
decision: 'Preservar o RED, provar os endpoints via executável e exigir os dois pares exatos usando os Paths já disponíveis.'
scope:
  include:
    - 'Fixture Spring, seleção CI Windows, provas locais descartáveis, mapas e continuidade.'
  exclude:
    - 'Resolvedor de produção, índice habitual e correção do caso uninstall.'
requirements:
  - id: REQ-01
    statement: 'Preservar o RED e provar a causa pela CLI'
    criteria:
      - id: C-01
        statement: 'O recibo basal distingue falha de representação de aresta incorreta'
  - id: REQ-02
    statement: 'Fortalecer a asserção Spring e selecionar o módulo na CI'
    criteria:
      - id: C-02
        statement: 'O módulo verifica os pares exatos e passa localmente nas duas plataformas'
  - id: REQ-03
    statement: 'Provar CI no SHA publicado e comparar falhas Windows'
    criteria:
      - id: C-03
        statement: 'O recibo de publicação confirma o passo Spring Windows e que saiu somente o ID Spring'
  - id: REQ-04
    statement: 'Fechar o Trilho e publicar a continuidade'
    criteria:
      - id: C-04
        statement: 'O recibo de fechamento confere as quatro saídas e a atualização de mapas e bead'
plan:
  - 'Preservar o RED e provar a causa pela CLI'
  - 'Fortalecer a asserção Spring e selecionar o módulo na CI'
  - 'Provar CI no SHA publicado e comparar falhas Windows'
  - 'Fechar o Trilho e publicar a continuidade'
tasks:
  - id: A-01
    action: 'Preservar o RED e provar a causa pela CLI'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Rodar python -B -m pytest -p no:cacheprovider tests/test_spring_events.py em Windows e Ubuntu e preservar JUnit. Rodar code-review-graph build em dois projetos descartáveis com a fixture existente e conferir pares e nós por LEFT JOIN bruto no SQLite.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Fortalecer a asserção Spring e selecionar o módulo na CI'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Derivar as duas expectativas dos Paths retornados pela fixture. Rodar pytest tests/test_spring_events.py nos dois sistemas, provar rejeição de par cruzado e de par faltante com dois registros e conferir git diff --check e ruff.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Provar CI no SHA publicado e comparar falhas Windows'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Executar a suíte integral Windows com JUnit. Comparar IDs com crg-iu1-hcl-references/comparison.json e conferir gh run view e gh run view --log por SHA, com execução nominal do caso Spring.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Fechar o Trilho e publicar a continuidade'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Rodar preflight e checklist-lint, validar mapas e referências, publicar e reler o bead Dolt, registrar veredito oficial e checkout. Publicar os registros do fechamento no Git.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Checklist 4/4 com provas, veredito oficial e checkout terminal, Git e Dolt publicados.'
risks:
  - 'Contagem correta com pacote errado pode passar. Verificar conjunto exato e manter contagem.'
  - 'Matriz verde sem execução nominal não prova cobertura Windows.'
uncertainties:
  - 'A paridade basal Ubuntu e o saldo integral após o corte ainda precisam de execução.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'pytest, executável CRG, SQLite read-only, ruff, git diff --check e GitHub Actions.'
execution_prompt: |
  /GOAL
  Execute .agents/PLAN-TASKS/2026-11-09-crg-iu1-spring-events.md em C:\CodexProjetos\code-review-graph até o veredito.
---

# Pares exatos de eventos Spring na CI Windows

Tipo: SPEC-PLAN-TASKs

Oráculo Pragmático no comando. Sprinter ordena, Clara projeta, Chato e Vigia fiscalizam, Ponytail controla o recorte e o mantenedor executa. Fonte dos quality_gates: ppirtv-workflow/PATTERNS.md, ppirtv-flow-base e receita local de manutenção iterativa. Origem factual: checkout `2604aed`, teste Spring e saldo HCL. Definição de pronto: quatro provas, CI Windows nominal, zero novos IDs, checkout terminal e publicação.

## SPEC

Pares esperados: Publisher.publish de alpha para Listener.on de alpha, e o mesmo para beta. Zero cruzamentos e zero pontas órfãs. O parser e o SQLite mantêm a identidade nativa. Se a prova basal revelar aresta errada, devolver ao Sprinter com a testemunha antes de editar.

## Checklist visual

- [x] A-01 [AÇÃO] Preservar o RED e provar a causa pela CLI | owner: mantenedor CRG | when: após goal_start | evidence: [RED](../receipts/crg-iu1-spring-events/red-windows.xml), [Ubuntu](../receipts/crg-iu1-spring-events/baseline-ubuntu.xml), [SQLite Windows](../receipts/crg-iu1-spring-events/baseline-windows.json), [SQLite Ubuntu](../receipts/crg-iu1-spring-events/baseline-ubuntu.json), `evd_20261110003942120_0572_0083` | source: crg-iu1
- [x] A-02 [AÇÃO] Fortalecer a asserção Spring e selecionar o módulo na CI | owner: mantenedor CRG | when: após A-01 | evidence: [Windows](../receipts/crg-iu1-spring-events/green-windows.xml), [Ubuntu](../receipts/crg-iu1-spring-events/green-ubuntu.xml), [controles negativos](../receipts/crg-iu1-spring-events/negative.json), `evd_20261110004030369_0573_0085` | source: crg-iu1
- [x] A-03 [AÇÃO] Provar CI no SHA publicado e comparar falhas Windows | owner: mantenedor CRG | when: após A-02 | evidence: [CI](../receipts/crg-iu1-spring-events/ci.json), [log Windows](../receipts/crg-iu1-spring-events/ci-windows-spring.txt), [saldo por ID](../receipts/crg-iu1-spring-events/comparison.json), `evd_20261110004555772_0587_0103` | source: crg-iu1
- [x] A-04 [AÇÃO] Fechar o Trilho e publicar a continuidade | owner: mantenedor CRG | when: após A-03 | evidence: [handoff](../receipts/crg-iu1-spring-events/handoff.json), [mapas](../MAPAS/INDEX.md) | source: crg-iu1

## Continuidade

Uninstall segue em crg-iu1, com o mantenedor antes do próximo release Windows. Reusar o gatilho CRG-ARESTA-ENDPOINTS-EXATOS. Hunt e Thomas, O Programador Pragmático, tradução Bookman 2010 da primeira edição, páginas 27, 259 e 264 do PDF, sustenta manter a regressão executável e automatizada.

## Revisão causal e lapidação antes do GOAL

- A-01 → REQ-01 → C-01 → ER-01. O mantenedor observa um RED nominal no JUnit Windows, o GREEN basal do Ubuntu e dois vínculos completos em cada SQLite. O exit do discriminador exige os três resultados, inclusive o RED esperado.
- A-02 → REQ-02 → C-02 → ER-02. Os dois pytest verificam o contrato editado. Uma mutação em memória injeta cruzamento ou repete o par alpha com duas linhas e deve falhar na comparação exata.
- A-03 → REQ-03 → C-03 → ER-03. Git determina o SHA. O log do runner confirma seleção e resultado, e os JUnit determinam o delta integral por ID.
- A-04 → REQ-04 → C-04 → ER-04. O readback do bead, dos mapas e dos quatro itens antecede o veredito. O checkout terminal e a publicação do recibo são gates de fechamento, sem depender do próprio veredito para produzir a prova A-04.

Revisão A–E apta. Estrutura v3, vínculos completos, critérios observáveis, produtores disponíveis e rota de reprodução conferida. Chato: dois registros do mesmo pacote e pontas órfãs precisam falhar. Ponytail: manter apenas o teste existente e um passo CI como diff de produto. Vigia: a prova parte de uma fixture isolada e não presume a paridade.

`runtime_semantics_scope: static_referential_integrity`, `structural_status: pass`, `causal_semantics_reviewed: true`, `semantic_status: pass`, `goal_start_readiness: ready`.

## Fechamento

Fluxo `flow_20261110003814125_0565_0075`. Produto `d22e6d6` publicado no remoto privado, CI 9/9 e módulo Spring 6/6 no runner Windows. Windows integral 2 → 1 IDs de falha, zero novos. Os índices SQLite usados na prova são descartáveis.

O bead `crg-iu1` segue em andamento e publicado no Dolt. Antes do release Windows, o mantenedor mede o modo efetivo de uma configuração descartável antes e depois do uninstall nos dois sistemas. A `.venv` Windows foi recriada pelo lockfile após o uv do WSL substituir o ambiente compartilhado. [Memória validada do isolamento](../memorias/crg-uv-wsl-venv-isolado.md). [Veredito oficial](../receipts/crg-iu1-spring-events/verdict.json).
