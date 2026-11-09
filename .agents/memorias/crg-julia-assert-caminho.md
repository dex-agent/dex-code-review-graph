---
implementation_version: v2
layer: L2
slug: crg-julia-assert-caminho
tags:
  - "#crg/julia"
  - "#crg/portabilidade"
---

# CRG-JULIA-ASSERT-CAMINHO — teste negativo precisa de caminho nativo

Em testes Julia, derive o prefixo da identidade do Path fornecido pela fixture e compare o nome qualificado completo. Um literal POSIX em `assert not any` pode deixar uma autochamada indevida invisível em Windows. Prove o negativo injetando uma autochamada com a origem nativa; prove o positivo com outro arquivo e outro escopo. No corte 9f1f19b, três contraprovas rejeitadas e 27/27 em Windows e Ubuntu. Fontes: `tests/test_julia_reconciliation.py`, `.agents/receipts/crg-iu1-julia/change.json` e `.agents/PLAN-TASKS/2026-11-09-crg-iu1-julia.md`.

#crg/julia #crg/portabilidade

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-julia-assert-caminho-content
