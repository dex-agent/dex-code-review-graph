---
dex_contract: spt
version: 3
status: 'CONCLUIDO'
owner: 'sessao:zcode (GO do dono via quiz do oraculo-solid: GO 0005 agora)'
date: '2026-11-19'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'ISSUE-LOCAL-0005 (auditoria READ-ONLY 2026-11-19); veredito oraculo-solid: REP l.5851/5863 — reuso exige release rastreada; faltava completar o ciclo do rastreio do fork'
goal:
  id: 'fecha-ciclo-auditoria-0005-20261119'
  title: 'Bloco 0005: desfecho dos 5 PRs dependabot + alerts ON + publish.yml desabilitado + CODEOWNERS'
  objective: 'Executar as 4 mutacoes pendentes do laudo da auditoria com receipt por passo, fechando o ISSUE-LOCAL-0005 e o ciclo do laudo'
context: 'Fork acompanha upstream por merge manual da casa (3ddf2c8b); PRs dependabot de 11-08 zumbis (1 vermelho, bot comenta sozinho); alerts OFF com updates ON; publish.yml latente (trigger release:published; tag seca nao dispara); CODEOWNERS ausente'
problem: 'Automacao orfa: updates que voltam semanalmente sobre PRs que ninguem quer, alertas de seguranca desligados, publish a um Release manual de distancia'
decision: 'Politica: acompanhar upstream manualmente — fechar os 5 PRs com razao, desligar version-updates (dependabot.yml), ligar vulnerability-alerts por API, desabilitar publish.yml ate politica de release, CODEOWNERS minimo'
scope:
  include:
    - 'gh pr close 5 PRs app/dependabot com comentario de razao apontando ISSUE-0005'
    - 'dependabot.yml: remover version-updates (commit+push)'
    - 'gh api PUT vulnerability-alerts (esperado 204)'
    - 'gh workflow disable publish.yml'
    - 'CODEOWNERS minimo dex-agent (commit+push)'
    - 'ISSUE-0005 fechado com receipts por mutacao + INDEX'
  exclude:
    - 'publicar release/tag nova; mexer em workflows de CI'
requirements:
  - id: REQ-01
    statement: 'Cada mutacao do laudo executada com receipt executavel'
    criteria:
      - id: C-01
        statement: 'Os 5 PRs dependabot fechados com comentario de razao apontando ISSUE-0005'
      - id: C-02
        statement: 'dependabot.yml sem version-updates no HEAD do main (commit+push)'
      - id: C-03
        statement: 'vulnerability-alerts ON (PUT retorna 204)'
      - id: C-04
        statement: 'publish.yml desabilitado no remoto'
      - id: C-05
        statement: 'CODEOWNERS minimo pushed e ISSUE-0005 fechado com receipts no TRACKER'
plan:
  - 'A-01 fechar 5 PRs com comentario de razao'
  - 'A-02 dependabot.yml sem version-updates (commit+push)'
  - 'A-03 alerts ON via API'
  - 'A-04 publish.yml disabled'
  - 'A-05 CODEOWNERS pushed'
  - 'A-06 fechar ISSUE-0005 + INDEX'
tasks:
  - id: A-01
    action: 'Fechar 5 PRs dependabot com razao'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'gh pr list -R dex-agent/dex-code-review-graph --state closed --author app/dependabot (5 fechados)'
        expectation: {kind: command_exit, expected_exit_code: 0}
  - id: A-02
    action: 'dependabot.yml sem version-updates'
    covers: [REQ-01]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'git show HEAD:.github/dependabot.yml (sem bloco updates)'
        expectation: {kind: command_exit, expected_exit_code: 0}
  - id: A-03
    action: 'Ligar vulnerability-alerts'
    covers: [REQ-01]
    done_when: [C-03]
    depends_on: []
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'gh api -X PUT repos/dex-agent/dex-code-review-graph/vulnerability-alerts (exit 0)'
        expectation: {kind: command_exit, expected_exit_code: 0}
  - id: A-04
    action: 'Desabilitar publish.yml'
    covers: [REQ-01]
    done_when: [C-04]
    depends_on: []
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'gh workflow list -R dex-agent/dex-code-review-graph --all (publish disabled)'
        expectation: {kind: command_exit, expected_exit_code: 0}
  - id: A-05
    action: 'CODEOWNERS minimo'
    covers: [REQ-01]
    done_when: [C-05]
    depends_on: []
    evidence_requirements:
      - id: ER-05
        proves: [C-05]
        method: command
        procedure: 'git show HEAD:.github/CODEOWNERS'
        expectation: {kind: command_exit, expected_exit_code: 0}
  - id: A-06
    action: 'Fechar ISSUE-0005 + INDEX + receipt'
    covers: [REQ-01]
    done_when: [C-05]
    depends_on: [A-01, A-02, A-03, A-04, A-05]
    evidence_requirements:
      - id: ER-06
        proves: [C-05]
        method: command
        procedure: 'rg "status" .agents/TRACKER/issues/0005-dependencia-dependabot-orfaos.md'
        expectation: {kind: command_exit, expected_exit_code: 0}
closure_gates:
  - 'Cada mutacao com receipt executavel; sem Release publicado; CI intocado'
gates:
  - 'preflight.mjs verde no Trilho antes da execucao'
risks:
  - 'Fechar PRs e reversivel (reopen); alerts ligados podem gerar ruido futuro — aceito pelo laudo'
uncertainties:
  - 'Run 44529405896 (classe 12) ainda em curso — fechamento da classe 12 ocorre na notificacao do watch, independente deste bloco'
validation:
  - 'receipts no corpo do ISSUE-0005'
execution_prompt: |
  /GOAL Bloco 0005: 4 mutacoes do laudo com receipt por passo.
---

# Bloco 0005 — fecha o ciclo do laudo da auditoria

## Checklist visual
- [x] A-01 — 5 PRs fechados com razão
- [x] A-02 — dependabot.yml sem version-updates (commit)
- [x] A-03 — vulnerability-alerts ON (204)
- [x] A-04 — publish.yml disabled
- [x] A-05 — CODEOWNERS pushed
- [x] A-06 — ISSUE-0005 fechado + INDEX + receipt
