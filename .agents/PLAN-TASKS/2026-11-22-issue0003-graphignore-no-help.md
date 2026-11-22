---
dex_contract: spt
version: 3
status: 'CONCLUIDO'
owner: 'paula-planeja-spt'
date: '2026-11-22'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'GO-CONTINUO do dono (lote de issues com SPT individual; lote #2 após o corte 0.1.21 do dex-memoria) pagando a ISSUE-LOCAL-0003 (P3, aberta 2026-11-17 pelo custo pago ao vivo pelo consumidor do registry de skills)'
goal:
  id: 'issue0003-graphignore-descobrivilidade-240dex3'
  title: 'Descobribilidade do .code-review-graphignore no --help de build/update/forget (2.4.0+dex.3)'
  objective: 'Tornar a exclusão de indexação visível na superfície onde o usuário procura (help do comando), fechando a ISSUE-LOCAL-0003 sem mecanismo novo'
context: 'repo main 8dbb6c45 limpo=origin (fork casa 2.4.0+dex.2 instalado no PATH); capacidade EXISTE e funciona (incremental.py l.814/l.831 carrega .code-review-graphignore; evidência do item: −86% nós/−73% arquivos/−67% físico no registry 698 skills); consumidor real procurou por flags no --help e NÃO achou; conselheiro oraculo-clean-code selou (Boundaries l.3035-3037: fronteira invisível = usuário reimplementa o que a ferramenta controla); padrão de teste existente: tests/test_cli_help.py com cli.build_parser() + format_help()'
problem: 'O --help de build/update/forget não menciona o arquivo .code-review-graphignore — a capacidade só é descobrível lendo o README/docs'
decision: 'Constante única _GRAPHIGNORE_NOTE + description= nos 3 subparsers (build/update/forget); linha cita sintaxe gitignore, raiz do repo e âncora docs/USAGE.md#ignore-patterns; bônus doctor (reportar inchaço markup) fica FORA do corte — item opcional, mecanismo novo sem consumidor medido neste escopo'
scope:
  include:
    - 'constante de help + description nos subparsers build/update/forget em code_review_graph/cli.py'
    - 'teste novo em tests/test_cli_help.py: format_help() dos 3 comandos menciona .code-review-graphignore (RED antes, GREEN depois)'
    - 'suíte pytest do repo verde + release do fork 2.4.0+dex.3 (uv build + uv tool install --force)'
    - 'TRACKER 0003 → integrado + estado vivo (ACTIVE/INDEX)'
  exclude:
    - 'mecanismo de doctor para inchaço markup (bônus opcional do item; sem consumidor medido)'
    - 'filtro de linguagem no código (o item explicitamente NÃO pede)'
    - 'mudança de comportamento de indexação (só superfície de help)'
requirements:
  - id: REQ-01
    statement: 'Help de build/update/forget menciona a exclusão'
    criteria:
      - id: C-01
        statement: 'format_help() de build, update e forget contém .code-review-graphignore (teste novo RED antes da cura, GREEN depois)'
  - id: REQ-02
    statement: 'Fork promovido e item fechado'
    criteria:
      - id: C-02
        statement: 'suíte de testes relevante verde (pytest exit 0)'
      - id: C-03
        statement: 'binário 2.4.0+dex.3 instalado no PATH com a linha nova no build --help'
      - id: C-04
        statement: 'TRACKER 0003 com status integrado e INDEX atualizado'
plan:
  - 'A-01: teste RED (help dos 3 comandos sem graphignore) arquivado'
  - 'A-02: cura (constante + description) + GREEN + pytest'
  - 'A-03: release 2.4.0+dex.3 (uv build + install --force) + PATH confere'
  - 'A-04: TRACKER 0003 integrado + estado vivo + verdict'
tasks:
  - id: A-01
    action: 'Provar RED: teste novo em tests/test_cli_help.py falha porque nenhum dos 3 helps menciona .code-review-graphignore'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'pytest tests/test_cli_help.py -k graphignore → 1 falha (RED) com saída arquivada em .agents/EVIDENCIAS/2026-11-22-issue0003/'
        expectation:
          kind: command_exit
          expected_exit_code: 1
  - id: A-02
    action: 'Cura: _GRAPHIGNORE_NOTE + description nos subparsers build/update/forget em cli.py; GREEN + suíte'
    covers: [REQ-01, REQ-02]
    done_when: [C-01, C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-01]
        method: command
        procedure: 'pytest tests/test_cli_help.py (GREEN) + pytest tests/ suíte relevante exit 0'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Promover fork: uv build + uv tool install --force; conferir binário'
    covers: [REQ-02]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'code-review-graph --version mostra 2.4.0+dex.3 e code-review-graph build --help mostra a linha do graphignore'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Fechar: TRACKER 0003 integrado + INDEX/ACTIVE + commit/push + verdict + memórias do lote'
    covers: [REQ-02]
    done_when: [C-03, C-04]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'git log com commit do corte + TRACKER INDEX com 0003 integrado + push origin main'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'RED antes da cura (vacina VACINA-DECLARADA-NAO-EXECUTADA)'
  - 'binário promovido confere no PATH (não só working copy — lição 0006)'
  - 'TRACKER 0003 + estado vivo na mesma sessão'
risks:
  - 'description de subparser pode alterar teste existente de banner/help — mitigação: rodar tests/test_cli_help.py inteiro e vizinhos (tests/test_cli_surface.py)'
  - 'wheel uv pode carregar versão local fora de padrão — mitigação: seguir o fluxo 2.4.0+dex.N do 0006 (uv build + uv tool install --force)'
uncertainties:
  - 'se oforget faz sentido na mesma linha (pedido diz idealmente) — decidido: entra, o esquecimento de nós também é afetado pelo que é indexável'
gates:
  - 'preflight.mjs exit 0 na criação e no fechamento (MCP spt_validate ausente nesta janela — preflight local + validação semântica com evidência)'
validation:
  - 'node C:/CodexProjetos/dex-PPIRTV/spt-kit/preflight.mjs .agents/PLAN-TASKS/2026-11-22-issue0003-graphignore-no-help.md'
  - 'pytest tests/test_cli_help.py + suíte relevante'
  - 'code-review-graph --version + build --help pós-instalação'
execution_prompt: |
  /GOAL
  Executar o Trilho .agents/PLAN-TASKS/2026-11-22-issue0003-graphignore-no-help.md no workspace C:\CodexProjetos\code-review-graph na ordem A-01..A-04: RED, cura de help em 3 subparsers, release 2.4.0+dex.3, TRACKER 0003 integrado e verdict. Lote #2 do GO-CONTINUO; conselheiro oraculo-clean-code já selou o desenho (Boundaries).
---

# ISSUE-LOCAL-0003 — descobribilidade do `.code-review-graphignore` no `--help`

**Tipo:** SPEC-PLAN-TASKs · **Owner:** paula-planeja-spt (Trilho) / sessão (execução)
**Origem:** GO-CONTINUO do dono (lote #2). Perguntas base pagas: item 0003 relido na íntegra + código (incremental.py l.814/l.831; cli.py l.1930/l.1966/l.2140) + padrão de teste (tests/test_cli_help.py) + conselheiro clean-code (Boundaries, selo documental).

## TASKs (checklist visual)

### A-01 · RED
- [x] Teste novo falha: nenhum help de build/update/forget menciona graphignore — `pytest tests/test_cli_help.py -k graphignore` → 1 failed (RED em `.agents/EVIDENCIAS/2026-11-22-issue0003/RED-graphignore-help.txt`)

### A-02 · Cura + GREEN
- [x] _GRAPHIGNORE_NOTE + description nos 3 subparsers; pytest verde — 11/11 em test_cli_help.py (GREEN arquivado); vizinhos: merge_check 8/8; opt-in cli_surface preexistentemente vermelho por ambiente (stash provou) — dívida irmã aberta como ISSUE-LOCAL-0007 (merge-check fora da tabela)

### A-03 · Fork 2.4.0+dex.3
- [x] uv build + uv tool install --force; PATH confere com a linha nova — `code-review-graph --version` = 2.4.0+dex.3; linha visível em build/update/forget --help (contagens 1/1); CHANGELOG +dex.3 (e +dex.2 registrada retroativamente)

### A-04 · Fechamento
- [x] TRACKER 0003 integrado + estado vivo + commit/push + verdict — INDEX com 0003 integrado + 0007 aberto; item com bloco Desfecho; ACTIVE atualizado

## goal_verdict

**PRONTO** — checklist visual 100% (A-01..A-04 com saídas reais).

- **C-01** ✓ RED (1 failed) → GREEN (11/11) em `tests/test_cli_help.py::test_indexing_help_mentions_graphignore`
- **C-02** ✓ suítes relevantes verdes (cli_help 11/11 + merge_check 8/8); ressalva declarada: suíte opt-in `-m cli_surface` preexistentemente vermelha no ambiente Windows (stash na árvore limpa prova — mesma falha), dívida irmã ISSUE-LOCAL-0007
- **C-03** ✓ binário 2.4.0+dex.3 no PATH com a linha nos 3 helps (provado com o executável instalado, não o working copy — lição 0006)
- **C-04** ✓ TRACKER 0003 com Desfecho + INDEX integrado (+ 0007 aberto para o achado irmão)

Ressalvas: bônus do doctor fora do corte (mecanismo novo sem consumidor medido); CHANGELOG +dex.2 registrada retroativamente (o corte 0006 não a tinha lançado).

Créditos: conselheiro **oraculo-clean-code** (selo documental Boundaries l.3035-3037 — fronteira invisível no help = usuário reimplementa o que a ferramenta controla), **chato** (E se? do stash: provar preexistência antes de atribuir os 15 failures à cura — foi isso que poupou o corte de caçar fantasma), **burrinha** (E se o usuário só rodar --help raiz? — fluxo real do consumidor desce ao comando; help raiz fica limpo).
