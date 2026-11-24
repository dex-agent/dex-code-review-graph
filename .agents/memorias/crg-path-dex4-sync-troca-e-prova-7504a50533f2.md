---
implementation_version: v2
layer: L2
slug: crg-path-dex4-sync-troca-e-prova-7504a50533f2
tags:
  - "#auto-memory/project"
---

# crg-path-dex4-sync-troca-e-prova

Espelho da auto-memory do host ZCode (arquivo crg-path-dex4-sync-troca-e-prova.md, tipo project).

Troca do PATH do CRG em 2026-11-23 (dex.3→dex.4): `uv tool install

O executável do PATH é um wheel congelado (`uv tool`); merge na `main` não o atualiza. Troca provada em 2026-11-23 (Trilho `2026-11-23-sync-path-dex4`, recibo `receipts/CRG-PATH-DEX4-20261123/`): bump nos 13 carimbos → wheel de `git archive` do HEAD → `uv tool install --force --offline -c constraints` → prova na cópia instalada → rollback ensaiado.

**Why:** sem o retrato de dependências, a 1ª instalação subiu `packaging` 26.3→26.4 em ferramenta compartilhada. E a primeira prova funcional "verde" rodou contra o CÓDIGO DO REPO: com o Python chamado da pasta do projeto, a pasta atual vence o `PYTHONPATH` — dei verde por motivo errado; o RED verdadeiro (3 falhas na dex.3) só apareceu com a origem conferida.

**How to apply:**
- Antes da troca: `uv pip list --python <tool>/Scripts/python.exe | sort > antes.txt`; gerar constraints (pular cabeçalho da tabela, pular a própria ferramenta) e instalar com `-c constraints.txt`; diff antes/depois deve mostrar só a linha da ferramenta.
- Prova na cópia instalada: `PYTHONPATH=<...>/Roaming/uv/tools/<tool>/Lib/site-packages python -P -B -c "import <pkg> as m; assert 'Roaming/uv/tools' in m.__file__"` e o pytest com `--rootdir`/`--confcutdir` fora do repo e `--import-mode=importlib`.
- Números de versão com `+` em regex são quantificador: `rg -q -F "2.4.0+dex.4"` (o `rg -q "..."` falso-negou o ER-04).
- Wheel com procedência: `git archive` do HEAD, comparar os 114 arquivos do pacote com o HEAD TIRANDO CRLF por LF (`core.autocrlf=true` transforma tudo; 106 iguais só com normalização, 0 diferentes de verdade, 7 gerados pelo hatchling).
- Suíte `packaging`: só passa em árvore limpa — da bancada o sdist leva `.venv-240dex` ( TRACKER 0012) e o run deixa `pip/cache` na raiz; `pytest ... | tail` esconde o exit — conferir `PIPESTATUS`.
- Grafos construídos antes de mudança de parser precisam de `build` completo (ISSUE-LOCAL-0011); `doctor` acusa o grafo atrasado.
- gatilho: CRG-TROCA-PATH-PROVA-COPIA-INSTALADA

Relaciona: [[hash-em-git-bash-leitura-binaria-nao-sha256sum-cut]], [[crg-versao-uma-fonte-gates-cegos-20261123]], [[espelho-auto-memory-mjs-ferramenta-canonica]].

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-path-dex4-sync-troca-e-prova-7504a50533f2-content
