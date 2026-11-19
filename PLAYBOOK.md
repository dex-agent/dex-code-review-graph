---
name: "code-review-graph playbook"
description: "Regras de decisao e procedimentos deste projeto - projecao gerada das fontes citadas. Nao editar a mao."
type: playbook
generated_by: "tools/playbook/generate-playbook.py"
authority: derived_projection
sources_revision: "sha256:f5b0f12011a467205af269019033bfadb1eb41c67ab1eedbf8774ad484b2b7ff"
sent_revision: "sha256:f5b0f12011a467205af269019033bfadb1eb41c67ab1eedbf8774ad484b2b7ff"
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

### CLI: code-review-graph

- Localizador: `CRG-BUMP-CONSUMIDORES`
- Gatilho: o [check de frescor](.agents/GATILHOS-VIVOS.md#staleness-artefatos-derivados).
- Extrato: **GATE DE CONSUMIDORES NO BUMP** (localizador `CRG-BUMP-CONSUMIDORES`): toda
- Fonte: `AGENTS.md#L86-L109`
- Selo: `pb-a8bd4dc6`

### Leitura obrigatoria (bootstrap)

- Localizador: `PENDENTES-LEDGER`
- Gatilho: 5. `.agents/PENDENTES.md` — ledger de pendências append-only (schema `dex.pendencias.v2`; gatilho `PENDENTES-LEDGER`)
- Extrato: 1. `AGENTS.md`
- Rotas (nomes, na ordem):
  - `AGENTS.md`
  - `.agents/ACTIVE.md`
  - `.agents/HANDOFF.md`
  - `.agents/PLAN-TASKS/ACTIVE.md`
- Fonte: `AGENTS.md#L132-L140`
- Selo: `pb-457239ee`

## Runbook <-> Playbook (procedimentos)

- (napkin ausente nesta copia)

## Plano de execucao vigente

- (sem trilho declarado neste repo)

## Fontes e revisao

| caminho | sha256 | Enviado? |
| --- | --- | --- |
| `AGENTS.md` | `368b9562794709ef756d94c749cef6522b030ea7cb436d13c62894817fd52842` | sim |
| `.agents/napkin.md` | `731d3b5d071fe69c1d5d504e990d1f331f802d5bf27d4567dac18c9a62116271` | sim |
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
- Graphify local -> `AGENTS.md#L110` (sem token de localizador)
- Continuidade local (leitura obrigatória antes de trabalho não trivial) -> `AGENTS.md#L125` (sem token de localizador)
- Regras -> `workflow/code-review-graph-manutencao-iterativa-com-evidencia/RULES.md#L3` (sem token de localizador)
- Limites -> `workflow/code-review-graph-manutencao-iterativa-com-evidencia/RULES.md#L27` (sem token de localizador)
