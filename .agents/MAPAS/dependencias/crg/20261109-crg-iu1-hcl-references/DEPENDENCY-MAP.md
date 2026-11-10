# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261109-crg-iu1-hcl-references
Observado em: 2026-11-10T00:27:34.244Z · Revisão: d6336d2ca9d4a4c96c65ffd8fd6996d8f80a31c7
Ambiente: Windows e Ubuntu · Escopo: Referências HCL por ID nativo e seleção Windows
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cli | CLI build em projeto HCL | command | mantenedor CRG | False | observed | [&#x27;win&#x27;, &#x27;ubuntu&#x27;] |  |
| parser | Parser emite referências HCL | function | mantenedor CRG | False | observed | [&#x27;parser&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] |  |
| store | GraphStore persiste os IDs nativos | storage | mantenedor CRG | False | observed | [&#x27;store&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] |  |
| test | Teste HCL compara referências exatas | test | mantenedor CRG | False | observed | [&#x27;test&#x27;] |  |
| ci | Seleção HCL no job Windows | workflow | mantenedor CRG | False | observed | [&#x27;workflow&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cli-parser | cli → parser | calls | Build do projeto HCL | True | observed | [&#x27;parser&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] |  | None |
| cli-store | cli → store | calls | Persistência das referências após o build | True | observed | [&#x27;store&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] |  | None |
| test-parser | test → parser | calls | Leitura do módulo HCL para provar as arestas | True | observed | [&#x27;test&#x27;] |  | None |
| ci-test | ci → test | executes | Passo Run HCL parser tests | True | observed | [&#x27;workflow&#x27;] |  | None |

## Fontes

- parser: ../../../../../code_review_graph/parser.py — parser; revisão d6336d2ca9d4a4c96c65ffd8fd6996d8f80a31c7; SHA256 67cb1b365c75b0dacc31db5b46dd6d0de680b29b704e737e57675827df96a05b; available.
- store: ../../../../../code_review_graph/graph.py — store; revisão d6336d2ca9d4a4c96c65ffd8fd6996d8f80a31c7; SHA256 e4b3a58495c5cd559c9a1a77f8dfc1e59a547e8a704d8a103a0608d14ad1ee32; available.
- test: ../../../../../tests/test_hcl_parser.py — test; revisão d6336d2ca9d4a4c96c65ffd8fd6996d8f80a31c7; SHA256 a04bc6923e0f936dc06ad9c65a76484bfbcdd3cbb9c0db006ba7737416a500bc; available.
- workflow: ../../../../../.github/workflows/ci.yml — workflow; revisão d6336d2ca9d4a4c96c65ffd8fd6996d8f80a31c7; SHA256 f22f84007cd1f37ebd21cbb8466bd01b7542da35e4ce4d7282542a2259ee48bf; available.
- win: ../../../../receipts/crg-iu1-hcl-references/baseline-windows.json — win; revisão 5225e8e14a3e2a003666969ad6440fda1227b518; SHA256 86956400a5649bb5f9d68ef35e0289556fcb6b12b313f2e70c5356a5a1b64983; available.
- ubuntu: ../../../../receipts/crg-iu1-hcl-references/baseline-ubuntu.json — ubuntu; revisão 5225e8e14a3e2a003666969ad6440fda1227b518; SHA256 e701b090b9297b17aafcfdee227f962a22e18819472279eaeacd964dd736efbb; available.

## Método e limites

Fonte viva, Git, CLI e igualdade de IDs no SQLite

Inventário: 5 nós; 4 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Prova com fixture HCL descartável.
- Fora do escopo: Índice habitual
- Fora do escopo: Outras famílias do crg-iu1
