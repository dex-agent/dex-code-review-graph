---
dex_contract: spt
version: 3
status: 'ATIVO'
owner: 'sessao:zcode (GO PADRAO do dono via quiz 2026-11-23)'
date: '2026-11-23'
workspace: 'C:/CodexProjetos/code-review-graph'
abertura:
  contexto: 'Main vermelha desde 21/11 por 3 testes de versao (test_documentation::test_release_version_is_current_everywhere_it_is_written_down, test_doctor::test_python_module_entry_asks_that_python, test_doctor::test_hooks_install_writes_now_check_the_copy_they_name); pyproject 2.4.0+dex.3 x __version__ 2.4.0+dex.1; copia no PATH com doctor falso-vermelho (1 problem found); uv.lock raiz em 2.4.0; suite packaging opt-in, so no promotion-gate (branch testing inexistente no fork) e rejeita sufixo local (test_packaging.py l.652); 3a ocorrencia da classe (16/11, 21/11, 22/11); fontes vivas: tests/test_documentation.py l.145-199, tests/test_packaging.py l.70-77 e l.646-662, tests/conftest.py l.101-137, docs/RELEASING.md, .github/workflows/ci.yml, .github/workflows/promotion-gate.yml, tools/playbook/hooks/pre-commit'
  ferramentas: 'reuso.py --skills x3 = sem candidato (TOOLSBOOK.json ausente no CRG); existentes no repo: 2 testes de versao + fixtures da suite packaging (artefacts, wheel_env); hook pre-commit ativo (core.hooksPath=tools/playbook/hooks); chama-o-vigia para o push; medidor de CC da casa; oraculos consultados: oraculo-solid, oraculo-clean-code, oraculo-teste-de-integracao, oraculo-teste-de-unidade'
  mentor: 'mentor-documental-git (leitura do indice no pre-commit) e mentor-documental-github-actions (job novo no ci.yml), se houver dificuldade tecnica'
origin: 'Anotacao do dono na analise do CI vermelho (2026-11-23): adiciona um teste de integracao pra garantir isso e um teste de regressao pra garantir que nao se repita; GO PADRAO via quiz'
goal:
  id: 'versao-uma-fonte-20261123'
  title: 'Versao do CRG com um dono so: stamps sincronizados, alarme provado e gate no commit'
  objective: 'A main do CRG volta a ficar verde com os 12 stamps em 2.4.0+dex.3, e um bump parcial nao consegue mais ser commitado nesta maquina nem passar sem ser visto no CI do fork'
context: 'Fork dex-agent/dex-code-review-graph empurra direto na main, sem PR e sem as branches staging/testing do fluxo do upstream'
problem: 'Um bump que mexe so no pyproject.toml deixa a main vermelha e o doctor falso-vermelho em toda copia instalada, e os alarmes existentes nao rodam no fork'
decision: 'Extrair a checagem para tools/release_version.py (um dono; leitura por abstracao), cobrir com regressao de mutacoes historicas e teste de integracao na copia instalada, e chamar a checagem no pre-commit (indice) e num job novo do ci.yml; comando unico de bump fica para o corte seguinte'
scope:
  include:
    - 'mover os 12 stamps para 2.4.0+dex.3 (pyproject ja esta; __init__, 5 READMEs, docs/GITHUB_ACTION.md, docs/USAGE.md, docs/FEATURES.md, .github/ISSUE_TEMPLATE/bug_report.yml, uv.lock pacote raiz)'
    - 'tools/release_version.py + linha em tools/INDEX.md; teste de regressao em tests/test_documentation.py; teste de integracao em tests/test_packaging.py'
    - 'tools/playbook/hooks/pre-commit chama a checagem; job novo em .github/workflows/ci.yml'
    - 'commit e push com identidade dex-agent, vigia do CI, reinstalacao do wheel no PATH'
    - 'rastro: TRACKER 0008, napkin, GATILHOS-VIVOS, plaquinha CRG-BUMP-CONSUMIDORES, skill code-review-graph do registry, itens do registry'
  exclude:
    - 'comando unico de bump (--set) = corte seguinte'
    - 'atualizar dependencias vulneraveis do uv.lock e do package-lock (corte do Dependabot; aqui so a linha do pacote raiz)'
    - 'protecao de branch no GitHub = quiz proprio depois do CI verde'
    - 'PR #6, revisao em bloco proprio'
requirements:
  - id: REQ-01
    statement: 'Os 12 stamps de versao dizem 2.4.0+dex.3 e a main fica verde no runner'
    criteria:
      - id: C-01
        statement: 'os 3 testes que falhavam no CI passam localmente'
      - id: C-02
        statement: 'run do ci.yml na main conclui success no SHA publicado'
  - id: REQ-02
    statement: 'O alarme de versao tem um dono so e esta provado que acende'
    criteria:
      - id: C-03
        statement: 'RED capturado antes do conserto, pelo motivo previsto'
      - id: C-04
        statement: 'cada uma das 5 mutacoes historicas devolve problema nomeando o arquivo mutado'
      - id: C-10
        statement: 'arvore sincronizada devolve lista vazia'
  - id: REQ-03
    statement: 'A copia instalada responde uma versao so por todos os canais'
    criteria:
      - id: C-05
        statement: 'teste de empacotamento aceita a versao com sufixo local X.Y.Z+dex.N'
      - id: C-15
        statement: 'o teste dos canais no venv limpo afirma --version igual a __version__ igual ao metadata, verde localmente'
      - id: C-06
        statement: 'o job novo do ci.yml executa a checagem no run publicado, sem skip'
  - id: REQ-04
    statement: 'Um bump parcial nao entra em commit nesta maquina'
    criteria:
      - id: C-07
        statement: 'commit com bump so no pyproject e recusado em clone de prova'
      - id: C-11
        statement: 'commit com arvore sincronizada e aceito no clone de prova'
  - id: REQ-05
    statement: 'A copia do PATH esta coerente'
    criteria:
      - id: C-08
        statement: 'as tres leituras de versao da copia do PATH (--version, __version__, metadata) sao iguais entre si'
      - id: C-12
        statement: 'doctor nao acusa problema na copia do PATH'
  - id: REQ-06
    statement: 'O aprendizado fica rastreado'
    criteria:
      - id: C-09
        statement: 'TRACKER 0008 registrado com evidencias'
      - id: C-13
        statement: 'o gatilho CRG-BUMP-UMA-FONTE aparece em napkin.md, GATILHOS-VIVOS.md, AGENTS.md'
      - id: C-14
        statement: 'os itens do registry ficam registrados no TRACKER do registry'
plan:
  - 'A-01 RED: testes novos antes do conserto, com o motivo previsto'
  - 'A-02 tools/release_version.py + regressao por mutacoes historicas'
  - 'A-03 mover os 12 stamps para 2.4.0+dex.3 e ver GREEN'
  - 'A-04 integracao na copia instalada (suite packaging)'
  - 'A-05 gate: pre-commit no indice + job no ci.yml + controle positivo'
  - 'A-06 publicar com vigia ate o CI verde'
  - 'A-07 reinstalar no PATH e conferir canais e doctor'
  - 'A-08 rastro e fechamento'
tasks:
  - id: A-01
    action: 'Escrever os testes novos e roda-los antes do conserto, registrando o motivo esperado antes da execucao'
    covers: [REQ-02]
    done_when: [C-03]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-03]
        method: command
        procedure: 'python -B -m pytest tests/test_documentation.py tests/test_doctor.py tests/test_packaging.py -m "packaging or not packaging" -k "release_version or installed_copy or same_everywhere or python_module_entry or hooks_install_writes" -q'
        expectation:
          kind: command_exit
          expected_exit_code: 1
  - id: A-02
    action: 'Criar tools/release_version.py com a lista de stamps e a checagem por funcao de leitura, e a regressao parametrizada pelas mutacoes historicas'
    covers: [REQ-02]
    done_when: [C-04, C-10]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-04, C-10]
        method: command
        procedure: 'python -B -m pytest tests/test_documentation.py -k "release_version" -q'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Mover os 12 stamps para 2.4.0+dex.3, incluindo a linha do pacote raiz no uv.lock'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-01]
        method: command
        procedure: 'python -B tools/release_version.py --check'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Fazer o teste de empacotamento aceitar versao local e afirmar os canais iguais no venv limpo'
    covers: [REQ-03]
    done_when: [C-05, C-15]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-05, C-15]
        method: command
        procedure: 'python -B -m pytest tests/test_packaging.py -m packaging -k "same_everywhere or installed_copy" -q'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-05
    action: 'Chamar a checagem no pre-commit (indice), criar o job no ci.yml e provar a recusa em clone de prova'
    covers: [REQ-04]
    done_when: [C-07, C-11]
    depends_on: [A-02, A-04]
    evidence_requirements:
      - id: ER-05
        proves: [C-07]
        method: command
        procedure: 'git -C <clone de prova> commit com bump so no pyproject: exit diferente de 0 com a mensagem da checagem'
        expectation:
          kind: command_exit
          expected_exit_code: 1
      - id: ER-09
        proves: [C-11]
        method: command
        procedure: 'git -C <clone de prova> commit com arvore sincronizada: exit 0'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-06
    action: 'Regenerar o PLAYBOOK, commitar com identidade dex-agent, empurrar com vigia e esperar o CI'
    covers: [REQ-01, REQ-03]
    done_when: [C-02, C-06]
    depends_on: [A-05]
    evidence_requirements:
      - id: ER-06
        proves: [C-02, C-06]
        method: command
        procedure: 'gh run view <run> -R dex-agent/dex-code-review-graph --json conclusion,jobs'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-07
    action: 'Conferir a procedencia do wheel do PATH, reinstalar a partir da arvore consertada e rodar doctor'
    covers: [REQ-05]
    done_when: [C-08, C-12]
    depends_on: [A-06]
    evidence_requirements:
      - id: ER-07
        proves: [C-08, C-12]
        method: command
        procedure: 'code-review-graph --version, __version__ e metadata do venv do tool, depois code-review-graph doctor'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-08
    action: 'Registrar TRACKER 0008, napkin, GATILHOS-VIVOS, plaquinha e itens do registry'
    covers: [REQ-06]
    done_when: [C-09, C-13, C-14]
    depends_on: [A-06]
    evidence_requirements:
      - id: ER-08
        proves: [C-09, C-13]
        method: command
        procedure: 'rg -n "CRG-BUMP-UMA-FONTE" .agents/napkin.md .agents/GATILHOS-VIVOS.md AGENTS.md .agents/TRACKER/INDEX.md'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-10
        proves: [C-14]
        method: command
        procedure: 'rg -n "CRG-BUMP-UMA-FONTE" C:/Users/Administrator/.agents/skills/.agents/TRACKER/INDEX.md'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'CI da main verde no SHA publicado'
  - 'doctor sem problemas na copia do PATH'
  - 'recusa do hook capturada em clone de prova'
  - 'fechamento de bloco com tabela achado-cura, memorias espelhadas e validadas'
risks:
  - 'uv lock pode re-resolver dependencias alem do pacote raiz: mitigacao = so a linha do pacote raiz muda; qualquer outra resolucao para o corte'
  - 'suite packaging precisa de rede para o pip do venv limpo: mitigacao = falha de rede e declarada, nunca virada em skip silencioso'
  - 'janelas paralelas commitando na mesma arvore: mitigacao = fetch antes do push, sem force'
  - 'ci.yml e arquivo do upstream: mitigacao = job isolado no fim do arquivo para conflito de baixo custo'
uncertainties:
  - 'a procedencia do wheel 2.4.0+dex.3 instalado no PATH so e conhecida ao conferir; a reinstalacao depende disso'
  - 'o job novo so prova que roda depois do push; se o runner nao o executar, C-06 fica aberto'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'python -B -m pytest tests/test_documentation.py tests/test_doctor.py -q'
  - 'python -B tools/release_version.py --check'
  - 'gh run list -R dex-agent/dex-code-review-graph --branch main --workflow ci.yml --limit 1'
execution_prompt: |
  /GOAL Executar o Trilho .agents/PLAN-TASKS/2026-11-23-versao-uma-fonte.md no workspace C:/CodexProjetos/code-review-graph: fases A-01 a A-08 sem parar entre fases — RED antes do conserto, tools/release_version.py dono unico da regra com regressao por mutacoes historicas, 12 stamps em 2.4.0+dex.3, teste de integracao na copia instalada, gate no pre-commit e job no ci.yml, push com vigia ate o CI verde, copia do PATH coerente com doctor limpo, rastro registrado; verdict no fim.
---

# Versão uma fonte — stamps sincronizados, alarme provado e gate no commit

## Checklist visual
- [ ] A-01 — RED antes do conserto
- [ ] A-02 — `tools/release_version.py` + regressão por mutações
- [ ] A-03 — 12 stamps em `2.4.0+dex.3`, GREEN
- [ ] A-04 — integração na cópia instalada
- [ ] A-05 — gate no `pre-commit` + job no `ci.yml`
- [ ] A-06 — publicar com vigia até o CI verde
- [ ] A-07 — PATH coerente, `doctor` limpo
- [ ] A-08 — rastro e fechamento
