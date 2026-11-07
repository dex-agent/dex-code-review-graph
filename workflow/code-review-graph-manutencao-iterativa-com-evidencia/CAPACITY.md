---
schema: dex.workflow.capacity.v1
fotografia_id: crg-piloto-268e0e1-2026-11-07
fotografia_date: '2026-11-07'
---

# CAPACITY — nascimento da receita local

- Objeto: roteiro de investigação de mudanças no Code Review Graph.
- Corte: Windows/Codex, grafo e Git em 268e0e1, arquivo query.py, piloto em USAGE.md.

## Capacidades observadas

| Capacidade | Owner / consumidor / gatilho | Comportamento e oracle independente | Evidência e limite |
| --- | --- | --- | --- |
| Confrontar a seleção do grafo com o diff | Mantenedor / revisor / análise restrita a um arquivo | Isolar a mudança por Git, consultar CRG e verificar símbolos no código | Controle executado em USAGE.md. Confirmou discrepância em um caso. |
| Rastrear a origem de símbolos fora do recorte | Mantenedor / executor / discrepância confirmada | Git log e blame ligam as linhas a um commit reabrível | d007bc1 explica as linhas do Copilot. O piloto não mede cobertura geral do grafo. |

## Laudo

- Confirmado no piloto: reprodução e atribuição de origem. Sem prova ainda: mudança de produto ponta a ponta, atualização do índice e publicação coordenada dos três mapas.
