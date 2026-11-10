# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261109-crg-iu1-uninstall-mode
Observado em: 2026-11-10T00:57:44.814Z · Revisão: f5fb25d75cf84e38e1730228fcd63ac8c8cf3060
Ambiente: Windows e Ubuntu · Escopo: Modo efetivo no uninstall e cobertura Windows
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cli | CLI uninstall | command | mantenedor CRG | False | observed | [&#x27;cli&#x27;, &#x27;test&#x27;] |  |
| writer | Escrita atômica do uninstall | function | mantenedor CRG | False | observed | [&#x27;writer&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] |  |
| file | Configuração no filesystem | storage | mantenedor CRG | False | observed | [&#x27;writer&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] |  |
| test | Teste do modo efetivo | test | mantenedor CRG | False | observed | [&#x27;test&#x27;] |  |
| ci | Passo uninstall Windows | workflow | mantenedor CRG | False | observed | [&#x27;workflow&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cli-writer | cli → writer | calls | Rota uninstall com configuração local | True | observed | [&#x27;cli&#x27;, &#x27;writer&#x27;, &#x27;test&#x27;] |  | None |
| writer-file | writer → file | other | Substituição atômica do arquivo gravável | True | observed | [&#x27;writer&#x27;, &#x27;win&#x27;, &#x27;ubuntu&#x27;] | Relação de escrita e substituição de arquivo, observada na fixture gravável. | None |
| test-writer | test → writer | calls | uninstall.run com fixture temporária | True | observed | [&#x27;test&#x27;, &#x27;writer&#x27;] |  | None |
| ci-test | ci → test | executes | Passo Run uninstall tests | True | observed | [&#x27;workflow&#x27;] |  | None |

## Fontes

- writer: ../../../../../code_review_graph/uninstall.py — writer; revisão f5fb25d75cf84e38e1730228fcd63ac8c8cf3060; SHA256 6fed584a1e8df2e3ca8f4ca466d95cb1b3bc79f354d4fec0aaf618ac03051315; available.
- cli: ../../../../../code_review_graph/cli.py — cli; revisão f5fb25d75cf84e38e1730228fcd63ac8c8cf3060; SHA256 7ddb5f8188a480638d264f7d23d9f96fe0633d7d74767c6820b6f61bcc985d37; available.
- test: ../../../../../tests/test_uninstall.py — test; revisão f5fb25d75cf84e38e1730228fcd63ac8c8cf3060; SHA256 481a4876455090651a1ea7c59aee316ed5ea75b7fe97bc7b04f6cda85400c8d3; available.
- workflow: ../../../../../.github/workflows/ci.yml — workflow; revisão f5fb25d75cf84e38e1730228fcd63ac8c8cf3060; SHA256 5a65b30da9d518b959ad66805d299ffc7689ec85139ebc76c6d75e6e4a173700; available.
- win: ../../../../receipts/crg-iu1-uninstall-mode/baseline-windows.json — win; revisão 95e74414c2d1cc03cdbb40b64dbc0e1fc5edca9f; SHA256 2b84d03460b7b4636f134d15699a73169c079451a26da639d2ec42c97562f68f; available.
- ubuntu: ../../../../receipts/crg-iu1-uninstall-mode/baseline-ubuntu.json — ubuntu; revisão 95e74414c2d1cc03cdbb40b64dbc0e1fc5edca9f; SHA256 0b73bb9294b7061465874818b20309b45704a573fb341d3bcb7c0105b7a340a9; available.

## Método e limites

Git, pytest, sonda do modo antes/depois e workflow

Inventário: 5 nós; 4 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Fixture descartável em filesystem real.
- Fora do escopo: ACLs
- Fora do escopo: Configuração somente leitura como entrada
- Fora do escopo: Release
