---
dex_contract: spt
version: 3
status: 'CONCLUIDO_COM_RESSALVAS'
owner: 'sprinter'
date: '2026-11-08'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO do dono para executar crg-08x, com Oraculo Clean Code no comando'
goal:
  id: 'crg-test-path-2026-11-08'
  title: 'Classificacao de testes por caminho no CRG'
  objective: 'Corrigir a classificacao de testes por caminho relativo ao checkout e provar o resultado na CLI e no SQLite'
context: 'CLI principal no origin privado Dex. Revisao adversarial reproduziu falsos testes no Windows.'
problem: 'Diretorio cujo nome termina em test e ancestral externo do checkout podem criar TESTED_BY indevido.'
decision: 'Limitar convencoes de diretorio a componentes do caminho relativo do checkout, preservando sinais de nome e anotacao.'
scope:
  include:
    - 'code_review_graph/parser.py'
    - 'code_review_graph/jedi_resolver.py'
    - 'tests/test_parser.py'
    - '.github/workflows/ci.yml'
    - '.agents/PLAN-TASKS'
    - '.agents/receipts/crg-test-path'
    - 'Continuidade local, beads e mapas do CRG'
  exclude:
    - 'Migracao ou rebuild do indice persistente e resolucao de homonimos PHP'
requirements:
  - id: REQ-01
    statement: 'Preservar RED por sufixo, ancestral e diretorio __tests__ na raiz'
    criteria:
      - id: C-01
        statement: 'Preservar RED por sufixo, ancestral e diretorio __tests__ na raiz'
  - id: REQ-02
    statement: 'Corrigir o detector compartilhado e passar controles no parser e na selecao nativa da CI'
    criteria:
      - id: C-02
        statement: 'Corrigir o detector compartilhado e passar controles no parser e na selecao nativa da CI'
  - id: REQ-03
    statement: 'Provar a classificacao e associacao direta no executavel e nas arestas SQLite'
    criteria:
      - id: C-03
        statement: 'Provar a classificacao e associacao direta no executavel e nas arestas SQLite'
  - id: REQ-04
    statement: 'Conferir a regressao integral no Windows e o pipeline do commit no origin privado'
    criteria:
      - id: C-04
        statement: 'Conferir a regressao integral no Windows e o pipeline do commit no origin privado'
plan:
  - 'Preservar RED por sufixo, ancestral e diretorio __tests__ na raiz'
  - 'Corrigir o detector compartilhado e passar controles no parser e na selecao nativa da CI'
  - 'Provar a classificacao e associacao direta no executavel e nas arestas SQLite'
  - 'Conferir a regressao integral no Windows e o pipeline do commit no origin privado'
tasks:
  - id: A-01
    action: 'Preservar RED por sufixo, ancestral e diretorio __tests__ na raiz'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Executar pytest no parser original do checkout e registrar somente IDs que falham por classificacao em red.json'
        expectation:
          kind: command_exit
          expected_exit_code: 1
  - id: A-02
    action: 'Corrigir o detector compartilhado e passar controles no parser e na selecao nativa da CI'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Executar pytest dos casos novos e PHPUnit existentes, Ruff e leitura dos seletores Windows em green.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Provar a classificacao e associacao direta no executavel e nas arestas SQLite'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Executar builds isolados da CLI original e corrigida com arquivos PHP e TS reais, comparar nos, arestas e JSON tests_for em cli.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Conferir a regressao integral no Windows e o pipeline do commit no origin privado'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Comparar IDs da suite Windows com baseline, exigir a selecao CI nativa e conferir jobs remotos do SHA exato em comparison.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Atualizar continuidade, tres mapas, bead e receipts. Publicar e conferir origin. Registrar verdict e fechar o flow.'
risks:
  - 'O detector e compartilhado entre linguagens. Testar vizinhos e preservar identidade, anotacoes e nomes.'
uncertainties:
  - 'A suite Windows integral tem 24 falhas anteriores. Comparar identidades antes de atribuir regressao.'
gates:
  - 'Executar preflight e spt_validate, revisar causalidade e o Trilho antes de goal_start.'
validation:
  - 'RED e GREEN com pytest. A/B com code-review-graph.exe e SQLite. Matriz GitHub Actions por SHA.'
execution_prompt: |
  /GOAL
  Execute .agents/PLAN-TASKS/2026-11-08-crg-test-path.md em C:\CodexProjetos\code-review-graph pela ordem de dependencias e registre o verdict oficial.
---

# Corrigir falsos testes por caminho no CRG

Tipo: SPEC-PLAN-TASKs

## SPEC e PLAN

O owner do detector é o parser comum. O caminho de classificação pode ser relativo ao checkout. As identidades de nó e aresta continuam com o caminho que o chamador forneceu. A fonte da decisão é o bead crg-08x e a prova histórica A/B contra c3682ac e 92fdfe0. A régua de Clean Code vem dos capítulos 9, 12 e 17 da edição de 2008. Os testes têm uma causa observável e protegem a fronteira compartilhada.

Durante o RED, a varredura de chamadores encontrou o enriquecimento Jedi. Ele também recebe a raiz existente, pois decide se deve complementar chamadas a partir do mesmo detector. O A-02 cobre esse consumidor direto.

## Revisão semântica e do Trilho

Causalidade conferida por cadeia. A-01 usa pytest com o mesmo código-fonte nos controles e identifica cada falha esperada antes de alterar o parser. A-02 exige os mesmos casos verdes e preserva PHPUnit. A-03 usa duas leituras do mesmo build, consulta pública e SQL, com oráculo de identidade do arquivo e edge direta. A-04 compara IDs da suíte Windows e exige resposta da CI vinculada ao SHA publicado. Cada prova recebe um arquivo estável para evitar stale no verdict. A revisão A–E conferiu escopo, ordem, oráculo, controles e fechamento. Chato verificou os casos rootless, nomes legítimos e as regras Julia e R que poderiam recolocar o falso verde. Ponytail mantém uma única implementação de classificação, sem mudar o schema ou a CLI. causal_semantics_reviewed=true, goal_start_readiness=ready.

## Checklist visual

- [x] A-01 [AÇÃO] Preservar RED por sufixo, ancestral e diretorio __tests__ na raiz | owner: mantenedor CRG | quando: após goal_start | prova: ER-01, [red.json](../receipts/crg-test-path/red.json), `evd_20261109015403793_0281_0220`
- [x] A-02 [AÇÃO] Corrigir o detector compartilhado e passar controles no parser e na selecao nativa da CI | owner: mantenedor CRG | quando: após A-01 | prova: ER-02, [green.json](../receipts/crg-test-path/green.json), `evd_20261109015550186_0282_0222`
- [x] A-03 [AÇÃO] Provar a classificacao e associacao direta no executavel e nas arestas SQLite | owner: mantenedor CRG | quando: após A-02 | prova: ER-03, [cli.json](../receipts/crg-test-path/cli.json), `evd_20261109015700250_0283_0224`
- [x] A-04 [AÇÃO] Conferir a regressao integral no Windows e o pipeline do commit no origin privado | owner: mantenedor CRG | quando: após A-03 | prova: ER-04, [comparison.json](../receipts/crg-test-path/comparison.json), `evd_20261109020442687_0289_0232`

## Revisão final do Chato com as lentes ativas

- **Clean Code.** A edição EN de 2008, caps. 9 e 17, p. 314, T5–T6, orienta testar fronteiras e casos próximos do defeito. A fonte foi reaberta com o hash do lock `61949fc2bc46431fb6cc7a71a472ce4dbfbcec7a2277f538e8d7ae9722c5618e`. Aplicação ao CRG: mesmos bytes PHP e TS, variando só o caminho. O RED local inclui seis falhas por ID.
- **Questionador.** E se um checkout sob `tests/` tiver um `src/` comum? A classificação descarta o ancestral externo. E se o nome for explícito? Os controles de anotação e nome continuam verdes. E se a consulta ocultar uma aresta que ficou no banco? O teste A/B lê os dois canais e exige zero em ambos.
- **Ponytail.** O detector comum faz o recorte lexical e o Jedi entrega a raiz que já possuía. Padrões de diretório redundantes de Julia e R foram absorvidos pela convenção `test/` e `tests/`. As identidades continuam nativas.
- **Cético.** Um build isolado prova a classificação da versão nova. A reclassificação de índice existente permanece no bead `crg-k4q`, com o mantenedor antes da próxima consulta ao persistente. O SHA de um update sozinho não prova reparse.
- **Revisor e Tio Testador.** Revisão vinculada ao commit `3fb1ab318f9c92f5bbb5d1d7f9b4462a24a5ff04`, prova `evd_20261109015809162_0288_0230`. A matriz Windows integral preservou os 24 IDs do baseline. A CI Ubuntu 3.12 sofreu uma interrupção na tentativa 1. A falha de compatibilidade com Python 3.14 apareceu também no baseline e foi isolada em `crg-hmu`.

## Resultados

- Windows integral 3.13.13: 2.298 passaram, 24 falhas com os mesmos IDs do baseline, 12 skips, 2 xpasses. Seleção Windows local 3.12: 522 passaram, 10 skips.
- Ubuntu WSL 3.12.14: 2.327 passaram, 7 skips, 2 xpasses, cobertura 82,14%. CI do commit exato: nove jobs aprovados após repetir os jobs incompletos da primeira tentativa. [CI](https://github.com/dex-agent/dex-code-review-graph/actions/runs/42548260647) e [primeira tentativa](../receipts/crg-test-path/ci-attempt-1.json).
- Os [três mapas históricos](../MAPAS/INDEX.md) registram a capacidade observada, a decisão e os consumidores. Flow oficial `flow_20261109015255779_0274_0212`.
- Próximo corte do mantenedor, antes de consultar o índice persistente: `crg-k4q`. Construir banco com o parser anterior, atualizar arquivo alheio com o parser atual, conferir o SHA e a classificação antes e depois do rebuild, e provar o sinal de frescor pelo executável.

## Veredito

**Pronto com ressalvas**, `vrd_20261109020535975_0294_0238`. Flow `flow_20261109015255779_0274_0212` completo, checklist 4/4, cinco evidências oficiais e zero bloqueadores no [readback](../receipts/crg-test-path/verdict.json).

As 24 falhas preexistentes da suíte Windows continuam em `crg-iu1`. A validade semântica do índice persistente anterior fica em `crg-k4q`. O gatilho L1 `CRG-TEST-PATH` já recupera o princípio e a prova original. As observações específicas deste corte foram reconciliadas no ledger do flow e nos mapas.
