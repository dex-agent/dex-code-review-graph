---
implementation_version: v2
layer: L2
slug: github-auditoria-repo-online-prompt-20261119-e5a03f701696
tags:
  - "#auto-memory/reference"
---

# github-auditoria-repo-online-prompt-20261119

Espelho da auto-memory do host ZCode (arquivo github-auditoria-repo-online-prompt-20261119.md, tipo reference).

Prompt pronto de auditoria COMPLETA de repo GitHub online (7 frentes,

Prompt pronto entregue ao dono (2026-11-19) para revisão completa de
repositório ONLINE no GitHub. Desenho:

- **7 frentes**: (1) metadados/branches/tags×releases; (2) PRs abertos
  (zumbi >14d, vermelho crônico, conflito) + últimos 20 mergeados; (3) issues
  (idade/labels/stale/duplicatas + 10 fechadas p/ prioridade real); (4) Actions
  (taxa de falha por workflow, runs presos, workflow quebrado); (5) mensagens/
  comentários (timeline de PRs/issue ativos, bots rugindo sozinhos); (6)
  higiene/segurança read-only (alerts, CODEOWNERS, SECURITY.md — nunca conteúdo
  de secret); (7) drift local×remoto (fetch --prune + status -sb).
- **Disciplina**: 100% READ-ONLY — zero comment/close/merge/re-run/label sem GO
  explícito; laudo em tabela `| Achado P1/P2/P3 | Evidência (URL/nº/run) |
  Ação |` — achado sem permalink/número não entra.

**Roteamento de ferramentas (esclarecido após pergunta do dono)**: `gh` CLI
sozinho cobre tudo — as skills do plugin github (github:pr/issue/repo/
workflow-run/release) são RECEITAS que giram o mesmo gh (rota B, útil só em
host sem terminal); NÃO existe skill de plugin para mensagens/comentários
(é `gh api`/`--comments`). Skills da casa que entram de verdade:
`dex-barata-scan` da classe antes de propor itens TRACKER (3 PRs zumbis da
mesma causa = 1 item); `dex-gerar-issues-git` SOMENTE se o dono der GO.

**VERSÃO FINAL consolidada entregue ao dono** (mesma data): rota-por-frente
no cabeçalho (gh mestra OU skill do plugin, "nunca as duas pela metade") +
fechamento com barata-scan de classe e dex-gerar-issues-git sob GO. Validação:
toda linha da tabela com evidência clicável + frente 7 respondendo o
alinhamento local×remoto; mutação sem GO = violação do prompt.

Related: [[crg-grafo-registry-scripts-20261117]] (mesma família de prompts
prontos coletados pelo dono)

#auto-memory/reference

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^github-auditoria-repo-online-prompt-20261119-e5a03f701696-content
