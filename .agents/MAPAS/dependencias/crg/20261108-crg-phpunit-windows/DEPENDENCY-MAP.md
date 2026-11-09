# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261108-crg-phpunit-windows
Observado em: 2026-11-09T00:54:50.604747+00:00 · Revisão: 92fdfe052c2d97755659d1c81a3a1593e204c1c6
Ambiente: Windows Python 3.13.13 e seleção CI 3.12 · Escopo: classificação e associação direta PHPUnit
Cobertura: partial · Evidência: mixed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| parser | Detector de arquivos de teste | function | mantenedor CRG | False | implemented | [&#x27;parser&#x27;] |  |
| graph | Grafo SQLite e TESTED_BY | store | mantenedor CRG | False | observed | [&#x27;proof&#x27;] |  |
| cli | CLI query tests_for | command | mantenedor CRG | False | observed | [&#x27;proof&#x27;] |  |
| ci | CI Windows | workflow | mantenedor CRG | False | implemented | [&#x27;ci&#x27;] |  |
| test | Regressões PHPUnit | test | mantenedor CRG | False | observed | [&#x27;proof&#x27;, &#x27;test&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| graph-parser | graph → parser | consumes_contract | Ao construir o grafo de um projeto PHP | True | observed | [&#x27;parser&#x27;, &#x27;proof&#x27;] |  | None |
| cli-graph | cli → graph | consumes_contract | Ao consultar tests_for | True | observed | [&#x27;proof&#x27;] |  | None |
| test-graph | test → graph | consumes_contract | Ao verificar TESTED_BY e identidade do teste | True | observed | [&#x27;test&#x27;, &#x27;proof&#x27;] |  | None |
| ci-test | ci → test | executes | Na seleção de testes Windows | True | implemented | [&#x27;ci&#x27;, &#x27;test&#x27;] |  | None |

## Fontes

- parser: ../../../../../code_review_graph/parser.py — _is_test_file; revisão 92fdfe052c2d97755659d1c81a3a1593e204c1c6; SHA256 d0242e568f4c7c01985b18d452a21a7d70517effaa1470caee6b61cb2204aeb8; available.
- proof: ../../../../../.agents/receipts/crg-phpunit-windows/summary.json — phpunit_cli; revisão 92fdfe052c2d97755659d1c81a3a1593e204c1c6; SHA256 c37c3df90771a3df0c10fc39cdc432ce7f883b5adec3531764a4fc9c87b605bc; available.
- ci: ../../../../../.github/workflows/ci.yml — Windows daemon and file handles; revisão 92fdfe052c2d97755659d1c81a3a1593e204c1c6; SHA256 8f4667b12ffe9ed879081529a231c4addf02acda4827a9e16f94af36984eb16f; available.
- test: ../../../../../tests/test_php_scoped_calls.py — test_phpunit_instance_call_creates_canonical_tested_by_edge; revisão 92fdfe052c2d97755659d1c81a3a1593e204c1c6; SHA256 da7b618012695fc5b5139ff61c25d9e379dfbb7dcacf36a48c2e6a27779fb30c; available.

## Método e limites

Git, pytest, CLI e SQLite

Inventário: 5 nós; 4 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- execução remota da CI fora da evidência local
- Fora do escopo: restante da arquitetura do CRG
