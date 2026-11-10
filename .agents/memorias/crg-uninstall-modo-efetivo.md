---
implementation_version: v2
layer: L2
slug: crg-uninstall-modo-efetivo
tags:
  - "#crg/portabilidade"
  - "#crg/uninstall"
  - "#python/chmod"
---

# Preservação de modo começa pelo estado efetivo da fixture

Antes de diagnosticar perda de modo numa substituição atômica, capture o modo efetivo da fixture depois de chmod e antes da operação. A fixture gravável do uninstall CRG com chmod 0o640 observou 0o666 antes e depois no Windows e 0o640 no Ubuntu. O teste exige 0o640 no POSIX e preservação do modo observado nos dois sistemas. A contraprova muda o modo após um replace real, em arquivo descartável, e precisa falhar na asserção. Verifique também JSON restante, erros e temporários. Essa prova cobre modo do arquivo gravável e não valida ACLs nem um arquivo inicialmente somente leitura. Recibos em ../receipts/crg-iu1-uninstall-mode/.

#crg/portabilidade #crg/uninstall #python/chmod

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-uninstall-modo-efetivo-content
