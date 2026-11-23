---
implementation_version: v2
layer: L2
slug: crg-versao-uma-fonte-gates-cegos-20261123-675313426b00
tags:
  - "#auto-memory/project"
---

# crg-versao-uma-fonte-gates-cegos-20261123

Espelho da auto-memory do host ZCode (arquivo crg-versao-uma-fonte-gates-cegos-20261123.md, tipo project).

CRG 2026-11-23 — bump de versão parcial (3ª ocorrência) curado com dono único + gate; lição de classe: alarme herdado do upstream fica cego no fork; armadilha do hook do Playbook em clone/worktree novo

Corte `versao-uma-fonte` (GO PADRAO do dono em 2026-11-23, Trilho `.agents/PLAN-TASKS/2026-11-23-versao-uma-fonte.md`). A `main` do fork `dex-agent/dex-code-review-graph` estava vermelha desde 21/11 porque dois bumps moveram só o `pyproject.toml` — a versão é escrita em **13** arquivos (contei 12 a sessão inteira; o `--schema` da ferramenta corrigiu). Cura em `b45272a9` + fechamento `87014cf9`: `tools/release_version.py` é o dono único da lista e da regra, o hook `pre-commit` recusa commit parcial lendo o índice do git, o job `release-stamps` do CI roda a checagem no fork, e a cópia do PATH foi reinstalada a partir do wheel novo (`doctor`: All good — antes ela se acusava de desatualizada: `--version` dex.3 contra `__version__` dex.1).

**Lição de classe (vale para qualquer fork da casa que acompanhe upstream):** um alarme pode existir e nunca rodar. Aqui em três formas — suíte opt-in cujo único gatilho era push para uma branch que o fork não tem (`promotion-gate.yml` → `testing`); regex de teste que rejeitava o sufixo local da versão da casa (`\d+\.\d+\.\d+` contra `2.4.0+dex.N`); e alarme que só toca no CI depois do push, num repo que empurra direto na `main`. Ao herdar workflow ou teste de upstream, conferir o `on:` contra `git branch -r` e as validações de formato contra o esquema real do fork.

**Armadilha operacional:** em clone ou worktree novo do CRG, o hook do Playbook recusa todo commit (`DRIFT DETECTADO`, exit 2). A projeção commitada só é fresca na árvore onde foi gerada (hash de bytes brutos, `generate-playbook.py` l.229) e o hook está no índice como `100644`. Regenerar com `generate-playbook.py --write` antes de commitar lá, sem commitar a projeção regenerada por engano. Causa e cura proposta: registry ISSUE-LOCAL-0051.

**Why:** o dono pediu teste de regressão "para garantir que não se repita"; a repetição vinha de alarmes desligados, não de falta de teste — por isso a cura tem gate no commit e não só teste.

**How to apply:** ao tocar versão do CRG, `python -B tools/release_version.py --check` (gatilho `CRG-BUMP-UMA-FONTE`); ao revisar CI de fork, checar primeiro se os jobs que deveriam pegar o defeito executam de fato; o repo ganhou livro de ferramentas (`TOOLSBOOK.index.md`) — consultar antes de criar ferramenta. Rastros: TRACKER local do CRG (0008 fechado; 0009 aberto — o grafo reporta "untested" para módulo carregado por `spec_from_file_location`), registry ISSUE-LOCAL-0048 a 0052 (oráculos de teste com âncoras de build antigo, receita de junction do oraculo-solid, skill do CRG em dex.1, Playbook, réguas de shell e YAML preparadas). Pendências de decisão do dono: proteção de branch; comando único de bump. Relaciona: [[crg-cura-ci-8-classes-20261119]], [[merge-check-gatilho-prompt-pronto-20261116]], [[regra-oraculo-solid-fechamento-analise-lentes-go-padrao]].

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-versao-uma-fonte-gates-cegos-20261123-675313426b00-content
