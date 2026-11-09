---
dex_contract: spt
version: 3
status: 'CONCLUIDO_COM_RESSALVAS'
owner: 'sprinter'
date: '2026-11-09'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO-PADRAO do dono para crg-x6m com Oraculo Clean Code'
goal:
  id: 'crg-x6m-2026-11-09'
  title: 'Resolver o destino PHP por identidade'
  objective: 'Respeitar o escopo PHP e provar a paridade de CALLS e TESTED_BY entre update e rebuild'
context: 'As duas rotas foram reproduzidas pela CLI e pelo SQLite na investigacao anterior.'
problem: 'Uma classe homonima pode receber CALLS e TESTED_BY apesar de contradizer o escopo da chamada.'
decision: 'Conservar a identidade PHP da chamada ate uma definicao valida ser indexada e impedir bypass pelo resolvedor generico.'
scope:
  include:
    - 'Parser PHP, resolvedor scoped, fronteira generica de grafo, testes e seletores de CI'
    - 'Fixture CLI isolada, receipts, Trilho, continuidade e mapas historicos'
  exclude:
    - 'Migracao em massa, indice persistente e mudanca na heuristica de nomenclatura da CLI'
requirements:
  - id: REQ-01
    statement: 'Preservar os dois REDs pelo executavel'
    criteria:
      - id: C-01
        statement: 'Preservar os dois REDs pelo executavel'
  - id: REQ-02
    statement: 'Corrigir a resolucao PHP e proteger os consumidores'
    criteria:
      - id: C-02
        statement: 'Corrigir a resolucao PHP e proteger os consumidores'
  - id: REQ-03
    statement: 'Provar update e rebuild com SQLite e CLI no mesmo HEAD'
    criteria:
      - id: C-03
        statement: 'Provar update e rebuild com SQLite e CLI no mesmo HEAD'
  - id: REQ-04
    statement: 'Revisar e publicar o corte com prova de qualidade'
    criteria:
      - id: C-04
        statement: 'Revisar e publicar o corte com prova de qualidade'
plan:
  - 'Preservar os dois REDs pelo executavel'
  - 'Corrigir a resolucao PHP e proteger os consumidores'
  - 'Provar update e rebuild com SQLite e CLI no mesmo HEAD'
  - 'Revisar e publicar o corte com prova de qualidade'
tasks:
  - id: A-01
    action: 'Preservar os dois REDs pelo executavel'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Executar as duas fixtures PHP pelo executavel no parser original e identificar as arestas indevidas no RED JSON'
        expectation:
          kind: command_exit
          expected_exit_code: 1
  - id: A-02
    action: 'Corrigir a resolucao PHP e proteger os consumidores'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Executar os testes PHP e Rust selecionados, linter e a matriz verde no parser corrigido'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Provar update e rebuild com SQLite e CLI no mesmo HEAD'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Executar a matriz CLI em dois repositorios Git isolados e verificar grafo, consulta e idempotencia'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Revisar e publicar o corte com prova de qualidade'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Comparar a suite Windows com o baseline, exigir selecao CI Windows e verificar a matriz remota do SHA publicado'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Registrar verdict, mapas, continuidade e bead e verificar a publicacao Git e Dolt.'
risks:
  - 'Bancos antigos podem carregar arestas canonicas da resolucao anterior. Adocao exige prova separada.'
  - 'O resolvedor e compartilhado com Rust e o fallback atende outras linguagens.'
uncertainties:
  - 'A suite integral Windows tem 24 IDs historicos a comparar.'
gates:
  - 'Preflight, spt_validate, revisao causal e fiscal do Trilho anteriores ao goal_start.'
validation:
  - 'CLI do venv, Git, pytest, SQLite, Ruff e GitHub Actions no SHA de produto.'
execution_prompt: |
  /GOAL
  Execute .agents/PLAN-TASKS/2026-11-09-crg-x6m-php-homonimos.md em C:\CodexProjetos\code-review-graph, por dependencias, ate o verdict.
---

# Impedir atribuição PHP ao homônimo errado

Tipo: SPEC-PLAN-TASKs

## Revisão semântica e do Trilho

A-01 observa os destinos qualificados para o mesmo teste em dois repos Git, com código original e fase identificada. A-02 verifica controles vizinhos e preserva os dois REDs como testes duráveis. A-03 compara a CLI e o banco após inserir só Payments e refazer o índice no mesmo HEAD, incluindo repetição do update. A-04 compara por ID com o baseline e vincula CI ao SHA publicado. Cada prova vai para um recibo estável. O Chato exige que nome simples, import de outro alias e aresta material sejam discriminados. Ponytail exige reutilizar evidência lexical e o espelhamento CALLS/TESTED_BY existente. Clean Code EN 2008, G32 e T5–T6, fornece a lente para explicitar precedência e testar vizinhos. causal_semantics_reviewed=true, goal_start_readiness=ready.

## Checklist visual

- [x] A-01 [AÇÃO] Preservar os dois REDs pelo executavel | owner: mantenedor CRG | quando: após goal_start | prova: [red.json](../receipts/crg-x6m/red.json), `evd_20261109054358815_0335_0288`
- [x] A-02 [AÇÃO] Corrigir a resolucao PHP e proteger os consumidores | owner: mantenedor CRG | quando: após A-01 | prova: [green.json](../receipts/crg-x6m/green.json), `evd_20261109054652065_0336_0290`
- [x] A-03 [AÇÃO] Provar update e rebuild com SQLite e CLI no mesmo HEAD | owner: mantenedor CRG | quando: após A-02 | prova: [cli.json](../receipts/crg-x6m/cli.json), `evd_20261109054813588_0337_0292`
- [x] A-04 [AÇÃO] Revisar e publicar o corte com prova de qualidade | owner: mantenedor CRG | quando: após A-03 | prova: [comparison.json](../receipts/crg-x6m/comparison.json), `evd_20261109055357222_0343_0300`

## Resultado observado

| Cenário | RED com só Shipping | Corrigido com só Shipping | Payments após update, repetição e rebuild |
|---|---:|---:|---|
| Namespace e import | 2 arestas erradas | 0 arestas | CALLS e TESTED_BY para construtor e método |
| Alias do Composer | 4 arestas erradas | 0 arestas | CALLS e TESTED_BY para construtor e método |

Os três estados finais têm o mesmo HEAD do Git e as mesmas arestas e consultas. O SQLite mantém zero CALLS e TESTED_BY para Shipping. Na CLI, `tests_for` retorna `testItAdds` como associação direta para Payments.

O produto `fb9fc22da3d1966f5754d9db7938cd4b0ad8caba` passou nos nove jobs da CI remota. A seleção Windows local passou em 524 testes, com 10 skips. A suíte Windows integral passou em 2300 testes e repetiu exatamente os 24 IDs do baseline.

O Chato conferiu a classe ausente, a chegada isolada de Payments, a repetição do update e a equivalência com rebuild. O Cético cruzou a consulta pública com as arestas materiais e o Git. Ponytail preservou o resolvedor compartilhado e o espelhamento existente. A lente Clean Code G32 e T5–T6 foi aplicada à precedência lexical e aos casos vizinhos. A adoção em índice legado exige backup e rebuild. O próximo corte recomendado é retomar `crg-iu1` pelos três IDs de caminhos PHP/Rust.

## Veredito

Checklist visual 4/4. PPIRTV `flow_20261109054125732_0328_0280` concluído com zero bloqueios, veredito `vrd_20261109055428929_0348_0306` pronto com ressalvas. [Recibo oficial resumido](../receipts/crg-x6m/verdict.json).
