---
dex_contract: spt
version: 3
status: CONCLUIDO
owner: sprinter
date: '2026-11-08'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'GO do dono para executar a recomendação do Oráculo Clean Code em crg-j6z'
goal:
  id: crg-python-reexports-20261108
  title: Corrigir a identidade de símbolos Python reexportados
  objective: Recuperar o teste omitido em tests_for com uma resolução verificável de reexportações Python.
context: 'O índice do piloto em 573580b tem CALLS e TESTED_BY apontando para tools/__init__.py em vez da definição em tools/query.py.'
problem: 'O teste que executa references_to passa no pytest, mas falta na consulta da definição pelo executável.'
decision: 'Preservar RED, corrigir o resolvedor de símbolo importado e provar build, update e o diff histórico pela CLI.'
scope:
  include:
    - 'Resolução estática de reexportações Python explícitas, regressões, índice isolado, recibos, mapas e publicação privada.'
  exclude:
    - 'Importar ou executar código indexado, mudar o contrato da CLI, ampliar cobertura de fluxos ou regenerar o índice persistente.'
requirements:
  - id: REQ-01
    statement: Capturar a falha antes da implementação.
    criteria:
      - id: C-01
        statement: A fixture RED falha por resolver a chamada para o arquivo intermediário.
  - id: REQ-02
    statement: Corrigir a identidade estática na fronteira do parser.
    criteria:
      - id: C-02
        statement: A fixture do parser valida a identidade canônica das arestas para os cenários positivos e negativos.
  - id: REQ-03
    statement: Validar a atualização do índice pelo executável.
    criteria:
      - id: C-03
        statement: A prova CLI da fixture valida a troca da associação depois do update.
  - id: REQ-04
    statement: Validar o resultado no diff histórico de um arquivo.
    criteria:
      - id: C-04
        statement: O oráculo Git e CLI de 573580b confirma a associação recuperada dentro do contrato anterior.
plan:
  - 'Reproduzir a identidade incorreta em fixture mínima com homônimo.'
  - 'Resolver reexportação explícita no parser com evidência local.'
  - 'Revisar vizinhos e testar build e update pelo executável.'
  - 'Confrontar CLI e Git no alvo histórico e preservar os mapas da prova.'
tasks:
  - id: A-01
    action: Preservar o RED da fixture
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: inspection
        procedure: 'Rodar pytest tests/test_parser.py -k python_explicit_reexport antes do fix e inspecionar exit 1 e o destino __init__.py no caso positivo.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-02
    action: Resolver o destino e revisar os efeitos vizinhos
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: inspection
        procedure: 'Rodar pytest tests/test_parser.py -k python_explicit_reexport e revisar o diff contra homônimo, ciclo, binding incerto e consumidores vizinhos.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-03
    action: Provar a troca de associação no índice de teste
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: inspection
        procedure: 'Rodar a fixture Git com o executável do checkout. Comparar query tests_for antes e depois do update no mesmo SQLite isolado.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-04
    action: Validar o commit real e registrar a prova
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: inspection
        procedure: 'Usar build no pai e update em 573580b. Verificar o teste exato em query tests_for e comparar detect-changes --files com Git e AST. Conferir os mapas contra os recibos.'
        expectation:
          kind: boolean_assertion
          expected: true
closure_gates:
  - 'Checklist visual 100 por cento com provas vinculadas, goal_verdict, publicação Git privada e fechamento Beads.'
risks:
  - 'Atribuir chamada por nome cria falso positivo para homônimos. Provar identidade por caminho e binding explícito.'
  - 'Um índice anterior pode manter aresta antiga. Provar update da reexportação sem usar o banco persistente.'
uncertainties:
  - 'A cobertura deste corte é de reexportações Python explícitas verificáveis. Imports dinâmicos seguem o fallback existente.'
gates:
  - 'Preflight zero achados, spt_validate v3 elegível, revisão causal e SPT Revisor apto antes de goal_start.'
validation:
  - 'pytest focal, suíte do repo, CLI build e update, Git e AST no piloto histórico e git diff --check.'
execution_prompt: |
  /GOAL Execute este Trilho na ordem de dependências em C:/CodexProjetos/code-review-graph.
---

# Corrigir símbolos Python reexportados no grafo

Tipo: SPEC-PLAN-TASKs

## SPEC

Sprint Goal do bead `crg-j6z`. A consulta pelo caminho da definição deve
recuperar o teste do ramo alterado. No caso real, o parser já produz duas
arestas, mas aponta ambas para a fachada. O ponto de correção é a resolução
do símbolo Python antes do espelhamento. A evidência inicial está no
[Trilho do piloto](2026-11-08-crg-cli-diff-real.md).

## PLAN

Um RED focal, a menor correção compartilhada, revisão adversarial e prova
pela CLI. Fonte dos quality gates: regras universais do manifesto de
domínios e workflow PPIRTV local. O Oráculo usa a lente de refinamento
incremental de Clean Code, cap. 9 e 14. O Chato fiscaliza homônimos, ciclos,
binding substituído e aresta antiga após update. Ponytail preserva os
contratos existentes de consulta e geração de arestas.

## Checklist visual das TASKs

- [x] A-01 [AÇÃO] Preservar o RED da identidade | owner: Tio Testador | when: antes da primeira linha do fix | source: REQ-01 / ER-01 | evidence: [RED](../receipts/crg-python-reexports/red.txt), `evd_20261108223642988_0194_0108`
- [x] A-02 [AÇÃO] Resolver e revisar a identidade das arestas | owner: mantenedor CRG | when: depois do RED | source: REQ-02 / ER-02 | evidence: [GREEN](../receipts/crg-python-reexports/green-parser.txt), `evd_20261108224206852_0196_0112`
- [x] A-03 [AÇÃO] Provar a troca no mesmo índice de teste | owner: Tio Testador | when: após revisão do fix | source: REQ-03 / ER-03 | evidence: [CLI](../receipts/crg-python-reexports/incremental.txt), `evd_20261108224206903_0197_0114`
- [x] A-04 [AÇÃO] Validar o alvo histórico e reconciliar os mapas | owner: Validador | when: depois da prova incremental | source: REQ-04 / ER-04 | evidence: [Git/CLI](../receipts/crg-python-reexports/historical.json), `evd_20261108224542585_0198_0116`

## Validação e limites

Os recibos ficam em `.agents/receipts/crg-python-reexports/`. Bancos e clones
ficam em TEMP. Importação dinâmica e ampliação do ranking da CLI ficam fora
deste corte. Definition of Done: quatro saídas reais, revisão vinculada,
veredito oficial e confirmação remota do commit.

Revisão pré-execução (SPT Revisor + Ponytail), apto. Estrutura v3, referências
e ordem conferidas no preflight e no spt_validate. A-01 mede exit e destino
no pytest sobre a fixture. A-02 usa o oráculo de identidade das duas arestas
em fonte local controlada. A-03 usa dois snapshots do mesmo SQLite produzidos
pelo build e update Git. A-04 usa Git/AST como referência independente para
o JSON histórico. Cada saída será vinculada por caminho e hash no PPIRTV.
runtime_semantics_scope=static_referential_integrity.
causal_semantics_reviewed=true; goal_start_readiness=ready.

## Resultados

- RED original: dois casos falharam porque o destino era `__init__.py`.
- O primeiro update manteve a aresta antiga. A revisão encontrou dois elos:
  extração do módulo relativo e descarte de dependentes com hash igual.
  [RED incremental](../receipts/crg-python-reexports/red-incremental.txt)
- GREEN incremental: alterar somente `bridge.py` atualizou três arquivos.
  O teste saiu da origem antiga, apareceu na nova e ficou ausente da homônima.
- CLI em `573580b`: `test_references_to_returns_type_dependents` aparece como
  associação direta em `tools/query.py::query_graph`. A consulta emite 100
  de 121 resultados. O teste exato está entre os emitidos. O Git e a AST
  confirmam `query_graph` nas linhas 228–690 e o recorte 1/1.
- Suíte Windows no mesmo ambiente: 2284 passaram ante 2277 no baseline.
  Os mesmos 27 testes falharam nos dois checkouts. Bead `crg-iu1`, owner
  mantenedor CRG, antes do próximo release Windows.
  [Comparação por ID](../receipts/crg-python-reexports/suite-comparison.json)
- Ruff do código de produção passou. Mapas publicados com fontes conferidas.
  O hash do índice persistente permaneceu igual.

O update trabalha com o limite de dependentes existente. No piloto, um
arquivo mudou no Git e 24 arquivos foram reprocessados. Para consumir a
correção em um índice anterior, fazer build com o executável atualizado.

## Veredito

**Pronto com ressalvas**. Flow `flow_20261108223556406_0187_0100` completo,
veredito `vrd_20261108224740560_0208_0128`, checklist 4/4. Revisão vinculada em
`evd_20261108224727015_0203_0122`.

O Oráculo Clean Code aplicou os gates de teste focal e refinamento em
passos, com a edição EN 2008 reaberta na análise deste caso. O Chato
exigiu a troca de destino no mesmo SQLite e o controle homônimo. O
Ponytail manteve a correção nos resolvedores e na invalidação existente.
Lição recuperável em [CRG-DEPENDENTE-HASH](../memorias/crg-dependente-hash-aresta.md),
validada L1↔L2 em 1/1 com Finder e rg.

Próximo corte único do mantenedor: fazer backup e build do índice
persistente com o executável atualizado, conferir o SHA e verificar a
associação direta pela CLI antes de usar o grafo.
