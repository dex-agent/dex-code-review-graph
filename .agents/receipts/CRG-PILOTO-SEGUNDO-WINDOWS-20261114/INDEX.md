# Piloto do wheel em um segundo Windows

↩ [Trilho do piloto](../../PLAN-TASKS/2026-11-14-crg-piloto-segundo-windows.md)

- [Verificador](verify.py) — confere wheel, executável do PATH, Git, SQLite e suíte.
- [Grafo do ensaio](rehearsal-graph.json) — índice descartável no PREDATOR.
- [Suíte do ensaio](rehearsal-suite.json) — Node, checkout final, resultado e contagens.

O ensaio usou o wheel promovido e a instalação já disponível no PATH do
PREDATOR. O controle sem `--rehearsal` encerrou com exit 1 antes de criar
a pasta de saída, impedindo que o ensaio contasse como execução independente.

O pacote fica em `package/` no disco do PREDATOR, sob este diretório.
Inclui o wheel aprovado, as restrições de dependências, o verificador e o
bundle Git privado do checkout de referência. A cópia do pacote aguarda
um segundo Windows com acesso autorizado. [Orientação do Dex](https://crsantos.slack.com/archives/D0C5E5Y8MRT/p1794684740842859).

| Arquivo local | SHA-256 |
| --- | --- |
| `code_review_graph-2.3.7-py3-none-any.whl` | `7f2f9b60802b253739c6851ee7d84e3b970a5cd9636eab800e831f72b7e051a0` |
| `constraints.txt` | `1e700cc63a598c7f8f406835c3b9479706eae51f26b0bf1c8e753d796f86c141` |
| `dex-whatsapp.bundle` | `a9d44a8861b0d322d9611914ef2cdbb63a9e737421c68e9eac9ab068029b8378` |
| `verify.py` | `57e79f31d6a5bcd6e04e4d7fec768ae5c27600b9d2cc3d9b33ba6cd8c7be7d73` |

No segundo Windows, com Python 3.12+, Git, uv e Node 22+ no PATH,
confira os quatro hashes e rode na pasta do pacote:

```powershell
py -3 -B .\verify.py --out .\aceite-crg
```

O uv provisiona Python 3.13 e instala o wheel em um diretório isolado.
O verificador usa um PATH restrito ao processo para resolver a nova CLI.
Reabra `aceite-crg/graph.json` e `aceite-crg/suite.json` após a execução.
O log da suíte é `aceite-crg/suite.txt`. O host e o campo `rehearsal=false`
devem identificar a execução independente.
