---
implementation_version: v2
layer: L2
slug: espelho-auto-memory-mjs-ferramenta-canonica-6c0a07084f49
tags:
  - "#auto-memory/reference"
---

# espelho-auto-memory-mjs-ferramenta-canonica

Espelho da auto-memory do host ZCode (arquivo espelho-auto-memory-mjs-ferramenta-canonica.md, tipo reference).

Espelho de auto-memory para o dex-memoria tem ferramenta canônica

Auto-memory do ZCode vira memória do projeto pela ferramenta canônica, não por memória escrita à mão. Com CWD no repo:

```
node "$USERPROFILE/.agents/skills/consciencia-memorias/scripts/espelhar-auto-memory.mjs" --memory-dir "C:/Users/Administrator/.zcode/cli/memories/projects/code-review-graph-c2beb1d341528cea/memory" --dry-run --json
# depois --apply --json --out .agents/receipts/espelho-auto-memory.json
python -B "$USERPROFILE/.agents/skills/consciencia-memorias/scripts/validate-memory-batch.py" --root .agents --l1 lembranca.md --dest-dir memorias --slugs <nomes.md, separados por vírgula>
```

Os arquivos novos em `.agents/memorias/` e as linhas novas em `.agents/lembranca.md` entram no próximo commit.

**Por que:** virou canônica em 2026-11-23 (Trilho `2026-11-23-espelho-auto-memory-mjs`, ISSUE-LOCAL-0043). Ela grava com o slug igual ao do arquivo do host, que é a mesma régua de prefixo-3 do passo `garimpo` do `scan-fechamento.py`. No fechamento do PR #6 o fiscal achou 27 auto-memories sem cópia: os espelhos que eu tinha escrito à mão tinham outros nomes e não contavam.

**Como aplicar:**
- Ao fechar qualquer bloco em que uma auto-memory foi criada, rodar o espelho antes do scan de fechamento.
- O espelho é cópia do momento. Se a auto-memory mudar depois, corrigir também o arquivo em `.agents/memorias/` (o espelho pula por prefixo e não atualiza).
- Espelho vai para o repo no push. No CRG o repo é público: varrer por credencial antes.
- O passo `gatilhos_vivos` do fiscal só lê linha na forma `- gatilho: NOME` na auto-memory, e o `NOME` precisa estar em `.agents/GATILHOS-VIVOS.md`; menção no meio da frase não conta.
- Para o fechamento formal, passar `--block-id`, `--workflow-review` e `--block-files`; sem eles as superfícies 13 a 15 ficam `n-a`. Candidato `create` gera aviso R16, que só fecha com ficha 5W2H no livro ou captura da receita.

Relaciona: [[artefato-em-temp-exige-destino-duravel-no-mesmo-bloco]], [[crg-pr6-effect-fn-revisao-20261123]].

#auto-memory/reference

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^espelho-auto-memory-mjs-ferramenta-canonica-6c0a07084f49-content
