# TOOLSBOOK — índice de consulta

Abra primeiro este índice; depois apenas as fichas pertinentes.
Fonte: TOOLSBOOK.json. Livro completo: TOOLSBOOK.md.
Resumo de descoberta, não prova de adequação nem cobertura total.

## release-version (reviewed)

Um dono para a lista dos 13 arquivos onde a versao e escrita e para a regra de que todos concordam com pyproject.toml
Quando: Bump de versao do CRG; CI vermelho em teste de versao; doctor acusando a propria copia; antes de commitar mudanca de versao; ao escrever teste que precise da lista de stamps ou dos padroes de literal de versao

## pre-commit-hook (reviewed)

Gate de commit do repo: recusa commit com a projecao do Playbook desatualizada ou com a versao diferente entre os arquivos de release
Quando: Todo git commit no clone com core.hooksPath=tools/playbook/hooks; ao investigar commit recusado; ao ativar a trava num clone

## code-review-graph-cli (reviewed)

Consultar o grafo de codigo do repo: o que mudou, o que e afetado e quais testes o grafo enxerga
Quando: Antes e depois de uma mudanca de codigo; ao revisar um diff; ao conferir as copias instaladas

Revisão: warning — external_sources_not_checked; reopen the canonical owner
## chama-o-vigia (reviewed)

Vigiar uma espera longa, como um run de CI, em background e trazer o veredito sem travar o turno
Quando: Toda espera material acima de um minuto: CI, build, teste longo, push

Revisão: warning — external_sources_not_checked; reopen the canonical owner
## uv (reviewed)

Construir wheel e sdist do pacote e instalar a copia do PATH a partir de um wheel local
Quando: Ao republicar a copia instalada do CRG; ao conferir se uv.lock esta em dia com o pyproject

Revisão: warning — external_sources_not_checked; reopen the canonical owner