# Revisão adversarial da associação PHPUnit no Windows

Objeto auditado: código `92fdfe052c2d97755659d1c81a3a1593e204c1c6`, baseline `c3682acb70bfcd15c024a27f60833ac54453db30`, fechamento `03ddddebb03c7691452e33bf9a28b4f14870d288`. O executável foi testado em Windows e em bancos sintéticos isolados.

## Achados reproduzidos

1. **P2, regressão do corte, confiança alta — cobertura falsa pelo caminho.** A normalização do caminho absoluto em `_is_test_file` torna `tests?/` capaz de casar o sufixo de `contest/` e o ancestral literal `tests/` fora da raiz. Em ambos os cenários PHP, os mesmos bytes eram Function e tinham zero arestas no baseline. Agora são Test, com uma aresta e `indirect=false`. O controle em raiz neutra continua Function e a pasta `tests/` interna produz o positivo esperado. TypeScript reproduziu o defeito em `describe`, inclusive criando um nó sintético de teste. [A/B CLI e SQLite](ab-cli.json) · [Harness](reproduce-cli.py) · [Controle TypeScript](parser/probe-ts-path.json) · [Parser](../../../code_review_graph/parser.py#L1807)
2. **P2, adoção de índice existente, confiança alta — SHA atual com classificação anterior.** Build com semântica antiga, update de um arquivo alheio e SHA alinhado deixaram o PHPUnit legítimo como Function sem aresta. O rebuild no mesmo HEAD recuperou Test e associação. Esse fluxo estava fora do recorte comprovado com banco novo. Bead `crg-k4q`. [Seleção incremental](../../../code_review_graph/incremental.py#L1191) · [Prova](graph/probe.json)
3. **P2, associação ambígua, confiança alta — aresta errada que sobrevive ao update.** Um import de Payments ainda sem definição pode ser resolvido para o único Calculator disponível, Shipping, e gravar aresta indevida. Adicionar Payments por update preservou a aresta para Shipping. Rebuild com os dois levou a aresta a Payments. Separadamente, o fallback de nomenclatura pode devolver `indirect=false` com `inferred_by=naming_convention` e zero arestas para o homônimo, uma ressalva de interpretação P3. São caminhos já existentes, agora também alcançados pelo PHPUnit camelCase no Windows. Bead `crg-x6m`. [Fallback](../../../code_review_graph/tools/query.py#L536) · [Resolver](../../../code_review_graph/scoped_resolver.py#L348) · [Prova](graph/probe.json)

## O que o verde anterior cobre

- Os três IDs PHPUnit já existiam e foram adicionados à seleção Windows da CI. A revisão independente repetiu 14 testes PHPUnit e conferiu os seis hashes de evidência.
- A comparação Windows completa confirma 27 → 24 IDs, sem novos IDs no recorte testado. A CI remota também encerrou todos os nove jobs com sucesso no SHA de fechamento. [Recibo](../crg-phpunit-windows/summary.json) · [CI remota](ci-remote.json)
- O controle negativo do corte anterior usava `src` em raiz neutra. Os dois contraexemplos mantêm o conteúdo e mudam a colocação. A prova original de associação cruzou CLI com SQLite. Um `indirect=false` isolado só é insuficiente quando a origem da associação não foi verificada.

## Repertório adversarial para o próximo Trilho

| Caso | Mudar uma variável | Contraprova e expectativa |
| --- | --- | --- |
| T1 — componente | Mesmo PHP em `src`, `contest` e `integrationtests` sob raiz neutra | Todos Function, zero TESTED_BY e consulta direta vazia |
| T2 — limite do checkout | Mover o mesmo checkout de uma raiz neutra para `tests/checkout` e manter `src/Example.php` | Classificação e associação invariantes por caminho relativo. Identidade persistida continua nativa |
| T3 — controles positivos | PHPUnit camelCase em `tests/nested` e marcador explícito `#[Test]` em localização comum | Casos positivos preservados. Conferir a identidade qualificada e a aresta exata |
| T4 — vizinho JS/TS | Repetir T1/T2 com uma função de produção `describe` e callback que chama `sum` | Sem Test sintético e sem associação. Controle positivo em componente `__tests__` |
| T5 — fronteira de API | Chamar parser com raiz, sem raiz e com entrada fora dela. Rodar em Windows e POSIX nativos | Fixar o contrato de classificação por componente sem normalizar o caminho gravado. Conferir `test`, `tests` e `__tests__` na primeira posição. A consulta Windows já passou em oito variantes de arquivo/qualificado, relativo/absoluto e barras nativas/alternativas |
| T6 — índice legado | Build antigo, update vazio, update alheio, update explícito com hash idêntico, edição material e rebuild | Medir SHA, kind e aresta separadamente. Só afirmar atualização da classificação quando os três forem compatíveis |
| T7 — homônimos | Payments e Shipping exportam Calculator.add. Construir com ambos e depois repetir adicionando Payments por update | Conferir alvo qualificado, aresta e `inferred_by` separadamente. Uma heurística sem aresta não é evidência de chamada |
| T8 — verificação do corte | Rodar T1–T4 no executável Windows, a seleção CI e o conjunto histórico restante | Exigir o RED das posições indevidas, GREEN pós-correção e comparação por ID. Manter harness reproduzível no clone |

**Investigação socrática.** Se o código é idêntico, o que mudou para a ferramenta chamar produção de teste? O A/B isolou nome de componente e ancestral fora da raiz. Se o SHA é atual, o que prova que o arquivo específico foi reclassificado? A aresta e o nó antes/depois separam a atualização do metadado da semântica do banco. Se há `indirect=false`, para qual alvo qualificado existe uma aresta? O discriminador do JSON e o SQLite separam heurística de ligação material.

**Oráculo Pragmático — confirmado documental.** Hunt e Thomas, *O Programador Pragmático*, edição PT-BR preservada, Dica 27 (fulltext 2226–2228) e seção 43/Dica 62 (5067–5082), fundamentam testar as condições que escaparam e automatizar os casos úteis. A prova de que o CRG classifica incorretamente vem do A/B, não do livro. Extrações reabertas `range_0093_0128.md` e `range_0245_0282.md`. SHA-256 do PDF confere com o lock da edição.

## Bateria ZCode

Três subagentes internos dividiram parser, grafo/CLI e testes/CI. Externamente, ZCode 0.17.0 recebeu o mesmo bundle sanitizado em 13 perfis e isolou o CWD por rodada. A [matriz](matrix.json) separa preço, conclusão técnica, resposta semântica e adjudicação. As respostas integrais e receipts ficam no disco local em `zcode/<perfil>/`.

- Dez resultados foram tecnicamente verificados, nove entregaram parecer substantivo e um ficou insuficiente. Dots encerrou com erro de runtime. Os dois Gemma encerraram na janela do timeout de 300 s com falha de transporte. Nenhum dos três entregou resposta utilizável.
- O perfil `agent-free.md` exato não existe. Os dois papéis instalados `agent-free-*` e `agent-openrouter-free` usam o mesmo router, cuja seleção interna não foi atestada. Para as respostas verificadas, os metadados identificam a seleção solicitada e o mesmo hash de entrada.
- Agnes e DeepSeek usam provedores customizados de custo não confirmado. Qwen 3.7, Qwen 3.8 e MiMo 2.6 usam variantes `:floor` pagas. O Nemotron Content Safety tem página gratuita, mas o endpoint exato retornou lista de provedores vazia no catálogo vivo. Esses sete perfis constam da matriz, sem despacho.
- `agent-free-code-review` encontrou a fronteira por substring. Outros revisores contribuíram com hipóteses de reparse e homônimos. A contraprova rejeitou a obrigação de usar barra POSIX no nome qualificado, a hipótese de que o ancestral seria irrelevante e a leitura de que 27→24 veio de uma seleção parcial. O A/B sustenta o veredito.

**Decisão.** Corrigir primeiro a regressão de classificação em `crg-08x`, antes de retomar o lote de fixtures em `crg-iu1`. Owner mantenedor CRG, antes do próximo release Windows. Casos T6 e T7 mantêm trilhas de evidência separadas. Revisão sem alteração do código de produto.
