---
implementation_version: v2
layer: L2
slug: crg-35-comandos-prompts-modelos-20261119-b150c10bbec7
tags:
  - "#auto-memory/reference"
---

# crg-35-comandos-prompts-modelos-20261119

Espelho da auto-memory do host ZCode (arquivo crg-35-comandos-prompts-modelos-20261119.md, tipo reference).

Índice 5W2H + tabela dos 35 comandos do CRG (fonte: --help do exe

Pedido do dono (2026-11-19, pós-ciclo da auditoria): explicar o CRG para leigo → índice 5W2H → lista de TODOS os comandos com prompt modelo ao lado. Fonte canônica: `code-review-graph --help` do executável do PATH (2.4.0+dex.1) — lido ao vivo (vacina CRG-BUMP-CONSUMIDORES: comandos ensinados × --help real; ajuda completa tem 35 comandos).

**As 6 famílias** (organização usada na entrega):
1. Instalação/saúde: `install`/`init`, `uninstall`, `doctor`
2. Mapa: `build`, `update` (+`--brief` = re-parse dos mudados; detect-changes NÃO re-parseia), `postprocess`, `embed`, `watch`, `forget` (identidade da pasta, sem rebuild), `status`, `context-history`
3. Multi-repo: `register`, `unregister`, `repos`, `daemon start/stop/status/add/remove`
4. Análise de mudança (a joia): `detect-changes`, `merge-check` (suíte em checkout descartável + regra dos 3 números), `impact`, `query tests_for`, `query`, `search`, `dead-code`, `large-functions`, `refactor`
5. Relatórios: `flows`/`flow`, `communities`/`community`, `architecture`, `visualize` (HTML), `wiki`
6. Serviço/avaliação: `serve`/`mcp` (stdio; `--http` localhost), `eval`

**Prompts modelos no estilo da casa** (como o dono pede à sessão): "Analise este diff contra o grafo" (detect-changes) · "Rode o merge-check antes de fechar este merge" · "Se eu mudar a função X, quem sente?" (impact) · "Quais testes testam X?" (query tests_for) · "Esqueça a pasta vendor/ do índice (identidade da pasta)" (forget) · "Rode o doctor sem mexer em nada" (fechamento de bloco). Dia a dia da casa: update → detect-changes → impact/query tests_for → merge-check → doctor.

**Desfecho (GO do dono, mesmo dia)**: a tabela completa virou **ISSUE-LOCAL-0023** no TRACKER do registry de skills (`.agents/TRACKER/issues/0023-crg-referencia-comandos-prompts-versionada.md`, commit `220b2a82` pushed; INDEX com `⏳ aguardando: governancia-skills`). O item carrega os dados completos (35 comandos/6 famílias + prompts) e a regra de frescor pedida pelo dono: a referência descreve a **v2.4.0+dex.1** e TODO bump de versão que mudar comandos/bandeiras exige atualizá-la NA MESMA SESSÃO (classe CRG-BUMP-CONSUMIDORES; check barato `--version`+`--help` contra a tabela).

**INTEGRAÇÃO CONCLUÍDA (2026-11-19, corte 3.533.1 do registry, commits `b1a69ef9`+`88630196` — hashes PRÉ-rewrite; ver [[identidade-git-dex-agent-rewrite-20261121]] p/ os novos)**: Governanta convocada (roteamento anti-rascunho: conteúdo em `references/`, SKILL.md só contrato) → `code-review-graph/references/commands-v2.4.0-dex.1.md` criado (nome hifenizado, versão exata 2.4.0+dex.1 no conteúdo; `+` em nome de arquivo é hostil a ferramentas) + ponteiro na seção "Versão da casa e schema" do SKILL.md com o gate de bump + CHANGELOG 3.533.1. Gates do pre-commit pegaram 2 dívidas pagas na hora: PLAYBOOK regenerado e **G7 re-foto do CAPACITY** (`skill_md_sha256` novo → validate-capacity 0 findings + generate-capacity-index --write). Achado alheio no regen: `dex-locate-memories/CAPACITY.md` frontmatter YAML inválido → ISSUE-LOCAL-0027 (renumerado de 0024 por COLISÃO com janela paralela — regra: colisão = alocar maior NNNN+1). Tropeço do repo compartilhado: janela paralela pushou MEU commit local antes do meu amend (push `behind 1` com meu hash no remoto) → cura `reset --hard origin/main` + delta como commit novo (napkin do registry: `PUSH-PARALELO-AMEND-PUBLICADO`).

Relacionado: [[crg-cura-ci-8-classes-20261119]] · [[merge-check-gatilho-prompt-pronto-20261116]] · [[untangle-codebase-com-crg-regimes-20261117]]

#auto-memory/reference

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-35-comandos-prompts-modelos-20261119-b150c10bbec7-content
