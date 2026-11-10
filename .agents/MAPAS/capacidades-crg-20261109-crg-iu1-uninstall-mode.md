---
fotografia_id: 20261109-crg-iu1-uninstall-mode
revision: f5fb25d75cf84e38e1730228fcd63ac8c8cf3060
observed_at: 2026-11-09
---

# Capacidades observadas no corte uninstall

| Consumidor | Gatilho | Resultado observado | Limite |
| --- | --- | --- | --- |
| Operador de uninstall | Configuração descartável com entradas CRG e alheia | Remove a entrada CRG, preserva o modo efetivo e o JSON alheio, sem erro ou temporário. | Arquivo gravável |
| Mantenedor | Teste de substituição atômica | A asserção reprova mudança pós-replace nos dois sistemas. | Modo efetivo, sem prova de ACL |
| CI Windows | Push do produto | Workflow seleciona o módulo de uninstall. | Execução observada no recibo CI |

[Windows](../receipts/crg-iu1-uninstall-mode/baseline-windows.json) · [Ubuntu](../receipts/crg-iu1-uninstall-mode/baseline-ubuntu.json) · [Trilho](../PLAN-TASKS/2026-11-09-crg-iu1-uninstall-mode.md).
