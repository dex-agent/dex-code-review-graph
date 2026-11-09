---
dex_contract: spt
version: 3
status: CONCLUIDO
owner: sprinter
date: '2026-11-08'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'GO do dono para reconstruir e validar o índice persistente do CRG'
goal:
  id: crg-indice-persistente-20261108
  title: Reconstruir o índice persistente da CLI
  objective: Reconstruir o índice persistente com backup íntegro e confirmar a associação direta pelo executável corrigido.
context: 'CLI 04fcb05. O piloto isolado recuperou o teste. O status do índice persistente aponta para 268e0e1.'
problem: 'O banco ativo foi produzido antes da correção de reexportações Python.'
decision: 'Confirmar a rota do banco, usar backup SQLite consistente e executar build seguido de provas independentes de SHA e associação.'
scope:
  include:
    - 'Índice persistente do checkout, backup local, CLI corrigida, provas de SHA e associação, mapas e veredito.'
  exclude:
    - 'Alterações em código de produção, instalação global e regeneração de índices de outros projetos.'
requirements:
  - id: REQ-01
    statement: Preservar o estado anterior.
    criteria:
      - id: C-01
        statement: O snapshot SQLite do banco ativo passa integrity_check com a proveniência anterior preservada.
  - id: REQ-02
    statement: Reconstruir o banco ativo no corte vigente.
    criteria:
      - id: C-02
        statement: O SHA indexado no status da CLI coincide com o HEAD observado pelo Git.
  - id: REQ-03
    statement: Recuperar o teste pelo símbolo definido.
    criteria:
      - id: C-03
        statement: A CLI retorna a associação direta do teste exato para a definição de query_graph.
plan:
  - 'Confirmar banco ativo e produzir backup SQLite com hash e integridade.'
  - 'Executar build com a CLI corrigida e conferir o status JSON contra Git.'
  - 'Consultar o símbolo qualificado, validar o teste e registrar mapas e veredito.'
tasks:
  - id: A-01
    action: Produzir backup verificado
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: inspection
        procedure: 'Usar a API SQLite backup, abrir a cópia em modo somente leitura, conferir integrity_check, SHA256 e revisão anterior.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-02
    action: Reconstruir o índice persistente
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: inspection
        procedure: 'Rodar build pelo executável do checkout. Comparar built_at_commit e current_sha do status JSON com git rev-parse HEAD.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-03
    action: Verificar associação direta e atualizar mapas
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: inspection
        procedure: 'Consultar query tests_for pelo caminho qualificado. Exigir um resultado test_references_to_returns_type_dependents em tests/test_tools.py com indirect=false e conferir a aresta TESTED_BY em leitura SQLite.'
        expectation:
          kind: boolean_assertion
          expected: true
closure_gates:
  - 'Checklist 3/3, provas, revisão, veredito oficial e confirmação do índice no HEAD após publicação documental.'
risks:
  - 'Cópia de arquivo pode perder transações no WAL. Usar backup consistente da API SQLite.'
  - 'Um resultado com mesmo nome pode ser associação indireta. Conferir símbolo, arquivo, flag e aresta direta.'
uncertainties:
  - 'O ranking da CLI tem limite próprio. A prova exige o item exato visível no JSON.'
gates:
  - 'Preflight zero achados, spt_validate v3 elegível, revisão causal e SPT Revisor apto antes de goal_start.'
validation:
  - 'SQLite integrity_check, CLI build/status/query, Git HEAD, aresta direta e hash das fontes dos mapas.'
execution_prompt: |
  /GOAL Execute as três tasks deste Trilho em C:/CodexProjetos/code-review-graph.
---

# Reconstrução do índice persistente da CLI

Tipo: SPEC-PLAN-TASKs

## SPEC e PLAN

Owner mantenedor CRG. A CLI do checkout resolve o banco em
`.code-review-graph/graph.db`. Preservar uma cópia recuperável em
`.agents/BACKUPS/` antes de qualquer escrita no banco.
O corte anterior validou o código em índice isolado. Este corte aplica a
mesma prova ao banco ativo. [Trilho anterior](2026-11-08-crg-python-reexports.md)

## Checklist visual

- [x] A-01 [AÇÃO] Backup SQLite íntegro | owner: mantenedor CRG | when: antes do build | source: ER-01 | evidence: [backup](../receipts/crg-indice-persistente/backup.json), `evd_20261109003931553_0223_0145`
- [x] A-02 [AÇÃO] Build e SHA comprovados | owner: mantenedor CRG | when: após backup íntegro | source: ER-02 | evidence: [status](../receipts/crg-indice-persistente/proof-status.json), `evd_20261109004012011_0224_0147`
- [x] A-03 [AÇÃO] Teste direto no JSON e na aresta | owner: Validador | when: após conferir SHA | source: ER-03 | evidence: [associação](../receipts/crg-indice-persistente/proof-association.json), `evd_20261109004126237_0225_0149`

O Chato fiscaliza WAL, concorrência e identidade do teste. Ponytail usa o
executável e a consulta já existentes. Gate causal: A-01 observa cópia via
SQLite, A-02 compara dois produtores independentes (Git e CLI), A-03
cruza saída pública com aresta SQLite e arquivo exato. Os receipts ficam
fora do próprio banco. Revisão pré-execução: apto, escopo e dependências
lineares. runtime_semantics_scope=static_referential_integrity.
causal_semantics_reviewed=true; goal_start_readiness=ready.

## Resultados

- Bead `crg-5vr`. O snapshot do banco anterior preservou 5006 nós e 40981
  arestas e passou no integrity_check. O arquivo e o SHA estão no recibo.
- A CLI do checkout reconstruiu o mesmo banco em `04fcb05`. O status
  confirmou `built_at_commit == current_sha == git rev-parse HEAD`.
- A consulta qualificada devolveu uma ocorrência do teste em
  `tests/test_tools.py:330` com `indirect: false`. A chamada na linha 358
  está em uma aresta `TESTED_BY` da definição de `query_graph`.
- A CLI retornou 100 dos 121 resultados. O teste exato está entre os
  exibidos. O build usou detecção de comunidades por arquivo, conforme
  o fallback já disponível neste ambiente.
- Os [três mapas](../MAPAS/INDEX.md) preservam a primeira prova. Depois da
  publicação documental, a verificação do HEAD novo fica nos recibos
  locais `final-status.json` e `final-association.json`.

## Veredito

**Pronto com ressalvas**, `vrd_20261109004217604_0235_0161`. Flow
`flow_20261109003904048_0216_0137`, checklist 3/3, revisão `evd_20261109004207658_0230_0155`.
O backup permanece local. A prova cobre a associação direta e o SHA do
índice no checkout da CLI. O bead `crg-iu1` segue como o próximo corte do
mantenedor antes do próximo release Windows.
