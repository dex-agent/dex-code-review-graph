---
dex_contract: spt
version: 3
status: 'CONCLUIDO_COM_RESSALVAS'
owner: 'sessao:zcode (CRG)'
date: '2026-11-23'
workspace: 'C:/CodexProjetos/code-review-graph'
abertura:
  contexto: 'Pedido do dono: limpar a casa com dex-higiene-scan, recolher as ferramentas em TEMP e TMP para o livro e revisar o garimpo. Medido antes de planejar: repo sem pasta TEMP/TMP e sem arquivo temporario (higiene 714 itens, 710 de cache gerado); Temp da maquina com 228 pastas e cerca de 11 GB; 158 scripts e temps (140 de sessao, 82 sem projeto identificavel no conteudo); so 3 sao claramente do CRG. Fontes vivas: .agents/receipts/higiene-20261123.json e INVENTARIO.json do registry'
  ferramentas: 'dex-higiene-scan/scripts/scan-hygiene.py (inventario read-only), dex-toolsbook/scripts/toolsbook.py (livro) e ficha-gate.py (contrato da guarda de staging), arquivar-temp.py (ja aplicado ao repo), dex-fechamento-projeto-atualizado (fiscal)'
  mentor: 'nao convocado: sem duvida de API ou sintaxe ate aqui'
origin: 'Pedido do dono em 2026-11-23: "temos que limpar a casa fazer uma dex-higiene-scan e recolher as ferramentas que estao em TEMP e TMP e organizar elas no nosso livro e as ferramentas dex-toolsbook; revisar os achados memoraveis se ouros foram garimpados e o que estamos deixando"'
goal:
  id: 'higiene-staging-toolsbook-20261123'
  title: 'Casa limpa com rastro: higiene medida, ferramentas da Temp recolhidas e registradas, garimpo revisado'
  objective: 'Todo script de sessao da Temp da maquina inventariado com hash e classificado por leitura; o que e do CRG recolhido para lugar duravel; o que e de outro dono listado por dono no TRACKER do registry; o livro do CRG atualizado; ouro e deixados do bloco revisados'
context: 'A Temp da maquina e a staging implicita de toda a casa; o fiscal de fechamento so olha dentro do repo (ISSUE-LOCAL-0053)'
problem: 'Ferramenta de sessao nasce na Temp, nao passa pelo combinado do livro e some na limpeza; o dono so descobre quando pergunta onde esta a copia'
decision: 'Inventariar e classificar por leitura antes de qualquer mudanca; mover só o que e do CRG; copiar so o que tem reuso; nao apagar nem mover trabalho de outra janela; apagar so o que e regeneravel e meu, com lista no fechamento'
scope:
  include:
    - 'higiene do repo com recibo em .agents/receipts/higiene-20261123.json'
    - 'inventario duravel da Temp da maquina (INVENTARIO.json) e triagem por leitura (TRIAGEM)'
    - 'recolhimento dos scripts do CRG para .agents/receipts/CRG-240DEX-MERGE-20261115/ com README e hash'
    - 'TOOLSBOOK.json do CRG: ferramentas examinadas, lacunas e destino declarado'
    - 'item no TRACKER do registry com a lista por dono'
    - 'revisao do garimpo: ouro gravado e deixados com dono e quando'
    - 'limpeza do que a propria sessao criou na Temp e dos caches ignorados do repo'
  exclude:
    - 'apagar ou mover script de outra janela ou de outro projeto'
    - 'apagar as cerca de 11 GB de pastas da Temp: lista fechada vai para decisao do dono'
    - 'implantar a guarda do livro (reuso.py e ficha-gate.py em tools/dev/): fica em PENDENTES PEND-2026-11-15-TOOLSBOOK'
    - 'promover a tools/ os scripts de triagem de merge: candidato para o proximo merge do upstream'
requirements:
  - id: REQ-01
    statement: 'Higiene e staging medidas, nao presumidas'
    criteria:
      - id: C-01
        statement: 'recibo de higiene do repo gravado e resumido'
      - id: C-02
        statement: 'inventario da Temp da maquina com hash por item gravado fora da Temp'
  - id: REQ-02
    statement: 'Cada script de sessao classificado por leitura'
    criteria:
      - id: C-03
        statement: 'triagem cobre os 140 scripts com classe, dono e destino'
      - id: C-04
        statement: 'os reutilizaveis estao listados com gatilho de reuso'
  - id: REQ-03
    statement: 'O que e do CRG tem destino duravel e o livro sabe'
    criteria:
      - id: C-05
        statement: 'scripts do CRG copiados com hash conferido e README'
      - id: C-06
        statement: 'TOOLSBOOK.json do CRG passa no --check'
  - id: REQ-04
    statement: 'O que e de outro dono esta encaminhado e o garimpo revisado'
    criteria:
      - id: C-07
        statement: 'item aberto e indexado no TRACKER do registry com a lista por dono'
      - id: C-08
        statement: 'fechamento traz tabela de ouro gravado e de deixados com dono e quando'
      - id: C-09
        statement: 'fiscal de fechamento sem vermelho depois do commit'
plan:
  - 'A-01 higiene e inventario'
  - 'A-02 triagem por leitura'
  - 'A-03 recolhimento do CRG e livro'
  - 'A-04 item por dono no registry'
  - 'A-05 revisao do garimpo e fechamento'
tasks:
  - id: A-01
    action: 'Rodar a higiene do repo e inventariar a Temp da maquina, tudo read-only'
    covers: [REQ-01]
    done_when: [C-01, C-02]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01, C-02]
        method: command
        procedure: 'python -B "$USERPROFILE/.agents/skills/dex-higiene-scan/scripts/scan-hygiene.py" --root . --exclude-dir .agents/LIXEIRA --json > /dev/null'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Classificar por leitura cada script de sessao em classe, dono e destino'
    covers: [REQ-02]
    done_when: [C-03, C-04]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-03, C-04]
        method: command
        procedure: 'test -s "$USERPROFILE/.agents/skills/.agents/receipts/higiene-temp-maquina-20261123/TRIAGEM.md"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Recolher os scripts do CRG com hash e README e atualizar o TOOLSBOOK.json'
    covers: [REQ-03]
    done_when: [C-05, C-06]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-05, C-06]
        method: command
        procedure: 'test -s .agents/receipts/CRG-240DEX-MERGE-20261115/RECOLHIMENTO.md && python -B "$USERPROFILE/.agents/skills/dex-toolsbook/scripts/toolsbook.py" --check TOOLSBOOK.json > /dev/null'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Abrir item no TRACKER do registry com a lista por dono e indexar'
    covers: [REQ-04]
    done_when: [C-07]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-04
        proves: [C-07]
        method: command
        procedure: 'rg -c "higiene-temp-maquina" "$USERPROFILE/.agents/skills/.agents/TRACKER/INDEX.md"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-05
    action: 'Revisar o garimpo, limpar o que e da sessao, commitar, empurrar e rodar o fiscal'
    covers: [REQ-04]
    done_when: [C-08, C-09]
    depends_on: [A-03, A-04]
    evidence_requirements:
      - id: ER-06
        proves: [C-08]
        method: command
        procedure: 'test -s .agents/receipts/garimpo-revisao-20261123.md'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-05
        proves: [C-09]
        method: command
        procedure: 'python -B "$USERPROFILE/.agents/skills/dex-fechamento-projeto-atualizado/scripts/scan-fechamento.py" --repo C:/CodexProjetos/code-review-graph --out - > /dev/null'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - '158 itens inventariados com hash e 140 classificados por leitura'
  - 'nada de outra janela movido ou apagado'
  - 'fiscal de fechamento sem vermelho no HEAD publicado'
risks:
  - 'trabalho de outras janelas esta em voo na Temp (OpenBot de ontem, oraculos de hoje): mitigacao = so leitura e copia, nunca mover'
  - 'triagem por leitura pode errar script que depende de contexto de outra sessao: mitigacao = classe e destino ficam visiveis no manifesto para o dono corrigir'
  - 'a lista de delecao da Temp e destrutiva: mitigacao = nao entra neste bloco, vai para decisao do dono'
uncertainties:
  - 'o numero exato de scripts do CRG so fecha depois da triagem por leitura; a pista por conteudo aponta 8'
  - 'nao sei se a casa ja tem lugar canônico para ferramenta recolhida de outros donos; usei o recibo do registry, que e privado'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'python -B "$USERPROFILE/.agents/skills/dex-toolsbook/scripts/toolsbook.py" --check TOOLSBOOK.json'
  - 'python -B "$USERPROFILE/.agents/skills/dex-fechamento-projeto-atualizado/scripts/scan-fechamento.py" --repo C:/CodexProjetos/code-review-graph'
execution_prompt: |
  /GOAL Executar o Trilho .agents/PLAN-TASKS/2026-11-23-higiene-staging-toolsbook.md no workspace C:/CodexProjetos/code-review-graph: fases A-01 a A-05 sem parar entre fases — higiene e inventario read-only, triagem por leitura, recolhimento do que e do CRG com hash, item por dono no TRACKER do registry, revisao do garimpo, commit, push e fiscal de fechamento; verdict no fim.
---

# Higiene, staging e livro

## Checklist visual
- [x] A-01 — higiene e inventário
- [x] A-02 — triagem por leitura
- [x] A-03 — recolhimento do CRG e livro
- [x] A-04 — item por dono no registry
- [x] A-05 — revisão do garimpo e fechamento

Recibos: `.agents/receipts/higiene-20261123.json` (repo), `.agents/receipts/garimpo-revisao-20261123.md` (garimpo) e, no registry, `.agents/receipts/higiene-temp-maquina-20261123/` (`INVENTARIO.json`, `TRIAGEM.json`, `TRIAGEM.md`, `reutilizaveis/` e os recibos do closeout do chato). Item da fila: ISSUE-LOCAL-0062 do registry; reincidências viraram itens: ISSUE-LOCAL-0063 (armadilha do hash) e ISSUE-LOCAL-0064 (ledger inválido). Fiscal formal: `.agents/receipts/fechamento-20261123-higiene.json` (avaliação de reuso em `workflow-review-higiene-20261123.json`, executáveis do bloco: nenhum). Original dos 15 arquivos do merge removido da Temp com registro em `.agents/LIXEIRA/2026-11-23-temp-originais-do-merge/MANIFEST.md`.
