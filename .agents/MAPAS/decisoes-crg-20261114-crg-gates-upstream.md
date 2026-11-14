---
fotografia_id: 20261114-crg-gates-upstream
revision: 'a2a72f1 + wheel local 8fd3127cb2e28d4f195f9c8a535efe3d89f0209610fd259c2e0b23957e8adb2c'
observed_at: 2026-11-14T17:01:03.5276021-03:00
---

# Decisões de comparação e merge

↩ [Mapas](INDEX.md)

| Decisão | Motivo | Prova |
| --- | --- | --- |
| Manter a base da casa | O oficial perde `TESTED_BY` direto de `install` e não aceita recorte `--files` | [Comparação](../receipts/CRG-GATES-UPSTREAM-20261114/comparison-matched.json) |
| Portar a estratégia UTF-8 no caminho `--brief` | O problema nasce na codificação do stream na fronteira da CLI | [Teste no wheel](../receipts/CRG-GATES-UPSTREAM-20261114/wheel-tests.xml) |
| Usar a suíte declarada para a decisão de integração | O caso combinado falhou mesmo com zero lacunas no grafo | [Regressão](../receipts/CRG-GATES-UPSTREAM-20261114/merge-semantic.json) |
| Avaliar alcance indireto e HTML separadamente | A fixture comprovou valor. A adoção dessas capacidades requer paridade dos contratos da casa | [Laudo](../receipts/CRG-GATES-UPSTREAM-20261114/INDEX.md) |
