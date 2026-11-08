---
dex_contract: spt
version: 3
status: CONCLUIDO
owner: sprinter
date: '2026-11-08'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'GO do dono para piloto da CLI em diff real de um arquivo'
goal:
  id: crg-cli-diff-real-20261108
  title: Validar a CLI em diff real de query.py
  objective: Atualizar um indice de teste, executar o recorte da CLI e reconciliar os simbolos do JSON com Git.
context: 'CLI da edicao Dex em bccd04a; piloto historico em 573580b.'
problem: 'A prova anterior usou fixtures; falta a comparacao ponta a ponta em um commit real.'
decision: 'Reusar o commit real de um arquivo e isolar o checkout e os dados do grafo.'
scope:
  include:
    - 'Checkout local do pai e do commit 573580b, build/update isolado, detect-changes --files, comparacao Git e tres mapas.'
  exclude:
    - 'Mudar implementacao, indice persistente ou instalacao global.'
requirements:
  - id: REQ-01
    statement: Fixar a revisao do indice de teste
    criteria:
      - id: C-01
        statement: O Git confirma um arquivo e status confirma indice isolado no pai antes e em 573580b depois do update.
  - id: REQ-02
    statement: Reconciliar o JSON com o diff de um arquivo
    criteria:
      - id: C-02
        statement: Cada simbolo retornado e esperado e classificado contra os hunks e a fonte, com omissoes e extras explicitados.
  - id: REQ-03
    statement: Preservar o resultado do piloto
    criteria:
      - id: C-03
        statement: Os tres mapas e a comparacao sao recuperaveis pelo Trilho e a revisao local preserva o indice original.
plan:
  - 'Criar clone local e indice proprio, medir build e update.'
  - 'Executar CLI e comparar JSON com Git e AST Python.'
  - 'Registrar evidencias, mapas, escopo e veredito.'
tasks:
  - id: A-01
    action: Construir e atualizar o indice isolado
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: inspection
        procedure: 'Conferir git diff --name-status, status --json antes e depois, base e alvo completos.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-02
    action: Executar e classificar cada simbolo
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: inspection
        procedure: 'Confrontar JSON bruto com o patch sem contexto e os intervalos AST da fonte do commit.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-03
    action: Registrar e conferir a evidencia do corte
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: inspection
        procedure: 'Abrir os tres mapas e conferir fontes, comparar SHA256 do indice original antes/depois e validar diff documental.'
        expectation:
          kind: boolean_assertion
          expected: true
closure_gates:
  - 'Checklist 3/3 com provas e verdict oficial.'
risks:
  - 'Indice no SHA errado pode devolver simbolos com linhas de outra revisao.'
  - 'Risco, fluxos e lacunas do grafo nao sao oracles de sobreposicao de hunks.'
uncertainties:
  - 'A conclusao e restrita a um diff Python e uma revisao do executavel.'
gates:
  - 'SPT v3 elegivel e revisao causal antes do goal_start.'
validation:
  - 'Build e update reais, JSON cru, Git/AST, tres mapas e diff check.'
execution_prompt: |
  /GOAL Execute todas as tasks deste Trilho em C:/CodexProjetos/code-review-graph.
---

# Piloto da CLI em diff real de um arquivo

Tipo: SPEC-PLAN-TASKs

## SPEC

Owner: mantenedor CRG. Bead `crg-r74`. Usar o executavel do checkout Dex
`bccd04a` contra clone isolado de `e84e86d` para `573580b`. Git confirmou
um arquivo, `code_review_graph/tools/query.py`. O grafo persistente reportou
um SHA historico e fica fora do oracle.

## PLAN

Build no pai, update no alvo, consultar pelo mesmo data dir. Conferir
HEAD, timestamp de fonte e geracao antes de consumir o derivado. Usar Git
sem contexto e AST da fonte para fazer a lista esperada; registrar acertos,
omissoes e extras mesmo se houver divergencia. Clone e SQLite em TEMP.

## TASKs

- [x] A-01 — build, update e proveniência. [Receipt](../receipts/crg-cli-diff-real/index.json), `evd_20261108192444197_0167_0075`.
- [x] A-02 — CLI, Git e comparação símbolo a símbolo. [Comparação](../receipts/crg-cli-diff-real/comparison.json), `evd_20261108192720431_0168_0077`.
- [x] A-03 — três mapas e hash do índice original conferidos. [Mapas](../MAPAS/INDEX.md), `evd_20261108192936708_0169_0079`.

## Riscos e validacao

Chato: e se a CLI resolver outro banco? CRG_DATA_DIR e CRG_HOME exclusivos,
com status do mesmo executavel e hash do banco original antes/depois.
Ponytail: Git e AST sao oracles locais; sem mudar produto para rodar o piloto.

Revisao causal: A-01 liga o diff e os dois SHAs ao status do mesmo banco.
A-02 usa AST e hunks como referencia independente dos simbolos no JSON.
A-03 verifica artefatos publicados e hash do banco original. Preflight
zero achados, spt_validate v3 elegivel e SPT Revisor apto.
causal_semantics_reviewed=true; goal_start_readiness=ready.

## Resultado observado

O build começou em `e84e86d` e o update indexou um arquivo em `573580b`.
`status --json` confirmou `built_at_commit == current_sha` no alvo.
O fim observado da geração ficou 2 s depois da última mudança da fonte.

| Símbolo esperado pela AST no alvo | Faixas novas do Git | Símbolo retornado | Resultado |
| --- | --- | --- | --- |
| `query_graph`, `code_review_graph/tools/query.py:228–690` | 408, 410–413, 417 | Mesmo caminho, nome e intervalo | 1/1, zero faltantes e zero extras |

Os hunks renomeiam uma variável local e ajustam a condição em
`references_to`. O oráculo compara símbolos de função ou classe.
O [patch](../receipts/crg-cli-diff-real/git.patch) e o [JSON bruto](../receipts/crg-cli-diff-real/detect.json) preservam a comparação.

Em `callers_of`, `query_graph_tool` aparece entre os 41 retornos e
`git show 573580b:code_review_graph/main.py` confirma a chamada direta na
função da linha 247. `affected_flows` veio vazio.

Em `tests_for`, 42 testes sem truncamento. O teste
`test_references_to_returns_type_dependents` ficou fora da lista.
O Git confirma que ele entra no ramo em `tests/test_tools.py:330`
e o [pytest isolado](../receipts/crg-cli-diff-real/test-branch.txt) passou
no alvo. A omissão foi registrada no bead `crg-j6z`. O valor
`test_gaps: []` do detect-changes não demonstra cobertura do ramo.

## Veredito

Pronto com ressalvas, `vrd_20261108193045516_0179_0091`.
Flow `flow_20261108192331225_0160_0067` completo, checklist 3/3.
Revisão registrada em `evd_20261108193031468_0174_0085`.

Chato e Questionador conferiram o risco de consultar o SHA errado.
Crítico Cético e Tio Testador separaram o recorte da cobertura e
confirmaram o ramo com Git e pytest. Ponytail manteve o experimento em
um arquivo e um índice isolado. O hash do banco persistente permaneceu igual.

Garimpo reconciliado no flow. A omissão específica já tinha registro no
piloto anterior. A prova atual e o bead preservam o novo resultado.

Próximo corte do mantenedor CRG, bead `crg-j6z`. Reproduzir a associação
ausente no mesmo SHA, rastrear sua origem, corrigir e provar pela CLI
que `tests_for` inclui o teste específico, mantendo o recorte 1/1.
