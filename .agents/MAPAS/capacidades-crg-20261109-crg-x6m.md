---
fotografia_id: 20261109-crg-x6m
revision: fb9fc22da3d1966f5754d9db7938cd4b0ad8caba
observed_at: 2026-11-09
---

# Capacidade de atribuição PHP por classe

| Cenário | Baseline | Corte comprovado |
| --- | --- | --- |
| Payments ausente e Shipping homônimo | Associação indevida no SQLite e na CLI | Zero CALLS e TESTED_BY para Shipping |
| Shipping importado sob outro alias via Composer | Fallback genérico também podia ligar método e construtor ao homônimo | Identidade lexical protege os dois pontos |
| Adição exclusiva de Payments | Aresta errada podia sobreviver ao update | Update, repetição e rebuild produzem as mesmas arestas para Payments no mesmo SHA |

Owner mantenedor CRG. [RED](../receipts/crg-x6m/red.json) · [Prova CLI e SQLite](../receipts/crg-x6m/cli.json). Índice persistente exige a rota de adoção por backup e rebuild.
