---
dex_contract: spt
version: 2
status: 'concluido_com_ressalvas'
owner: 'validador-pronto'
date: '2026-07-31'
workspace: 'C:\CodexProjetos\code-review-graph'
origin: 'pedido do usuario: arqueologia dex do install do escritorio e repeticao no ambiente casa'
goal:
  id: 'replicar-code-review-graph-casa'
  title: 'Replicar no ambiente casa a instalacao do code-review-graph e do bd feita no escritorio'
  objective: 'Entender por arqueologia PPIRTV como o code-review-graph foi instalado no escritorio e repetir o mesmo aqui: bd global, CRG em uv tool com extras, adapter governada, MCP Codex com allowlist produtiva e validacao real.'
context: 'O repo foi importado do escritorio com .agents/.ppirtv/.beads/.code-review-graph e shims de ~/.local/bin, mas sem o venv do uv tool nem o bd instalados; a sessao Codex atual nao carregava o MCP CRG.'
decision: 'Reproduzir o Trilho do escritorio com os mesmos canais oficiais e a mesma allowlist de 25 tools, preservando o grafo existente (HEAD casado) e a adapter ja presente no registry.'
scope:
  include:
    - 'Backups SHA-256 dos alvos globais e locais antes da mudanca.'
    - 'Instalacao global do bd 1.1.2 via npm @beads/bd e bd prime.'
    - 'Instalacao do CRG 2.3.7 via uv tool Python 3.13 com extras [all] e google-genai explicito.'
    - 'Configuracao MCP global+local com allowlist produtiva e env offline.'
    - 'Handshake stdio 25/5/0, codex mcp list/get, smoke de grafo e validacao da adapter.'
    - 'Registro de evidencia, Trilho e memoria recuperavel.'
  exclude:
    - 'Instalacao de hooks upstream no Windows.'
    - 'Exposicao das 5 tools mutantes no perfil produtivo.'
    - 'Push git / bd dolt push (publicacao fora do corte).'
    - 'Correcao de codigo upstream ou alteracao de segredos.'
spec: 'Ao final, bd e CRG devem responder globalmente, o MCP Codex deve expor exatamente a allowlist de 25 tools (5 mutantes ausentes), o handshake stdio deve fechar 25/5/0 e o grafo deve casar com o HEAD.'
plan:
  - 'Arqueologia: SPTs do escritorio, ledger/flows .ppirtv, Git e configs.'
  - 'Backups SHA-256 antes da mudanca.'
  - 'Instalar bd global e criar/reivindicar bead crg-frc.'
  - 'Instalar CRG via uv tool e provar versao, imports e pip check.'
  - 'Configurar MCP global+local com allowlist e env offline.'
  - 'Provar codex mcp list/get, handshake stdio e smoke de grafo.'
  - 'Validar adapter no registry e registrar evidencia/Trilho/memoria.'
tasks:
  - 'Arqueologia dex-arqueologia-evolutiva-ppirtv concluida (parcial, sem ppirtv_trace).'
  - 'Backups SHA-256 registrados.'
  - 'bd 1.1.2 global + bd prime + bead crg-frc.'
  - 'CRG 2.3.7 uv tool + imports + uv pip check.'
  - 'MCP global configurado e codex mcp list/get verdes.'
  - 'Handshake stdio 25/5/0 e smoke 5006/40981 no HEAD.'
  - 'Adapter validada e evidencias registradas.'
validation:
  - 'bd --version, bd prime, bd show crg-frc.'
  - 'code-review-graph --version, uv tool list, uv pip check, imports.'
  - 'codex mcp list/get com allowlist e env.'
  - 'mcp-handshake.mjs: 25 tools, 5 prompts, 0 resources, exit 0.'
  - 'code-review-graph status/architecture no repo.'
  - 'quick_validate.py na adapter.'
done_criteria:
  - 'bd 1.1.2 e CRG 2.3.7 globais respondendo.'
  - 'MCP expoe exatamente a allowlist produtiva sem as 5 tools mutantes.'
  - 'Handshake real 25/5/0 e grafo casado com HEAD.'
  - 'Evidencia, Trilho e memoria recuperaveis registrados.'
risks:
  - 'Sessao Codex Desktop atual precisa restart/reconnect para carregar o MCP.'
  - 'Perfil offline depende de cache MiniLM local (falha explicita sem cache).'
  - 'Publicacao git/dolt permanece pendente de autorizacao.'
execution_prompt: |
  /GOAL
  Execute o Trilho em C:\CodexProjetos\code-review-graph\.agents\PLAN-TASKS\2026-07-31-replicar-code-review-graph-casa.md em modo full.
  Reproduza no ambiente casa o install do escritorio (bd + CRG uv tool + MCP allowlist), preserve o grafo existente e nao publique git/dolt sem autorizacao.
---

# Trilho — replicação casa do code-review-graph

Tipo: SPEC-PLAN-TASKs

## Resultado

Instalação replicada e validada em 2026-07-31. Detalhes e recibos no laudo
`.agents/EVIDENCIAS/2026-07-31-code-review-graph-home-replication.md`.

## Próximo passo

Reiniciar/reconectar o Codex Desktop para a sessão carregar o MCP CRG e, em
seguida, usar a adapter em uma revisão real de baixo risco (mesmo próximo passo
do escritório). Quando o usuário autorizar, publicar commit/beads via git e
`bd dolt push`.

