---
dex_contract: spt
version: 3
status: 'CONCLUIDO'
owner: 'sprinter / Paula Planeja (ordem "troca" do dono 2026-11-16)'
date: '2026-11-16'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'Ordem "troca" do dono (combinada no fechamento do corte 2.4.0-dex): promover o wheel 2.4.0+dex.1 ao PATH com receipt e rollback documentados'
goal:
  id: 'crg-240dex-path-troca-20261116'
  title: 'Promocao do wheel 2.4.0+dex.1 ao PATH'
  objective: 'Substituir o executavel do PATH (2.4.0-oficial PyPI) pelo wheel combinado 2.4.0+dex.1 com provas das joias da casa e rollback documentado'
context: 'Corte 2.4.0-dex concluido 2026-11-15 (verdict vrd_20261115233016729_0849_0001 pronto_com_ressalvas; push 3ddf2c8b). Wheel local dist-240dex/code_review_graph-2.4.0+dex.1-py3-none-any.whl. PATH atual: ~/.local/bin/code-review-graph = 2.4.0 oficial (uv tool, PyPI, sem recibo). Nenhum processo serve ativo na janela (conferido via Get-CimInstance). Gotcha conhecido do AGENTS.md: instancias serve do Codex travam o executavel — se travar, exigira liberacao/restart antes de repetir. Rollback: uv tool install --force code-review-graph==2.4.0 (PyPI) OU wheel casa 7f2f9b60 (kit crg-2w-extracao).'
problem: 'O PATH executa o 2.4.0 oficial sem as joias da casa (merge-check, detect-changes --files, PHP identidade) e sem recibo de origem'
decision: 'uv tool install --force do wheel local 2.4.0+dex.1 com verificacoes deterministicas e receipt versionado'
scope:
  include:
    - 'instalacao do wheel 2.4.0+dex.1 via uv tool no PATH'
    - 'verificacao: versao, --files, merge-check, doctor, build descartavel schema 15'
    - 'receipt .agents/receipts/CRG-240DEX-PATH-20261116 com rollback documentado'
    - 'atualizacao de ACTIVE/HANDOFF/memoria + commit/push'
  exclude:
    - 'migracao ou abertura de indices persistentes schema-9 (projetos reconstroem; Dex WhatsApp descartavel por ordem do dono)'
    - 'promocao do adapter a rota permanente de review da casa (item X-01 separado)'
requirements:
  - id: REQ-01
    statement: 'PATH executando 2.4.0+dex.1 com joias comprovadas'
    criteria:
      - id: C-01
        statement: 'code-review-graph --version exibe 2.4.0+dex.1'
      - id: C-02
        statement: 'detect-changes expoe --files e o subcomando merge-check existe no executavel do PATH'
      - id: C-03
        statement: 'build descartavel de banco novo registra schema_version 15 pelo executavel do PATH'
  - id: REQ-02
    statement: 'Troca rastreavel e reversivel'
    criteria:
      - id: C-04
        statement: 'receipt com estado anterior, comando executado, saida e rotas de rollback versionado no repo'
plan:
  - 'A-01 instalar wheel via uv tool --force'
  - 'A-02 verificar C-01..C-03'
  - 'A-03 receipt + docs + memoria + commit/push'
tasks:
  - id: A-01
    action: 'uv tool install --force do wheel local 2.4.0+dex.1'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'code-review-graph --version -> 2.4.0+dex.1'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Verificar joias e schema pelo executavel do PATH'
    covers: [REQ-01]
    done_when: [C-02, C-03]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'code-review-graph detect-changes --help | grep --files; code-review-graph merge-check --help'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'build descartavel em fixture temporaria + consulta schema_version=15'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Receipt com rollback + superficies + commit/push'
    covers: [REQ-02]
    done_when: [C-04]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'git show do receipt versionado no main'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Memoria: pendencia PATH da memoria do merge marcada paga'
  - 'Indices: ACTIVE/HANDOFF atualizados'
  - 'Git: commit + push concluidos'
risks:
  - 'Executavel travado por instancia serve do Codex — mitigacao: janela conferida sem travadores; se travar, registrar bloqueio e rotear liberacao antes de repetir (nunca forcar)'
  - 'Primeira abertura de indice schema-9 mig-ra para 15 — mitigacao: excluso do escopo; projetos reconstroem'
uncertainties:
  - 'uv pode rejeitar versao local com + em ambientes restritivos; se ocorrer, rota alternativa: pip install --force do wheel na venv do uv tool (documentada no receipt)'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'node C:/CodexProjetos/dex-PPIRTV/spt-kit/preflight.mjs <este trilho>'
execution_prompt: |
  /GOAL
  Executar a troca do PATH para 2.4.0+dex.1 no workspace C:\CodexProjetos\code-review-graph:
  install uv tool, verificacoes (versao, --files, merge-check, schema 15), receipt com
  rollback, docs, memoria, commit e push.
---

# Promoção do wheel 2.4.0+dex.1 ao PATH (ordem "troca")

SPT-simples da ordem "troca" (2026-11-16), pendência do corte 2.4.0-dex.

## Checklist visual

- [x] A-01 — wheel instalado no PATH: `code-review-graph --version` → **2.4.0+dex.1** (C-01)
- [x] A-02 — joias + schema 15 pelo executável do PATH: `--files` ✓ · `merge-check` ✓ · banco descartável **schema 15** ✓ · e2e `tests_for(soma)`=1 ✓ (C-02, C-03)
- [x] A-03 — receipt [CRG-240DEX-PATH-20261116](../receipts/CRG-240DEX-PATH-20261116/INDEX.md) com rollback + docs + memória + commit/push (C-04)
