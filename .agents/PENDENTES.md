# PENDENTES.md — Ledger de pendências ativas (append-only)

> NUNCA apagar item: concluir (prova), adiar (quando), superseder (motivo + por) ou adicionar.
> Fonte de verdade parseável: bloco JSON abaixo (schema `dex.pendencias.v2`).

## Abertas
- [ ] CRG-CREDENCIAL-BACKUP [P1] — Confirmar rotacao da credencial exposta em backup historico local — quando: Antes de reutilizar a credencial historica; backup excluido do Git neste corte — owner: dono-da-conta
- [ ] CRG-UPSTREAM-GATES [P2] — Revalidar refactor, uninstall e hooks Windows antes de habilitar no perfil real — quando: Antes de habilitar as operacoes no perfil real; achados PARK-20260728-02 — owner: mantenedor-CRG
- [ ] CRG-GRAPHIFY-HISTORICO [P2] — Regenerar Graphify com corpus atual e confirmar labeling e versao — quando: Na proxima consulta relacional que exigir grafo atual; antes de citar o corte antigo — owner: mantenedor-Graphify
- [ ] CRG-ZCODE-CONTRATO [P2] — Provar contrato de cliente ZCode com fonte e tools-list real — quando: Antes de declarar compatibilidade ou editar configuracao ZCode — owner: mantenedor-ZCode
- [ ] CRG-WHEEL-PATH-SEM-EFFECT-FN-20261123 [P2] — A cópia do CRG no PATH (2.4.0+dex.3) não tem a indexação de Effect.fn do PR #6 — quando: próximo bump (dex.4), que também fecha a entrada Unreleased do FEATURES; decisão do dono
- [ ] CRG-HARNESS-DIFERENCIAL-SEM-FICHA-20261123 [P3] — Harness diferencial de parser em Temp, fora do repo, sem tríade e sem ficha — quando: próximo PR de parser; senão LIXEIRA com MANIFEST
## Adiadas
## Supersedidas
- [~] CRG-PROMOCAO-MCP [P2] — Promover a correcao testada para o runtime MCP instalado — quando: No proximo corte de instalacao apos o repo privado publicado — motivo: Dono definiu CLI como interface principal da edicao Dex; priorizar o recorte no executavel — supercedido por: CRG-CLI-RECORTE — owner: mantenedor-CRG
## Consumidas
- [x] CRG-CLI-RECORTE [P2] — Expor recorte por arquivo em detect-changes na CLI com prova Git e JSON — quando: No proximo corte funcional da edicao Dex — prova: 1e12485; quatro casos pelo executavel contra Git; 222 testes passaram na suite isolada — owner: mantenedor-CRG
<!-- PENDENTES:JSON:START -->
{
  "schema": "dex.pendencias.v2",
  "repo": "code-review-graph",
  "updated_at": "2026-11-19",
  "itens": [
    {
      "id": "CRG-CREDENCIAL-BACKUP",
      "titulo": "Confirmar rotacao da credencial exposta em backup historico local",
      "status": "aberta",
      "nivel": "P1",
      "quando": "Antes de reutilizar a credencial historica; backup excluido do Git neste corte",
      "data_limite": null,
      "owner": "dono-da-conta",
      "prova": null,
      "motivo": null,
      "supercedido_por": null,
      "criado_em": "2026-11-08",
      "concluida_em": null,
      "atualizado_em": null
    },
    {
      "id": "CRG-PROMOCAO-MCP",
      "titulo": "Promover a correcao testada para o runtime MCP instalado",
      "status": "supersedida",
      "nivel": "P2",
      "quando": "No proximo corte de instalacao apos o repo privado publicado",
      "data_limite": null,
      "owner": "mantenedor-CRG",
      "prova": null,
      "motivo": "Dono definiu CLI como interface principal da edicao Dex; priorizar o recorte no executavel",
      "supercedido_por": "CRG-CLI-RECORTE",
      "criado_em": "2026-11-08",
      "concluida_em": null,
      "atualizado_em": "2026-11-08"
    },
    {
      "id": "CRG-UPSTREAM-GATES",
      "titulo": "Revalidar refactor, uninstall e hooks Windows antes de habilitar no perfil real",
      "status": "aberta",
      "nivel": "P2",
      "quando": "Antes de habilitar as operacoes no perfil real; achados PARK-20260728-02",
      "data_limite": null,
      "owner": "mantenedor-CRG",
      "prova": null,
      "motivo": null,
      "supercedido_por": null,
      "criado_em": "2026-11-08",
      "concluida_em": null,
      "atualizado_em": null
    },
    {
      "id": "CRG-GRAPHIFY-HISTORICO",
      "titulo": "Regenerar Graphify com corpus atual e confirmar labeling e versao",
      "status": "aberta",
      "nivel": "P2",
      "quando": "Na proxima consulta relacional que exigir grafo atual; antes de citar o corte antigo",
      "data_limite": null,
      "owner": "mantenedor-Graphify",
      "prova": null,
      "motivo": null,
      "supercedido_por": null,
      "criado_em": "2026-11-08",
      "concluida_em": null,
      "atualizado_em": null
    },
    {
      "id": "CRG-ZCODE-CONTRATO",
      "titulo": "Provar contrato de cliente ZCode com fonte e tools-list real",
      "status": "aberta",
      "nivel": "P2",
      "quando": "Antes de declarar compatibilidade ou editar configuracao ZCode",
      "data_limite": null,
      "owner": "mantenedor-ZCode",
      "prova": null,
      "motivo": null,
      "supercedido_por": null,
      "criado_em": "2026-11-08",
      "concluida_em": null,
      "atualizado_em": null
    },
    {
      "id": "CRG-CLI-RECORTE",
      "titulo": "Expor recorte por arquivo em detect-changes na CLI com prova Git e JSON",
      "status": "concluida",
      "nivel": "P2",
      "quando": "No proximo corte funcional da edicao Dex",
      "data_limite": null,
      "owner": "mantenedor-CRG",
      "prova": "1e12485; quatro casos pelo executavel contra Git; 222 testes passaram na suite isolada",
      "motivo": null,
      "supercedido_por": null,
      "criado_em": "2026-11-08",
      "concluida_em": "2026-11-08",
      "atualizado_em": "2026-11-08"
    },
    {
      "id": "PEND-2026-11-15-TOOLSBOOK",
      "titulo": "Bootstrap do toolsbook do repo (dex.toolsbook.v2) com entrada CRG 2.4.0+dex.1",
      "contexto": "Corte 2.4.0-dex fechou sem livro de ferramentas no repo; criar superficie meia-boca violaria o schema da casa. Em 2026-11-23 o livro nasceu com cobertura parcial declarada (TOOLSBOOK.json, 5 fichas, --check exit 0, porta no AGENTS.md); resta implantar a guarda (reuso.py e ficha-gate.py em tools/dev/) depois de pagar a staging CRG-TEMP-RELOCAR",
      "owner": "mantenedor CRG",
      "origem": "Trilho 2026-11-15-crg-240-dex-merge (closure gate)",
      "status": "aberta",
      "supercedido_por": null,
      "criado_em": "2026-11-15",
      "concluida_em": null,
      "atualizado_em": "2026-11-15"
    },
    {
      "id": "CRG-VULNS-HERDADAS",
      "titulo": "Política para 137 vulnerabilidades herdadas do lockfile upstream (8 critical, 57 high, 62 moderate, 10 low)",
      "status": "aberta",
      "nivel": "P2",
      "quando": "Ao definir política própria de dependências; hoje a política é acompanhar upstream por merge manual (ISSUE-LOCAL-0005)",
      "data_limite": null,
      "owner": "dono",
      "prova": "push 187cf778 imprimiu o inventário; gh api repos/dex-agent/dex-code-review-graph/dependabot/alerts",
      "motivo": "Alerts ligados em 2026-11-19 revelaram dívida invisível até então",
      "supercedido_por": null,
      "criado_em": "2026-11-19",
      "concluida_em": null,
      "atualizado_em": null
    },
    {
      "id": "CRG-FLOW-PPIRTV-ORFAO",
      "titulo": "Flow PPIRTV 20261114193314577_0711 zumbi: active/0-done/sem verdict há 5 dias com trabalho real já pago",
      "status": "aberta",
      "nivel": "P3",
      "quando": "No próximo fechamento PPIRTV ou descarte consciente (goal_verdict ou archive)",
      "data_limite": null,
      "owner": "sessao-do-projeto",
      "prova": ".ppirtv/flows/flow_20261114193314577_0711_0108.json (status=active, verdict ausente) vs memória reconhecimento-code-review-graph (ensaio ZIP 2º Windows VERDE 2026-11-14)",
      "motivo": "Contradição contrato×execução: flow diz 0/3, realidade diz concluído",
      "supercedido_por": null,
      "criado_em": "2026-11-19",
      "concluida_em": null,
      "atualizado_em": null
    },
    {
      "id": "CRG-AGENTS-BEADS-DRIFT",
      "titulo": "AGENTS local manda \"bd for ALL task tracking\" (boilerplate beads do fork) mas a casa opera TRACKER local + Trilhos SPT",
      "status": "aberta",
      "nivel": "P3",
      "quando": "Na próxima edição do AGENTS.md do projeto",
      "data_limite": null,
      "owner": "dono",
      "prova": "AGENTS.md (bloco Beads Issue Tracker) vs .agents/TRACKER/INDEX.md + PLAN-TASKS",
      "motivo": "Hierarquia resolve (global>projeto), mas o texto local ensina errado para janela fria",
      "supercedido_por": null,
      "criado_em": "2026-11-19",
      "concluida_em": null,
      "atualizado_em": null
    },
    {
      "id": "CRG-TEMP-RELOCAR",
      "titulo": ".agents/TEMP com 1842 arq/260.4MB acumulados — relocar por classe (nada é apagado)",
      "status": "aberta",
      "nivel": "P3",
      "quando": "Corte próprio de garimpo de TEMP (bloco dedicado); apontado pelo fechamento 2026-11-19",
      "data_limite": null,
      "owner": "sessao-do-projeto",
      "prova": "scan fechamento superficie TEMP/TMP (receipt fechamento-20261119.json)",
      "motivo": "Dívida antiga pré-bloco; garimpo antes de qualquer remoção",
      "supercedido_por": null,
      "criado_em": "2026-11-19",
      "concluida_em": null,
      "atualizado_em": null
    },
    {
      "id": "CRG-REGISTRY-ITENS-BUMP-20261123",
      "titulo": "Registry — itens a abrir no TRACKER do repo dono após o corte versao-uma-fonte: (a) skills oraculo-teste-de-integracao e oraculo-teste-de-unidade com âncoras de linha do build r2 (07874ccf) contra o corpus vivo r3 (971c316328560ffc) e grafo da porta ainda no build antigo; (b) oraculo-solid SKILL.md ensina receita de junction (readlink -f) que falha no registry; (c) skill code-review-graph em 2.4.0+dex.1 (SKILL.md l.81/89, CAPACITY.md l.13) com o PATH em 2.4.0+dex.3; (d) skill dex-playbook-entrada (dona do gerador instalado em tools/playbook/generate-playbook.py): o hash das fontes usa bytes brutos (l.229 read_bytes), então a projeção commitada dá DRIFT (exit 2) em qualquer clone novo — medido no clone de prova nos commits f86f9920 e 9153a5ce — e tools/playbook/hooks/pre-commit está no índice como 100644 (não-executável no POSIX: o hook nunca roda em clone Linux/Mac)",
      "status": "concluida",
      "nivel": "P2",
      "quando": "Fechamento do Trilho 2026-11-23-versao-uma-fonte; se a sessão não chegar, a próxima janela do registry",
      "data_limite": "2026-11-25",
      "owner": "sessao-do-projeto",
      "prova": "Itens abertos offline no registry em 2026-11-23: ISSUE-LOCAL-0048 (oráculos de teste, âncoras r2), 0049 (oraculo-solid, receita de junction), 0050 (skill code-review-graph em dex.1), 0051 (dex-playbook-entrada, hash de bytes brutos e hook 100644); laudo em .agents/receipts/issues/20261123-1605-bump-crg-consumidores/ do registry. Sem commit no registry.",
      "motivo": "Gate CRG-BUMP-CONSUMIDORES do AGENTS local: consumidor documental stale vira item no TRACKER do repo dono (registry), não conserto paralelo",
      "supercedido_por": null,
      "criado_em": "2026-11-23",
      "concluida_em": "2026-11-23",
      "atualizado_em": "2026-11-23"
    },
    {
      "id": "CRG-SUITES-PROMOTION-GATE-CEGAS-20261123",
      "titulo": "Suites que só rodam no promotion-gate.yml (gatilho: push para testing, branch inexistente no fork) nunca rodam no CI do fork: packaging completo (14 dos 16 testes), determinism, corpus, upgrade-path (skipped no ci.yml) e platform_lifecycle",
      "status": "aberta",
      "nivel": "P2",
      "quando": "Corte próprio de CI do fork; descoberta ao curar o ISSUE-LOCAL-0008 (irmã da classe 'alarme que não roda no fork')",
      "data_limite": "2026-12-07",
      "owner": "mantenedor CRG",
      "prova": ".github/workflows/promotion-gate.yml (on: push branches [testing] e workflow_dispatch); o ci.yml só roda 2 testes de packaging, pelo job release-stamps",
      "motivo": "R8/R15: classe verificada nos irmãos; medir antes de decidir (gh workflow run promotion-gate.yml) — não ligar suíte pesada sem prova de custo",
      "supercedido_por": null,
      "criado_em": "2026-11-23",
      "concluida_em": null,
      "atualizado_em": null
    },
    {
      "id": "CRG-WHEEL-PATH-SEM-EFFECT-FN-20261123",
      "titulo": "A copia do CRG instalada no PATH (wheel de b45272a9, 2.4.0+dex.3) nao tem a indexacao de Effect.fn do PR #6: quem usa o executavel da casa nao ganha as funcoes ate um wheel novo",
      "status": "aberta",
      "nivel": "P2",
      "quando": "Proximo bump (2.4.0+dex.4), que tambem fecha a entrada Unreleased do docs/FEATURES.md; decisao do dono",
      "data_limite": "2026-12-01",
      "owner": "mantenedor CRG",
      "prova": "code-review-graph build com o executavel do PATH num repo com Effect.fn indexa so load (2026-11-23, provado no bloco do PR #6); a sonda tools/js_form_probe.py --caso red_green reproduz",
      "motivo": "Troca de executavel dispara o gate CRG-BUMP-CONSUMIDORES do AGENTS local e exige mover as 13 fontes de versao junto; nao e acao de fim de bloco",
      "supercedido_por": null,
      "criado_em": "2026-11-23",
      "concluida_em": null,
      "atualizado_em": null
    },
    {
      "id": "CRG-HARNESS-DIFERENCIAL-SEM-FICHA-20261123",
      "titulo": "Harness diferencial de parser em .agents/receipts/CRG-PR6-REVISAO-20261123/harness-diferencial/ (bin/diffdump.py, diffcmp.py, mkprobes.py) esta so em disco, sem triade, sem teste e sem ficha no TOOLSBOOK",
      "status": "aberta",
      "nivel": "P3",
      "quando": "Proximo PR que mude o parser; se nao houver ate la, LIXEIRA com MANIFEST",
      "data_limite": "2026-12-07",
      "owner": "sessao-do-projeto",
      "prova": "TOOLSBOOK.json, campo unexplored; README.md na pasta do harness; comparacao de 160 arquivos em 6 corpora re-executada sobre os dumps guardados em 2026-11-23; resgatado da Temp no mesmo dia",
      "motivo": "R13 e REUSO-ANTES-DE-CRIAR: nasceu sem recibo de reuso; promover a tools/ com triade, teste e ficha, ou aposentar com MANIFEST",
      "supercedido_por": null,
      "criado_em": "2026-11-23",
      "concluida_em": null,
      "atualizado_em": null
    }
  ]
}
<!-- PENDENTES:JSON:END -->
