# TOOLSBOOK

code-review-graph (fork dex-agent/dex-code-review-graph): ferramentas examinadas e usadas no Trilho .agents/PLAN-TASKS/2026-11-23-versao-uma-fonte.md. Livro inicial: cobertura parcial declarada, nao inventario do repo.

Fonte autorada: TOOLSBOOK.json. Projecao de leitura; nao editar esta copia.
Checagem mecanica: structural_fresh.
Adequacao semantica e prontidao de commit: nao avaliadas pelo motor.

## Cobertura declarada

Inspecionado:
- tools/release_version.py: lido inteiro, criado e executado neste bloco (--check, --check --from-index, --schema, --usage, --help)
- tools/playbook/hooks/pre-commit: lido e editado; executado pelo git em dois commits e em tres provas de clone
- tests/test_documentation.py e tests/test_packaging.py: consumidores (22 e 2 testes verdes em 2026-11-23)
- code-review-graph 2.4.0+dex.3 no PATH: --version, doctor, update, detect-changes
- chama-o-vigia/scripts/vigia.mjs: vigia do run 45243420297, concluido success
- uv 0.11.16: uv build, uv tool install, uv lock --check

Nao inspecionado:
- scripts/*.py do upstream (8 arquivos) e .agents/scripts: nao examinados neste bloco
- tools/playbook/generate-playbook.py: lido em parte (l.66-70, 229-240, 404-463) e executado (--check, --write); fora de sources porque nao responde a triade (--schema e --usage saem com exit 2). Dono do molde: skill dex-playbook-entrada (registry ISSUE-LOCAL-0045 e ISSUE-LOCAL-0051)
- guarda do toolsbook (reuso.py e ficha-gate.py em tools/dev/, toolsbook-guarda.json) nao implantada: a staging .agents/TEMP com 1842 arquivos bloquearia o gate (PENDENTES CRG-TEMP-RELOCAR e PEND-2026-11-15-TOOLSBOOK)
- gh, git, python, pytest e ruff: usados como ferramentas de plataforma; sem ficha propria neste livro

## release-version

**Estado autorado:** reviewed

**purpose:**
Um dono para a lista dos 13 arquivos onde a versao e escrita e para a regra de que todos concordam com pyproject.toml

**when:**
Bump de versao do CRG; CI vermelho em teste de versao; doctor acusando a propria copia; antes de commitar mudanca de versao; ao escrever teste que precise da lista de stamps ou dos padroes de literal de versao

**how:**
Da raiz do repo: python -B tools/release_version.py [--check] [--from-index]. Em Python: carregar o modulo com importlib.util.spec_from_file_location e chamar release_version_mismatches(read). Consumidores: tests/test_documentation.py, tests/test_packaging.py, tools/playbook/hooks/pre-commit e o job release-stamps de .github/workflows/ci.yml. Python 3.10+ com biblioteca padrao; git necessario so para --from-index.

**inputs:**
Os arquivos do repo que o leitor entrega (arvore de trabalho ou indice do git); nenhuma flag obrigatoria

**outputs:**
Lista das divergencias em stderr, ou 'The version is the same in every file a release moves.'; exit 0 em acordo ou modo relatorio, 1 em divergencia com --check, 2 quando um stamp nao pode ser lido; JSON do contrato em --schema

**risks:**
Somente leitura; nao altera arquivo nem indice. Com --from-index conta so o que esta staged: edicao fora do indice nao entra no gate. O hash desta ficha e dos bytes da arvore de trabalho; checkout com outro fim de linha pode reportar fonte vencida (classe do registry ISSUE-LOCAL-0047).

**owner:**
casa dex-agent (fork dex-agent/dex-code-review-graph); Trilho .agents/PLAN-TASKS/2026-11-23-versao-uma-fonte.md

**next_review:**
Quando STAMP_FILES mudar, quando docs/RELEASING.md ganhar um passo novo, ou quando o comando unico de bump nascer

**capabilities:**
- Listar os arquivos de stamp que divergem do pyproject.toml
- Gate com exit 1 em divergencia (--check)
- Ler o indice do git (--from-index) para julgar o proximo commit, nao o disco
- Biblioteca: release_version_mismatches(read) com leitor injetavel; padroes INIT_VERSION e PYPROJECT_VERSION; lista STAMP_FILES
- Triade: --help, --schema (crg.release_version.v1) e --usage

**not_for:**
- Mover a versao: nao existe bump automatico nem --set (corte seguinte)
- Conferir dependencias do uv.lock alem da linha do pacote raiz
- Rodar com --from-index em pasta sem indice git
- Afirmar que a copia instalada responde um so valor: isso e o teste de empacotamento

**evidence:**
- RED antes do conserto (2026-11-23): 11 divergencias listadas, entre elas __version__ 2.4.0+dex.1 contra pyproject 2.4.0+dex.3 e uv.lock em 2.4.0; GREEN depois: exit 0
- Execucao: tests/test_documentation.py com 22 passed (5 mutacoes historicas, controle negativo, indice contra disco)
- Execucao em clone de prova de b45272a9: bump so no pyproject recusado com exit 1; arvore sincronizada aceita com exit 0
- Execucao no runner: passos do job release-stamps do run 45243420297 concluidos success
- Medida: CC maximo 5 pelo verificar-teto-cc.py da casa; ruff check e ruff format limpos

**Fontes examinadas:**
- `tools/release_version.py` — SHA256 `429ed9e5f06cc7d838e5681c9f8f83e9f5d5dab265cc277daf96f086327d3ca0`

## pre-commit-hook

**Estado autorado:** reviewed

**purpose:**
Gate de commit do repo: recusa commit com a projecao do Playbook desatualizada ou com a versao diferente entre os arquivos de release

**when:**
Todo git commit no clone com core.hooksPath=tools/playbook/hooks; ao investigar commit recusado; ao ativar a trava num clone

**how:**
Ativar: git config core.hooksPath tools/playbook/hooks. O git roda tools/playbook/hooks/pre-commit (POSIX sh) a partir da raiz do repo; o script chama python -B tools/playbook/generate-playbook.py --repo . --check e python -B tools/release_version.py --check --from-index. No Windows roda mesmo com modo 100644 porque core.filemode e false.

**inputs:**
Indice do git e arvore de trabalho do repo

**outputs:**
Texto dos dois gates; exit 0 deixa o commit seguir, exit nao-zero recusa

**risks:**
Bloqueia commits. Nao altera arquivos. Saida declarada: git commit --no-verify, ou regenerar o PLAYBOOK com generate-playbook.py --write.

**owner:**
casa dex-agent; o gate do Playbook e copia instalada do molde da skill dex-playbook-entrada (registry)

**next_review:**
Quando a skill dex-playbook-entrada corrigir o hash de bytes brutos e o modo do hook (registry ISSUE-LOCAL-0051)

**capabilities:**
- Recusar commit quando PLAYBOOK.md ou PLAYBOOK.index.json divergem das fontes
- Recusar commit quando a versao esta dessincronizada, lendo o indice do git
- Rodar os dois gates em toda chamada e devolver exit nao-zero se qualquer um falhar

**not_for:**
- Clone Linux ou Mac: o arquivo esta no indice como 100644 e o git ignora o hook
- Clone novo: a projecao commitada do Playbook da DRIFT (exit 2) e todo commit e recusado ate regenerar
- Substituir o CI: quem commita com --no-verify ou sem hooksPath so e pego depois do push

**evidence:**
- Execucao pelo git nos commits 9153a5ce (amend) e b45272a9: 'FRESCO: projecao bate byte-a-byte' e 'The version is the same in every file a release moves.'
- Execucao em clone de b45272a9 (2026-11-23): commit limpo recusado pelo gate do Playbook com DRIFT exit 2 (defeito anterior, tambem em f86f9920); depois de regenerar, bump parcial recusado pelo gate de versao com exit 1 e commit sincronizado aceito com exit 0

**Fontes examinadas:**
- `tools/playbook/hooks/pre-commit` — SHA256 `ea40fb3e5c69ad40ea3b2e05d5ef4f93068822ba12fa246bd82bfb588b661548`

## code-review-graph-cli

**Estado autorado:** reviewed
**Revisao da fonte:** warning — external_sources_not_checked; reopen the canonical owner

**purpose:**
Consultar o grafo de codigo do repo: o que mudou, o que e afetado e quais testes o grafo enxerga

**when:**
Antes e depois de uma mudanca de codigo; ao revisar um diff; ao conferir as copias instaladas

**how:**
No PATH: code-review-graph <comando>. O grafo vive em .code-review-graph/graph.db do repo consumidor. Nao cadastrar no MCP do Codex (AGENTS local).

**inputs:**
Repo com git e codigo em linguagem suportada; ref de base para detect-changes

**outputs:**
Texto ou JSON do comando; update escreve o grafo no disco do repo consumidor

**risks:**
update escreve no banco local do grafo, ignorado pelo git; doctor e leitura

**owner:**
upstream tirth8205/code-review-graph; fork dex-agent/dex-code-review-graph

**next_review:**
No proximo bump do executavel (gate CRG-BUMP-CONSUMIDORES do AGENTS.md)

**capabilities:**
- detect-changes --base <ref>: funcoes alteradas, lacunas de teste e risco de um diff
- update: atualizar o grafo incremental do repo consumidor
- doctor: saude das copias instaladas, versao e frescor do grafo
- --version

**not_for:**
- Prova de cobertura de modulo carregado por spec_from_file_location: reporta 'untested' para funcoes testadas (ISSUE-LOCAL-0009)
- Substituir pytest

**evidence:**
- Execucao: doctor respondeu 'All good.' com o wheel novo (copia, PATH e grafo em ok)
- Execucao: detect-changes --base f86f9920 listou 27 arquivos e risco 0.65; as 9 lacunas de teste sao falso positivo do grafo (ISSUE-LOCAL-0009)
- Execucao: update processou 319 arquivos apos o conserto e 3 no delta seguinte

**Fontes externas (fora do check local):**
- code-review-graph, dono fork dex-agent/dex-code-review-graph, C:/Users/Administrator/.local/bin/code-review-graph.exe (uv tool instalado de dist/code_review_graph-2.4.0+dex.3-py3-none-any.whl, sha256 c9c18d90115653253a199bfa4f1974e90d92c8d2eb0110ab9c0c518263c4e64c, build de b45272a9), 2.4.0+dex.3; doctor e detect-changes executados em 2026-11-23

**Fontes examinadas:**

## chama-o-vigia

**Estado autorado:** reviewed
**Revisao da fonte:** warning — external_sources_not_checked; reopen the canonical owner

**purpose:**
Vigiar uma espera longa, como um run de CI, em background e trazer o veredito sem travar o turno

**when:**
Toda espera material acima de um minuto: CI, build, teste longo, push

**how:**
node "$USERPROFILE/.agents/skills/chama-o-vigia/scripts/vigia.mjs" --alvo-ci <run> --repo <owner/name> --rotulo <texto> --intervalo <s> --max-espera <s>, sempre em background.

**inputs:**
ID do run e repo, ou os comandos de status, pronto e conclusao; no Windows os comandos rodam via cmd.exe, sem 2>/dev/null e sem aspas internas

**outputs:**
Log do watcher em background e notificacao ao concluir

**risks:**
Somente leitura; mantem um processo node em background ate concluir ou atingir --max-espera

**owner:**
registry de skills (skill chama-o-vigia)

**next_review:**
Quando a skill mudar de interface

**capabilities:**
- Vigiar run de CI com --alvo-ci <id> --repo owner/name
- Vigiar classe livre com --status-cmd, --pronto e --conclusao-cmd

**not_for:**
- Esperas curtas, abaixo de um minuto
- Flags com redirecionamento de shell ou aspas internas, que o cmd.exe quebra

**evidence:**
- Execucao: run 45243420297 vigiado com --intervalo 60 --max-espera 3600; o watcher terminou depois que o run concluiu success

**Fontes externas (fora do check local):**
- chama-o-vigia, dono registry de skills dex-agent/skills, $USERPROFILE/.agents/skills/chama-o-vigia/scripts/vigia.mjs (sha256 comeca eb9c1664e739f71), arvore de trabalho do registry em 2026-11-23 com HEAD 065b4172; run 45243420297 vigiado ate success

**Fontes examinadas:**

## uv

**Estado autorado:** reviewed
**Revisao da fonte:** warning — external_sources_not_checked; reopen the canonical owner

**purpose:**
Construir wheel e sdist do pacote e instalar a copia do PATH a partir de um wheel local

**when:**
Ao republicar a copia instalada do CRG; ao conferir se uv.lock esta em dia com o pyproject

**how:**
Na raiz do repo: uv build --out-dir dist; uv tool install --force C:/CodexProjetos/code-review-graph/dist/<wheel>.

**inputs:**
Arvore do repo e, para o tool, um wheel local

**outputs:**
dist/*.whl e *.tar.gz; ambiente do tool em uv tool dir com uv-receipt.toml

**risks:**
uv tool install --force recria o ambiente do tool; instancia com o executavel em uso trava a troca (AGENTS local)

**owner:**
astral-sh/uv (ferramenta externa)

**next_review:**
Na proxima troca do wheel no PATH

**capabilities:**
- uv build --out-dir dist
- uv tool install --force <wheel> e uv tool dir / uv tool list
- uv lock --check

**not_for:**
- Publicar no PyPI: o fork nao publica

**evidence:**
- Execucao: uv build de b45272a9 produziu o wheel de sha256 c9c18d90115653253a199bfa4f1974e90d92c8d2eb0110ab9c0c518263c4e64c
- Execucao: uv lock --check ficou limpo depois de mover so a linha do pacote raiz

**Fontes externas (fora do check local):**
- uv, dono astral-sh/uv, no PATH, 0.11.16 (135a36367 2026-05-21 x86_64-pc-windows-msvc), usado em 2026-11-23 para build, tool install e lock --check

**Fontes examinadas:**
