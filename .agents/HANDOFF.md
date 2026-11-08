# HANDOFF — retomada curta

Ultima atualizacao: 2026-11-08

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

