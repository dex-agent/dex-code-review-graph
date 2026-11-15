---
name: "code-review-graph playbook"
description: "Regras de decisao e procedimentos deste projeto - projecao gerada das fontes citadas. Nao editar a mao."
type: playbook
generated_by: "tools/playbook/generate-playbook.py"
authority: derived_projection
sources_revision: "sha256:de7568462e371bf2986ce97ef81106e1f6993621833fa58cf9761a06da05b1c8"
sent_revision: "sha256:de7568462e371bf2986ce97ef81106e1f6993621833fa58cf9761a06da05b1c8"
do_not_edit: true
---
# Playbook - code-review-graph

## Como usar este playbook

Projecao GERADA das regras de decisao deste repo; a decisao completa mora na fonte citada.
Executar uma regra exige ler a fonte; extratos terminam em '...' quando truncados.
Regenerar apos editar fonte: `python -B tools/playbook/generate-playbook.py --repo . --write`.
Verificar frescor: `python -B tools/playbook/generate-playbook.py --repo . --check` (exit 0 limpo, exit 2 drift).
Ativar trava de commit: `git config core.hooksPath tools/playbook/hooks`.
Destinatario do projeto: `--check-sent` valida as fontes enviadas neste clone.

## Regras de decisao (plaquinhas)

### Leitura obrigatoria (bootstrap)

- Localizador: `PENDENTES-LEDGER`
- Gatilho: 5. `.agents/PENDENTES.md` — ledger de pendências append-only (schema `dex.pendencias.v2`; gatilho `PENDENTES-LEDGER`)
- Extrato: 1. `AGENTS.md`
- Rotas (nomes, na ordem):
  - `AGENTS.md`
  - `.agents/ACTIVE.md`
  - `.agents/HANDOFF.md`
  - `.agents/PLAN-TASKS/ACTIVE.md`
- Fonte: `AGENTS.md#L123-L131`
- Selo: `pb-5756ab4e`

## Runbook <-> Playbook (procedimentos)

- (napkin ausente nesta copia)

## Plano de execucao vigente

- (sem trilho declarado neste repo)

## Fontes e revisao

| caminho | sha256 | Enviado? |
| --- | --- | --- |
| `AGENTS.md` | `1a16cde7723bb4f8616abf18e80f87f3d4684f451517227ce4bf0caf1a6d4365` | sim |
| `.agents/napkin.md` | `28961d68eaff55794e2cd81379eefb03585cfb8650fd19ed2898cfe94a4c4f3a` | sim |
| `workflow/code-review-graph-manutencao-iterativa-com-evidencia/RULES.md` | `c17e9297ebcb43f01558f95fc11c84eb2fc8f33171dbe4d0cd2df16ab12a7e05` | sim |

## Superficie enviada vs local

- O clone entrega: raiz commitada (fontes enviadas, PLAYBOOK.md, PLAYBOOK.index.json, tools/).
- Nao viajam: `.agents/` inteiro (napkin, trilhos, auditorias) - itens marcados (local).
- Como reagir: regra completa esta na fonte enviada; procedimento (local) pede data e localizador ao dono.

## Secoes nao decodificadas

- Quick Reference -> `AGENTS.md#L5` (sem token de localizador)
- Non-Interactive Shell Commands -> `AGENTS.md#L15` (sem token de localizador)
- Beads Issue Tracker -> `AGENTS.md#L40` (sem token de localizador)
- Session Completion -> `AGENTS.md#L59` (sem token de localizador)
- CLI: code-review-graph -> `AGENTS.md#L86` (sem token de localizador)
- Graphify local -> `AGENTS.md#L101` (sem token de localizador)
- Continuidade local (leitura obrigatória antes de trabalho não trivial) -> `AGENTS.md#L116` (sem token de localizador)
- Regras -> `workflow/code-review-graph-manutencao-iterativa-com-evidencia/RULES.md#L3` (sem token de localizador)
- Limites -> `workflow/code-review-graph-manutencao-iterativa-com-evidencia/RULES.md#L27` (sem token de localizador)
