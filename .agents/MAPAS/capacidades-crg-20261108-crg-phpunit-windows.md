---
fotografia_id: 20261108-crg-phpunit-windows
revision: 92fdfe052c2d97755659d1c81a3a1593e204c1c6
observed_at: 2026-11-08
---

# Capacidades do CRG no corte PHPUnit Windows

Owner mantenedor CRG. Consumidor é quem consulta testes de métodos PHP pela CLI. O gatilho é construir um índice com método PHPUnit camelCase sob `tests` em Windows e consultar `tests_for` pelo método de produção.

| Capacidade | Antes | Depois | Oráculo |
| --- | --- | --- | --- |
| Associação direta PHPUnit | Método classificado como Function, zero aresta direta | Método classificado como Test, uma aresta TESTED_BY, JSON com indirect=false | Build e query da CLI cruzados com SQLite em uma fixture isolada |
| Controle de produção | Método testProductionHelper em src é Function | Function preservada | SQLite na mesma fixture |

Ambiente Windows Python 3.13.13. [Trilho](../PLAN-TASKS/2026-11-08-crg-phpunit-windows.md) e [prova](../receipts/crg-phpunit-windows/summary.json). O corte cobre o executável do checkout e a fixture. A validação integral Windows ainda tem 24 falhas conhecidas.
