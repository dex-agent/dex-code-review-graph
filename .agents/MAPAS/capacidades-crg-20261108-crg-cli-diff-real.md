---
fotografia_id: 20261108-crg-cli-diff-real
observed_at: '2026-11-08T16:23:51-03:00'
revision: bccd04a76f49f0af72ecb4f4c293b5dd12bb7b53
owner: mantenedor CRG
---

# Capacidades da CLI em um diff real

| Operação | Resultado observado | Fonte |
| --- | --- | --- |
| Build no pai e update em 573580b | Um arquivo atualizado e SHA do índice igual ao checkout alvo. | [Status e índice](../receipts/crg-cli-diff-real/index.json) |
| Detectar com `--files code_review_graph/tools/query.py` | Um símbolo, `query_graph`, linhas 228–690. As três faixas do Git caem dentro dele. | [Git e AST × JSON](../receipts/crg-cli-diff-real/comparison.json) |
| Consultar chamadores | 41 retornados, incluindo `query_graph_tool`, confirmado no código. | [JSON](../receipts/crg-cli-diff-real/callers_of.json) |
| Consultar testes | 42 retornados, sem truncamento. O teste que passa pelo ramo `references_to` ficou de fora. | [JSON](../receipts/crg-cli-diff-real/tests_for.json), [pytest](../receipts/crg-cli-diff-real/test-branch.txt) |

`affected_flows` e `test_gaps` vieram vazios. O primeiro resultado registra
zero fluxos emitidos para o corte. O segundo não atesta a cobertura do ramo.
Escopo parcial, limitado a um commit, um arquivo Python e um índice de teste.
