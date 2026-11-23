---
name: "code-review-graph playbook"
description: "Regras de decisao e procedimentos deste projeto - projecao gerada das fontes citadas. Nao editar a mao."
type: playbook
generated_by: "tools/playbook/generate-playbook.py"
authority: derived_projection
sources_revision: "sha256:62645c954db72312484cc8cef815506f676ebfacb0f4fb4a60c60dad0b592ced"
sent_revision: "sha256:62645c954db72312484cc8cef815506f676ebfacb0f4fb4a60c60dad0b592ced"
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
- Fonte: `AGENTS.md#L86-L118`
- Selo: `pb-0f77b1c2`

### Leitura obrigatoria (bootstrap)

- Localizador: `PENDENTES-LEDGER`
- Gatilho: 5. `.agents/PENDENTES.md` — ledger de pendências append-only (schema `dex.pendencias.v2`; gatilho `PENDENTES-LEDGER`)
- Extrato: 1. `AGENTS.md`
- Rotas (nomes, na ordem):
  - `AGENTS.md`
  - `.agents/ACTIVE.md`
  - `.agents/HANDOFF.md`
  - `.agents/PLAN-TASKS/ACTIVE.md`
- Fonte: `AGENTS.md#L141-L149`
- Selo: `pb-fadeaf9c`

## Runbook <-> Playbook (procedimentos)

- (napkin ausente nesta copia)

## Plano de execucao vigente

- (sem trilho declarado neste repo)

## Fontes e revisao

| caminho | sha256 | Enviado? |
| --- | --- | --- |
| `AGENTS.md` | `1c45f94d4e2652a240d757d848b99d9d682452f2b7a19aee61a3e31b9a23c99f` | sim |
| `.agents/napkin.md` | `506b5c33c302d4af103b15d388c51e301de65b349bbde023fee43b8c343e9a60` | sim |
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
- Graphify local -> `AGENTS.md#L119` (sem token de localizador)
- Continuidade local (leitura obrigatória antes de trabalho não trivial) -> `AGENTS.md#L134` (sem token de localizador)
- Toolsbook — consulta e registro de ferramentas -> `AGENTS.md#L150` (sem token de localizador)
- Regras -> `workflow/code-review-graph-manutencao-iterativa-com-evidencia/RULES.md#L3` (sem token de localizador)
- Limites -> `workflow/code-review-graph-manutencao-iterativa-com-evidencia/RULES.md#L27` (sem token de localizador)
