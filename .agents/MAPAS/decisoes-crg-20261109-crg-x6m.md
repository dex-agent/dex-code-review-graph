---
fotografia_id: 20261109-crg-x6m
revision: fb9fc22da3d1966f5754d9db7938cd4b0ad8caba
observed_at: 2026-11-09
---

# Decisões sobre resolução PHP

- **D-01** O mantenedor usou identidade de classe declarada e escopo lexical da chamada. Uma classe com o mesmo nome simples em outro namespace fica fora da resolução de um receptor construído.
- **D-02** Enquanto a classe não estiver indexada, o endpoint mantém a evidência de pendência já reconhecida pelo grafo. Isso protege a resolução por nome simples e as consultas de fallback.
- **D-03** A prova de aceite usa CLI e SQLite, com a mesma versão Git para update, repetição e rebuild. A comparação exige ausência de Shipping e presença de Payments com associação direta sem inferência por nome.

[Trilho](../PLAN-TASKS/2026-11-09-crg-x6m-php-homonimos.md) · [Provas](../receipts/crg-x6m/cli.json).
