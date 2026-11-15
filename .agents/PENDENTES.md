# PENDENTES.md — Ledger de pendências ativas (append-only)

> NUNCA apagar item: concluir (prova), adiar (quando), superseder (motivo + por) ou adicionar.
> Fonte de verdade parseável: bloco JSON abaixo (schema `dex.pendencias.v2`).

## Abertas
- [ ] CRG-CREDENCIAL-BACKUP [P1] — Confirmar rotacao da credencial exposta em backup historico local — quando: Antes de reutilizar a credencial historica; backup excluido do Git neste corte — owner: dono-da-conta
- [ ] CRG-UPSTREAM-GATES [P2] — Revalidar refactor, uninstall e hooks Windows antes de habilitar no perfil real — quando: Antes de habilitar as operacoes no perfil real; achados PARK-20260728-02 — owner: mantenedor-CRG
- [ ] CRG-GRAPHIFY-HISTORICO [P2] — Regenerar Graphify com corpus atual e confirmar labeling e versao — quando: Na proxima consulta relacional que exigir grafo atual; antes de citar o corte antigo — owner: mantenedor-Graphify
- [ ] CRG-ZCODE-CONTRATO [P2] — Provar contrato de cliente ZCode com fonte e tools-list real — quando: Antes de declarar compatibilidade ou editar configuracao ZCode — owner: mantenedor-ZCode
## Adiadas
## Supersedidas
- [~] CRG-PROMOCAO-MCP [P2] — Promover a correcao testada para o runtime MCP instalado — quando: No proximo corte de instalacao apos o repo privado publicado — motivo: Dono definiu CLI como interface principal da edicao Dex; priorizar o recorte no executavel — supercedido por: CRG-CLI-RECORTE — owner: mantenedor-CRG
## Consumidas
- [x] CRG-CLI-RECORTE [P2] — Expor recorte por arquivo em detect-changes na CLI com prova Git e JSON — quando: No proximo corte funcional da edicao Dex — prova: 1e12485; quatro casos pelo executavel contra Git; 222 testes passaram na suite isolada — owner: mantenedor-CRG
<!-- PENDENTES:JSON:START -->
{
  "schema": "dex.pendencias.v2",
  "repo": "code-review-graph",
  "updated_at": "2026-11-15",
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
      "contexto": "Corte 2.4.0-dex fechou sem livro de ferramentas no repo; criar superficie meia-boca violaria o schema da casa",
      "owner": "mantenedor CRG",
      "origem": "Trilho 2026-11-15-crg-240-dex-merge (closure gate)",
      "estado": "aberta",
      "supercedido_por": null,
      "criado_em": "2026-11-15",
      "concluida_em": null,
      "atualizado_em": "2026-11-15"
    }
  ]
}
<!-- PENDENTES:JSON:END -->
