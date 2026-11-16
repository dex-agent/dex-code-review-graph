# Rollback da troca do PATH (2.4.0+dex.1 -> anteriores)

Rota A — voltar ao 2.4.0 oficial (PyPI):
  uv tool install --force code-review-graph==2.4.0

Rota B — voltar ao wheel da casa 2.3.7 (schema 9):
  uv tool install --force "<caminho>/crg-2w-extracao/candidate/code_review_graph-2.3.7-*.whl"
  (sha 8fd3127c... do kit CRG-PACOTE-SEGUNDO-WINDOWS; verificado no corte do piloto)

Aviso: primeira abertura de índice schema-9 pelo 2.4.0+dex.1 migra o banco para 15
(upstream migrations). Projetos da casa reconstroem índices; Dex WhatsApp é descartável
(ordem do dono 2026-11-15).
