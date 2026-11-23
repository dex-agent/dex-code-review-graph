---
implementation_version: v2
layer: L2
slug: sonda-e-script-de-prova-seguem-o-dex-toolsbook-reus-1dfc5c64c85d
tags:
  - "#crg/ferramenta"
  - "#dex-toolsbook/regra"
  - "#agente/comportamento"
---

# Sonda e script de prova seguem o dex-toolsbook: reuso antes, triade, ficha; ferramenta mora em tools

Cobranca do dono em 2026-11-23: cinco scripts de sonda criados em /tmp sem recibo de reuso, sem triade e sem ficha. Regra: antes de criar qualquer arquivo de script, inclusive em TEMP, rodar reuso.py com --receipt --para; ferramenta de repo nasce em tools/ com triade (--help, --schema, --usage), lint e regua de CC, entrada em tools/INDEX.md e ficha no TOOLSBOOK.json no mesmo bloco; alternativa valida quando nao e ferramenta: prototipo inline declarado ou teste no pytest; ferramenta externa usada sem ficha e divida do mesmo bloco. Nunca git add -f sob .agents/receipts/: tests/test_install_outputs_are_ignored.py::test_no_tracked_file_is_ignored proibe arquivo rastreado em caminho ignorado e quebrou a main no run 45256809972. Commit de documentacao que rastreia um .py exige rodar as suites-guarda antes do push. Exemplo: tools/js_form_probe.py, ficha js-form-probe. Relaciona: artefato-com-valor-de-reuso-em-local-descartavel.

#crg/ferramenta #dex-toolsbook/regra #agente/comportamento

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^sonda-e-script-de-prova-seguem-o-dex-toolsbook-reus-1dfc5c64c85d-content
