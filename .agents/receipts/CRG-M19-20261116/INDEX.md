# crg-m19 — Recorte da CLI 2.4.0+dex.1

Base Git `54efb64c7470002a66a9b8b974d75d2bd6a35ba1`. Windows, Python 3.13.13.
Cada execução da CLI fez build em banco novo com `CRG_DATA_DIR` separado.
O teste usa o executável instalado na venv e confere os símbolos com o patch Git.

O commit `c6146110` foi confirmado em `origin/main`. O flow
`flow_20261116181924488_0001_0001` terminou com o veredito
`vrd_20261116182752984_0027_0001` (`pronto_com_ressalvas`).

| Artefato | SHA-256 |
| --- | --- |
| Wheel da base | `93a5d18b8b649b3c34c494d29f34dc4ce30c48c13d0d6a2e8cf482feedc6344f` |
| Wheel corrigido | `25eb9f0ea737100e2105dce6c3a783b2eb2e575277b7968f0c758de7467df511` |

- [RED](red.txt) — `pytest -q -s --tb=short tests/test_cli.py -k detect_changes_file_scope`, exit 1 por 4 divergências em símbolos e deleções. Os dois controles de recorte sem diff passaram.
- [GREEN e suíte](green.txt) — `pytest -q -s --tb=short --basetemp <diretório sem ancestral com marcador CRG> tests/test_cli.py tests/test_changes.py tests/test_merge_check.py`, exit 0, 99 aprovados.
- Sob a pasta temporária do perfil, um teste de descoberta de raiz falha também no wheel da base, pois sobe até o marcador habitual. A execução final em `C:/Users/Public` retirou esse marcador ancestral da fixture sem alterar o teste ou o ambiente habitual.

## Mapas do corte

**Capacidades.** Para os nomes simples e com espaço/acento, A+B retorna apenas `a`. B sem diff de A retorna zero símbolos. A com deleção em B retorna zero remoções; selecionar B recupera `removed`.

**Decisões.** O filtro atua antes de mapear símbolos e preserva os caminhos que os chamadores explícitos já fornecem. Faixas disponíveis que ficam vazias após aplicar o recorte continuam precisas. O fallback para arquivos inteiros continua disponível quando o diff não fornece faixas.

**Dependências.** A CLI descobre candidatos por Git, cruza com `--files` e chama `analyze_changes`. O analisador restringe o mapa `DiffRanges` antes de consultar nós ou o lado antigo. `update --brief`, `merge-check`, `tools.context` e `tools.review` reutilizam esse analisador. A suíte preserva o contrato de chaves relativas e absolutas.

↩ [Trilho](../../PLAN-TASKS/2026-11-16-crg-m19-recorte-cli.md)
