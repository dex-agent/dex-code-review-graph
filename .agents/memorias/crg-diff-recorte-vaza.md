---
implementation_version: v2
layer: L2
slug: crg-diff-recorte-vaza
tags:
  - "#crg/diff"
---

# CRG-DIFF-RECORTE-VAZA

No HEAD 268e0e1, detect_changes(base=573580b^, changed_files=[code_review_graph/tools/query.py]) declarou 1 arquivo e devolveu query_graph mais 6 símbolos ligados a d007bc1 (Copilot). Com base=573580b, query.py tem diff vazio, mas os 6 símbolos permanecem. Compare git diff <base> -- com git diff <pai> <commit>. tools/review.py calcula faixas globais e changes.py::analyze_changes usa todo o mapa para escolher nós, sem restringir a changed_files. tools/context.py também usa analyze_changes. Ao corrigir, preserve esse RED e distinga ausência de faixas no recorte de indisponibilidade de faixas.

#crg/diff

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-diff-recorte-vaza-content
