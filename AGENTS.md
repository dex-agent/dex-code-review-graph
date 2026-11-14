# Agent Instructions

This project uses **bd** (beads) for issue tracking. Run `bd prime` for full workflow context.

## Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work atomically
bd close <id>         # Complete work
bd dolt push          # Push beads data to remote
```

## Non-Interactive Shell Commands

**ALWAYS use non-interactive flags** with file operations to avoid hanging on confirmation prompts.

Shell commands like `cp`, `mv`, and `rm` may be aliased to include `-i` (interactive) mode on some systems, causing the agent to hang indefinitely waiting for y/n input.

**Use these forms instead:**
```bash
# Force overwrite without prompting
cp -f source dest           # NOT: cp source dest
mv -f source dest           # NOT: mv source dest
rm -f file                  # NOT: rm file

# For recursive operations
rm -rf directory            # NOT: rm -r directory
cp -rf source dest          # NOT: cp -r source dest
```

**Other commands that may prompt:**
- `scp` - use `-o BatchMode=yes` for non-interactive
- `ssh` - use `-o BatchMode=yes` to fail instead of prompting
- `apt-get` - use `-y` flag
- `brew` - use `HOMEBREW_NO_AUTO_UPDATE=1` env var

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:ca08a54f -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd dolt push
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->

## CLI: code-review-graph

**TRACKER-LOCAL** — leia [.agents/TRACKER/INDEX.md](.agents/TRACKER/INDEX.md)
na retomada para encontrar issues locais abertas.

Use o executável do PATH para consultar o grafo. Antes da consulta, aplique
o [check de frescor](.agents/GATILHOS-VIVOS.md#staleness-artefatos-derivados).
Use `detect-changes` para revisar diffs, `impact` para rastrear efeitos e
`query` para consultar relações como `tests_for`. Confira achados no Git e
no código-fonte.

Mantenha o CRG fora do cadastro MCP do Codex. No Windows, o Codex inicia
`code-review-graph serve` pelo mesmo executável do PATH, e as instâncias
ativas impedem a substituição desse executável durante a instalação do wheel.

## Graphify local

<!-- GRAPHIFY-LOCAL:START -->
Catálogo automático; preserve regras humanas fora destes marcadores.

- **Grafo registrado**: `agents-graphify-gatilhos-crg-2026-07-31` (16 nós, 13 arestas, 8 comunidades, 0 arquivos)
  - Localizador: `GRAPHIFY-LOCAL::agents-graphify-gatilhos-crg-2026-07-31`
  - Status: `ativo`
  - Graph: `.agents/GRAPHIFY/gatilhos-crg-2026-07-31/graphify-out/graph.json`
  - Report: `.agents/GRAPHIFY/gatilhos-crg-2026-07-31/graphify-out/GRAPH_REPORT.md`
  - Consulta: `graphify query "<pergunta>" --graph ".agents/GRAPHIFY/gatilhos-crg-2026-07-31/graphify-out/graph.json"`

- Todo achado Graphify é `source: graphify` até confirmação por `rg` ou fonte viva.
<!-- GRAPHIFY-LOCAL:END -->

## Continuidade local (leitura obrigatória antes de trabalho não trivial)

- Leia `.agents/ACTIVE.md`
- Leia `.agents/HANDOFF.md`
- Leia `.agents/napkin.md` — runbook tático ativo: gotchas, comandos confiáveis, "Faça em vez disso"
- Leia `.agents/GATILHOS-VIVOS.md` — lembrança quente: gatilhos de reuso da janela de contexto atual

## Leitura obrigatoria (bootstrap)
1. `AGENTS.md`
2. `.agents/ACTIVE.md`
3. `.agents/HANDOFF.md`
4. `.agents/PLAN-TASKS/ACTIVE.md`
5. `.agents/PENDENTES.md` — ledger de pendências append-only (schema `dex.pendencias.v2`; gatilho `PENDENTES-LEDGER`)
6. `.agents/napkin.md`

<!-- playbook-pointer:start -->
## Playbook (entrada externa)

Este repo publica `PLAYBOOK.md` e `PLAYBOOK.index.json` na raiz: projecao GERADA
das regras de decisao (fontes declaradas em `tools/playbook/playbook-sources.txt`).
Nao editar a mao; a decisao completa mora na fonte citada.
Regenerar apos editar fonte:
`python -B tools/playbook/generate-playbook.py --repo . --write`.
Verificar frescor: mesmo comando com `--check` (exit 0 limpo, exit 2 drift).
Ativar trava de commit: `git config core.hooksPath tools/playbook/hooks`.
<!-- playbook-pointer:end -->
