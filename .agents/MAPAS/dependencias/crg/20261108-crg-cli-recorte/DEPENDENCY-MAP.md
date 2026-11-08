# Mapa relacional de dependências

Objeto: crg · Fotografia: 20261108-crg-cli-recorte
Observado em: 2026-11-08T16:01:23-03:00 · Revisão: 1e12485776652e2812bbfebf09a48bc1d8e73190
Ambiente: Windows, Python 3.13, Git · Escopo: CLI detect-changes, parser de diff e inventario do build Git
Cobertura: partial · Evidência: implemented
Visualização: Graphify interativo; vis-network via CDN; abertura no navegador não verificada pelo CLI

[Modelo JSON](DEPENDENCY-GRAPH.json) · [Visualização](DEPENDENCY-GRAPH.html)

A → B: A depende de B. Referência documental não prova dependência de execução.

## Nós

| ID | Nome | Tipo | Owner | Externo | Evidência | Fontes | Limite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| n-cli | CLI detect-changes --files | command | mantenedor CRG | False | implemented | [&#x27;s-cli&#x27;, &#x27;s-proof&#x27;] |  |
| n2 | analyze_changes | function | mantenedor CRG | False | implemented | [&#x27;s-diff&#x27;] |  |
| n-discovery | get_changed_files | function | mantenedor CRG | False | implemented | [&#x27;s-git&#x27;] |  |
| n-ranges | parse_git_diff_ranges | function | mantenedor CRG | False | implemented | [&#x27;s-diff&#x27;] |  |
| n-build | CLI build | command | mantenedor CRG | False | implemented | [&#x27;s-cli&#x27;, &#x27;s-proof&#x27;] |  |
| n-tracked | get_all_tracked_files | function | mantenedor CRG | False | implemented | [&#x27;s-git&#x27;] |  |
| n-fixture | TestDetectChangesEndToEnd | test | mantenedor CRG | False | implemented | [&#x27;s-test&#x27;, &#x27;s-proof&#x27;] |  |

## Relações

| ID | Origem → Destino | Natureza | Condição | Propaga | Evidência | Fontes | Limite | Contrato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cli-discovery | n-cli → n-discovery | calls | descoberta da lista de arquivos | True | implemented | [&#x27;s-cli&#x27;, &#x27;s-git&#x27;] |  | None |
| cli-analyze | n-cli → n2 | calls | lista filtrada ou selecao automatica | True | implemented | [&#x27;s-cli&#x27;, &#x27;s-diff&#x27;] |  | None |
| analyze-ranges | n2 → n-ranges | calls | Git com mudancas no recorte, via parse_diff_ranges | True | implemented | [&#x27;s-diff&#x27;] |  | None |
| build-tracked | n-build → n-tracked | calls | build Git via full_build e collect_all_files | True | implemented | [&#x27;s-cli&#x27;, &#x27;s-git&#x27;] |  | None |
| test-cli | n-fixture → n-cli | executes | 4 casos de Git vs JSON | True | implemented | [&#x27;s-test&#x27;, &#x27;s-proof&#x27;] |  | None |
| test-build | n-fixture → n-build | executes | indice separado por fixture | True | implemented | [&#x27;s-test&#x27;, &#x27;s-proof&#x27;] |  | None |

## Fontes

- s-cli: ../../../../../code_review_graph/cli.py — main, subcomandos detect-changes e build; revisão 1e12485776652e2812bbfebf09a48bc1d8e73190; SHA256 bbd5283fde05997e2a08a8d2ded5f43db5ec9bbe6b2ef0786bfc86f8fe14b379; available.
- s-diff: ../../../../../code_review_graph/changes.py — analyze_changes e parse_git_diff_ranges; revisão 1e12485776652e2812bbfebf09a48bc1d8e73190; SHA256 36e31380c85153573291cd8640a09cc187fff0a290f85a77dd22816efae6de8e; available.
- s-git: ../../../../../code_review_graph/incremental.py — get_changed_files e get_all_tracked_files; revisão 1e12485776652e2812bbfebf09a48bc1d8e73190; SHA256 31a988339c7c4259d5128558b4460bbe0daad19490aff0181d5371d5a9ac83ca; available.
- s-test: ../../../../../tests/test_cli.py — test_detect_changes_file_scope; revisão 1e12485776652e2812bbfebf09a48bc1d8e73190; SHA256 d9742a0d260bf331372ab84dac0aa3f14cdfa784e519a050f931c1b71f59abd0; available.
- s-proof: ../../../../receipts/crg-cli-recorte/green-final.txt — quatro casos Git versus JSON; revisão 20261108-crg-cli-recorte; SHA256 015b45fa5eb034eaeeb597356968fbd1bf5c70ced75203bc2135ce49a926caa4; available.

## Método e limites

Fonte do commit e execucao Git/CLI em quatro fixtures

Inventário: 7 nós; 6 relações (paralelas incluídas).
Alcance e contagens não comprovam quebra, qualidade ou melhoria arquitetural.
- Corte anterior excluia CLI; nao comparavel globalmente.
- Fora do escopo: MCP, SVN, outros comandos e indice persistente
