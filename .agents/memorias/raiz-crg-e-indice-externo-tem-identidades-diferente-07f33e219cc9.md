---
implementation_version: v2
layer: L2
slug: raiz-crg-e-indice-externo-tem-identidades-diferente-07f33e219cc9
tags:
  - "#crg/cli"
  - "#crg/raiz-projeto"
---

# Raiz CRG e índice externo têm identidades diferentes

Raiz do projeto e diretório de armazenamento do índice são conceitos independentes. No HEAD 0ad706e, build --repo com pasta sem Git/SVN funciona no armazenamento padrão e falha com --data-dir externo; com Git o armazenamento externo funciona. Na prova descartável, o caso sem VCS e externo gravou a associação exata no registry e criou SQLite, mas _validate_repo_root recusou a raiz e o banco ficou com zero nós File. search também recusou a raiz porque _find_explicit_repo_root só reconhece marcadores locais. Em alterações futuras, preservar controle sem raiz, subprojeto com marcador próprio e isolamento de armazenamento. Fontes: code_review_graph/cli.py (_find_explicit_repo_root, _handle_data_dir_option), code_review_graph/tools/_common.py (_validate_repo_root), code_review_graph/incremental.py (get_data_dir) e crg-iu1.

#crg/cli #crg/raiz-projeto

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^raiz-crg-e-indice-externo-tem-identidades-diferente-07f33e219cc9-content
