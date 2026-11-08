# ACTIVE — code-review-graph (casa)

- Ultima atualizacao: 2026-11-08.
- Fechamento atual: checklist 3/3, flow completo e verdict `vrd_20261108131605649_0126_0025` pronto com ressalvas. Publicacao Git/Dolt concluida; risco P1 de credencial no ledger.
- Corte atual: [organizar repo privado](PLAN-TASKS/2026-11-08-crg-repo-privado-higiene.md), bead `crg-pr9` fechado. Repositorio `dex-agent/dex-code-review-graph` privado, commit organizador `e326cfd` publicado e readback Git/API igual. Remotos `origin` da casa e `upstream` original. Dolt push concluido.
- Estado local separado por `.gitignore`; backups, runtime e grafos historicos preservados. Organizacao em [edicao Dex](../docs/EDICAO-DEX.md). Debitos vivos em [PENDENTES](PENDENTES.md).

- Corte 2026-11-07: recorte do diff corrigido no analisador comum. RED 2/2 reproduzido, GREEN 2/2, suíte 38/38 e consumidores verificados em índice isolado. [Trilho](PLAN-TASKS/2026-11-07-crg-diff-recorte.md) e [mapas](MAPAS/INDEX.md). Owner: mantenedor, promoção do MCP quando publicar a correção.

- Objetivo atual: manter o repo recuperável e operacional após import do
  escritório (CRG + bd + MCP + memória + Graphify).
- Fechamento historico: replicação casa concluída com ressalvas (2026-07-31) —
  detalhe em `.agents/PLAN-TASKS/ACTIVE.md` e laudo
  `.agents/EVIDENCIAS/2026-07-31-code-review-graph-home-replication.md`.
- Proximo corte funcional: promover a correcao para o runtime MCP e provar os dois casos pela ferramenta instalada, apos fechamento desta publicacao. Owner: mantenedor CRG.
- Lembrança quente: `.agents/GATILHOS-VIVOS.md`; runbook: `.agents/napkin.md`.

