---
implementation_version: v2
layer: L2
slug: registry-governanca-3505-guarda-plaquinhas-c9be73967e8f
tags:
  - "#auto-memory/project"
---

# registry-governanca-3505-guarda-plaquinhas

Espelho da auto-memory do host ZCode (arquivo registry-governanca-3505-guarda-plaquinhas.md, tipo project).

Corte 3.505.0 do registry de skills (2026-11-14) — guarda-plaquinhas

Pedido direto do dono (2026-11-14): "quando precisa de escolha ou decisao peça com AskUserQuestion com contexto e recomendacao — adicione isso nas $guarda-plaquinhas". Executado pelo gate da Governanta (plaquinha `SKILL-ADMISSION-GATE-OBRIGATORIO`, que cobre EDITAR): rota validada como contrato da própria skill (não conteúdo informacional → não era caso de napkin/mesa).

**Corte 3.505.0** (bump minor de 3.504.0): seção `## Protocolo de decisao (pergunta ao dono)` em `~/.agents/skills/guarda-plaquinhas/SKILL.md` (~linha 128) — decisão do dono = quiz com alternativas (AskUserQuestion no ZCode) com contexto acumulado + recomendação da casa como PRIMEIRA alternativa + opções fechadas, esgotando fontes antes; ponte para a regra global `INTERROGAR-ESGOTOU-PESQUISAR-NAO-ADIVINHAR` (sem duplicar o texto). INDEX não tocado (sem mudança de descoberta). Arquivos: SKILL.md + `00-governanca-mesa-de-skills.md` (bump) + `CHANGELOG.md` (entrada 3.505.0). Validado por rg nas três superfícies; cold-start intacto.

**RESOLVIDO (2026-11-14, turno seguinte)**: a janela paralela commitou meu corte E o **generalizou** — commit `5337df14` "feat(guarda-plaquinhas): protocolo de decisao generalizado p/ TODO bloco de trabalho (GO do dono 2026-11-14 + feedback fb-1794695615784)": SKILL.md +25 linhas (minha seção ~L132 preservada + generalização citando as palavras do dono) + CAPACITY.md. Minha sessão conferiu integridade (seção + CHANGELOG 3.505.0 no topo) e **publicou**: push via `dex-git-fechamento` (4 cortes ahead → `main`=`origin/main`, remote github dex-agent/skills). A anomalia staged/unstaged era mesmo a janela concorrente. Receipt do scan de fechamento `fechamento-20261114-1942.json` commitado (`8134e2e2`) e pushed. **4 REDs do scan (memoria-viva, garimpo, gatilhos_vivos, git/tree suja 19) são dívida da janela NIM em voo** (3ª leva dex-ignore mid-apply) — declarados com owner no receipt, NÃO corrigidos (colisão). Primeira aplicação prática do protocolo: AskUserQuestion p/ escopo CRG, recomendada em 1º, dono aceitou.

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^registry-governanca-3505-guarda-plaquinhas-c9be73967e8f-content
