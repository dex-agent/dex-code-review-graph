---
dex_contract: spt
version: 3
status: 'RASCUNHO'
owner: 'sprinter / mantenedor CRG'
date: '2026-11-14'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'GO do usuário ao piloto recomendado pelo Dex no Slack.'
goal:
  id: 'crg-piloto-segundo-windows-20261114'
  title: 'Validar wheel do CRG em um segundo Windows'
  objective: 'Reproduzir o wheel exato do CRG em outro Windows com checkout limpo, índice descartável, prova CLI e SQL e suíte separada.'
context: 'O PREDATOR já comprovou o wheel. Repetir em outro Windows discrimina dependências locais.'
problem: 'Falta prova independente do wheel, da CLI e da associação direta em outro Windows.'
decision: 'Fixar o hash anteriormente promovido e usar um checkout limpo da referência Git em índice descartável.'
scope:
  include:
    - 'Artefato exato, ambiente isolado e evidências versionadas em repo privado CRG.'
  exclude:
    - 'Código do produto, índice persistente, MCP, remoto do Dex WhatsApp e publicação pública.'
requirements:
  - id: REQ-01
    statement: 'Fixar e ensaiar o pacote'
    criteria:
      - id: C-01
        statement: 'O wheel exato e o checkout limpo estão prontos e o procedimento foi ensaiado localmente.'
  - id: REQ-02
    statement: 'Executar no segundo Windows'
    criteria:
      - id: C-02
        statement: 'O host Windows distinto confirma o wheel, o PATH, quick_check, HEAD, inventário e TESTED_BY direto.'
  - id: REQ-03
    statement: 'Registrar suíte e fechar'
    criteria:
      - id: C-03
        statement: 'O log da suíte do segundo Windows e o fechamento foram registrados separadamente.'
plan:
  - 'Fixar e ensaiar o pacote'
  - 'Executar no segundo Windows'
  - 'Registrar suíte e fechar'
tasks:
  - id: A-01
    action: 'Fixar e ensaiar o pacote'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Conferir o SHA256, criar bundle do HEAD de referência e ensaiar o verificador e a suíte em saídas distintas.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-02
    action: 'Executar no segundo Windows'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Executar o verificador no segundo Windows acessível e reabrir os recibos.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-03
    action: 'Registrar suíte e fechar'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Conferir o exit code e resumo da suíte, versionar bloco e avisar Dex.'
        expectation:
          kind: boolean_assertion
          expected: true
closure_gates:
  - 'Commit e push por bloco fechado. Piloto pronto somente com prova de segundo Windows.'
risks:
  - 'Execução local no PREDATOR prova apenas o procedimento.'
uncertainties:
  - 'Peers Windows conhecidos aparecem offline. Aguardar rota indicada pelo Dex ou disponibilidade verificável.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'SHA-256, Windows identificado, CLI do PATH, quick_check, Git e TESTED_BY SQL, log de suíte separado.'
execution_prompt: |
  /GOAL
  Execute o piloto do segundo Windows até o veredito.
---

# Piloto do CRG em um segundo Windows

- [x] A-01 — Fixar e ensaiar o pacote. [Recibo do grafo](../receipts/CRG-PILOTO-SEGUNDO-WINDOWS-20261114/rehearsal-graph.json) e [recibo da suíte](../receipts/CRG-PILOTO-SEGUNDO-WINDOWS-20261114/rehearsal-suite.json).
- [ ] A-02 — Executar no segundo Windows.
- [ ] A-03 — Registrar suíte e fechar.

Bloqueio de A-02 confirmado pelo Dex no Slack em 2026-11-14. O próximo passo
do Dex é disponibilizar um segundo Windows com acesso autorizado para executar
o [roteiro do piloto](../receipts/CRG-PILOTO-SEGUNDO-WINDOWS-20261114/INDEX.md).
