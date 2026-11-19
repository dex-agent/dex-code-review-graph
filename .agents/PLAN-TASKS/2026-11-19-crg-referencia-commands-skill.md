---
dex_contract: spt
version: 3
status: 'CONCLUIDO'
owner: 'sessao:zcode (silencio do dono apos GO ofertado = segue o recomendado, acao reversivel)'
date: '2026-11-19'
workspace: 'C:/Users/Administrator/.agents/skills (registry) — Trilho mora no repo code-review-graph'
origin: 'ISSUE-LOCAL-0023 do TRACKER do registry (pedido direto do dono: referencia versionada dos 35 comandos DENTRO da skill code-review-graph)'
goal:
  id: 'crg-referencia-commands-na-skill-20261119'
  title: 'Reference versionada commands-v2.4.0-dex.1.md no pacote da skill + ponteiro com gate de bump + item 0023 fechado'
  objective: 'Executar o aceite do ISSUE-LOCAL-0023: a tabela dos 35 comandos com prompts modelos morando em references/ da skill, apontada do SKILL.md com versao declarada e gate de frescor no bump'
context: 'Governanta convocada (pre): roteamento anti-rascunho manda conteudo informacional em references/, SKILL.md so contrato; INDEX nao muda (sem impacto de descoberta); CHANGELOG obrigatorio'
problem: 'A lista dos comandos so existiu em conversa — janela fria regenera do zero; referencia sem versao envelhece mentindo'
decision: 'references/commands-v2.4.0-dex.1.md (nome de arquivo hifenizado, versao exata 2.4.0+dex.1 no conteudo) + 3 linhas de ponteiro na secao Versao da casa e schema + CHANGELOG + fechar 0023'
scope:
  include:
    - 'criar <skill>/references/commands-v2.4.0-dex.1.md com as 6 familias/35 comandos/prompts + regra de frescor'
    - 'apontar do SKILL.md (secao Versao da casa e schema) com versao e gate de bump'
    - 'entrada curta no CHANGELOG.md do registry'
    - 'fechar ISSUE-LOCAL-0023 (status/criterios/dialogo) + linha INDEX do TRACKER'
  exclude:
    - 'INDEX.md do registry (sem mudanca de descoberta); CAPACITY (foto de hoje ja tem a ponte projeto_fonte); Governance-Version (sem regra viva nova)'
requirements:
  - id: REQ-01
    statement: 'Referencia versionada viva dentro do pacote da skill, com gate de bump e item fechado'
    criteria:
      - id: C-01
        statement: 'references/commands-v2.4.0-dex.1.md existe com as 35 entradas e a versao exata 2.4.0+dex.1 declarada'
      - id: C-02
        statement: 'SKILL.md aponta a referencia com versao + gate de bump (mesma sessao do bump, --help contra a tabela)'
      - id: C-03
        statement: 'ISSUE-LOCAL-0023 fechado com receipt e INDEX do TRACKER atualizado'
plan:
  - 'A-01 criar a reference no pacote'
  - 'A-02 ponteiro no SKILL.md + CHANGELOG'
  - 'A-03 fechar 0023 + push + validacoes'
tasks:
  - id: A-01
    action: 'Criar references/commands-v2.4.0-dex.1.md'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'rg -c "2.4.0\\+dex.1" <skill>/references/commands-v2.4.0-dex.1.md (>=1) e wc -l (conteudo integral)'
        expectation: {kind: command_exit, expected_exit_code: 0}
  - id: A-02
    action: 'Ponteiro no SKILL.md + CHANGELOG do registry'
    covers: [REQ-01]
    done_when: [C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'rg -n "commands-v2.4.0-dex.1" <skill>/SKILL.md CHANGELOG.md'
        expectation: {kind: command_exit, expected_exit_code: 0}
  - id: A-03
    action: 'Fechar 0023 + push + validacoes'
    covers: [REQ-01]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'rg "status: fechado" TRACKER/issues/0023* + git push + validate-registry-catalog --fail-on-drift'
        expectation: {kind: command_exit, expected_exit_code: 0}
closure_gates:
  - 'Commit pushed com gates do pre-commit do registry verdes; referencia conferivel por rg'
gates:
  - 'preflight.mjs verde no Trilho antes da execucao'
risks:
  - 'Nome de arquivo com + seria hostil a ferramentas — resolvido: hifen no nome, versao exata no conteudo'
uncertainties:
  - 'validate-registry-catalog pode acusar drift pela edicao do pacote — se acusar, regenerar na mesma janela (regra da Governanta)'
validation:
  - 'rg de versao na reference + ponteiro no SKILL.md + push verde'
execution_prompt: |
  /GOAL Aceite do 0023: reference versionada na skill + ponteiro com gate + item fechado.
---

# Referência versionada dos 35 comandos na skill (ISSUE-LOCAL-0023)

## Checklist visual
- [x] A-01 — reference criada (35 comandos + versão exata)
- [x] A-02 — ponteiro no SKILL.md + CHANGELOG
- [x] A-03 — 0023 fechado + pushed + gates verdes

> FECHADO 2026-11-19: registry commits `b1a69ef9` (reference + ponteiro + re-foto G7 CAPACITY 0 findings + CHANGELOG 3.533.1 + 0023 fechado) e `88630196` (renumber colisão 0024→0027) e napkin `PUSH-PARALELO...`, todos pushed. Provas: rg versão (1 hit), ponteiro SKILL.md l.88, CHANGELOG l.22, status fechado l.4. Incidente paralelo resolvido: janela irmã publicou meu commit original antes do amend (napkin do registry documenta).
