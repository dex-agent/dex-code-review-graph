# Capacidades do recorte de diff

Fotografia: 20261107-crg-diff-recorte. Revisão: 603bdd2 + [patch preservado](../receipts/crg-diff-recorte/produto.patch). Windows, Python 3.13, Git e grafo de teste isolado. Owner: mantenedor da análise de mudanças. Escopo: seleção de símbolos por arquivo; fora: runtime instalado, descoberta geral de fluxos e cobertura global.

| Consumidor e gatilho | Comportamento observável | Oracle e evidência |
| --- | --- | --- |
| Revisor, detect_changes com lista explícita | A+B no diff e A solicitado → só a; só B no diff e A solicitado → zero símbolos, lacunas e risco zero. | Git real como oracle, RED/verde e smoke em [saída dos consumidores](../receipts/crg-diff-recorte/consumidores.txt). |
| Agente, contexto mínimo com lista explícita | Entidades de risco respeitam o mesmo recorte nos dois casos. | Git real + [smoke isolado](../receipts/crg-diff-recorte/consumidores.txt). |

Confirmadas no ambiente local do corte. Instalação/deploy e outras combinações de VCS não foram observados no smoke.
