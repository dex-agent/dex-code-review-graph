# Napkin tático — code-review-graph (casa)

Runbook operacional curto. Item forte = `[LOCALIZADOR] regra -> Faça em vez
disso:`.

- [CRG-REPO-PRIVADO] Publicar corte da casa -> confirmar `origin=dex-agent/dex-code-review-graph` privado e `upstream=tirth8205/code-review-graph`; revisar stage. Configs, backups, `.ppirtv` e caches locais estao ignorados. Origem publica nao e destino de push desta edicao.
- [CRG-HIGIENE-README-EXEMPLOS] Aviso de path fixo no README -> abrir as linhas antes de alterar. `/home/user/project-a` e `C:\\path\\to\\...` sao exemplos genericos de instalacao; registrar a classificacao.

- [CRG-TRAMPOLINE] `code-review-graph` falha com `uv trampoline failed to
  canonicalize script path` -> Faça em vez disso: reinstalar o runtime
  `uv tool install "code-review-graph[all]==2.3.7" --with google-genai
  --python 3.13 --force`; nunca editar shims de `~/.local/bin` à mão.
- [CRG-HANDSHAKE] Provar MCP CRG/dex_ppirtv -> Faça em vez disso: rodar
  `node .agents/scripts/mcp-handshake.mjs` e
  `node .agents/scripts/mcp-handshake-dex.mjs` (stdio real); config/arquivo não
  prova sessão.
- [PPI-CODEX] Verificar/instalar dex_ppirtv -> Faça em vez disso:
  `python C:\Users\crsan\.agents\skills\ppi-install\scripts\install-ppirtv.py
  --client Codex --workspace <WS> --verify --json`; `--apply` somente com
  autorização explícita (backup/rollback automáticos em
  `C:\Users\crsan\.ppi-install-backups`).
- [PATHS-PORTATEIS] Scripts/configs novos -> Faça em vez disso: `$env:USERPROFILE`
  (PowerShell), `%USERPROFILE%` (bat) ou `process.env.USERPROFILE` (Node);
  nunca `C:\Users\crsan` fixo em script novo; `.ppirtv` histórico não reescrever.
- [GRAPHIFY-RECALL] Consulta semântica de memória/gatilhos -> Faça em vez disso:
  corpus controlado em `.agents/GRAPHIFY/<id>/corpus`, `graphify <corpus>
  --mode deep`, `graphify query "<pergunta>" --graph
  ".agents/GRAPHIFY/<id>/graphify-out/graph.json"`, confirmar cada hit na fonte
  viva; atualizar catálogo com `scan_graphify_registry.py`.
- [BD-SESSAO] Fechar bloco no repo -> Faça em vez disso: `bd prime`, fechar
  beads abertos com motivo, reportar; push git/`bd dolt push` somente com
  autorização (perfil conservador).

