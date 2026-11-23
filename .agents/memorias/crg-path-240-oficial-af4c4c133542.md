---
implementation_version: v2
layer: L2
slug: crg-path-240-oficial-af4c4c133542
tags:
  - "#auto-memory/project"
---

# crg-path-240-oficial

Espelho da auto-memory do host ZCode (arquivo crg-path-240-oficial.md, tipo project).

PATH habitual do CRG trocado por 2.4.0 upstream (2026-11-14 20:12,

Em 2026-11-14 20:12 o executável habitual `~\.local\bin\code-review-graph.exe` foi trocado por **2.4.0 OFICIAL do upstream** (github.com/tirth8205/code-review-graph) via `uv tool` do índice/PyPI — venv recriado em `AppData\Roaming\uv\tools\code-review-graph\`, entry point novo `crg-daemon`, **sem recibo em `.agents/receipts/`** (a adoção 2.3.7 anterior tinha rota offline+rollback documentadas). Repo local segue 2.3.7; a troca contraria o verdict `vrd_20261114200615016` do Trilho crg-gates-upstream ("manter o CRG da casa como base").

Riscos medidos na comparação de ontem: 2.4.0 usa **schema 15 e MIGRA o banco ao abrir** (índice persistente Dex WhatsApp está em schema 9 — abrir só DB novos); `tests_for` de install = 0 resultados e `detect-changes --files` exit 2; ganhos: UTF-8 nativo em CP1252, cobertura indireta, HTML por seções. Dono foi perguntado (quiz) reverter/manter/documentar e não respondeu — **nada foi mexido**; wheel da casa `8fd3127c` segue disponível em `crg-2w-execucao/run1/candidate`. Relacionado: [[reconhecimento-code-review-graph]].

2026-11-15: dono não viu o quiz → situação explicada por nota de voz Telegram (message_id 1191, roteiro `Temp\roteiro-crg-240.txt`; Edge TTS caiu em 429, entregue pela rota alternativa Kokoro `pf_dora` via OpenRouter). Decisão segue pendente — ordens combinadas: "reverte" (rollback documentado, receipt `crg-cjs-runtime-20261113`) ou "mantém e documenta" (update ACTIVE/HANDOFF com riscos).

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-path-240-oficial-af4c4c133542-content
