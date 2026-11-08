---
fotografia_id: 20261108-crg-cli-recorte
observed_at: '2026-11-08T16:01:23-03:00'
revision: 1e12485776652e2812bbfebf09a48bc1d8e73190
owner: mantenedor CRG
---

# Capacidades da CLI no recorte de diff

Escopo Windows, Python 3.13 e Git real. Cada fixture usa build e executavel
da edicao Dex com banco isolado. A API, o MCP instalado e o indice
persistente ficam fora desta fotografia.

| Consumidor e gatilho | Resultado observado | Oracle |
| --- | --- | --- |
| Revisor chama detect-changes --files A com A+B alterados | JSON contem somente a em A; a outra funcao em A tambem fica fora do hunk. | Git --name-only e patch com hunk da linha 2, confrontados com JSON. |
| Revisor chama o mesmo comando com apenas B alterado | JSON tem zero simbolos, fluxos, lacunas e risco. | Git mostra B e patch de A vazio. |
| A tem espaco e acento | Os mesmos resultados com o nome preservado do inventario ao JSON. | Git ls-files -z e os dois casos repetidos. |

[Prova pelo executavel](../receipts/crg-cli-recorte/green-final.txt) e
[Trilho](../PLAN-TASKS/2026-11-08-crg-cli-recorte.md). A fotografia de
2026-11-07 observava outros consumidores e excluia CLI.
