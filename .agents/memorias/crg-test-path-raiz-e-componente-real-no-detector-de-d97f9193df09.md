---
implementation_version: v2
layer: L2
slug: crg-test-path-raiz-e-componente-real-no-detector-de-d97f9193df09
tags:
  - "#crg/test-path"
---

# CRG-TEST-PATH raiz e componente real no detector de testes

No Windows, 92fdfe0 habilitou PHPUnit em tests, mas o detector passou a casar tests?/ no caminho absoluto. A mesma fixture de producao em contest/ ou em src/ com checkout sob um ancestral tests/ virou Test e gerou TESTED_BY direto. A prova A/B da CLI compara c3682ac com 92fdfe0 e preserva controle positivo em tests/ e negativo em src/ neutro. Antes de mexer no detector, separe caminho relativo ao checkout para classificar e caminho nativo para identidade. Exija ausencia de Test, de aresta e de resultado direto nos negativos. Prova local: .agents/receipts/crg-phpunit-adversarial/ab-cli.json.

#crg/test-path

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-test-path-raiz-e-componente-real-no-detector-de-d97f9193df09-content
