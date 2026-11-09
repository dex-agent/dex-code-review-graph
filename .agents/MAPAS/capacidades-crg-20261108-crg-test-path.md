---
fotografia_id: 20261108-crg-test-path
revision: 3fb1ab318f9c92f5bbb5d1d7f9b4462a24a5ff04
observed_at: 2026-11-08
---

# Capacidades do CRG no corte de classificação por caminho

O mantenedor CRG responde pela classificação na construção do grafo. O consumidor consulta testes pela CLI.

| Cenário | Antes | Depois | Prova |
| --- | --- | --- | --- |
| PHP em `contest/` ou checkout sob `tests/` | Test e uma associação direta por cenário | Function e zero associações | Nós, arestas e JSON da CLI |
| TypeScript com callback `describe` nos mesmos caminhos | Test sintético e uma associação direta por cenário | Zero nós Test sintéticos e zero associações | Nós, arestas e JSON da CLI |
| PHP em `tests/` e TS em `__tests__/` na raiz | Uma associação direta por cenário | Uma associação direta por cenário, com identidade nativa | Nós, arestas e JSON da CLI |

A prova usa o executável Windows em bancos isolados, com os mesmos bytes por linguagem. O [Trilho](../PLAN-TASKS/2026-11-08-crg-test-path.md) tem os demais controles. A [matriz A/B](../receipts/crg-test-path/cli.json) identifica o parser pelo SHA-256. O índice persistente anterior exige checagem própria antes de ser usado, rastreada em `crg-k4q`.
