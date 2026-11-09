# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261109-crg-x6m
Observado em: 2026-11-09T05:49:40.3656800Z · Revisão: fb9fc22da3d1966f5754d9db7938cd4b0ad8caba
Ambiente: Windows nativo, Git e SQLite isolados · Escopo: destino PHP construído e fallback genérico
Cobertura: partial · Evidência: mixed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| parser | Parser PHP | function | mantenedor CRG | False | implemented | [&#x27;parser&#x27;] |  |
| scoped | Resolvedor scoped PHP/Rust | function | mantenedor CRG | False | implemented | [&#x27;scoped&#x27;] |  |
| graph | Armazenamento e fallback de arestas | store | mantenedor CRG | False | implemented | [&#x27;graph&#x27;] |  |
| cli | CLI build, update e tests_for | command | mantenedor CRG | False | observed | [&#x27;proof&#x27;] |  |
| ci | Regressão na seleção Windows | workflow | mantenedor CRG | False | implemented | [&#x27;ci&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scoped-parser | scoped → parser | consumes_contract | Depois da extração lexical | True | implemented | [&#x27;parser&#x27;, &#x27;scoped&#x27;] |  | None |
| graph-scoped | graph → scoped | consumes_contract | Ao tratar endpoints qualificados e pendentes | True | implemented | [&#x27;scoped&#x27;, &#x27;graph&#x27;] |  | None |
| cli-graph | cli → graph | consumes_contract | Ao persistir e consultar a associação | True | observed | [&#x27;proof&#x27;, &#x27;graph&#x27;] |  | None |
| ci-cli | ci → cli | consumes_contract | Cobertura de regressão e paridade funcional | True | implemented | [&#x27;ci&#x27;, &#x27;proof&#x27;] |  | None |

## Fontes

- parser: ../../../../../code_review_graph/parser.py — php_class_scope; revisão fb9fc22da3d1966f5754d9db7938cd4b0ad8caba; SHA256 67cb1b365c75b0dacc31db5b46dd6d0de680b29b704e737e57675827df96a05b; available.
- scoped: ../../../../../code_review_graph/scoped_resolver.py — resolve_scoped_calls; revisão fb9fc22da3d1966f5754d9db7938cd4b0ad8caba; SHA256 b8fffcb01e3837d685a988335d1100f820ce6f9303de26874dc96d852ff58491; available.
- graph: ../../../../../code_review_graph/graph.py — _resolve_bare_endpoints; revisão fb9fc22da3d1966f5754d9db7938cd4b0ad8caba; SHA256 e4b3a58495c5cd559c9a1a77f8dfc1e59a547e8a704d8a103a0608d14ad1ee32; available.
- proof: ../../../../../.agents/receipts/crg-x6m/cli.json — scenarios; revisão fb9fc22da3d1966f5754d9db7938cd4b0ad8caba; SHA256 04963d1064c8fb29be3b3b6e6ae17128f2e16b49a9caaaf15da48e602a71bdf6; available.
- ci: ../../../../../.github/workflows/ci.yml — test_php_imported_constructor_and_method_keep_namespace; revisão fb9fc22da3d1966f5754d9db7938cd4b0ad8caba; SHA256 60b87763035279cdd47d1d0612d011067b2668822dd917618da2929214bb83c4; available.

## Método e limites

CLI, SQLite, pytest e revisão de fonte

Inventário: 5 nós; 4 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- dois cenários Git PHP
- Fora do escopo: adoção no banco persistente
