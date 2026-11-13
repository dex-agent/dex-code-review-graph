---
fotografia_id: 20261113-crg-cjs
revision: b7f4e5e mais diff local identificado no recibo
observed_at: 2026-11-13
---

# Decisões para reconhecer `.cjs`

O responsável pelo efeito é o mantenedor CRG. Decisões e observações deste corte são de 13/11/2026.

| ID | Origem e escolha | Aceite e estado |
| --- | --- | --- |
| D-01 | A arqueologia reportou exit 0 com 0/19. Medir igualdade de conjuntos pelo Git e SQLite, com um controle de staging. | 19/19 e zero staging provados no wheel. [Inventário](../receipts/crg-cjs-20261113/proof.json). |
| D-02 | O `.cjs` ausente ligava ao `.js` homônimo. Reusar o parser JavaScript e suprimir a troca de extensão apenas para o caminho `.cjs` explícito, preservando busca por índice de diretório. Depende da reprodução dos casos. | Quatro REDs históricos e suíte verde. [Evidências](../EVIDENCIAS/2026-11-13-crg-cjs.md) · [Teste](../../tests/test_commonjs_imports.py). |
| D-03 | A versão textual coincide entre os executáveis. Aceitar o wheel pelo hash da fonte e leitura do banco. | Instalação isolada e rollback verificados. A adoção habitual foi autorizada depois, com executáveis em uso. [Prova](../receipts/crg-cjs-20261113/proof.json) · [Estado da adoção](../EVIDENCIAS/2026-11-13-crg-cjs.md). |
