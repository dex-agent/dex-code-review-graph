# Lembranças


- Ao revisar um único arquivo com changed_files e surgirem símbolos de outros arquivos no Code Review Graph. -> [CRG-DIFF-RECORTE-VAZA](memorias/crg-diff-recorte-vaza.md) [[memorias/crg-diff-recorte-vaza|CRG-DIFF-RECORTE-VAZA]] #crg/diff ^crg-diff-recorte-vaza

- CRG detect-changes retorna zero para arquivo alterado com espaco ou acento, ou build ignora o arquivo -> [CRG-GIT-PATHS-IDENTIDADE](memorias/crg-git-paths-identidade.md) [[memorias/crg-git-paths-identidade|CRG-GIT-PATHS-IDENTIDADE]] #crg/paths-git ^crg-git-paths-identidade

- CRG-DEPENDENTE-HASH: use quando build resolve a aresta e update deixa o destino antigo depois de mudar import ou reexportacao. -> [Hash do dependente nao atesta frescor das arestas](memorias/crg-dependente-hash-aresta.md) [[memorias/crg-dependente-hash-aresta|Hash do dependente nao atesta frescor das arestas]] #crg/incremental #crg/reexportacao ^crg-dependente-hash-aresta

- Aprendizado de projeto local CRG-PHPUNIT-WINDOWS: quando tests_for omite PHPUnit no Windows, con -> [Aprendizado de projeto local CRG-PHPUNIT-WINDOWS: quando tests_for omite PHPUnit no Windows, con](memorias/aprendizado-de-projeto-local-crg-phpunit-windows-qu-5cd693d51260.md) [[memorias/aprendizado-de-projeto-local-crg-phpunit-windows-qu-5cd693d51260|Aprendizado de projeto local CRG-PHPUNIT-WINDOWS: quando tests_for omite PHPUnit no Windows, con]] #crg/phpunit-windows ^aprendizado-de-projeto-local-crg-phpunit-windows-qu-5cd693d51260

- Mantenedor CRG: reconciliar os 24 IDs Windows no crg-iu1 antes do próximo release Windows. -> [Mantenedor CRG: reconciliar os 24 IDs Windows no crg-iu1 antes do próximo release Windows.](memorias/mantenedor-crg-reconciliar-os-24-ids-windows-no-crg-68baeee331a7.md) [[memorias/mantenedor-crg-reconciliar-os-24-ids-windows-no-crg-68baeee331a7|Mantenedor CRG: reconciliar os 24 IDs Windows no crg-iu1 antes do próximo release Windows.]] #crg/phpunit-windows ^mantenedor-crg-reconciliar-os-24-ids-windows-no-crg-68baeee331a7

- Achado de review: A expectativa da fixture com separadores misturados foi corrigida e o método d -> [Achado de review: A expectativa da fixture com separadores misturados foi corrigida e o método d](memorias/achado-de-review-a-expectativa-da-fixture-com-separ-baf08bb65555.md) [[memorias/achado-de-review-a-expectativa-da-fixture-com-separ-baf08bb65555|Achado de review: A expectativa da fixture com separadores misturados foi corrigida e o método d]] #crg/phpunit-windows ^achado-de-review-a-expectativa-da-fixture-com-separ-baf08bb65555

- Quando revisar classificacao de testes por caminho no CRG ou corrigir _is_test_file apos 92fdfe0 -> [CRG-TEST-PATH raiz e componente real no detector de testes](memorias/crg-test-path-raiz-e-componente-real-no-detector-de-d97f9193df09.md) [[memorias/crg-test-path-raiz-e-componente-real-no-detector-de-d97f9193df09|CRG-TEST-PATH raiz e componente real no detector de testes]] #crg/test-path ^crg-test-path-raiz-e-componente-real-no-detector-de-d97f9193df09

- Quando update do CRG marcar SHA atual apos mudanca de parser ou quando tests_for for usado como evidencia direta -> [CRG-INDEX-PARSER-SEMANTICS SHA atual exige prova do no e da aresta](memorias/crg-index-parser-semantics-sha-atual-exige-prova-do-2177cbfc69d8.md) [[memorias/crg-index-parser-semantics-sha-atual-exige-prova-do-2177cbfc69d8|CRG-INDEX-PARSER-SEMANTICS SHA atual exige prova do no e da aresta]] #crg/index-semantics ^crg-index-parser-semantics-sha-atual-exige-prova-do-2177cbfc69d8

- Quando corrigir crg-x6m, receiver_scope PHP, Composer PSR-4, single_match ou atribuição de CALLS e TESTED_BY a homônimos. -> [CRG-PHP-ESCOPO-FALLBACK importa por chamada, não por arquivo](memorias/crg-php-escopo-fallback-importa-por-chamada-nao-por-618c8b1d575e.md) [[memorias/crg-php-escopo-fallback-importa-por-chamada-nao-por-618c8b1d575e|CRG-PHP-ESCOPO-FALLBACK importa por chamada, não por arquivo]] #crg/php-resolver #crg/coverage ^crg-php-escopo-fallback-importa-por-chamada-nao-por-618c8b1d575e

- Quando reconstruir, substituir ou promover um banco CRG que já tem embeddings. -> [CRG-REBUILD-PRESERVA-EMBEDDINGS no candidato isolado](memorias/crg-rebuild-preserva-embeddings-no-candidato-isolad-ddbe87c32bec.md) [[memorias/crg-rebuild-preserva-embeddings-no-candidato-isolad-ddbe87c32bec|CRG-REBUILD-PRESERVA-EMBEDDINGS no candidato isolado]] #crg/indice #crg/embeddings ^crg-rebuild-preserva-embeddings-no-candidato-isolad-ddbe87c32bec

- CRG-JULIA-ASSERT-CAMINHO quando uma asserção de aresta positiva ou negativa passa em POSIX e usa identidade de caminho em Windows -> [CRG-JULIA-ASSERT-CAMINHO — teste negativo precisa de caminho nativo](memorias/crg-julia-assert-caminho.md) [[memorias/crg-julia-assert-caminho|CRG-JULIA-ASSERT-CAMINHO — teste negativo precisa de caminho nativo]] #crg/julia #crg/portabilidade ^crg-julia-assert-caminho

- CRG-FORGET-IDENTIDADE-PASTA: esquecer pasta Windows por grafia alternativa ou preservar homônimas e prefixos vizinhos -> [Forget literal usa identidade da pasta](memorias/forget-literal-usa-identidade-da-pasta-25856efd39ca.md) [[memorias/forget-literal-usa-identidade-da-pasta-25856efd39ca|Forget literal usa identidade da pasta]] #crg/forget #windows/caminhos ^forget-literal-usa-identidade-da-pasta-25856efd39ca

- CRG-RAIZ-INDICE-EXTERNO: build ou search rejeita pasta sem Git quando o graph.db está em --data-dir externo -> [Raiz CRG e índice externo têm identidades diferentes](memorias/raiz-crg-e-indice-externo-tem-identidades-diferente-07f33e219cc9.md) [[memorias/raiz-crg-e-indice-externo-tem-identidades-diferente-07f33e219cc9|Raiz CRG e índice externo têm identidades diferentes]] #crg/cli #crg/raiz-projeto ^raiz-crg-e-indice-externo-tem-identidades-diferente-07f33e219cc9

- CRG-CLI-LAUNCHER-SYSCONFIG: WinError 2 no subprocesso de testes da CLI, especialmente fora do virtualenv -> [Launcher dos testes CLI segue a instalação Python](memorias/launcher-dos-testes-cli-segue-a-instalacao-python-805f9a0b7627.md) [[memorias/launcher-dos-testes-cli-segue-a-instalacao-python-805f9a0b7627|Launcher dos testes CLI segue a instalação Python]] #crg/cli #crg/testes ^launcher-dos-testes-cli-segue-a-instalacao-python-805f9a0b7627

- CRG-ARESTA-ENDPOINTS-EXATOS: teste de grafo falha só em Windows com caminhos embutidos em nomes qualificados -> [Identidade de aresta se confirma pelos dois nós persistidos](memorias/identidade-de-aresta-se-confirma-pelos-dois-nos-per-dabb096ff0a0.md) [[memorias/identidade-de-aresta-se-confirma-pelos-dois-nos-per-dabb096ff0a0|Identidade de aresta se confirma pelos dois nós persistidos]] #crg/portabilidade #crg/cli ^identidade-de-aresta-se-confirma-pelos-dois-nos-per-dabb096ff0a0

- CRG-UV-WSL-VENV-ISOLADO: rodar uv no WSL em checkout NTFS compartilhado com Windows -> [WSL precisa de ambiente uv próprio no CRG](memorias/crg-uv-wsl-venv-isolado.md) [[memorias/crg-uv-wsl-venv-isolado|WSL precisa de ambiente uv próprio no CRG]] #crg/portabilidade #python/uv #windows/wsl ^crg-uv-wsl-venv-isolado

- CRG-UNINSTALL-MODO-EFETIVO: teste de substituição atômica compara chmod POSIX no Windows -> [Preservação de modo começa pelo estado efetivo da fixture](memorias/crg-uninstall-modo-efetivo.md) [[memorias/crg-uninstall-modo-efetivo|Preservação de modo começa pelo estado efetivo da fixture]] #crg/portabilidade #crg/uninstall #python/chmod ^crg-uninstall-modo-efetivo

- CRG-COBERTURA-NOMINAL-CJS — antes de usar o índice para revisar um corpus CommonJS -> [Cobertura nominal de .cjs no CRG](memorias/crg-cobertura-nominal-cjs.md) [[memorias/crg-cobertura-nominal-cjs|Cobertura nominal de .cjs no CRG]] #crg/commonjs #crg/cobertura ^crg-cobertura-nominal-cjs

- CRG-NODE-TEST-LEXICAL: antes de ler Untested em .test.cjs ou .spec.cjs, confronte o binding lexical e o TESTED_BY qualificado. -> [CRG CommonJS: prova lexical de node:test e associação direta](memorias/crg-commonjs-prova-lexical-de-node-test-e-associaca-a956887e0c23.md) [[memorias/crg-commonjs-prova-lexical-de-node-test-e-associaca-a956887e0c23|CRG CommonJS: prova lexical de node:test e associação direta]] #crg/commonjs #crg/testes ^crg-commonjs-prova-lexical-de-node-test-e-associaca-a956887e0c23

- CRG-MERGE-CHECK-ZERO-LACUNAS: merge-tree limpo e zero gaps precedem a prova na suíte declarada -> [Merge textual limpo e zero lacunas exigem suíte no resultado combinado](memorias/merge-limpo-zero-lacunas-suite.md) [[memorias/merge-limpo-zero-lacunas-suite|Merge textual limpo e zero lacunas exigem suíte no resultado combinado]] #crg/merge-check #testes/regressao ^merge-limpo-zero-lacunas-suite

- CURA-CI-VERMELHO-CRG-20261119 · STEPS-CI-PARAM-PRIMEIRO-ERRO · MERGE-ENGOLE-COMMIT-LOG-S-CEGO · PYTHON-I-MATA-LANGUAGE-PACK -> [Cura do CI vermelho cronico do CRG: 11 classes em 4 levas, run verde 44517837083](memorias/cura-do-ci-vermelho-cronico-do-crg-11-classes-em-4-245705d61c79.md) [[memorias/cura-do-ci-vermelho-cronico-do-crg-11-classes-em-4-245705d61c79|Cura do CI vermelho cronico do CRG: 11 classes em 4 levas, run verde 44517837083]] #ci/cura #crg/oficina #metodo/red-first ^cura-do-ci-vermelho-cronico-do-crg-11-classes-em-4-245705d61c79

- bloco-0005-dependabot-orfao-staging-fantasma -> [Bloco 0005 CRG: dependabots orfaos fechados - branch staging fantasma](memorias/bloco-0005-crg-dependabots-orfaos-fechados-branch-s-731b83a4e192.md) [[memorias/bloco-0005-crg-dependabots-orfaos-fechados-branch-s-731b83a4e192|Bloco 0005 CRG: dependabots orfaos fechados - branch staging fantasma]] #crg/oficina ^bloco-0005-crg-dependabots-orfaos-fechados-branch-s-731b83a4e192

- merge-240dex-refs-fantasma-apply-3 -> [Merge 2.4.0-dex fechado - wheel 2.4.0+dex.1 no PATH com receipt e rollback](memorias/merge-2-4-0-dex-fechado-wheel-2-4-0-dex-1-no-path-c-67631ed90d4d.md) [[memorias/merge-2-4-0-dex-fechado-wheel-2-4-0-dex-1-no-path-c-67631ed90d4d|Merge 2.4.0-dex fechado - wheel 2.4.0+dex.1 no PATH com receipt e rollback]] #crg/oficina ^merge-2-4-0-dex-fechado-wheel-2-4-0-dex-1-no-path-c-67631ed90d4d

- grafo-registry-scripts-cross-skill -> [Grafo CRG do codigo dos scripts cross-skill do registry de skills](memorias/grafo-crg-do-codigo-dos-scripts-cross-skill-do-regi-0e5bbc2f5fad.md) [[memorias/grafo-crg-do-codigo-dos-scripts-cross-skill-do-regi-0e5bbc2f5fad|Grafo CRG do codigo dos scripts cross-skill do registry de skills]] #crg/oficina ^grafo-crg-do-codigo-dos-scripts-cross-skill-do-regi-0e5bbc2f5fad

- Ao tocar versao do code-review-graph, ao revisar CI de fork que acompanha upstream por merge, ao commitar em clone ou worktree novo do CRG e o hook do Playbook recusar -> [CRG: bump de versao parcial (3a ocorrencia) curado com dono unico e gate; alarme herdado do upstream fica cego no fork](memorias/crg-bump-de-versao-parcial-3a-ocorrencia-curado-com-e6be04d2a42c.md) [[memorias/crg-bump-de-versao-parcial-3a-ocorrencia-curado-com-e6be04d2a42c|CRG: bump de versao parcial (3a ocorrencia) curado com dono unico e gate; alarme herdado do upstream fica cego no fork]] #code-review-graph/release #code-review-graph/ci #code-review-graph/hook ^crg-bump-de-versao-parcial-3a-ocorrencia-curado-com-e6be04d2a42c

- CRG-PR6-EFFECT-FN-MERGEADO-20261123 -> [PR #6 do CRG: Effect.fn revisado, lapidado, re-autorado e mergeado](memorias/pr-6-do-crg-effect-fn-revisado-lapidado-re-autorado-5a824c43bcdc.md) [[memorias/pr-6-do-crg-effect-fn-revisado-lapidado-re-autorado-5a824c43bcdc|PR #6 do CRG: Effect.fn revisado, lapidado, re-autorado e mergeado]] #crg/pr #crg/parser-typescript #projeto/estado ^pr-6-do-crg-effect-fn-revisado-lapidado-re-autorado-5a824c43bcdc

- SONDA-E-SCRIPT-SEGUEM-DEX-TOOLSBOOK -> [Sonda e script de prova seguem o dex-toolsbook: reuso antes, triade, ficha; ferramenta mora em tools](memorias/sonda-e-script-de-prova-seguem-o-dex-toolsbook-reus-1dfc5c64c85d.md) [[memorias/sonda-e-script-de-prova-seguem-o-dex-toolsbook-reus-1dfc5c64c85d|Sonda e script de prova seguem o dex-toolsbook: reuso antes, triade, ficha; ferramenta mora em tools]] #crg/ferramenta #dex-toolsbook/regra #agente/comportamento ^sonda-e-script-de-prova-seguem-o-dex-toolsbook-reus-1dfc5c64c85d

- RELATORIO-DISTINGUE-ALTERADO-DE-CRIADO -> [Relatorio distingue arquivo alterado de ferramenta criada](memorias/relatorio-distingue-arquivo-alterado-de-ferramenta-02e1d83b5594.md) [[memorias/relatorio-distingue-arquivo-alterado-de-ferramenta-02e1d83b5594|Relatorio distingue arquivo alterado de ferramenta criada]] #agente/comportamento #relatorio/regra ^relatorio-distingue-arquivo-alterado-de-ferramenta-02e1d83b5594

- artefato-em-temp-exige-destino-duravel-no-mesmo-bloco -> [artefato-em-temp-exige-destino-duravel-no-mesmo-bloco](memorias/artefato-em-temp-exige-destino-duravel-no-mesmo-blo-7fcf5ea2eb43.md) [[memorias/artefato-em-temp-exige-destino-duravel-no-mesmo-blo-7fcf5ea2eb43|artefato-em-temp-exige-destino-duravel-no-mesmo-bloco]] #auto-memory/feedback ^artefato-em-temp-exige-destino-duravel-no-mesmo-blo-7fcf5ea2eb43

- crg-240dex-merge-fechado-20261115 -> [crg-240dex-merge-fechado-20261115](memorias/crg-240dex-merge-fechado-20261115-aa9b6b16dbff.md) [[memorias/crg-240dex-merge-fechado-20261115-aa9b6b16dbff|crg-240dex-merge-fechado-20261115]] #auto-memory/project ^crg-240dex-merge-fechado-20261115-aa9b6b16dbff

- crg-35-comandos-prompts-modelos-20261119 -> [crg-35-comandos-prompts-modelos-20261119](memorias/crg-35-comandos-prompts-modelos-20261119-b150c10bbec7.md) [[memorias/crg-35-comandos-prompts-modelos-20261119-b150c10bbec7|crg-35-comandos-prompts-modelos-20261119]] #auto-memory/reference ^crg-35-comandos-prompts-modelos-20261119-b150c10bbec7

- crg-cura-ci-8-classes-20261119 -> [crg-cura-ci-8-classes-20261119](memorias/crg-cura-ci-8-classes-20261119-4f3ee30d7254.md) [[memorias/crg-cura-ci-8-classes-20261119-4f3ee30d7254|crg-cura-ci-8-classes-20261119]] #auto-memory/project ^crg-cura-ci-8-classes-20261119-4f3ee30d7254

- crg-grafo-registry-scripts-20261117 -> [crg-grafo-registry-scripts-20261117](memorias/crg-grafo-registry-scripts-20261117-5fe109962211.md) [[memorias/crg-grafo-registry-scripts-20261117-5fe109962211|crg-grafo-registry-scripts-20261117]] #auto-memory/project ^crg-grafo-registry-scripts-20261117-5fe109962211

- crg-path-240-oficial -> [crg-path-240-oficial](memorias/crg-path-240-oficial-af4c4c133542.md) [[memorias/crg-path-240-oficial-af4c4c133542|crg-path-240-oficial]] #auto-memory/project ^crg-path-240-oficial-af4c4c133542

- crg-piloto-adapter-veredito-20261114 -> [crg-piloto-adapter-veredito-20261114](memorias/crg-piloto-adapter-veredito-20261114-3423b9460083.md) [[memorias/crg-piloto-adapter-veredito-20261114-3423b9460083|crg-piloto-adapter-veredito-20261114]] #auto-memory/project ^crg-piloto-adapter-veredito-20261114-3423b9460083

- crg-pr6-effect-fn-revisao-20261123 -> [crg-pr6-effect-fn-revisao-20261123](memorias/crg-pr6-effect-fn-revisao-20261123-a715e7b80c99.md) [[memorias/crg-pr6-effect-fn-revisao-20261123-a715e7b80c99|crg-pr6-effect-fn-revisao-20261123]] #auto-memory/project ^crg-pr6-effect-fn-revisao-20261123-a715e7b80c99

- crg-versao-uma-fonte-gates-cegos-20261123 -> [crg-versao-uma-fonte-gates-cegos-20261123](memorias/crg-versao-uma-fonte-gates-cegos-20261123-675313426b00.md) [[memorias/crg-versao-uma-fonte-gates-cegos-20261123-675313426b00|crg-versao-uma-fonte-gates-cegos-20261123]] #auto-memory/project ^crg-versao-uma-fonte-gates-cegos-20261123-675313426b00

- dado-herdado-de-resumo-e-hipotese-reexecutar -> [dado-herdado-de-resumo-e-hipotese-reexecutar](memorias/dado-herdado-de-resumo-e-hipotese-reexecutar-c5be2e1ed932.md) [[memorias/dado-herdado-de-resumo-e-hipotese-reexecutar-c5be2e1ed932|dado-herdado-de-resumo-e-hipotese-reexecutar]] #auto-memory/feedback ^dado-herdado-de-resumo-e-hipotese-reexecutar-c5be2e1ed932

- dex-audio-motor-contrato-novo-20261121 -> [dex-audio-motor-contrato-novo-20261121](memorias/dex-audio-motor-contrato-novo-20261121-afec3eca0d8f.md) [[memorias/dex-audio-motor-contrato-novo-20261121-afec3eca0d8f|dex-audio-motor-contrato-novo-20261121]] #auto-memory/reference ^dex-audio-motor-contrato-novo-20261121-afec3eca0d8f

- dex-ignore-auditoria-registry-20261114 -> [dex-ignore-auditoria-registry-20261114](memorias/dex-ignore-auditoria-registry-20261114-58706b71e0bd.md) [[memorias/dex-ignore-auditoria-registry-20261114-58706b71e0bd|dex-ignore-auditoria-registry-20261114]] #auto-memory/project ^dex-ignore-auditoria-registry-20261114-58706b71e0bd

- entropia-conserta-na-descoberta-20261116 -> [entropia-conserta-na-descoberta-20261116](memorias/entropia-conserta-na-descoberta-20261116-6b6c163b7d99.md) [[memorias/entropia-conserta-na-descoberta-20261116-6b6c163b7d99|entropia-conserta-na-descoberta-20261116]] #auto-memory/feedback ^entropia-conserta-na-descoberta-20261116-6b6c163b7d99

- github-auditoria-executada-crg-20261119 -> [github-auditoria-executada-crg-20261119](memorias/github-auditoria-executada-crg-20261119-e0e5ca2698f2.md) [[memorias/github-auditoria-executada-crg-20261119-e0e5ca2698f2|github-auditoria-executada-crg-20261119]] #auto-memory/project ^github-auditoria-executada-crg-20261119-e0e5ca2698f2

- github-auditoria-repo-online-prompt-20261119 -> [github-auditoria-repo-online-prompt-20261119](memorias/github-auditoria-repo-online-prompt-20261119-e5a03f701696.md) [[memorias/github-auditoria-repo-online-prompt-20261119-e5a03f701696|github-auditoria-repo-online-prompt-20261119]] #auto-memory/reference ^github-auditoria-repo-online-prompt-20261119-e5a03f701696

- identidade-git-dex-agent-rewrite-20261121 -> [identidade-git-dex-agent-rewrite-20261121](memorias/identidade-git-dex-agent-rewrite-20261121-0cd25611ea22.md) [[memorias/identidade-git-dex-agent-rewrite-20261121-0cd25611ea22|identidade-git-dex-agent-rewrite-20261121]] #auto-memory/project ^identidade-git-dex-agent-rewrite-20261121-0cd25611ea22

- merge-check-gatilho-prompt-pronto-20261116 -> [merge-check-gatilho-prompt-pronto-20261116](memorias/merge-check-gatilho-prompt-pronto-20261116-49f29c8892ec.md) [[memorias/merge-check-gatilho-prompt-pronto-20261116-49f29c8892ec|merge-check-gatilho-prompt-pronto-20261116]] #auto-memory/project ^merge-check-gatilho-prompt-pronto-20261116-49f29c8892ec

- ppirtv-mcp-stdio-harness-review-envelope -> [ppirtv-mcp-stdio-harness-review-envelope](memorias/ppirtv-mcp-stdio-harness-review-envelope-9e3fbefacaae.md) [[memorias/ppirtv-mcp-stdio-harness-review-envelope-9e3fbefacaae|ppirtv-mcp-stdio-harness-review-envelope]] #auto-memory/reference ^ppirtv-mcp-stdio-harness-review-envelope-9e3fbefacaae

- ppirtv-tracker-0012-attribution-verdict-20261117 -> [ppirtv-tracker-0012-attribution-verdict-20261117](memorias/ppirtv-tracker-0012-attribution-verdict-20261117-5e9c6a2c805e.md) [[memorias/ppirtv-tracker-0012-attribution-verdict-20261117-5e9c6a2c805e|ppirtv-tracker-0012-attribution-verdict-20261117]] #auto-memory/project ^ppirtv-tracker-0012-attribution-verdict-20261117-5e9c6a2c805e

- reconhecimento-code-review-graph -> [reconhecimento-code-review-graph](memorias/reconhecimento-code-review-graph-641357db608d.md) [[memorias/reconhecimento-code-review-graph-641357db608d|reconhecimento-code-review-graph]] #auto-memory/project ^reconhecimento-code-review-graph-641357db608d

- registry-governanca-3505-guarda-plaquinhas -> [registry-governanca-3505-guarda-plaquinhas](memorias/registry-governanca-3505-guarda-plaquinhas-c9be73967e8f.md) [[memorias/registry-governanca-3505-guarda-plaquinhas-c9be73967e8f|registry-governanca-3505-guarda-plaquinhas]] #auto-memory/project ^registry-governanca-3505-guarda-plaquinhas-c9be73967e8f

- regra-oraculo-solid-fechamento-analise-lentes-go-padrao -> [regra-oraculo-solid-fechamento-analise-lentes-go-padrao](memorias/regra-oraculo-solid-fechamento-analise-lentes-go-pa-0e3723b2e1f9.md) [[memorias/regra-oraculo-solid-fechamento-analise-lentes-go-pa-0e3723b2e1f9|regra-oraculo-solid-fechamento-analise-lentes-go-padrao]] #auto-memory/feedback ^regra-oraculo-solid-fechamento-analise-lentes-go-pa-0e3723b2e1f9

- relatorios-distinguem-arquivo-alterado-de-ferramenta-criada -> [relatorios-distinguem-arquivo-alterado-de-ferramenta-criada](memorias/relatorios-distinguem-arquivo-alterado-de-ferrament-2d1ead95e14a.md) [[memorias/relatorios-distinguem-arquivo-alterado-de-ferrament-2d1ead95e14a|relatorios-distinguem-arquivo-alterado-de-ferramenta-criada]] #auto-memory/feedback ^relatorios-distinguem-arquivo-alterado-de-ferrament-2d1ead95e14a

- revisao-adversarial-workflow-prompt-20261117 -> [revisao-adversarial-workflow-prompt-20261117](memorias/revisao-adversarial-workflow-prompt-20261117-1ad0d1b00791.md) [[memorias/revisao-adversarial-workflow-prompt-20261117-1ad0d1b00791|revisao-adversarial-workflow-prompt-20261117]] #auto-memory/reference ^revisao-adversarial-workflow-prompt-20261117-1ad0d1b00791

- triade-cli-argparse-required-e-library-importada -> [triade-cli-argparse-required-e-library-importada](memorias/triade-cli-argparse-required-e-library-importada-6ab419a079fa.md) [[memorias/triade-cli-argparse-required-e-library-importada-6ab419a079fa|triade-cli-argparse-required-e-library-importada]] #auto-memory/project ^triade-cli-argparse-required-e-library-importada-6ab419a079fa

- untangle-codebase-com-crg-regimes-20261117 -> [untangle-codebase-com-crg-regimes-20261117](memorias/untangle-codebase-com-crg-regimes-20261117-a458223d46a1.md) [[memorias/untangle-codebase-com-crg-regimes-20261117-a458223d46a1|untangle-codebase-com-crg-regimes-20261117]] #auto-memory/project ^untangle-codebase-com-crg-regimes-20261117-a458223d46a1

- zcode-session-db-lookup-receita-20261117 -> [zcode-session-db-lookup-receita-20261117](memorias/zcode-session-db-lookup-receita-20261117-4f91200015de.md) [[memorias/zcode-session-db-lookup-receita-20261117-4f91200015de|zcode-session-db-lookup-receita-20261117]] #auto-memory/reference ^zcode-session-db-lookup-receita-20261117-4f91200015de

- espelho-auto-memory-mjs-ferramenta-canonica -> [espelho-auto-memory-mjs-ferramenta-canonica](memorias/espelho-auto-memory-mjs-ferramenta-canonica-6c0a07084f49.md) [[memorias/espelho-auto-memory-mjs-ferramenta-canonica-6c0a07084f49|espelho-auto-memory-mjs-ferramenta-canonica]] #auto-memory/reference ^espelho-auto-memory-mjs-ferramenta-canonica-6c0a07084f49

- regra-repetida-pelo-dono-vira-gate-nao-novo-id -> [regra-repetida-pelo-dono-vira-gate-nao-novo-id](memorias/regra-repetida-pelo-dono-vira-gate-nao-novo-id-1e0c689f2260.md) [[memorias/regra-repetida-pelo-dono-vira-gate-nao-novo-id-1e0c689f2260|regra-repetida-pelo-dono-vira-gate-nao-novo-id]] #auto-memory/feedback ^regra-repetida-pelo-dono-vira-gate-nao-novo-id-1e0c689f2260

- crg-ci-macos-runner-nao-adquirido-e-infra -> [crg-ci-macos-runner-nao-adquirido-e-infra](memorias/crg-ci-macos-runner-nao-adquirido-e-infra-360dfb906aa1.md) [[memorias/crg-ci-macos-runner-nao-adquirido-e-infra-360dfb906aa1|crg-ci-macos-runner-nao-adquirido-e-infra]] #auto-memory/reference ^crg-ci-macos-runner-nao-adquirido-e-infra-360dfb906aa1
- temp-da-maquina-e-staging-implicita-inventario-no-registry -> [temp-da-maquina-e-staging-implicita-inventario-no-registry](memorias/temp-da-maquina-e-staging-implicita-inventario-no-r-d920dcb4ee15.md) [[memorias/temp-da-maquina-e-staging-implicita-inventario-no-r-d920dcb4ee15|temp-da-maquina-e-staging-implicita-inventario-no-registry]] #auto-memory/project ^temp-da-maquina-e-staging-implicita-inventario-no-r-d920dcb4ee15

- hash-em-git-bash-leitura-binaria-nao-sha256sum-cut -> [hash-em-git-bash-leitura-binaria-nao-sha256sum-cut](memorias/hash-em-git-bash-leitura-binaria-nao-sha256sum-cut-960b5ebace67.md) [[memorias/hash-em-git-bash-leitura-binaria-nao-sha256sum-cut-960b5ebace67|hash-em-git-bash-leitura-binaria-nao-sha256sum-cut]] #auto-memory/reference ^hash-em-git-bash-leitura-binaria-nao-sha256sum-cut-960b5ebace67

- tamanho-citado-sai-de-uma-medicao-em-bytes-com-unidade -> [tamanho-citado-sai-de-uma-medicao-em-bytes-com-unidade](memorias/tamanho-citado-sai-de-uma-medicao-em-bytes-com-unid-d90234c2269a.md) [[memorias/tamanho-citado-sai-de-uma-medicao-em-bytes-com-unid-d90234c2269a|tamanho-citado-sai-de-uma-medicao-em-bytes-com-unidade]] #auto-memory/feedback ^tamanho-citado-sai-de-uma-medicao-em-bytes-com-unid-d90234c2269a

- crg-path-dex4-sync-troca-e-prova -> [crg-path-dex4-sync-troca-e-prova](memorias/crg-path-dex4-sync-troca-e-prova-7504a50533f2.md) [[memorias/crg-path-dex4-sync-troca-e-prova-7504a50533f2|crg-path-dex4-sync-troca-e-prova]] #auto-memory/project ^crg-path-dex4-sync-troca-e-prova-7504a50533f2
