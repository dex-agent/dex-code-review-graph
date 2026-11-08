---
dex_contract: spt
version: 3
status: RASCUNHO
owner: sprinter
date: '2026-11-08'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'GO do dono para recorte por arquivo no detect-changes da CLI'
goal:
  id: crg-cli-recorte-20261108
  title: Expor recorte de arquivos na CLI do CRG
  objective: Implementar o recorte por arquivo no detect-changes e publicar a correcao provada pelo executavel.
context: 'Edicao Dex prioriza CLI; analisador ja filtra faixas por arquivo.'
problem: 'detect-changes da CLI ainda nao recebe uma lista explicita de arquivos.'
decision: 'Reusar --files de impact e intersectar com o conjunto descoberto pelo Git antes do analisador.'
scope:
  include:
    - 'CLI detect-changes, teste de executavel, docs e tres mapas do corte.'
  exclude:
    - 'Mudar contrato do MCP, instalacao global ou reconstruir banco persistente.'
requirements:
  - id: REQ-01
    statement: Preservar RED dos dois casos pelo executavel
    criteria:
      - id: C-01
        statement: Os dois casos falham pela rejeicao de --files antes da implementacao.
  - id: REQ-02
    statement: Respeitar o recorte no resultado JSON
    criteria:
      - id: C-02
        statement: Git e JSON confirmam somente A no diff A+B e zero simbolos no diff apenas B.
  - id: REQ-03
    statement: Publicar com continuidade
    criteria:
      - id: C-03
        statement: Tres mapas registrados e HEAD publicado no main privado confirmado por readback.
plan:
  - 'Criar fixture Git isolada e preservar RED.'
  - 'Conectar argumento ao seletor, revisar e validar pelo executavel.'
  - 'Registrar mapas, commitar, publicar e reler o destino.'
tasks:
  - id: A-01
    action: Preservar o RED de executavel
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'uv run --no-sync pytest -q tests/test_cli.py -k file_scope'
        expectation:
          kind: command_exit
          expected_exit_code: 1
  - id: A-02
    action: Implementar e comprovar a saida JSON
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'uv run --no-sync pytest -q -s tests/test_cli.py -k file_scope'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: Publicar com os mapas e confirmar o remoto
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: inspection
        procedure: 'Reabrir os tres mapas e comparar HEAD, origin/main e API do repositorio privado.'
        expectation:
          kind: boolean_assertion
          expected: true
closure_gates:
  - 'Checklist integral, suite pertinente, diff e verdict oficial.'
risks:
  - 'Intersecao vazia nao pode reativar a descoberta automatica.'
  - 'Manter chamadas sem --files e a variante --brief.'
uncertainties:
  - 'A prova usa grafos isolados do checkout atual, sem medir runtime global.'
gates:
  - 'spt_validate v3 e revisao causal antes de goal_start.'
validation:
  - 'Provas RED/GREEN pela entrada publica, suite CLI e changes, readback privado.'
execution_prompt: |
  /GOAL Execute todas as tasks deste Trilho em C:/CodexProjetos/code-review-graph.
---

# Recorte por arquivo em detect-changes

Tipo: SPEC-PLAN-TASKs

## SPEC

Com `--files A`, diff A+B reporta apenas A; diff apenas B devolve JSON com
zero simbolos, gaps e risco zero. Caminhos sao comparados na raiz do repo.
Sem a opcao, preservar a selecao existente. Baseline `016092d`; bead `crg-dqq`.

## PLAN

Sprinter e checklist visual: fixture Git + executavel primeiro, pequena mudanca
no parser e na selecao ja existente, suite e publicacao. Se houver regressao,
reverter apenas o corte. O indice persistente e historico; fixture recebe
banco proprio construido pelo executavel antes de cada comparacao.

## TASKs

- [x] A-01 — RED dos dois casos, rejeicao de --files. Prova `evd_20261108190035825_0141_0043`.
- [x] A-02 — Quatro casos Git/JSON passaram, 222 testes na suite isolada e Ruff verde. Prova `evd_20261108190035866_0142_0045`.
- [ ] A-03 — tres mapas, commit, push e readback

## Riscos e validacao

Chato: e se nenhum arquivo passar? Retornar JSON vazio no modo selecionado e
impedir que o analisador receba um arquivo sem mudanca. Ponytail: o parser
segue a forma de impact e o analisador existente continua dono das faixas.
Prova independente: git diff --name-only e patch com hunk; JSON e consumido
como stdout da entrada instalada no ambiente do checkout.

Gate Sprinter, SPT Revisor e Ponytail: preflight com zero achados; estrutura
v3 elegivel. Revisao causal A-01/REQ-01/C-01/ER-01 exige erro do parser nos
dois processos, com build da fixture ja provado. A-02/REQ-02/C-02/ER-02
valida nomes, caminhos e risco quando o Git mostra a intersecao vazia.
A-03/REQ-03/C-03/ER-03 combina artefatos em disco com readback independente.
causal_semantics_reviewed=true; goal_start_readiness=ready; SPT apto.

Revisao durante a execucao: a variante com espaco revelou tab no cabecalho
do diff; a variante com acento revelou que o build recebia nomes escapados
de `git ls-files`. Ambos afetam o mesmo recorte. O decoder de inventario
adota NUL como as outras entradas Git e o parser remove o separador do
cabecalho. O oracle conserva as duas variantes de nome.

Provas em `.agents/receipts/crg-cli-recorte/`; commit de produto `1e12485`.
Suite: 222 passaram e 1 skip previsto no Windows. Revisor isolou o teste
de search que herdava marcador do perfil no basetemp padrao. A falha tambem
ocorre em 016092d e desaparece em arvore temporaria isolada.

Meta-analise do Chato: o filtro nasce na fronteira CLI, com o analisador
dono das faixas. E se o inventario mudar a identidade? NUL evita escapes;
tab de cabecalho e tratado no parser, que preserva o nome. A prova compara
Git e executavel em vez de tomar o indice como oracle. Mapas preservados
por corte em `../MAPAS/INDEX.md`. O banco persistente permanece historico.
