---
fotografia_id: 20261108-crg-indice-persistente
observed_at: '2026-11-08T21:40:30-03:00'
revision: 04fcb050275595bb096d1371f6be7d9305c08913
owner: mantenedor CRG
---

# Capacidades verificadas no índice persistente

| Operação | Resultado | Evidência |
| --- | --- | --- |
| Backup SQLite online | Snapshot da revisão 268e0e1, íntegro e com SHA256 registrado. | [Backup](../receipts/crg-indice-persistente/backup.json) |
| Build pela CLI do checkout | Banco ativo na revisão 04fcb05, SHA confirmado contra Git e quick_check ok. | [Build](../receipts/crg-indice-persistente/proof-build.json) |
| Consulta qualificada de `query_graph` | Teste de `references_to` aparece com `indirect: false` e uma aresta `TESTED_BY` para o arquivo exato. | [Associação](../receipts/crg-indice-persistente/proof-association.json) |

Fotografia do build inicial. Após a publicação documental, o status final
do banco é confirmado pelo recibo local `final-status.json`.
