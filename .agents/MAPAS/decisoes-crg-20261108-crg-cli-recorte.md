---
fotografia_id: 20261108-crg-cli-recorte
observed_at: '2026-11-08T16:01:23-03:00'
revision: 1e12485776652e2812bbfebf09a48bc1d8e73190
mode: historico
---

# Decisoes historicas do recorte na CLI

Owner do corte: mantenedor CRG. Fontes: GO do dono, [Trilho](../PLAN-TASKS/2026-11-08-crg-cli-recorte.md), Git e provas pelo executavel.

| ID | Origem e decisao | Efeito observado |
| --- | --- | --- |
| D-01 | O corte anterior moveu a selecao de faixas para o analisador comum. [Historico](decisoes-crg-20261107-crg-diff-recorte.md) | A CLI reutiliza essa politica de faixas. |
| D-02 | Dono priorizou CLI em 016092d e autorizou o recorte. Reusar --files e intersectar a lista descoberta antes do analisador. | Casos A+B e B-only passam pelo executavel. |
| D-03 | RED em caminho com espaco e acento. Corrigir o separador no patch e usar inventario Git delimitado por NUL. | Build inclui o arquivo e a mesma selecao produz JSON correto. |

[RED da opcao](../receipts/crg-cli-recorte/red.txt),
[RED do caminho](../receipts/crg-cli-recorte/red-path.txt) e
[GREEN](../receipts/crg-cli-recorte/green-final.txt). A suite isolada
preserva o controle do ambiente para a resolucao de raizes.
