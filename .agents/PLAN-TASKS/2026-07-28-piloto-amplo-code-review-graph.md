---
dex_contract: spt
version: 2
status: 'concluido_com_ressalvas'
owner: 'validador-pronto'
date: '2026-07-28'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'reuniao PPIRTV aprovada pelo usuario'
goal:
  id: 'piloto-amplo-code-review-graph'
  title: 'Piloto amplo, instrumentado e reversivel do code-review-graph'
  objective: 'Medir a utilidade, os efeitos colaterais e a portabilidade das capacidades completas do code-review-graph antes de decidir sua integracao ao ecossistema Dex.'
context: 'O diagnostico confirmou 30 tools MCP, 5 prompts, 7 skills upstream, banco inicialmente vazio e riscos Windows localizados em hooks, uninstall e prewarm de embeddings.'
problem: 'Uma proposta anterior reduzia antecipadamente a superficie do piloto e poderia produzir uma conclusao enviesada contra a ferramenta.'
decision: 'Exercitar a superficie completa em ambientes controlados, isolando o raio de impacto sem amputar capacidades e sem alterar ainda o registry global ou os perfis reais dos clientes.'
scope:
  include:
    - 'Baseline sem grafo e inventario before/after do workspace.'
    - 'tools/list real, build/update, postprocess, consultas, fluxos, comunidades, arquitetura, review e wiki.'
    - 'Embeddings locais com telemetria de cache, rede, tempo e tamanho.'
    - 'refactor_tool e apply_refactor_tool com aplicacao real em fixture ou worktree descartavel.'
    - 'list_repos e cross_repo_search em registry controlado.'
    - 'Installer, hooks e uninstall em perfil de usuario redirecionado e repositorio temporario.'
    - 'Compatibilidade workspace-local com Codex Desktop, Codex CLI e ZCode.'
    - 'Avaliacao separada das 7 skills upstream e dos 5 prompts.'
    - 'Comparacao com Graphify e skills owners do ecossistema Dex.'
  exclude:
    - 'Copiar ou admitir skill no registry global.'
    - 'Alterar INDEX.md, governanca ou CHANGELOG do registry global.'
    - 'Instalar hooks no perfil real do usuario.'
    - 'Alterar configuracoes reais de Codex Desktop, Codex CLI, ZCode ou MCP.'
    - 'Aplicar refatoracao em codigo vivo fora de fixture ou worktree descartavel.'
    - 'Enviar codigo real a provedor externo de embeddings sem autorizacao especifica.'
    - 'Commit, push, release ou publicacao.'
spec: 'O piloto deve manter as 30 tools disponiveis, exercitar cada familia funcional em alvo controlado, registrar comandos, resultados, arquivos criados ou alterados, downloads, rede, rollback e comparar tarefas equivalentes com e sem o MCP. Falha de uma superficie deve bloquear apenas a superficie causalmente afetada.'
plan:
  - 'Congelar revision, ambiente e inventario before.'
  - 'Validar o servidor por tools/list real e construir o grafo completo.'
  - 'Executar consultas estruturais, review, fluxos, comunidades, wiki e embeddings locais.'
  - 'Executar refatoracao real somente em fixture ou worktree descartavel e provar rollback.'
  - 'Executar multi-repo e installer em perfis e registries controlados.'
  - 'Avaliar clientes, prompts e skills upstream sem admissao global.'
  - 'Revisar findings, procurar padroes vizinhos e executar a bateria Windows.'
  - 'Consolidar matriz de evidencia e emitir veredito de adocao, adaptacao ou rejeicao.'
tasks:
  - 'Registrar revision, versoes, dependencias, git status e estado before.'
  - 'Obter tools/list real e confirmar a lista de 30 tools, 5 prompts e 0 resources.'
  - 'Executar build_or_update_graph_tool com full_rebuild e postprocess completo.'
  - 'Executar stats, arquitetura, comunidades, fluxos, impacto, review e perguntas sugeridas.'
  - 'Gerar wiki controlada e inventariar os arquivos produzidos.'
  - 'Executar embeddings locais e registrar cache, downloads, tempo e cobertura.'
  - 'Criar fixture descartavel e exercitar refactor_tool e apply_refactor_tool de ponta a ponta.'
  - 'Criar registry multi-repo controlado e exercitar list_repos e cross_repo_search.'
  - 'Executar install e uninstall em HOME ou USERPROFILE redirecionado e validar rollback.'
  - 'Validar configuracoes workspace-local propostas para Codex Desktop, Codex CLI e ZCode.'
  - 'Comparar as 7 skills upstream e os 5 prompts contra os owners Dex.'
  - 'Executar review findings-first, testes proporcionais e veredito final.'
expected_evidence:
  - 'Receipt MCP tools/list com nomes e schemas reais.'
  - 'Stats before e after com arquivos, nodes, edges, linguagens e timestamp.'
  - 'Matriz de chamadas das 30 tools com status, mutacao, efeito e limite observado.'
  - 'Inventario before/after de wiki, banco, cache, registry e perfil descartavel.'
  - 'Receipt de apply_refactor em fixture com diff e rollback comprovado.'
  - 'Receipt de embedding local com provider, modelo, cache, rede, tempo e tamanho.'
  - 'Receipt multi-repo controlado com repos registrados e resultados cruzados.'
  - 'Receipt install/uninstall Windows em perfil redirecionado.'
  - 'Resultados de testes existentes e smokes de cliente.'
  - 'Matriz comparativa das skills e prompts upstream com owners Dex.'
  - 'Review findings-first e matriz final de prontidao.'
done_criteria:
  - 'Fonte dos quality_gates registrada como PATTERNS.md ppirtv-mcp/mcp-tool-contract, package-hygiene e ppirtv-regression-gate.'
  - 'inputSchema das tools e prompts foi confirmado por MCP real.'
  - 'Erro de tool nao derruba o transporte stdio.'
  - 'As 30 tools foram chamadas ou receberam bloqueio causal, reproduzivel e explicitamente documentado.'
  - 'O grafo completo foi construido e seu valor comparado com um baseline sem MCP.'
  - 'Toda mutacao ocorreu apenas em alvo controlado e possui inventario e rollback.'
  - 'Nenhum segredo, payload privado ou codigo real foi enviado a provedor externo.'
  - 'Os REDs Windows foram preservados e atribuidos somente as superficies afetadas.'
  - 'Nenhuma configuracao, hook ou skill global real foi alterada.'
  - 'O veredito distingue fato confirmado, inferencia, lacuna e risco residual.'
risks:
  - 'O build pode gerar banco e wiki dentro do repositorio; o inventario before/after deve tornar o efeito rastreavel.'
  - 'O runtime pode preaquecar embeddings e baixar modelo mesmo sem chamada explicita.'
  - 'apply_refactor_tool usa dry_run false por default e deve receber somente caminho descartavel.'
  - 'Installer upstream pode tocar HOME, hooks, AGENTS e gitignore; o perfil real permanece fora de alcance.'
  - 'Registry multi-repo default e global; o teste deve redirecionar a raiz ou usar perfil descartavel.'
  - 'bd e exigido pelo AGENTS local, mas nao esta instalado ou disponivel no PATH.'
  - 'A tool spt_validate pode estar configurada no Codex CLI, mas indisponivel como tool conectada nesta janela.'
uncertainties:
  - 'Nao esta provado que todas as tools aceitam redirecionamento completo de storage no Windows.'
  - 'Nao esta provado que ZCode consome todas as extensoes FastMCP usadas pelo servidor.'
  - 'Nao esta provado que as sete skills upstream agregam valor alem dos owners Dex.'
  - 'Nao esta provado que embeddings melhoram suficientemente a busca para justificar cache, rede e dependencias.'
gates:
  - 'spt_validate deve retornar valid=true, contract_version=2, missing=[] e contract_errors=[].'
  - 'Nenhuma fase de mutacao inicia sem inventario before do alvo.'
  - 'Toda chamada mutante deve nomear alvo controlado e caminho de rollback.'
  - 'Egress externo, custo ou uso de segredo exige autorizacao especifica adicional.'
  - 'Falha material retorna para a fase PPIRTV causal.'
  - 'Veredito positivo exige evidencias frescas ligadas a revision e ambiente.'
validation:
  - 'MCP real: tools/list, prompts/list e resources/list.'
  - 'MCP real: build completo, consultas e operacoes mutantes em alvos controlados.'
  - 'Testes Python upstream por superficies core, tools, Windows, refactor e install/uninstall.'
  - 'git status e inventario de arquivos antes e depois.'
  - 'Rollback executado nas fixtures, perfil descartavel e registry controlado.'
  - 'Review findings-first e busca do mesmo padrao em superficies vizinhas.'
execution_prompt: |
  /GOAL
  Execute o Trilho em C:\CodexProjetos\code-review-graph\.agents\PLAN-TASKS\2026-07-28-piloto-amplo-code-review-graph.md no modo full.
  Preserve as fronteiras de alvos controlados, gere evidencias por fase e nao altere o registry global nem os perfis reais dos clientes.
---

# Trilho - Piloto amplo do code-review-graph

Tipo: SPEC-PLAN-TASKs

## Ata resumida

A mesa corrigiu a decisao anterior: riscos localizados nao justificam amputar
a superficie do produto. O piloto deve manter capacidade completa e controlar
o raio de impacto por perfis, registries, fixtures e worktrees descartaveis.

## Decisao de implementacao

Executar a matriz completa antes de decidir adaptacao ou admissao global.

## Escopo

As 30 tools, os 5 prompts, as 7 skills upstream e as superficies Codex, ZCode,
Windows, embeddings, multi-repo, installer e rollback.

## Fora do escopo

Registry global, hooks reais, perfis reais, codigo vivo mutado e egress de
codigo real.

## SPEC

Cada capacidade deve produzir recibo observavel e ser comparada com baseline.
O ambiente pode ser isolado; a capacidade nao pode ser removida sem RED causal.

## PLAN

1. Congelar baseline.
2. Construir e consultar o grafo.
3. Exercitar capacidades mutantes em alvos controlados.
4. Comparar clients, prompts e skills.
5. Revisar, testar, validar e decidir.

## TASKs

- [x] Baseline e tools/list real.
- [x] Grafo completo e consultas.
- [x] Wiki e embeddings locais.
- [x] Refatoracao real em fixture com rollback.
- [x] Multi-repo controlado.
- [x] Installer e clientes em perfis descartaveis.
- [x] Skills e prompts comparados.
- [x] Review, testes e veredito.

## Cooperadores materiais

- `questionador`: pressiona premissas; protege o gate de experimento nao enviesado.
- `chato`: procura lacunas e extrapolacoes; protege o gate de falso seguro.
- `akita-dev-raiz`: separa fundamento, ferramenta e promessa; protege a leitura tecnica do piloto.
- `governancia-skills`: decide pre-admissao e fronteiras; protege o registry global.
- `mapeador-implementacao`: controla alvo, invariantes e ordem; protege as mutacoes do piloto.
- `revisor-codigo`: revisa findings e padroes vizinhos; protege o gate tecnico.
- `tio-testador`: admite somente evidencia executada; protege o gate de teste.
- `validador-pronto`: consolida a matriz final; nao autoriza integracao global.
- `estacionamento` e `garimpeiro`: preservam residuos e ouro com owner e quando.

## Riscos e gates

Os riscos e gates executaveis estao no front matter. O RED de Beads permanece
declarado: `bd` nao foi encontrado no PATH em 2026-07-28.

## Validacao

O piloto somente fecha depois de tools/list real, chamadas funcionais, testes,
rollback e matriz de evidencia ligada a revision e ambiente.

## Evidencia da implementacao controlada

- Recibo MCP real: 30 tools, 5 prompts obtidos por `prompts/get` e 0 resources.
- Grafo estabilizado: 234 arquivos, 4.979 nos, 40.782 arestas, 189 fluxos e
  18 comunidades.
- Wiki: 19 paginas, 92.688 bytes.
- Embeddings CLI local: 4.745 nos; MCP `uvx` permaneceu RED por isolamento do
  extra, com `search_mode=none`.
- Refactor em fixture: apply retornou sucesso, omitiu import e quebrou o teste;
  rollback restaurou `FixtureExitCode=0`.
- Multi-repo: dois repos e 11 resultados; ranking segue rank local, nao score
  global.
- Install/uninstall em perfil controlado: rollback de regras GREEN; remocao
  indevida do registry global controlado RED.
- Testes focados: 394 pass e 1 fail antes dos extras dev.
- Suite completa apos extras dev: 2.270 pass, 28 fail, 12 skip e 2 xpass no
  Windows/Python 3.14.
- CI-equivalente Windows estreito: `tests/test_windows_compat.py` passou 1/1.
- Ruff no source: GREEN. Mypy com flags do CI: tres REDs em Windows/Python
  3.14.
- Laudo: `.agents/EVIDENCIAS/2026-07-28-code-review-graph-pilot.md`.
- PPIRTV: flow completo, veredito `pronto_com_ressalvas`,
  `vrd_20260728134911497_0032_0001`.
- Memória: um L1↔L2 forte consolidado; 43 promoções automáticas fracas
  arquivadas recuperavelmente com manifesto.
- RED vizinho de memória: `accept_ledger_only` reclassificou e gravou dois
  duplicados no tema Codex; ambos foram arquivados com suplemento de manifesto.

## Prompt /GOAL para o trilho

`/GOAL Execute C:\CodexProjetos\code-review-graph\.agents\PLAN-TASKS\2026-07-28-piloto-amplo-code-review-graph.md em modo full.`
