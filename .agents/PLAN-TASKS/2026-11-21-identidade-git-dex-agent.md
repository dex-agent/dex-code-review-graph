---
dex_contract: spt
version: 3
status: 'CONCLUIDO'
owner: 'sessao:zcode (decisao do dono via quiz: "Reescrever tudo")'
date: '2026-11-21'
workspace: 'C:/CodexProjetos/code-review-graph + C:/Users/Administrator/.agents/skills (registry)'
origin: 'Correcao do dono: commits exibiam ultraflashlan (email ultraflash@flexworksolutions.shop no ~/.gitconfig global); correto e dex-agent <dex-agent@proton.me> (conta github.com/dex-agent; email JA vinculado — provado por commits existentes)'
goal:
  id: 'identidade-git-dex-agent-20261121'
  title: 'Identidade git da casa: config corrigido (feito) + historico reescrito nos 2 repos com commit-map preservado'
  objective: 'Todos os commits dos repos dex-agent/dex-code-review-graph e dex-agent/skills exibem autor dex-agent <dex-agent@proton.me>, com mapa velho->novo duravel para a rastreabilidade da casa'
context: 'Config global JA trocado (dex-agent@proton.me, efetivo em commits futuros de todas as janelas). Email antigo casa so nos OBJETOS de commit; upstream commits (autores de terceiros) NAO podem ser tocados — callback so casa o email antigo'
problem: 'Commits publicados exibem a conta errada (ultraflashlan) e o dono mandou corrigir o historico; forca-push muda hashes citados em memorias/TRACKER/receipts/flows'
decision: 'git filter-repo com email-callback (so ultraflash@flexworksolutions.shop -> dex-agent@proton.me) por repo; commit-map de cada repo preservado como receipt commitado; force-push com lease + tags; verificacao por gh api'
scope:
  include:
    - 'pre-condicoes: status limpo, sem worktrees ativas, URL do origin anotada (filter-repo a remove)'
    - 'CRG: filter-repo -> commit-map em .agents/receipts/rewrite-20261121/ -> re-add origin -> push --force-with-lease + --force tags (v2.4.0+dex.1 muda)'
    - 'registry: idem (historia inteira da casa muda; tags se houver)'
    - 'verificacao: gh api commits -> author.login == dex-agent nos 2 repos'
    - 'receipt do mapa commitado (novo hash estavel) + aviso a janelas paralelas (pull --rebase)'
  exclude:
    - 'commits do upstream (autores de terceiros) — callback nao casa com eles; regra: so o email antigo da casa e trocado'
requirements:
  - id: REQ-01
    statement: 'Historico reescrito com mapa preservado e verificado no remoto'
    criteria:
      - id: C-01
        statement: 'commits recentes dos 2 repos exibem author.login dex-agent (gh api)'
      - id: C-02
        statement: 'commit-map velho->novo commitado como receipt em cada repo'
      - id: C-03
        statement: 'tag v2.4.0+dex.1 re-empurrada apontando para o commit novo correspondente'
plan:
  - 'A-01 pre-condicoes e ferramenta (filter-repo instalado?)'
  - 'A-02 reescrita CRG + mapa + push + tag'
  - 'A-03 reescrita registry + mapa + push'
  - 'A-04 verificacao remota + receipt + avisos'
tasks:
  - id: A-01
    action: 'Pre-condicoes: status/worktrees/origin URLs/filter-repo'
    covers: [REQ-01]
    done_when: [C-01]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'git status limpo + git worktree list vazio + filter-repo disponivel'
        expectation: {kind: command_exit, expected_exit_code: 0}
  - id: A-02
    action: 'Reescrever CRG com mapa e push'
    covers: [REQ-01]
    done_when: [C-01, C-03]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-02
        proves: [C-01, C-03]
        method: command
        procedure: 'filter-repo commit-map salvo; push force-with-lease aceito; git ls-remote tag'
        expectation: {kind: command_exit, expected_exit_code: 0}
  - id: A-03
    action: 'Reescrever registry com mapa e push'
    covers: [REQ-01]
    done_when: [C-01, C-02]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-03
        proves: [C-01, C-02]
        method: command
        procedure: 'idem A-02 no registry'
        expectation: {kind: command_exit, expected_exit_code: 0}
  - id: A-04
    action: 'Verificar remoto + commitar mapas + avisos'
    covers: [REQ-01]
    done_when: [C-01, C-02]
    depends_on: [A-02, A-03]
    evidence_requirements:
      - id: ER-04
        proves: [C-01]
        method: command
        procedure: 'gh api commits?per_page=5 -> todos author.login == dex-agent'
        expectation: {kind: command_exit, expected_exit_code: 0}
closure_gates:
  - 'Commits do upstream intocados (callback restrito); mapas duraveis; verificacao por API'
gates:
  - 'preflight.mjs verde antes de executar'
risks:
  - 'Janelas paralelas com base velha: mitigacao = aviso no fechamento + mapa (pull --rebase resolve)'
  - 'Referencias antigas a hashes ficam no mapa (receipt consultavel)'
uncertainties:
  - 'filter-repo remove o remote origin ao final (comportamento documentado) — URL anotada antes e re-adicionada depois'
validation:
  - 'gh api dos 2 repos mostrando author.login dex-agent'
execution_prompt: |
  /GOAL Reescrever identidade dos commits da casa para dex-agent@proton.me nos 2 repos, com mapa preservado.
---

# Identidade git dex-agent — reescrita com mapa preservado

## Checklist visual
- [x] A-01 — pre-condições OK (status/worktrees/filter-repo)
- [x] A-02 — CRG reescrito + pushed + tag
- [x] A-03 — registry reescrito + pushed
- [x] A-04 — verificação remota + mapas commitados + avisos

> FECHADO 2026-11-21: config global dex-agent@proton.me; CRG reescrito (2238 mapas, main 350aaf3e->b9da3d8d, tag v2.4.0+dex.1 9ca592aa->ddbc4a0d, upstream intocado — tag v2.4.0 intacta); registry reescrito (496 mapas, 02e720de->8053bbfa + 2 commits a-frente de janela paralela incluidos); verificacao gh api 5/5 dex-agent em ambos; mapas commitados como receipt (.agents/receipts/rewrite-20261121/ nos 2 repos); lembranca da janela paralela restaurado do backup pos-rewrite; CI do push forcado 44952868734 vigiado (watch). Hashes antigos continuam consultaveis pelos commit-maps.
