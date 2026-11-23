---
implementation_version: v2
layer: L2
slug: tamanho-citado-sai-de-uma-medicao-em-bytes-com-unid-d90234c2269a
tags:
  - "#auto-memory/feedback"
---

# tamanho-citado-sai-de-uma-medicao-em-bytes-com-unidade

Espelho da auto-memory do host ZCode (arquivo tamanho-citado-sai-de-uma-medicao-em-bytes-com-unidade.md, tipo feedback).

Regra do chato lapidada em 2026-11-23 (preferência

Todo tamanho citado (MB, GB) em recibo, ledger, livro ou fechamento sai de uma única medição em bytes, com a unidade declarada, e os outros documentos do bloco copiam o mesmo número.

**Why:** em 2026-11-23 a mesma pasta da Temp apareceu como 1,3 GB num documento e 1,4 GB em outro (MiB contra MB decimal), e a venv do mesmo repo como 338 MB e 329 MB, dentro do mesmo bloco de higiene do CRG. Eu achei ao reconferir antes de fechar; ninguém cobrou.

**How to apply:**
- Medir uma vez em bytes (soma de `os.path.getsize` ou `du -sb`) e converter para uma única unidade (MB e GB decimais) antes de escrever o primeiro número.
- Escrever a unidade junto; se o número importa para uma decisão, anotar data e comando da medição.
- Se um segundo documento do bloco citar o mesmo tamanho, copiar o número; não remedir em outra unidade.
- A regra mora no pacote do chato (`apontamento-publico-exige-medicao`, emenda de 2026-11-23), lapidada sem id novo. Recibo do closeout: `valid=true`.
- gatilho: TAMANHO-CITADO-UMA-MEDICAO-EM-BYTES

Relaciona: [[regra-repetida-pelo-dono-vira-gate-nao-novo-id]], [[temp-da-maquina-e-staging-implicita-inventario-no-registry]].

#auto-memory/feedback

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^tamanho-citado-sai-de-uma-medicao-em-bytes-com-unid-d90234c2269a-content
