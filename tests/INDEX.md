# Testes do CRG

↩ [Nível acima](../INDEX.md)

- [Verificação de merge](test_merge_check.py) — integração pela CLI, cobertura parcial, repetição e saída CP1252.
- [Saídas do install ignoradas](test_install_outputs_are_ignored.py) — o que `install` escreve no checkout não aparece no `git status`; também proíbe arquivo rastreado em caminho ignorado (por isso nunca `git add -f` sob `.agents/receipts/`).
- [Diff do parser](test_parser_diff.py) — `tools/parser_diff.py`: despejo, comparação por arquivo, gate `--expect-identical` e a tríade.
