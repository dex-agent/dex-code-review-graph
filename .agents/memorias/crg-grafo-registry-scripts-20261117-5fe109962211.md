---
implementation_version: v2
layer: L2
slug: crg-grafo-registry-scripts-20261117-5fe109962211
tags:
  - "#auto-memory/project"
---

# crg-grafo-registry-scripts-20261117

Espelho da auto-memory do host ZCode (arquivo crg-grafo-registry-scripts-20261117.md, tipo project).

Grafo CRG dos SCRIPTS das ~700 skills construído no registry

Pedido do dono "CRG específico para dependências/relacionamentos de skills no
registry" (2026-11-17) — entregue em 2 camadas com veredito honesto:

- **Camada 1 FEITA**: CRG nativo sobre o CÓDIGO dos scripts (lacuna real —
  nenhum tool mapeava imports/calls/tests cross-skill). Build:
  `4717 arquivos · 100.826 nós · 260.950 arestas · 418 TESTED_BY` (1.266
  arquivos de código: 903 py, 179 mjs, 84 ps1...). Hotspots imediatos:
  `technical-book-to-skill-router/scripts/run-rich-skill-workflow.py:execute`
  **L1774**, `ppi-install:execute` L573, anatomy kit L444-544.
- **Camada 2 DEFERIDA (R17)**: skills-como-nós (semântica skill↔skill) já tem
  dono — grafo rico Graphify (`SKILLS-CATALOG-GRAPHIFY-CURRENT`,
  candidate-696-merge) + capacity-index; feeder no molde Delphi só se
  pergunta concreta provar evidência exclusiva.

**Publicação contratual** (skill CRG): data dir `.agents/CODE-REVIEW-GRAPH/`
gitignored + receipt `.agents/CODE-REVIEW-GRAPH-INDEX.md` + ficha 5W2H no hub
(via helper `gatilhos-vivos.py render`; check 22 registros/0 achados) + regra
no AGENTS.md do registry + PLAYBOOK regen no mesmo commit. Commit+push
`012084bd`. Gitignore do registry: `**/.agents/*` (l.11) exige NEGAÇÃO
explícita `!.agents/CODE-REVIEW-GRAPH-INDEX.md` no molde dex-ignore.

**Limites**: PowerShell (84 ps1) NÃO parseado; grafo engole artefatos gerados
(catalog.json 181k linhas, graph.json de knowledge-graph) → queries de função
usam `--kind Function` / `--path scripts/`; 6 erros de parser pendentes;
grafo nasce stale no dia (registry muda todo dia → doctor antes de citar).

**Queries de uso**: `doctor` → `query callers_of|imports_of|tests_for` /
`large-functions --kind Function --min-lines 200` (tem flags --kind/--path).

**Tropeços pagos ao vivo**: (1) `/tmp` Git Bash ≠ path de python nativo —
usar `$TEMP` ou pipe direto; (2) skip-check de inserção de gatilho deve casar
a LINHA de índice 5W2H (`| GATILHO |` no início), não qualquer menção da
string (o hub tem menções em outras tabelas — inseriu skip falso 1x);
(3) `render` do helper devolve JSON {linha_indice, bloco_detalhe} no stdout —
inserir linha após header+separator da tabela `| Gatilho |` e append do bloco
no fim.

**ISSUE-LOCAL-0010 aberta (2026-11-17, push `ceb6791b`, mesma sessão do grafo
— ISSUES-POR-REPO-DONO)**: hotspots (execute L1774 book-router, ppi-install
573, anatomy 444-544) + os 6 erros de parser não listados viraram item
TRACKER P2/tarefa com pacote de receipt
`.agents/receipts/issues/20261117-0745-crg-hotspots/` (laudo.md com método
reprodutível + corpo + manifesto com hashes b81f40c3/653ad495). Cura
sugerida: ronda untangle (1 alvo/rodada, medir-cc antes→depois) + captura
dos 6 erros com stderr redirecionado (build não os lista; data dir só tem
graph.db). Dedupe feito (0 duplicatas da classe). Próximo passo natural:
ronda untangle do `execute` L1774.

**Tropeço 4 (pago ao vivo na abertura do 0010)**: heredoc bash com EOF não
fechado VAZOU linhas do harness (`__zcode_status=$?…exit`) para DENTRO do
laudo.md — conferir sempre a cauda do arquivo após heredoc; arquivo se
escreve com Write/Edit nativo (EDICAO-ARQUIVO-HIERARQUIA), shell heredoc é
rota errada para conteúdo canônico.

Related: [[untangle-codebase-com-crg-regimes-20261117]],
[[crg-240dex-merge-fechado-20261115]], [[merge-check-gatilho-prompt-pronto-20261116]]

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-grafo-registry-scripts-20261117-5fe109962211-content
