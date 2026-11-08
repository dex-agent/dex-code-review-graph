# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261108-crg-cli-diff-real
Observado em: 2026-11-08T16:23:51-03:00 · Revisão: bccd04a76f49f0af72ecb4f4c293b5dd12bb7b53 (CLI), 573580bdb06cac6d34b075812d5045163e1cb244 (alvo)
Ambiente: Windows, Python 3.13, Git · Escopo: Piloto CLI e índice isolado com diff real de query.py
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| n-index | Índice isolado no commit alvo | database | mantenedor CRG | False | observed | [&#x27;index&#x27;] |  |
| n-cli | CLI detect-changes --files | command | mantenedor CRG | False | observed | [&#x27;cli&#x27;, &#x27;index&#x27;] |  |
| n-oracle | Comparação Git e AST com JSON | validation | mantenedor CRG | False | observed | [&#x27;oracle&#x27;] | Escopo de funções e classes. |
| n-tests | Consulta tests_for | command | mantenedor CRG | False | observed | [&#x27;tests&#x27;, &#x27;index&#x27;] | O teste do ramo está ausente. |
| n-branch-test | Teste do ramo references_to | test | mantenedor CRG | False | observed | [&#x27;test&#x27;] | Fixture com índice próprio. |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cli-index | n-cli → n-index | consumes_contract | CLI usa o CRG_DATA_DIR do update. | True | observed | [&#x27;cli&#x27;, &#x27;index&#x27;] |  | None |
| oracle-cli | n-oracle → n-cli | references | Compara caminho, nome e faixa com a saída. | False | observed | [&#x27;oracle&#x27;, &#x27;cli&#x27;] |  | None |
| tests-index | n-tests → n-index | consumes_contract | Consulta usa o mesmo índice isolado. | True | observed | [&#x27;tests&#x27;, &#x27;index&#x27;] |  | None |
| tests-branch | n-tests → n-branch-test | references | Comparação de cobertura observada; a associação não saiu no JSON. | False | observed | [&#x27;tests&#x27;, &#x27;test&#x27;] |  | None |

## Fontes

- index: ../../../../receipts/crg-cli-diff-real/index.json — built_at_commit e update_stdout; revisão 573580bdb06cac6d34b075812d5045163e1cb244; SHA256 0b214a39be45d509fb86fd240b7f44f936b18650d32cfec67cf760143c704aaf; available.
- cli: ../../../../receipts/crg-cli-diff-real/detect.json — changed_functions; revisão bccd04a76f49f0af72ecb4f4c293b5dd12bb7b53; SHA256 5fa919ac8f5666c57e8fabfcc03642c723321aed498717cd8daf7315f10e56ab; available.
- oracle: ../../../../receipts/crg-cli-diff-real/comparison.json — Git hunks, AST e matched; revisão 573580bdb06cac6d34b075812d5045163e1cb244; SHA256 3df7b8339c4130f3fc86c55921e19383fa5881cd0921e4b9362df674fbcf7e2b; available.
- test: ../../../../receipts/crg-cli-diff-real/test-branch.txt — pytest no checkout histórico; revisão 573580bdb06cac6d34b075812d5045163e1cb244; SHA256 ea6f40ef0dbae3b9969da330838ef95aedcce9d07931bf6875e7831201aa6efa; available.
- tests: ../../../../receipts/crg-cli-diff-real/tests_for.json — 42 associações, sem o teste do ramo; revisão 573580bdb06cac6d34b075812d5045163e1cb244; SHA256 985b484bd9cec10f9d320ccb3e5b1e8b7f3212eacdded39fc1caa743103257f3; available.

## Método e limites

Build e update no Git, CLI, AST e pytest do alvo

Inventário: 5 nós; 4 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Fotografia de um diff real, escopo diferente do corte sintético.
- Fora do escopo: Índice persistente, outros commits e outros parsers
