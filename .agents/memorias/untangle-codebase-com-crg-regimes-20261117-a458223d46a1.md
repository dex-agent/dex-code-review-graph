---
implementation_version: v2
layer: L2
slug: untangle-codebase-com-crg-regimes-20261117-a458223d46a1
tags:
  - "#auto-memory/project"
---

# untangle-codebase-com-crg-regimes-20261117

Espelho da auto-memory do host ZCode (arquivo untangle-codebase-com-crg-regimes-20261117.md, tipo project).

Playbook entregue ao dono (2026-11-17) — dex-untangle-codebase ×

Integração `dex-untangle-codebase` × CRG entregue ao dono em 3 prompts
prontos (2026-11-17). Princípio: a skill manda "scriptar grafo de
dependências / usar git como evidência / achar testes que não pegam bug" —
o CRG JÁ É isso (queries + detect-changes + tests_for); skill decide (QUÊ),
CRG prova (COMO).

Mapeamento por classe da skill → query CRG:
- hidden links → `query communities` (Leiden = muda-junto morando separado) +
  `search` (cópias de lógica) + `imports_of`/`callers_of`;
- needless links → `imports_of <estável>` importa volátil? + `impact --files`
  (quem paga quando muda);
- surplus → `callers_of` = 0 + `tests_for` ausente;
- special cases → `large-functions` (leverage) + `detect-changes --files`
  no que mais mudou (`git log --name-only`).
Regra da casa: achado de grafo só entra no decision log com file:line aberto
NA FONTE. Fase 4: `callers_of` = lista completa de call sites ao mover
(anti bug-fantasma). Fase 5: `detect-changes --files` (risco+test_gaps) +
merge-check na integração de branch.

3 regimes de prompt:
- **A — Campanha completa** (untangle inteiro, 1x ou quando B revela
  emaranhado sistêmico): fases 1-5 da skill com CRG em cada uma.
- **B — Ronda contínua** (~30-60min, 1-3 alvos/sprint): doctor →
  detect-changes/large-functions → diagnóstico com prova → fix único
  (árvore) → fecho com evidência + APPEND no decision log do repo
  (`.agents/UNTANGLE-LOG.md`). Cadência: 1 ronda por sprint ou após bloco
  que toque >5 arquivos; entropia nascida fora da ronda vai pro log, não
  fica solta.
- **C — Consulta pontual** (2 min, uma suspeita): callers_of/imports_of/
  tests_for/impact no alvo → veredito 4 linhas (mexer agora / agendar no
  log / limpo).
Uso: C na dúvida · B toda sprint (entropia nunca acumula) · A só no
sistêmico. UNTANGLE-LOG é a memória que amarra os três.

Limites declarados: CRG é estrutural (não julga semântica/comentários);
Delphi → rota feeder; grafo stale = mapa velho (doctor antes de cada ronda).

**Variante dex-PPIRTV entregue (2026-11-17): dex-untangle-codebase +
dex-untangle-prune-tests + CRG combinados.** Ordem obrigatória: prune-tests
RODA POR ÚLTIMO (teste é a rede de regressão do refactor). Destaques do
prompt: (1) FRONTEIRA com TRACKER-0012 — untangle é ESTRUTURAL, não toca os
sítios comportamentais em voo (flow-engine.ts:2554/2579/2599 etc.); achado
estrutural naquela região vira linha do UNTANGLE-LOG + item TRACKER, não
diff; (2) entrada pelo monolito flow-engine.ts (`large-functions`) com régua
literal do repo (árvore, não remendo — nasceu lá); (3) prune-tests com CRG:
`query tests_for` = mapa teste→alvo, `detect-changes --files` = test_gaps;
classes da prune-skill (o passado / nada / a implementação) casadas com
callers_of=0 (código removido pelo untangle → testes juntos) e acoplamento
a interno; (4) PROTEGIDO: teste de caracterização (ex. harness do 0012) é
behavior-anchored, NUNCA podar — veredito na dúvida é do
$oraculo-refatoracao (owner evolutivo), não da poda; (5) fechamento com
merge-check três vias + defeitos comportamentais descobertos → TRACKER.

**CORREÇÃO do dono (2026-11-17) — fase ASK NÃO pergunta ao dono**: o "Ask"
da untangle-skill (Comments/Tests) é decidido por INTERROGATÓRIO DOCUMENTAL
com `$interrogador-documental` + `$entrevista-com-docs` sobre as fontes
vivas (AGENTS do repo + dex-regras-desenvolvimento-casa R1-R17 + PRINCIPLES
+ histórico CHANGELOG/Trilhos), veredito COM citação (fonte+linha). Quiz de
1 pergunta SÓ se as fontes ficarem mudas ou conflitantes (molde
INTERROGAR-ESGOTOU: recomendada em primeiro, silêncio = segue a recomendada
declarada no fechamento). Princípio geral do dono: perguntar ao dono o que
as fontes da casa respondem = adivinhação transferida.

**2 skills acrescentadas ao prompt dex-PPIRTV por consulta grafo rico +
CAPACITY (2026-11-17, pedido do dono)** — receita replicável: capacity-index
(`governancia-skills/references/capacity-index.json`, cards capability_tags)
→ `graphify query` no grafo do registry (`.agents/GRAPHIFY/skills-catalog/
candidate-696-merge/graph.json`) → confirmar no SKILL.md vivo:
1. **$dex-duplicacao-codigo** (fase 2, hidden links): mesma comunidade do
   untangle no grafo; cópias com nomes trocados/variantes de comportamento
   equivalente, disciplina de FONTE DONA + consumidores — o `search` do CRG
   acha o suspeito textual, a skill decide quem é a árvore-mãe (R6 da régua).
2. **$dex-complexidade-ciclomatica** (fases 3/7): `medir-cc.py` nativo js/ts,
   régua teto CC 10/linhas 50 — BASELINE do monolito antes da 1ª árvore,
   re-medida no fechamento com número antes→depois (RESPIRA item 8); acima
   do teto = árvore que falta plantar, não ressalva.

**VERSÃO GENÉRICA do prompt dex-PPIRTV (2026-11-17/19)** — para qualquer
repo: capability-check de exe (0a), COBERTURA DE LINGUAGEM antes de tudo (0b:
ps1 não parseado; Delphi → feeder; lingua principal fora do CRG = declara e
pergunta), frescor/gitignore do data dir (0c); monolito DESCOBERTO por
`large-functions --kind Function` + `architecture` (não assumido); suíte do
repo descoberta ou lacuna declarada (caracterização = rede mínima);
baseline `medir-cc.py <hotspot>`; oráculo da dúvida = owner local do AGENTS
ou $oraculo-refatoracao. Validação do genérico: executor que pedir "qual é o
monolito?" = prompt falhou (a fase 2 descobre, não pergunta).

Related: [[ppirtv-tracker-0012-attribution-verdict-20261117]],
[[crg-240dex-merge-fechado-20261115]], [[merge-check-gatilho-prompt-pronto-20261116]],
[[entropia-conserta-na-descoberta-20261116]]

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^untangle-codebase-com-crg-regimes-20261117-a458223d46a1-content
