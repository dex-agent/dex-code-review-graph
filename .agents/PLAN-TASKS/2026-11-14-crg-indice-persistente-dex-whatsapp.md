---
dex_contract: spt
version: 3
status: 'RASCUNHO'
owner: 'sprinter / mantenedor CRG'
date: '2026-11-14'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'GO do usuário CRG-INDICE-PERSISTENTE-20261114.'
goal:
  id: 'crg-indice-persistente-dex-whatsapp-20261114'
  title: 'Adotar índice persistente Dex WhatsApp'
  objective: 'Validar e adotar o índice SQLite persistente do Dex WhatsApp com a CLI do PATH, sem interferir em uso concorrente e com rollback verificado.'
context: 'A CLI do PATH já tem a correção. O banco habitual servia a saída anterior.'
problem: 'Mesmo HEAD pode coexistir com parser antigo e associação direta ausente.'
decision: 'Validar cópia isolada, proteger a troca com exclusão SQLite e manter backup verificável.'
scope:
  include:
    - 'Índice habitualmente resolvido, candidato, rollback e evidência local.'
  exclude:
    - 'Interrupção de processos, alteração de código, MCP, commits e remoto.'
requirements:
  - id: REQ-01
    statement: 'Medir alvo e preparar rollback'
    criteria:
      - id: C-01
        statement: 'O backup consistente passa quick_check e reproduz o estado anterior em um ensaio.'
  - id: REQ-02
    statement: 'Reconstruir e validar candidato'
    criteria:
      - id: C-02
        statement: 'O candidato íntegro concorda com Git, arquivos CommonJS e associação direta na CLI e no SQL.'
  - id: REQ-03
    statement: 'Adotar e verificar pelo caminho habitual'
    criteria:
      - id: C-03
        statement: 'A CLI habitual e o SQL confirmam a mesma associação do candidato após promoção protegida.'
  - id: REQ-04
    statement: 'Fechar o corte'
    criteria:
      - id: C-04
        statement: 'Evidência, mapas e estado de retomada permitem recuperar a operação e o rollback.'
plan:
  - 'Medir alvo e preparar rollback'
  - 'Reconstruir e validar candidato'
  - 'Adotar e verificar pelo caminho habitual'
  - 'Fechar o corte'
tasks:
  - id: A-01
    action: 'Medir alvo e preparar rollback'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Resolver PATH e banco habitual, medir checkout, sidecars e processos, usar SQLite backup e ensaiar restauração.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-02
    action: 'Reconstruir e validar candidato'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Rodar build da CLI do PATH com índice isolado no checkout observado, comparar caminhos, hashes, SHA e TESTED_BY.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-03
    action: 'Adotar e verificar pelo caminho habitual'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Rever disponibilidade sem interromper processos, obter exclusão SQLite, promover e repetir CLI e SQL. Restaurar com readback se houver divergência.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-04
    action: 'Fechar o corte'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Salvar recibos, marcar checklist e rodar fiscal de fechamento.'
        expectation:
          kind: boolean_assertion
          expected: true
closure_gates:
  - 'Checklist 100 por cento após provas e goal_verdict registrado. Bloqueio real preserva candidato.'
risks:
  - 'Writer, leitor ou WAL ativo. O acesso à base permanece intacto se o gate de disponibilidade falhar.'
uncertainties:
  - 'O checkout tem mudanças anteriores. O aceite registra HEAD e os hashes dos arquivos reais.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'PRAGMA quick_check nos bancos, Git HEAD, inventário e hashes e teste pela CLI e SQL.'
execution_prompt: |
  /GOAL
  Execute o Trilho CRG-INDICE-PERSISTENTE-20261114 sem push.
---

# CRG-INDICE-PERSISTENTE-20261114

- [x] A-01 — Medir alvo e preparar rollback. [Prova](../receipts/CRG-INDICE-PERSISTENTE-20261114/backup.json).
- [x] A-02 — Reconstruir e validar candidato. [Prova](../receipts/CRG-INDICE-PERSISTENTE-20261114/candidate.json).
- [x] A-03 — Adotar e verificar pelo caminho habitual. [Prova](../receipts/CRG-INDICE-PERSISTENTE-20261114/promotion.json).
- [x] A-04 — Fechar o corte. [Prova](../receipts/CRG-INDICE-PERSISTENTE-20261114/INDEX.md).
