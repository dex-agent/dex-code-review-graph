# Napkin tático — code-review-graph (casa)

Runbook operacional curto. Item forte = `[LOCALIZADOR] regra -> Faça em vez
disso:`.

- [CRG-NODE-TEST-LEXICAL] Para testar o vínculo de um runner CommonJS, confira o escopo em ECMAScript e a API `node:test` no mentor Node. Use as [referências abertas e a prova de sombra](receipts/crg-commonjs-tests-20261114/INDEX.md#referências-da-linguagem).

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

- [CI-CAMADAS-OCULTAS] Job de CI falhou e a cura subiu -> Faça em vez disso:
  inventariar o job INTEIRO no `.github/workflows/ci.yml` ANTES do push —
  steps de um job param no 1º erro, então cada cura revela a camada seguinte
  (pago 2x em 2026-11-19: forget/dbt/hcl e depois o teste f145ca80 morto);
  conferir cada node-id citado no workflow contra o repo (`rg` no tests/) e,
  se um commit "sumir" num merge, lembrar que `git log -S` é CEGO a
  remoções em resolução de merge — usar `git branch --contains <sha>` +
  `git show <sha> -- <arquivo>` + `git apply -3` para recuperar.
- [HARNESS-PYTHON-I] Prova in-process do parser/build -> Faça em vez disso:
  `python -c` SEM `-I` — o modo isolado não carrega os language-packs e o
  parser morre em silêncio devolvendo "0 nodes" (falso-negativo de
  INSTRUMENTO medido em 2026-11-19; o produto estava são). Exe de teste
  e2e: `shutil.which("code-review-graph")`, nunca
  `python.with_name(...)` (o script mora em Scripts/, não ao lado do
  interpretador).

## [TRACKER-LOCAL-ONLY] (2026-11-19, bloco 0005)

`.agents/TRACKER/` é **local-only** (0 arquivos tracked; casou .gitignore):
`git add .agents/TRACKER` recusa (exit 1) mesmo para arquivos já editados.
**Faça em vez disso:** commitar apenas `.agents/PLAN-TASKS/*.md` (negado no
gitignore) — o título "docs(tracker)" do 41738e63 só versionou o Trilho.
Confirmação: `git ls-files .agents/TRACKER | wc -l` = 0.

## [GHCACHE-PR-LIST] (2026-11-19, bloco 0005)

`gh pr list --state open` logo após `gh pr close` em lote pode devolver
contagem STALE (mostrou "1 aberto" com 5 fechados) — cache da API, não reopen
do bot. **Faça em vez disso:** re-listar (a 2ª chamada veio vazia) antes de
concluir "o bot reabriu".
