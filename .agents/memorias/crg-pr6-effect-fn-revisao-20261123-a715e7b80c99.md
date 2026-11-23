---
implementation_version: v2
layer: L2
slug: crg-pr6-effect-fn-revisao-20261123-a715e7b80c99
tags:
  - "#auto-memory/project"
---

# crg-pr6-effect-fn-revisao-20261123

Espelho da auto-memory do host ZCode (arquivo crg-pr6-effect-fn-revisao-20261123.md, tipo project).

PR #6 do CRG (Index TypeScript functions created by Effect.fn),

PR #6 do fork `dex-agent/dex-code-review-graph` (branch `codex/crg-effect-fn`): o parser do CRG passa a indexar funções TypeScript criadas com `Effect.fn`. Veio do agente do dono noutra máquina. Trilho `.agents/PLAN-TASKS/2026-11-23-revisao-pr6.md`.

**Estado final (2026-11-23):** veredito "aprovado com lapidas recomendadas"; dono escolheu "Re-autorar e completar"; commits `a9e490ae` (o do PR) e `d3771a6b` (lapida), ambos de `dex-agent <dex-agent@proton.me>`; CI do PR run `45259265180` success (20 jobs, 1 skipped); **mergeado às 20:47Z, merge commit `fd2fb339`**; pasta principal em `fd2fb339` com o `Effect.fn` no `parser.py`; worktree `crg-pr6-wt` removido da Temp e branch local apagada (a branch remota foi preservada). CI do merge: run `45262935195`.

**Por que importa:** sem isso o CRG não via essas funções (37 nós nos ai-docs do OpenBot; a função `execute` com 21 ligações no arquivo em vez da função).

**How to apply:**
- `code_review_graph/parser.py` é arquivo do upstream (23 mil linhas), não é ferramenta minha; só o trecho do Effect.fn (cinco funções `_js_effect_fn_*`, `_js_string_first_argument`, `_js_imports_from`) é do fork.
- Lapida provada sem mudança de comportamento: 53 testes no arquivo; suíte JS/TS ampla com as mesmas 54 falhas de base nas duas árvores; sonda `tools/js_form_probe.py` idêntica; `parser.py` com 73 achados de CC, igual à main.
- `update` não reparsa arquivo inalterado: grafo antigo precisa de `build` completo (provado por execução; ISSUE-LOCAL-0011).
- Pendências: TRACKER 0010 (parâmetro local chamado `test`) e 0011 abertos; wheel do PATH (2.4.0+dex.3) sem a feature até bump dex.4, que também fecha a entrada Unreleased do FEATURES. O harness diferencial foi promovido a `tools/parser_diff.py` no fechamento (ficha `parser-diff`).
- gatilho: CRG-RECEIPTS-NAO-RASTREAR
- Desvio da sessão: o commit `e6a9a40e` deixou a main vermelha por force-add sob `.agents/receipts/`; curado em `b9976bd3` (run `45258942044` success).
- **Temp:** o `/tmp` do Git Bash é `%LOCALAPPDATA%\Temp\16\`. O harness diferencial (`diffdump.py`, `diffcmp.py`, `mkprobes.py`, despejos e 17 sondas) só existia lá; resgatado para `.agents/receipts/CRG-PR6-REVISAO-20261123/harness-diferencial/` (com README). Evidências pequenas de blocos antigos e o patch do commit descartável `6f0b85d` foram para `.agents/receipts/resgate-temp-20261123/`. Com autorização do dono, apagados dois bancos de grafo derivados (`crg-build-capture`, 504 MB; `crg-merge-v0tz2wgi`, 211 MB). Não tocados: cópia de 170 MB do registry (`tmp.00KmGXj9G4`) e outras `tmp.*` sem origem atribuída ao CRG.
- **A cobrança que veio depois:** resgatei os arquivos e segui sem gravar o aprendizado; o dono cobrou ("não fez o mínimo esforço pra aprender; isso é um achado memorável"). A lição está em [[artefato-em-temp-exige-destino-duravel-no-mesmo-bloco]] (gatilho L1 `ARTEFATO-EM-TEMP-EXIGE-DESTINO-DURAVEL`). As quatro perguntas do dono (virar aprendizado, ser recuperável, sintoma ou causa, teste automatizado) foram respondidas no fechamento: a cura de engenharia é o Trilho `2026-11-23-fechamento-temp-fora-do-repo` no workspace do registry (ISSUE-LOCAL-0053, testes T1 a T6 especificados, ponto cego provado com controle positivo), aguardando GO.
- Ao relatar, o dono cobra três coisas sobre artefato em pasta temporária: onde está a cópia durável, por que foi alterado ali e quem limpa. Responder com inventário conferido no disco e nomear o responsável pela limpeza.
- Saídas de comando com `ls` sem limite despejaram a listagem inteira de uma pasta de 12 mil arquivos; sempre limitar (`| head`) e conferir tamanho antes de listar.

Relaciona: [[sonda-e-script-de-prova-seguem-dex-toolsbook]], [[dado-herdado-de-resumo-e-hipotese-reexecutar]], [[artefato-em-temp-exige-destino-duravel-no-mesmo-bloco]], [[identidade-git-dex-agent-rewrite-20261121]], [[crg-versao-uma-fonte-gates-cegos-20261123]].

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-pr6-effect-fn-revisao-20261123-a715e7b80c99-content
