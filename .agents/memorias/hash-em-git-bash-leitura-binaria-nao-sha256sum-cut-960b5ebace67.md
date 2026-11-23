---
implementation_version: v2
layer: L2
slug: hash-em-git-bash-leitura-binaria-nao-sha256sum-cut-960b5ebace67
tags:
  - "#auto-memory/reference"
---

# hash-em-git-bash-leitura-binaria-nao-sha256sum-cut

Espelho da auto-memory do host ZCode (arquivo hash-em-git-bash-leitura-binaria-nao-sha256sum-cut.md, tipo reference).

Reincidência (2026-11-23) da armadilha SHA256SUM-BARRA-ESPURIA, já

`sha256sum` (coreutils) escapa nome de arquivo que contém barra invertida e imprime uma `\` antes do hash: `\<hash> *C:\Users\...`. Um `cut -d' ' -f1` devolve `\hash`, que nunca é igual ao hash limpo do outro lado. Em 2026-11-23 isso acusou 15 falsos "DIFERENTE" entre os originais da Temp e as cópias recolhidas; a leitura binária em Python deu 15 iguais.

**Why:** eu ia apagar os originais da Temp a partir dessa comparação. O alarme era do comparador, não dos arquivos. E a casa já conhecia a armadilha: memória global `SHA256SUM-BARRA-ESPURIA` (2026-11-19) e ficha 5W2H no GATILHOS-VIVOS do registry. Esta foi a segunda instância medida; a primeira tinha sujado o `skill_md_sha256` do CAPACITY de dex-locate-memories. Eu tropecei de novo porque este projeto não tinha ponteiro para a ficha e eu não consultei o hub do registry antes de comparar hash.

**How to apply:**
- Para comparar dois arquivos por hash em Git Bash: leitura binária em Python (`hashlib.sha256(open(p, "rb").read()).hexdigest()`), ou caminho no formato `/c/Users/...`. `sha256sum -c manifesto` serve para conferir cópias contra hashes anotados com caminho relativo.
- Todo alarme de comparador nasce com controle positivo: um par de arquivos diferentes precisa ser acusado antes de o resultado valer (regra-mãe no AGENTS global: `REVISAO-MINIMA-1-OLHADA`, emenda de 2026-11-23).
- Armadilha irmã, da mesma ficha: escape de barra em `python -c` chamado pelo bash gera caractere de form feed invisível (chr 12) no texto gravado. Conferir o conteúdo gravado com `rg`/`od`, não só o exit code.
- Regra já vacinada que reincide não pede memória nova: pede ponteiro no ponto de uso e gate. A segunda instância está em item do TRACKER do registry (ISSUE-LOCAL-0063).
- gatilho: SHA256SUM-BARRA-ESPURIA

Relaciona: [[temp-da-maquina-e-staging-implicita-inventario-no-registry]], [[dado-herdado-de-resumo-e-hipotese-reexecutar]], [[regra-repetida-pelo-dono-vira-gate-nao-novo-id]].

#auto-memory/reference

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^hash-em-git-bash-leitura-binaria-nao-sha256sum-cut-960b5ebace67-content
