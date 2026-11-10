---
implementation_version: v2
layer: L2
slug: crg-uv-wsl-venv-isolado
tags:
  - "#crg/portabilidade"
  - "#python/uv"
  - "#windows/wsl"
---

# WSL precisa de ambiente uv próprio no CRG

Antes de invocar uv sync ou uv run no WSL sobre o checkout CRG montado em /mnt/c, aponte UV_PROJECT_ENVIRONMENT para um caminho no filesystem Linux, por exemplo /home/crsan/.cache/crg-spring-venv. Sem essa variável, uv run --offline --no-sync --python 3.12 recriou a .venv Windows como Linux. No corte Spring, o ambiente Windows foi refeito com uv sync --python 3.12 --locked --extra dev e pytest passou. Verifique .venv/Scripts/python.exe no Windows e o bin/python Linux fora do checkout antes de rodar provas cruzadas. A chave de isolamento resolve concorrência de ambientes e se aplica a ambientes descartáveis de validação.

#crg/portabilidade #python/uv #windows/wsl

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^crg-uv-wsl-venv-isolado-content
