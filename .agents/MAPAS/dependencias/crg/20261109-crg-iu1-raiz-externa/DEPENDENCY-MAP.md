# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261109-crg-iu1-raiz-externa
Observado em: 2026-11-09T23:01:35.497Z · Revisão: f145ca80519846eb7581bd047188a7054c801be6
Ambiente: Windows, Ubuntu e GitHub Actions · Escopo: Identidade da raiz explícita com índice externo
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cli | CLI build e search | command | mantenedor CRG | False | observed | [&#x27;red&#x27;, &#x27;green&#x27;] |  |
| identity | Regra comum de identidade de projeto | function | mantenedor CRG | False | observed | [&#x27;common&#x27;, &#x27;green&#x27;] |  |
| registry | Associação exata no registry | registry | mantenedor CRG | False | observed | [&#x27;common&#x27;, &#x27;red&#x27;] |  |
| test | Regressão executável e controles | test | mantenedor CRG | False | observed | [&#x27;green&#x27;] |  |
| ci | Job Windows | workflow | mantenedor CRG | False | observed | [&#x27;workflow&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cli-identity | cli → identity | calls | Reconhecimento da raiz explícita | True | observed | [&#x27;common&#x27;, &#x27;green&#x27;] |  | None |
| identity-registry | identity → registry | consumes_contract | Consulta somente o vínculo exato do projeto | True | observed | [&#x27;common&#x27;] |  | None |
| test-cli | test → cli | executes | Build e search no subprocesso | True | observed | [&#x27;green&#x27;] |  | None |
| ci-test | ci → test | executes | Etapa Run explicit project root tests | True | observed | [&#x27;workflow&#x27;] |  | None |

## Fontes

- red: ../../../../receipts/crg-iu1-raiz-externa/red.json — red; revisão 92d7ca02ce051cd8e66cef55dfa4151f0cc5ab0a; SHA256 5ec6b73b3fd474b80009990e2ba2d286ca796e4104025137b97b7435fc41a0ca; available.
- green: ../../../../receipts/crg-iu1-raiz-externa/green.json — green; revisão f145ca80519846eb7581bd047188a7054c801be6; SHA256 1178188133396b1e3816b74b90e6ccd66e429f2b6ede380bff30d8af377a2dda; available.
- common: ../../../../../code_review_graph/tools/_common.py — common; revisão f145ca80519846eb7581bd047188a7054c801be6; SHA256 92ecfd9d96431f7b3c0f89b72a06a54b9d16ee8cbe57271e24b97e84b41d5e6f; available.
- workflow: ../../../../../.github/workflows/ci.yml — workflow; revisão f145ca80519846eb7581bd047188a7054c801be6; SHA256 38f39c159c34e2a7773d02e14a7bdda1e4f3ca42814ac6463d82a6b3ba32a3ca; available.

## Método e limites

Git, CLI, SQLite e workflow

Inventário: 5 nós; 4 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Prova do executável em projetos descartáveis.
- Fora do escopo: Índice persistente
- Fora do escopo: Outras famílias do crg-iu1
