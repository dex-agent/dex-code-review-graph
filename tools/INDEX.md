# Ferramentas do projeto

↩ [Nivel acima](../INDEX.md)

- [Playbook](playbook/INDEX.md) — geracao e fiscalizacao da projecao de regras.
- [release_version.py](release_version.py) — dono unico da lista de arquivos onde a versao e escrita e da regra que os confere; `--check` e gate (exit 1), `--from-index` le o proximo commit. Chamado por `tests/test_documentation.py` e pelo hook pre-commit.
- [js_form_probe.py](js_form_probe.py) — sonda in-process das formas JS/TS que o parser de uma arvore indexa (Effect.fn, rotulo, corpo, parametro tipado sombreando runner); triade `--help`, `--schema`, `--usage`. Roda com `PYTHONPATH=.` na raiz da arvore sob prova, nunca com `python -I`. Ficha `js-form-probe` no [TOOLSBOOK](../TOOLSBOOK.index.md).
- [parser_diff.py](parser_diff.py) — diff do que o parser de uma arvore do CRG produz, por arquivo: `dump` despeja nos e arestas sobre corpora rotulados, `cmp` compara dois despejos, e `--expect-identical <rotulos>` e gate (exit 1 se um rotulo que devia ficar igual mudou). Complementa `tests/test_real_repo_corpus.py` (propriedades agregadas de repos publicos fixados): aqui e por arquivo, em pasta local, sem clone nem rede. `dump` roda sem `python -I`. Ficha `parser-diff` no [TOOLSBOOK](../TOOLSBOOK.index.md).
