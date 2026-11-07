# Configuração e histórico do CRG

## Configuração do corte

- Alvo: checkout Git do Code Review Graph, núcleo Python e extensão TypeScript. Parser CRG nativo. O feeder é reservado aos projetos Object Pascal.
- Owner: mantenedor do CRG. Consumidores: CLI, MCP e extensão VS Code, conforme os caminhos tocados.
- Tracker: `bd prime`; abrir ou reutilizar o bead do corte antes de mudar código. Trilho em `.agents/PLAN-TASKS/`, com critérios e evidências por caso.
- Baseline: `git rev-parse HEAD 'HEAD^{tree}'`, `git status --porcelain=v2`, `git diff --stat`, `git diff --cached --stat` e `code-review-graph status --repo .`. Confirme também o repo e SHA em `get_minimal_context_tool`. Preserve as leituras se divergem.
- Banco e data dir: confirme o SQLite efetivamente aberto pela CLI ou pelo MCP e registre caminho, schema, versão e origem no recibo do corte. Em novo índice governado, use `.agents/CODE-REVIEW-GRAPH` pela skill `code-review-graph`. Divergência de resolução entre CLI e MCP exige confirmar o banco consumidor antes de comparar ou atualizar.
- Exporter: `$env:USERPROFILE/.agents/skills/code-review-graph/scripts/crg-snapshot/export_crg_snapshot.py`. Confira `--help`, `--schema` e `--usage`; passe o SQLite confirmado em `--database`, a raiz Git em `--repo-root` e um JSON novo em `--output`, no diretório de evidência do corte. Compare versões, escopo, normalização e cobertura antes de interpretar o delta.
- Teste Python: use o ambiente de desenvolvimento do repo, confirme `python -m pytest --version` e execute `python -m pytest -q tests/test_changes.py` para a área de análise de mudanças; acrescente o teste focado do consumidor tocado. Falha de coleta é falha de ambiente, não RED de comportamento. Para TypeScript, leia `code-review-graph-vscode/package.json` e execute o script existente apropriado ao diff.

## PPIRTV e régua

| Fase | Owner na sessão | Prova de saída |
| --- | --- | --- |
| Pensamentos | Reunião, com Chato | Pergunta material, hipótese, fonte, sintomas versus causa e escopo do corte. |
| Planejamento | Sprinter | Trilho com comportamento, consumidores, RED, rollback, owner e quando. Âncora/Auto Fluxo conferem transição. |
| Implementação | Mapeador | Menor fatia ponta a ponta; procure reuso antes de criar e preserve contrato e tratamento de erro. |
| Revisão/Ajustes | Revisor | Diff e fronteiras conferidos, busca de vizinhos e impacto em CLI/MCP/extensão quando aplicável. |
| Teste | Tio Testador | RED anterior, mesmos casos após ajuste, regressões pertinentes e reprodução pela entrada pública. |
| Validação | Validador Pronto | Critérios do Trilho ligados às provas, três mapas após atualização, ressalvas e veredito. |

- Régua `dex-regras-desenvolvimento-casa`: R1/R2 passo reversível com prova anterior; R3 percurso de entrada a saída; R4–R7 coesão, dependências, reuso e simplicidade; R8 registrar degradação com owner e quando; R9 testar contrato/erros; R10 automatizar prova repetível com a toolchain existente. Medições de complexidade são evidência auxiliar, com configuração e escopo registrados.
- Chato conduz as perguntas de princípio, causa, owner e efeito. Questionador, Crítico Cético, Entrevista-me, Burrinha e Ponytail confrontam premissas e prova proporcional. Incidente vai à fonte pelo Interrogador Documental e à busca de vizinhos pelo Barata Scan. Achado memorável segue Dex Memória e validação de L1↔L2 ou L1↔L3. Fechamento material usa `dex-fechamento-projeto-atualizado`.
- Meta-análise na criação, antes do veredito e entre SPTs, inclusive o último. Se a fonte mudar a decisão, retornar à fase afetada, ajustar, retestar e registrar efeito nos próximos dependentes.

## Três mapas por atualização do CRG

Gatilho: código/versão do CRG atualizado ou índice estrutural do alvo reconstruído/atualizado, inclusive atualização fora de um SPT. O executor publica o corte antes de fechar a rodada. O mantenedor confirma fontes e limites. Uma consulta read-only não dispara publicação.

1. Antes da atualização, identifique o último corte comparável ou capture baseline real. Separe HEAD, árvore de trabalho, versão do executável e estado do índice. Preserve as fotografias anteriores; falta de baseline fica explícita.
2. Depois, use um ID novo comum, com data/hora, revisão e recorte, e publique em `.agents/MAPAS/`. Use `.agents/MAPAS/INDEX.md` para ligar o corte, o Trilho/receipt e a evidência dos três mapas.
3. **Capacidades** (`dex-mapa-capacidades`): publique `capacidades-crg-ID.md`, com owner, consumidor, gatilho, comportamento, oracle independente, prova e limite. Compare fotos somente quando comparáveis; declare o que continua sem prova.
4. **Decisões** (`dex-mapa-das-decisoes`): publique `decisoes-crg-ID.md`, modo histórico. Registre escolha, origem, estado, data, owner, provas, eventos e efeito observado. Mantenha IDs entre cortes; se nada mudou no conjunto de decisões, registre a revisão e as evidências consultadas, sem inventar decisão.
5. **Dependências** (`dex-mapa-relacional-dependencias`): publique `dependencias/crg/ID/` com Markdown, JSON e HTML usando o CLI da skill. Valide o modelo com `dependency_map.py validate --input`, publique com `publish --input … --out …`; quando houver corte A comparável, execute `compare --before … --after … --out …` e indexe Markdown/JSON do delta. Confira consumidores, direção, condição, fonte e lacunas. Visualização parcial exige ressalva e não invalida a projeção textual.
6. Reabra o índice e as saídas. Verifique que cada arquivo identifica o mesmo corte e traz fontes reabríveis. Se atualização/publicação falhar, mantenha o último corte publicado, registre a tentativa com causa, responsável e quando e recupere as provas faltantes antes de afirmar fechamento completo.

## Meta-análise da criação

- Pergunta: o mapa pode usar a própria saída do CRG como única prova? O controle com diff vazio em USAGE.md refuta a suficiência do grafo para este caso.
- Oráculo: Oráculo Pragmático, Hunt e Thomas, *O Programador Pragmático*, PT-BR 2000, capítulo 10, `fulltext.txt:1215–1217`, extração `range_0047_0092.md:389` reaberta. O livro sustenta retorno cedo em ambiente real. A aplicação ao CRG é decisão local.
- Impacto e decisão: adotar Git/fonte/teste como oracles independentes e manter o primeiro corte pequeno. Ausência de fotografia anterior não bloqueia novo baseline. Aplicável também a atualizações só do índice.
- Reteste e avanço: verificar a receita com o checker composto e reabrir o exemplo do piloto. Mantenedor executa o primeiro corte de produto quando houver Trilho validado. A execução dos três mapas após atualização será comprovada naquele corte.
