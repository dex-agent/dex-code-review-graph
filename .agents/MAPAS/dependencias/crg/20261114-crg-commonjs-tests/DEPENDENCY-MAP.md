# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261114-crg-commonjs-tests
Observado em: 2026-11-14T14:13:52.8005364-03:00 · Revisão: 56986f7 + parser SHA-256 2ca0223c0ef234be3fc4558fb0453c1445b188250d2431a54aac585b50a30115
Ambiente: Windows, CLI e SQLite isolados · Escopo: Reconhecimento de testes CommonJS e relação direta no diff real
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cli | CLI build e query | command | mantenedor CRG | False | observed | [&#x27;proof&#x27;] |  |
| parser | Extração de teste CommonJS | module | mantenedor CRG | False | observed | [&#x27;parser&#x27;] |  |
| test | distribution.test.cjs:4 | test | mantenedor CRG | False | observed | [&#x27;proof&#x27;] |  |
| install | scripts/install.cjs::install | function | mantenedor CRG | False | observed | [&#x27;proof&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| build-parser | cli → parser | executes | build de fonte JavaScript .cjs | True | observed | [&#x27;parser&#x27;, &#x27;proof&#x27;] |  | None |
| distribution-install | test → install | calls | callback do teste de distribuição | True | observed | [&#x27;proof&#x27;] | SQLite espelha a chamada em TESTED_BY no sentido install → teste. | None |

## Fontes

- parser: C:/CodexProjetos/code-review-graph/code_review_graph/parser.py — _commonjs_test_runner; revisão 56986f7 + parser SHA-256 2ca0223c0ef234be3fc4558fb0453c1445b188250d2431a54aac585b50a30115; SHA256 2ca0223c0ef234be3fc4558fb0453c1445b188250d2431a54aac585b50a30115; available.
- proof: C:/CodexProjetos/code-review-graph/.agents/receipts/crg-commonjs-tests-20261114/proof.json — after_direct; revisão 56986f7 + parser SHA-256 2ca0223c0ef234be3fc4558fb0453c1445b188250d2431a54aac585b50a30115; SHA256 758a5ee321978e29cbecfdc06c25692bdbd0dec13868bf99d7ad9d4ba306670d; available.

## Método e limites

Snapshot do Git, wheel, CLI e consulta SQL read-only

Inventário: 4 nós; 2 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Relação estrutural no commit eb7d95b do Dex WhatsApp.
- Fora do escopo: Promoção ao PATH habitual
- Fora do escopo: Rebuild do índice persistente
