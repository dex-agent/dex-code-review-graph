---
fotografia_id: 20261109-crg-iu1-raiz-externa
revision: f145ca80519846eb7581bd047188a7054c801be6
observed_at: 2026-11-09
---

# Capacidades observadas da raiz explícita

| Capacidade | Consumidor e gatilho | Prova | Limite |
| --- | --- | --- | --- |
| Indexar projeto sem VCS em armazenamento externo | Operador usa `build --repo ... --data-dir ...` | [RED](../receipts/crg-iu1-raiz-externa/red.json) e [prova cruzada](../receipts/crg-iu1-raiz-externa/green.json) | Vínculo local explícito de armazenamento |
| Buscar do projeto registrado ou de um descendente | Operador usa `search --repo ...` | [Canário do subprojeto e SQLite](../../tests/test_cli.py) | A raiz reconhecida mais próxima vence |
| Recusar pasta sem identidade de projeto | Operador aponta `--repo` sem marcadores e sem associação | [Controles da CLI](../receipts/crg-iu1-raiz-externa/green.json) | `CRG_DATA_DIR` sozinho só configura armazenamento |

Owner mantenedor CRG. [Trilho](../PLAN-TASKS/2026-11-09-crg-iu1-raiz-externa.md).
