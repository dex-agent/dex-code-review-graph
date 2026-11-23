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
## js-form-probe (candidate)

Sonda in-process das formas JS/TS que o parser de uma arvore do CRG indexa, para comparar duas arvores do mesmo repo
Quando: Revisar PR que muda o parser JS/TS; reproduzir ISSUE-LOCAL-0010; comparar o comportamento de duas arvores antes de afirmar diferenca

## consulta-tema (reviewed)

Porta unica de consulta aos grafos ricos dos temas de mentores (AprendizadoConsultado), sem abrir graph.json direto
Quando: Toda consulta de conselheiro oraculo-* (clausula GATE-CONSUMO-RELACIONAL); pergunta relacional sobre um tema com grafo registrado

Revisão: warning — external_sources_not_checked; reopen the canonical owner
## validate-evolution-closeout (reviewed)

Gate de fechamento das lentes com PADRAO_EVOLUTIVO (chato, bruninha-agulha, oraculos): so fecha com estado terminal valido
Quando: Antes do veredito de todo bloco com chato, bruninha-agulha ou oraculo-* ativo

Revisão: warning — external_sources_not_checked; reopen the canonical owner
## verificar-teto-cc (reviewed)

Medir complexidade ciclomatica e tamanho por funcao em Python e julgar contra o teto da casa (CC 10, 50 linhas)
Quando: Medir codigo novo ou alterado; comparar duas arvores; conferir ferramenta criada na sessao

Revisão: warning — external_sources_not_checked; reopen the canonical owner
## gh (reviewed)

Ler estado de PR, checks e logs de run do GitHub pela linha de comando
Quando: Revisar PR ou CI de repo do fork; conferir autor e assinatura de commit; ler resultado de run vigiado

Revisão: warning — external_sources_not_checked; reopen the canonical owner
## parser-diff (candidate)

Provar que uma mudanca no parser so mexe onde diz que mexe: diff de nos e arestas, por arquivo, entre duas arvores do CRG sobre os mesmos corpora
Quando: Revisar PR que muda o parser; comparar arvore ou wheel novo contra o atual sobre um corpus local, inclusive privado
