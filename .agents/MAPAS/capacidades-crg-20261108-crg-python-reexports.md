---
fotografia_id: 20261108-crg-python-reexports
observed_at: '2026-11-08T19:43:49-03:00'
revision: 'crg-j6z sobre ad0b736, alvo histórico 573580b'
owner: mantenedor CRG
---

# Capacidades do CRG para reexportações Python

| Consumidor e operação | Resultado observado | Fonte |
| --- | --- | --- |
| Parser, chamada via reexportação explícita | `CALLS` e `TESTED_BY` usam a identidade da definição. Sombra, ciclos e bindings incertos preservam o fallback. | [Pytest focal](../receipts/crg-python-reexports/green-parser.txt) |
| CLI, build e update de uma fachada intermediária | A associação migra para a nova definição. A homônima continua sem teste associado. | [CLI e Git](../receipts/crg-python-reexports/incremental.txt) |
| CLI, consulta de `query_graph` em 573580b | Recupera o teste de `references_to` como direto e preserva a correspondência 1/1 do recorte Git. | [Prova histórica](../receipts/crg-python-reexports/historical.json) |

Cobertura parcial. O limite da consulta é observado no recibo histórico.
O índice persistente ficou fora da fotografia.
