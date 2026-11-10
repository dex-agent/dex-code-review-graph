---
dex_contract: spt
version: 3
status: 'CONCLUIDO_COM_RESSALVAS'
owner: 'sprinter'
date: '2026-11-09'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO integral do dono sobre a recomendação do Oráculo TDD para uninstall'
goal:
  id: 'crg-iu1-uninstall-mode-20261109'
  title: 'Preservar o modo efetivo no uninstall'
  objective: 'Preservar o modo efetivo da configuração no teste de uninstall e fechar o último RED Windows de crg-iu1'
context: 'O corte Spring encerrou com um único ID de falha na suíte integral Windows.'
problem: 'O teste compara com um modo POSIX solicitado sem observar o modo efetivo na preparação.'
decision: 'Provar o ponto da divergência antes de editar a asserção existente, com cobertura Windows.'
scope:
  include:
    - 'Teste de uninstall, seleção CI Windows, provas descartáveis, mapas e fechamento de crg-iu1.'
  exclude:
    - 'Alterar escritor sem prova de perda real, ACLs, arquivo somente leitura como entrada e release.'
requirements:
  - id: REQ-01
    statement: 'Preservar o RED e medir o modo real'
    criteria:
      - id: C-01
        statement: 'O baseline localiza a divergência de modo antes da substituição'
  - id: REQ-02
    statement: 'Corrigir a expectativa de preservação do modo'
    criteria:
      - id: C-02
        statement: 'O teste nominal passa e detecta perda de modo nos dois sistemas'
  - id: REQ-03
    statement: 'Revisar a fronteira de escrita e cobrir o Windows na CI'
    criteria:
      - id: C-03
        statement: 'O módulo integral de uninstall passa nas duas plataformas'
  - id: REQ-04
    statement: 'Publicar o SHA e fechar o saldo de crg-iu1'
    criteria:
      - id: C-04
        statement: 'O recibo do corte comprova CI Windows nominal e zero IDs na suíte integral'
plan:
  - 'Preservar o RED e medir o modo real'
  - 'Corrigir a expectativa de preservação do modo'
  - 'Revisar a fronteira de escrita e cobrir o Windows na CI'
  - 'Publicar o SHA e fechar o saldo de crg-iu1'
tasks:
  - id: A-01
    action: 'Preservar o RED e medir o modo real'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Rodar pytest tests/test_uninstall.py::test_atomic_config_replace_preserves_file_mode com JUnit nos dois sistemas e executar sonda descartável pela API uninstall.run para comparar o modo inicial, após chmod e após uninstall, JSON, erros e temporários.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Corrigir a expectativa de preservação do modo'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Capturar stat.S_IMODE depois da preparação, exigir modo de grupo no POSIX e comparar o modo após uninstall. Rodar o teste nominal em ambos e injetar alteração de modo após replace real para provar que a asserção reprova.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Revisar a fronteira de escrita e cobrir o Windows na CI'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Selecionar tests/test_uninstall.py no job Windows existente. Rodar o módulo completo nos dois sistemas, conferir os controles fsync e replace, o teste de escopo da CLI, ruff e git diff --check.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Publicar o SHA e fechar o saldo de crg-iu1'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Publicar o SHA de produto, conferir o log do passo uninstall e os nove jobs, rodar JUnit integral Windows e comparar por ID com o corte Spring. Fechar o bead se o saldo for zero, publicar Dolt e validar o readback. Reconciliar mapas e continuidade, conferir checklist-lint e preparar prova para o veredito.'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Checklist visual 4/4, provas vinculadas, goal_verdict, checkout terminal e publicação do recibo no Git.'
risks:
  - 'Comparar valor pedido ao valor observado dá falso RED. Capturar modo independente antes da ação.'
  - 'Uma comparação tautológica ou skip reduz cobertura. O controle de mutação deve falhar na asserção.'
uncertainties:
  - 'A suíte integral e o runner Windows ainda precisam confirmar o saldo do SHA corrigido.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'Pytest com JUnit, sonda em NTFS e filesystem Linux, ruff, git diff --check, GitHub Actions e Dolt.'
execution_prompt: |
  /GOAL
  Execute .agents/PLAN-TASKS/2026-11-09-crg-iu1-uninstall-mode.md em C:\CodexProjetos\code-review-graph até o veredito.
---

# Preservar o modo efetivo no uninstall

Tipo: SPEC-PLAN-TASKs

Oráculo TDD no comando, Sprinter no plano, Clara no checklist, Chato e Vigia na fiscalização e Ponytail no escopo. Executor e owner do bead: mantenedor CRG. Fonte dos quality_gates: ppirtv-workflow/PATTERNS.md, ppirtv-flow-base e receita local de manutenção iterativa.

## SPEC

Preservar o modo efetivo do arquivo gravável e o conteúdo da entrada não CRG. No POSIX, provar que a fixture estabelece `0o640`. Se o diagnóstico basal observar diferença entre o modo efetivo antes e depois, devolver ao Sprinter antes de editar. O cenário principal usa o sistema de arquivos real. O Chato exige uma contraprova da asserção e mantém os controles vizinhos de falha.

## Checklist visual

- [x] A-01 [AÇÃO] Preservar o RED e medir o modo real | owner: mantenedor CRG | when: após goal_start | evidence: [RED](../receipts/crg-iu1-uninstall-mode/red-windows.xml), [Windows](../receipts/crg-iu1-uninstall-mode/baseline-windows.json), [Ubuntu](../receipts/crg-iu1-uninstall-mode/baseline-ubuntu.json), `evd_20261110005433669_0602_0122` | source: crg-iu1
- [x] A-02 [AÇÃO] Corrigir a expectativa de preservação do modo | owner: mantenedor CRG | when: após A-01 | evidence: [GREEN Windows](../receipts/crg-iu1-uninstall-mode/green-windows.xml), [GREEN Ubuntu](../receipts/crg-iu1-uninstall-mode/green-ubuntu.xml), [contraprova Windows](../receipts/crg-iu1-uninstall-mode/negative-windows.json), [contraprova Ubuntu](../receipts/crg-iu1-uninstall-mode/negative-ubuntu.json), `evd_20261110005453131_0603_0124` | source: crg-iu1
- [x] A-03 [AÇÃO] Revisar a fronteira de escrita e cobrir o Windows na CI | owner: mantenedor CRG | when: após A-02 | evidence: [módulo Windows](../receipts/crg-iu1-uninstall-mode/module-windows.xml), [módulo Ubuntu](../receipts/crg-iu1-uninstall-mode/module-ubuntu.xml), `evd_20261110005517485_0604_0126` | source: crg-iu1
- [x] A-04 [AÇÃO] Publicar o SHA e fechar o saldo de crg-iu1 | owner: mantenedor CRG | when: após A-03 | evidence: [CI](../receipts/crg-iu1-uninstall-mode/ci.json), [log nominal Windows](../receipts/crg-iu1-uninstall-mode/ci-windows-uninstall.txt), [saldo integral](../receipts/crg-iu1-uninstall-mode/comparison.json), [handoff](../receipts/crg-iu1-uninstall-mode/handoff.json) | source: crg-iu1

## Fundamento

Kent Beck, TDD Desenvolvimento Guiado por Testes, PDF p. 9 e 22, ciclo e RED observável. Casa do Código, Teste e Design no Mundo Real, seção 10.2, PDF p. 132–133, dependência concreta para provar integração. Limites de chmod Windows conferidos na referência Python 3.12. Reusar CRG-UV-WSL-VENV-ISOLADO.

## Revisão causal e lapidação antes do GOAL

- A-01 → REQ-01 → C-01 → ER-01. O mantenedor obtém JUnit nas duas plataformas e mede o mesmo arquivo antes e depois da entrada pública. O exit zero do discriminador exige o RED nominal esperado e preservação do modo efetivo.
- A-02 → REQ-02 → C-02 → ER-02. Pytest mede o resultado nominal. A mutação pós-replace roda só na fixture e deve falhar na asserção de modo em ambos os sistemas.
- A-03 → REQ-03 → C-03 → ER-03. Os JUnit integrais do módulo exercitam controles de falha existentes e escopo da CLI. O diff e o lint confirmam a seleção no workflow.
- A-04 → REQ-04 → C-04 → ER-04. Git identifica o SHA, Actions observa o runner, JUnit mede o saldo por ID e Dolt relê o fechamento. O veredito e a publicação de seu recibo vêm depois da prova e são gates de encerramento.

Revisão A–E apta, com estrutura conferida, cadeias sem órfãos, critérios com testemunha, produtores disponíveis e comandos reproduzíveis. Chato exige contraprova da igualdade. Ponytail mantém a mudança no teste existente e no job. Vigia limita o resultado ao arquivo gravável e conserva os dois ambientes separados.

`runtime_semantics_scope: static_referential_integrity`, `structural_status: pass`, `causal_semantics_reviewed: true`, `semantic_status: pass`, `goal_start_readiness: ready`.

## Fechamento

Fluxo `flow_20261110005352147_0595_0114`, produto `f5fb25d` publicado. CI 9/9, módulo Windows 46/46 e caso nominal aprovado. Suíte integral Windows: 2.326 aprovados, 12 skips, 2 XPASS e zero IDs de falha. Saiu somente o ID de modo do uninstall. Bead `crg-iu1` fechado e publicado no Dolt.

O teste usa configuração gravável em ambiente descartável. ACLs e arquivo originalmente somente leitura ficam fora da prova. Antes do release Windows, o mantenedor valida um wheel em instalação Windows limpa e prova versão e execução CLI sobre uma fixture descartável. [Veredito](../receipts/crg-iu1-uninstall-mode/verdict.json).
