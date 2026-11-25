"""Safe CommonJS/dynamic-import subset reconciled from PR #95."""

from pathlib import Path

import pytest

from code_review_graph.parser import CodeParser


def _parse(tmp_path: Path, source: str, suffix: str = ".js"):
    path = tmp_path / f"app{suffix}"
    path.write_text(source, encoding="utf-8")
    return path, CodeParser().parse_file(path)


def _imports(edges):
    return [edge for edge in edges if edge.kind == "IMPORTS_FROM"]


def test_static_require_resolves_relative_file_and_deduplicates(tmp_path):
    dependency = tmp_path / "dependency.js"
    dependency.write_text("export function run() {}\n", encoding="utf-8")
    path, (_nodes, edges) = _parse(
        tmp_path,
        "const first = require('./dependency');\n"
        "const second = require('./dependency');\n",
    )

    imports = _imports(edges)
    assert len(imports) == 1
    assert imports[0].source == path.as_posix()
    assert imports[0].target == dependency.resolve().as_posix()


def test_destructured_require_populates_import_map_for_call_resolution(tmp_path):
    dependency = tmp_path / "dependency.js"
    dependency.write_text("export function run() {}\n", encoding="utf-8")
    _path, (_nodes, edges) = _parse(
        tmp_path,
        "const { run } = require('./dependency');\n"
        "run();\n",
    )

    calls = [edge for edge in edges if edge.kind == "CALLS"]
    assert any(edge.target == f"{dependency.resolve().as_posix()}::run" for edge in calls)


def test_cjs_indexes_exports_and_resolves_explicit_require(tmp_path):
    (tmp_path / "package.json").write_text('{"type":"module"}', encoding="utf-8")
    dependency = tmp_path / "dependency.cjs"
    dependency.write_text("module.exports.run = () => 1;\n", encoding="utf-8")
    path, (nodes, edges) = _parse(
        tmp_path,
        "const dependency = require('./dependency.cjs');\n"
        "const unresolved = require('./dependency');\n"
        "module.exports.start = () => dependency.run();\n",
        suffix=".cjs",
    )

    assert any(node.kind == "File" and node.language == "javascript" for node in nodes)
    assert any(
        node.kind == "Function" and node.name == "module.exports.start"
        for node in nodes
    )
    assert [(edge.source, edge.target) for edge in _imports(edges)] == [
        (path.as_posix(), dependency.resolve().as_posix()),
        (path.as_posix(), "./dependency"),
    ]


@pytest.mark.parametrize("suffix", [".cjs", ".CJS"])
def test_missing_explicit_cjs_does_not_bind_to_javascript_homonym(tmp_path, suffix):
    dependency = tmp_path / "dependency.js"
    dependency.write_text("export function run() {}\n", encoding="utf-8")
    path, (_nodes, edges) = _parse(
        tmp_path,
        f"const {{ run }} = require('./dependency{suffix}');\nrun();\n",
    )

    assert [(edge.source, edge.target) for edge in _imports(edges)] == [
        (path.as_posix(), f"./dependency{suffix}"),
    ]
    assert all(
        edge.target != f"{dependency.resolve().as_posix()}::run"
        for edge in edges if edge.kind == "CALLS"
    )


def test_require_cjs_named_directory_resolves_its_index(tmp_path):
    directory = tmp_path / "dependency.cjs"
    directory.mkdir()
    index = directory / "index.js"
    index.write_text("module.exports = () => 1;\n", encoding="utf-8")
    (tmp_path / "dependency.js").write_text("module.exports = () => 2;\n", encoding="utf-8")
    _path, (_nodes, edges) = _parse(tmp_path, "require('./dependency.cjs');\n")

    assert [edge.target for edge in _imports(edges)] == [index.resolve().as_posix()]


def test_static_dynamic_import_is_recorded(tmp_path):
    dependency = tmp_path / "dependency.js"
    dependency.write_text("export const value = 1;\n", encoding="utf-8")
    _path, (_nodes, edges) = _parse(
        tmp_path,
        "async function load() { return import('./dependency'); }\n",
    )

    assert [edge.target for edge in _imports(edges)] == [dependency.resolve().as_posix()]


def test_package_require_remains_an_unresolved_package_edge(tmp_path):
    _path, (_nodes, edges) = _parse(tmp_path, "const express = require('express');\n")
    assert [edge.target for edge in _imports(edges)] == ["express"]


def test_dynamic_template_require_is_not_misrepresented_as_a_file(tmp_path):
    _path, (_nodes, edges) = _parse(
        tmp_path,
        "const command = require(`./commands/${name}`);\n"
        "const helper = import(`./utils/${name}.js`);\n",
    )
    assert _imports(edges) == []


def test_path_join_require_is_not_reduced_to_the_last_segment(tmp_path):
    _path, (_nodes, edges) = _parse(
        tmp_path,
        "const command = require(path.join(__dirname, group, 'handler'));\n",
    )
    assert _imports(edges) == []


def test_empty_and_argumentless_require_are_ignored(tmp_path):
    _path, (_nodes, edges) = _parse(
        tmp_path,
        "const empty = require('');\nconst missing = require();\n",
    )
    assert _imports(edges) == []


@pytest.mark.parametrize("suffix", [".test.cjs", ".spec.cjs", ".TEST.CJS"])
def test_commonjs_test_suffix_outside_test_directory(tmp_path, suffix):
    path = tmp_path / "src" / f"core{suffix}"
    nodes, _ = CodeParser(tmp_path).parse_bytes(
        path, b"const test = require('node:test');\ntest('core', () => {});\n",
    )

    assert [(node.kind, node.is_test) for node in nodes if node.kind == "File"] == [
        ("File", True),
    ]
    assert [node.name for node in nodes if node.kind == "Test"] == ["test:core@L2"]


def test_commonjs_node_test_alias_in_test_directory(tmp_path):
    path = tmp_path / "tests" / "distribution.test.cjs"
    nodes, edges = CodeParser(tmp_path).parse_bytes(
        path,
        b"const t = require('node:test'), assert = require('node:assert/strict');\n"
        b"t('install', () => install());\n",
    )

    assert [node.name for node in nodes if node.kind == "Test"] == ["test:install@L2"]
    assert any(
        edge.kind == "TESTED_BY" and edge.source == "install"
        and edge.target == f"{path.as_posix()}::test:install@L2"
        for edge in edges
    )


@pytest.mark.parametrize("shadow", [
    "function helper(t) { t('shadow', () => wrong()); }",
    "function helper({t}) { t('shadow', () => wrong()); }",
    "{ const t = other; t('shadow', () => wrong()); }",
    "function helper() { t('shadow', () => wrong()); if (flag) { var t = other; } }",
    "try {} catch (t) { t('shadow', () => wrong()); }",
    "function helper() { function t() {} t('shadow', () => wrong()); }",
    "for (const t of runners) { t('shadow', () => wrong()); }",
    "function helper() { t('shadow', () => wrong()); for (var t of runners) {} }",
    "switch (kind) { case 1: const t = other; t('shadow', () => wrong()); }",
])
def test_commonjs_node_test_alias_respects_shadowing(tmp_path, shadow):
    path = tmp_path / "tests" / "distribution.test.cjs"
    nodes, edges = CodeParser(tmp_path).parse_bytes(
        path,
        ("const t = require('node:test');\n"
         f"{shadow}\n"
         "t('install', () => install());\n").encode(),
    )

    assert [node.name for node in nodes if node.kind == "Test"] == ["test:install@L3"]
    assert not any(edge.kind == "TESTED_BY" and edge.source == "wrong" for edge in edges)


def test_commonjs_local_test_function_is_not_a_runner(tmp_path):
    path = tmp_path / "tests" / "distribution.test.cjs"
    nodes, edges = CodeParser(tmp_path).parse_bytes(
        path, b"function test(name, callback) { callback(); }\ntest('local', () => wrong());\n",
    )

    assert not any(node.kind == "Test" for node in nodes)
    assert not any(edge.kind == "TESTED_BY" and edge.source == "wrong" for edge in edges)


def test_commonjs_destructured_node_test_alias_and_modifier(tmp_path):
    path = tmp_path / "src" / "distribution.spec.cjs"
    nodes, _ = CodeParser(tmp_path).parse_bytes(
        path,
        b"const {test: t, mock} = require('node:test');\n"
        b"t.only('install', () => install());\n"
        b"mock('not a runner', () => wrong());\n",
    )

    assert [node.name for node in nodes if node.kind == "Test"] == ["test:install@L2"]


def test_commonjs_shadowed_require_does_not_create_a_node_test_alias(tmp_path):
    path = tmp_path / "src" / "distribution.test.cjs"
    nodes, _ = CodeParser(tmp_path).parse_bytes(
        path,
        b"function configure(require) {\n"
        b"  const t = require('node:test');\n"
        b"  t('fake', () => wrong());\n"
        b"}\n",
    )

    assert not any(node.kind == "Test" for node in nodes)


@pytest.mark.parametrize("module", ["mocha", "@jest/globals", "vitest"])
def test_commonjs_runner_with_named_framework_import(tmp_path, module):
    nodes, _ = CodeParser(tmp_path).parse_bytes(
        tmp_path / "tests" / "framework.test.cjs",
        f"const {{it}} = require('{module}');\nit('works', () => {{}});\n".encode(),
    )

    assert [node.name for node in nodes if node.kind == "Test"] == ["it:works@L2"]
