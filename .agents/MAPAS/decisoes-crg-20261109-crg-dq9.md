---
fotografia_id: 20261109-crg-dq9
revision: eeb486bd894c16c2db85a803560d26ddce3c4968
observed_at: 2026-11-09
---

# Decisões da adoção do índice

- **D-01** O mantenedor escolheu gerar o candidato no mesmo checkout e em armazenamento isolado. A imagem partiu do backup para seguir o comportamento do rebuild nativo e preservar embeddings existentes. Um candidato construído do zero passou no controle funcional, mas ficou sem tabela de embeddings. [Candidato adotado](../receipts/crg-adocao-indice-php/candidate.json).
- **D-02** O executor promoveu pelo SQLite sob lock exclusivo, com precondições de hash e caminho. O ensaio recuperou a imagem anterior depois de uma alteração deliberada. [Backup](../receipts/crg-adocao-indice-php/backup.json).
- **D-03** O aceite de consumo passou pela CLI sem overrides e pelo SQL da associação qualificada. A regressão PHP usou os dois repositórios isolados. [Readback](../receipts/crg-adocao-indice-php/promotion.json).

[Trilho](../PLAN-TASKS/2026-11-09-crg-adocao-indice-php.md).
