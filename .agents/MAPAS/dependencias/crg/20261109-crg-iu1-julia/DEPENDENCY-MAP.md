# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261109-crg-iu1-julia
Observado em: 2026-11-09T06:47:40.4334289Z · Revisão: 9f1f19be7ee97adf2e5477ae40e9299b925d0d2d
Ambiente: Windows, Ubuntu WSL e GitHub Actions · Escopo: Portabilidade Julia e saldo Windows por ID
Cobertura: partial · Evidência: observed
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fixture | Entrada de caminho nativo | test_fixture | mantenedor CRG | False | observed | [&#x27;baseline&#x27;, &#x27;change&#x27;] |  |
| assertions | Asserções Julia de identidade completa | test | mantenedor CRG | False | observed | [&#x27;change&#x27;, &#x27;focused&#x27;] |  |
| ci | Etapa Julia no job Windows | workflow | mantenedor CRG | False | observed | [&#x27;comparison&#x27;] |  |
| delta | Saldo Windows por ID | report | mantenedor CRG | False | observed | [&#x27;baseline&#x27;, &#x27;comparison&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| assertions-fixture | assertions → fixture | consumes_contract | Caminho esperado vem da entrada, mantendo arquivo, escopo e símbolo | True | observed | [&#x27;change&#x27;, &#x27;focused&#x27;] |  | None |
| ci-assertions | ci → assertions | executes | A etapa Windows roda todo o arquivo e registra cada ID | True | observed | [&#x27;comparison&#x27;] |  | None |
| delta-ci | delta → ci | consumes_contract | O corte exige CI no SHA publicado além da suíte Windows integral | True | observed | [&#x27;comparison&#x27;] |  | None |

## Fontes

- baseline: ../../../../receipts/crg-iu1-julia/baseline.json — baseline; revisão 186259e733b043d8fd8cfe145cf7dc1919b41ea4; SHA256 8068e9a40ee50ac4e5ea222bc1fc35ed151670f7cd13364d289b07aa5820333a; available.
- change: ../../../../receipts/crg-iu1-julia/change.json — change; revisão 9f1f19be7ee97adf2e5477ae40e9299b925d0d2d; SHA256 f352f0591549cf556630cc2dc2d05434f982ffa3655482b73022fec15a5dd8b4; available.
- focused: ../../../../receipts/crg-iu1-julia/focused.json — focused; revisão 9f1f19be7ee97adf2e5477ae40e9299b925d0d2d; SHA256 256222fc12f1aab6c7aac95dd77807b737563c26998846c756bd67979841d822; available.
- comparison: ../../../../receipts/crg-iu1-julia/comparison.json — comparison; revisão 9f1f19be7ee97adf2e5477ae40e9299b925d0d2d; SHA256 91ea91ee628a9c2c1aecea78e6e5b6f56fed195d914415d5bc9afcf5e3c998e7; available.

## Método e limites

Pytest JUnit, contraprova e log remoto por SHA

Inventário: 4 nós; 3 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- CI Windows seletiva; saldo integral vem da execução local.
- Fora do escopo: Índice persistente
- Fora do escopo: Diagnóstico dos oito IDs residuais
