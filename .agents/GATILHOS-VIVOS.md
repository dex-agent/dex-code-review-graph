# Gatilhos Vivos — code-review-graph (ambiente casa)

Índice quente de reuso da janela de contexto atual. Fonte viva: laudo
`.agents/EVIDENCIAS/2026-07-31-code-review-graph-home-replication.md`, Trilhos em
`.agents/PLAN-TASKS/`, memória governada no vault (`temas/mcp`, `temas/ppirtv`,
`temas/codex`, `global`) e `.ppirtv/README-PATHS.md`.

Regra: cada linha é `[TRIGGER] sintoma -> ação -> fonte/validação`. Atualizar
este arquivo quando um gatilho mudar de estado (resolvido, supersedido ou novo
material). Achado Graphify só vira fato após abrir a fonte (`source: graphify`
até lá).

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
