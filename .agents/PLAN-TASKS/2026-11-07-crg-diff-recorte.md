---
dex_contract: spt
version: 3
status: 'RASCUNHO'
owner: 'sprinter'
date: '2026-11-07'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'GO do usuario para corrigir o vazamento de changed_files'
goal:
  id: 'crg-diff-recorte-20261107'
  title: 'Corrigir o recorte do diff'
  objective: 'Restringir os simbolos alterados ao recorte de arquivos solicitado no Code Review Graph.'
context: 'Receita local manutencao iterativa e evidencia CRG-DIFF-RECORTE-VAZA.'
problem: 'Faixas Git fora de changed_files contam como simbolos alterados.'
decision: 'Aplicar o recorte na selecao compartilhada em analyze_changes.'
scope:
  include:
    - 'Seletor de faixas, consumidores pertinentes, testes e evidencias locais.'
  exclude:
    - 'Reparar descoberta geral de fluxos, Graphify e publicar remotamente.'
requirements:
  - id: REQ-01
    statement: 'Preservar a regressao executavel'
    criteria:
      - id: C-01
        statement: 'O teste parametrizado reproduz o vazamento antes da correcao.'
  - id: REQ-02
    statement: 'Corrigir o seletor compartilhado'
    criteria:
      - id: C-02
        statement: 'O teste parametrizado respeita o recorte solicitado.'
  - id: REQ-03
    statement: 'Validar os consumidores'
    criteria:
      - id: C-03
        statement: 'A suite focada da analise de mudancas passa.'
plan:
  - 'Preparar ambiente e preservar RED nos casos A+B e somente B.'
  - 'Corrigir a selecao por arquivo com fallback preservado.'
  - 'Revisar CLI/MCP e provar a saida dos consumidores.'
tasks:
  - id: A-01
    action: 'Preservar a regressao executavel'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'uv run --no-sync pytest -q tests/test_changes.py -k requested_file_ranges'
        expectation:
          kind: command_exit
          expected_exit_code: 1
  - id: A-02
    action: 'Corrigir o seletor compartilhado'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'uv run --no-sync pytest -q tests/test_changes.py -k requested_file_ranges'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Validar os consumidores'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'uv run --no-sync pytest -q tests/test_changes.py'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Checklist com provas, revisao SOLID e verdict oficial.'
risks:
  - 'Faixas fora do recorte nao podem reativar fallback de arquivo inteiro.'
uncertainties:
  - 'A prova local nao comprova deploy no runtime MCP instalado.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'uv run --no-sync pytest -q tests/test_changes.py'
execution_prompt: |
  /GOAL
  Execute este Trilho em C:/CodexProjetos/code-review-graph.
---

# Corrigir o recorte do diff no CRG

Tipo: SPEC-PLAN-TASKs

## SPEC

Diff com A e B, recorte A: apenas simbolos de A. Diff apenas em B, recorte A: zero simbolos. Sem faixas disponiveis, preservar fallback. Baseline historico 268e0e1 e d007bc1.

## PLAN

RED antes da implementacao. Centralizar a selecao sem duplicar politica; SRP de Martin 2002, capitulo 8, linhas 2633 e 2695 do corpus. Revisar consumidores e revalidar. Reverter somente o diff do corte se houver regressao. Refresh persistente do indice, se ocorrer, publica os tres mapas; fixtures isoladas sao evidencias de teste.

## TASKs

- [x] A-01 — RED: 2 falhas pelo símbolo b | evidence: evd_20261107232708982_0087_0009
- [x] A-02 — GREEN: mesmos 2 casos passaram | evidence: evd_20261107232729841_0088_0011
- [x] A-03 — Suite: 38 passaram; dois consumidores em grafo isolado | evidence: evd_20261107232802211_0089_0013

## Riscos e gates

Chato: e se o filtro esvaziar o mapa? A saida deve ter zero simbolos. E se paths forem relativos? Comparar identidades na raiz. Ponytail: uma politica no analisador. Meta-analise antes do verdict e do fechamento, com prova, impacto e retorno quando necessario.

## Validacao

Comandos e expectativas no contrato acima. PPI: planejamento Sprinter, checklist Clara, revisao SPT e fiscal Chato.

Revisão de entrada: preflight achados=0; spt_validate v3 válido e elegível; causal_semantics_reviewed=true, goal_start_readiness=ready. RED distingue assert de erro de coleta; GREEN usa as mesmas entradas; suíte e smoke usam Git e banco locais. SPT Revisor e Ponytail: apto; caso sem mudança no recorte é explícito, sem novo filtro em cada consumidor.

Meta-análise final: Martin, livro 2002, SRP l.2633 e l.2695, extrações 0101–0120 e 0121–0140 reabertas; PDF SHA-256 8F0FC1EC8A8182BDEBDB50217D9D470EBD34C169A9DBD31FD5246D509C9AA51F. E se o filtro esvaziar as faixas? O smoke prova zero sem fallback. Decisão: manter uma política na seleção compartilhada. Impacto: detect_changes e contexto mínimo verificados, fallback preservado pela suíte. Próximo SPT desta missão: N/A. Risco residual: serviço MCP instalado ainda requer promoção própria. Owner: mantenedor, quando publicar a correção. Evidência: revisão evd_20261107232838696_0095_0021.

Histórico: [três mapas](../MAPAS/INDEX.md). Flow: flow_20261107232627051_0080_0001.

Fechamento oficial: `complete`, sem bloqueios, veredito `pronto_com_ressalvas` `vrd_20261107233038858_0102_0030`. Revisão fiscal selecionada: `evd_20261107233031378_0101_0028`. A mineração oficial tentada após o avanço terminal retornou `FLOW_TERMINAL_IMMUTABLE`; memória causal já recuperável por CRG-DIFF-RECORTE-VAZA.

## Execucao

/GOAL: seguir o contrato v3 deste arquivo.
