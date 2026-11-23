---
implementation_version: v2
layer: L2
slug: identidade-git-dex-agent-rewrite-20261121-0cd25611ea22
tags:
  - "#auto-memory/project"
---

# identidade-git-dex-agent-rewrite-20261121

Espelho da auto-memory do host ZCode (arquivo identidade-git-dex-agent-rewrite-20261121.md, tipo project).

REESCRITA DE IDENTIDADE GIT (2026-11-21, decisão do dono via quiz 'Reescrever tudo'): ~/.gitconfig global trocado para dex-agent <dex-agent@proton.me>; git filter-repo com callback restrito reescreveu CRG (2238 commits, 350aaf3e→b9da3d8d, tag v2.4.0+dex.1 9ca592aa→ddbc4a0d) e registry de skills (496 commits, 02e720de→8053bbfa); commit-maps velho→novo commitados como receipt nos 2 repos; upstream intocado

Correção do dono (2026-11-21): commits da casa exibiam a conta **ultraflashlan** no GitHub porque o `~/.gitconfig` global tinha `ultraflash@flexworksolutions.shop` — correto é **`dex-agent <dex-agent@proton.me>`** (conta github.com/dex-agent; email JÁ vinculado, provado por commits existentes atribuídos ao login dex-agent). `gh` autentica como dex-agent (quem pusha/operou API); a autoria EXIBIDA vinha do email do git config.

**Cura em 2 partes**: (1) config global trocado (afeta commits futuros de TODAS as janelas); (2) dono escolheu **"Reescrever tudo"** via quiz informado (viu que hashes mudam e rastreabilidade quebra) → `git filter-repo --force --email-callback` restrito ao email antigo:
- **CRG**: 2238 commits reescritos (main `350aaf3e`→`b9da3d8d`; tag `v2.4.0+dex.1` `9ca592aa`→`ddbc4a0d`, conteúdo idêntico); tag upstream `v2.4.0` INTACTA (callback não toca terceiros) — 3.24s.
- **registry de skills**: 496 commits (`02e720de`→`8053bbfa`; incluiu 2 commits a-frente de janela paralela) — 9.8s.
- Verificação: `gh api commits` 5/5 = `dex-agent | dex-agent@proton.me` em ambos.

**A engenharia que preservou a rastreabilidade**: commit-map velho→novo de cada repo commitado como receipt durável (`.agents/receipts/rewrite-20261121/` em ambos — CRG 2239 linhas, registry 497). Hashes antigos citados em memórias/TRACKER/receipts/flows continuam consultáveis pelo mapa.

**Regra permanente (dono, 2026-11-23, ao responder o quiz do PR #6):** "troca pra `dex-agent` **sempre** — às vezes é algum email que estava na máquina que estava testando". Commit que chega de outra máquina com email esquecido (caso: `crsantosxx@gmail.com` no PR #6) é do próprio dono; re-autorar sem perguntar de novo. Receita usada: no worktree da branch, `git rebase origin/main`, commit novo pelo caminho normal (hooks rodam), e re-autoria por plumbing com árvore idêntica — `GIT_AUTHOR_NAME=dex-agent GIT_AUTHOR_EMAIL=dex-agent@proton.me GIT_AUTHOR_DATE="<data de autor original>" git commit-tree <árvore> -p <pai> -m "<mensagem>"` seguido de `git update-ref refs/heads/<branch> <novo>` — e push com `--force-with-lease=<branch>:<sha revisado>`. Precaução que continua valendo: commit de terceiro de verdade não se re-autora (apaga atribuição).

**Vacinas medidas**: (1) filter-repo REMOVE o remote origin e o upstream tracking ao final — anotar URL antes, `git remote add` + `push --set-upstream` depois; (2) filter-refo faz checkout e DESCARTA edição unstaged (o `lembranca.md` de janela paralela caiu — restaurado de BACKUP prévio; backup antes de rewrite é obrigatório em repo compartilhado); (3) `git pull --rebase` falha com unstaged changes → o rewrite roda mesmo assim com --force, mas alinhar com o remoto ANTES (fetch + rebase) é o correto para reescrever também os commits mais novos; (4) CI dos pushes forçados (docs-only) na fila — vigília por watch.

Relacionado: [[crg-cura-ci-8-classes-20261119]] · [[crg-35-comandos-prompts-modelos-20261119]] · [[dex-audio-motor-contrato-novo-20261121]]

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^identidade-git-dex-agent-rewrite-20261121-0cd25611ea22-content
