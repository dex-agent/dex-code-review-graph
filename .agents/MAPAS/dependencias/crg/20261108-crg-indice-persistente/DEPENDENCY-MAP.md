# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261108-crg-indice-persistente
Observado em: 2026-11-08T21:40:30-03:00 · Revisão: 04fcb050275595bb096d1371f6be7d9305c08913
Ambiente: Windows, Python e Git · Escopo: Backup, rebuild e tests_for do banco persistente
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| build | CLI build e status | command | mantenedor CRG | False | observed | [&#x27;build&#x27;] |  |
| db | SQLite persistente | database | mantenedor CRG | False | observed | [&#x27;build&#x27;, &#x27;association&#x27;] |  |
| backup | Snapshot SQLite anterior | artifact | mantenedor CRG | False | observed | [&#x27;backup&#x27;] |  |
| query | CLI tests_for | command | mantenedor CRG | False | observed | [&#x27;association&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| build-db | build → db | consumes_contract | Build e status usam o banco persistente resolvido. | True | observed | [&#x27;build&#x27;] |  | None |
| query-db | query → db | consumes_contract | A consulta retorna o teste associado à definição. | True | observed | [&#x27;association&#x27;] |  | None |
| backup-db | backup → db | references | Snapshot verificado antes da reconstrução. | False | observed | [&#x27;backup&#x27;] |  | None |

## Fontes

- backup: ../../../../receipts/crg-indice-persistente/backup.json — SQLite backup; revisão 04fcb050275595bb096d1371f6be7d9305c08913; SHA256 6f79ae8c2ae04e5f5d8ced2c9c25fea2f3142399f6eee8940b933be09dc4c2f4; available.
- build: ../../../../receipts/crg-indice-persistente/proof-build.json — status e Git HEAD; revisão 04fcb050275595bb096d1371f6be7d9305c08913; SHA256 db290329d60d41f5baa18c27140767696ac0e643d0e08233aafe44e0d81a812a; available.
- association: ../../../../receipts/crg-indice-persistente/proof-association.json — TESTED_BY e indirect=false; revisão 04fcb050275595bb096d1371f6be7d9305c08913; SHA256 23d55c2de9a06bb37c51d75ead8116394773e14cc6d48800b3492463c89922c3; available.

## Método e limites

SQLite online backup, build/status/query pela CLI, Git e leitura da aresta

Inventário: 4 nós; 3 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Fotografia da revisão inicial, antes da publicação documental.
- Fora do escopo: Índices de outros projetos e runtime global
