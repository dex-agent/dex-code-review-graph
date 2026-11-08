# Estacionamento

## Ativos

### PARK-20260731-01 - Publicação git/dolt da integração casa

- tipo: `publicacao pendente`
- origem: `replicar-code-review-graph-casa`
- status: `promovido`
- motivo: `autorizacao explicita em 2026-11-08; execucao no Trilho crg-repo-privado-higiene-20261108`
- destino: `commit local + git push + bd dolt push`
- owner: `usuario`
- quando: `neste corte de publicacao privada; readback no Trilho de 2026-11-08`

### PARK-20260731-02 - Sessao Codex Desktop precisa restart para carregar o MCP CRG

- tipo: `ativacao de sessao`
- origem: `replicar-code-review-graph-casa`
- status: `concluido`
- motivo: `tools code_review_graph e dex_ppirtv expostas no host em 2026-11-08; runtime_probe confirmou este workspace`
- destino: `nova tools/list na sessao apos restart (get_minimal_context_tool respondendo)`
- owner: `usuario`
- quando: `no proximo restart/reconnect do Codex Desktop`

### PARK-20260731-03 - Aplicar dex_ppirtv workspace-local com bundle V2 (ou decidir global-only)

- tipo: `config drift MCP`
- origem: `ppi-install --verify` (receipt `configuration_drift`)
- status: `promovido`
- motivo: `runtime launcher provado por stdio (32 tools, 14 obrigatorias), mas .codex/config.toml do repo nao declara dex_ppirtv e faltam as env keys do bundle V2`
- garimpo vinculado: `config correta nao prova sessao; handshake stdio e tools do host sao camadas separadas`
- destino: `aplicado em 2026-07-31 via ppi-install --apply (receipt bundle_configured, backup verificado)`
- owner: `ppi-install`
- quando: `resolvido em 2026-07-31; restart do Codex pendente para tools/list do host`

### PARK-20260731-04 - Decisao de sanitizacao do historico .ppirtv (paths Administrator)

- tipo: `decisao de dados`
- origem: `triagem de paths hardcoded`
- status: `ativo`
- motivo: `ledger/flows sao proveniencia PPIRTV do escritorio; reescrever quebraria recibos e hashes`
- garimpo vinculado: `README-PATHS.md documenta a politica; reescrita exige backup e validacao`
- destino: `reescrita sanitizada com backup+validacao, se autorizada`
- owner: `usuario`
- quando: `somente se o usuario autorizar reescrita do historico`

### PARK-20260731-05 - Graphify community labeling falhou por JSON malformado

- tipo: `tropeco upstream`
- origem: `graphify cluster-only --backend gemini` (corpus gatilhos-crg-2026-07-31)
- status: `ativo`
- motivo: `labeling retornou "Unterminated string starting at: line 2 column 6"; fallback Community N funcionou e o grafo segue consultavel`
- garimpo vinculado: `lapidar o contrato do pipeline (retry/JSON explicito/upstream), nao o grafo`
- destino: `retry com backend/JSON explicito ou patch upstream graphify`
- owner: `upstream graphify`
- quando: `na proxima extracao profunda com corpus novo`

### PARK-20260728-02 - Correcões upstream antes da promoção produtiva

- tipo: `divida tecnica upstream`
- origem: `piloto amplo code-review-graph`
- status: `ativo`
- motivo: `apply_refactor omite import; uninstall remove state multi-repo; hooks Codex sao POSIX; extra Google aponta para pacote incompatível; receipts build/stats divergem`
- garimpo vinculado: `cinco achados confirmados por fixture, código, MCP e testes; não descartar como limitação genérica`
- destino: `issues/patches upstream ou adapter guardada`
- owner: `upstream code-review-graph + owner da futura adapter`
- quando: `antes de habilitar apply_refactor, hooks ou uninstall no perfil real`

### PARK-20260728-03 - Contrato ZCode não provado

- tipo: `compatibilidade de cliente`
- origem: `matriz de clientes do piloto`
- status: `ativo`
- motivo: `ZCode não aparece em PLATFORMS e nenhum path/config/tools-list real foi identificado`
- garimpo vinculado: `não inventar arquivo de configuração; a ausência é uma lacuna de contrato, não prova de incompatibilidade definitiva`
- destino: `diagnóstico do runtime ZCode`
- owner: `owner operacional de ZCode`
- quando: `antes de declarar compatibilidade ou editar qualquer configuração ZCode`

## Resolvidos recentes

### PARK-20260728-01 - Beads indisponivel no PATH

- tipo: `dependencia operacional`
- origem: `bd prime` exigido pelo AGENTS local
- status: `concluído`
- garimpo vinculado: `a ausência foi resolvida pelo canal oficial, sem shim improvisado`
- destino: `consumido por crg-4b5`
- owner: `dex-agent`
- quando: `resolvido em 2026-07-28`
- evidência: `bd 1.1.2 global, bd prime e bead crg-4b5`
