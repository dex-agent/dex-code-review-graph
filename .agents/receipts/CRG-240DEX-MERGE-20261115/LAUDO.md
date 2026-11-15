# LAUDO — Versão combinada 2.4.0-dex (merge casa × upstream fresco)

Data: 2026-11-15 · Trilho: [2026-11-15-crg-240-dex-merge](../../PLAN-TASKS/2026-11-15-crg-240-dex-merge.md)
Flow: `flow_20261115215507246_0807_0001` · Branch: `release/2.4.0-dex` · Merge: `732b7609`

## Decisão executiva

Unir o melhor das duas linhas: upstream/main fresco `7ba9d17a` (1.249 commits além da
base comum `90d760a`) mesclado na casa (52 commits), preservando os 4 deltas reais e
adotando as implementações upstream onde os dois lados resolveram o mesmo problema
de forma independente.

## Provas (comandos medidos)

| Critério | Prova | Resultado |
| --- | --- | --- |
| C-01 merge | `git log -1 --format="%P" 732b7609` | pais `17d35d47` + `7ba9d17a` ✓ |
| C-02/C-03 joias | `rg -c '"--files"\|merge-check' cli.py` | `--files`×2, merge-check×3, `merge_check.py` presente ✓ |
| C-05 schema | consulta `schema_version` banco novo | 15 (20.411 nós / 141.513+ arestas) ✓ |
| C-06 canário | índice descartável AprendizadoConsultado | 14.714 arquivos, 1.341 nós Test, 9.141 TESTED_BY, `tests_for(run)`=3 ✓ |
| C-07 tests_for | `query tests_for _parse_unified_diff` | 11 resultados ✓ |
| C-08 --files | `detect-changes --base 17d35d47 --files <40>` | exit 0, JSON parseável, 35/35 arquivos no escopo do diff ✓ |
| C-09 wheel | `python -m build --wheel` | `code_review_graph-2.4.0+dex.1-py3-none-any.whl` ✓ |
| C-04 suíte | A/B merged vs upstream puro (mesma máquina/venv/isolamento) | ver c04-suite.txt |

## Dogfooding (a versão combinada revisou o próprio merge)

`detect-changes --brief --base 17d35d47`: risk review funcional, painel Token Savings
4.085.929 → 676.261 tokens (**83% economizados**), e achado REAL: `_sum_signals`
(changes.py:1357, risk 0.85) **sem testes** — gap pré-existente do upstream
(confirmado: nenhum teste em nenhuma das linhas), fielmente exposto pela versão nova.

## Descobertas do corte

1. **Refs locais fantasma**: `8ac8cdc` não existe mais no upstream (história reescrita).
   Regra da casa a partir daqui: comparar upstream SEMPRE via fetch/clone fresco.
2. **Divergência real**: 52 (casa) × 1.249 (upstream) desde `90d760a` — a casa é o lado
   pequeno; merge (não rebase) preserva os hashes que os receipts citam.
3. **Duplicações independentes** (casa adotou upstream): `.cjs` (parser:1252 +
   `[cm]?[jt]sx?` cobre `.test.cjs`), `_configure_utf8_stdio`, ls-files text-mode
   utf-8, re-exports Python, PHPUnit, direção TESTED_BY #515.
4. **Deltas exclusivos da casa preservados**: merge-check três vias (`merge_check.py`
   + wiring), `detect-changes --files` com escopo, PHP por identidade de classe
   lexical (fb9fc22 no scoped_resolver com mirror TESTED_BY), assert posix no uninstall.
5. **PEP 440**: a forma literal "2.4.0-dex.1" é inválida; a canônica equivalente é
   `2.4.0+dex.1` (versão local, ordena após 2.4.0). Registrada aqui a equivalência.
6. **`git apply -3` pode escrever marcadores mesmo dizendo "cleanly"** — o gate de
   sintaxe (compileall) pegou 3 arquivos mutilados antes do commit. Vacina:
   varredura de marcadores + compileall sempre após resolves.

## Ressalvas

- Suíte: números finais e classificação A/B no [c04-suite.txt](c04-suite.txt)
  (baseline upstream puro na mesma máquina; falhas comuns = ambientais).
- Repositório ainda sem superfície toolsbook (`dex.toolsbook.v2`) — pendência
  registrada no ledger; entrada da ferramenta fica neste LAUDO interinamente.
- Promoção do wheel `2.4.0+dex.1` ao PATH = decisão posterior do dono (substitui a
  pendência do 2.4.0-oficial em aberto desde 2026-11-14).
- Testes que invocam via subprocess CLI não geram TESTED_BY (semântica: a aresta
  exige CALL direto) — documentado para não virar falso alarme futuro.
