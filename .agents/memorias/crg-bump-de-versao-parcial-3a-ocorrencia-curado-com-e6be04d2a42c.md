---
implementation_version: v2
layer: L2
slug: crg-bump-de-versao-parcial-3a-ocorrencia-curado-com-e6be04d2a42c
tags:
  - "#code-review-graph/release"
  - "#code-review-graph/ci"
  - "#code-review-graph/hook"
---

# CRG: bump de versao parcial (3a ocorrencia) curado com dono unico e gate; alarme herdado do upstream fica cego no fork

Corte versao-uma-fonte (GO PADRAO do dono em 2026-11-23; Trilho .agents/PLAN-TASKS/2026-11-23-versao-uma-fonte.md). A main do fork dex-agent/dex-code-review-graph estava vermelha desde 21/11 porque dois bumps moveram so o pyproject.toml: a versao e escrita em 13 arquivos. Cura em b45272a9 e fechamento 87014cf9: tools/release_version.py e o dono unico da lista e da regra (python -B tools/release_version.py --check), o hook pre-commit recusa commit parcial lendo o indice do git, o job release-stamps do CI roda a checagem no fork, e a copia do PATH foi reinstalada (doctor: All good; antes ela se acusava de desatualizada porque --version lia o metadata dex.3 e __version__ dizia dex.1).

LICAO DE CLASSE, vale para qualquer fork da casa: um alarme pode existir e nunca rodar. Tres formas medidas aqui: suite opt-in cujo unico gatilho era push para uma branch que o fork nao tem (promotion-gate.yml para testing); regex de teste que rejeitava o sufixo local da versao da casa; alarme que so toca no CI depois do push, num repo que empurra direto na main. Ao herdar workflow ou teste de upstream, conferir o on: contra git branch -r e as validacoes de formato contra o esquema real do fork.

ARMADILHA OPERACIONAL: em clone ou worktree novo do CRG o hook do Playbook recusa todo commit (DRIFT DETECTADO, exit 2). A projecao commitada so e fresca na arvore onde foi gerada (hash de bytes brutos no generate-playbook.py) e o hook esta no indice como 100644. Regenerar com generate-playbook.py --write antes de commitar la, sem commitar a projecao regenerada por engano. Causa e cura proposta: ISSUE-LOCAL-0051 do registry.

Por que: o dono pediu teste de regressao para garantir que nao se repita; a repeticao vinha de alarmes desligados, nao de falta de teste, por isso a cura tem gate no commit e nao so teste.

Como aplicar: ao tocar versao do CRG rodar python -B tools/release_version.py --check (gatilho CRG-BUMP-UMA-FONTE); ao revisar CI de fork checar primeiro se os jobs que deveriam pegar o defeito executam de fato; consultar TOOLSBOOK.index.md do repo antes de criar ferramenta. Rastros: TRACKER local do CRG (0008 fechado; 0009 aberto, o grafo reporta untested para modulo carregado por spec_from_file_location); registry ISSUE-LOCAL-0048 a 0052. Pendem decisao do dono: protecao de branch e comando unico de bump.

#code-review-graph/release #code-review-graph/ci #code-review-graph/hook

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-bump-de-versao-parcial-3a-ocorrencia-curado-com-e6be04d2a42c-content
