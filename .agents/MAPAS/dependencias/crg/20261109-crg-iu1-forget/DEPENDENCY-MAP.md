# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261109-crg-iu1-forget
Observado em: 2026-11-09T21:08:35.773Z · Revisão: aca7f74688daa12d52982ff6f99e69fc12b0745b
Ambiente: Windows, Ubuntu e GitHub Actions · Escopo: Seleção literal da CLI forget
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cli | CLI forget | command | mantenedor CRG | False | observed | [&#x27;red&#x27;, &#x27;windows&#x27;, &#x27;ubuntu&#x27;] |  |
| matcher | Seletor literal de pasta | function | mantenedor CRG | False | observed | [&#x27;red&#x27;, &#x27;windows&#x27;, &#x27;ubuntu&#x27;] |  |
| sqlite | Índice SQLite | database | mantenedor CRG | False | observed | [&#x27;windows&#x27;, &#x27;ubuntu&#x27;] |  |
| regression | Regressão de identidade da pasta | test | mantenedor CRG | False | observed | [&#x27;windows&#x27;, &#x27;ubuntu&#x27;] |  |
| ci | Job Windows | workflow | mantenedor CRG | False | observed | [&#x27;workflow&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cli-matcher | cli → matcher | calls | Padrão literal é comparado ao conjunto de caminhos armazenados | True | observed | [&#x27;red&#x27;, &#x27;windows&#x27;, &#x27;ubuntu&#x27;] |  | None |
| matcher-sqlite | matcher → sqlite | consumes_contract | O comando remove usando as chaves originais devolvidas pelo seletor | True | observed | [&#x27;windows&#x27;, &#x27;ubuntu&#x27;] |  | None |
| regression-sqlite | regression → sqlite | references | Asserção do conjunto remanescente | False | observed | [&#x27;windows&#x27;, &#x27;ubuntu&#x27;] |  | None |
| ci-regression | ci → regression | executes | Etapa Run forget path tests | True | observed | [&#x27;workflow&#x27;] |  | None |

## Fontes

- red: ../../../../receipts/crg-iu1-forget/red.json — red; revisão 6d1c5df111bc7b8d90a6e109e37ee8cfd104fabc; SHA256 c66625de9843c8beda1face4a0f5ea9c7aa1c5122e4eae6bed4c3d1395a8f65c; available.
- windows: ../../../../receipts/crg-iu1-forget/green-windows.json — windows; revisão aca7f74688daa12d52982ff6f99e69fc12b0745b; SHA256 fd5cc95c367390c8d5b08866032fec5a9159e7648e6cbc246694c5caab7163be; available.
- ubuntu: ../../../../receipts/crg-iu1-forget/green-ubuntu.json — ubuntu; revisão aca7f74688daa12d52982ff6f99e69fc12b0745b; SHA256 cd46e0dd1ab6cdc4ec277d21481fb9eaa0944f6412075a37b707d49558e3f47d; available.
- workflow: ../../../../../.github/workflows/ci.yml — workflow; revisão aca7f74688daa12d52982ff6f99e69fc12b0745b; SHA256 5a9e018e997cef0a7d68ae1e95bd1731891eb9f0c1eeaa60d623471e8590bd23; available.

## Método e limites

Git, executável, SQLite e workflow

Inventário: 5 nós; 4 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Observado em repos descartáveis com caminho Windows comum e pastas distintas no Ubuntu.
- Fora do escopo: Índice persistente
- Fora do escopo: Outras famílias do crg-iu1
