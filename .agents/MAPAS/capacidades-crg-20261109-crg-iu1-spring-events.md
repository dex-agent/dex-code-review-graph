---
fotografia_id: 20261109-crg-iu1-spring-events
revision: d22e6d6a645bcfccfc4f4ed013931f311bcb4631
observed_at: 2026-11-09
---

# Capacidades observadas no corte Spring

| Consumidor | Gatilho | Resultado observado | Limite |
| --- | --- | --- | --- |
| Operador da CLI | Build Java com eventos Spring | Dois CALLS completos e sem cruzamentos em Windows e Ubuntu. | Fixture descartável |
| Mantenedor | Teste de homônimos | Comparação exata rejeita cruzamento e ausência de beta com duas linhas. | Teste Spring |
| CI Windows | Push | Spring 6/6 no run 42730177128. | Passo dedicado |

[SQLite Windows](../receipts/crg-iu1-spring-events/baseline-windows.json) · [SQLite Ubuntu](../receipts/crg-iu1-spring-events/baseline-ubuntu.json) · [Trilho](../PLAN-TASKS/2026-11-09-crg-iu1-spring-events.md).
