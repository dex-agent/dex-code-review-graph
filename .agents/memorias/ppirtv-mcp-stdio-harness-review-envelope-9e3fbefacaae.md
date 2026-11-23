---
implementation_version: v2
layer: L2
slug: ppirtv-mcp-stdio-harness-review-envelope-9e3fbefacaae
tags:
  - "#auto-memory/reference"
---

# ppirtv-mcp-stdio-harness-review-envelope

Espelho da auto-memory do host ZCode (arquivo ppirtv-mcp-stdio-harness-review-envelope.md, tipo reference).

Receita do ciclo GOAL PPIRTV sem MCP do host (harness stdio) +

Ciclo GOAL/SPT v3 completo rodado sem MCP do host via harness stdio próprio (`crg-2w-execucao/mcp-call.mjs`, spawn de `dex-PPIRTV/dist/index.js` com `cwd: env MCP_CWD` = workspace-alvo, pois o servidor assume CWD como project_root; erros PPIRTV_INPUT_INVALID nomeiam campo/tipo/exemplo — corrigir e reenviar). Fatos de contrato pagos ao vivo (fluxo `flow_20261114231445529_0771_0001`):

- `goal_start`: `objective` deve ser LITERALMENTE igual ao `goal.objective` do SPT; `evidence_required: true` obrigatório.
- `evidence_add` criterion_proof: `revision_set` é ARRAY de `{workspace, paths:[{path,sha256}]}` (git_head_base o próprio servidor amarra); exige `environment`, `producer`, `timestamp`, `limits`. Provas citam só o sha VIGENTE (plaquinha STALE).
- **Envelope da review estrutural** (bloqueio `review_required`/`review_evidence_coherent`; 5 tentativas até o molde; fonte `flow-engine.ts:3636-3682`, `gate-resolution.ts:158`): evidência `kind: code_review` com `satisfies: [diff_reviewed, barata_scan, regression_risks]` + `observed_result {diff_reviewed, reviewed_targets cobrindo TODOS os changed_files, barata_scan, searched_patterns, findings, regression_risks}` + `reviewed_implementation_fingerprint` EXATO do snapshot + `scope_classification: "target"` + `scope_reference`; depois `goal_gate_check {phase:"revisao", persist:true}` e só então `goal_verdict` citando essa evidência. Diagnóstico oficial: `import dist/gate-resolution.js → reviewEvidenceDiagnostics(flow, evidence)` nomeia os reasons exatos (ex.: `changed_files_not_fully_reviewed`).
- `goal_verdict`: exige `next_step`; `verdict`/`residual_risks`/`next_step`/`memoria_viva_reconciled` no advance terminal.
Molde E2E canônico: `tests/goal-lifecycle.e2e.test.ts` (D-35) do dex-PPIRTV. Related: [[crg-piloto-adapter-veredito-20261114]].

#auto-memory/reference

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^ppirtv-mcp-stdio-harness-review-envelope-9e3fbefacaae-content
