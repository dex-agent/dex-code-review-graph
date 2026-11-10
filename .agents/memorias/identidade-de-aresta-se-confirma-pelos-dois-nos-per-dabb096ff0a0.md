---
implementation_version: v2
layer: L2
slug: identidade-de-aresta-se-confirma-pelos-dois-nos-per-dabb096ff0a0
tags:
  - "#crg/portabilidade"
  - "#crg/cli"
---

# Identidade de aresta se confirma pelos dois nós persistidos

Antes de editar o parser, preserve o RED e construa um índice descartável pela CLI nos dois sistemas. Faça JOIN da aresta com os dois nós pelo qualified_name bruto e verifique tipo e símbolo; não normalize os dois lados, pois isso pode esconder uma ponta órfã. No dbt, a comparação literal POSIX falhava no Windows, mas a aresta CONTAINS ligava exatamente File a Class nos dois sistemas. Corrija a fixture com Path nativo quando o vínculo bruto estiver íntegro. Esse discriminador SQLite complementa CRG-JULIA-ASSERT-CAMINHO, que trata falsos negativos em testes de Julia. Prova .agents/receipts/crg-iu1-dbt-contains/baseline-windows.json e baseline-ubuntu.json.

#crg/portabilidade #crg/cli

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^identidade-de-aresta-se-confirma-pelos-dois-nos-per-dabb096ff0a0-content
