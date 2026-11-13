# HANDOFF — retomada curta

- 2026-11-13 — O [E2E da CLI CommonJS](PLAN-TASKS/2026-11-13-crg-cjs-e2e.md) já cobre Git, SQLite, consulta pública, recorte e repetição pelo wheel isolado. A prova que falta para adoção é o canário 19/19 pelo launcher habitual depois de liberar os arquivos em uso.

- 2026-11-13 — A adoção habitual do wheel `.cjs` está autorizada. O mantenedor retoma quando os processos `serve` do Codex liberarem o launcher e o Python da instalação habitual. Verifica o acesso exclusivo, usa o wheel conferido e as [constraints de rollback](receipts/crg-cjs-20261113/rollback-constraints.txt), e confirma o hash e o inventário 19/19 em novo índice pelo executável do PATH. [Bloqueio e canário isolado](EVIDENCIAS/2026-11-13-crg-cjs.md).

Ultima atualizacao: 2026-11-13

- [Modo efetivo no uninstall](PLAN-TASKS/2026-11-09-crg-iu1-uninstall-mode.md) — `f5fb25d` e CI 9/9. `crg-iu1` fechado após o saldo integral chegar a zero IDs de falha. Antes de publicar um release Windows, o mantenedor valida o wheel em uma instalação Windows limpa e isolada, conferindo a versão, o executável e um smoke CLI com projeto descartável. [Saldo por ID](receipts/crg-iu1-uninstall-mode/comparison.json) · [Modo efetivo](memorias/crg-uninstall-modo-efetivo.md).

- [Pares exatos de eventos Spring](PLAN-TASKS/2026-11-09-crg-iu1-spring-events.md) — `d22e6d6` e CI 9/9. Antes do próximo release Windows, o mantenedor retoma `crg-iu1` pelo caso uninstall `test_atomic_config_replace_preserves_file_mode`. Medir modo efetivo antes e depois do replace em configuração descartável nos dois sistemas e conferir a preservação do JSON restante. [Saldo por ID](receipts/crg-iu1-spring-events/comparison.json). Para provas WSL, [isolar a venv](memorias/crg-uv-wsl-venv-isolado.md).

- [Referências HCL com caminhos nativos](PLAN-TASKS/2026-11-09-crg-iu1-hcl-references.md) — `d6336d2` e CI 9/9. O mantenedor retoma `crg-iu1` pelo teste Spring de eventos homônimos antes do próximo release Windows. Reproduzir nos dois sistemas e verificar no SQLite `CALLS` de alpha para alpha e de beta para beta, com zero cruzamentos. [Saldo por ID](receipts/crg-iu1-hcl-references/comparison.json).

- [Identidade da aresta CONTAINS no dbt](PLAN-TASKS/2026-11-09-crg-iu1-dbt-contains.md) — a CLI e o SQLite comprovaram o vínculo exato nos dois sistemas. Antes do próximo release Windows, o mantenedor retoma `crg-iu1` pelo teste HCL `test_for_expression_references_are_emitted_for_local_binding` e confere as referências a `var.items` e `var.enabled` pelos IDs brutos. [Saldo por ID](receipts/crg-iu1-dbt-contains/comparison.json).

- [Raiz explícita com índice externo](PLAN-TASKS/2026-11-09-crg-iu1-raiz-externa.md) — o caso sem VCS passa em Windows e Ubuntu. O mantenedor retoma `crg-iu1` pelo caso dbt `TestDbtModelParsing::test_contains_edge` antes do próximo release Windows. Reproduzir nos dois sistemas e comparar a identidade da aresta com a representação do caminho. [Saldo por ID](receipts/crg-iu1-raiz-externa/comparison.json).

- [Seleção exata do forget no Windows](PLAN-TASKS/2026-11-09-crg-iu1-forget.md): `aca7f74` e CI 9/9. `pkg_extra` fica no índice e o Ubuntu distingue `PKG` de `pkg`. Restam cinco IDs em `crg-iu1`. O mantenedor começa pelo caso de `--repo` explícito sem marcadores antes do próximo release Windows. [Saldo por ID](receipts/crg-iu1-forget/comparison.json).

- [Portabilidade dos testes Julia](PLAN-TASKS/2026-11-09-crg-iu1-julia.md): `9f1f19b`, 27/27 Windows e Ubuntu, 27/27 no job Windows e CI 9/9. `crg-iu1` fica com oito IDs. Próximo corte: reproduzir o trio de `_match_files_to_forget` e conferir `forget --dry-run` em banco descartável. [Comparação por ID](receipts/crg-iu1-julia/comparison.json).

- [Caminhos PHP/Rust no Windows e Ubuntu](PLAN-TASKS/2026-11-09-crg-iu1-caminhos-php-rust.md): `f825c25`, 7/7 em cada sistema, 9/9 na CI e três IDs removidos do baseline Windows. Este corte histórico registrou 21 falhas antes da rodada Julia. [Comparação por ID](receipts/crg-iu1-caminhos/comparison.json).

- [Adoção da correção PHP no índice persistente](PLAN-TASKS/2026-11-09-crg-adocao-indice-php.md): `crg-dq9`, checklist 5/5, banco habitual adotado e reaberto pela CLI em `eeb486b`. Backup local restaurável, 4.745 embeddings retidos. `crg-87w` registra o frescor de vetores das fontes alteradas. [Veredito](receipts/crg-adocao-indice-php/verdict.json).
- [Resolução PHP de homônimos](PLAN-TASKS/2026-11-09-crg-x6m-php-homonimos.md): produto `fb9fc22`, com a identidade lexical comprovada para construtor e método, inclusive com Composer. [Veredito pronto com ressalvas](receipts/crg-x6m/verdict.json), checklist 4/4.

- [Frescor semântico do índice](PLAN-TASKS/2026-11-08-crg-k4q-frescor-indice.md): backup verificado e rebuild isolado provam a reclassificação no mesmo SHA. Antes de adotar nova semântica no índice persistente, use a rota no [gatilho vivo](GATILHOS-VIVOS.md#staleness-artefatos-derivados).
- [Classificação por caminho](PLAN-TASKS/2026-11-08-crg-test-path.md): regressões corrigidas em `3fb1ab3`, com CLI, SQLite e nove jobs de CI. `crg-iu1` mantém os 24 IDs preexistentes.
- [Revisão adversarial PHPUnit](receipts/crg-phpunit-adversarial/LAUDO.md): origem do RED. Evidências operacionais separadas em `crg-k4q` e `crg-x6m`.

- [PHPUnit no Windows](PLAN-TASKS/2026-11-08-crg-phpunit-windows.md): consulta direta comprovada em banco isolado, 3 regressões verdes e seleção CI Windows reproduzida localmente. Mantenedor CRG retoma as 24 falhas restantes de `crg-iu1` antes do próximo release Windows. O índice persistente passa pelo check de staleness antes do próximo consumo.

- [Índice persistente](PLAN-TASKS/2026-11-08-crg-indice-persistente.md): backup SQLite íntegro, build com a CLI do checkout, SHA conferido e associação direta comprovada. Conferir staleness pelo `status --json` antes de consumir.

- [Reexportações Python](PLAN-TASKS/2026-11-08-crg-python-reexports.md): `crg-j6z`, identidade canônica e update com regressão pela CLI. O histórico em `573580b` retorna o teste direto e mantém o recorte 1/1. Índice persistente preservado. Rebuild com backup é o próximo corte antes de usar a correção no grafo persistente.

- [Piloto CLI em diff real](PLAN-TASKS/2026-11-08-crg-cli-diff-real.md): build no pai de 573580b, update isolado e comparação Git/AST/JSON. `query_graph` cobre os três hunks. O teste do ramo `references_to` passou e faltou em `tests_for`. Bead `crg-j6z`, owner mantenedor CRG, próximo corte.

- Direcao atual: [CLI como interface principal](../docs/EDICAO-DEX.md#direcao-do-produto). `CRG-CLI-RECORTE` provado pelo executavel em `1e12485`; [Trilho](PLAN-TASKS/2026-11-08-crg-cli-recorte.md) e [mapas](MAPAS/INDEX.md). Use o executavel do checkout para reproduzir as provas.

- Fechamento oficial do recorte CLI: flow `flow_20261108185314975_0133_0033` completo, veredito `vrd_20261108190531226_0153_0059` pronto com ressalvas, checklist 3/3. Produto `1e12485` e mapas `cd179cf` confirmados no main privado. Suite isolada 222 passou, 1 skip previsto. Git e Dolt publicados.

- Corte corrente: [repo privado e higiene](PLAN-TASKS/2026-11-08-crg-repo-privado-higiene.md). A autorizacao do dono cobre criacao, commit e push. `origin` privado `dex-agent/dex-code-review-graph`; origem publica preservada em `upstream`.
- Separacao: fontes e registros curados versionados. Config local `.codex/config.toml`, interacoes Beads, `.ppirtv`, backups e Graphify bruto ficam no disco e ignorados. Um backup historico contem credencial. Verificacao de rotacao no ledger com dono e quando.

- Recorte do diff: código local e testes em `changes.py` e `test_changes.py`; leia o [Trilho](PLAN-TASKS/2026-11-07-crg-diff-recorte.md) e os [mapas](MAPAS/INDEX.md). Validação local não atualizou o MCP instalado.

1. Leia `AGENTS.md`, `.agents/ACTIVE.md`, `.agents/napkin.md` e
   `.agents/GATILHOS-VIVOS.md` antes de trabalho não trivial.
2. Estado e evidência: laudo
   `.agents/EVIDENCIAS/2026-07-31-code-review-graph-home-replication.md`;
   Trilhos em `.agents/PLAN-TASKS/`; tracker `bd` (crg-frc fechado).
3. Runtime: `bd` 1.1.2, `code-review-graph` 2.3.7 (uv tool), MCP
   `dex_ppirtv` workspace-local (bundle V2, `bundle_configured`), CRG allowlist
   25 tools; handshakes provados por stdio.
4. Debitos atuais: [PENDENTES](PENDENTES.md). Historico `.ppirtv` preservado como prova local e excluido da publicacao. As tools MCP estao expostas nesta sessao. O runtime CRG ainda usa a instalacao anterior ao patch.
5. Segurança: não repetir valores de chaves; rotacionar `experimental_bearer_token`
   do provider DeepSeek (exposto em leitura do config global).

