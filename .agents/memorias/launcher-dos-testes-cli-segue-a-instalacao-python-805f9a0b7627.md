---
implementation_version: v2
layer: L2
slug: launcher-dos-testes-cli-segue-a-instalacao-python-805f9a0b7627
tags:
  - "#crg/cli"
  - "#crg/testes"
---

# Launcher dos testes CLI segue a instalação Python

No CRG, o executável instalado vem de [project.scripts] em pyproject.toml. Resolva pelo diretório sysconfig.get_path('scripts') do interpretador que executa o pytest e pelo sufixo da plataforma. O atalho Path(sys.executable).with_name(...) passou em um venv local, mas a CI Windows 42716760673 falhou com WinError 2 antes de invocar a CLI. A varredura encontrou três fixtures irmãs em tests/test_cli.py; 61ff0da migrou as três. Reproduza com python -m pytest -v tests/test_cli.py no venv e confira o passo Run explicit project root tests no runner Windows, que instala o pacote na distribuição padrão. Veja .agents/receipts/crg-iu1-raiz-externa/ci-windows-launcher-red.txt.

#crg/cli #crg/testes

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^launcher-dos-testes-cli-segue-a-instalacao-python-805f9a0b7627-content
