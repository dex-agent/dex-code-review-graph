# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261109-crg-iu1-caminhos
Observado em: 2026-11-09T06:30:13.3308660Z · Revisão: f825c2597e6bfba1a489a8b96856a9f4aa1a1f8b
Ambiente: Windows nativo, Ubuntu WSL e GitHub Actions · Escopo: Provas de caminho PHP e Rust e saldo da suíte Windows
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fixture | Fixture PHP/Rust e destino qualificado | test | mantenedor CRG | False | observed | [&#x27;change&#x27;, &#x27;focused&#x27;] |  |
| ci | Job Windows nativo | workflow | mantenedor CRG | False | observed | [&#x27;comparison&#x27;] |  |
| reconcile | Comparação de IDs Windows | command | mantenedor CRG | False | observed | [&#x27;comparison&#x27;] |  |
| baseline | Baseline de 24 IDs | report | mantenedor CRG | False | observed | [&#x27;comparison&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ci-fixture | ci → fixture | executes | Seleção obrigatória dos três node IDs no workflow existente | True | observed | [&#x27;change&#x27;, &#x27;comparison&#x27;] |  | None |
| reconcile-baseline | reconcile → baseline | consumes_contract | Comparação de conjuntos de node IDs em Windows 3.13 | True | observed | [&#x27;comparison&#x27;] |  | None |

## Fontes

- change: ../../../../receipts/crg-iu1-caminhos/change.json — change; revisão f825c2597e6bfba1a489a8b96856a9f4aa1a1f8b; SHA256 2cf44e69c779d077a8f3cdb9f1fc1b9e0bda7f39bd37d7e510f3fbc7005a9082; available.
- focused: ../../../../receipts/crg-iu1-caminhos/focused.json — focused; revisão f825c2597e6bfba1a489a8b96856a9f4aa1a1f8b; SHA256 5ad61fc1312d6b145e163702750d6feac05a277f85bcb65ea6b3ff5e20b6b051; available.
- comparison: ../../../../receipts/crg-iu1-caminhos/comparison.json — comparison; revisão f825c2597e6bfba1a489a8b96856a9f4aa1a1f8b; SHA256 a87cbb59f1fd75ce5dbb68f0fc78be7ee9df4771caa7cd67058dca839999c78c; available.

## Método e limites

Pytest JUnit, Git e leitura da CI por SHA

Inventário: 4 nós; 2 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- O job Windows usa seleção de testes.
- Fora do escopo: Índice persistente
- Fora do escopo: Diagnóstico das outras 21 falhas
