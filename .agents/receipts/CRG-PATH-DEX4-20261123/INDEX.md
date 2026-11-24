# INDEX — CRG-PATH-DEX4-20261123

Troca do PATH: `2.4.0+dex.3` → `2.4.0+dex.4` (2026-11-23).
Trilho: [2026-11-23-sync-path-dex4](../../PLAN-TASKS/2026-11-23-sync-path-dex4.md).
Motivo: a cópia do PATH não tinha a indexação de `Effect.fn` do PR #6 (merge
`fd2fb339`); o parser instalado era idêntico ao de `6b48d125`, com 0 ocorrências
de `_js_effect_fn_`.

## Artefato instalado

- Wheel: `dist/code_review_graph-2.4.0+dex.4-py3-none-any.whl`
  sha256 `28a89653e9dd78819e9d3d51d03da5b2ccd162df895b7460f1a78beef6d97000`
  (1.129.454 bytes), construído por `uv build` a partir da exportação
  (`git archive`) do commit do bump `095c403f`.
- Prova de procedência: 114 arquivos do pacote; 107 idênticos ao HEAD
  (106 iguais tirando CRLF por LF — `core.autocrlf=true` nesta máquina — e 1
  byte a byte) e 0 diferentes de verdade; os 7 restantes são as skills
  empacotadas geradas pelo hatchling (`_bundled_skills`).
- Bump: 13 carimbos numa só fonte (`tools/release_version.py --check` exit 0;
  `--from-index` conferido no commit); entrada Unreleased do `Effect.fn`
  virou a seção `2.4.0+dex.4` no `docs/FEATURES.md` e no `CHANGELOG.md`.

## Comando e provas

```
uv tool install --force --offline -c .agents/receipts/path-dex4-constraints.txt \
  dist/code_review_graph-2.4.0+dex.4-py3-none-any.whl
```

- C-01/02: `release_version.py --check` exit 0; 75 testes de documentação e
  `Effect.fn` verdes no repo; 77 dos vizinhos (doctor, failure_reporting, cli).
- C-03: wheel em `dist/` com o parser do HEAD (6 ocorrências de
  `_js_effect_fn_`); METADATA `Version: 2.4.0+dex.4`.
- C-04: `code-review-graph --version` → `2.4.0+dex.4`; `doctor` All good;
  parser instalado com a feature.
- C-05: `tests/test_js_wrapped_functions.py` 53/53 contra a cópia instalada,
  com a origem da importação conferida (`Roaming/uv/tools`; `python -P` para a
  pasta atual não vencer o `PYTHONPATH`). RED de abertura medido: a mesma prova
  na cópia dex.3 deu 3 falhas. `code-review-graph build` reconstruiu o índice do
  repo (730 arquivos, 20.595 nós) pelo executável novo.
- Suíte `packaging`: 18/18 em clone limpo de `095c403f` (92 s). Na bancada,
  17/18 — a falha é o resíduo local (`.venv-240dex` entra no sdist) e virou o
  ISSUE-LOCAL-0012 do tracker local.

## Dependências

Retrato antes/depois em `path-dex4-deps-antes.txt` e
`path-dex4-deps-depois.txt` (só no disco): a única linha que muda é a da própria
ferramenta. A primeira instalação subiu `packaging` 26.3→26.4; reinstalado com
os 70 vínculos travados (`path-dex4-constraints.txt`), derivado do retrato de
antes — padrão da casa de preservar versões na ferramenta compartilhada.

## Rollback (ensaado nos dois sentidos em 2026-11-23)

- Rota A — voltar ao wheel dex.3:
  `uv tool install --force --offline -c .agents/receipts/path-dex4-constraints.txt dist/code_review_graph-2.4.0+dex.3-py3-none-any.whl`
  (sha256 do wheel dex.3: `c9c18d90115653253a199bfa4f1974e90d92c8d2eb0110ab9c0c518263c4e64c`).
  Ensaio: voltou para dex.3 e subiu para dex.4 de novo, `doctor` All good nas
  duas pontas.
- Rota B — 2.4.0 oficial do PyPI:
  `uv tool install --force code-review-graph==2.4.0`
  (migração de índice schema-9→15 não se aplica: índices da casa já estão em 15).

## Consumidores (gate `CRG-BUMP-CONSUMIDORES`)

`cli.py` idêntico byte a byte entre dex.3 e dex.4: nenhum comando ensinado
mudou. Citações defasadas viraram o ISSUE-LOCAL-0067 no TRACKER do registry:
`code-review-graph` (SKILL.md l.89, CAPACITY.md l.13 e 21,
`references/commands-v2.4.0-dex.3.md`) em dex.3 e o delphi-feeder em dex.1.
Correção de pacote é corte da Governanta; decisão de desenho (versão citada vs.
piso) é do dono.

## Efeitos colaterais pagos

- `code-review-graph build` reconstruiu o índice do repo (o `update` não
  reparsa arquivo inalterado — ISSUE-LOCAL-0011; sua seção "Fora deste item"
  foi atualizada).
- O primeiro run da suíte `packaging` deixou `pip/cache` (92,7 MB) na raiz;
  removido; registra no mesmo ISSUE-LOCAL-0012.
- Pendência `CRG-WHEEL-PATH-SEM-EFFECT-FN-20261123` consumida pelo CLI do
  ledger com prova.

Só em disco: `.agents/receipts/` é ignorado pelo git, exceto este `INDEX.md`
(exceção `!` no `.gitignore`, no commit).
