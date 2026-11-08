---
implementation_version: v2
layer: L2
slug: crg-git-paths-identidade
tags:
  - "#crg/paths-git"
---

# CRG-GIT-PATHS-IDENTIDADE

Separe inventario, faixas e recorte. No inventario de arquivos rastreados, git ls-files sem -z escapa nomes UTF-8 e o build pode perder o arquivo. Use git ls-files -z com decodificacao de filesystem. No patch Git, core.quotepath=off preserva UTF-8; remova apenas o tab separador do cabecalho. Na CLI, intersecte o conjunto descoberto antes de analisar. Prova reproduzivel: uv run --no-sync pytest -q -s tests/test_cli.py -k file_scope, com diff A+B e B apenas em nomes simples e com espaco/acento. Fonte: Trilho 2026-11-08-crg-cli-recorte e commit 1e12485.

#crg/paths-git

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-git-paths-identidade-content
