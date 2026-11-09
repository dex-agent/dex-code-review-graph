---
fotografia_id: 20261109-crg-iu1-raiz-externa
revision: f145ca80519846eb7581bd047188a7054c801be6
observed_at: 2026-11-09
---

# Decisões do corte de raiz externa

| Decisão | Motivo | Prova |
| --- | --- | --- |
| Isolar a fixture negativa em commit próprio | O marcador real acima da pasta de teste mascarava a causa | [Pytest da fixture](../receipts/crg-iu1-raiz-externa/fixture.xml) |
| Compartilhar a regra de reconhecimento da raiz | O registro já vinculava o índice externo e as duas entradas ignoravam a associação | [RED](../receipts/crg-iu1-raiz-externa/red.json) e [regra comum](../../code_review_graph/tools/_common.py) |
| Preservar controles no executável | Um grafo ancestral válido pode responder por outro projeto se a raiz escolhida estiver errada | [Provas cruzadas](../receipts/crg-iu1-raiz-externa/green.json) |
| Cobrir o corte no job Windows existente | O job seletivo precisa executar a regressão explicitamente | [Workflow](../../.github/workflows/ci.yml) |
| Resolver o launcher pelo diretório de scripts do Python | A CI Windows falhou antes de abrir a CLI porque a fixture procurava o executável ao lado do interpretador | [RED do launcher](../receipts/crg-iu1-raiz-externa/ci-windows-launcher-red.txt) e [fixture compartilhada](../../tests/test_cli.py) em `61ff0da` |

Owner mantenedor CRG. [Trilho](../PLAN-TASKS/2026-11-09-crg-iu1-raiz-externa.md).
