---
dex_contract: spt
version: 3
status: CONCLUIDO
owner: sprinter
date: '2026-11-08'
workspace: 'C:/CodexProjetos/code-review-graph'
origin: 'Pedido do dono para criar repo privado e organizar a casa'
goal:
  id: crg-repo-privado-higiene-20261108
  title: Organizar e publicar a edicao privada CRG
  objective: Preservar fontes e evidencias uteis, separar estado local e publicar a edicao da casa em repositorio privado.
context: 'Checkout com upstream publico, dois commits locais e estado misturado.'
problem: 'Backups de configuracao e runtime concorrem com fontes curadas no inventario Git.'
decision: 'Preservar historico upstream, usar origin privado e ignorar estado especifico da maquina.'
scope:
  include:
    - 'Classificacao, regras Git, continuidade, documentacao e publicacao privada.'
  exclude:
    - 'Instalacao global do MCP e regeneracao de grafos historicos.'
requirements:
  - id: REQ-01
    statement: Separar conteudo curado e estado local
    criteria:
      - id: C-01
        statement: Configuracoes locais e backups sensiveis ficam fora do stage e continuam preservados no disco.
  - id: REQ-02
    statement: Preservar correcao e governanca
    criteria:
      - id: C-02
        statement: Testes de changes passam e os registros de continuidade apontam o corte atual.
  - id: REQ-03
    statement: Publicar privadamente
    criteria:
      - id: C-03
        statement: Repositorio remoto privado tem o mesmo HEAD do checkout e origin/main sem divergencia.
plan:
  - Inventariar e classificar antes de alterar.
  - Aplicar exclusoes e reconciliar fontes de entrada.
  - Testar, commitar, publicar e reler o remoto.
tasks:
  - id: A-01
    action: Separar conteudo curado e estado local
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: inspection
        procedure: Conferir git check-ignore e git ls-files, sem imprimir valores de configuracao.
        expectation:
          kind: boolean_assertion
          expected: true
  - id: A-02
    action: Preservar correcao e governanca
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: uv run --no-sync pytest -q tests/test_changes.py
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: Publicar privadamente
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: inspection
        procedure: Comparar git rev-parse HEAD, git ls-remote origin refs/heads/main e API private=true.
        expectation:
          kind: boolean_assertion
          expected: true
closure_gates:
  - 'Stage revisado, diff check, testes e readback privado.'
risks:
  - 'Backup local contem credencial historica. Preservar no lugar e excluir da publicacao.'
uncertainties:
  - 'Rotacao da credencial historica depende do dono da conta.'
gates:
  - 'Validar contrato antes de executar alteracoes.'
validation:
  - 'Testes, check de playbook e readback remoto.'
execution_prompt: |
  /GOAL Execute todas as tasks deste Trilho em C:/CodexProjetos/code-review-graph.
---

# Organizar a edicao privada CRG

Tipo: SPEC-PLAN-TASKs

## SPEC

Owner da execucao e fechamento Git e a sessao atual. Origem preservada em upstream. Destino privado dex-agent/dex-code-review-graph. Nenhum dado local e descartado.

## PLAN

Garimpo por categorias. Configuracao, backups, transacoes e bancos sao estado local. Fontes, testes, mapas e recibos selecionados compoem o corte versionado. Reusar os CLIs de higiene e fechamento existentes.

## TASKs

- [x] A-01 — exclusoes e preservacao no disco verificadas, stage sem padrao de segredo. Prova `evd_20261108131350755_0114_0009`.
- [x] A-02 — 38 testes e Ruff verdes, continuidade reconciliada. Prova `evd_20261108131350810_0115_0011`.
- [x] A-03 — Git e API confirmam private=true e SHA e326cfd49ebdca79f82b479e5932423f716b680e igual ao checkout. Prova `evd_20261108131413211_0116_0013`.

## Riscos e gates

Chato pergunta se um ignore esconderia evidencia util. Resposta: permitir explicitamente as fontes curadas e manter o restante no disco, com classificacao recuperavel. Ponytail recomenda manter a arvore upstream e um documento curto da edicao. E se a autenticacao gh estiver vazia? Usar o credential manager existente sem expor segredo.

## Validacao

Revisao causal da entrada: cada task produz o criterio associado. ER-01 protege os dados locais, ER-02 verifica o comportamento ja corrigido, ER-03 prova o destino real. goal_start_readiness=ready; causal_semantics_reviewed=true. SPT Revisor e Ponytail: desenho apto com readback e sem descarte.

## Execucao e meta-analise final

Flow `flow_20261108130638616_0107_0001`. Bead `crg-pr9` fechado. Git publicou a correcao em `b987efa` e a organizacao em `e326cfd`. O CLI Beads gerou automaticamente `8b1b76c` e `e391cec` ao trocar o remoto de sincronizacao. O primeiro tambem capturou as remocoes do indice ja preparadas, preservando os dois arquivos no disco. Diff desses commits conferido. Dolt push concluiu depois da inicializacao do main remoto.

Chato e Ponytail conferiram origem, destino, escopo e recuperabilidade. Achado concreto foi o backup com credencial, excluido e preservado. O aviso de path do README foi interrogado na fonte e corresponde a exemplos genericos. E se o ignore ocultar fonte util? A allowlist inclui Trilhos, mapas e recibos escolhidos; todos os alvos dos INDEX versionados foram conferidos. E se o Git mostrar limpo com lixo local? O inventario bruto continua em receipts locais e a classificacao esta em docs/EDICAO-DEX.md. Nenhum arquivo local foi descartado.

Fiscal sem RED mecanico. Modo strict mantem tres categorias nao avaliadas pelo auto-discovery e um aviso P1 de credencial; nao foi declarado verde integral. Avaliacao de receita recomenda reusar fechamento-corte no proximo corte, sem criar outro pacote. CI remoto retornou zero runs, portanto a prova de teste deste corte e local. Risco residual de produto: runtime MCP instalado ainda anterior ao fix. Proxima acao unica de seguranca: dono da conta confirma rotacao antes de reutilizar a credencial historica. Promocao MCP segue no ledger para o mantenedor.

Fechamento oficial em 2026-11-08: checklist 3/3, verdict `vrd_20261108131605649_0126_0025` com status `pronto_com_ressalvas`, flow `complete` e blockers vazios. Revisao `evd_20261108131538075_0121_0019`. Garimpo resolveu seis candidatos como ledger-only por serem estados operacionais ja rastreados, com zero novas memorias fracas/duplicadas. A consolidacao documental deste fechamento recebe commit proprio apos o verdict.
