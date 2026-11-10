---
fotografia_id: 20261109-crg-iu1-dbt-contains
revision: b02a4ba519a05dd30c707bcedd6a2b88575cc81e
observed_at: 2026-11-09
---

# Decisões do corte dbt

| ID | Decisão | Gatilho e fonte |
| --- | --- | --- |
| D-01 | Preservar o RED antes de editar a fixture | O [teste Windows](../receipts/crg-iu1-dbt-contains/red-windows.txt) isolou a comparação literal POSIX |
| D-02 | Corrigir a expectativa e conferir o destino persistido pelo ID bruto | A [prova Windows](../receipts/crg-iu1-dbt-contains/baseline-windows.json) e a [prova Ubuntu](../receipts/crg-iu1-dbt-contains/baseline-ubuntu.json) resolveram os dois endpoints |
| D-03 | Executar o módulo dbt na CI Windows | A [matriz](../../.github/workflows/ci.yml) usa seleção explícita nesse runner |

Owner mantenedor CRG. [Trilho](../PLAN-TASKS/2026-11-09-crg-iu1-dbt-contains.md).
