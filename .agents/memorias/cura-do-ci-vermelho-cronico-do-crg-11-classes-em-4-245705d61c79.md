---
implementation_version: v2
layer: L2
slug: cura-do-ci-vermelho-cronico-do-crg-11-classes-em-4-245705d61c79
tags:
  - "#ci/cura"
  - "#crg/oficina"
  - "#metodo/red-first"
---

# Cura do CI vermelho cronico do CRG: 11 classes em 4 levas, run verde 44517837083

Bloco GO 2026-11-19 (Trilho cura-ci-vermelho): CI do fork dex-agent/dex-code-review-graph vermelho desde 11-14. Decomposicao em 11 classes de causa em 4 levas, todas RED-first com causa lida na fonte: (1) 71f5fae7 = as 17 FAILED do run 43929195987 (pins de versao, banner merge-check, gitignore de receipts, TESTES upstream contradizendo o contrato 774 de path forward-slash, resolver de reexport com 5 edges, declaracao JS runner); (2) 19669fa2 = camada OCULTA porque steps do job Windows param no primeiro erro — testes de forget/dbt/hcl formato + BUG REAL de produto no matcher case-sensitive do forget (cura os.path.normcase, Linux preserva case); (3) af2210c6 = o merge 3ddf2c8b da casa engoliu PARCIALMENTE o commit f145ca80 (ficou a linha no ci.yml, perderam-se teste E fix) — recuperado via git show + apply -3; (4) 9ca592aa = _ensure_project_marker criava dir local mesmo com --data-dir externo registrado; cura de 1 linha com _has_project_identity. Veredito: run VERDE 44517837083 (22/22 jobs), tag seca v2.4.0+dex.1 sem Release (publish.yml so dispara em release:published), TRACKER 0004 fechado + 0005 aberto (dependabots orfaos). ARMADILHAS TRANSVERSAIS MEDIDAS: steps de job GitHub Actions param no 1o erro e escondem camadas (inventariar o job INTEIRO antes do push); git log -S e cego a remocoes feitas em resolucao de MERGE (commit perdido por merge so se acha com git branch --contains + git show); python -I no harness mata language-packs e produz falso-negativo de instrumento (parser morto, produto sao); hipotese sem prova empurrada como diagnostico foi refutada pelo runner (WinError 2 igual) — hipotese nao e diagnostico. Metodo de prova de zero-regressao: paridade 2 rodadas com git stash + grep FAILED | sort + comm -13 (exclusivos meus = 0 em todas as levas). Verde local Windows nao e veredito (375 falhas baseline de formato + 21 ERROR browser pre-existentes); o runner e o juiz.

#ci/cura #crg/oficina #metodo/red-first

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^cura-do-ci-vermelho-cronico-do-crg-11-classes-em-4-245705d61c79-content
