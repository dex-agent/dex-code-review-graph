---
implementation_version: v2
layer: L2
slug: crg-rebuild-preserva-embeddings-no-candidato-isolad-ddbe87c32bec
tags:
  - "#crg/indice"
  - "#crg/embeddings"
---

# CRG-REBUILD-PRESERVA-EMBEDDINGS no candidato isolado

No crg-dq9, um build isolado a partir de um banco vazio passou em status e tests_for, mas ficou sem a tabela embeddings. O banco habitual tinha 4.745 vetores. Para promover uma reconstrução preservando o comportamento do rebuild nativo, faça backup SQLite, semeie a cópia isolada com esse backup e rode build sobre a cópia. Compare a tabela e os vetores de fontes inalteradas antes da adoção; no corte, 4.745 linhas foram retidas e 4.164 vetores de fontes com hash igual conferiram byte a byte. Preservação não comprova atualização dos vetores das fontes alteradas. Provas: receipts/crg-adocao-indice-php/maps.json e candidate.json. Owner: mantenedor CRG.

#crg/indice #crg/embeddings

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-rebuild-preserva-embeddings-no-candidato-isolad-ddbe87c32bec-content
