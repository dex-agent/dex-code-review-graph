# USAGE — manutenção do CRG

## Exemplos executados

- 2026-11-07, HEAD e grafo `268e0e1`: `git diff --name-status '573580b^' 573580b` mostrou só `code_review_graph/tools/query.py`. `detect_changes_tool(base="573580b^", changed_files=["code_review_graph/tools/query.py"])` declarou um arquivo e retornou sete símbolos, seis ligados ao Copilot.
- Controle repetido na criação: `detect_changes_tool(base="573580b", changed_files=["code_review_graph/tools/query.py"])` retornou os seis símbolos do Copilot. `git diff --quiet 573580b HEAD -- code_review_graph/tools/query.py` saiu 0. `git log` e `git blame` localizaram `d007bc1` como origem das linhas do Copilot no recorte.
- Evidência recuperável: memória local `CRG-DIFF-RECORTE-VAZA` e revisões Git acima. Estado: reprodução read-only. A correção, a execução completa do PPIRTV e a publicação de três mapas após uma atualização pertencem ao primeiro corte de produto.
