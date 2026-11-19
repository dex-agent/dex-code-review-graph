---
implementation_version: v2
layer: L2
slug: bloco-0005-crg-dependabots-orfaos-fechados-branch-s-731b83a4e192
tags:
  - "#crg/oficina"
---

# Bloco 0005 CRG: dependabots orfaos fechados - branch staging fantasma

GO do dono (quiz do oraculo-solid 'GO 0005 agora', 2026-11-19) fechou o ISSUE-LOCAL-0005 do fork dex-agent/dex-code-review-graph com receipt por mutacao: (1) 5 PRs dependabot zumbis (abertos 11-08) fechados com comentario de razao; (2) .github/dependabot.yml REMOVIDO (commit c55bc695) — ACHADO: o yml apontava target-branch staging para uma branch que NAO EXISTE no remoto (git ls-remote --heads origin | grep -c staging = 0): automacao orfa de fork herdando config de upstream; licao transversal: antes de manter version-updates em fork, conferir ls-remote da branch-alvo; (3) vulnerability-alerts ON via gh api -X PUT (204); (4) publish.yml disabled_manually ate politica de release (trigger release:published — tag seca nao dispara); (5) CODEOWNERS minimo dex-agent (13fbe68f). Politica selada: fork acompanha upstream por merge manual da casa. Trilho .agents/PLAN-TASKS/2026-11-19-bloco-0005-auditoria.md CONCLUIDO (preflight achados=0); .agents/TRACKER e local-only (0 tracked — commitar so PLAN-TASKS). Tudo reversivel: pr reopen, restore yml, workflow enable, api DELETE alerts.

#crg/oficina

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^bloco-0005-crg-dependabots-orfaos-fechados-branch-s-731b83a4e192-content
