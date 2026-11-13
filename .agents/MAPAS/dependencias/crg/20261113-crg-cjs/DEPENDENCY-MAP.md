# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261113-crg-cjs
Observado em: 2026-11-13T20:43:45.4036730Z · Revisão: b7f4e5e + diff sha256:20832c42368d000af52898c7fe767ae22daa8cb9e13abdca40537c95decfd7b6
Ambiente: Windows, wheel local isolado · Escopo: Reconhecimento .cjs, require explícito e referências CommonJS
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cli | CLI build e update | command | mantenedor CRG | False | observed | [&#x27;cli&#x27;, &#x27;proof&#x27;] |  |
| parser | Parser JavaScript e resolvedor | function | mantenedor CRG | False | observed | [&#x27;parser&#x27;, &#x27;test&#x27;] |  |
| test | Oráculos CommonJS | test | mantenedor CRG | False | observed | [&#x27;test&#x27;] |  |
| sqlite | Índice SQLite descartável | storage | mantenedor CRG | False | observed | [&#x27;cli&#x27;, &#x27;proof&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cli-parser | cli → parser | calls | Build ou update de arquivo .cjs | True | observed | [&#x27;cli&#x27;, &#x27;parser&#x27;, &#x27;proof&#x27;] | A CLI aciona o parser por meio da indexação incremental ou completa. | None |
| test-parser | test → parser | calls | Regressões CommonJS | True | observed | [&#x27;test&#x27;, &#x27;parser&#x27;] |  | None |
| cli-sqlite | cli → sqlite | other | Indexar ou consultar a fixture e o corpus | True | observed | [&#x27;cli&#x27;, &#x27;proof&#x27;] | A CLI persiste os nós e arestas observados no índice SQLite. | None |

## Fontes

- cli: ../../../../../code_review_graph/cli.py — build/update; revisão b7f4e5e + diff sha256:20832c42368d000af52898c7fe767ae22daa8cb9e13abdca40537c95decfd7b6; SHA256 7ddb5f8188a480638d264f7d23d9f96fe0633d7d74767c6820b6f61bcc985d37; available.
- parser: ../../../../../code_review_graph/parser.py — detect_language e _resolve_module_to_file; revisão b7f4e5e + diff sha256:20832c42368d000af52898c7fe767ae22daa8cb9e13abdca40537c95decfd7b6; SHA256 d6926988a1d8488bc6fa4a5cb3c5ee93f7ec96ad8addee345e95abb65d4237be; available.
- test: ../../../../../tests/test_commonjs_imports.py — oráculos CommonJS; revisão b7f4e5e + diff sha256:20832c42368d000af52898c7fe767ae22daa8cb9e13abdca40537c95decfd7b6; SHA256 adc784491cde60bff5e5aef77ad2132596ce8feea47006b1cddbc5a39394a578; available.
- proof: ../../../../receipts/crg-cjs-20261113/proof.json — corpus nominal e SQLite; revisão b7f4e5e + diff sha256:20832c42368d000af52898c7fe767ae22daa8cb9e13abdca40537c95decfd7b6; SHA256 43b2951f721ee1a11b8e39e9493a26f33ac0afe4e6395dbf91c748fcf95e3007; available.

## Método e limites

Git, CLI do wheel, pytest e readback SQLite

Inventário: 4 nós; 3 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Snapshot de 19 .cjs rastreados e uma fixture sintética.
- Fora do escopo: Promoção do launcher habitual
- Fora do escopo: Aliases de exportação
- Fora do escopo: Fallback de sufixo duplo
