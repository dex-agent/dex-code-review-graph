---
fotografia_id: 20261109-crg-iu1-caminhos
revision: f825c2597e6bfba1a489a8b96856a9f4aa1a1f8b
observed_at: 2026-11-09
---

# Decisões sobre portabilidade dos testes de caminho

| Decisão | Motivo | Verificação |
| --- | --- | --- |
| Selecionar a fixture PHP pelo arquivo e restringir a mutação à aresta do controller | Os homônimos fazem parte do cenário | [Destino errado rejeitado](../receipts/crg-iu1-caminhos/change.json) |
| Comparar caminho completo e nome qualificado com separador portátil | O separador varia por plataforma, a identidade do alvo continua exata | [Windows e Ubuntu](../receipts/crg-iu1-caminhos/focused.json) |
| Acrescentar os IDs ao job Windows existente | A seleção anterior deixava o corte fora da CI nativa | [CI no SHA publicado](../receipts/crg-iu1-caminhos/comparison.json) |
| Manter crg-iu1 aberto e priorizar o primeiro caso Julia | 13 das 21 falhas restantes aparecem no mesmo arquivo | [Saldo por ID](../receipts/crg-iu1-caminhos/comparison.json) |

O recorte altera testes e workflow. O índice persistente fica sujeito ao check de staleness antes do próximo consumo.
