# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261108-crg-k4q
Observado em: 2026-11-09T02:29:20.2967540Z · Revisão: 5ec476253c5052fe3227ea1750f51657190cc5dd
Ambiente: Windows Python 3.13 e Git isolado · Escopo: reclassificação PHPUnit após rebuild
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cli | CLI status e tests_for | command | mantenedor CRG | False | observed | [&#x27;cli&#x27;, &#x27;rebuild&#x27;] | Fixture isolada |
| update | Update de arquivo alheio | command | mantenedor CRG | False | observed | [&#x27;update&#x27;] | Fixture isolada |
| backup | Backup SQLite read-only | store | mantenedor CRG | False | observed | [&#x27;backup&#x27;] | Fixture isolada |
| rebuild | Rebuild e classificação nova | command | mantenedor CRG | False | observed | [&#x27;rebuild&#x27;] | Fixture isolada |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cli-update | cli → update | consumes_contract | Leitura de SHA após update | True | observed | [&#x27;cli&#x27;, &#x27;update&#x27;] | Fixture isolada | None |
| backup-update | backup → update | consumes_contract | Cópia do estado anterior ao rebuild | True | observed | [&#x27;update&#x27;, &#x27;backup&#x27;] | Fixture isolada | None |
| cli-rebuild | cli → rebuild | consumes_contract | Consulta de associação direta após rebuild | True | observed | [&#x27;cli&#x27;, &#x27;rebuild&#x27;] | Fixture isolada | None |

## Fontes

- cli: ../../../../../code_review_graph/cli.py — built_at_commit; revisão 5ec476253c5052fe3227ea1750f51657190cc5dd; SHA256 bbd5283fde05997e2a08a8d2ded5f43db5ec9bbe6b2ef0786bfc86f8fe14b379; available.
- update: ../../../../../.agents/receipts/crg-k4q/update.json — git_changed_files; revisão 5ec476253c5052fe3227ea1750f51657190cc5dd; SHA256 89769db77351e1ab41662d990e42c4855c06a3a5c0e1f7294eae732337a48032; available.
- backup: ../../../../../.agents/receipts/crg-k4q/backup.json — integrity_check; revisão 5ec476253c5052fe3227ea1750f51657190cc5dd; SHA256 c210d1cc8ce970a7bc7f2c6e56954ac7d7b921d986b1741f0dc6b284f78648dc; available.
- rebuild: ../../../../../.agents/receipts/crg-k4q/rebuild.json — TESTED_BY; revisão 5ec476253c5052fe3227ea1750f51657190cc5dd; SHA256 f7eae20a65825e1d83c3aa12bc0f8135f48e9542c0aa86d9c3b43736cab79665; available.

## Método e limites

Git, CLI e SQLite

Inventário: 4 nós; 3 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- um caso PHP e duas revisões
- Fora do escopo: índice persistente
