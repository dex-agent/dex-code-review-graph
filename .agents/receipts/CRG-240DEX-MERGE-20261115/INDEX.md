# INDEX — CRG-240DEX-MERGE-20261115

Versão combinada 2.4.0-dex (casa 2.3.7 + upstream/main fresco `7ba9d17a`).
Trilho: [2026-11-15-crg-240-dex-merge](../../PLAN-TASKS/2026-11-15-crg-240-dex-merge.md).
Flow: `flow_20261115215507246_0807_0001`.

## Recibos

- [LAUDO.md](LAUDO.md) — laudo executivo do corte.
- [c01-c03-joias.txt](c01-c03-joias.txt) — merge commit/pais + joias no cli.py (C-01..C-03).
- [c05-schema15.txt](c05-schema15.txt) — banco novo schema_version 15, 20.411 nós (C-05).
- [c06-canario.txt](c06-canario.txt) — canário AprendizadoConsultado: 1.341 Test, 9.141 TESTED_BY, tests_for(run)=3 (C-06/C-07).
- [c07-testsfor.txt](c07-testsfor.txt) — tests_for(_parse_unified_diff)=11 no repo mesclado (C-07).
- [c08-detect-files.txt](c08-detect-files.txt) — detect-changes --files 35/35 no escopo do diff (C-08).
- [er07-wheel.txt](er07-wheel.txt) — wheel `code_review_graph-2.4.0+dex.1-py3-none-any.whl` (C-09).
- [c04-suite.txt](c04-suite.txt) — suíte A/B: merged vs upstream baseline puro (C-04).

## Ambiente

- venv isolada `.venv-240dex` (editável) e `.venv-base` no clone fresco `crg-upstream-fresh`.
- Índices descartáveis: `CRG_DATA_DIR` em Temp (repo CRG + AprendizadoConsultado) — nenhum índice persistente tocado.
- Logs completos das suítes: `Temp/suite-240dex-full.log` e `Temp/suite-upstream-baseline.log` (não versionados; números finais no c04-suite.txt).
