---
implementation_version: v2
layer: L2
slug: triade-cli-argparse-required-e-library-importada-6ab419a079fa
tags:
  - "#auto-memory/project"
---

# triade-cli-argparse-required-e-library-importada

Espelho da auto-memory do host ZCode (arquivo triade-cli-argparse-required-e-library-importada.md, tipo project).

Tríade CLI (--schema/--usage) em scripts da casa — 2 armadilhas:

Implementando tríade CLI (`--help`/`--schema` JSON/`--usage`, gate
`--require-cli-triad`) em scripts Python da casa — 2 armadilhas medidas na
cura do feeder Delphi (ISSUE-LOCAL-0008, corte 3.513.0):

1. **`required=True` do argparse MATA a tríade**: `--schema` morre exit 2
   ("arguments are required") ANTES de qualquer early return. Cura (molde
   `export_crg_snapshot.py`): `required=False` + após os early-returns de
   --schema/--usage validar com `parser.error("--x é obrigatório (exceto com
   --schema/--usage)")` — exit 2/stderr preservados.
2. **Pattern inline em library importada sequestra o IMPORTADOR**: se A.py
   importa B.py e A roda com `--schema`, checks module-level de B disparam no
   processo de A. Cura: inline checks (`if '--schema' in sys.argv`) vivem
   DENTRO do `if __name__ == "__main__":` da library — gate aceita, importador
   imune (prova: `feed_crg_from_delphi --schema` devolve o schema do feed, não
   o do per_function_parser).

Prova: tríade 18/18; gate 20/3/12→31/3/0; py_compile 6/6; self-test exit 0;
feed sem args exit 2.

Espelho dex-memoria (global L2): `remember-3b1672c100efc963b7f76ecb`.
Related: [[entropia-conserta-na-descoberta-20261116]]

#auto-memory/project

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^triade-cli-argparse-required-e-library-importada-6ab419a079fa-content
