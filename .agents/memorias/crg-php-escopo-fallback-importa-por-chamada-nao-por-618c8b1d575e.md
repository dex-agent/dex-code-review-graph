---
implementation_version: v2
layer: L2
slug: crg-php-escopo-fallback-importa-por-chamada-nao-por-618c8b1d575e
tags:
  - "#crg/php-resolver"
  - "#crg/coverage"
---

# CRG-PHP-ESCOPO-FALLBACK importa por chamada, não por arquivo

Em d6a1df0, o probe histórico crg-phpunit-adversarial/graph/probe.py reproduz Shipping ligado ao método cujo receiver_scope é App\Payments\Calculator. Há uma segunda rota medida: na fixture sticky_homonym com Payments ausente, acrescente use App\Shipping\Calculator as ShippingCalculator e composer.json com PSR-4 App\ para src/. Desative só resolve_scoped_calls com mock durante o build mínimo, para isolar o fallback genérico. IMPORTS_FROM de Shipping vira caminho absoluto, e _resolve_bare_endpoints liga CALLS add e o TESTED_BY espelhado a Shipping, apesar do receiver_scope Payments; também observamos atribuição bare do construtor Calculator. tests_for devolve o método com indirect=false e sem inferred_by, pois há aresta material errada. O teste de regressão deve cobrir os dois caminhos e consultar o par de nomes qualificados. Preserve a chamada sem resolução quando o alvo explícito não estiver indexado e prove paridade quando o alvo entrar por update. Fontes: code_review_graph/parser.py, scoped_resolver.py, graph.py e tools/query.py. O mock separa causas, não é o teste de aceite.

#crg/php-resolver #crg/coverage

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-php-escopo-fallback-importa-por-chamada-nao-por-618c8b1d575e-content
