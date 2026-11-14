---
implementation_version: v2
layer: L2
slug: merge-limpo-zero-lacunas-suite
tags:
  - "#crg/merge-check"
  - "#testes/regressao"
---

# Merge textual limpo e zero lacunas exigem suíte no resultado combinado

Execute a mesma suíte na base, nos dois pais e no resultado combinado, com cópias descartáveis. A fixture mudou o limite de <= para < em um lado e o valor de entrada de 4 para 5 no outro. Git merge-tree voltou 0, e CRG achou test_boundary com zero lacunas. As três referências passaram; o merge saiu 17, o código reservado da asserção. Uma falha prévia ou do executor pede diagnóstico próprio. Recibos: .agents/receipts/CRG-GATES-UPSTREAM-20261114/merge-semantic.json e .agents/receipts/CRG-GATES-UPSTREAM-20261114/merge-failing.json.

#crg/merge-check #testes/regressao

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^merge-limpo-zero-lacunas-suite-content
