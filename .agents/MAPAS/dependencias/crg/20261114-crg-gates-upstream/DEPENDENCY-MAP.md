# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261114-crg-gates-upstream
Observado em: 2026-11-14T17:01:03.5276021-03:00 · Revisão: a2a72f1 + wheel local 8fd3127cb2e28d4f195f9c8a535efe3d89f0209610fd259c2e0b23957e8adb2c
Ambiente: Windows, Git 2.54, wheel descartável · Escopo: Merge local declarado, impacto, candidatos e suíte
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cli | CLI merge-check | command | mantenedor CRG | False | observed | [&#x27;implementation&#x27;, &#x27;proof&#x27;] |  |
| git | Git merge-tree | command | mantenedor CRG | True | observed | [&#x27;implementation&#x27;, &#x27;proof&#x27;] |  |
| crg | CRG análise de mudanças | module | mantenedor CRG | False | observed | [&#x27;analysis&#x27;, &#x27;implementation&#x27;] |  |
| suite | Suíte declarada | test | mantenedor CRG | True | observed | [&#x27;implementation&#x27;, &#x27;proof&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cli-git | cli → git | executes | base e dois commits válidos | True | observed | [&#x27;implementation&#x27;, &#x27;proof&#x27;] | exit 1 classifica conflito textual | None |
| cli-crg | cli → crg | executes | merge textual limpo | True | observed | [&#x27;implementation&#x27;, &#x27;proof&#x27;] | cobertura e risco informativos | None |
| cli-suite | cli → suite | executes | merge textual limpo | True | observed | [&#x27;implementation&#x27;, &#x27;proof&#x27;] | baseline e lados passam antes do teste do merge | None |

## Fontes

- implementation: C:/CodexProjetos/code-review-graph/code_review_graph/merge_check.py — _check; revisão a2a72f1 + wheel local 8fd3127cb2e28d4f195f9c8a535efe3d89f0209610fd259c2e0b23957e8adb2c; SHA256 61a84f62ca7b03f32cbfc19126e9ad2a242b5f2de2b04336ce349cdd6ec28ef3; available.
- analysis: C:/CodexProjetos/code-review-graph/code_review_graph/changes.py — analyze_changes; revisão a2a72f1 + wheel local 8fd3127cb2e28d4f195f9c8a535efe3d89f0209610fd259c2e0b23957e8adb2c; SHA256 36e31380c85153573291cd8640a09cc187fff0a290f85a77dd22816efae6de8e; available.
- proof: C:/CodexProjetos/code-review-graph/.agents/receipts/CRG-GATES-UPSTREAM-20261114/merge-semantic.json — outcome; revisão a2a72f1 + wheel local 8fd3127cb2e28d4f195f9c8a535efe3d89f0209610fd259c2e0b23957e8adb2c; SHA256 0159f6bbd33ea010b5a1fb24cdf6cc4cfd0ac84dd8d195df6fb16f6365488c7b; available.

## Método e limites

Receipts CLI e código do fluxo

Inventário: 4 nós; 3 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Fixture sintética e suíte declarada
- Fora do escopo: CI e índice habitual
