# Laudo — Piloto do adapter do CRG em revisão real (2026-11-14)

Trilho: [2026-11-14-crg-piloto-adapter-revisao-real.md](../../PLAN-TASKS/2026-11-14-crg-piloto-adapter-revisao-real.md) · Flow: `flow_20261114231445529_0771_0001` · GO do dono 2026-11-14 (recomendação oraculo-solid).
Wheel sob prova: candidato `8fd3127cb2e28d4f195f9c8a535efe3d89f0209610fd259c2e0b23957e8adb2c` (venv `crg-2w-execucao/run1/candidate`, sem sentence-transformers).

## A-01 — Ambiente isolado ✅

- Clone descartável do bundle `a9d44a8861b0d322d9611914ef2cdbb63a9e737421c68e9eac9ab068029b8378` em `C:/CodexProjetos/crg-2w-execucao/piloto/dex-whatsapp`, HEAD `eb7d95b11b29fa02384323b9e6bae063a40493dc` (oráculo confere).
- `pip show sentence-transformers` → **ausente** na venv (prewarm incondicional do Windows não tem com que contatar HF).
- Cache HF **antes = 89 arquivos** · **depois = 89 arquivos** → **egress zero, escrita zero**.
- PATH, instalação habitual, MCP e índices existentes **intocados** (CLI sempre por caminho absoluto da venv).

## A-02 — Canário oraculado ✅

| Medida | Valor |
| --- | --- |
| build índice descartável | exit 0, **3s**, 25 arquivos, 242 nós, 2.565 arestas |
| `status` | `current_sha == built_at_commit == eb7d95b11b2…` ✅ |
| suíte `node --test` (3 famílias) | **73 pass / 0 fail / 0 skip** (324ms) |
| `tests/distribution.test.cjs` isolado | **2 pass / 0 fail** |
| rehearsal PREDATOR (mesmo HEAD, node 24.15) | 72/72 (receipt `rehearsal-suite.json`) |
| `query tests_for scripts/install.cjs::install` (CLI) | 1 resultado, **direto** (`indirect: false`), `distribution.test.cjs` **linha 4** |
| SQLite `mode=ro` | `quick_check=ok`; aresta `TESTED_BY install.cjs::install → distribution.test.cjs@L4` **idêntica à CLI** |

**Finding (não bloqueante)**: o "21/21" do LEIA-ME é número defasado — o rehearsal do primeiro host mediu **72/72** e o piloto **73/73** (delta +1 entre node 24.15→24.16). Substância do oráculo (tudo verde + TESTED_BY :4 + HEAD) 100% atendida.

## A-03 — Revisão real medida (diff do commit `5356307`) ✅

- Índice descartável do próprio repo CRG: build exit 0, **10s**, 255 arquivos, 5.163 nós, 43.366 arestas, HEAD `53563070` == current.
- `detect-changes --base HEAD~1`: **33 funções/classe alteradas**, 18 test_gaps, risk score 0.65; saída em `detect-changes-5356307.json` (dir do piloto).
- Gabarito independente (git diff `-U0` → funções com linhas alteradas): 35 itens.

| Métrica | Valor bruto | Após classificação com evidência do diff |
| --- | --- | --- |
| TP | 32 | 32 |
| FN | 3 | **0 real** — os 3 são artefatos do gabarito (docstring de módulo em cli.py; granularidade de intervalo em parser.py; adições de funções novas adjacentes em test_commonjs) — o CRG é que acerta |
| FP | 1 | **0 real** — `CodeParser` é o relatório em grão CLASSE contendo os métodos alterados (informação correta, grão distinto) |
| Precisão / Recall | 97% / 91% | **100% / 100%** contra gabarito corrigido |

O `detect-changes` listou corretamente toda a bateria do merge-check (`_git`, `_text`, `_isolated_graph_git`, `_inspect_merge`, `_run_suite`, `_check`, `check_merge`), a família CommonJS do parser (`_commonjs_test_runner`, `_js_test_runner_export`, `_commonjs_binding`, `_js_scope_binding`, `_js_pattern_binds`, `_is_test_function`, `_extract_calls`) e as 7 funções de teste novas — exatamente o que o commit 5356307 fez.

## A-04 — Reuso das tools master_maximus (sessão `sess_8a7ea947`)

| Tool | Veredicto no piloto |
| --- | --- |
| `grafo_gate.py` (built_at_commit==HEAD + coerência) | **Reuso imediato validado** — a checagem equivalente (`status` HEAD==built + quick_check) foi o gate do canário; nos próximos pilotos, invocar o gate diretamente. |
| `normalize_name()` (index duplo nome+linha) | **Candidato** — não exigido neste piloto (nomes bateram literais); adotar quando cruzar fontes heterogêneas. |
| Lições `callers_of` cego a tests/ · FTS falso-negativo | **Respeitadas** — nenhum código-morto concluído; TP/FP/FN calculado contra gabarito independente, não contra FTS. |

## Veredicto do piloto

O adapter do CRG (wheel `8fd3127c`) **destravou a revisão real**: canário oraculado verde nas duas vias (CLI+SQLite), revisão medida com precisão/recall efetivos 100% contra gabarito corrigido, ambiente 100% isolado com egress zero, tempos íntegros (build 3–10s). **Pronto para promoção a rota de revisão da casa** — decisão de instalação permanente pertence ao dono.

Ressalvas: (1) número "21/21" do LEIA-ME defasado (real: 72/72→73/73); (2) grão classe-vs-função do `detect-changes` deve ser documentado para consumidores; (3) gabarito por heurística de intervalo precisa de refinamento se vier a ser ferramenta (não é — ferramenta sob prova era o CRG).
