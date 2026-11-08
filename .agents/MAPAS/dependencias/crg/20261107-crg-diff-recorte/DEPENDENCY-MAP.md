# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261107-crg-diff-recorte
Observado em: 2026-11-07T20:29:37.3610303-03:00 · Revisão: 603bdd2 + .agents/receipts/crg-diff-recorte/produto.patch
Ambiente: Windows, Python 3.13 · Escopo: dois consumidores da analise de recorte
Cobertura: partial · Evidência: implemented
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| n0 | detect_changes_func | function | mantenedor CRG | False | implemented | [&#x27;s0&#x27;] |  |
| n1 | get_minimal_context | function | mantenedor CRG | False | implemented | [&#x27;s1&#x27;] |  |
| n2 | analyze_changes | function | mantenedor CRG | False | implemented | [&#x27;s2&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n0-analyze | n0 → n2 | calls | analise de arquivos selecionados | True | implemented | [&#x27;s0&#x27;, &#x27;s2&#x27;] | recorte de mudancas, nao descoberta geral de fluxos | None |
| n1-analyze | n1 → n2 | calls | analise de arquivos selecionados | True | implemented | [&#x27;s1&#x27;, &#x27;s2&#x27;] | recorte de mudancas, nao descoberta geral de fluxos | None |

## Fontes

- s0: code_review_graph/tools/review.py — detect_changes_func; revisão 603bdd2 + produto.patch; SHA256 3f209b6b0d86602849a74ad2f9a6abc5cde57be65e1256c2aa166950a0a51a6b; available.
- s1: code_review_graph/tools/context.py — get_minimal_context; revisão 603bdd2 + produto.patch; SHA256 321e8e8a37f63a6118c29469601a2748502beacd29c35456d51b3f6bd3727633; available.
- s2: code_review_graph/changes.py — analyze_changes; revisão 603bdd2 + produto.patch; SHA256 8a99524c5d0726c7cb8764e8af25835baf00543388b1b4d20a42dfecd03487f1; available.

## Método e limites

fonte e smoke isolado

Inventário: 3 nós; 2 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- sem baseline formal comparavel
- Fora do escopo: CLI e benchmarks
