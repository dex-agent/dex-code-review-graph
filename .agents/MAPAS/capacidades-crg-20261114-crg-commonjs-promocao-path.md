---
fotografia_id: 20261114-crg-commonjs-promocao-path
revision: '56986f7 + wheel SHA-256 7f2f9b60802b253739c6851ee7d84e3b970a5cd9636eab800e831f72b7e051a0'
observed_at: 2026-11-14T14:30:34.1993866-03:00
---

# CLI habitual após a promoção CommonJS

↩ [Mapas](INDEX.md)

| Capacidade | Resultado observado |
| --- | --- |
| Reinstalar versão anterior | Mesmo parser, mesmas 126 versões, zero associação direta de install. |
| Reconhecer o artefato instalado | Hash do parser instalado igual ao do wheel validado. |
| Consultar associação direta | Uma aresta de install para distribution.test.cjs:4 pela CLI do PATH e SQLite descartável. |
| Comparar cobertura do snapshot | 21/21 arquivos .cjs no Git, HEAD indexado igual a eb7d95b. |

[Promoção](../receipts/crg-commonjs-path-20261114/promotion.json) · [Aceite](../receipts/crg-commonjs-path-20261114/acceptance.json)
