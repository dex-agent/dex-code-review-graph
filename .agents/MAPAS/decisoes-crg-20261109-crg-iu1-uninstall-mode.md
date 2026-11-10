---
fotografia_id: 20261109-crg-iu1-uninstall-mode
revision: f5fb25d75cf84e38e1730228fcd63ac8c8cf3060
observed_at: 2026-11-09
---

# Decisões do corte uninstall

| ID | Decisão | Fonte |
| --- | --- | --- |
| D-01 | Medir o modo depois da preparação, antes de substituir | [RED](../receipts/crg-iu1-uninstall-mode/red-windows.txt) e [sonda](../receipts/crg-iu1-uninstall-mode/probe.py) |
| D-02 | Manter a exigência POSIX e comparar o modo efetivo nos dois sistemas | [Teste](../../tests/test_uninstall.py) e [controle Windows](../receipts/crg-iu1-uninstall-mode/negative-windows.json) |
| D-03 | Incluir uninstall no runner Windows | [Workflow](../../.github/workflows/ci.yml) e [log nominal](../receipts/crg-iu1-uninstall-mode/ci-windows-uninstall.txt) |
| D-04 | Fechar crg-iu1 pela comparação de IDs | [Saldo integral](../receipts/crg-iu1-uninstall-mode/comparison.json) |

Owner mantenedor CRG. [Trilho](../PLAN-TASKS/2026-11-09-crg-iu1-uninstall-mode.md).
