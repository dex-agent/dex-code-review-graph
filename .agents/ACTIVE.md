# ACTIVE — code-review-graph (casa)

- 2026-11-13 — [E2E da CLI CommonJS](PLAN-TASKS/2026-11-13-crg-cjs-e2e.md), bead `crg-09r`. Doze comandos saíram 0, incluindo recorte de diff e segunda execução sem duplicação. A adoção habitual segue bloqueada por uso concorrente.

- 2026-11-13 — [Reconhecimento `.cjs`](PLAN-TASKS/2026-11-13-crg-cjs.md), bead `crg-4t2`. A adoção local foi autorizada. Sete processos `serve` do Codex mantêm o launcher e o Python habituais em uso (Windows 32). O wheel isolado repetiu 19/19 caminhos e 24 importações relativas explícitas em um índice novo. [Prova e bloqueio](EVIDENCIAS/2026-11-13-crg-cjs.md).

- Ultima atualizacao: 2026-11-13.
- [Modo efetivo no uninstall](PLAN-TASKS/2026-11-09-crg-iu1-uninstall-mode.md) — `f5fb25d`, CI 9/9 e uninstall Windows 46/46. A suíte integral Windows zerou as falhas, com 2.326 aprovados. Bead `crg-iu1` fechado. [Veredito](receipts/crg-iu1-uninstall-mode/verdict.json).
- [Pares exatos de eventos Spring](PLAN-TASKS/2026-11-09-crg-iu1-spring-events.md) — `d22e6d6`, CLI e SQLite confirmam os dois pares, CI 9/9 e Spring Windows 6/6. Resta um ID histórico na suíte integral. [Veredito](receipts/crg-iu1-spring-events/verdict.json).
- [Referências HCL com caminhos nativos](PLAN-TASKS/2026-11-09-crg-iu1-hcl-references.md) — `d6336d2` corrige a expectativa da fixture. CLI e SQLite confirmam as duas arestas pelos IDs. CI 9/9, módulo HCL Windows 3/3 e dois IDs históricos restantes na suíte integral. [Veredito](receipts/crg-iu1-hcl-references/verdict.json).
- [Identidade da aresta CONTAINS no dbt](PLAN-TASKS/2026-11-09-crg-iu1-dbt-contains.md) — `b02a4ba` corrige a expectativa de caminho nativo e verifica o nó pelo ID bruto. CI 9/9, módulo dbt Windows 9/9. A suíte integral Windows fica com três IDs históricos. [Veredito](receipts/crg-iu1-dbt-contains/verdict.json).
- [Raiz explícita com índice externo](PLAN-TASKS/2026-11-09-crg-iu1-raiz-externa.md) — `f145ca8` reconhece o vínculo registrado na CLI e `61ff0da` corrige o launcher dos testes. CI 9/9, Windows 5/5 no passo dedicado, quatro falhas conhecidas na suíte integral. [Veredito](receipts/crg-iu1-raiz-externa/verdict.json).
- [Seleção exata do forget no Windows](PLAN-TASKS/2026-11-09-crg-iu1-forget.md): `aca7f74` corrige `forget PKG` com prova no executável e SQLite. CI 9/9, módulo Windows 13/13, suíte integral Windows 8 → 5 IDs conhecidos. Próxima retomada de `crg-iu1`: resolução explícita de repositório sem marcadores antes do release Windows. [Saldo por ID](receipts/crg-iu1-forget/comparison.json).
- [Portabilidade dos testes Julia](PLAN-TASKS/2026-11-09-crg-iu1-julia.md): `9f1f19b`, 27/27 em cada sistema e na CI Windows. A suíte integral caiu de 21 para 8 falhas, sem novos IDs. O mantenedor retoma `crg-iu1` pelos três casos de seleção do comando `forget` antes do próximo release Windows. [Comparação por ID](receipts/crg-iu1-julia/comparison.json).
- [Caminhos PHP/Rust no Windows e Ubuntu](PLAN-TASKS/2026-11-09-crg-iu1-caminhos-php-rust.md): `f825c25`, 7/7 em cada sistema e CI 9/9. A suíte Windows passou de 24 a 21 falhas, sem novos IDs. O mantenedor retoma `crg-iu1` pelo primeiro caso de identidade Julia antes do próximo release Windows. [Comparação por ID](receipts/crg-iu1-caminhos/comparison.json).
- [Adoção da correção PHP no índice persistente](PLAN-TASKS/2026-11-09-crg-adocao-indice-php.md): banco habitual reconstruído em `eeb486b`, backup íntegro e restauração ensaiada. [Readback da CLI e SQLite](receipts/crg-adocao-indice-php/promotion.json). O mantenedor retoma `crg-iu1` antes do próximo release Windows.
- [Resolução PHP de homônimos](PLAN-TASKS/2026-11-09-crg-x6m-php-homonimos.md): produto `fb9fc22`. Duas fixtures com zero arestas para Shipping e paridade de update e rebuild para Payments. [Prova pela CLI e pelo SQLite](receipts/crg-x6m/cli.json).
- [Frescor semântico do índice](PLAN-TASKS/2026-11-08-crg-k4q-frescor-indice.md): update alinhou o SHA sem reclassificar, rebuild no mesmo SHA recuperou a aresta direta. A rota de adoção está nos [gatilhos vivos](GATILHOS-VIVOS.md#staleness-artefatos-derivados).
- [Classificação por caminho](PLAN-TASKS/2026-11-08-crg-test-path.md): commit `3fb1ab3` publicado. PHP e TypeScript em `contest/` e sob ancestral externo `tests/` perderam associações indevidas, com controles positivos preservados. [Provas e CI](receipts/crg-test-path/comparison.json).
- Fechamento atual: adoção no índice persistente, checklist 5/5 e veredito `vrd_20261109061157643_0378_0345` pronto com ressalvas. O risco P1 histórico de credencial segue no ledger.
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

