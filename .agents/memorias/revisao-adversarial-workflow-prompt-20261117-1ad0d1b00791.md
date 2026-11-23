---
implementation_version: v2
layer: L2
slug: revisao-adversarial-workflow-prompt-20261117-1ad0d1b00791
tags:
  - "#auto-memory/reference"
---

# revisao-adversarial-workflow-prompt-20261117

Espelho da auto-memory do host ZCode (arquivo revisao-adversarial-workflow-prompt-20261117.md, tipo reference).

Prompt pronto entregue ao dono (2026-11-17) para invocar o workflow

Workflow `revisao-adversarial` (revisão adversarial multi-modelo, 2 ondas,
diff congelado 1x, meta-análise contínua por metadados) vive em
`~/.zcode/workflows/revisao-adversarial.dwf.ts`; nasceu do merge das janelas
`sess_4c9a494d` + `sess_209fd1b4` (GO do dono 2026-11-07); cúria mais recente
2026-11-13 (metadados + meta-análise + protocolo de confirmação).

Contrato de invocação (args, todos CRAVADOS literais no draft — AmendWorkflow
roda com args={}, plaquinha ARGS-CRAVADOS):
- `alvo` (obrigatório): slug/caminho do corte ou pacote;
- `range_commits`: range git do diff congelado (default HEAD);
- `perfil`: "rapido" (5 lentes CORE, ≤14min, default do dono) | "completo"
  (10 lentes, 2 ondas, CONSOLIDADO-PARCIAL, ≤27min);
- `contexto`: fatos extras (corte, commit, verdict do flow);
- `outdir`: default `.agents/AUDITORIAS/adversarial`.

Regras vivas do run: revisor preso >15min → TaskStop + AmendWorkflow com args
re-cravados (journal `.zcode/workflow-runs/<id>.mjs`). Achados saem NÃO
confirmados POR DESENHO — a sessão dona confere na fonte/oráculo e anexa ao
JSONL da série (`~/.agents/workflow-meta/revisao-adversarial.jsonl`) UMA linha
`{"tipo":"confirmacao","run_id":...,"confirmados":N,"falso_positivos":N}`
(alimenta o fp_pct da meta-análise). Saídas esperadas: CONSOLIDADO.md,
META-ANALISE.md (tendências por lente + recomendações de calibração),
linha nova no JSONL — sem o JSONL alimentado a próxima meta-análise fica cega.
Fechamento: P1/P2 confirmados com file:line viram correção (conserte na
descoberta no escopo do repo; senão TRACKER do repo dono).

Uso: perfil rapido para corte comum; completo para release/PR importante.

CORREÇÃO 2026-11-17: a ID `sess_4c9a494d` citada no changelog do workflow NÃO
identifica o projeto daquela sessão — o projeto real dela é o TRACKER-0012 do
dex-PPIRTV ([[ppirtv-tracker-0012-attribution-verdict-20261117]]); o arquivo
.dwf.ts apenas a menciona como uma das janelas do merge de 2026-11-07. Lookup
de sessão por ID sempre pelo banco ([[zcode-session-db-lookup-receita-20261117]]).
Related: [[untangle-codebase-com-crg-regimes-20261117]], [[merge-check-gatilho-prompt-pronto-20261116]]

#auto-memory/reference

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^revisao-adversarial-workflow-prompt-20261117-1ad0d1b00791-content
