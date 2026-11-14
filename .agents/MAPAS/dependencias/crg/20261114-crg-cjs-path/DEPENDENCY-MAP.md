# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261114-crg-cjs-path
Observado em: 2026-11-14T11:30:53.045565-03:00 · Revisão: 201f3c0a9627b282fc7eba4e03646179c3ddd7a3
Ambiente: Windows, CLI habitual no PATH · Escopo: Adoção local do wheel e cobertura de arquivos .cjs
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cli | CLI do PATH (build e status) | command | mantenedor CRG | False | observed | [&#x27;adoption&#x27;, &#x27;cli&#x27;] |  |
| parser | Parser JavaScript e resolvedor | function | mantenedor CRG | False | observed | [&#x27;adoption&#x27;, &#x27;parser&#x27;] |  |
| sqlite | Índice SQLite descartável | storage | mantenedor CRG | False | observed | [&#x27;adoption&#x27;, &#x27;cli&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cli-parser | cli → parser | calls | Build de snapshot .cjs | True | observed | [&#x27;adoption&#x27;, &#x27;cli&#x27;, &#x27;parser&#x27;] | Hash do parser instalado coincide com o wheel. | None |
| cli-sqlite | cli → sqlite | other | Build e status de cada snapshot | True | observed | [&#x27;adoption&#x27;, &#x27;cli&#x27;] | Igualdade nominal com Git: 19/19 e 21/21. Bancos novos. | None |

## Fontes

- cli: ../../../../../code_review_graph/cli.py — build/update; revisão b7f4e5e + diff sha256:20832c42368d000af52898c7fe767ae22daa8cb9e13abdca40537c95decfd7b6; SHA256 7ddb5f8188a480638d264f7d23d9f96fe0633d7d74767c6820b6f61bcc985d37; available.
- parser: ../../../../../code_review_graph/parser.py — detect_language e _resolve_module_to_file; revisão b7f4e5e + diff sha256:20832c42368d000af52898c7fe767ae22daa8cb9e13abdca40537c95decfd7b6; SHA256 d6926988a1d8488bc6fa4a5cb3c5ee93f7ec96ad8addee345e95abb65d4237be; available.
- adoption: ../../../../receipts/crg-cjs-runtime-20261113/adopt-path-verdict.json — parser_sha256 e validation; revisão 201f3c0a9627b282fc7eba4e03646179c3ddd7a3; SHA256 4e7962e2f591ad82edb614b216aae472f8e6f24a86fff38c19ef4b04609afa12; available.

## Método e limites

uv tool install, hash do parser, Git, CLI e SQLite

Inventário: 3 nós; 2 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Snapshots dos .cjs de dois commits do Dex WhatsApp em bancos descartáveis.
- Fora do escopo: Rebuild do índice persistente
- Fora do escopo: Reexecução da suíte
