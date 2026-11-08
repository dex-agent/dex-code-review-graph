---
fotografia_id: 20261108-crg-python-reexports
observed_at: '2026-11-08T19:43:49-03:00'
revision: 'crg-j6z sobre ad0b736, alvo histórico 573580b'
mode: historico
---

# Decisões históricas da correção de reexportações

| Decisão | Evidência e efeito |
| --- | --- |
| Canonicalizar antes de espelhar as arestas. | O RED apontava para `__init__.py`. A definição real passa a ser compartilhada por `CALLS` e `TESTED_BY`. |
| Preservar dependências de imports relativos. | O SQLite do primeiro teste registrava o nome do símbolo importado no lugar do módulo intermediário. A extração passa a usar o campo `module_name`. |
| Reprocessar dependentes com fonte idêntica. | Mesmo com o import relativo correto, o hash do dependente ocultava uma mudança de destino. O update agora remove a associação antiga. |

[Trilho](../PLAN-TASKS/2026-11-08-crg-python-reexports.md) ·
[RED incremental](../receipts/crg-python-reexports/red-incremental.txt) ·
[GREEN incremental](../receipts/crg-python-reexports/incremental.txt)
