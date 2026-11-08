---
implementation_version: v2
layer: L2
slug: crg-dependente-hash-aresta
tags:
  - "#crg/incremental"
  - "#crg/reexportacao"
---

# Hash do dependente nao atesta frescor das arestas

Em crg-j6z, o Git alterou apenas pkg/bridge.py. O build tinha TESTED_BY correta, mas o update manteve o destino antigo mesmo depois de registrar IMPORTS_FROM corretamente: o hash do consumidor nao mudou. Ao reparar resolucao contextual, confira IMPORTS_FROM, a lista de dependentes e as arestas no mesmo indice antes/depois. Reprocesse o dependente identificado apesar de bytes iguais. Exija que o destino antigo perca a associacao, o novo ganhe e o homonimo fique vazio. Prova: .agents/receipts/crg-python-reexports/red-incremental.txt e incremental.txt. O alcance segue os limites do update; indice anterior a correcao precisa de build novo.

#crg/incremental #crg/reexportacao

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-dependente-hash-aresta-content
