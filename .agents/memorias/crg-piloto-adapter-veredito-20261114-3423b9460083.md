---
implementation_version: v2
layer: L2
slug: crg-piloto-adapter-veredito-20261114-3423b9460083
tags:
  - "#auto-memory/project"
---

# crg-piloto-adapter-veredito-20261114

Espelho da auto-memory do host ZCode (arquivo crg-piloto-adapter-veredito-20261114.md, tipo project).

Piloto do adapter CRG CONCLUÍDO 2026-11-14 — flow PPIRTV completo,

**Piloto do adapter do CRG em revisão real — CONCLUÍDO (2026-11-14, GO do dono via GO-PADRAO)**. Flow PPIRTV `flow_20261114231445529_0771_0001` **completo** (concepcao→implementacao→revisao→validacao→complete), verdict **`vrd_20261114233626991_0803_0001` `pronto_com_ressalvas`**. Commits `18bb2568` (Trilho+estado vivo) + `17d35d47` (receipts LAUDO/INDEX versionados — exigiram exceção por diretório no `.gitignore` do CRG, padrão `!dir/ + dir/* + !dir/arquivo`) — pushed + bd dolt push. Trilho: `.agents/PLAN-TASKS/2026-11-14-crg-piloto-adapter-revisao-real.md` (4/4 checklist com evidência). Laudo: `.agents/receipts/CRG-PILOTO-ADAPTER-20261114/LAUDO.md`.

Resultados medidos: canário Dex WhatsApp `eb7d95b` clonado do **bundle privado** `a9d44a88…` (mora em `.agents/receipts/CRG-PILOTO-SEGUNDO-WINDOWS-20261114/package/` — "aguardava o 2º Windows autorizado"); suíte **73/73 0 fail** (rehearsal PREDATOR 72/72); `TESTED_BY` direto `distribution.test.cjs` **linha 4 idêntico CLI+SQLite**; `current_sha==built_at_commit`. Revisão real do diff `5356307` (o próprio commit merge-check como "PR" com gabarito conhecido): `detect-changes` 33 funções vs gabarito independente `git diff -U0` → **TP=32, FN=0-real, FP=0-real** (3 "FN" eram artefatos do gabarito por heurística de intervalo — docstring de módulo e funções novas adjacentes; 1 "FP" = grão classe `CodeParser`, correto em outro grão). Egress zero: venv candidate sem sentence-transformers, cache HF 89=89. Builds: 3s canário / 10s repo CRG.

**Envelope da review estrutural PPIRTV (custou 5 tentativas — decifrado na fonte `flow-engine.ts:3636-3682` + `gate-resolution.ts:158` + E2E `goal-lifecycle.e2e.test.ts`)**: evidência `kind=code_review` exige `satisfies` com os 3 tokens (`diff_reviewed`,`barata_scan`,`regression_risks`) + `observed_result` com `reviewed_targets` **cobrindo TODOS os `changed_files`** (não 2 de 5!) + `reviewed_implementation_fingerprint` igual ao fingerprint do flow + `scope_classification:"target"`/`scope_reference` relativo; depois `goal_gate_check {phase:"revisao", persist:true}` → verde → verdict cita essa evidência. Outros gotchas do motor: `goal_start` exige `objective` LITERAL do SPT + `evidence_required:true` + servidor com CWD=workspace (`GOAL_WORKSPACE_STORE_MISMATCH`); gates só aceitam chaves canônicas (`implementation_done`,`changed_files`,`diff_reviewed`,`barata_scan`,`test_executed`,`review_artifact_path`,`review_findings`,`residual_risks`,`next_step`,`memoria_viva_reconciled`) — chaves livres viram `provided_ignored`; `criterion_proof.revision_set` é array de `{workspace, paths[{path,sha256}]}` (git_head o servidor amarra); servidor tem `satisfies_blockers` p/ `code_review`. Rota sem MCP do host: harness stdio próprio `C:\CodexProjetos\crg-2w-execucao\mcp-call.mjs` (env `MCP_CWD` define o project_root).

Ressalvas/pendências: **"21/21" do kit DEFASADO** (real 72/72→73/73; 2 ocorrências: `LEIA-ME.md:76` + `PROMPT-2-PROVAS.md:8` — correção editorial pendente); granularidade classe-vs-função do `detect-changes` merece doc. Estacionado: X-01 promoção a rota permanente (GO do dono, com o laudo na mão), X-02 coluna `clean_name` p/ 502 nós CHAVE* (upstream master_maximus, sessão `sess_8a7ea947` — tools de reuso: `grafo_gate.py` validado no piloto, `normalize_name()` candidato). Artefatos do piloto preservados em `C:\CodexProjetos\crg-2w-execucao\piloto\` (clone, índices descartáveis, detect-changes JSON). Lições master_maximus respeitadas: `callers_of` cego a tests/; FTS falso-negativo em nome ofuscado (zero hit ≠ ausência).

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-piloto-adapter-veredito-20261114-3423b9460083-content
