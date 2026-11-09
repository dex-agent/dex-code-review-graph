---
dex_contract: spt
version: 3
status: 'CONCLUIDO_COM_RESSALVAS'
owner: 'sprinter'
date: '2026-11-08'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO do dono para executar crg-k4q com o Oraculo Clean Code'
goal:
  id: 'crg-k4q-frescor-2026-11-08'
  title: 'Frescor semantico do indice CRG'
  objective: 'Provar em indice isolado quando o update alinha o SHA e quando o rebuild reclassifica o teste PHPUnit'
context: 'O status da CLI registra o SHA do checkout. O bead crg-k4q investiga se isso implica reparse.'
problem: 'Update de arquivo alheio pode alinhar o SHA sem reclassificar um teste existente.'
decision: 'Isolar fixture Git, rodar revisoes reais pelo executavel e confrontar estado SQLite e JSON.'
scope:
  include:
    - 'Fixture isolada, script de reproducao, receipts, Trilho, continuidade e mapas'
  exclude:
    - 'Alterar o produto, o indice persistente e a instalacao da CLI'
requirements:
  - id: REQ-01
    statement: 'Construir o banco com o executavel carregando o parser anterior'
    criteria:
      - id: C-01
        statement: 'Construir o banco com o executavel carregando o parser anterior'
  - id: REQ-02
    statement: 'Atualizar exclusivamente um arquivo alheio com a CLI atual'
    criteria:
      - id: C-02
        statement: 'Atualizar exclusivamente um arquivo alheio com a CLI atual'
  - id: REQ-03
    statement: 'Criar e validar um backup SQLite anterior ao rebuild'
    criteria:
      - id: C-03
        statement: 'Criar e validar um backup SQLite anterior ao rebuild'
  - id: REQ-04
    statement: 'Reconstruir com a CLI atual e provar a associacao direta'
    criteria:
      - id: C-04
        statement: 'Reconstruir com a CLI atual e provar a associacao direta'
plan:
  - 'Construir o banco com o executavel carregando o parser anterior'
  - 'Atualizar exclusivamente um arquivo alheio com a CLI atual'
  - 'Criar e validar um backup SQLite anterior ao rebuild'
  - 'Reconstruir com a CLI atual e provar a associacao direta'
tasks:
  - id: A-01
    action: 'Construir o banco com o executavel carregando o parser anterior'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'Verificar origem do modulo antigo e comparar Git, status, no e aresta no snapshot baseline.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Atualizar exclusivamente um arquivo alheio com a CLI atual'
    covers: [REQ-02]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'Verificar um arquivo atualizado e SHA novo, preservando bytes do PHP alvo e a classificacao antiga em update.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Criar e validar um backup SQLite anterior ao rebuild'
    covers: [REQ-03]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'Reabrir a copia em modo read-only, conferir integrity_check, hash, metadado de SHA, no e aresta em backup.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Reconstruir com a CLI atual e provar a associacao direta'
    covers: [REQ-04]
    done_when: [C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'Manter HEAD e bytes do alvo, comparar no, aresta, JSON e hash do backup apos rebuild em rebuild.json'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Registrar rota operacional, mapas do indice isolado, continuidade, bead, Git e verdict.'
risks:
  - 'O status pode atualizar o SHA sem reprocessar arquivos intactos.'
  - 'Copia direta de SQLite pode omitir transacoes do WAL.'
uncertainties:
  - 'A reproducao cobre a fixture PHP e as duas revisoes medidas.'
gates:
  - 'Preflight e spt_validate verdes e revisao causal anterior ao goal_start.'
validation:
  - 'Executavel Windows e Git reais. SQLite somente leitura para inspecao. Backup SQLite com integrity_check.'
execution_prompt: |
  /GOAL
  Execute .agents/PLAN-TASKS/2026-11-08-crg-k4q-frescor-indice.md em C:\CodexProjetos\code-review-graph pela ordem e registre o verdict oficial.
---

# Frescor semântico do índice CRG

Tipo: SPEC-PLAN-TASKs

## SPEC e PLAN

O mantenedor CRG responde pela operação do índice. A CLI anterior e a atual usam o mesmo executável do venv e módulos importados de snapshots Git distintos. A fixture usa um único alvo PHP e um único teste camelCase, evitando homônimos e usando a aresta exata como oráculo. O banco e `CRG_HOME` ficam numa pasta temporária dedicada, com a cópia preservada localmente em receipts.

## Revisão semântica e do Trilho

A-01 liga a origem do parser ao nó antigo, com controle positivo posterior no mesmo arquivo. A-02 liga o commit Git de um único arquivo à saída de update e ao estado antigo. A-03 liga a API de backup à leitura independente em modo somente leitura. A-04 só compara os estados se o Git, a identidade e os bytes do alvo continuarem iguais após o rebuild. A evidência de cada fase é imutável. Chato exige aresta exata em SQL e resultado público sem inferência. Ponytail reutiliza o padrão Git archive, fixture temporária e leitura JSON já provados. Clean Code fundamenta o desenho controlado, enquanto Git e SQLite provam o caso CRG. causal_semantics_reviewed=true, goal_start_readiness=ready.

## Checklist visual

- [x] A-01 [AÇÃO] Construir o banco com o executavel carregando o parser anterior | owner: mantenedor CRG | quando: após goal_start | prova: [baseline.json](../receipts/crg-k4q/baseline.json), `evd_20261109022753579_0309_0255`
- [x] A-02 [AÇÃO] Atualizar exclusivamente um arquivo alheio com a CLI atual | owner: mantenedor CRG | quando: após A-01 | prova: [update.json](../receipts/crg-k4q/update.json), `evd_20261109022753625_0310_0257`
- [x] A-03 [AÇÃO] Criar e validar um backup SQLite anterior ao rebuild | owner: mantenedor CRG | quando: após A-02 | prova: [backup.json](../receipts/crg-k4q/backup.json), `evd_20261109022753666_0311_0259`
- [x] A-04 [AÇÃO] Reconstruir com a CLI atual e provar a associacao direta | owner: mantenedor CRG | quando: após A-03 | prova: [rebuild.json](../receipts/crg-k4q/rebuild.json), `evd_20261109022753709_0312_0261`

## Resultados e revisão do Chato

| Etapa | SHA Git e banco | Nó testAdd | Arestas para o par exato | CLI tests_for |
| --- | --- | --- | --- | --- |
| Build antigo `c3682ac` | `00dd248` | Function | 0 | vazio |
| Update atual de `src/Unrelated.php` | `5445efc` | Function | 0 | vazio |
| Backup SQLite read-only | `5445efc` gravado no banco | Function | 0 | leitura SQL |
| Rebuild atual `5ec4762` | `5445efc` | Test | 1 | `testAdd`, `indirect=false`, sem inferência |

O update informou um arquivo. Git e SHA-256 dos dois fontes PHP confirmaram que o alvo e seu teste ficaram intactos. O rebuild processou três arquivos. O backup abriu em modo somente leitura com `integrity_check=ok` e conservou o hash `2f7862cbfc640c1b02746c389989fdf65059027ef8afb2dcb182163fe646963f` após o rebuild. Cópia local excluída do Git.

**E se o SHA verde esconder um nó antigo?** O snapshot do update demonstra esse estado. **E se a consulta sugerir um teste pelo nome?** Compare a aresta SQLite entre os dois nomes qualificados e exija `inferred_by=null` no JSON. **E se o backup tiver omitido WAL?** A cópia usou a API SQLite e preservou o metadado e os nós do banco fonte.

O Oráculo usou a superfície `clean-code` e autenticou, na edição EN 2008, cap. 17, p. 314, T5–T6, o desenho de testar fronteiras e vizinhanças do defeito. A extração `range_0301_0360.md` localizou a passagem, e o PDF foi reaberto com SHA-256 `61949fc2bc46431fb6cc7a71a472ce4dbfbcec7a2277f538e8d7ae9722c5618e`. O comportamento do CRG foi provado pela execução.

A rota fica no [gatilho vivo](../GATILHOS-VIVOS.md#staleness-artefatos-derivados). O aprendizado reutilizável já existe em `CRG-INDEX-PARSER-SEMANTICS`. Os [mapas históricos](../MAPAS/INDEX.md) registram o alcance do experimento.

## Veredito

**Pronto com ressalvas**, `vrd_20261109023002598_0322_0273`. Flow `flow_20261109022540270_0302_0247` completo, checklist 4/4, cinco evidências e zero bloqueadores. [Readback oficial](../receipts/crg-k4q/verdict.json).

O índice persistente ficou fora do escopo. A regra de reclassificação é um procedimento operacional. Próximo corte recomendado: `crg-x6m`, provar que um import explícito não atribui CALLS ou TESTED_BY ao homônimo errado e que update e rebuild produzem a mesma aresta correta.
