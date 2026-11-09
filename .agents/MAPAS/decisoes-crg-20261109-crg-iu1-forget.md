---
fotografia_id: 20261109-crg-iu1-forget
revision: aca7f74688daa12d52982ff6f99e69fc12b0745b
observed_at: 2026-11-09
---

# Decisões do corte forget

| Decisão | Motivo | Prova |
| --- | --- | --- |
| Portar a fixture em commit próprio | Separar o falso RED da fixture do defeito observado no executável | [Resultado das fixtures](../receipts/crg-iu1-forget/fixtures.xml) |
| Recuperar a grafia do diretório existente no Windows | O prefixo lexical ignorava a identidade confirmada pelo filesystem | [RED](../receipts/crg-iu1-forget/red.json) e [GREEN](../receipts/crg-iu1-forget/green-windows.json) |
| Preservar o separador no limite e as chaves SQLite | Evitar selecionar `pkg_extra` e preservar a remoção das chaves realmente indexadas | [Windows](../receipts/crg-iu1-forget/green-windows.json) e [Ubuntu](../receipts/crg-iu1-forget/green-ubuntu.json) |
| Incluir o módulo completo no job Windows existente | O job seletivo deixava o módulo fora | [Workflow](../../.github/workflows/ci.yml) |

Owner mantenedor CRG. [Trilho](../PLAN-TASKS/2026-11-09-crg-iu1-forget.md).
