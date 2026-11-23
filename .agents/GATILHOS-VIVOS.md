# Gatilhos Vivos — code-review-graph (ambiente casa)

Índice quente de reuso da janela de contexto atual. Fonte viva: laudo
`.agents/EVIDENCIAS/2026-07-31-code-review-graph-home-replication.md`, Trilhos em
`.agents/PLAN-TASKS/`, memória governada no vault (`temas/mcp`, `temas/ppirtv`,
`temas/codex`, `global`) e `.ppirtv/README-PATHS.md`.

Regra: cada linha é `[TRIGGER] sintoma -> ação -> fonte/validação`. Atualizar
este arquivo quando um gatilho mudar de estado (resolvido, supersedido ou novo
material). Achado Graphify só vira fato após abrir a fonte (`source: graphify`
até lá).

## Regras do bloco do PR #6 (promoção do napkin, 2026-11-23)

Atualização em 2026-11-23. Trilho: `.agents/PLAN-TASKS/2026-11-23-revisao-pr6.md`.

- [ARTEFATO-EM-TEMP-EXIGE-DESTINO-DURAVEL] Pasta, script, worktree ou clone
  criado em `/tmp`, `%TEMP%` ou `mktemp -d` -> decidir o destino na hora, no
  mesmo bloco: ferramenta em `tools/` com ficha, evidência em
  `.agents/receipts/`, ou descarte declarado; gravar o aprendizado antes de
  seguir. No fechamento, conferir `git worktree list` e a Temp do sistema: o
  `/tmp` do Git Bash nesta máquina é `%LOCALAPPDATA%\Temp\16\`. ->
  Fonte/validação: memória global `ARTEFATO-EM-TEMP-EXIGE-DESTINO-DURAVEL`;
  `tools/parser_diff.py` como exemplo de promoção; registry ISSUE-LOCAL-0053
  (o fiscal de fechamento ainda é cego para a Temp do sistema).
- **E se??** o artefato já está na Temp e o bloco acabou? -> Resgatar antes de
  qualquer limpeza, declarar destino durável ou descarte, e só então apagar;
  apagar dado não atribuído exige palavra do dono.
- [CRG-RECEIPTS-NAO-RASTREAR] Commit de evidência sob `.agents/receipts/` ->
  nunca `git add -f`: a guarda
  `tests/test_install_outputs_are_ignored.py::test_no_tracked_file_is_ignored`
  proíbe arquivo rastreado em caminho ignorado e derruba a main. Evidência
  pequena que precisa viajar ganha exceção `!` explícita no `.gitignore`, no
  mesmo commit. -> Fonte/validação: run 45256809972 (vermelho) e cura
  `b9976bd3` (run 45258942044); antes do push de commit com `.py` rastreado,
  rodar `python -B -m pytest tests/test_install_outputs_are_ignored.py
  tests/test_documentation.py -q`.
- [DADO-HERDADO-DE-RESUMO-E-HIPOTESE] Número, veredito ou achado que veio de
  resumo de contexto, de memória ou de outra sessão -> re-executar a evidência
  nesta sessão antes de usar em veredito ou fechamento; o que a fonte refuta
  entra como REFUTADO, não some. -> Fonte/validação: memória global
  `DADO-HERDADO-DE-RESUMO-E-HIPOTESE`; no PR #6 derrubou 1 achado, 2 números e
  1 fato.
- [IDENTIDADE-GIT-SEMPRE-DEX-AGENT] Commit de outra máquina com autor
  diferente de `dex-agent <dex-agent@proton.me>` -> re-autorar antes de
  publicar (plumbing `commit-tree` com a árvore idêntica e a data original,
  depois `--force-with-lease`); commit de terceiro de verdade não se
  re-autora. -> Fonte/validação: memória
  `identidade-git-dex-agent-rewrite-20261121`; commits `a9e490ae` e `d3771a6b`
  do PR #6.
- **E se??** a main já recebeu o commit com o email errado? -> Não reescrever
  a main publicada por conta própria: registrar em PENDENTES e levar a
  decisão ao dono (o rewrite de 2026-11-21 foi escolha dele).
- [CRG-RED-ENTRE-WORKTREES] RED de teste que não reproduz com duas árvores do
  mesmo repo -> pytest de uma árvore pode importar o pacote de outra; provar
  RED→GREEN por sonda direta na árvore (`PYTHONPATH=<árvore> python -B
  tools/js_form_probe.py --rotulo <árvore>`), nunca por pytest cruzado entre
  worktrees. -> Fonte/validação: napkin `[CRG-RED-ENTRE-WORKTREES]`;
  `tools/js_form_probe.py` (ficha `js-form-probe`).
- [CRG-SONDA-E-FERRAMENTA] Script de prova ou sonda de parser -> antes de
  criar, `reuso.py` com recibo; ferramenta única em `tools/` com tríade
  (`--help`, `--schema`, `--usage`), teste e ficha no `TOOLSBOOK.json`; nunca
  scripts soltos em `/tmp`. -> Fonte/validação: `tools/js_form_probe.py` e
  `tools/parser_diff.py`; recibos em `.agents/receipts/reuso/`.

## Regras do bloco de higiene (2026-11-23)

Atualização em 2026-11-23. Trilho:
`.agents/PLAN-TASKS/2026-11-23-higiene-staging-toolsbook.md`.

- [TEMP-MAQUINA-STAGING-IMPLICITA] Pedido de "limpar a casa", higiene ou
  fechamento -> a higiene do repo não enxerga a Temp da máquina; partir do que
  já existe: inventário com sha256 e triagem por leitura em
  `~/.agents/skills/.agents/receipts/higiene-temp-maquina-20261123/`
  (`INVENTARIO.json`, `TRIAGEM.md`, `reutilizaveis/`), fila por dono no
  ISSUE-LOCAL-0062 do registry. -> Fonte/validação: 158 itens (138 para a
  lixeira, 18 em voo, 2 ferramentas sem cópia viva); 15 arquivos do merge
  recolhidos e originais removidos com registro em `.agents/LIXEIRA/`.
- **E se??** aparecer arquivo novo na Temp depois da triagem? -> Inventariar de
  novo só o que mudou (hash), ler e classificar; nunca mover arquivo de outra
  janela (o que tem mtime de 22–23/11 está marcado em voo).
- [SHA256SUM-BARRA-ESPURIA] (nome canônico da casa; ficha 5W2H no
  GATILHOS-VIVOS do registry e memória global de 2026-11-19) Comparar dois
  arquivos por hash em Git Bash -> leitura binária (`hashlib.sha256`, modo `rb`)
  ou caminho `/c/Users/...`; nunca `sha256sum | cut` com caminho `C:\...`: o
  utilitário põe `\` antes do hash e o `cut` acusa falso "DIFERENTE". Antes de
  acreditar em alarme, controle positivo (um par diferente precisa ser acusado).
  -> Fonte/validação: 15 falsos "DIFERENTE" medidos em 2026-11-23 neste repo
  (reincidência: o hub do projeto não apontava a ficha); a leitura binária deu
  15 iguais; registro da reincidência no registry ISSUE-LOCAL-0063.
- **E se?? só preciso conferir cópia contra um manifesto?** -> `sha256sum -c`
  com caminho relativo serve; a armadilha é comparar dois caminhos absolutos.

## CRG-BUMP-UMA-FONTE

Atualização em 2026-11-23. Trilho:
`.agents/PLAN-TASKS/2026-11-23-versao-uma-fonte.md`.

- [CRG-BUMP-UMA-FONTE] Bump de versão do CRG, CI vermelho em teste de versão,
  ou `doctor` dizendo que a cópia no PATH é mais nova ou mais velha que ela
  mesma -> Faça em vez disso: `python -B tools/release_version.py` (lista os
  arquivos atrasados; `--check` é gate; `--from-index` lê o próximo commit).
  Um bump mexe em 13 arquivos; commit parcial é recusado pelo hook pre-commit e
  o job `release-stamps` do CI roda a checagem no fork. -> Fonte/validação:
  `tools/release_version.py` (dono único da lista),
  `tests/test_documentation.py` (mutações históricas) e
  `tests/test_packaging.py` (canais da cópia instalada).
- **E se??** O clone não tem `core.hooksPath` ativo, ou o commit passou com
  `--no-verify`? O job `release-stamps` do CI ainda acusa depois do push;
  travar antes do push é proteção de branch, decisão do dono (quiz próprio).
- **E se??** O `uv lock --check` pede outras mudanças além da linha do pacote
  raiz? Isso é o corte do Dependabot, não o bump; pare e registre.

## STALENESS-ARTEFATOS-DERIVADOS

Atualizacao de inventario em 2026-11-08. Os mapas do corte
`20261107-crg-diff-recorte` existem em `.agents/MAPAS/INDEX.md` e preservam a
revisao demonstrada naquele corte. Para usa-los como atuais, confronte os
hashes das fontes e o Git. Graphify continua historico, local e excluido do
clone privado. PLAYBOOK passa a usar o gerador local em `tools/playbook/`
quando instalado neste fechamento, com `--check` antes da consulta.

- **O que:** check de atualidade de qualquer projeção derivada antes de usar
  seu conteúdo como evidência.
- **Por que:** cada derivado fotografa fontes em um corte. Fonte posterior à
  geração torna a fotografia velha para uso atual e pode produzir falso verde.
- **Como:** antes de abrir o conteúdo, identifique o conjunto real de fontes
  e leia só a proveniência do derivado. Registre três números na mesma base
  UTC: **F**, segundos Unix da alteração mais recente da fonte; **A**, segundos
  Unix da geração do artefato; **Δ = F − A**, em segundos. Use
  `git log -1 --format=%cI -- <fontes>` para as fontes rastreadas e
  `(Get-Item -LiteralPath $filePath).LastWriteTimeUtc` para mudanças locais
  ou fontes sem Git. Confira staged, unstaged e não rastreados no recorte;
  inclua mtime apenas das fontes pertinentes. Para converter uma data com fuso,
  use `([DateTimeOffset]$instante).ToUnixTimeSeconds()`. Se Δ > 0,
  marque **STALE**, regenere pela rota abaixo, repita o check e só então cite.
  Conferir também SHA/fingerprint, escopo, versão e links quando aplicáveis;
  divergência material mantém o derivado pendente mesmo com Δ ≤ 0. Um mtime
  de cópia ou uma data sem hora/fuso não prova a geração: recupere o recibo
  ou registre Δ indeterminado. Preserve fotografias históricas e gere novo
  corte para responder sobre o estado atual.
- **Quando:** antes de toda leitura/citação como fonte derivada, inclusive
  janela fria, re-arqueologia e decisões que usem grafo, projeção ou recibo.
  Leia este gatilho antes de consumir os índices derivados do bootstrap.
- **Onde:** este hub e o inventário abaixo. Comandos são relativos à raiz
  deste repo, salvo indicação. A coluna de atualização é para uso futuro
  quando o check exigir, não para a instalação do gatilho.
- **E se??**
  - **Sem Git?** Compare o maior mtime UTC dos arquivos-fonte com o timestamp
    da geração. Identifique também adições e remoções no conjunto de fontes.
  - **STALE e ferramenta de regeneração ausente ou incompatível?** Marque
    **não consultável**, não cite números do derivado e use a fonte viva.
    Estacione a recuperação com owner e quando; instale só pela rota do owner.
  - **Verde, mas o conteúdo parece errado?** Atualidade não prova semântica.
    Abra a fonte e confronte a alegação. Fonte viva sempre vence memória.
  - **CRG com SHA igual após mudança de parser?** Confirme `kind/is_test`,
    a aresta `TESTED_BY` entre os nomes qualificados e o JSON `tests_for`
    para um caso conhecido. Um update de arquivo alheio pode manter o nó antigo.
    Para adotar a semântica nova, confirme o banco ativo, faça backup consistente
    pela API SQLite e verifique `PRAGMA integrity_check`. Com o rebuild
    autorizado, rode `code-review-graph build --repo <repo>` e repita as
    três verificações no mesmo SHA. [Prova isolada](PLAN-TASKS/2026-11-08-crg-k4q-frescor-indice.md).
  - **CRG com embeddings existentes?** Semeie o candidato isolado com o backup SQLite antes do build. Compare o estado auxiliar e os vetores das fontes de hash igual. Um build a partir de banco vazio pode passar no controle funcional e perder a tabela de embeddings. [Memória operacional](memorias/crg-rebuild-preserva-embeddings-no-candidato-isolad-ddbe87c32bec.md).
  - **SHA diferente com alteração só documental?** Confira o diff e o recorte.
    O banco continua sendo um corte antigo; se o consumidor exige o HEAD,
    atualize antes de citá-lo como atual.

### Inventário e rotas

| Derivado encontrado | Proveniência e check de leitura | Regeneração quando necessária |
| --- | --- | --- |
| CRG: `.code-review-graph/graph.db` | `code-review-graph status --repo .`: Last updated, Built at commit. Confirme a revisão do consumidor com `get_minimal_context_tool` e compare fontes indexáveis com o SHA do build. No inventário de 2026-11-07, o build declarou `2026-07-28T18:28:45` sem offset e `268e0e1`; HEAD `603bdd2` diverge por documentos da receita. | Com backup e banco/data dir efetivo confirmado, `code-review-graph update --repo .` na resolução padrão deste checkout; se precisar reconstruir, `code-review-graph build --repo .`. Se a resolução mudar, use `--data-dir` do banco confirmado. Revalide SHA e publique os três mapas conforme a receita local. |
| Graphify: `.agents/GRAPHIFY/gatilhos-crg-2026-07-31/graphify-out/graph.json` e `graphify-out/2026-07-31/graph.json` sob a mesma pasta | `Get-Item` nos dois arquivos para LastWriteTimeUtc; no inventário, `2026-07-31T18:58:41Z` e `2026-07-31T18:58:25Z`. Compare o corpus controlado em `gatilhos-crg-2026-07-31/corpus/` **e** as fontes vivas de que foi copiado, como este hub. O segundo arquivo é um corte datado; não o sobrescreva. | Refaça as cópias sanitizadas a partir das fontes vivas em pasta de corte nova. Do diretório desse corte, use `graphify extract ./corpus --mode deep` com a configuração do owner, depois reconcilie `.agents/GRAPHIFY/INDEX.md` via `catalogar-grafos-graphify`. |
| INDEX curados: `INDEX.md`, `docs/INDEX.md`, `workflow/INDEX.md`, `examples/INDEX.md`, `profiles/INDEX.md` e `references/INDEX.md` dentro da receita local; `.agents/PLAN-TASKS/INDEX.md` e `.agents/GRAPHIFY/INDEX.md` | Use commit do índice ou mtime quando local, compare com mudanças no inventário correspondente, confira alvos e entradas faltantes. Fiscal: `python -B "$env:USERPROFILE/.agents/skills/dex-fechamento-projeto-atualizado/scripts/scan-fechamento.py" --repo .`; também confira links e inventário das subpastas, que o scan geral não certifica. | Índices curados: reconciliar as entradas manualmente com o inventário no disco e repetir o fiscal. Índice Graphify: seguir o catálogo da linha anterior, preservando entradas de outros cortes. |
| CAPACITY: `workflow/code-review-graph-manutencao-iterativa-com-evidencia/CAPACITY.md` | Frontmatter `fotografia_id=crg-piloto-268e0e1-2026-11-07` e `fotografia_date=2026-11-07`. Compare revisão, evidência de `USAGE.md` e estado do alvo; a data sozinha não fornece A em segundos. | Executar a skill `dex-mapa-capacidades` com novos oracles observados, salvar o novo corte em `.agents/MAPAS/`, indexar e reconciliar o CAPACITY da receita quando mudar a capacidade demonstrada. Valide a receita com `check-workflow.py` do owner. |

**Ausentes no inventário de 2026-11-07:** PLAYBOOK.md, PLAYBOOK.index.json,
`tools/playbook/generate-playbook.py`, `.agents/MAPAS/`, DECISION-FLOW local e
`graphify-out/graph.json` na raiz. Sem comando de check local para PLAYBOOK:
quando o mantenedor instalar o playbook pela rota `dex-playbook-entrada`,
usar `python -B tools/playbook/generate-playbook.py --repo . --check` (exit 2 =
drift) e registrar o comando de geração verificado. Os primeiros mapas são
do executor na próxima atualização do CRG; DECISION-FLOW entra no inventário
se o mantenedor adotar essa projeção. Para o Graphify, o CLI instalado emitiu
aviso de versão inferior à skill; o mantenedor confirma compatibilidade na
próxima regeneração, antes de publicar o novo corte.

Rota do catálogo Graphify já registrada neste hub: executar
`scan_graphify_registry.py --roots C:\CodexProjetos <USERPROFILE>\.agents --out <USERPROFILE>\.agents\graphify`
pela skill `catalogar-grafos-graphify`, com revisão do catálogo e do INDEX
local após publicar o corte. A ajuda do script confirma os argumentos.

## A — CRG / MCP (instalação e runtime)

- [CRG-GIT-PATHS-IDENTIDADE] Recorte retorna zero em arquivo alterado com
  espaco ou acento -> confira inventario Git, faixas do patch e filtro CLI
  separadamente. Prova: `uv run --no-sync pytest -q -s tests/test_cli.py -k file_scope`.
  Fonte: [memoria do projeto](memorias/crg-git-paths-identidade.md).

- [CRG-REPLICADO-CASA] CRG 2.3.7 (uv tool Python 3.13, extras `[all]` +
  `google-genai`), bd 1.1.2 (`@beads/bd`), MCP allowlist 25 tools, handshake
  25/5/0 -> se falhar, seguir CRG-SHIM-UV-QUEBRADO -> fonte: laudo +
  memória `mcp` L1 `CRG: replicar install do escritorio em maquina nova`.
- [CRG-SHIM-UV-QUEBRADO] `uv trampoline failed to canonicalize script path`
  -> reinstalar `uv tool install "code-review-graph[all]==2.3.7" --with
  google-genai --python 3.13 --force` (shims de `~/.local/bin` não viajam entre
  máquinas) -> validação: `code-review-graph --version` + `uv tool list`.
- [MCP-TOOLS-LIST-REAL-VIA-STDIO] config/arquivo/docs parecem verdes -> exigir
  `tools/list` real via harness `.agents/scripts/mcp-handshake*.mjs` ou cliente
  carregado -> fonte: tema `mcp` L1.
- [MCP-RESTART-NAO-PRIMEIRA-REACAO] tools ausentes na sessão -> provar stdio
  ANTES de pedir restart; restart é só UI -> fonte: tema `mcp` L1.
- [MCP-SESSION-NAO-PROVA-REPO-LOCAL] tools vivas na sessão ≠ config repo-local
  -> provar config do cliente ativo -> fonte: tema `mcp` L1.
- [CRG-GRAFO-HEAD] grafo importado 5006 nós/40981 arestas no commit `268e0e1`
  -> `code-review-graph status --repo .`; se stale, rebuild com backup (sem
  embeddings) -> fonte: laudo + CLI status.
- [CRG-PREWARM-OFFLINE] startup com sentence-transformers acessa rede -> manter
  `HF_HUB_OFFLINE=1`/`TRANSFORMERS_OFFLINE=1`; sem cache MiniLM falha explícito
  -> fonte: tema `mcp` L2 prewarm.
- [CRG-ALLOWLIST-25] 5 tools mutantes excluídas (`apply_refactor`,
  `build_or_update`, `embed`, `wiki`, `postprocess`) -> nunca expor no perfil
  produtivo; laboratório exige autorização + rollback -> fonte: adapter
  `code-review-graph` + `.codex/config.toml`.

## B — PPI / PPIRTV

- [DEX-PPIRTV-WORKSPACE-LOCAL-V2] dex_ppirtv no `.codex/config.toml` do repo com
  launcher + `--workspace` fixo + bundle V2 (`DEX_MEMORIA_HOME`,
  `PPIRTV_DEX_MEMORIA_CANONICAL_ROOT`, `PPIRTV_DEX_MEMORIA_V2_ENTRYPOINT`,
  `PPIRTV_MEMORY_WRITER_PROFILE=v2`) -> aplicar/verificar via ppi-install;
  backup em `C:\Users\crsan\.ppi-install-backups\20260731T185456*` -> fonte:
  laudo PPI + config.
- [PPI-BUNDLE-CONFIGURED-DIRTY] `bundle_configured` quando repo dex-PPIRTV tem
  artefatos sujos -> não pedir commit; registrar e aguardar restart para
  `host_tools_list_verified` -> fonte: laudo PPI (receipt apply/verify).
- [PPI-VERIFY-POS-APPLY] verify pós-apply `not_evaluable` por
  `runtime_selected_artifacts_dirty` ≠ drift de config -> separar camadas:
  config aplicada (hash mudou) vs trust de runtime (repo sujo) -> fonte: laudo.
- [PPIRTV-MCP-INSTALL-PPI-GRAPHIFY] instalar/configurar dex_ppirtv -> usar
  ppi-install + tools/list real; arquivo não prova -> fonte: tema `ppirtv` L1.
- [PPIRTV-LAUNCHER-WORKSPACE-ISOLATION] launcher resolve workspace consumidor;
  sem sinal falha seguro e não grava `.ppirtv` no repo errado -> fonte: tema
  `ppirtv` L1.
- [SPT-V2-LEITURA-SPT-V3-EXECUCAO] SPT v2 é leitura histórica/retry; execução
  nova exige SPT v3 com `spt_validate` `valid=true` -> não liberar execução nova
  por v2 -> fonte: ancora-fluxo + contrato PPIRTV.
- [PPIRTV-EVIDENCIA-ESTRUTURADA] `evidence_add` exige origin/objective/
  procedure/observed_result -> complementar evidência antes do veredito ->
  fonte: tema `ppirtv` L1.

## C — Paths / portabilidade

- [PATHS-PORTATEIS] código vivo, scripts e docs com `C:\Users\<user>` -> usar
  `$env:USERPROFILE`/`USERPROFILE`/`os.homedir()`; script que precise literal
  usa o usuário do perfil atual -> validação:
  `rg -n -i "administrator" -g "!**/.ppirtv/**" -g "!**/backups/**" .`.
- [PPIRT-HISTORICO-PRESERVAR] `.ppirtv` (ledger/flows) contém paths do
  escritório -> NÃO reescrever: são proveniência com recibos/hashes; reescrita
  exige autorização + backup -> fonte: `.ppirtv/README-PATHS.md`.
- [CODEX-USERPROFILE-PATH-PORTAVEL] memória/prompt/import-export com caminho
  fixo de usuário -> normalizar para `$env:USERPROFILE` quando texto
  operacional -> fonte: tema `codex` L1.

## D — PowerShell / Windows

- [PS-MOTOR-HARNESS-P72] inline grande de PS/Node/CDP falha (try/catch,
  `ConvertTo-Json`, `node -e`) -> harness local validado com `node --check` ->
  fonte: tema `codex` L1.
- [POWERSHELL-QUOTING-VARIAVEIS] `$HOME` read-only ou regex com `$` expandiu ->
  nomes específicos + aspas simples -> fonte: tema `codex` L1.
- [CDP-PORTA-DINAMICA] WebView2/Chrome CDP -> porta livre por run, nunca 9222
  fixo sem exceção manual -> fonte: AGENTS global.

## E — Graphify

- [GRAPHIFY-CORPUS-CONTROLADO] recall de memória/GATILHOS/SPT -> construir
  corpus controlado estreito (`.agents/GRAPHIFY/<id>/corpus`) antes de confiar
  em grafo raiz; `graphify <corpus> --mode deep`; grafo fraco/zero nós ->
  voltar para `rg` + fonte viva -> fonte: graphify SKILL + grafo local
  `gatilhos-crg-2026-07-31`.
- [GRAPHIFY-CONFIRMAR-FONTE] todo hit é `source: graphify` até abrir/cruzar com
  rg, código, docs ou teste -> nunca promover nó direto -> fonte: AGENTS
  `## Graphify local` + skills.
- [GRAPHIFY-CATALOGO] grafo novo/movido -> rodar
  `scan_graphify_registry.py --roots C:\CodexProjetos <USERPROFILE>\.agents
  --out <USERPROFILE>\.agents\graphify` (atualiza registro central, INDEX e
  AGENTS) -> fonte: catalogar-grafos-graphify.
- [GRAPHIFY-LABEL-FALHA-PARSE] community labeling falhou (`Unterminated
  string`) -> fallback `Community N` é aceitável; reter para retry/upstream ->
  fonte: PARK-20260731-05.

## F — Memória / continuidade

- [FECHAMENTO-LENTES-ESPECIALISTAS-PROXIMO-PASSO] fechamento de bloco -> analisar
  com lentes ativas e indicar `Próximo passo recomendado` com motivo/quando ->
  fonte: memória `global` L1.
- [CONTEXT-CLOSE-ORCHESTRATION-GLOBAL] troca de janela/contexto denso -> rota
  `encerramento-contexto-inteligente` + writers governados -> fonte: memória
  `global` L1.
- [MEMORIA-VIVA-GATE] fechamento de Trilho/SPT -> reconciliar
  `.agents/ACTIVE.md`, `.agents/HANDOFF.md`, `.agents/PLAN-TASKS/ACTIVE.md` e
  bootstrap no `AGENTS.md` -> fonte: skill memoria-viva.
- [DEX-MEMORIA-RECUPERAVEL] gravar aprendizado forte -> `dex-memoria v2
  remember` (L1→L2 ou L1→L3) + validação consciencia-memorias/Finder/rg ->
  fonte: tema `global` L1 + skill dex-memoria.
- [GATILHOS-VIVOS-ATUALIZAR] gatilho mudou de estado (novo/resolvido/
  supersedido) -> atualizar este arquivo e `.agents/GRAPHIFY/INDEX.md` quando o
  grafo mudar -> fonte: este arquivo + catalogar-grafos-graphify.

## G — Beads / tracker

- [BD-AGENTES-PROTOCOLO] trabalho no repo -> `bd create` antes de codar, `bd
  update --claim`, `bd close` no fim; perfil conservador: push/dolt só com
  autorização -> fonte: `bd prime` + AGENTS.md do projeto.
- [BD-REMEMBER] conhecimento persistente do tracker -> `bd remember "<insight>"`
  (store próprio do beads, separado do dex-memoria) -> fonte: `bd prime`.

| TRACKER-LOCAL-ONLY | sessão do projeto | commitar fechamento de issue do TRACKER | commitar só PLAN-TASKS; TRACKER é local-only (`git ls-files .agents/TRACKER` = 0) | .agents/napkin.md#TRACKER-LOCAL-ONLY |
| GHCACHE-PR-LIST | sessão do projeto | `gh pr list` logo após close em lote mostra "1 aberto" | re-listar antes de concluir reopen; cache da API devolve stale | .agents/napkin.md#GHCACHE-PR-LIST |

| FECHAMENTO-SCAN-ARMADILHAS | sessão do projeto | montar workflow-review.json ou ler exit do scan de fechamento | repo=path absoluto; INDEX local=workflow/INDEX.md raiz (com sha real); exit sem pipe | .agents/napkin.md#FECHAMENTO-SCAN-ARMADILHAS |

| DEX-AUDIO-MOTOR-CONTRATO-NOVO | sessão do projeto | enviar áudio da burrinha/dex-pai | motor.py enviar --uso dex-pai --texto-arquivo (a ponte .ps1 está SUPERSEDED; exigir message_id) | .agents/napkin.md#DEX-AUDIO-MOTOR-CONTRATO-NOVO |

| ULTIMO-PUSH-EXIGE-WATCH | sessão do projeto | push final de fechamento de bloco | watch (background) do run + veredito no fechamento; add -f de receipt exige negação .gitignore | .agents/napkin.md#ULTIMO-PUSH-EXIGE-WATCH |
