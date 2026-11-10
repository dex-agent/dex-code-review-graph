---
fotografia_id: 20261109-crg-iu1-dbt-contains
revision: b02a4ba519a05dd30c707bcedd6a2b88575cc81e
observed_at: 2026-11-09
---

# Capacidades observadas da aresta dbt

| Consumidor | Gatilho | Resultado observado | Limite |
| --- | --- | --- | --- |
| Operador da CLI | `build --repo` em projeto dbt | Uma aresta `CONTAINS` liga o arquivo ao modelo `fct_orders`, com ambos os IDs resolvidos no SQLite em cada sistema | Projeto descartável com `ref` |
| Mantenedor de testes | Pytest do módulo dbt | Fixture compara endpoints pela identidade nativa e consulta o nó persistido pelo ID da aresta | Módulo dbt |

[Windows](../receipts/crg-iu1-dbt-contains/baseline-windows.json) · [Ubuntu](../receipts/crg-iu1-dbt-contains/baseline-ubuntu.json) · [Trilho](../PLAN-TASKS/2026-11-09-crg-iu1-dbt-contains.md).
