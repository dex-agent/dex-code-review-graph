---
dex_contract: spt
version: 3
status: 'RASCUNHO'
owner: 'sprinter / mantenedor CRG'
date: '2026-11-14'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'Pedido direto CRG-PACOTE-SEGUNDO-WINDOWS-20261114 após CRG-GATES-UPSTREAM-20261114.'
goal:
  id: 'crg-pacote-segundo-windows-20261114'
  title: 'Preparar e testar o ZIP do CRG para o segundo Windows'
  objective: 'Entregar um ZIP local da base vencedora, aceito após extração, instalação limpa, testes e rollback no PREDATOR.'
context: 'O wheel verificado inclui merge-check e ajuste UTF-8. O pacote anterior contém checkout privado e outro wheel.'
problem: 'Carlos precisa executar a validação com fixture sintética sem afetar a instalação habitual.'
decision: 'Empacotar wheels fixados, dependências Windows e verificador autossuficiente com índices novos.'
scope:
  include:
    - 'ZIP local, dependências, licenças, fixture sintética, provas, rollback e prompts.'
  exclude:
    - 'Checkout de outro repo, promoção ao PATH, MCP habitual, índice habitual, segundo host, remoto, transferência e push.'
requirements:
  - id: REQ-01
    statement: 'Fixar composição licenciada'
    criteria:
      - id: C-01
        statement: 'Wheel aprovado e rollback conferidos por SHA-256, manifesto e wheelhouse local verificáveis.'
  - id: REQ-02
    statement: 'Montar ZIP autossuficiente'
    criteria:
      - id: C-02
        statement: 'Instalação e rollback isolados, fixture, gates, suíte separada, instruções e dois prompts incluídos.'
  - id: REQ-03
    statement: 'Provar ZIP extraído'
    criteria:
      - id: C-03
        statement: 'Instalação limpa e verificações no PREDATOR com esperado real, hashes e limites publicados apenas localmente.'
plan:
  - 'Fixar composição licenciada'
  - 'Montar ZIP autossuficiente'
  - 'Provar ZIP extraído'
tasks:
  - id: A-01
    action: 'Fixar composição licenciada'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Wheel aprovado e rollback conferidos por SHA-256, manifesto e wheelhouse local verificáveis.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-02
    action: 'Montar ZIP autossuficiente'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Instalação e rollback isolados, fixture, gates, suíte separada, instruções e dois prompts incluídos.'
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-03
    action: 'Provar ZIP extraído'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Instalação limpa e verificações no PREDATOR com esperado real, hashes e limites publicados apenas localmente.'
        expectation:
          kind: boolean_assertion
          expected: true
closure_gates:
  - 'SHA externo, relatos saneados, ZIP pronto somente após o ensaio do pacote extraído.'
risks:
  - 'Mesmo número de versão em dois wheels exige comprovante por hash.'
uncertainties:
  - 'Segundo host será exercitado por Carlos; este corte mede Windows x64 no PREDATOR.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes do goal_start.'
validation:
  - 'Manifesto, instalação offline, verificador CLI SQLite, gates, suíte e rollback da cópia extraída.'
execution_prompt: |
  /GOAL
  Empacote e verifique localmente a base vencedora sem transferência ou push.
---

# CRG-PACOTE-SEGUNDO-WINDOWS-20261114

- [x] A-01 — Fixar composição. [Dependências e hashes](../receipts/CRG-PACOTE-SEGUNDO-WINDOWS-20261114/staging/DEPENDENCIAS.md).
- [x] A-02 — Montar pacote. [ZIP e SHA externo](../receipts/CRG-PACOTE-SEGUNDO-WINDOWS-20261114/INDEX.md).
- [x] A-03 — Provar extração, instalação e rollback. [Recibos](../receipts/CRG-PACOTE-SEGUNDO-WINDOWS-20261114/INDEX.md).
