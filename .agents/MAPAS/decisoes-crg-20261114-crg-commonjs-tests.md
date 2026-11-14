---
fotografia_id: 20261114-crg-commonjs-tests
revision: '56986f7 + parser SHA-256 2ca0223c0ef234be3fc4558fb0453c1445b188250d2431a54aac585b50a30115'
observed_at: 2026-11-14T14:13:52.8005364-03:00
---

# Decisões de reconhecimento CommonJS

↩ [Mapas](INDEX.md)

| Decisão | Motivo | Prova |
| --- | --- | --- |
| Classificar extensões .test.cjs e .spec.cjs no detector comum. | O RED mostrou que testes sob src/ ficavam fora. | [RED](../receipts/crg-commonjs-tests-20261114/red.txt) |
| Resolver a origem do runner no escopo lexical. | Alias, função local e sombra não podem compartilhar o critério. | [GREEN](../receipts/crg-commonjs-tests-20261114/green.txt) |
| Conservar a direção de tests_for e comparar executáveis em bancos novos. | O teste de distribuição chama install diretamente, e install chama verify. | [CLI e SQLite](../receipts/crg-commonjs-tests-20261114/proof.json) |
