# ACTIVE — code-review-graph (casa)

- Ultima atualizacao: 2026-11-08.
- Próximo corte do mantenedor CRG: `crg-k4q` antes da próxima consulta ao índice persistente. Reproduzir update que alinha o SHA sem reclassificar e provar a rota de frescor.
- [Classificação por caminho](PLAN-TASKS/2026-11-08-crg-test-path.md): commit `3fb1ab3` publicado. PHP e TypeScript em `contest/` e sob ancestral externo `tests/` perderam associações indevidas, com controles positivos preservados. [Provas e CI](receipts/crg-test-path/comparison.json).
- Fechamento atual: PHPUnit Windows, checklist 4/4 e veredito `vrd_20261109005555936_0268_0205` pronto com ressalvas. O risco P1 histórico de credencial segue no ledger.
- Corte atual: [organizar repo privado](PLAN-TASKS/2026-11-08-crg-repo-privado-higiene.md), bead `crg-pr9` fechado. Repositorio `dex-agent/dex-code-review-graph` privado, commit organizador `e326cfd` publicado e readback Git/API igual. Remotos `origin` da casa e `upstream` original. Dolt push concluido.
- Estado local separado por `.gitignore`; backups, runtime e grafos historicos preservados. Organizacao em [edicao Dex](../docs/EDICAO-DEX.md). Debitos vivos em [PENDENTES](PENDENTES.md).

- Corte 2026-11-07: recorte do diff corrigido no analisador comum. RED 2/2 reproduzido, GREEN 2/2, suíte 38/38 e consumidores verificados em índice isolado. [Trilho](PLAN-TASKS/2026-11-07-crg-diff-recorte.md) e [mapas](MAPAS/INDEX.md).

- Objetivo atual: evoluir a edicao Dex com a [CLI como interface principal](../docs/EDICAO-DEX.md#direcao-do-produto).
- Fechamento historico: replicação casa concluída com ressalvas (2026-07-31) —
  detalhe em `.agents/PLAN-TASKS/ACTIVE.md` e laudo
  `.agents/EVIDENCIAS/2026-07-31-code-review-graph-home-replication.md`.
- Corte funcional atual: [recorte na CLI](PLAN-TASKS/2026-11-08-crg-cli-recorte.md). `detect-changes --files` provado em Git/JSON no commit `1e12485` e publicado. Owner: mantenedor CRG.
- Prova real da CLI: [Trilho](PLAN-TASKS/2026-11-08-crg-cli-diff-real.md), recorte 1/1 em 573580b e índice de teste no SHA alvo. A consulta de testes omitiu o teste do ramo `references_to`.
- Corte de reexportações Python: [Trilho](PLAN-TASKS/2026-11-08-crg-python-reexports.md), checklist 4/4 e prova CLI no alvo histórico. A suíte Windows mantém 27 falhas do baseline, em `crg-iu1`.
- Índice persistente reconstruído pelo executável corrigido. O teste de `references_to` aparece como associação direta. [Trilho](PLAN-TASKS/2026-11-08-crg-indice-persistente.md)
- [PHPUnit no Windows](PLAN-TASKS/2026-11-08-crg-phpunit-windows.md): associação direta provada pela CLI e pelo SQLite em `92fdfe0`. A suíte caiu de 27 para 24 falhas, sem IDs novos. O mantenedor retoma `crg-iu1` antes do próximo release Windows.
- Lembrança quente: `.agents/GATILHOS-VIVOS.md`; runbook: `.agents/napkin.md`.

