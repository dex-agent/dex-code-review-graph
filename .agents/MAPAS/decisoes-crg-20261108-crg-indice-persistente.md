---
fotografia_id: 20261108-crg-indice-persistente
observed_at: '2026-11-08T21:40:30-03:00'
revision: 04fcb050275595bb096d1371f6be7d9305c08913
mode: historico
---

# Decisões da reconstrução persistente

| Decisão | Efeito observado |
| --- | --- |
| Resolver o banco pela própria CLI e usar backup online do SQLite. | Snapshot íntegro da revisão anterior sem depender da cópia isolada do arquivo principal em presença de WAL. |
| Rodar build no executável do checkout e verificar o SHA com Git. | A revisão da correção está registrada no status do banco ativo. |
| Consultar o símbolo qualificado e cruzar a saída pública com a aresta gravada. | O teste específico aparece como associação direta em `tests/test_tools.py`. |

[Trilho](../PLAN-TASKS/2026-11-08-crg-indice-persistente.md) ·
[Associação](../receipts/crg-indice-persistente/proof-association.json)
