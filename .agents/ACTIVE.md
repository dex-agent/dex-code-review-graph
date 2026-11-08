# ACTIVE — code-review-graph (casa)

- Ultima atualizacao: 2026-11-08.
- Fechamento atual: checklist 3/3, flow completo e verdict `vrd_20261108131605649_0126_0025` pronto com ressalvas. Publicacao Git/Dolt concluida; risco P1 de credencial no ledger.
- Corte atual: [organizar repo privado](PLAN-TASKS/2026-11-08-crg-repo-privado-higiene.md), bead `crg-pr9` fechado. Repositorio `dex-agent/dex-code-review-graph` privado, commit organizador `e326cfd` publicado e readback Git/API igual. Remotos `origin` da casa e `upstream` original. Dolt push concluido.
- Estado local separado por `.gitignore`; backups, runtime e grafos historicos preservados. Organizacao em [edicao Dex](../docs/EDICAO-DEX.md). Debitos vivos em [PENDENTES](PENDENTES.md).

- Corte 2026-11-07: recorte do diff corrigido no analisador comum. RED 2/2 reproduzido, GREEN 2/2, suíte 38/38 e consumidores verificados em índice isolado. [Trilho](PLAN-TASKS/2026-11-07-crg-diff-recorte.md) e [mapas](MAPAS/INDEX.md).

- Objetivo atual: evoluir a edicao Dex com a [CLI como interface principal](../docs/EDICAO-DEX.md#direcao-do-produto).
- Fechamento historico: replicação casa concluída com ressalvas (2026-07-31) —
  detalhe em `.agents/PLAN-TASKS/ACTIVE.md` e laudo
  `.agents/EVIDENCIAS/2026-07-31-code-review-graph-home-replication.md`.
- Corte funcional atual: [recorte na CLI](PLAN-TASKS/2026-11-08-crg-cli-recorte.md). `detect-changes --files` provado em Git/JSON no commit `1e12485`. Publicacao em andamento. Owner: mantenedor CRG.
- Lembrança quente: `.agents/GATILHOS-VIVOS.md`; runbook: `.agents/napkin.md`.

