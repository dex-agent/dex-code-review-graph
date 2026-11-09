# HANDOFF — retomada curta

Ultima atualizacao: 2026-11-09

- [Caminhos PHP/Rust no Windows e Ubuntu](PLAN-TASKS/2026-11-09-crg-iu1-caminhos-php-rust.md): `f825c25`, 7/7 em cada sistema, 9/9 na CI e três IDs removidos do baseline Windows. Em `crg-iu1`, 13 das 21 falhas restantes são de Julia. Começar por `test_qualified_definitions_have_collision_free_identities` em Windows e Ubuntu, capturando a primeira divergência antes de editar. [Comparação por ID](receipts/crg-iu1-caminhos/comparison.json).

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

