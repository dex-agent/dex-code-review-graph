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
    assert imports[0].source == str(path)
    assert imports[0].target == str(dependency.resolve())


def test_destructured_require_populates_import_map_for_call_resolution(tmp_path):
    dependency = tmp_path / "dependency.js"
    dependency.write_text("export function run() {}\n", encoding="utf-8")
    _path, (_nodes, edges) = _parse(
        tmp_path,
        "const { run } = require('./dependency');\n"
        "run();\n",
    )

    calls = [edge for edge in edges if edge.kind == "CALLS"]
    assert any(edge.target == f"{dependency.resolve()}::run" for edge in calls)


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
        (str(path), str(dependency.resolve())),
        (str(path), "./dependency"),
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
        (str(path), f"./dependency{suffix}"),
    ]
    assert all(
        edge.target != f"{dependency.resolve()}::run"
        for edge in edges if edge.kind == "CALLS"
    )


def test_require_cjs_named_directory_resolves_its_index(tmp_path):
    directory = tmp_path / "dependency.cjs"
    directory.mkdir()
    index = directory / "index.js"
    index.write_text("module.exports = () => 1;\n", encoding="utf-8")
    (tmp_path / "dependency.js").write_text("module.exports = () => 2;\n", encoding="utf-8")
    _path, (_nodes, edges) = _parse(tmp_path, "require('./dependency.cjs');\n")

    assert [edge.target for edge in _imports(edges)] == [str(index.resolve())]


def test_static_dynamic_import_is_recorded(tmp_path):
    dependency = tmp_path / "dependency.js"
    dependency.write_text("export const value = 1;\n", encoding="utf-8")
    _path, (_nodes, edges) = _parse(
        tmp_path,
        "async function load() { return import('./dependency'); }\n",
    )

    assert [edge.target for edge in _imports(edges)] == [str(dependency.resolve())]


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
