---
dex_contract: spt
version: 3
status: 'CONCLUIDO'
owner: 'sessao:zcode (GO do dono via quiz: cura do CI agora — recomendado oraculo-solid)'
date: '2026-11-19'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'Auditoria READ-ONLY do repo online 2026-11-19 (laudo): P1 CI vermelho cronico no main desde 11-14 (>=6 failures); root parcial evidenciado = path-separator Windows (assert C:/ == C:\\); oraculo-solid selou Fragilidade (l.2432) + Viscosidade (l.2424) do corpus 2002/2000'
goal:
  id: 'cura-ci-vermelho-20261119'
  title: 'CI do main verde: curar path-separator no chokepoint e triar as classes do run 43929195987'
  objective: 'Tornar o workflow CI verde no push do main do dex-agent/dex-code-review-graph, curando na causa (normalizacao canonica de path no boundary que produz file_path) a classe path-separator Windows evidenciada no run 43929195987, com RED-first local, e registrando as classes triadas no TRACKER'
context: 'Laudo da auditoria: runs 43654239307..43929195987 failure; job Windows daemon morre em assert method.file_path == str(path) com C:/ vs C:\\ (classe as_posix que o A/B 2.4.0+dex.1 curou localmente mas o runner ainda paga); jobs ubuntu (3.10-3.13 + floors) tambem falham com root nao triada; local behind 2 (2fababd5, c6146110 fix --files) + uv.lock sujo'
problem: 'CI vermelho cronico no main: Fragilidade (detalhe de plataforma vaza na assercao) + Viscosidade (vermelho ignorado); verde local nao e veredito — o runner e'
decision: 'Bloco unico de cura: pull -> log-failed triado por classe -> RED local da classe Windows -> cura no chokepoint (nao nos testes) -> push com CI verde -> TRACKER das classes + tag seca v2.4.0+dex.1'
scope:
  include:
    - 'git pull --rebase (behind 2) + resolver uv.lock'
    - 'download gh run view 43929195987 --log-failed + triagem por classe com contagem'
    - 'RED-first local: reproduzir 1 assercao path-separator falhando'
    - 'cura no boundary produtor de file_path (arvore pequena; callers via CRG)'
    - 'push e verificacao CI verde no main (gh run watch/list)'
    - 'TRACKER: itens das 2 classes (CI curado + dependabot orfao) + tag seca v2.4.0+dex.1'
  exclude:
    - 'triagem/fechamento dos 5 PRs dependabot (mutacao separada, outro GO)'
    - 'mudanca de workflows (.github) exceto se o root exigir'
requirements:
  - id: REQ-01
    statement: 'Causa da classe path-seulator curada no chokepoint'
    criteria:
      - id: C-01
        statement: 'RED local reproduz a assercao falhando antes da cura e verde depois'
      - id: C-02
        statement: 'classes do run 43929195987 triadas com contagem no receipt'
  - id: REQ-02
    statement: 'CI verde no main do remoto'
    criteria:
      - id: C-03
        statement: 'apos push, workflow CI conclui success no main (run ID registrado)'
      - id: C-04
        statement: 'TRACKER atualizado com as classes + tag seca v2.4.0+dex.1 no commit verde'
plan:
  - 'A-01 base: pull rebase + uv.lock'
  - 'A-02 prova: log-failed baixado e triado'
  - 'A-03 RED local + cura no chokepoint + suite local'
  - 'A-04 push + CI verde remoto'
  - 'A-05 TRACKER + tag seca + fechamento'
tasks:
  - id: A-01
    action: 'Alinhar base local (behind 2) e limpar uv.lock'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'git status -sb limpo e HEAD == origin/main'
        expectation: {kind: command_exit, expected_exit_code: 0}
  - id: A-02
    action: 'Baixar log-failed e triar classes'
    covers: [REQ-01]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'gh run view 43929195987 --log-failed > receipt; contagem por classe'
        expectation: {kind: command_exit, expected_exit_code: 0}
  - id: A-03
    action: 'RED-first + cura no chokepoint + suite local'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-01]
        method: command
        procedure: 'harness RED -> cura -> suite verde'
        expectation: {kind: command_exit, expected_exit_code: 0}
  - id: A-04
    action: 'Push e CI verde remoto'
    covers: [REQ-02]
    done_when: [C-03]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-03]
        method: command
        procedure: 'gh run list --branch main | grep success (run ID no receipt)'
        expectation: {kind: command_exit, expected_exit_code: 0}
  - id: A-05
    action: 'TRACKER classes + tag seca + fechamento'
    covers: [REQ-02]
    done_when: [C-04]
    depends_on: [A-04]
    evidence_requirements:
      - id: ER-05
        proves: [C-04]
        method: command
        procedure: 'rg TRACKER + git tag -l v2.4.0+dex.1'
        expectation: {kind: command_exit, expected_exit_code: 0}
closure_gates:
  - 'CI verde no main (run ID) — nao basta suite local'
  - 'Nenhuma mutacao no remoto alem do push de cura e tag (dependabots intocados)'
risks:
  - 'root ubuntu pode ser classe distinta (nao path) — mitigacao: triagem A-02 decide escopo; se classe nova grande, registra no TRACKER e nao amplia este bloco'
  - 'CI pode ter falhas ambientais persistentes alem da classe curada — mitigacao: veredito e o CI verde; se restar falha ambiental, TRACKER com evidencia e ressalva declarada'
uncertainties:
  - 'Tempo de runner (~10min por run de CI) — verificacao pode atravessar fechamento de janela; registrar run ID e conferir'
gates:
  - 'spt_validate valido antes de goal_start (consumidor MCP indisponivel na sessao; preflight local como validador com evidencia)'
validation:
  - 'node C:/CodexProjetos/dex-PPIRTV/spt-kit/preflight.mjs <este trilho>'
execution_prompt: |
  /GOAL
  Curar o CI vermelho cronico do main (run 43929195987): triar classes,
  RED-first da classe path-separator, cura no chokepoint, push com CI verde,
  TRACKER + tag seca v2.4.0+dex.1.
---

# Cura do CI vermelho (P1 do laudo 2026-11-19)

## Checklist visual

- [x] A-01 — base alinhada (behind 2 resolvido, uv.lock limpo) — HEAD 2fababd5 == origin/main
- [x] A-02 — log-failed baixado, classes contadas — 17 FAILED distintos (12 asserts path-separator; receipt log-failed.txt 5544 linhas)
- [x] A-03 — RED local + cura no chokepoint + suite verde — 8 classes curadas (C1-C8, tabela em receipts/CI-43929195987/green-battery.txt): 65 passed na bateria; paridade 2-rodadas = 0 regressões exclusivas (22 vs 28 baseline); ruff/mypy limpos nos tocados. RESSALVA: C4 recalibrado na evidência — o chokepoint é o TESTE (contrato #774 forward-slash), não o produtor; C7 virou resolver de reexport (5 edges: alias-chain/shadowed/capture/cycle/conditional-star) + C8 declaração runner JS.
- [x] A-04 — push + CI verde no main (run ID) — 4 levas até o verde: 71f5fae7 (C1-C8) → 19669fa2 (camada oculta C9-C10: steps do job Windows param no 1º erro; matcher forget ganha normcase) → af2210c6 (camada 3 C11: merge 3ddf2c8b engolira fix+teste f145ca80) → 9ca592aa (marker honra registro externo + exe via which). RUN VERDE: 44517837083 (22/22 jobs ✓)
- [x] A-04 — ADENDO pós-fechamento (classe 12/13, levas 5-6): a tag seca virou input da suíte test_released_shapes (5ª forma de ocultação: skip condicional com 0 tags) — d08a0013 (placeholders do instalador de hoje) + fb76a964 (skips honestos quando só tag dinâmica); armadilha: 33 tags upstream locais = falsa premissa; reprodução fiel do runner = clone shallow da tag. RE-VERDE CONFIRMADO: run 44529405896 completed success (2026-11-19)
- [x] A-05 — TRACKER classes + tag seca + fechamento — ISSUE-LOCAL-0004 (fechado, 11 classes) + 0005 (dependabot, aberto aguardando GO) + INDEX; tag seca v2.4.0+dex.1 no commit verde
