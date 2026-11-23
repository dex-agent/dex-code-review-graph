---
implementation_version: v2
layer: L2
slug: relatorios-distinguem-arquivo-alterado-de-ferrament-2d1ead95e14a
tags:
  - "#auto-memory/feedback"
---

# relatorios-distinguem-arquivo-alterado-de-ferramenta-criada

Espelho da auto-memory do host ZCode (arquivo relatorios-distinguem-arquivo-alterado-de-ferramenta-criada.md, tipo feedback).

Dono leu meu relatório do PR #6 (2026-11-23) e entendeu que eu

Ao relatar mudanças, dizer explicitamente o que é arquivo existente que eu alterei (de quem é, tamanho, o que mudou nele) e o que é ferramenta nova que eu criei. Não basta listar nomes de arquivo com "refactor(parser)" e "+102/−37 linhas".

**Why:** em 2026-11-23, depois do meu fechamento do PR #6 do CRG, o dono perguntou "eu vi vc fazer essa ferramenta `parser.py`, me explica por quê?". `parser.py` é o núcleo do CRG herdado do upstream; eu só reorganizei 49 linhas dele, e a ferramenta criada era `tools/js_form_probe.py`. A pergunta veio depois de uma sequência em que ele já tinha cobrado scripts fora do `dex-toolsbook`, então a ambiguidade gerou desconfiança a mais. (Interpretação minha: não foi correção explícita; o dono só pediu explicação.)

**How to apply:** em veredito e fechamento, abrir a parte de código com uma frase por item: "alterei X (existente, de Y): o quê e por quê" e "criei Z: para quê". Explicar em linguagem comum primeiro (o que o arquivo faz) e só depois o detalhe técnico.

Relaciona: [[sonda-e-script-de-prova-seguem-dex-toolsbook]], [[crg-pr6-effect-fn-revisao-20261123]].

#auto-memory/feedback

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^relatorios-distinguem-arquivo-alterado-de-ferrament-2d1ead95e14a-content
