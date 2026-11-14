---
fotografia_id: 20261114-crg-cjs-path
revision: 201f3c0a9627b282fc7eba4e03646179c3ddd7a3
observed_at: 2026-11-14T11:30:53.045565-03:00
---

# Decisões de adoção da CLI do PATH

↩ [Mapas](INDEX.md)

| Decisão | Origem | Aceite observado |
| --- | --- | --- |
| Usar o CRG no Codex por CLI. | Pedido do dono após rastrear o erro 32 ao `serve` iniciado pelo Codex. | Registros removidos e zero processos `serve` após reinício. |
| Instalar o wheel pelo gerenciador da instalação habitual. | GO do dono condicionado à liberação dos executáveis e à preservação do rollback. | Abertura exclusiva, instalação offline e hash do parser conferido. |
| Validar o recorte original e o commit atual em bancos novos. | O Git atual ganhou dois arquivos `.cjs` desde o recorte de 19. | 19/19 e 21/21, igualdade nominal, integridade SQLite e SHA do índice igual ao Git. |

[Trilho](../PLAN-TASKS/2026-11-13-crg-cjs.md#continuação-da-adoção-habitual) · [Prova](../receipts/crg-cjs-runtime-20261113/adopt-path-verdict.json)
