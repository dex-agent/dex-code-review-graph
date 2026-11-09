# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261109-crg-dq9
Observado em: 2026-11-09T03:09:14.1139408-03:00 · Revisão: eeb486bd894c16c2db85a803560d26ddce3c4968
Ambiente: Windows, SQLite, Git e CLI do checkout · Escopo: Adoção da correção PHP no índice persistente
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| backup | Backup restaurável | database | mantenedor CRG | False | observed | [&#x27;backup&#x27;] |  |
| candidate | Build sobre cópia em armazenamento separado | command | mantenedor CRG | False | observed | [&#x27;candidate&#x27;] |  |
| active | Banco SQLite ativo | database | mantenedor CRG | False | observed | [&#x27;promotion&#x27;] |  |
| query | CLI tests_for | command | mantenedor CRG | False | observed | [&#x27;promotion&#x27;] |  |
| fixture | Fixtures PHP isoladas | test | mantenedor CRG | False | observed | [&#x27;php-fixtures&#x27;] | Fixtures em repositórios separados |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| candidate-backup | candidate → backup | consumes_contract | Build parte da cópia para manter estado auxiliar | True | observed | [&#x27;candidate&#x27;, &#x27;backup&#x27;] |  | None |
| active-candidate | active → candidate | consumes_contract | Adoção sob lock depois do aceite | True | observed | [&#x27;promotion&#x27;, &#x27;candidate&#x27;] |  | None |
| query-active | query → active | consumes_contract | Reabre o caminho habitual após a adoção | True | observed | [&#x27;promotion&#x27;] |  | None |
| candidate-fixture | candidate → fixture | consumes_contract | Gate PHP no mesmo código da CLI | True | observed | [&#x27;candidate&#x27;, &#x27;php-fixtures&#x27;] |  | None |

## Fontes

- backup: ../../../../receipts/crg-adocao-indice-php/backup.json — Restauração e hash lógico; revisão eeb486bd894c16c2db85a803560d26ddce3c4968; SHA256 98e1d59eabe0c2c9d3483122a377533b32b0e54c3612cb9f3a7038e20f3f2190; available.
- candidate: ../../../../receipts/crg-adocao-indice-php/candidate.json — Build, SQLite e embeddings; revisão eeb486bd894c16c2db85a803560d26ddce3c4968; SHA256 3b0f3cc66739b9ad267bb6adf0da2c2c5853b37e69605663831f8c55c4149170; available.
- promotion: ../../../../receipts/crg-adocao-indice-php/promotion.json — Readback do banco ativo; revisão eeb486bd894c16c2db85a803560d26ddce3c4968; SHA256 1ab5438a1cc48f2fde4d8298e440685c2d8585af4020996207e0c98a4c78a95e; available.
- php-fixtures: ../../../../receipts/crg-adocao-indice-php/php-fixtures.json — Fixtures scoped e Composer; revisão eeb486bd894c16c2db85a803560d26ddce3c4968; SHA256 72ca9caa3d23df7d2a42b5f9056b2ca5568edee3dd91a01d2ddfcb21b094452d; available.

## Método e limites

SQLite backup, lock exclusivo, CLI build/status/tests_for e SQL

Inventário: 5 nós; 4 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Controle do índice real separado das fixtures sintéticas.
- Fora do escopo: Atualização de vetores de fontes alteradas
- Fora do escopo: Suíte integral Windows
