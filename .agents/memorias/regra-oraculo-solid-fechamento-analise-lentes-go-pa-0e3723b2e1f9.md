---
implementation_version: v2
layer: L2
slug: regra-oraculo-solid-fechamento-analise-lentes-go-pa-0e3723b2e1f9
tags:
  - "#auto-memory/feedback"
---

# regra-oraculo-solid-fechamento-analise-lentes-go-padrao

Espelho da auto-memory do host ZCode (arquivo regra-oraculo-solid-fechamento-analise-lentes-go-padrao.md, tipo feedback).

GO do dono 2026-11-19 (sessão CRG cura-CI): todo pedido de ANÁLISE ao oraculo-solid termina com lentes dos especialistas ativos + Próximo passo único GO-PADRAO (sem alternativas) + Resumo claro; decisão pendente = AskUserQuestion com recomendada em 1º; silêncio = recomendada

Comando do dono (2026-11-19, mesma família da regra do chato `fechamento-lentes-go-unico-resumo-claro` gravada no mesmo dia): **sempre que o oraculo-solid receber pedido de `análise`**, o trabalho da análise finaliza com:

1. **Opiniões das lentes dos especialistas cooperadores ATIVOS** sobre o trabalho executado — nomeadas, cada uma com o achado que mudou decisão;
2. **"Próximo passo único recomendado GO-PADRAO:"** — com detalhes e **sem alternativas opcionais** (o rótulo GO-PADRAO liga o passo ao contrato `GO-ACEITE-RECOMENDACAO`: aceite do dono dispara o pipeline inteiro — Trilho/SPT v3 → validação → execução de todas as tasks → adversarial → verdict, sem encerrar turno entre fases);
3. **"Resumo claro:"**;
4. Se o final exigir definir/selecionar/escolha/decisão → **AskUserQuestion com contexto acumulado e recomendada EM PRIMEIRO**; nenhuma alternativa selecionada ⇒ **a recomendada é a escolhida** (ressalva da casa: decisão irreversível, destrutiva ou dinheiro real NÃO entra no automático — declara pendência e espera).

**Por que:** o dono padronizou o fechamento de análise para nunca terminar pendurado em menu e sempre sair com rota acionável acoplada ao pipeline GO-PADRAO.

**Como aplicar:** em qualquer janela/projeto que convoque o oraculo-solid. A regra voltou a viver no pacote da skill em 2026-11-23, na preferência `analise-termina-com-lentes-go-padrao-unico-resumo-claro` (receipt committed/validated, closeout valid=true): na sessão de 23/11 conferi e esse id não constava de nenhum `adopted-preferences*.json` do registry, nem do histórico git da skill — o registro de 19/11 não tinha ficado; regravei com o texto do dono. No mesmo dia entrou a irmã `analise-proximo-passo-o-que-indica-e-passo-a-passo-261123` (pedido de análise de próximo passo via grafo/semântico/RAG/FTS5 responde em duas partes: "O que indica" com selo e "Próximo passo a passo detalhado" com gate e critério de pronto por fase). Demais rastros: fila gate-feedback `fb-1795093509855-e32603ce`; espelho dex-memoria global receipt `3143802e`, gatilho `PADRAO-EVOLUTIVO-ORACULO-SOLID-ANALISE-LENTES-GO-PADRAO`. Irmã da regra do chato (feedback `fb-1795090629934`) — a casa tem fechamento contratado nas duas portas: execução pelo chato, análise pelo comandante oraculo-solid.

#auto-memory/feedback

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^regra-oraculo-solid-fechamento-analise-lentes-go-pa-0e3723b2e1f9-content
