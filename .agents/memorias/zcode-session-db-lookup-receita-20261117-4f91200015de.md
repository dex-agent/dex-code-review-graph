---
implementation_version: v2
layer: L2
slug: zcode-session-db-lookup-receita-20261117-4f91200015de
tags:
  - "#auto-memory/reference"
---

# zcode-session-db-lookup-receita-20261117

Espelho da auto-memory do host ZCode (arquivo zcode-session-db-lookup-receita-20261117.md, tipo reference).

Receita de lookup de sessão ZCode por ID no banco local (read-only)

Para saber O QUE uma sessão ZCode (`sess_<uuid>`) realmente foi — antes de
responder prompt "para esse trabalho sess_x" — interrogar o banco, não
grep em arquivos (grep pegou só menções/comments de terceiros e causou
misatribuição paga ao vivo 2026-11-17: sess_4c9a494d foi confundida com a
janela do workflow revisao-adversarial porque o changelog do .dwf.ts cita a
ID; o projeto real era TRACKER-0012 do dex-PPIRTV).

```python
import sqlite3, json
con = sqlite3.connect('file:C:/Users/Administrator/.zcode/cli/db/db.sqlite?mode=ro', uri=True)
# 1) metadados: workspace (directory), título, timestamps
con.execute("SELECT * FROM session WHERE id=?", ('sess_<uuid>',))
# 2) conteúdo: texto NÃO está em message (vem vazio) — mora na tabela part
con.execute("SELECT p.data FROM part p JOIN message m ON p.message_id=m.id "
            "WHERE m.session_id=? ORDER BY p.id DESC LIMIT N", ('sess_<uuid>',))
# cada part.data é JSON; type 'text'/'reasoning'/'tool_use' — filtrar por type
```

Skill irmã `zcode-listar-sessoes-id-banco-cli` (scripts/listar-sessoes-zcode.py)
só INVENTARIA por workspace (não lê transcrições — fronteira declarada dela);
para as ÚLTIMAS MENSAGENS o caminho é o query direto acima. Banco aberto
sempre `mode=ro`.
Related: [[ppirtv-tracker-0012-attribution-verdict-20261117]]

#auto-memory/reference

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^zcode-session-db-lookup-receita-20261117-4f91200015de-content
