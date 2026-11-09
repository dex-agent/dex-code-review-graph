---
fotografia_id: 20261109-crg-iu1-forget
revision: aca7f74688daa12d52982ff6f99e69fc12b0745b
observed_at: 2026-11-09
---

# Capacidades observadas do forget

| Capacidade | Consumidor e gatilho | Prova | Limite |
| --- | --- | --- | --- |
| Selecionar a mesma pasta por grafia equivalente | Operador ou automação executa `forget PKG` no Windows | [RED](../receipts/crg-iu1-forget/red.json) e [CLI/SQLite corrigidos](../receipts/crg-iu1-forget/green-windows.json) | Pasta em volume que equipara as grafias |
| Distinguir diretórios que diferem por caixa | Operador executa `forget PKG` no Ubuntu com `pkg` e `PKG` distintos | [CLI/SQLite no Ubuntu](../receipts/crg-iu1-forget/green-ubuntu.json) | Filesystem Linux nativo |
| Medir os testes herdados por ID | Mantenedor roda a suíte Windows integral | [Comparação 8 → 5, zero novos](../receipts/crg-iu1-forget/comparison.json) | Os cinco IDs restantes seguem em `crg-iu1` |

Owner mantenedor CRG. [Trilho](../PLAN-TASKS/2026-11-09-crg-iu1-forget.md).
