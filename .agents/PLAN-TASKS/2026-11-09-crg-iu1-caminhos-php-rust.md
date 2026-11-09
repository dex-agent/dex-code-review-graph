---
dex_contract: spt
version: 3
status: 'CONCLUIDO_COM_RESSALVAS'
owner: 'sprinter'
date: '2026-11-09'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO do dono apos recomendacao do Oraculo Pragmatico para crg-iu1'
goal:
  id: 'crg-iu1-caminhos-20261109'
  title: 'Tornar portaveis os tres testes de caminho PHP e Rust'
  objective: 'Provar tres testes de caminho PHP e Rust no Windows e Ubuntu, obrigatorios na CI Windows e reconciliados com o baseline'
context: 'crg-iu1 tem 24 IDs Windows preexistentes. Os tres selecionados expuseram separadores e setup da fixture.'
problem: 'O job Windows atual passa sem selecionar os tres IDs, que falham na suite local.'
decision: 'Corrigir a selecao da fixture e a comparacao dos caminhos nos testes, preservando o nome qualificado e ativando a selecao CI.'
scope:
  include:
    - 'Dois arquivos de teste, workflow CI existente, baseline, provas e continuidade'
  exclude:
    - 'Resolver produtivo, banco persistente e demais IDs de crg-iu1'
requirements:
  - id: REQ-01
    statement: 'Fixar os tres IDs na revisao anterior'
    criteria:
      - id: C-01
        statement: 'O recibo pre-patch distingue tres falhas Windows e o controle Ubuntu'
  - id: REQ-02
    statement: 'Consertar fixture e assercoes de identidade'
    criteria:
      - id: C-02
        statement: 'A prova qualificada rejeita o homonimo e a CI Windows seleciona os tres IDs'
  - id: REQ-03
    statement: 'Provar resultado cruzado do corte'
    criteria:
      - id: C-03
        statement: 'Os mesmos tres IDs passam no Windows e no Ubuntu sem skip'
  - id: REQ-04
    statement: 'Medir delta real da regressao'
    criteria:
      - id: C-04
        statement: 'O conjunto de falhas Windows perde os tres IDs e a CI do commit publicado passa'
  - id: REQ-05
    statement: 'Deixar o corte e os residuos rastreaveis'
    criteria:
      - id: C-05
        statement: 'Mapas, continuidade e bead registram a evidencia e os casos restantes'
plan:
  - 'Preservar baseline nos dois sistemas'
  - 'Corrigir as provas de caminho e ativar os IDs no CI'
  - 'Validar os testes focados por ID'
  - 'Comparar a suite integral e confirmar CI publicada'
  - 'Registrar o saldo e a continuidade'
tasks:
  - id: A-01
    action: 'Preservar baseline nos dois sistemas'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Executar pytest dos tres IDs com JUnit no Windows 3.13 e no Ubuntu em copia Git da revisao base. Recibo baseline.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Corrigir as provas de caminho e ativar os IDs no CI'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Verificar diff e Ruff, executar contraprova com alvo concorrente em copia e conferir os node IDs no workflow. Recibo change.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Validar os testes focados por ID'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Executar pytest com JUnit e comparar os IDs, exercitando os controles vizinhos de namespace e PHPUnit. Recibo focused.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Comparar a suite integral e confirmar CI publicada'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Comparar o conjunto de falhas Windows 3.13 com os 24 IDs conhecidos e conferir os jobs por SHA no remoto. Recibo comparison.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-05
    action: 'Registrar o saldo e a continuidade'
    covers: [REQ-05]
    done_when: [C-05]
    depends_on: [A-04]
    evidence_requirements:
      - id: ER-05
        proves: [C-05]
        method: command
        procedure: 'Reabrir mapas, provas e estado de crg-iu1 e verificar os vinculos antes do verdict. Recibo handoff.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Checklist integral com provas reais, verdict oficial, checkout terminal e Git e Dolt publicados.'
risks:
  - 'Comparar fragmento ou so exit zero pode mascarar homonimo ou skip; exigir alvo completo e JUnit por ID.'
  - 'Suíte integral tem reds históricos; comparar por conjunto no mesmo ambiente, em vez de só contar.'
uncertainties:
  - 'O conjunto final precisa ser medido; o baseline historico tem 24 IDs.'
gates:
  - 'Preflight e spt_validate v3, revisao causal e SPT Revisor antes de goal_start.'
validation:
  - 'pytest com JUnit, ruff check, Git diff e readback GitHub Actions por SHA.'
execution_prompt: |
  /GOAL
  Execute .agents/PLAN-TASKS/2026-11-09-crg-iu1-caminhos-php-rust.md no workspace C:\CodexProjetos\code-review-graph ate o veredito.
---

# Provar caminhos PHP e Rust no Windows e no Ubuntu

Tipo: SPEC-PLAN-TASKs

Fonte dos quality_gates: manifesto de domínios, contratos da suíte pytest, workflow CI e baseline Windows de crg-x6m. Mantenedor CRG executa e publica o recorte, e mantém crg-iu1 aberto enquanto restarem IDs.

## Revisão causal e revisão do Trilho

A estrutura passou no preflight e no spt_validate v3. A semântica estática do runtime verifica vínculos. A revisão causal separada conferiu cada cadeia e os respectivos produtores.

- A-01 → REQ-01 → C-01 → ER-01. Pytest/JUnit preserva o resultado dos três IDs em Windows e Ubuntu antes de editar os testes. O recibo compara IDs, plataforma e revisão.
- A-02 → REQ-02 → C-02 → ER-02. A leitura do YAML prova a seleção de três IDs no job existente. O contracaso com homônimo em cópia precisa falhar na igualdade do destino qualificado.
- A-03 → REQ-03 → C-03 → ER-03. JUnit em Windows e Ubuntu prova três testes aprovados, sem skips. Os controles de namespace e PHPUnit cercam o corte.
- A-04 → REQ-04 → C-04 → ER-04. A suíte Windows 3.13 fornece o conjunto de falhas e a API de CI fornece jobs no SHA publicado. Exit não zero da suíte integral é observado e interpretado pelo comparador.
- A-05 → REQ-05 → C-05 → ER-05. Mapas e continuidade reabrem provas com hash e o bead registra os IDs restantes. O veredito e o push final são gates separados.

SPT Revisor A–E: apto. O Chato exigiu JUnit por ID, contraexemplo de homônimo e comparação de conjuntos. Ponytail reutiliza o job Windows, os testes existentes e o contrato de caminhos do resolvedor, com normalização somente na comparação dos testes. `runtime_semantics_scope=static_referential_integrity`, `causal_semantics_reviewed=true`, `goal_start_readiness=ready`.

## Checklist visual

- [x] A-01 [AÇÃO] Preservar baseline nos dois sistemas | owner: mantenedor CRG | quando: após goal_start | prova: [baseline.json](../receipts/crg-iu1-caminhos/baseline.json), `evd_20261109062147606_0393_0362`
- [x] A-02 [AÇÃO] Corrigir as provas de caminho e ativar os IDs no CI | owner: mantenedor CRG | quando: após A-01 | prova: [change.json](../receipts/crg-iu1-caminhos/change.json), `evd_20261109062306109_0394_0364`
- [x] A-03 [AÇÃO] Validar os testes focados por ID | owner: mantenedor CRG | quando: após A-02 | prova: [focused.json](../receipts/crg-iu1-caminhos/focused.json), `evd_20261109062349088_0395_0366`
- [x] A-04 [AÇÃO] Comparar a suite integral e confirmar CI publicada | owner: mantenedor CRG | quando: após A-03 | prova: [comparison.json](../receipts/crg-iu1-caminhos/comparison.json), `evd_20261109062939138_0401_0374`
- [x] A-05 [AÇÃO] Registrar o saldo e a continuidade | owner: mantenedor CRG | quando: após A-04 | prova: [handoff.json](../receipts/crg-iu1-caminhos/handoff.json), `evd_20261109063045106_0402_0376`

## Resultado observado

- Windows nativo e Ubuntu WSL. Os três IDs e os quatro controles passaram em cada ambiente, sem skips. Os três contracasos falharam ao exigir o destino qualificado correto.
- Em `f825c25`, os nove jobs da CI passaram, incluindo Windows. A suíte integral Windows 3.13 caiu de 24 para 21 falhas, com 2.303 aprovados e zero IDs novos.
- O Chato conferiu o resultado por ID, e Ponytail manteve a correção nos testes e no job existente. A lente do Oráculo Pragmático ligou a reprodução à contraprova e separou o corte concluído do saldo de `crg-iu1`.

## Encerramento

Checklist 5/5. Flow `flow_20261109062016039_0386_0354` completo, sem bloqueios, veredito `vrd_20261109063105983_0407_0382` pronto com ressalvas. [Recibo](../receipts/crg-iu1-caminhos/verdict.json).

Próximo corte sob `crg-iu1`. Retomar crg-iu1 pelo teste test_qualified_definitions_have_collision_free_identities em Windows nativo e Ubuntu no mesmo SHA. Capturar caminhos e identidades qualificadas e localizar a primeira divergência antes de editar, sob o mantenedor CRG antes do próximo release Windows.
