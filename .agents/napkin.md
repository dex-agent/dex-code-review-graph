# Napkin tático — code-review-graph (casa)

Runbook operacional curto. Item forte = `[LOCALIZADOR] regra -> Faça em vez
disso:`.

- [CRG-NODE-TEST-LEXICAL] Para testar o vínculo de um runner CommonJS, confira o escopo em ECMAScript e a API `node:test` no mentor Node. Use as [referências abertas e a prova de sombra](receipts/crg-commonjs-tests-20261114/INDEX.md#referências-da-linguagem).

- [CRG-BUMP-UMA-FONTE] Bump de versão que mexeu só no `pyproject.toml` (CI
  vermelho em 3 testes, `doctor` acusando a própria cópia de desatualizada,
  `--version` diferente de `__version__`) -> Faça em vez disso: um bump são 13
  arquivos de uma vez; `python -B tools/release_version.py` lista os atrasados
  (`--check` é gate; `--from-index` lê o próximo commit). O hook pre-commit
  recusa commit parcial e o job `release-stamps` do CI roda a checagem no
  fork. Ocorrências: 16/11, 21/11 (`6aa3cb23`), 22/11 (`f86f9920`).

- [CRG-TESTED-BY-MODULO-POR-CAMINHO] `detect-changes` lista "Untested" para
  função de módulo carregado por `spec_from_file_location` (idioma de
  `scripts/` em `tests/test_action_render.py`) -> Faça em vez disso: não
  abra falta de teste por esse relato sem conferir; o `pytest` do arquivo é a
  prova (ISSUE-LOCAL-0009).

- [CRG-PLAYBOOK-CLONE-NOVO-BLOQUEIA] Em clone ou worktree novo, todo commit é
  recusado com `DRIFT DETECTADO (exit 2)` pelo gate do Playbook -> Faça em
  vez disso: rodar `python -B tools/playbook/generate-playbook.py --repo .
  --write` antes de commitar nesse clone, sem levar a projeção regenerada
  junto por engano. Causa: a projeção commitada só é fresca na árvore onde foi
  gerada (hash de bytes brutos) e o hook vai como `100644`. Registry
  ISSUE-LOCAL-0051.

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

## [FECHAMENTO-SCAN-ARMADILHAS] (2026-11-19, garimpo do ciclo)

Três armadilhas do `scan-fechamento.py --workflow-review` pagas ao vivo:
(1) campo `repo` da avaliação resolve como PATH (`Path(repo).resolve()`) —
"code-review-graph" (nome) diverge; usar caminho absoluto do repo;
(2) INDEX local de workflows para `repo_kind: project` mora em
`workflow/INDEX.md` NA RAIZ do repo (fonte workflow_review.py l.157) — e
NESTE repo ele EXISTE (1 receita); declarar sha256 REAL, não null de
"ausente"; `sha256: null` só passa para índice comprovadamente ausente;
(3) medir exit de `cmd | tail` dá o exit do tail — rodar o scan sem pipe
(ou separado) para o número real.
**Faça em vez disso:** gerar workflow-review.json APÓS todas as mutações das
fontes citadas (hash muda junto); conferir `rg -n "local_root" workflow_review.py`
antes de declarar caminho de INDEX.

## [DEX-AUDIO-MOTOR-CONTRATO-NOVO] (2026-11-21, bloco rewrite)

A skill `dex-audio` MUDOU de contrato: a rota viva é
`python -B <REGISTRY>/dex-audio-motor/scripts/motor.py enviar --uso dex-pai --texto-arquivo <resumo.txt> --idempotency-key <chave>`
(recibo JSON com message_id; erros tipados 1-4). A ponte antiga
`~/.dex-agent/skills/dex-agent-audio-summary/scripts/send-dex-agent-audio-summary.ps1`
está **SUPERSEDED** — chamar o .ps1 antigo abre PowerShell e morre sem JSON
(pago 2× em 2026-11-21 sem recibo até ler o SKILL.md do motor).
**Faça em vez disso:** `motor.py resolver --uso dex-pai` para conferir o
contato; `motor.py enviar` para entregar; exigir `message_id` no JSON.

## [ULTIMO-PUSH-EXIGE-WATCH] (2026-11-21, classe 14 do CI)

O push FINAL de um fechamento de bloco também gera run de CI — fechar sem
vigiar o run dele deixou um vermelho 2 dias invisível (44628482990, 11-19).
**Faça em vez disso:** todo push que encerra bloco entra com watch
(background) e o veredito entra no fechamento; vermelho ⇒ classe triada pela
régua, sem esperar o dono perguntar.

- [CRG-SPAWN-WINDOWS-CMD] Suíte spawnada como lista (`["npm","test"]`) no
  Windows morre com `WinError 2` (npm é `npm.cmd`; CreateProcess sem extensão
  não acha) e vira `execution_error` sem veredito — pago no merge-check
  (ISSUE-LOCAL-0006, consumidor: hook do dex-memoria, 2.4.0+dex.1).
  **Faça em vez disso:** resolver o executável com `shutil.which` antes do
  `subprocess.run` (PATH+PATHEXT; `resolve_suite_command` no chokepoint
  `_run_suite`); paths com separador de diretório NÃO reescrever (são
  resolvidos pelo cwd do checkout, não do processo). Prova: RED→GREEN Windows
  real + PATH0006_OK (receipt CRG-0006-WINERROR2-20261121).
