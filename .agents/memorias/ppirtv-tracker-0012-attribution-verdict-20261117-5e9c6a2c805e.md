---
implementation_version: v2
layer: L2
slug: ppirtv-tracker-0012-attribution-verdict-20261117-5e9c6a2c805e
tags:
  - "#auto-memory/project"
---

# ppirtv-tracker-0012-attribution-verdict-20261117

Espelho da auto-memory do host ZCode (arquivo ppirtv-tracker-0012-attribution-verdict-20261117.md, tipo project).

TRACKER-0012 dex-PPIRTV (sess_4c9a494d "Problema com issue remoto")

Sessão `sess_4c9a494d-82e9-4000-8544-8a93e7ed5fc5` (workspace
`C:\CodexProjetos\dex-PPIRTV`, título "Problema com issue remoto") trabalha a
**cura do TRACKER-0012** (`.agents/TRACKER/issues/0012-verdict-sem-attribution-citada-retomam-alheios.md`,
aberto, P2). Origem: flow `flow_20261115211534924_2319_0001` (4 rejeições de
verdict + 2 regress cirúrgicos desperdiçados; workspace com janela paralela).

**Arestas medidas:**
- (a) `goal_verdict` SEM `scope_attribution_evidence_ids` re-executa
  `applyReviewScopeAttributions` com `evidenceIds=[]` → `corroborated.changed_files`
  volta a ser o git inteiro (alheios incluídos) → fiscal rejeita `review_required`
  mesmo com review estrutural válida + attribution aprovada no flow. Erro NÃO
  nomeia o campo faltante (variante da 0003: erro não aponta a cura).
- (b) Verdict rejeitado pós-attribution persiste estado HÍBRIDO:
  `changed_files=8` antigo + `implementation_fingerprint` do conjunto 13 →
  `evidence_add code_review` morre `FINGERPRINT_MISMATCH` → única saída era
  `goal_regress` + advance com conjunto unificado (regress é recurso escasso, max 3).

**Sítios decifrados:** `flow-engine.ts:2554/2579` (verdict mescla/aplica
attribution) e `:2599` (`restoreBlockedVerdictSnapshot`); `review-scope-attribution.ts:13/44/100/171-176`;
`review-snapshot.ts:319` (declaredReviewPaths); `gate-resolution.ts:114-165/467`;
`verdict-fiscal-policy.ts:68`; `ppirtv-checkin.ts:235-236` (regex
review_visible/tests_visible — ponto de costura, intocado no D-52).

**Cura (2 pontos):** (1) corroboração REUTILIZA attribution aprovada quando o
binding (`git_head_base` + fingerprint das exclusões) segue válido — ou, mínimo,
o erro do fiscal NOMEIA `scope_attribution_evidence_ids`; (2) rejeição reconcilia
`changed_files`+`implementation_fingerprint` ATOMICAMENTE (persiste os dois ou
nenhum).

**Estado**: Parte 1 (mesa de cooperadores) paga — ORÁCULO-INDICADO
`$oraculo-refatoracao` (owner evolutivo de flow-engine.ts), selo
`confirmado_documental` (âncoras Fowler: caracterização ANTES de mudar
comportamento). **Parte 2 (prompt de execução) entregue ao dono 2026-11-17**:
SPT-simples → RED-first reproduzindo as 2 arestas do flow 2319 em harness →
cura nos sítios (árvore, não remendo) → GREEN + suíte + barata-scan da classe
(erros irmãos que não nomeiam a cura em gate-resolution/verdict-fiscal-policy)
→ item fechado com evidência + push. Regra de ouro: RED não reproduz → PARE e
interrogue. **Teste de aceitação**: workspace com janela paralela ativa fecha
em 1 verdict limpo (hoje custa 4 rejeições + 2 regress).
**Fronteira irmã**: prompt untangle+prune-tests+CRG do mesmo repo (2026-11-17)
declara-se ESTRUTURAL — não toca os sítios do 0012; seu harness de
caracterização é protegido de poda por definição
([[untangle-codebase-com-crg-regimes-20261117]]).
Related: [[ppirtv-mcp-stdio-harness-review-envelope]], [[zcode-session-db-lookup-receita-20261117]]

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^ppirtv-tracker-0012-attribution-verdict-20261117-5e9c6a2c805e-content
