---
dex_contract: spt
version: 3
status: 'EM_EXECUCAO'
owner: 'sessao:zcode (CRG)'
date: '2026-11-24'
workspace: 'C:/CodexProjetos/code-review-graph'
abertura:
  contexto: 'Pedido do dono em 2026-11-24: usar $entrevista-com-docs, $interrogador-documental, $investigador-socratico em modo auto de contexto vivo fora de contrato/memorias, com $garimpeiro e $estacionamento ativos; gravar ouro forte no padrao canonico sem permissao, NOTAVEL em dex-notas-citaveis, validar L1<->L2/L1<->L3 com consciencia-memorias, colocar as duas plaquinhas (APRENDIZADO-MEMORAVEL-CONTINUO e AUTO-MEMORY-ZCODE-GARIMPA-DEX-MEMORIA) nas superficies quentes, e fechar com $dex-fechamento-projeto-atualizado. Medido: as duas regras existem no AGENTS global, mas rg nas superficies quentes do CRG nao acha nenhuma das duas'
  ferramentas: 'skills carregadas na sessao: dex-find-tools, dex-find-contexto-integrado, entrevista-com-docs, interrogador-documental, investigador-socratico, garimpeiro, estacionamento, dex-notas-citaveis, guarda-plaquinhas, consciencia-memorias, dex-memoria, grava-contexto-local, dex-fechamento-projeto-atualizado; scripts: gate-notas-citaveis.py emit/check, validate-memory-batch.py, espelhar-auto-memory.mjs, check-plaquinhas.py, scan-fechamento.py'
  mentor: 'nao convocado: a duvida e de rota de conhecimento, respondida pelas skills donas e pelo contrato operacional'
origin: 'Pedido literal do dono em 2026-11-24 com a frase exata das duas plaquinhas e a clausula de nao pedir permissao para gravar ouro garimpado'
goal:
  id: 'garimpo-vivo-plaquinhas-20261124'
  title: 'Ouro vivo recolhido, tropecos catalogados e regra de fechamento achavel nas plaquinhas do projeto'
  objective: 'Investigar o contexto vivo fora de contrato e memoria, classificar ouro forte e notavel com fonte e destino, gravar sem permissao no canal canonico, validar conexoes bidirecionais, estacionar residuo utero com quando, tornar as duas regras achaveis nas superficies quentes do CRG e fechar com o fiscal'
context: 'As regras estao no AGENTS global, mas uma janela fria do projeto nao as encontra nas plaquinhas locais; e parte do aprendizado dos ultimos blocos vive so em receitas e trancricoes'
problem: 'Sem ponteiro quente no projeto, o dono precisa repetir o pedido; sem garimpo ativo, aprendizado forte fica em conversa ou em recibo sem L1'
decision: 'Usar as skills donas na sessao; gravar ouro forte via dex-memoria com L1<->L2 ou L1<->L3 validado; NOTAVEL citavel pelo gate de notas; tropeco tactico no napkin; residuo com quando no estacionamento; plaquinhas locais como ponteiro para as regras globais, sem duplicar contrato; fiscal no fim'
scope:
  include:
    - 'revisao das superficies vivas do repo e do registry por aprendizado nao recolhido'
    - 'classificacao com garimpeiro: memoravel, notavel, tropeço, estacionar, nao promover'
    - 'escrita canonica via dex-memoria + validacao L1<->L2 ou L1<->L3 + espelho da auto-memory se escrita'
    - 'nota citavel pelo gate, com gatilho e indice na mesma sessao'
    - 'atualizacao do napkin e/ou plaquinhas quentes com ponteiros para as duas regras'
    - 'estacionamento com item lateral e quando, se houver candidato material'
    - 'fiscal de fechamento e relatorio com contagens'
  exclude:
    - 'reescrever contratos densos das duas plaquinhas no AGENTS global'
    - 'mover ou apagar memoria antiga sem garimpo'
    - 'capturar receita nova sem autorizacao; apenas recomendacao encaminhada'
    - 'transcrever segredo, .env, cookie, Authorization header ou dado pessoal para memoria'
requirements:
  - id: REQ-01
    statement: 'Ouro vivo foi investigado e classificado com fonte'
    criteria:
      - id: C-01
        statement: 'superficies vivas consultadas e candidatos listados com destino'
      - id: C-02
        statement: 'duplicatas e imaturos separados com motivo'
  - id: REQ-02
    statement: 'Ouro forte e NOTAVEL tem destino canonico'
    criteria:
      - id: C-03
        statement: 'memoria gravada com L1 e um destino ativo, validada bidirecionalmente'
      - id: C-04
        statement: 'nota citavel gravada pelo gate com gatilho, indice e ponteiro'
  - id: REQ-03
    statement: 'Plaquinhas e tropeços ficam achaveis'
    criteria:
      - id: C-05
        statement: 'as duas regras citadas nas superficies quentes do projeto'
      - id: C-06
        statement: 'tropeco tactico no napkin com localizador e Faça em vez disso'
  - id: REQ-04
    statement: 'Fechamento auditado'
    criteria:
      - id: C-07
        statement: 'fiscal de fechamento rodado com vermelho 0 ou ressalva declarada'
      - id: C-08
        statement: 'relatorio com contagens, gatilhos L1 e pergunta de edicao'
plan:
  - 'A-01 investigar e classificar'
  - 'A-02 gravar ouro e validar conexoes'
  - 'A-03 nota citavel pelo gate'
  - 'A-04 plaquinhas, napkin e estacionamento'
  - 'A-05 fiscal e relatorio'
tasks:
  - id: A-01
    action: 'Consultar fontes vivas e listar candidatos com fonte, classe e destino'
    covers: [REQ-01]
    done_when: [C-01, C-02]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01, C-02]
        method: command
        procedure: 'test -s .agents/receipts/garimpo-vivo-20261124/CLASSIFICACAO.md'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Gravar ouro forte via dex-memoria e validar L1 com destino unico'
    covers: [REQ-02]
    done_when: [C-03]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-03]
        method: command
        procedure: 'python -B "$USERPROFILE/.agents/skills/consciencia-memorias/scripts/validate-memory-batch.py" --root .agents --l1 lembranca.md --dest-dir memorias > /dev/null'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Gravar NOTAVEL citavel pelo gate e provar gatilho, indice e ponteiro'
    covers: [REQ-02]
    done_when: [C-04]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-03
        proves: [C-04]
        method: command
        procedure: 'python -B "$USERPROFILE/.agents/skills/dex-notas-citaveis/scripts/gate-notas-citaveis.py" check 2>&1 | rg -q "handoff-data-depois-da-meia-noite" && exit 1 || python -B "$USERPROFILE/.agents/skills/dex-notas-citaveis/scripts/gate-notas-citaveis.py" check 2>&1 | rg -q "2026-11-10-padrão-quiz-exaurir-recomendado"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Escrever plaquinhas locais, tropeço no napkin e item lateral no estacionamento'
    covers: [REQ-03]
    done_when: [C-05, C-06]
    depends_on: [A-02, A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-05]
        method: command
        procedure: 'rg -q "APRENDIZADO-MEMORAVEL-CONTINUO" .agents/GATILHOS-VIVOS.md && rg -q "AUTO-MEMORY-ZCODE-GARIMPA-DEX-MEMORIA" .agents/GATILHOS-VIVOS.md'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-05
        proves: [C-06]
        method: command
        procedure: 'rg -q "HANDOFF-DATA-DEPOIS-DA-MEIA-NOITE" .agents/napkin.md'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-05
    action: 'Rodar fiscal de fechamento e entregar relatorio com contagens'
    covers: [REQ-04]
    done_when: [C-07, C-08]
    depends_on: [A-04]
    evidence_requirements:
      - id: ER-06
        proves: [C-07]
        method: command
        procedure: 'python -B "$USERPROFILE/.agents/skills/dex-fechamento-projeto-atualizado/scripts/scan-fechamento.py" --repo C:/CodexProjetos/code-review-graph --out - > /dev/null'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-07
        proves: [C-08]
        method: command
        procedure: 'test -s .agents/receipts/garimpo-vivo-20261124/RELATORIO.md'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'nenhum segredo ou dado pessoal em memoria, nota ou plaquinha'
  - 'as duas regras achaveis por rg no projeto e no global'
  - 'validacao L1<->L2 ou L1<->L3 registrada'
risks:
  - 'repetir regra ja gravada: mitigacao = RG pre-write em auto-memory, CONTRACTS e notas antes de escrever'
  - 'escrever nota orfa: mitigacao = gate emit/check na mesma sessao'
  - 'plaquinha no destino errado: mitigacao = guarda-plaquinhas como fiscal e grava-contexto-local como executor'
uncertainties:
  - 'qual parte da transcricao compactada ainda guarda ouro nao recolhido: a busca em part e indireta e nao substitui fonte viva'
  - 'o item lateral do estacionamento pode nao ter owner natural fora do dono; se nao houver, nao promover'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'python -B "$USERPROFILE/.agents/skills/consciencia-memorias/scripts/validate-memory-batch.py" --root .agents --l1 lembranca.md --dest-dir memorias'
  - 'python -B "$USERPROFILE/.agents/skills/dex-notas-citaveis/scripts/gate-notas-citaveis.py" check'
  - 'python -B "$USERPROFILE/.agents/skills/guarda-plaquinhas/scripts/check-plaquinhas.py" --surface gatilhos --target APRENDIZADO-MEMORAVEL-CONTINUO --root C:/CodexProjetos/code-review-graph'
execution_prompt: |
  /GOAL Executar o Trilho .agents/PLAN-TASKS/2026-11-24-garimpo-vivo-plaquinhas.md no workspace C:/CodexProjetos/code-review-graph: A-01 a A-05 sem parar, com garimpeiro e estacionamento ativos, gravacao canonica sem permissao, validacao de conexoes, plaquinhas quentes e fiscal; relatorio no fim.
---

# Garimpo vivo, plaquinhas e fechamento

## Checklist visual
- [x] A-01 investigar e classificar
- [x] A-02 gravar ouro e validar conexoes
- [x] A-03 nota citavel pelo gate
- [x] A-04 plaquinhas, napkin e estacionamento
- [x] A-05 fiscal e relatorio

Recibos: `.agents/receipts/garimpo-vivo-20261124/` (classificação e relatório), `.agents/receipts/fechamento-20261124-garimpo.json` (fiscal). Memória global COMMITTED `HANDOFF-DATA-DEPOIS-DA-MEIA-NOITE`; nota citável `handoff-data-depois-da-meia-noite` pelo gate; ponteiro das duas regras no GATILHOS-VIVOS; tropeço no napkin; dívida antiga do acervo de notas estacionada em `.agents/ESTACIONAMENTO/itens/NOTAS-CITAVEIS-DEVIDA-20261110.md`.
