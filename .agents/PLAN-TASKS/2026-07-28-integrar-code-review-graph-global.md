---
dex_contract: spt
version: 2
status: 'concluido_com_ressalvas'
owner: 'sprinter'
date: '2026-07-28'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'proposta de integração aprovada explicitamente pelo usuário'
goal:
  id: 'integrar-code-review-graph-global'
  title: 'Integrar code-review-graph global com adapter governada'
  objective: 'Disponibilizar o code-review-graph e o bd globalmente no Windows, conectar o MCP ao Codex em perfil de análise e admitir uma única skill adaptadora governada com rollback comprovado.'
context: 'O piloto amplo concluiu ADAPTAR E PILOTAR: o CRG agrega grafo estrutural de código, mas possui REDs causais em apply_refactor, hooks Windows, uninstall compartilhado, isolamento uvx e prewarm de embeddings.'
problem: 'O MCP atual usa uvx e não compartilha os extras instalados; bd está ausente; o registry ainda não possui owner e autoridade negativa explícitos para o CRG.'
decision: 'Instalar bd e CRG globalmente em runtimes reutilizáveis, instalar todos os extras do CRG no mesmo uv tool, filtrar a superfície produtiva pelo --tools nativo, criar uma adapter única code-review-graph e preservar Graphify e skills existentes como owners de seus domínios.'
scope:
  include:
    - 'Instalação global oficial do bd e smoke com bd prime.'
    - 'Instalação global do code-review-graph 2.3.7 por uv tool a partir da revisão local auditada, com todos os extras e google-genai explícito no mesmo runtime.'
    - 'Backup e troca da configuração global do MCP code-review-graph no Codex Desktop e CLI, que compartilham config.toml.'
    - 'Allowlist produtiva de tools estruturais e analíticas via --tools.'
    - 'Criação da skill adaptadora code-review-graph com agents/openai.yaml e referência de política operacional.'
    - 'Pós-admissão em INDEX.md, governança e CHANGELOG do registry.'
    - 'Provas reais de versão, imports opcionais, tools/list, prompts/list, resources/list, build/consulta e rollback documental.'
  exclude:
    - 'Instalação de hooks upstream no perfil real do Windows.'
    - 'Exposição produtiva de apply_refactor_tool, build_or_update_graph_tool, embed_graph_tool, generate_wiki_tool e run_postprocess_tool.'
    - 'Cópia das sete skills upstream para o registry.'
    - 'Substituição de Graphify, owners de review, regressão, contrato, segurança, Delphi ou memória.'
    - 'Configuração do ZCode sem prova independente do cliente.'
    - 'Envio de código ou segredo a embeddings externos.'
    - 'Correção do código upstream ou publicação de release.'
spec: 'Ao final, bd e code-review-graph devem estar resolvíveis globalmente; o Codex deve lançar o executável instalado, não uvx; tools/list deve mostrar somente a allowlist produtiva; a adapter deve declarar owners, consumers, aliases crg-*, autoridade negativa e rota de laboratório; os arquivos globais devem possuir backup e rollback executável.'
plan:
  - 'Congelar estado, revisão, versões, configuração e hashes antes da mudança.'
  - 'Instalar bd globalmente pelo canal oficial e registrar o trabalho no tracker do projeto.'
  - 'Instalar o CRG via uv tool com extras no mesmo ambiente e provar imports.'
  - 'Inicializar e preencher a adapter única, executar pré e pós-admissão governada.'
  - 'Trocar o MCP Codex para o executável global com allowlist produtiva.'
  - 'Revisar alterações e procurar padrões vizinhos de conflito ou mutação.'
  - 'Executar tools/list real, smoke estrutural, validações do registry e rollback documental.'
  - 'Consolidar veredito, estado recuperável, memória forte e próximo passo com quando.'
tasks:
  - 'Criar e validar este SPT v2 com checklist visual.'
  - 'Registrar baseline e backups dos alvos globais.'
  - 'Instalar bd globalmente e executar bd prime.'
  - 'Criar e reivindicar um bead para esta integração.'
  - 'Instalar code-review-graph global por uv tool com todos os extras.'
  - 'Provar imports e executável no runtime uv tool.'
  - 'Criar a skill adaptadora code-review-graph pelo skill-creator.'
  - 'Executar pré-admissão e pós-admissão da Governanta.'
  - 'Atualizar INDEX.md, governança e CHANGELOG do registry.'
  - 'Configurar o MCP global do Codex com allowlist produtiva.'
  - 'Obter initialize, tools/list, prompts/list e resources/list reais.'
  - 'Executar smoke de grafo e consulta pelo runtime instalado.'
  - 'Revisar diff, autoridade negativa e padrão vizinho.'
  - 'Executar validadores da skill, registry e checklist.'
  - 'Provar instruções de rollback sem apagar dados compartilhados.'
  - 'Fechar bead, estado PPIRTV e veredito com evidências.'
expected_evidence:
  - 'Versões e caminhos globais de bd, uv e code-review-graph.'
  - 'bd prime e bead desta integração.'
  - 'uv tool list e imports fastmcp, tree_sitter, sentence_transformers, igraph, matplotlib, google.genai, ollama e jedi no mesmo ambiente.'
  - 'Backup com SHA-256 de config.toml e dos três arquivos centrais do registry.'
  - 'Skill adapter validada por quick_validate.py e agents/openai.yaml coerente.'
  - 'Decisão de pré e pós-admissão da Governanta.'
  - 'codex mcp get/list apontando para o executável global e allowlist.'
  - 'Receipt MCP real com 25 tools produtivas, 5 prompts e 0 resources.'
  - 'Smoke de stats/arquitetura/consulta no repositório auditado.'
  - 'Diff revisado e validações do registry.'
  - 'Mapa exato de rollback preservando ~/.code-review-graph.'
done_criteria:
  - 'Fonte dos quality_gates registrada como PATTERNS.md ppirtv-mcp/mcp-tool-contract, package-hygiene e ppirtv-regression-gate.'
  - 'spt_validate retorna valid=true, contract_version=2, missing=[] e contract_errors=[].'
  - 'bd global responde e o trabalho está rastreado por um bead.'
  - 'O CRG global usa um único ambiente uv tool com todos os extras previstos.'
  - 'O MCP Codex não usa uvx e expõe exatamente a allowlist produtiva.'
  - 'As cinco tools mutantes excluídas não aparecem em tools/list produtivo.'
  - 'A adapter única code-review-graph está localizável, validada e catalogada.'
  - 'Graphify e os owners Dex existentes permanecem explicitamente não substituídos.'
  - 'Nenhum hook upstream, ZCode, segredo ou provedor externo foi alterado.'
  - 'Rollback restaura configuração e registry sem executar uninstall destrutivo nem apagar dados compartilhados.'
  - 'Review, testes e validação final usam evidência fresca ligada à revisão e aos hashes finais.'
risks:
  - 'O prewarm de embeddings no Windows pode acessar Hugging Face e escrever cache já no startup.'
  - 'A instalação local editável deixaria o runtime dependente do worktree; o pacote deve ser instalado como snapshot não editável.'
  - 'O extra google-embeddings não declara google-genai corretamente; a dependência deve ser adicionada explicitamente.'
  - 'A configuração Codex é global e atende Desktop e CLI; erro afeta ambos até rollback.'
  - 'O registry global pode estar sujo; alterações devem ser estreitas e não reverter trabalho alheio.'
  - 'O banco e registry de CRG são compartilhados; uninstall upstream sem keep-data é proibido no rollback.'
  - 'A allowlist reduz mutação produtiva, mas não impede um operador de chamar manualmente o executável completo no laboratório.'
uncertainties:
  - 'A versão atual do bd pode exigir migração da base .beads existente.'
  - 'O uv tool pode escolher Python diferente do Python global; a compatibilidade final será decidida por smoke real.'
  - 'O Codex Desktop pode exigir reinício para carregar a configuração já provada por stdio.'
  - 'O prewarm pode reutilizar cache existente e não produzir novo download nesta execução.'
gates:
  - 'Nenhuma instalação começa antes de spt_validate valid=true.'
  - 'Todo arquivo global alterado possui backup e hash antes da escrita.'
  - 'A instalação do bd usa fonte oficial e canal global reproduzível.'
  - 'A instalação CRG é não editável e inclui google-genai explicitamente.'
  - 'A pré-admissão define slug, domínio, owner, aliases, consumers e autoridade negativa antes da criação da adapter.'
  - 'apply_refactor_tool e outras tools mutantes não entram na allowlist produtiva.'
  - 'Falha material regressa à fase causal e preserva o RED.'
  - 'Veredito positivo exige tools/list real e não aceita somente config ou existência de arquivo.'
validation:
  - 'python do skill-creator quick_validate.py na adapter.'
  - 'Validadores read-only de governancia-skills aplicáveis ao registry.'
  - 'checklist-lint.py no quadro visual.'
  - 'codex mcp list --json e codex mcp get code-review-graph --json.'
  - 'MCP stdio initialize, tools/list, prompts/list e resources/list pelo comando configurado.'
  - 'code-review-graph --version, status e consultas estruturais.'
  - 'bd version, bd prime, bd show e bd ready.'
  - 'git diff/status e busca de padrões vizinhos.'
  - 'Hashes before/after e simulação documental de rollback.'
execution_prompt: |
  /GOAL
  Execute este Trilho em modo full.
  Instale bd e code-review-graph globalmente, crie uma única adapter governada e conecte o Codex em perfil produtivo de análise com allowlist real.
  Não instale hooks upstream, não exponha apply_refactor_tool no perfil produtivo e não apague dados compartilhados no rollback.
---

# Trilho — integração global governada do code-review-graph

Tipo: SPEC-PLAN-TASKs

## Sprint Goal

Disponibilizar `bd` e `code-review-graph` para reuso global e conectar o CRG
ao Codex com superfície produtiva de análise, uma única adapter governada e
rollback comprovado.

## Decisão de pré-admissão

- Slug: `code-review-graph`.
- Classe/domínio: `tool-adapter` para grafo estrutural de código.
- Owner do produto: CRG é owner do grafo estrutural de código persistido em
  `.code-review-graph`.
- Aliases portáveis: `crg`, `crg-structural-graph`, `crg-code-review`.
- Consumers: `mapa-contexto-codigo`, `mapeador-implementacao`,
  `projeto-checar-regressao`, `projeto-checar-quebra-de-contrato`,
  `projeto-auditar-seguranca`, skills de review/refatoração e skills Delphi
  apenas quando a linguagem estiver suportada.
- Autoridade negativa: não substituir Graphify, memória L1/L2/L3, LSP,
  compilador, review, teste, segurança, contrato, Delphi ou validador; não
  aplicar refactor, hooks, wiki, build, postprocess ou embeddings no perfil
  produtivo.
- Composição: importar uma adapter; não importar as sete skills upstream.
- Catalogação: `INDEX.md`, governança e `CHANGELOG.md`; sem promoção Gen3,
  `rich`, especialista ou owner de SPT.

## Checklist visual — dose Quadro

Fonte viva: este SPT e o laudo
`.agents/EVIDENCIAS/2026-07-28-code-review-graph-pilot.md`.
Owner da ordem: `sprinter`.

### P🧠 Pensamentos

- [x] C-01 [CRITÉRIO] Objetivo, owner e fronteiras recuperados | source: SPT anterior + memória viva | owner: sprinter | when: antes do planejamento | evidence: `.agents/PLAN-TASKS/ACTIVE.md` + Finder em duas formas
- [x] R-01 [RISCO] REDs causais preservados sem amputar a instalação global | source: laudo do piloto | owner: chato | when: antes da decisão | evidence: apply_refactor, hooks, uninstall, uvx e prewarm listados no front matter

### P🗂️ Planejamento

- [x] A-01 [AÇÃO] Validar o SPT v2 e iniciar GOAL full | source: contrato SPT v2 | owner: sprinter | when: antes de instalar | evidence: valid=true + `flow_20260728211327716_0036_0001`
- [x] A-02 [AÇÃO] Congelar baseline e backups com SHA-256 | source: gate de reversibilidade | owner: mapeador-implementacao | when: antes da primeira escrita global | depends_on: A-01 | evidence: manifesto before em `.agents/EVIDENCIAS/2026-07-28-code-review-graph-global-integration.md`

### I🛠️ Implementação

- [x] A-03 [AÇÃO] Instalar `bd` global e registrar/reivindicar o bead | source: GitHub gastownhall/beads + AGENTS.md | owner: mapeador-implementacao | when: após A-02 | depends_on: A-02 | evidence: bd 1.1.2 + `crg-4b5`
- [x] A-04 [AÇÃO] Instalar CRG 2.3.7 global por `uv tool` com todos os extras | source: pyproject.toml auditado | owner: mapeador-implementacao | when: após A-02 | depends_on: A-02 | evidence: uv tool + Python 3.13.13 + imports + pip check
- [x] A-05 [AÇÃO] Criar adapter única `code-review-graph` | source: pré-admissão acima | owner: skill-creator | when: após A-02 | depends_on: A-02 | evidence: SKILL.md + agents/openai.yaml + referência
- [x] A-06 [AÇÃO] Catalogar a adapter no registry | source: governancia-skills | owner: governancia-skills | when: após A-05 | depends_on: A-05 | evidence: registry 3.75.5 + admission_complete
- [x] A-07 [AÇÃO] Trocar MCP Codex de `uvx` para executável global e allowlist | source: codex mcp get + CRG --tools | owner: mapeador-implementacao | when: após A-04 | depends_on: A-04 | evidence: config global/local + codex mcp get/list

### R🔎 Revisão

- [x] C-02 [CRITÉRIO] Revisar diffs, owners, aliases, consumers e autoridade negativa | source: arquivos finais | owner: revisor-codigo | when: após A-06 e A-07 | depends_on: A-06,A-07 | evidence: review findings-first da Mesa + Chato
- [x] R-02 [RISCO] Procurar barata vizinha em outras tools mutantes e configs MCP | source: princípio neighboring-pattern | owner: chato | when: durante review | depends_on: C-02 | evidence: 30 tools classificadas; `refactor_tool` analítica

### T🧪 Teste

- [x] C-03 [CRITÉRIO] Provar `bd`, runtime CRG, imports opcionais e skill | source: instalações finais | owner: tio-testador | when: após review | depends_on: C-02 | evidence: versões + pip check + imports + quick_validate; RED 166/1/1 preservado
- [x] C-04 [CRITÉRIO] Provar MCP real com 25 tools, 5 prompts e 0 resources | source: configuração Codex final | owner: tio-testador | when: após A-07 | depends_on: A-07 | evidence: handshake stdio final offline
- [x] C-05 [CRITÉRIO] Provar smoke de grafo/consulta e validadores do registry | source: repo + registry finais | owner: tio-testador | when: após C-03 | depends_on: C-03 | evidence: grafo fresco 5006/40981 + adapter admission_complete

### V✅ Validação

- [x] C-06 [CRITÉRIO] Provar rollback sem `uninstall` destrutivo e sem apagar dados | source: backups A-02 | owner: validador-pronto | when: antes do veredito | depends_on: C-04 | evidence: mapa exato + precondição de hash no laudo
- [x] A-08 [AÇÃO] Fechar bead, estado PPIRTV, checklist e memória forte elegível | source: contratos de fechamento | owner: validador-pronto | when: após todos os critérios | depends_on: C-05,C-06 | evidence: sessão pós-restart 25/5/0 + `crg-4b5` closed + verdict `vrd_20260729090936382_0076_0001` + ACTIVE

### Fora do corte

- [ ] X-01 [RESÍDUO] [OUT] Hooks Windows upstream | source: RED do piloto | owner: estacionamento | when: quando existir teste Windows dedicado | evidence: novo SPT aprovado
- [ ] X-02 [RESÍDUO] [OUT] ZCode | source: lacuna de cliente | owner: estacionamento | when: quando o executável/configuração real do ZCode for identificado | evidence: tools/list no cliente
- [ ] X-03 [RESÍDUO] [OUT] Correção upstream do `apply_refactor` | source: RED causal | owner: estacionamento | when: quando houver patch upstream + teste definition/import/caller/test | evidence: issue/PR e teste verde

## Handoff

O executor deve atualizar este quadro somente com evidência rastreável. Item
fora do corte não bloqueia o objetivo atual. Qualquer divergência material
regressa à fase PPIRTV causal.
