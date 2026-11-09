---
fotografia_id: 20261109-crg-dq9
revision: eeb486bd894c16c2db85a803560d26ddce3c4968
observed_at: 2026-11-09
---

# Capacidade operacional do índice persistente

| Capacidade | Prova | Limite |
| --- | --- | --- |
| Restaurar a imagem anterior | [Backup ensaiado](../receipts/crg-adocao-indice-php/backup.json), integridade e hash lógico idênticos | Arquivo SQLite local, fora do Git |
| Reconstruir e preservar estado auxiliar | [Candidato](../receipts/crg-adocao-indice-php/candidate.json), 4.745 embeddings antes e depois e 4.164 vetores estáveis iguais em bytes | Vetores de fontes alteradas podem exigir nova geração |
| Adotar sob exclusão SQLite | [Banco ativo](../receipts/crg-adocao-indice-php/promotion.json), segunda conexão recebeu SQLITE_BUSY | Revisão fixada durante a operação |
| Separar aceites | [Fixtures PHP](../receipts/crg-adocao-indice-php/php-fixtures.json) e controle real de references_to | Fixtures executadas em repositórios separados |

Owner mantenedor CRG. [Trilho](../PLAN-TASKS/2026-11-09-crg-adocao-indice-php.md).
