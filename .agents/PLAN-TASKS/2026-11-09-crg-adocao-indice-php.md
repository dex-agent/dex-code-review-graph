---
dex_contract: spt
version: 3
status: 'CONCLUIDO_COM_RESSALVAS'
owner: 'sprinter'
date: '2026-11-09'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO do dono para adotar a correcao PHP no indice persistente'
goal:
  id: 'crg-adocao-indice-php-20261109'
  title: 'Adotar a correcao PHP no indice ativo'
  objective: 'Reconstruir e adotar o indice CRG do checkout com rollback ensaiado e associacao direta comprovada pelo consumidor habitual'
context: 'crg-x6m corrigiu o produto e provou Payments em fixtures separadas.'
problem: 'O indice ativo registrou c3682ac enquanto o checkout ja inclui fb9fc22.'
decision: 'Construir no mesmo checkout com armazenamento separado e adotar a imagem validada pelo mecanismo transacional do SQLite.'
scope:
  include:
    - 'Banco efetivo, backup local, ensaio, promocao, recibos, mapas e continuidade'
  exclude:
    - 'Mudancas no produto e reconciliacao dos testes crg-iu1'
requirements:
  - id: REQ-01
    statement: 'Identificar o banco efetivamente selecionado pela CLI'
    criteria:
      - id: C-01
        statement: 'O status da CLI e o SQLite direto identificam o mesmo banco e SHA anterior'
  - id: REQ-02
    statement: 'Produzir um backup consistente e restauravel'
    criteria:
      - id: C-02
        statement: 'O backup e a restauracao ensaiada preservam a imagem logica do baseline'
  - id: REQ-03
    statement: 'Reconstruir em armazenamento isolado para o mesmo checkout'
    criteria:
      - id: C-03
        statement: 'O candidato no SHA alvo passa no controle semantico SQL e CLI e nas duas fixtures PHP'
  - id: REQ-04
    statement: 'Promover o candidato com exclusao de escritor e rollback'
    criteria:
      - id: C-04
        statement: 'A CLI habitual reabre o banco ativo e confirma o mesmo SHA e a associacao direta'
  - id: REQ-05
    statement: 'Registrar os tres mapas e deixar provas reabriveis'
    criteria:
      - id: C-05
        statement: 'Os mapas de capacidades, decisoes e dependencias apontam para as provas desta operacao'
plan:
  - 'Fixar a identidade do banco e o baseline'
  - 'Preservar e ensaiar a restauracao'
  - 'Construir e validar o candidato separado'
  - 'Adotar e reabrir pelo consumidor real'
  - 'Consolidar o fechamento operacional'
tasks:
  - id: A-01
    action: 'Fixar a identidade do banco e o baseline'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Executar a fase baseline do harness com a CLI do venv e SQLite somente leitura. Recibo: baseline.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Preservar e ensaiar a restauracao'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Executar a fase backup, comparar digest logico e integrity_check e testar uma segunda conexao escritora. Recibo: backup.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Construir e validar o candidato separado'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Executar a fase candidate que invoca build, status, tests_for, SQL e o reproducer do crg-x6m. Recibo: candidate.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Adotar e reabrir pelo consumidor real'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Executar a fase promote do harness, testar exclusao de escritor, reler o alvo pela CLI sem overrides e verificar a copia de rollback. Recibo: promotion.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-05
    action: 'Consolidar o fechamento operacional'
    covers: [REQ-05]
    done_when: [C-05]
    depends_on: [A-04]
    evidence_requirements:
      - id: ER-05
        proves: [C-05]
        method: command
        procedure: 'Validar os links e hashes dos tres mapas e registrar o checklist, com verdict e publicacao como gates de fechamento. Recibo: maps.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Checklist visual completo, verdict oficial, checkout terminal, fechamento Dex e publicacao dos documentos e recibos sanitizados.'
risks:
  - 'WAL e escritor concorrente: ensaiar exclusao numa copia, revalidar baseline sob lock e manter rollback.'
  - 'SHA verde e heuristica: exigir aresta exata e resultado publico direto, com fixture PHP separada.'
uncertainties:
  - 'A imagem ativa pode mudar ate a aquisicao do lock. O executor deve conferir antes de promover.'
gates:
  - 'Preflight, spt_validate, revisao causal e SPT Revisor antes de goal_start.'
validation:
  - 'Executar o harness com .venv/Scripts/python.exe -B e as fases baseline, backup, candidate e promote nesta ordem.'
  - 'Conferir os resultados pelo Git, status e query da CLI, consultas SQLite e hashes locais.'
execution_prompt: |
  /GOAL
  Execute .agents/PLAN-TASKS/2026-11-09-crg-adocao-indice-php.md no workspace C:\CodexProjetos\code-review-graph ate o veredito.
---

# Adotar a correção PHP no índice persistente

Tipo: SPEC-PLAN-TASKs

Fonte dos quality_gates: manifesto de domínios e controles operacionais do gatilho de staleness, crg-k4q e crg-x6m. O mantenedor CRG responde pelo banco, pelos recibos e pelo rollback. Os backups ficam fora do Git. Crg-iu1 segue separado.

O corte usa a associação direta de references_to como controle do projeto e as fixtures de Payments como prova PHP. A promoção transacional preserva o caminho e o registro do consumidor. Se o banco divergir do baseline antes da promoção, o executor preserva o banco encontrado e atualiza a caracterização antes de tentar novamente.

## Revisão antes do GOAL

O Sprinter revisou A–E com SPT Revisor e Ponytail. O Chato exigiu os negativos de concorrência e de homônimo, e a validação semântica separou o controle do checkout da fixture sintética. Estrutura v3 apta. Escopo do veredito estático do runtime: `static_referential_integrity`.

- A-01 → REQ-01 → C-01 → ER-01. CLI e leitura direta do metadado SQLite comparam o banco efetivo, Git e revisão persistida; o harness emite baseline.json.
- A-02 → REQ-02 → C-02 → ER-02. A API SQLite copia banco e backup, os checks comparam conteúdo lógico e integridade, e uma segunda conexão tenta escrever; backup.json registra o resultado.
- A-03 → REQ-03 → C-03 → ER-03. O build isolado gera banco para o checkout fixado. A CLI, o SQLite e o reprodutor PHP existente medem o resultado em candidate.json.
- A-04 → REQ-04 → C-04 → ER-04. O SQLite adota a imagem sob exclusão e o executável reabre o caminho habitual. A verificação independe do código que realiza a cópia. promotion.json comprova sucesso e retenção do backup.
- A-05 → REQ-05 → C-05 → ER-05. O executor gera os mapas e verifica os ponteiros e hashes contra o disco. maps.json comprova o inventário do corte.

Todos os critérios são avaliados pelo exit real da respectiva fase. `causal_semantics_reviewed=true`, `goal_start_readiness=ready`.

## Checklist visual

- [x] A-01 [AÇÃO] Fixar a identidade do banco e o baseline | owner: mantenedor CRG | quando: após goal_start | prova: [baseline.json](../receipts/crg-adocao-indice-php/baseline.json), `evd_20261109060554897_0361_0321`
- [x] A-02 [AÇÃO] Preservar e ensaiar a restauracao | owner: mantenedor CRG | quando: após A-01 | prova: [backup.json](../receipts/crg-adocao-indice-php/backup.json), `evd_20261109060606226_0362_0323`
- [x] A-03 [AÇÃO] Construir e validar o candidato separado | owner: mantenedor CRG | quando: após A-02 | prova: [candidate.json](../receipts/crg-adocao-indice-php/candidate.json), `evd_20261109060828403_0363_0325`
- [x] A-04 [AÇÃO] Adotar e reabrir pelo consumidor real | owner: mantenedor CRG | quando: após A-03 | prova: [promotion.json](../receipts/crg-adocao-indice-php/promotion.json), `evd_20261109060847334_0364_0327`
- [x] A-05 [AÇÃO] Consolidar o fechamento operacional | owner: mantenedor CRG | quando: após A-04 | prova: [maps.json](../receipts/crg-adocao-indice-php/maps.json), `evd_20261109061018475_0365_0329`

## Resultado operacional

O banco habitual saiu de `c3682ac` para `eeb486b`. O backup restaurou em cópia com o mesmo hash lógico e `integrity_check=ok`. O build isolado percorreu 265 arquivos. A adoção usou a transação da API SQLite sob lock exclusivo. Outra conexão recebeu `SQLITE_BUSY`, o daemon estava inativo e o executável habitual reabriu a imagem validada.

O SQLite manteve o nó `Test`, `is_test=1` e uma aresta qualificada `TESTED_BY` de `query_graph`. A CLI devolveu o teste de references_to com `indirect=false` e `inferred_by=null`. As duas fixtures PHP passaram separadamente com zero CALLS e TESTED_BY para Shipping.

**E se o candidato verde perder estado auxiliar?** O ensaio com banco vazio passou no controle da CLI e perdeu a tabela de embeddings. O candidato adotado foi semeado pelo backup. Ele preservou 4.745 linhas e 4.164 vetores byte a byte para fontes de hash igual. Vetores de fontes alteradas ficaram fora da prova. [Memória validada](../memorias/crg-rebuild-preserva-embeddings-no-candidato-isolad-ddbe87c32bec.md).

**Lentes ativas.** Feathers fundamenta a caracterização e a escolha do ponto de teste próximo da alteração, no corpus Bookman PT-BR 2013, caps. 2, 12 e 13, pp. 35, 181 e 189–191 do PDF, SHA-256 `fdb8b95669909e071d04b6d64e24a6e88b1f28702e1769a86eaa782f5e128b08`. Chato separou bloqueio real de escritor, hash, integridade, semântica e estado auxiliar. Ponytail reaproveitou o build e o teste PHP existentes, sem mudança no produto.

## Veredito

Bead `crg-dq9`. Checklist visual 5/5. O flow `flow_20261109060414853_0354_0313` encerrou sem bloqueios, com veredito `vrd_20261109061157643_0378_0345` pronto com ressalvas. [Recibo oficial](../receipts/crg-adocao-indice-php/verdict.json).

O mantenedor retoma `crg-iu1` antes do próximo release Windows. A checagem do frescor de embeddings nas fontes alteradas ficou no `crg-87w`, antes de usar o ranking semântico nessas fontes.
