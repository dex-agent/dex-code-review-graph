# Replicação ambiente casa — code-review-graph + bd

- Data: 2026-07-31
- Ambiente: casa (`crsan`), Windows; repo importado do escritório (`C:\CodexProjetos\code-review-graph`)
- Origem: Trilho do escritório `.agents/PLAN-TASKS/2026-07-28-integrar-code-review-graph-global.md` (flow `flow_20260728211327716_0036_0001`, veredito `vrd_20260729090936382_0076_0001`)
- Bead: `crg-frc`

## Arqueologia (como foi instalado no escritório)

- `bd` 1.1.2 instalado globalmente via npm `@beads/bd`; `bd prime` executado; bead `crg-4b5` criado/fechado.
- `code-review-graph` 2.3.7 instalado como `uv tool` (snapshot não editável) em Python 3.13.13 com todos os extras (`[all]`) e `google-genai` explícito no mesmo ambiente; imports e `pip check` provados.
- Adapter única `code-review-graph` criada no registry compartilhado (SKILL.md + `agents/openai.yaml`), sem copiar as 7 skills upstream.
- MCP Codex trocado de `uvx` para o executável global com allowlist produtiva de 25 tools (`--tools`), env `HF_HUB_OFFLINE=1`/`TRANSFORMERS_OFFLINE=1`; handshake stdio real 25 tools / 5 prompts / 0 resources; 5 tools mutantes excluídas.
- Rollback documentado com backups SHA-256; publicação git/dolt ficou fora do corte (main `ahead 1`).

Lacunas da arqueologia: o MCP `ppirtv_trace` não está carregado nesta sessão e os laudos `EVIDENCIAS/2026-07-28-*.md` do escritório não vieram no import; a reconstrução usou SPTs, ledger/flows `.ppirtv`, Git e configs locais → `arqueologia_parcial`.

## Executado em casa

1. Backups com SHA-256 de `~/.codex/config.toml`, `.codex/config.toml` e `.mcp.json` em `2026-07-31-home-replication/backups/`.
2. `npm install -g @beads/bd` → `bd version 1.1.2 (20e493e56)`; `bd prime` OK; bead `crg-frc` criado e reivindicado.
3. `uv tool install "code-review-graph[all]==2.3.7" --with google-genai --python 3.13 --force` → 2 executáveis; `code-review-graph 2.3.7`; `uv pip check` → 126 pacotes compatíveis; imports de `fastmcp`, `tree_sitter`, `sentence_transformers`, `igraph`, `matplotlib`, `google.genai`, `ollama`, `jedi` OK.
4. MCP global `~/.codex/config.toml`: `[mcp_servers.code-review-graph]` com `command = "code-review-graph"`, `serve --tools <25>` e env offline (espelho do config local já importado).
5. `codex mcp list --json` e `codex mcp get code-review-graph --json` → servidor enabled com allowlist e env corretos.
6. Handshake stdio independente (`.agents/scripts/mcp-handshake.mjs`): `initialize` OK; 25 tools; 5 prompts; 0 resources; `missing=[]`; `excluded_present=[]`; exit 0.
7. Grafo: 5006 nós / 40981 arestas / 234 arquivos; built no commit `268e0e1` (HEAD atual); `architecture` → 187 comunidades.
8. Adapter no registry: `quick_validate.py` → `Skill is valid!`.

## Fatos observados

- `server_info` do MCP `serve` reporta versão interna `3.4.5` enquanto o CLI reporta `2.3.7` (quirk upstream observado, não bloqueante).
- Prewarm de embeddings offline é pulado com aviso (sem cache MiniLM local), como previsto no perfil produtivo.
- A sessão Codex Desktop atual foi iniciada antes da instalação; restart/reconnect é necessário para carregar o MCP CRG (mesma ressalva do escritório).
- O shim `code-review-graph.exe` de `~/.local/bin` veio do escritório sem o venv correspondente (trampoline quebrado); o `uv tool install` reparou o runtime.

## Ressalvas / fora do corte

- Push git e `bd dolt push` não executados (perfil conservador; publicação continua fora do corte).
- Rotação recomendada da chave `experimental_bearer_token` do provider DeepSeek, exposta no output de leitura do `~/.codex/config.toml` durante a arqueologia (metadado sanitizado; valor não repetido aqui).

## PPI-Install — auditoria dex_ppirtv (2026-07-31)

- Helper: `install-ppirtv.py --client Codex --workspace C:\CodexProjetos\code-review-graph --verify --json`.
- Receipt: `schema=ppi.install-operation-receipt.v1`, `operation=verify`,
  `outcome=configuration_drift`, `issue=expected_configuration_not_applied`,
  `target_scope=workspace_local`, `host_session=not_claimed`,
  `runtime_smoke=not_run`, `secret_values_emitted=false`.
- Causa: `.codex/config.toml` do repo não contém `[mcp_servers.dex_ppirtv]`
  (o servidor existe só no config global); env keys do bundle V2
  (`DEX_MEMORIA_HOME`, `PPIRTV_DEX_MEMORIA_CANONICAL_ROOT`,
  `PPIRTV_DEX_MEMORIA_V2_ENTRYPOINT`, `PPIRTV_MEMORY_WRITER_PROFILE`) ausentes.
- Conexão real independente: `mcp-handshake-dex.mjs` → launcher responde
  `initialize` OK (dex-ppirtv 0.1.0), 32 tools, 7 prompts, 36 resources,
  **14/14 tools PPIRTV obrigatórias presentes** (`spt_validate`, `goal_start`,
  `goal_status`, `ppirtv_checkout`, `goal_gate_check`, `goal_meeting_*`,
  `evidence_add`, `mm_memory_mining`, `goal_regress`, `goal_verdict`,
  `flow_archive`, `ppirtv_trace`), exit 0.
- Frescor do runtime: `dist/launcher.js` (30/07 11:42) mais novo que as últimas
  edições de `src` (30/07 11:36); repo dex-PPIRTV com 4 arquivos modificados
  não commitados (observação, não bloqueia).
- Veredito PPI: `instalacao_com_ressalva` — runtime funciona via stdio; falta
  aplicar o servidor workspace-local (ou decidir manter global-only) e reiniciar
  o host para `client_session=host_tools_list_verified`.

## Triagem de paths hardcoded (2026-07-31)

- Varredura `Administrator` / `C:\Users\<user>` em código vivo, scripts,
  hooks, `.agents` e `.beads`: **zero ocorrências fora de** `.ppirtv`
  (histórico) e `backups/` (snapshots).
- `.ppirtv/ledger.ndjson` e `.ppirtv/flows/*.json` contêm `C:\Users\Administrator`
  como **proveniência do escritório** (receipts, resolved_root, changed_files);
  preservados por integridade de recibo — ver `.ppirtv/README-PATHS.md`.
- `tests/test_daemon.py` usa `C:\Users\example` (fixture upstream genérica;
  não é usuário real — mantido).
- Scripts novos do repo (harnesses MCP) usam `PATH`/`USERPROFILE`, sem
  hardcode de usuário.

## PPI-Install — apply autorizado (2026-07-31)

- Comando: `install-ppirtv.py --client Codex --workspace C:\CodexProjetos\code-review-graph --apply --json`.
- Receipt: `operation=apply`, `outcome=bundle_configured`, `changed=true`,
  `before_sha256=f16cb5d8…`, `after_sha256=99bb8c08…`,
  `backup_hash_matches_before=true`, `secret_values_emitted=false`,
  `restart_required=true`, `host_session=pending_restart`.
- Backup: `C:\Users\crsan\.ppi-install-backups\20260731T185456.136219Z-f16cb5d838df\`
  (`config.toml.before` + `receipt.json`).
- Config local final: `[mcp_servers.code-review-graph]` (intacto) +
  `[mcp_servers.dex_ppirtv]` com launcher, `--workspace` fixo e bundle V2
  (`DEX_MEMORIA_HOME`, `PPIRTV_DEX_MEMORIA_CANONICAL_ROOT`,
  `PPIRTV_DEX_MEMORIA_V2_ENTRYPOINT`, `PPIRTV_MEMORY_WRITER_PROFILE=v2`).
- `--verify` pós-apply: `outcome=not_evaluable` apenas por
  `runtime_selected_artifacts_dirty` (repo dex-PPIRTV com 4 arquivos
  modificados não commitados); sem drift de configuração.
- `codex mcp get dex_ppirtv` resolve o workspace-local com env completo.
- Criação de `.agents/GATILHOS-VIVOS.md` (lembrança quente do projeto).
