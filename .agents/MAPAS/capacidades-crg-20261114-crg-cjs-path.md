---
fotografia_id: 20261114-crg-cjs-path
revision: 201f3c0a9627b282fc7eba4e03646179c3ddd7a3
observed_at: 2026-11-14T11:30:53.045565-03:00
---

# Cobertura CommonJS pela CLI do PATH

↩ [Mapas](INDEX.md)

| Consumidor | Gatilho | Resultado observado | Limite |
| --- | --- | --- | --- |
| Mantenedor CRG | Instalar o wheel offline pelo `uv` | O hash do parser instalado coincide com o wheel. As versões das dependências foram comparadas com as constraints do rollback. | CLI 2.3.7 no Windows. |
| Revisor Dex WhatsApp | `build` e `status --json` em dois bancos novos | Git e SQLite concordam nos caminhos e na classificação JavaScript: 19/19 no commit original e 21/21 no atual. | Snapshots dos arquivos `.cjs` dos dois commits. |

[Veredito da adoção](../receipts/crg-cjs-runtime-20261113/adopt-path-verdict.json)
