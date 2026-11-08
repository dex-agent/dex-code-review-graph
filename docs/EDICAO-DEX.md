# Edicao Dex do Code Review Graph

Repositorio privado da casa em `dex-agent/dex-code-review-graph`, derivado do
upstream `tirth8205/code-review-graph`. O historico Git e a licenca MIT original
sao preservados. O remoto `origin` aponta para a edicao privada e `upstream`
permite comparar a evolucao do projeto de origem.

## Organizacao

- `code_review_graph/` e `tests/` mantem a estrutura do produto original.
- `workflow/` contem a receita local de manutencao com evidencia.
- `.agents/PLAN-TASKS/` preserva Trilhos e comprovacoes por corte.
- `.agents/MAPAS/` preserva capacidades, decisoes e dependencias demonstradas.
- `.agents/ACTIVE.md` e `.agents/HANDOFF.md` indicam o estado corrente.
- `.agents/PENDENTES.md` referencia os debitos, com owner e quando.
- `.agents/receipts/crg-diff-recorte/` preserva RED, GREEN e smoke da correcao.

Configuracoes pessoais, bancos, logs brutos, backups e grafos gerados ficam
locais pelas regras de `.gitignore`. A selecao e explicita para que um novo
backup de credencial nao entre automaticamente no stage. Remover do indice
Git preserva o arquivo de trabalho. Commits anteriores continuam no historico.

## Corte funcional inicial

O analisador compartilhado restringe as faixas do diff aos arquivos pedidos.
Dois cenarios Git verificam mudanca em A+B com recorte A e mudanca apenas em B
com recorte A. A suite focada e o smoke dos consumidores estao ligados ao
Trilho `2026-11-07-crg-diff-recorte`.

```powershell
uv sync --frozen
uv run --no-sync pytest -q tests/test_changes.py
git fetch upstream
git log --oneline upstream/main..main
```

## Inventario de higiene de 2026-11-08

O scan inicial encontrou 111 arquivos nao rastreados, 63 ocorrencias de cache
gerado, dois locais de backup e nenhum temporario. As categorias se sobrepoem.
Garimpo preservou os registros curados. Runtime `.ppirtv/`, transacoes de
memoria, corpus/cache Graphify e backups de configuracao permanecem no disco,
excluidos da publicacao. Um backup antigo apresentou padrao de credencial.
A verificacao de rotacao pertence ao dono da conta e esta no ledger.

O aviso do runtime sobre caminhos fixos no README corresponde a exemplos
genericos de configuracao (`/home/user/project-a` e `C:\\path\\to\\...`).
O exemplo e intencional. Sua presenca nao identifica um caminho desta maquina.

Grafos historicos exigem o staleness-check antes de consulta. A publicacao Git
da correcao nao promove automaticamente o runtime MCP instalado.
