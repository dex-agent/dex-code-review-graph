---
implementation_version: v2
layer: L2
slug: temp-da-maquina-e-staging-implicita-inventario-no-r-d920dcb4ee15
tags:
  - "#auto-memory/project"
---

# temp-da-maquina-e-staging-implicita-inventario-no-registry

Espelho da auto-memory do host ZCode (arquivo temp-da-maquina-e-staging-implicita-inventario-no-registry.md, tipo project).

A higiene de repo (dex-higiene-scan --root) não enxerga a Temp da

`scan-hygiene.py --root <repo>` só olha dentro do repo. A Temp da máquina (`%LOCALAPPDATA%\Temp`; no Git Bash desta máquina `TEMP` e `TMP` são a mesma pasta, `Temp\16`) é onde as sessões deixam script e evidência: em 2026-11-23 tinha 158 itens com sha256 (144 scripts de sessão e 14 temporários de aplicativo), nenhum marcado `Reuso:` ou `Descartável:`, e cerca de 11 GB em pastas.

**Why:** o dono pediu "limpar a casa" e a evidência de blocos fechados do CRG (15 arquivos do merge 2.4.0-dex) estava solta na Temp, fora de qualquer livro. Dos 144 scripts lidos, só 7 eram ferramenta reutilizável, e 2 delas não tinham outra cópia na máquina desde julho.

**O que já existe (medido, não presumir de novo):**
- `~/.agents/skills/.agents/receipts/higiene-temp-maquina-20261123/`: `INVENTARIO.json`, `TRIAGEM.json` e `TRIAGEM.md` (contrato `triagem.temp-maquina.v1`) e `reutilizaveis/` com cópia durável das 2 ferramentas (`create-dex-memory-pre-hygiene-backup.ps1`, do dex-memoria; `preserve-worktree-state.mjs`, sem dono).
- Destinos da triagem: 138 para a lixeira com manifesto, 18 em voo (mtime 22–23/11, não tocar), 2 para promover. Cinco ferramentas já têm versão viva mais nova (não promover duplicata).
- Fila por dono: ISSUE-LOCAL-0062 do registry. Em 2026-11-23 os recibos e o item estavam em disco e sem commit no registry.
- Do CRG: os 15 arquivos recolhidos para `.agents/receipts/CRG-240DEX-MERGE-20261115/`; os originais saíram da Temp com registro em `.agents/LIXEIRA/`. Ficaram 2,2 GB de índice derivado e venv esperando palavra do dono (PENDENTES `CRG-RESIDUO-FORA-DO-REPO-20261123`).

**How to apply:**
- Pedido de limpeza ou fechamento: a higiene do repo não basta; conferir a Temp da máquina. Se o inventário já existe, partir da triagem em vez de retribuir.
- Ordem que funcionou: inventariar com hash (read-only) -> classificar por leitura -> copiar só o que é do próprio repo -> item por dono no TRACKER -> só então apagar original, depois de cópia conferida.
- Nunca mover nem apagar arquivo de outra janela (mtime recente) ou de outro dono; o que é de outro dono vira item no tracker dele.
- O livro e o motor do `dex-toolsbook` do registry podem estar em edição por outra janela: `git status` lá antes de mexer.
- Cinco arquivos do bloco de 2026-11-01 do registry têm e-mails pessoais: manifesto de lixeira só com metadados saneados.
- gatilho: TEMP-MAQUINA-STAGING-IMPLICITA

Relaciona: [[artefato-em-temp-exige-destino-duravel-no-mesmo-bloco]] (o lado da criação do artefato), [[hash-em-git-bash-leitura-binaria-nao-sha256sum-cut]], [[sonda-e-script-de-prova-seguem-dex-toolsbook]].

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^temp-da-maquina-e-staging-implicita-inventario-no-r-d920dcb4ee15-content
