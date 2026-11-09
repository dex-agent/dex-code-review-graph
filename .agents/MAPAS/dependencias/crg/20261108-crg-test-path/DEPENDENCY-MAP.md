# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261108-crg-test-path
Observado em: 2026-11-09T01:58:58.4515632Z · Revisão: 3fb1ab318f9c92f5bbb5d1d7f9b4462a24a5ff04
Ambiente: Windows Python 3.13.13 e GitHub Actions · Escopo: classificação de testes pelo caminho relativo e consulta de associações
Cobertura: partial · Evidência: mixed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| parser | Detector por caminho relativo | function | mantenedor CRG | False | implemented | [&#x27;parser&#x27;] |  |
| jedi | Enriquecimento Jedi | function | mantenedor CRG | False | implemented | [&#x27;jedi&#x27;] |  |
| graph | Grafo SQLite e TESTED_BY | store | mantenedor CRG | False | observed | [&#x27;proof&#x27;] |  |
| cli | CLI query tests_for | command | mantenedor CRG | False | observed | [&#x27;proof&#x27;] |  |
| ci | Seleção Windows | workflow | mantenedor CRG | False | implemented | [&#x27;ci&#x27;] |  |
| test | Regressões de classificação | test | mantenedor CRG | False | implemented | [&#x27;test&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| jedi-parser | jedi → parser | consumes_contract | Durante enriquecimento Python | True | implemented | [&#x27;jedi&#x27;, &#x27;parser&#x27;] |  | None |
| graph-parser | graph → parser | consumes_contract | Ao construir os bancos isolados | True | observed | [&#x27;proof&#x27;, &#x27;parser&#x27;] |  | None |
| cli-graph | cli → graph | consumes_contract | Ao consultar tests_for | True | observed | [&#x27;proof&#x27;] |  | None |
| ci-test | ci → test | executes | Na seleção de testes Windows | True | implemented | [&#x27;ci&#x27;, &#x27;test&#x27;] |  | None |

## Fontes

- parser: ../../../../../code_review_graph/parser.py — _is_test_file; revisão 3fb1ab318f9c92f5bbb5d1d7f9b4462a24a5ff04; SHA256 dc6d7ef3618ffb0aa81ff92aaf8b10f80c14fad53f4a02607f8ab71924b29ee7; available.
- jedi: ../../../../../code_review_graph/jedi_resolver.py — enrich_jedi_calls; revisão 3fb1ab318f9c92f5bbb5d1d7f9b4462a24a5ff04; SHA256 c4fd89096f622897f4ee17538e87117248e45e2c3b8ff4fe3e03f95e7638b19f; available.
- test: ../../../../../tests/test_parser.py — test_phpunit_path_scope; revisão 3fb1ab318f9c92f5bbb5d1d7f9b4462a24a5ff04; SHA256 2bd11f3f1aaf1ddf522443038ab523f5ae97bcf9ddab5d76523394611d9046be; available.
- ci: ../../../../../.github/workflows/ci.yml — Windows daemon and file handles; revisão 3fb1ab318f9c92f5bbb5d1d7f9b4462a24a5ff04; SHA256 99a4116b23b4b400c0284ead514d9d9cc223379fb8d9977c1b0b5e3dc03b02e4; available.
- proof: ../../../../../.agents/receipts/crg-test-path/cli.json — results; revisão 3fb1ab318f9c92f5bbb5d1d7f9b4462a24a5ff04; SHA256 684a58055e00fe3947759a52a741c4d17b45bcc0e6b5e1d03c8acc4c517bbbc8; available.

## Método e limites

Git, pytest, executável e SQLite

Inventário: 6 nós; 4 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Jedi confirmado pelo contrato em código
- Fora do escopo: demais fluxos e migração do índice persistente
