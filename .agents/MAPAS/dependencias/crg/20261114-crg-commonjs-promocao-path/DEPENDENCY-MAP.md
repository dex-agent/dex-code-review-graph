# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261114-crg-commonjs-promocao-path
Observado em: 2026-11-14T14:30:34.1993866-03:00 · Revisão: 56986f7 + wheel SHA-256 7f2f9b60802b253739c6851ee7d84e3b970a5cd9636eab800e831f72b7e051a0
Ambiente: Windows local · Escopo: CLI habitual e banco descartável do Dex WhatsApp
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cli | code-review-graph.exe do PATH | command | mantenedor CRG | False | observed | [&#x27;promotion&#x27;] |  |
| package | Wheel promovido no uv | artifact | mantenedor CRG | False | observed | [&#x27;promotion&#x27;] |  |
| sqlite | Banco descartável do Dex WhatsApp | database | mantenedor CRG | False | observed | [&#x27;accept&#x27;] |  |
| distribution | distribution.test.cjs:4 | test | mantenedor CRG | False | observed | [&#x27;accept&#x27;] |  |
| install | scripts/install.cjs::install | function | mantenedor CRG | False | observed | [&#x27;accept&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| launch | cli → package | executes | resolução habitual do uv | True | observed | [&#x27;promotion&#x27;] |  | None |
| query | cli → sqlite | consumes_contract | build e tests_for com CRG_DATA_DIR temporário | True | observed | [&#x27;accept&#x27;] |  | None |
| calls | distribution → install | calls | chamada no callback de distribuição | True | observed | [&#x27;accept&#x27;] |  | None |

## Fontes

- accept: C:/CodexProjetos/code-review-graph/.agents/receipts/crg-commonjs-path-20261114/acceptance.json — tested_by; revisão 56986f7 + wheel SHA-256 7f2f9b60802b253739c6851ee7d84e3b970a5cd9636eab800e831f72b7e051a0; SHA256 949fab8eebc4b870573621c0f5441a3cd4e4b15f023083b3718d67bd05ade7bb; available.
- promotion: C:/CodexProjetos/code-review-graph/.agents/receipts/crg-commonjs-path-20261114/promotion.json — installed_parser_sha256; revisão 56986f7 + wheel SHA-256 7f2f9b60802b253739c6851ee7d84e3b970a5cd9636eab800e831f72b7e051a0; SHA256 44a22db86097bc3f383aa5470716b72e239c401343e6e8d27c0954ca348a2687; available.

## Método e limites

Hash, uv, executável do PATH, Git e consulta SQL

Inventário: 5 nós; 3 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Snapshot por Git no commit eb7d95b.
- Fora do escopo: Adoção no banco persistente
