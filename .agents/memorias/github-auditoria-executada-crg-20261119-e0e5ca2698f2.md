---
implementation_version: v2
layer: L2
slug: github-auditoria-executada-crg-20261119-e0e5ca2698f2
tags:
  - "#auto-memory/project"
---

# github-auditoria-executada-crg-20261119

Espelho da auto-memory do host ZCode (arquivo github-auditoria-executada-crg-20261119.md, tipo project).

Auditoria 7-frentes EXECUTADA no dex-agent/dex-code-review-graph

Auditoria read-only 7-frentes executada no repo ONLINE da casa
(`dex-agent/dex-code-review-graph`, 2026-11-19; prompt em
[[github-auditoria-repo-online-prompt-20261119]]). Laudo entregue; ZERO
mutações; **2 itens TRACKER propostos, aguardando GO do dono**.

**Armadilha medida (vacina)**: `gh` sem `-R` resolve o remote `upstream`
(tirth8205/code-review-graph) em vez do `origin` — em repo com 2 remotes,
TODO gh call precisa de `-R dex-agent/dex-code-review-graph` explícito.

**Achados (tabela do laudo)**:
- **P1 — CI vermelho crônico no main**: ≥6 failures (11-14→11-16; runs
  43929195987…43654239307), TODOS os jobs de teste. Root parcial decifrado
  no log-failed: job "Windows daemon and file handles" morre em
  `assert 'C:/…Example.php' == 'C:\\…Example.php'` — classe path-separator
  (as_posix) IRMÃ da que o A/B 2.4.0+dex.1 curou localmente; ubuntu root
  não triada. Lição: suíte A/B verde local ≠ CI verde.
- **P2 — Dependabot zumbi ×5** (PRs #1-#5 de 11-08, base andou 100+ commits
  pós-merge, mergeable UNKNOWN, #1 FAILURE) + bot pr-review-comment do
  próprio CRG comentando sozinho; **alerts dependabot OFF** com updates ON.
- **P2 — Drift local**: behind 2 (`2fababd5` crg-m19 verdict/handoff,
  `c6146110` fix `--files` scope — de outra janela) + `uv.lock` sujo.
- **P3**: 0 tags/0 releases (tag SECA `v2.4.0+dex.1` ok — NUNCA criar
  Release: `publish.yml` (PyPI) dispara em `release:published` + environment
  pypi); main sem proteção; CODEOWNERS ausente; publish.yml latente no fork.
- F3 verde por desenho (0 issues GitHub = TRACKER local, padrão OFFLINE).

**Barata-scan: 2 classes** (não 8 achados): (A) automação órfã do fork (CI +
dependabot + bot + alerts = ninguém é dono do que o upstream deixou rodando);
(B) path-separator Windows no CI (irmã da classe A/B curada). Se GO: 2 itens
TRACKER local via dex-gerar-issues-git com runs/PRs como evidência.

Related: [[crg-240dex-merge-fechado-20261115]], [[reconhecimento-code-review-graph]]

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^github-auditoria-executada-crg-20261119-e0e5ca2698f2-content
