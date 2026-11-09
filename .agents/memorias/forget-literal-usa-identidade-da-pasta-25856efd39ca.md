---
implementation_version: v2
layer: L2
slug: forget-literal-usa-identidade-da-pasta-25856efd39ca
tags:
  - "#crg/forget"
  - "#windows/caminhos"
---

# Forget literal usa identidade da pasta

No Windows, a CLI forget retornava 0 com zero alvos para PKG, embora a pasta pkg fosse a mesma segundo samefile. O seletor agora usa a grafia estrita obtida do filesystem apenas no prefixo de diretório, sem substituir a chave gravada. Prova pelo executável e SQLite: pkg saiu e pkg_extra ficou. O contracaso Ubuntu mantém pkg quando PKG é outra pasta. Para mudanças futuras, rodar o caso real e o contracaso e conferir o conjunto SQLite, além dos testes de caminho nativo. Fontes: .agents/receipts/crg-iu1-forget/ e tests/test_forget.py.

#crg/forget #windows/caminhos

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^forget-literal-usa-identidade-da-pasta-25856efd39ca-content
