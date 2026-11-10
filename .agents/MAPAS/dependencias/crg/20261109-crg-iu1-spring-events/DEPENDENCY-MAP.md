# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261109-crg-iu1-spring-events
Observado em: 2026-11-10T00:47:34.977Z · Revisão: d22e6d6a645bcfccfc4f4ed013931f311bcb4631
Ambiente: Windows e Ubuntu · Escopo: Identidade Spring e cobertura Windows
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cli | CLI build no projeto Spring | command | mantenedor CRG | False | observed | [&#x27;win&#x27;, &#x27;ubuntu&#x27;] |  |
| resolver | Resolvedor de eventos Spring | function | mantenedor CRG | False | observed | [&#x27;resolver&#x27;, &#x27;incremental&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] |  |
| store | SQLite com os endpoints nativos | storage | mantenedor CRG | False | observed | [&#x27;store&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] |  |
| test | Teste de homônimos Spring | test | mantenedor CRG | False | observed | [&#x27;test&#x27;] |  |
| ci | Passo Spring Windows | workflow | mantenedor CRG | False | observed | [&#x27;workflow&#x27;, &#x27;ci&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cli-resolver | cli → resolver | calls | Build completo Java | True | observed | [&#x27;incremental&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] |  | None |
| resolver-store | resolver → store | calls | Persistência das arestas CALLS | True | observed | [&#x27;resolver&#x27;, &#x27;store&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] |  | None |
| test-resolver | test → resolver | calls | Full build da fixture | True | observed | [&#x27;test&#x27;, &#x27;incremental&#x27;] |  | None |
| ci-test | ci → test | executes | Passo Run Spring event tests | True | observed | [&#x27;workflow&#x27;, &#x27;ci&#x27;] |  | None |

## Fontes

- resolver: ../../../../../code_review_graph/event_resolver.py — resolver; revisão d22e6d6a645bcfccfc4f4ed013931f311bcb4631; SHA256 99680cd5f750c11551704b8fef2474c533918d723b3b43e5df7a6f2be1d7af08; available.
- incremental: ../../../../../code_review_graph/incremental.py — incremental; revisão d22e6d6a645bcfccfc4f4ed013931f311bcb4631; SHA256 a6fc6eaaeaac35e4b04c7af34a31b9365e5c4fa013c95fa125d88938fe5335a9; available.
- store: ../../../../../code_review_graph/graph.py — store; revisão d22e6d6a645bcfccfc4f4ed013931f311bcb4631; SHA256 e4b3a58495c5cd559c9a1a77f8dfc1e59a547e8a704d8a103a0608d14ad1ee32; available.
- test: ../../../../../tests/test_spring_events.py — test; revisão d22e6d6a645bcfccfc4f4ed013931f311bcb4631; SHA256 1f91ac90c72857ed2169523b99b013319332033406d7476dfae08a3eefe6a9f6; available.
- workflow: ../../../../../.github/workflows/ci.yml — workflow; revisão d22e6d6a645bcfccfc4f4ed013931f311bcb4631; SHA256 1db65e8975a55a97a87752d4b95da35d64bc7a336c2e5a3152b1af7b11934cde; available.
- win: ../../../../receipts/crg-iu1-spring-events/baseline-windows.json — win; revisão 2604aed545410d5b126fde54f149363af8b31131; SHA256 256f69739b9cf415563f576d2166dcd8f9e29360559dc3e62b1fdca306dbda8b; available.
- ubuntu: ../../../../receipts/crg-iu1-spring-events/baseline-ubuntu.json — ubuntu; revisão 2604aed545410d5b126fde54f149363af8b31131; SHA256 4b446d89cf282c5271a00798bc50e1f8ee1fb23d795747ca473d4c1e34a410f4; available.
- ci: ../../../../receipts/crg-iu1-spring-events/ci.json — ci; revisão d22e6d6a645bcfccfc4f4ed013931f311bcb4631; SHA256 dcbb78fd4b28f627dac78b1b8e988f6257d409821f3cd35bf9333e64921706de; available.

## Método e limites

Git, CLI, SQLite e CI por SHA

Inventário: 5 nós; 4 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Fixture descartável para a prova SQLite.
- Fora do escopo: Índice habitual
- Fora do escopo: Uninstall
