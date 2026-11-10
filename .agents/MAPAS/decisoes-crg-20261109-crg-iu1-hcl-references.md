---
fotografia_id: 20261109-crg-iu1-hcl-references
revision: d6336d2ca9d4a4c96c65ffd8fd6996d8f80a31c7
observed_at: 2026-11-09
---

# Decisões do corte HCL

| ID | Decisão | Gatilho e fonte |
| --- | --- | --- |
| D-01 | Preservar o RED e verificar os dois endpoints brutos | [Teste Windows](../receipts/crg-iu1-hcl-references/red-windows.txt) e [SQLite](../receipts/crg-iu1-hcl-references/baseline-windows.json) separam expectativa de comportamento |
| D-02 | Derivar a expectativa do Path da fixture | [Teste corrigido](../../tests/test_hcl_parser.py) preserva a comparação de conjunto e a semântica do parser |
| D-03 | Executar o módulo HCL no runner Windows | [Workflow](../../.github/workflows/ci.yml) dá cobertura explícita ao caso que falhava |

Owner mantenedor CRG. [Trilho](../PLAN-TASKS/2026-11-09-crg-iu1-hcl-references.md).
