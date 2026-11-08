# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261108-crg-python-reexports
Observado em: 2026-11-08T19:43:49-03:00 · Revisão: ad0b736 + parser 9b151e90a43d02e35a49a7c6d08a478c3011ff4739aa5f063379ac8620e4e46d; alvo 573580bdb06cac6d34b075812d5045163e1cb244
Ambiente: Windows, Python 3.13, Git · Escopo: Reexportações explícitas e seus consumidores CLI
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| parser | Resolução Python e arestas | function | mantenedor CRG | False | observed | [&#x27;red&#x27;, &#x27;parser&#x27;] |  |
| deps | Dependentes de import relativo | data | mantenedor CRG | False | observed | [&#x27;update&#x27;] |  |
| update | CLI build e update | command | mantenedor CRG | False | observed | [&#x27;update&#x27;] |  |
| query | CLI query tests_for | command | mantenedor CRG | False | observed | [&#x27;historical&#x27;, &#x27;update&#x27;] |  |
| diff | CLI detect-changes --files | command | mantenedor CRG | False | observed | [&#x27;historical&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| update-deps | update → deps | consumes_contract | A mudança de fachada encontra os importadores. | True | observed | [&#x27;update&#x27;] |  | None |
| update-parser | update → parser | calls | Reprocessa dependentes mesmo sem alteração nos bytes. | True | observed | [&#x27;update&#x27;, &#x27;parser&#x27;] |  | None |
| query-parser | query → parser | consumes_contract | A consulta usa a identidade da definição gravada no índice. | True | observed | [&#x27;parser&#x27;, &#x27;historical&#x27;] |  | None |
| diff-parser | diff → parser | consumes_contract | O recorte usa a faixa indexada da função. | True | observed | [&#x27;historical&#x27;] |  | None |

## Fontes

- red: ../../../../receipts/crg-python-reexports/red.txt — Identidade anterior; revisão ad0b736; SHA256 1bc9aa331d1e6720d8c71bd985306195a06bc5c7c6b77740fba350c662bba66f; available.
- parser: ../../../../receipts/crg-python-reexports/green-parser.txt — CALLS e TESTED_BY; revisão 9b151e90a43d02e35a49a7c6d08a478c3011ff4739aa5f063379ac8620e4e46d; SHA256 27fc173fe2cb2f150bbb4292e2dce250936e91f6de1dd665102842d9b70bd150; available.
- update: ../../../../receipts/crg-python-reexports/incremental.txt — Troca de associação após update; revisão 20261108-crg-python-reexports; SHA256 a13b4668e8e81b5cd2fcf03ce1319d287da61f6458b7dfda40e3e31bc8971312; available.
- historical: ../../../../receipts/crg-python-reexports/historical.json — Resultado e base Git; revisão 573580bdb06cac6d34b075812d5045163e1cb244; SHA256 b3934350e41bfca719a67873aa2a6ef736d98a1c0800e97c2d8b5d8d1b851ea0; available.

## Método e limites

RED/GREEN, build e update Git, AST e CLI

Inventário: 5 nós; 4 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- O limite padrão de expansão incremental é mantido.
- Fora do escopo: Índice persistente e imports dinâmicos
