---
implementation_version: v2
layer: L2
slug: artefato-em-temp-exige-destino-duravel-no-mesmo-blo-7fcf5ea2eb43
tags:
  - "#auto-memory/feedback"
---

# artefato-em-temp-exige-destino-duravel-no-mesmo-bloco

Espelho da auto-memory do host ZCode (arquivo artefato-em-temp-exige-destino-duravel-no-mesmo-bloco.md, tipo feedback).

Cobrança do dono (2026-11-23): artefato com valor de reuso que

Artefato com valor de reuso que nasce em lugar descartável (Temp do sistema, `mktemp -d`, worktree ou clone temporário) é dívida do bloco que o criou: ou ganha destino durável na mesma sessão (`tools/` com ficha, recibo em disco), ou é declarado descartável. Pendência registrada não é destino.

**Why:** o dono perguntou "temos uma versão ou cópia dela onde?" sobre um harness que eu tinha deixado só na Temp e rotulado de "pendência". Resgatei os arquivos e segui o trabalho, sem gravar nada. A cobrança veio em seguida: "não fez o mínimo esforço pra aprender com isso, isso é um achado memorável". Três instâncias medidas no mesmo dia no CRG: o harness diferencial ficou uma janela inteira só na Temp; o commit `6f0b85d` existia só numa pasta descartável há sete dias; e eu criei cinco scripts em `/tmp`. Duas regras que mandavam fazer diferente já existiam no pacote do chato (`intervencao-termina-em-aprendizado`, `ouro-garimpado-auto-gravar-sem-cobranca`) e eu não as apliquei.

**Mecanismo do meu erro:** (1) registrar uma pendência parecia resolver; (2) deixei o aprendizado "para o fechamento", que é o primeiro passo que eu adianto quando o contexto pesa; (3) o gate de fechamento do chato já tinha sido consumido e, quando chegou evidência nova, não reabri; (4) gravei só a lição que o dono tinha cobrado explicitamente.

**How to apply:**
- Ao criar qualquer coisa fora do repo e do acervo, decidir o destino na hora. "Decido depois" não existe.
- Pergunta do dono que revela lacuna é intervenção: a resposta executa a cura e grava o aprendizado (dex-memoria com gatilho, mais validação) antes de retomar a tarefa interrompida.
- Gate de fechamento consumido não vale para evidência que chega depois: reabrir a classificação.
- Ferramenta de fechamento da casa (`dex-fechamento-projeto-atualizado`, passo TEMP/TMP) só olha `.agents/TEMP`, `TEMP` e `TMP` dentro do repo: dá verde com artefato do bloco na Temp do sistema. Provado em 2026-11-23 com controle positivo: repo vazio mais resíduo plantado na Temp → `temp_tmp ok`. A cura de engenharia está especificada em ISSUE-LOCAL-0053 do registry (testes T1 a T6) e no Trilho `2026-11-23-fechamento-temp-fora-do-repo`, aguardando GO do dono.
- Memória gravada não garante recall: só o gate determinístico não depende de eu lembrar.
- gatilho: ARTEFATO-EM-TEMP-EXIGE-DESTINO-DURAVEL

Relaciona: [[sonda-e-script-de-prova-seguem-dex-toolsbook]], [[dado-herdado-de-resumo-e-hipotese-reexecutar]], [[crg-pr6-effect-fn-revisao-20261123]].

#auto-memory/feedback

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^artefato-em-temp-exige-destino-duravel-no-mesmo-blo-7fcf5ea2eb43-content
