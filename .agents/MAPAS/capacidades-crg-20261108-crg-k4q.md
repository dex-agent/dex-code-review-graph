---
fotografia_id: 20261108-crg-k4q
revision: 5ec476253c5052fe3227ea1750f51657190cc5dd
observed_at: 2026-11-08
---

# Capacidades observadas no índice isolado

| Operação | Prova observada |
| --- | --- |
| Update incremental | Processou um arquivo alheio, alinhou SHA e preservou Function e zero arestas para o alvo. |
| Backup consistente | Preservou metadado e nós, com integrity_check ok e hash idêntico após rebuild. |
| Rebuild | No mesmo SHA, reclassificou o método como Test e expôs uma associação direta no SQLite e no JSON. |

Owner mantenedor CRG. [Update](../receipts/crg-k4q/update.json) · [Backup](../receipts/crg-k4q/backup.json) · [Rebuild](../receipts/crg-k4q/rebuild.json).
