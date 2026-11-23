---
implementation_version: v2
layer: L2
slug: merge-check-gatilho-prompt-pronto-20261116-49f29c8892ec
tags:
  - "#auto-memory/project"
---

# merge-check-gatilho-prompt-pronto-20261116

Espelho da auto-memory do host ZCode (arquivo merge-check-gatilho-prompt-pronto-20261116.md, tipo project).

Merge-check gate por repo — DECISÃO FINAL do dono (2026-11-16, 2ª

**DECISÃO FINAL do dono (2026-11-16, CORREÇÃO supersede "agente evoca sem
hook/CI")**: "é instalar sim hooks no git — isso que é engenharia que evita o
problema!!" + precedente vivo citado pelo dono: `dex-playbook-entrada` já usa
hook sempre (`core.hooksPath` + script commitado; bloqueou 2 commits meus hoje
no registry e no repo CRG). O gate do merge-check mora em **HOOK DE GIT
`pre-merge-commit`**, padrão casa playbook. O momento permanece: dispara ANTES
DE INTEGRAR DUAS LINHAS DE DESENVOLVIMENTO — nunca no commit rotineiro, nunca
no update do índice do CRG.

**Desenho do hook (decifrado na fonte, entregue como prompt-pronto por repo)**:
- Momento git: `pre-merge-commit` (merge resolvido, ANTES do commit de merge
  nascer): OURS=`git rev-parse HEAD`, THEIRS=`git rev-parse MERGE_HEAD`,
  BASE=`git merge-base HEAD MERGE_HEAD`. Não-merge (sem MERGE_HEAD) → exit 0.
- **Vacina contra falso-positivo (armadilha medida na leitura do
  merge_check.py)**: o merge-check REFAZ o merge textual (`merge-tree`) sem a
  resolução humana → merge com conflito resolvido à mão daria `text_conflict`
  exit 1 e bloquearia merge legítimo. Cura no hook: MERGE_MSG com
  "# Conflicts:" → pular a camada textual e rodar a SUÍTE direto no worktree
  resolvido (o mesmo "merged checkout" da camada 3); sem conflito manual →
  merge-check completo (exit 0 passa · 1 bloqueia o commit de merge · 2
  execution_error REPORTA e NÃO bloqueia — suíte doente não é veredito).
- **hooksPath NUNCA sobrescrito**: se `core.hooksPath` já setado (ex.
  `tools/playbook/hooks`), o `pre-merge-commit` mora NO MESMO DIR (arquivo
  adicional) — trocar o valor orfandaria o hook do playbook.
- Suíte declarada em `tools/hooks/merge-check.conf` (1 linha `SUITE="..."`);
  sem suíte → avisa e NÃO bloqueia (nunca bloquear por forma).
- Escapes documentados no cabeçalho: `MERGE_CHECK_SKIP=1` ou
  `git merge --no-verify`.
- **`code-review-graph install` NÃO serve para isto** (confirmado no `--help`
  da 2.4.0+dex.1): registra MCP/skills/instruções e hooks de PLATAFORMA
  (contexto do grafo) — não é gate de merge; não usar nesta rota.
- **Lacuna declarada**: merge via PR (GitHub) não passa por hook local — nessas
  o gate volta a ser o agente evocar o merge-check antes de clicar em "Merge"
  (ficha 5W2H `MERGE-CHECK-HOOK-PRE-MERGE` no GATILHOS-VIVOS cobre).
- Prova do setup: `bash -n` + invocação em estado não-merge (exit 0) +
  hooksPath conferido com hooks antigos intactos; primeira prova real = o
  próximo `git merge`.

**Doctor false-red decifrado na fonte (defeito cosmético real da casa)**:
`code-review-graph doctor` reporta "This copy: 2.4.0" (fail) porque o literal
`__init__.py:__version__ = "2.4.0"` ficou no merge, enquanto dist-info/METADATA
= `2.4.0+dex.1` (o que a CLI `--version` lê). A instalação está CORRETA
(merge_check.py presente; `merge-check --help` exit 0; fumaça real com commits
3ddf2c8b/82f1fad3/54efb64c → passed exit 0, suíte 4/4 checkouts). Doctor nunca
fica verde até alinhar o literal à metadata (cura candidata: derivar
`__version__` de importlib.metadata). Item de TRACKER no repo CRG pendente de
abertura. Doctor também acusa grafo local stale (schema v9, built eeb486b) —
esperado, não afeta merge-check (laboratório descartável próprio).

**VERSAO FINAL = PROMPT JUNTO (hook + staleness, 1 paste só)**: o dono pediu
revisão do SEU prompt de STALENESS-CHECK e a junção com o meu de hook.
Entregue como UM prompt com 2 partes + relatório final. Revisões que fiz no
texto do dono: (1) `code-review-graph .exe status` → `code-review-graph
doctor` (read-only, mostra built-at vs HEAD + hooks de uma vez; path da casa
`.agents/CODE-REVIEW-GRAPH/` além de `.code-review-graph/`); (2) PLAYBOOK
registrado com o PAR completo (check exit 2 = drift; `--write` = regen — o
dele citava só o check); (3) bootstrap do hub GATILHOS-VIVOS e capability
check compartilhados pelas 2 partes.

**Parte B do prompt (staleness, conteúdo do dono lapidado)**: inventário
PROCURADO dos derivados (CRG/graphify/PLAYBOOK/INDEX/.agents/MAPAS — caminho
+ como saber quando gerado + comando de REGEN) → ficha 5W2H
`STALENESS-ARTEFATOS-DERIVADOS` com regra dos **3 números** ((a) fonte mudou
via `git log -1 --format=%cI`/stat, (b) artefato gerado, (c) fonte > artefato
→ STALE → regen → só então citar; medido, nunca "parece atual") + 3 E se??
(sem git → mtime; regenerador ausente → artefato "não consultável", nunca
citar número + estacionar com owner/quando; verde mas conteúdo errado →
verde de staleness não é prova de semântica, abre a FONTE). Validação:
`rg "STALENESS|MERGE-CHECK-HOOK"` + comandos READ-ONLY apenas (nunca regen
no setup). Duas fichas no hub com cross-ref: índice CRG stale NÃO invalida o
gate (merge-check tem laboratório próprio).

Contexto: diagnóstico ao vivo no PHP_AUTO_GERADO_V3 (pelo dono) deu capacidade
VERDE (exe 2.4.0+dex.1) e repo NÃO configurado.
Related: [[crg-240dex-merge-fechado-20261115]], [[entropia-conserta-na-descoberta-20261116]]

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^merge-check-gatilho-prompt-pronto-20261116-49f29c8892ec-content
