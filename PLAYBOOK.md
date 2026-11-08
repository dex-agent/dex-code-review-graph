---
name: "code-review-graph playbook"
description: "Regras de decisao e procedimentos deste projeto - projecao gerada das fontes citadas. Nao editar a mao."
type: playbook
generated_by: "tools/playbook/generate-playbook.py"
authority: derived_projection
sources_revision: "sha256:ae3676b07efcd7702e1fa081e3e95527202eccf7d12087edf52548d1c9b5a62f"
sent_revision: "sha256:ae3676b07efcd7702e1fa081e3e95527202eccf7d12087edf52548d1c9b5a62f"
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
- Fonte: `AGENTS.md#L147-L155`
- Selo: `pb-8572b9fc`

## Runbook <-> Playbook (procedimentos)

- (napkin ausente nesta copia)

## Plano de execucao vigente

- (sem trilho declarado neste repo)

## Fontes e revisao

| caminho | sha256 | Enviado? |
| --- | --- | --- |
| `AGENTS.md` | `c9ed3751d23b307949a86f006de4b7a29c3dce31d2871b7fbf855e2a1db9e515` | sim |
| `.agents/napkin.md` | `c9a5048699f7b1d24cf0591c110919b2e5b0d3d4d976ff58bb66f3ef2327afa0` | sim |
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
- MCP Tools: code-review-graph -> `AGENTS.md#L87` (sem token de localizador)
- Graphify local -> `AGENTS.md#L125` (sem token de localizador)
- Continuidade local (leitura obrigatória antes de trabalho não trivial) -> `AGENTS.md#L140` (sem token de localizador)
- Regras -> `workflow/code-review-graph-manutencao-iterativa-com-evidencia/RULES.md#L3` (sem token de localizador)
- Limites -> `workflow/code-review-graph-manutencao-iterativa-com-evidencia/RULES.md#L27` (sem token de localizador)
