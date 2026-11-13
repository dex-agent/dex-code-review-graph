---
fotografia_id: 20261113-crg-cjs
revision: b7f4e5e mais diff local identificado no recibo
observed_at: 2026-11-13
---

# Capacidades observadas no recorte `.cjs`

Ambiente Windows, executável instalado do wheel local. Owner mantenedor CRG.

| Consumidor | Gatilho | Resultado e oráculo | Limite |
| --- | --- | --- | --- |
| Revisor Dex WhatsApp | `build` no corpus descartável | 19 caminhos do Git = 19 nós `File` JavaScript no SQLite. Uma cópia de staging rastreada na fixture foi excluída pelo ignore. | Corpus de 19 fontes com hashes conferidos. |
| Revisor CommonJS | `query imports_of` | Caminho explícito existente ganha aresta. Ausências preservam o literal. SQLite e Git corroboram 24 pares do corpus. | Resolução estática, incluindo os casos protegidos pelos testes. |
| Mantenedor da CLI | `update` após alteração de `app.cjs` | `status --json` coincide com Git. SQLite contém a nova função exportada e sua chamada. | Um caminho alterado. Adoção de cobertura preexistente foi provada por `build`. |

[Prova e identidade](../receipts/crg-cjs-20261113/proof.json) · [Trilho](../PLAN-TASKS/2026-11-13-crg-cjs.md).
