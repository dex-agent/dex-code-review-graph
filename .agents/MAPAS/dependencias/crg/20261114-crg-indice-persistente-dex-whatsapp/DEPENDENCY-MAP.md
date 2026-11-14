# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261114-crg-indice-persistente-dex-whatsapp
Observado em: 2026-11-14T15:05:56.5195316-03:00 · Revisão: Dex WhatsApp eb7d95b + hashes do checkout no recibo baseline
Ambiente: Windows, CLI habitual do PATH · Escopo: Adoção do SQLite persistente do Dex WhatsApp
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cli | CLI do PATH | command | mantenedor CRG | False | observed | [&#x27;promote&#x27;] |  |
| live | SQLite persistente | database | mantenedor CRG | False | observed | [&#x27;promote&#x27;] |  |
| backup | Backup SQLite | database | mantenedor CRG | False | observed | [&#x27;backup&#x27;] |  |
| test | distribution.test.cjs:4 | test | mantenedor CRG | False | observed | [&#x27;promote&#x27;] |  |
| install | scripts/install.cjs::install | function | mantenedor CRG | False | observed | [&#x27;promote&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| read | cli → live | consumes_contract | tests_for | True | observed | [&#x27;promote&#x27;] |  | None |
| seed | live → backup | other | rollback da adoção | False | observed | [&#x27;backup&#x27;] | Backup usado para restabelecer a imagem anterior. | None |
| call | test → install | calls | callback de distribuição | True | observed | [&#x27;promote&#x27;] |  | None |

## Fontes

- promote: C:/CodexProjetos/code-review-graph/.agents/receipts/CRG-INDICE-PERSISTENTE-20261114/promotion.json — matching_edges; revisão Dex WhatsApp eb7d95b + hashes do checkout no recibo baseline; SHA256 30174fce56ff623619656ad39b7c8d2afc479984d3c11d6b4e65f818403cf2ab; available.
- backup: C:/CodexProjetos/code-review-graph/.agents/receipts/CRG-INDICE-PERSISTENTE-20261114/backup.json — restoration_reopened; revisão Dex WhatsApp eb7d95b + hashes do checkout no recibo baseline; SHA256 2ebf0a87945c9559144f72a168fac2a4b79bfcaf9f04353e3b1beec4f5bd501c; available.

## Método e limites

SQLite backup, exclusão, Git e tests_for

Inventário: 5 nós; 3 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Estados do checkout observados na sessão.
- Fora do escopo: Alterações de código e Git
