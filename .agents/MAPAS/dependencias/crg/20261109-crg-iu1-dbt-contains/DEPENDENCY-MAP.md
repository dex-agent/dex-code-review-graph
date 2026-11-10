# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261109-crg-iu1-dbt-contains
Observado em: 2026-11-10T00:12:15.091Z · Revisão: b02a4ba519a05dd30c707bcedd6a2b88575cc81e
Ambiente: Windows e Ubuntu · Escopo: Identidade CONTAINS no dbt e cobertura Windows
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cli | CLI build em projeto dbt | command | mantenedor CRG | False | observed | [&#x27;win&#x27;, &#x27;ubuntu&#x27;] |  |
| parser | Parser dbt emite CONTAINS | function | mantenedor CRG | False | observed | [&#x27;parser&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] |  |
| store | GraphStore persiste IDs nativos | storage | mantenedor CRG | False | observed | [&#x27;store&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] |  |
| test | Fixture dbt compara vínculo exato | test | mantenedor CRG | False | observed | [&#x27;fixture&#x27;] |  |
| ci | Job Windows executa módulo dbt | workflow | mantenedor CRG | False | observed | [&#x27;workflow&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cli-parser | cli → parser | calls | Build do SQL dbt | True | observed | [&#x27;parser&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] |  | None |
| cli-store | cli → store | calls | Persistência da aresta após build | True | observed | [&#x27;store&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] |  | None |
| test-store | test → store | calls | Consulta do destino pelo ID bruto | True | observed | [&#x27;fixture&#x27;] |  | None |
| ci-test | ci → test | executes | Passo Run dbt model tests | True | observed | [&#x27;workflow&#x27;] |  | None |

## Fontes

- parser: ../../../../../code_review_graph/parser.py — parser; revisão b02a4ba519a05dd30c707bcedd6a2b88575cc81e; SHA256 67cb1b365c75b0dacc31db5b46dd6d0de680b29b704e737e57675827df96a05b; available.
- store: ../../../../../code_review_graph/graph.py — store; revisão b02a4ba519a05dd30c707bcedd6a2b88575cc81e; SHA256 e4b3a58495c5cd559c9a1a77f8dfc1e59a547e8a704d8a103a0608d14ad1ee32; available.
- fixture: ../../../../../tests/test_dbt_parser.py — fixture; revisão b02a4ba519a05dd30c707bcedd6a2b88575cc81e; SHA256 53bf654d7e6de1502f57be9f327218753e941dfc6f06970e9fcd806d9e0f12a1; available.
- workflow: ../../../../../.github/workflows/ci.yml — workflow; revisão b02a4ba519a05dd30c707bcedd6a2b88575cc81e; SHA256 d895256167fa4fb571aac766cd23ed026fd9d26f45e9517cb4c5797652b41aa1; available.
- win: ../../../../receipts/crg-iu1-dbt-contains/baseline-windows.json — win; revisão b7d411cdf4141d169254eb87212a4d3543d94b1e; SHA256 df40d003ec3ac993b9543d04a9f6b269f7e1c115afd1af632160a62fb6afcad1; available.
- ubuntu: ../../../../receipts/crg-iu1-dbt-contains/baseline-ubuntu.json — ubuntu; revisão b7d411cdf4141d169254eb87212a4d3543d94b1e; SHA256 02b8e26c974b7cbb85171c8a95ae4b3d8235c6e8c17e78cc3f32b359e08fbd21; available.

## Método e limites

Fonte viva, Git, CLI e join SQLite por identidade exata

Inventário: 5 nós; 4 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Projeto dbt descartável e apenas os contratos exercitados.
- Fora do escopo: Índice persistente
- Fora do escopo: Outras famílias do crg-iu1
