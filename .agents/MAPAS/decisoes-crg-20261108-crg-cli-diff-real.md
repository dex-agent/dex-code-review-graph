---
fotografia_id: 20261108-crg-cli-diff-real
observed_at: '2026-11-08T16:23:51-03:00'
revision: bccd04a76f49f0af72ecb4f4c293b5dd12bb7b53
mode: historico
---

# Decisões do piloto com diff real

| Decisão | Origem | Efeito observado |
| --- | --- | --- |
| Reusar o commit real 573580b do piloto de query.py. | GO do dono e diff Git com um arquivo. | Comparação limitada às três faixas do ramo `references_to`. |
| Construir no pai, atualizar no alvo e consultar pelo mesmo banco isolado. | Risco de comparar linhas de revisões diferentes. | O status confirma o SHA alvo e o SHA256 do banco persistente permaneceu igual. |
| Comparar símbolos por caminho, nome e intervalo e revisar testes em separado. | Git e AST dão a referência para os símbolos do diff. | Recorte 1/1. Omissão do teste específico registrada em `crg-j6z`. |

[Trilho](../PLAN-TASKS/2026-11-08-crg-cli-diff-real.md) ·
[Patch Git](../receipts/crg-cli-diff-real/git.patch)
