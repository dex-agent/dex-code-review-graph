---
implementation_version: v2
layer: L2
slug: crg-240dex-merge-fechado-20261115-aa9b6b16dbff
tags:
  - "#auto-memory/project"
---

# crg-240dex-merge-fechado-20261115

Espelho da auto-memory do host ZCode (arquivo crg-240dex-merge-fechado-20261115.md, tipo project).

Versão combinada 2.4.0+dex.1 merged/pushed/verdict — aprendizados

Corte 2026-11-15 CONCLUÍDO: versão combinada **2.4.0+dex.1** (casa 2.3.7 × upstream/main
fresco `7ba9d17a`) mergeada em `732b7609` + curas A/B `24195945`, fechamento `4155b870`,
main pushed `3ddf2c8b`. Flow `flow_20261115215507246_0807_0001` COMPLETE, verdict
`vrd_20261115233016729_0849_0001` **pronto_com_ressalvas** (11 evidências; review canônica
`evd_..._0847_0001`). 4 deltas casa preservados (merge-check, detect-changes --files,
PHP identidade de classe, cp1252→upstream utf8). Suíte A/B: zero regressão merge-causada
(36 curadas/classificadas; 407 ambientais Windows presentes no upstream puro). Issues
abertas: crg-41c (`_sum_signals` sem teste), crg-lum (composer-alias xfail).

Aprendizados fortes do corte:
- **Refs locais do upstream podem ser FANTASMA** (`8ac8cdc` não existia mais — história
  reescrita); comparar upstream SEMPRE via clone/fetch fresco antes de planejar merge.
- **`git apply -3` pode escrever marcadores de conflito dizendo "cleanly"** — vacina:
  varredura `grep -c '^<<<<<<<'` + `compileall` após TODA resolução (pegou 3 arquivos
  mutilados antes do commit).
- **`scope_reference` da review estrutural PPIRTV tem que ser path AUTORIZADO dentro de
  `reviewed_targets`** (um dos changed_files, ex. `pyproject.toml`) — workspace path dá
  `scope_reference_not_authorized`; diagnosticar com
  `node -e "import('./dist/gate-resolution.js')...reviewEvidenceDiagnostics(flow, evd)"`.
- **PEP 440**: `2.4.0-dex.1` é inválida; canônica `2.4.0+dex.1` (local version).
- **1 critério = 1 prova** no verdict PPIRTV (co-cobertura ER→2 critérios exige provas
  separadas por criterion_id).

PENDÊNCIA PAGA 2026-11-16 (ordem "troca" do dono): PATH agora executa o wheel
`2.4.0+dex.1` (uv tool --force, janela sem travadores; `--files`/`merge-check`/schema 15/e2e
verificados pelo executável do PATH). Receipt + rotas de rollback em
`.agents/receipts/CRG-240DEX-PATH-20261116/` (rota A PyPI 2.4.0; rota B wheel casa 2.3.7).
Primeira abertura de índice schema-9 migra para 15 — projetos reconstroem índices.
Wheel local: `dist-240dex/code_review_graph-2.4.0+dex.1-py3-none-any.whl` (ignorado, fora do git).

FROTA (rollout iniciado 2026-11-16, origem `origin/main @ 82f1fad3`): comando canônico de
troca nas outras máquinas: `uv tool install --force "git+https://github.com/dex-agent/dex-code-review-graph.git"`
(o uv regrava sozinho o `.exe` do `~/.local/bin`; alternativa offline: `uv tool install --force <caminho-do-clone>`).
Provas mínimas pós-install: `code-review-graph --version` → 2.4.0+dex.1 e
`detect-changes --help | grep -- --files`. Avisos: fechar Codex/serve antes (trava o .exe
no Windows); primeira abertura de índice schema-9 migra pra 15 (ou apagar `.code-review-graph/`
e rebuild); rollback 1 linha `uv tool install --force code-review-graph==2.4.0`.
**Primeira máquina da frota VALIDADA 2026-11-16**: LABORATORIO-POC-DOCS (repo
`C:\DeepProjetos\gerador-variantes-similares`, branch master) — ambas as provas verdes.

Uso do `merge-check` (decisão do dono 2026-11-16 via quiz: **agente evoca** — sem esteira,
sem hook, sem CI; confirmado na fonte que não há wiring automático nenhum): em cada repo da
frota rodar `code-review-graph install` 1x (grava a referência LLM pros agentes) e depois
perguntar em linguagem natural ("posso integrar X com Y sem quebrar?"). Semântica do comando:
3 camadas — texto (`merge-tree`) → grafo da árvore mesclada (risk/flows/test_candidates) →
suíte nos 4 checkouts (base/ours/theirs/merged; verde nos pais + vermelho no merged =
`regression` = conflito de integração que o git não vê). Exits: passed=0, text_conflict/
regression=1, execution_error=2. Contrato: base ancestral dos dois lados; suíte deve passar
nos pais. `merge-check.py` é exclusivo da casa (upstream não tem).
Related: [[crg-path-240-oficial]], [[ppirtv-mcp-stdio-harness-review-envelope]]

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-240dex-merge-fechado-20261115-aa9b6b16dbff-content
