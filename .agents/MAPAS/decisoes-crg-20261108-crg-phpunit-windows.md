---
fotografia_id: 20261108-crg-phpunit-windows
revision: 92fdfe052c2d97755659d1c81a3a1593e204c1c6
observed_at: 2026-11-08
---

# Decisões do corte PHPUnit Windows

**D-01** O dono aprovou o corte PHPUnit de `crg-iu1`. O mantenedor ajustou a representação do separador na fronteira de classificação do parser, preservando a identidade nativa gravada. A validação exigiu teste direto via executável, aresta SQLite e controle de método de produção.

**D-02** A etapa Windows da CI passou a selecionar os três IDs PHPUnit que expuseram o erro. O mantenedor verificou a seleção localmente em Python 3.12.

**E-01** A fixture no baseline `c3682ac` provou Function e zero aresta. **E-02** A correção em `92fdfe0` provou Test e uma aresta direta. **E-03** A suíte integral reduziu 27 para 24 falhas, sem IDs novos.

[Trilho](../PLAN-TASKS/2026-11-08-crg-phpunit-windows.md) · [Prova](../receipts/crg-phpunit-windows/summary.json). O bead continua com o mantenedor até a reconciliação Windows antes do próximo release.
