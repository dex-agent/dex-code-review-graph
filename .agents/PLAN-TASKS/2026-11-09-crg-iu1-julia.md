---
dex_contract: spt
version: 3
status: 'CONCLUIDO_COM_RESSALVAS'
owner: 'sprinter'
date: '2026-11-09'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO explicito do dono apos recomendacao do Oraculo SOLID para crg-iu1'
goal:
  id: 'crg-iu1-julia-20261109'
  title: 'Portabilidade dos testes Julia'
  objective: 'Tornar portaveis os 27 casos Julia e comprovar a remocao exata dos 13 IDs Windows sem novas falhas'
context: 'Em 186259e o saldo Windows era 21 IDs, 13 da familia Julia; a prova previa em copia passou 27 em cada sistema.'
problem: 'A fixture produz caminhos nativos e as expectativas assumem separador POSIX.'
decision: 'Derivar a expectativa do Path de entrada e incluir o arquivo no job windows-native existente.'
scope:
  include:
    - 'Arquivo de testes Julia, job Windows existente, provas, mapas e continuidade'
  exclude:
    - 'Parser produtivo, banco persistente e oito IDs residuais esperados'
requirements:
  - id: REQ-01
    statement: 'Fixar baseline cruzado'
    criteria:
      - id: C-01
        statement: 'O comparador confirma os 13 IDs Julia em RED no Windows e os 27 em GREEN no Ubuntu'
  - id: REQ-02
    statement: 'Manter identidade qualificada e habilitar CI nativa'
    criteria:
      - id: C-02
        statement: 'O verificador de diff e contraprovas aceita o recorte e rejeita origens adulteradas'
  - id: REQ-03
    statement: 'Provar paridade da suite Julia'
    criteria:
      - id: C-03
        statement: 'O comparador JUnit confirma 27 aprovacoes sem skips por sistema'
  - id: REQ-04
    statement: 'Medir a regressao por conjunto'
    criteria:
      - id: C-04
        statement: 'O verificador confirma o delta integral e a CI verde no commit do patch'
  - id: REQ-05
    statement: 'Deixar o saldo retomavel'
    criteria:
      - id: C-05
        statement: 'O verificador reabre mapas e continuidade e confirma o saldo no bead'
plan:
  - 'Baseline, patch e revisao adversarial, teste cruzado, CI e suite integral, mapas e handoff'
tasks:
  - id: A-01
    action: 'Preservar o RED Julia por ID'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Rodar pytest -p no:cacheprovider --junitxml para tests/test_julia_reconciliation.py nos dois sistemas e comparar com o saldo anterior. Recibo baseline.json.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Corrigir expectativas e revisar identidade'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Rodar ruff check, git diff --check e duas contraprovas na assercao exata; conferir a selecao Windows em .github/workflows/ci.yml. Recibo change.json.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Testar os 27 casos nos dois sistemas'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Rodar pytest -p no:cacheprovider --junitxml sobre o arquivo corrigido no Windows e Ubuntu e comparar os IDs. Recibo focused.json.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Confirmar suite integral e CI publicada'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Rodar pytest integral em Windows 3.13 e comparar conjuntos por ID; consultar jobs e log pytest -v da etapa Julia no GitHub Actions pelo SHA. Recibo comparison.json.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-05
    action: 'Reconciliar mapas e continuidade'
    covers: [REQ-05]
    done_when: [C-05]
    depends_on: [A-04]
    evidence_requirements:
      - id: ER-05
        proves: [C-05]
        method: command
        procedure: 'Reabrir fontes e hashes dos mapas de capacidade, decisoes e dependencias e validar ACTIVE, HANDOFF e bd show crg-iu1. Recibo handoff.json.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Checklist 5/5, goal_verdict, checkout terminal, mapas, Git e Dolt publicados'
risks:
  - 'Um resultado verde pode esconder identidade enfraquecida; preservar arquivo e escopo e testar dois alvos errados.'
uncertainties:
  - 'O saldo integral e os jobs devem ser observados no SHA publicado.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'pytest com JUnit, ruff check, git diff --check e leitura dos jobs GitHub por SHA'
execution_prompt: |
  /GOAL
  Execute .agents/PLAN-TASKS/2026-11-09-crg-iu1-julia.md no workspace C:\CodexProjetos\code-review-graph ate o verdict.
---

# Portabilidade dos testes Julia no Windows e Ubuntu

Tipo: SPEC-PLAN-TASKs

Owner: mantenedor CRG. Fonte: GO do dono, diagnóstico do Oráculo SOLID, saldo de crg-iu1 e código de teste. Fonte dos quality_gates: ppirtv-workflow/PATTERNS.md, ppirtv-flow-base, e a receita de manutenção iterativa do projeto.

## SPEC, PLAN e riscos

O único motivo de mudança é a expectativa do caminho no teste. O capítulo SRP de Martin (2002, fulltext linha 2633) embasa a separação. O custo de abstração do OCP (linha 2890) embasa manter o contrato de identidade produtivo. O teste precisa rejeitar outro arquivo e outro escopo. Fixar o caminho de entrada dá independência do resultado produzido pelo parser. O banco persistente passa pelo gatilho de staleness antes de qualquer consumo futuro.

## TASKs — checklist visual

- [x] A-01 [AÇÃO] Preservar o RED Julia por ID | owner: mantenedor CRG | quando: após goal_start | prova: [baseline.json](../receipts/crg-iu1-julia/baseline.json), `evd_20261109064043766_0420_0397`
- [x] A-02 [AÇÃO] Corrigir expectativas e revisar identidade | owner: mantenedor CRG | quando: após A-01 | prova: [change.json](../receipts/crg-iu1-julia/change.json), `evd_20261109064142964_0421_0399`
- [x] A-03 [AÇÃO] Testar os 27 casos nos dois sistemas | owner: mantenedor CRG | quando: após A-02 | prova: [focused.json](../receipts/crg-iu1-julia/focused.json), `evd_20261109064226716_0427_0407`
- [x] A-04 [AÇÃO] Confirmar suite integral e CI publicada | owner: mantenedor CRG | quando: após A-03 | prova: [comparison.json](../receipts/crg-iu1-julia/comparison.json), `evd_20261109064736695_0434_0416`
- [x] A-05 [AÇÃO] Reconciliar mapas e continuidade | owner: mantenedor CRG | quando: após A-04 | prova: [handoff.json](../receipts/crg-iu1-julia/handoff.json), `evd_20261109064802454_0435_0418`

## Validação semântica e revisão do Trilho

- A-01 → REQ-01 → C-01 → ER-01. Pytest/JUnit nos ambientes disponíveis, em fontes idênticas, fornece IDs e estados. O comparador aceita os 13 REDs do histórico no Windows e 27 GREENs Ubuntu.
- A-02 → REQ-02 → C-02 → ER-02. Git e Ruff conferem o escopo. A contraprova injeta em memória outro caminho e outro escopo, exige falha na asserção do primeiro caso e preserva os nós observados.
- A-03 → REQ-03 → C-03 → ER-03. Pytest/JUnit do arquivo corrigido observa aprovação por ID nos dois sistemas, inclusive os 14 controles, sem skips.
- A-04 → REQ-04 → C-04 → ER-04. O comparador usa os IDs Windows e a API de CI no SHA publicado. Uma etapa pytest verbosa no job Windows entrega os 27 IDs no log, sem novo job ou artefato externo.
- A-05 → REQ-05 → C-05 → ER-05. O mantenedor reabre fontes, hashes, continuidade e Beads. A verificação é independente dos estados declarados no checklist.

SPT Revisor A–E apto após lapidação da prova CI. Chato exigiu teste negativo por arquivo e por escopo, igualdade dos IDs e leitura remota por SHA. Ponytail preserva parser e indexador, usa uma constante de fixture e o job existente. `runtime_semantics_scope=static_referential_integrity`, `causal_semantics_reviewed=true`, `goal_start_readiness=ready`.

## Progresso observado

- Flow `flow_20261109063944151_0413_0389`. A revisão está vinculada ao escopo dos dois arquivos e ao fingerprint da implementação.
- Patch `9f1f19b` publicado no main privado. A suíte Windows integral registrou 8 falhas, 2.316 aprovações, 12 skips e 2 xpasses. A-04 exige também os 27 IDs no [run do SHA publicado](https://github.com/dex-agent/dex-code-review-graph/actions/runs/42574737872).
- A leitura do log confirmou os 27 IDs Julia aprovados, sem skips. O run inteiro passou 9/9. As três contraprovas rejeitaram arquivo errado, escopo errado e autochamada.

## Encerramento

Checklist 5/5. Checkout completo sem bloqueios. Veredito `vrd_20261109064902297_0441_0426` pronto com ressalvas. [Recibo](../receipts/crg-iu1-julia/verdict.json).

O Oráculo SOLID separou a identidade que o parser produz da representação esperada pela fixture. Ponytail manteve o corte em dois arquivos. O Chato comprovou que a asserção negativa detecta a autochamada e que a positiva rejeita dois alvos errados.

Retomar crg-iu1 pelos três casos de _match_files_to_forget. Reproduzir o caso de caminho absoluto e os dois vizinhos em Windows e Ubuntu, comparar caminho armazenado, raiz e padrão normalizado, depois confirmar o conjunto exato pela CLI forget --dry-run em índice descartável antes de editar. Owner mantenedor CRG, antes do próximo release Windows.
