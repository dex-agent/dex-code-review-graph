#!/usr/bin/env python
"""Sonda in-process: quais formas JS/TS o parser de uma arvore do CRG indexa.

A arvore sob prova e a que responde a ``import code_review_graph``. Rode com o
cwd na raiz dela e ``PYTHONPATH=.``, sem ``-I``: o modo isolado nao carrega os
language-packs e o parser devolve nada em silencio. A sonda observa e imprime;
nao julga a arvore.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import tempfile

CONTRACT = "crg.js_form_probe.v1"

# As quatro declaracoes que o PR #6 (Effect.fn) passou a indexar.
RED_GREEN_SRC = """import { Effect, Effect as Fx } from "effect";
import * as EffectModule from "effect/Effect";
import { fn as traced } from "effect/Effect";
function load() { return 1; }
function options() { return {}; }
function transform(value: unknown) { return value; }
export const scan = Effect.fn("scan", options())(function* () { return load(); }, transform);
export const alias = Fx.fn(function* () { return load(); });
export const namespace = EffectModule.fn("scan")(function* () { return load(); });
export const direct = traced(function* () { return load(); });
export function caller() { return scan(); }
"""
RED_GREEN_EXPECTED = frozenset({"scan", "alias", "namespace", "direct"})

# Fronteiras da forma Effect.fn. ``fn`` importado da raiz "effect" nao existe
# nos typings 4.0.0-beta.48 (a raiz so exporta o namespace): serve para
# confirmar que o parser ignora a forma invalida.
FORMS_SRC = """import { Effect, fn } from "effect";
import { fn as fnSub } from "effect/Effect";
const NAME = "computed-label";
function load() { return 1; }
export const a_tpl = Effect.fn(`dyn-${NAME}`)(function* () { return load(); });
export const b_arrow = Effect.fn("arrow")((value: number) => value + 1);
export const c_namevar = Effect.fn(NAME)(function* () { return load(); });
export const d_rootfn = fn(function* () { return load(); });
export const e_subfn = fnSub(function* () { return load(); });
"""
FORMS_LABELS = (
    ("a_tpl", "rotulo template"),
    ("b_arrow", "corpo arrow"),
    ("c_namevar", "rotulo por variavel"),
    ("d_rootfn", "fn importado de effect (raiz)"),
    ("e_subfn", "fn importado de effect/Effect"),
)

# Parametro local com nome de runner em arquivo de teste TypeScript.
TYPED_SHADOW_SRC = """import test from "node:test";
const { test: t } = require("node:test");
export function holder(test: (name: string, fn: () => void) => void) {
  test("plain-shadow", () => { console.log(1); });
}
export function typed(t: (name: string, fn: () => void) => void) {
  t("alias-shadow", () => { console.log(1); });
}
export function plain() { test("outer", () => {}); t("outer-alias", () => {}); }
"""


def _parse(parser_cls, source: str, name: str):
    path = pathlib.Path(tempfile.mkdtemp()) / name
    path.write_text(source, encoding="utf-8")
    return parser_cls().parse_file(path)


def _observe_red_green(parser_cls) -> list[str]:
    nodes, edges = _parse(parser_cls, RED_GREEN_SRC, "effects.ts")
    indexed = RED_GREEN_EXPECTED & {n.name for n in nodes if n.kind == "Function"}
    calls = sum(
        1 for edge in edges
        if edge.kind == "CALLS"
        and edge.source.rsplit("::", 1)[-1] in RED_GREEN_EXPECTED
        and edge.target.endswith("::load")
    )
    return [
        "funcoes indexadas %d/4 %s" % (len(indexed), sorted(indexed)),
        "chamadas a load a partir delas: %d" % calls,
    ]


def _observe_forms(parser_cls) -> list[str]:
    nodes, _ = _parse(parser_cls, FORMS_SRC, "forms.ts")
    names = {n.name for n in nodes if n.kind == "Function"}
    return [
        "%-9s %-32s -> %s" % (var, label, "INDEXADO" if var in names else "nao indexado")
        for var, label in FORMS_LABELS
    ]


def _observe_typed_shadow(parser_cls) -> list[str]:
    consulted = []
    original = parser_cls._commonjs_test_runner

    def spy(self, call, source):
        consulted.append(call)
        return original(self, call, source)

    parser_cls._commonjs_test_runner = spy
    try:
        nodes, _ = _parse(parser_cls, TYPED_SHADOW_SRC, "shadow.test.ts")
    finally:
        parser_cls._commonjs_test_runner = original
    tests = sorted(n.name.split("::")[-1] for n in nodes if n.kind == "Test")
    return [
        "Test indexados: %s" % tests,
        "_commonjs_test_runner consultado %d vez(es)" % len(consulted),
    ]


CASES = {
    "red_green": _observe_red_green,
    "forms": _observe_forms,
    "typed_shadow": _observe_typed_shadow,
}


def _schema() -> int:
    print(json.dumps({
        "contract": CONTRACT,
        "subject": "arvore do CRG que responde a import code_review_graph",
        "cases": {
            "red_green": "as 4 declaracoes Effect.fn do PR #6: quantas viram Function "
                         "e quantas chamam load",
            "forms": "rotulo template, corpo arrow, rotulo por variavel, "
                     "fn da raiz, fn de effect/Effect",
            "typed_shadow": "parametro local chamado test ou t em arquivo .test.ts: "
                            "quais Test sao indexados",
        },
        "flags": {
            "--caso": "red_green | forms | typed_shadow | todos (padrao: todos)",
            "--rotulo": "texto impresso na primeira linha, para comparar duas arvores",
        },
        "requires": "cwd na raiz da arvore sob prova e PYTHONPATH=. ; nunca python -I",
        "exit_codes": {"0": "casos rodados", "2": "arvore sob prova nao importavel"},
    }, ensure_ascii=False, indent=1))
    return 0


def _usage() -> int:
    run = "cd <raiz da arvore> && PYTHONPATH=. python -B <caminho>/js_form_probe.py"
    print(run)
    print(run + " --caso typed_shadow --rotulo main")
    return 0


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="js_form_probe.py",
        description=(
            "Sonda in-process das formas JS/TS que o parser de uma arvore do CRG indexa."
        ),
    )
    parser.add_argument("--caso", choices=[*CASES, "todos"], default="todos")
    parser.add_argument("--rotulo", default="", help="texto impresso na primeira linha")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--schema" in argv:
        return _schema()
    if "--usage" in argv:
        return _usage()
    args = _parse_args(argv)
    try:
        from code_review_graph.parser import CodeParser
    except ImportError as error:
        print("arvore sob prova nao importavel (%s): rode com PYTHONPATH=. e sem -I" % error,
              file=sys.stderr)
        return 2
    print("arvore: %s | rotulo: %s" % (pathlib.Path.cwd(), args.rotulo))
    selected = CASES if args.caso == "todos" else {args.caso: CASES[args.caso]}
    for name, observe in selected.items():
        print("[caso %s]" % name)
        for line in observe(CodeParser):
            print("   " + line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
