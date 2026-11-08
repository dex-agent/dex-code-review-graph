# Trilho ativo

- Atual: [Reexportações Python](2026-11-08-crg-python-reexports.md) | bead `crg-j6z` | checklist 4/4, flow completo e veredito `vrd_20261108224740560_0208_0128` pronto com ressalvas.

- Anterior: [piloto CLI em diff real](2026-11-08-crg-cli-diff-real.md), checklist 3/3. Flow `flow_20261108192331225_0160_0067` completo, veredito `vrd_20261108193045516_0179_0091` pronto com ressalvas. Recorte 1/1 em 573580b, omissão de teste no bead `crg-j6z`.
- Anterior: [recorte na CLI](2026-11-08-crg-cli-recorte.md), checklist 3/3, bead `crg-dqq` fechado, flow `flow_20261108185314975_0133_0033` completo. Veredito `vrd_20261108190531226_0153_0059` pronto com ressalvas. Produto `1e12485` e mapas `cd179cf` publicados no repo privado.

- Corte anterior: [repo privado e higiene](2026-11-08-crg-repo-privado-higiene.md), checklist 3/3, bead `crg-pr9` fechado, flow `flow_20261108130638616_0107_0001` completo. Verdict `vrd_20261108131605649_0126_0025` pronto com ressalvas. Publicacao Git e Dolt comprovadas em 2026-11-08. Owner: mantenedor CRG.

- Último corte: [recorte do diff](2026-11-07-crg-diff-recorte.md) — checklist 3/3, flow completo, veredito `vrd_20261107233038858_0102_0030` pronto com ressalvas. O registro abaixo preserva a replicação histórica.

- ID: `replicar-code-review-graph-casa` (2026-07-31)
- Status: `concluído com ressalvas`
- Owner atual: `validador-pronto`
- Abre: `.agents/PLAN-TASKS/2026-07-31-replicar-code-review-graph-casa.md`
- Objetivo: replicar no ambiente casa a instalação do escritório (bd 1.1.2 +
  CRG 2.3.7 uv tool + MCP allowlist 25 tools) e provar por handshake real.
- Fechamento: `bd` 1.1.2, CRG 2.3.7, handshake 25/5/0, grafo 5006/40981 no
  HEAD `268e0e1`; bead `crg-frc` aberto até o fechamento do bloco.
- Origem escritório: `integrar-code-review-graph-global`
  (`flow_20260728211327716_0036_0001`, `vrd_20260729090936382_0076_0001`).
- Próximo passo: reiniciar/reconectar o Codex Desktop para carregar o MCP CRG
  e usar a adapter em uma revisão real de baixo risco; publicar git/dolt apenas
  com autorização explícita.
- Evidência de origem:
  `.agents/EVIDENCIAS/2026-07-31-code-review-graph-home-replication.md`.
- REDs preservados: `apply_refactor`, hooks Windows, uninstall compartilhado,
  falha residual da CLI, cache offline de embeddings e publicação fora do corte.
