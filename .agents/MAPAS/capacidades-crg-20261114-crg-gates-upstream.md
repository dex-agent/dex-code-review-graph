---
fotografia_id: 20261114-crg-gates-upstream
revision: 'a2a72f1 + wheel local 8fd3127cb2e28d4f195f9c8a535efe3d89f0209610fd259c2e0b23957e8adb2c'
observed_at: 2026-11-14T17:01:03.5276021-03:00
---

# Capacidades de comparação e merge

↩ [Mapas](INDEX.md)

| Consumidor | Gatilho | Comportamento | Prova |
| --- | --- | --- | --- |
| Revisor | IDs de base, lados e comando da suíte | `merge-check` resolve o merge em ambiente descartável e distingue conflito, falha de execução e regressão | [Casos e saídas](../receipts/CRG-GATES-UPSTREAM-20261114/INDEX.md) |
| Revisor | Saída `--brief` redirecionada | A CLI emite UTF-8 também quando o processo inicia em CP1252 | [Teste no wheel](../receipts/CRG-GATES-UPSTREAM-20261114/wheel-tests.xml) |
| Mantenedor | Avaliação de portabilidade | Ambos os wheels indexam 21 caminhos. A edição da casa retém o vínculo e aceita `--files` | [Comparação equiparada](../receipts/CRG-GATES-UPSTREAM-20261114/comparison-matched.json) |
