---
fotografia_id: 20261109-crg-iu1-julia
revision: 9f1f19be7ee97adf2e5477ae40e9299b925d0d2d
observed_at: 2026-11-09
---

# Decisões históricas do corte Julia

| Decisão | Motivo | Prova |
| --- | --- | --- |
| Derivar o caminho esperado da entrada da fixture | A aresta tinha o alvo semântico esperado nos dois sistemas | [Nós e arestas antes do patch](../receipts/crg-iu1-julia/baseline.json) |
| Verificar também a ausência de autochamada | Um literal POSIX podia tornar o teste negativo insensível no Windows | [Contraprova de autochamada](../receipts/crg-iu1-julia/change.json) |
| Adicionar etapa Julia ao job Windows existente | A CI precisava provar os 27 IDs e expor skips | [Leitura remota por SHA](../receipts/crg-iu1-julia/comparison.json) |
| Manter crg-iu1 aberto e começar pelo grupo forget | Oito IDs permanecem, três no matcher do comando | [Saldo Windows](../receipts/crg-iu1-julia/comparison.json) |

O parser e o formato persistido continuam com a mesma implementação. [Trilho](../PLAN-TASKS/2026-11-09-crg-iu1-julia.md).
