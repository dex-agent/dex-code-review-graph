---
implementation_version: v2
layer: L2
slug: dex-ignore-auditoria-registry-20261114-58706b71e0bd
tags:
  - "#auto-memory/project"
---

# dex-ignore-auditoria-registry-20261114

Espelho da auto-memory do host ZCode (arquivo dex-ignore-auditoria-registry-20261114.md, tipo project).

Auditoria dex-ignore no registry de skills (2ª passada 2026-11-14)

Auditoria `$dex-ignore` (read-only) no repo de skills `~/.agents/skills` (HEAD `9d4ca7b5`, 2026-11-14). Achados: **229 arquivos de conhecimento durável ignorados** que o clone perderia — `.agents/REPORTS/` (16 laudos/provas), 70 laudos `.md` de `GRAPHIFY/skills-catalog` (PILOT/REBUILD-REPORTs), Trilhos/evidências aninhados de skills (`technical-book-to-skill-router/.agents/{PLAN-TASKS,TEST-BATTERIES}`, `codex-orquestrador-multimodelo/.agents/EVIDENCIAS`, `governancia-skills/.agents/AUDITORIAS`), 11 receipts colaterais em `AUDITORIAS/EVIDENCIAS/**/.agents/**` e `probe-hud-playback.ps1`. Regra vencedora da quase totalidade: `**/.agents/*` (L11). Falsos alarmes descartados com prova: clean-code (só `*.bak-*`; 18 chapters rastreados) e probe de sensibilidade (2 hits = descrição da skill ngrok). Exclusões corretas mantidas: CHECKPOINTS, ARQUIVO-TEMP, SYNC-LAB, `.dex-memoria/transactions` (120M ledger), `.ppirtv` (41M runtime), LIXEIRA, backups.

**Diff proposto ensaiado em fixture v2 (verde: 9 candidatos elegíveis, 9 sentinelas ignoradas)** — anexar ao final do `.gitignore` do registry: `!.agents/REPORTS/`, `!.agents/SCRIPTS/` + `.agents/SCRIPTS/*` + `!probe-hud-playback.ps1`, `!.agents/GRAPHIFY/skills-catalog/*.md`, `!.agents/AUDITORIAS/EVIDENCIAS/**` + re-asserto `*.log`/`**/__pycache__/`/`*.pyc`, e as 4 exceções aninhadas explícitas. A lição semântica (reabrir ancestrais; negação de descendente não desce em pai excluído) já mora em `dex-ignore/references/git.md` — não duplicar.

**RESOLVIDO (2026-11-14, turno seguinte)**: o dono deu GO em outra via e a **janela paralela aplicou a auditoria como "3ª leva"** — commits `bcdea41a` (grafo ATIVO 688 + receitas REBUILD/PILOT versionados, GO "Ativo + receitas") e `e1083f48` (gitignore 3ª leva: logs de prova de auditoria cega, estado vivo aninhado de skills, guards `memory/.gitignore` minimal — re-incluiu `technical-book-to-skill-router/.agents/{TEST-BATTERIES,COMPARACOES,PESQUISA,SQUADS,REPORTS,REUNIAO,PROMPTS,PROJECT.md,MEMORY.ndjson,ESTACIONAMENTO.md}`, `codex-orquestrador/.agents/EVIDENCIAS`, `governancia-skills/.agents/AUDITORIAS`, `upgrade-skill-v3/.agents/REPORTS`, `dex-notas-citaveis/.agents/EVIDENCIAS`, `pragmatico/.agents/{lembranca,memorias}`), tudo **pushed** por esta sessão. Ainda **in-flight da janela NIM**: complemento 3b do `.gitignore` (unstaged, mid-merge) + 19 arquivos elegíveis não-commitados — não tocar. As lacunas declaradas (espelho `.ppirtv/verdicts|evidence` por flow, `ppi-install-codex-fix/`) seguem em aberto com a janela NIM. Laudo da 2ª passada entregue só na resposta (read-only). Relacionado: [[reconhecimento-code-review-graph]] e [[registry-governanca-3505-guarda-plaquinhas]].

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^dex-ignore-auditoria-registry-20261114-58706b71e0bd-content
