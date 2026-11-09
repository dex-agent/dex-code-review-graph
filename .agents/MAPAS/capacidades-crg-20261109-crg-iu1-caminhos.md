---
fotografia_id: 20261109-crg-iu1-caminhos
revision: f825c2597e6bfba1a489a8b96856a9f4aa1a1f8b
observed_at: 2026-11-09
---

# Provas de caminho PHP e Rust em Windows e Ubuntu

| Capacidade | Prova | Limite |
| --- | --- | --- |
| Validar o destino qualificado dos três testes | [Baseline](../receipts/crg-iu1-caminhos/baseline.json), [contraprovas](../receipts/crg-iu1-caminhos/change.json) e [JUnit comparado](../receipts/crg-iu1-caminhos/focused.json) | Três IDs e quatro controles, em índices isolados |
| Executar os três IDs na CI Windows | [Nove jobs e SHA exato](../receipts/crg-iu1-caminhos/comparison.json) | O job Windows usa uma seleção da suíte |
| Medir a regressão por conjunto de IDs | [Comparação da suíte Windows](../receipts/crg-iu1-caminhos/comparison.json), 24 → 21, zero novos | 21 falhas preexistentes em crg-iu1, sendo 13 Julia |

Owner mantenedor CRG. [Trilho](../PLAN-TASKS/2026-11-09-crg-iu1-caminhos-php-rust.md).
