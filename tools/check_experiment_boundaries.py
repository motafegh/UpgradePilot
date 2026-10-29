"""Check the explicit experiment inventory and static executable dependency model.

Parses project source/configuration without importing it. This developer check
owns no product or experiment semantics and is not a sandbox: computed imports,
aliases hidden by arbitrary code, generated code and semantic authority need their
normal review. It rejects unresolved dynamic loading in product source rather than
pretending absence from a static import graph proves a safe dynamic dependency.
"""

from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import sys
import tomllib
from pathlib import Path


def _module(path):
    return str(path.with_suffix("")).replace("/", ".").removesuffix(".__init__")


def _imports(path, tree, modules):
    name = _module(path)
    package = name if path.name == "__init__.py" else name.rpartition(".")[0]
    aliases = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.asname:
                    aliases[alias.asname] = alias.name
                yield alias.name, alias.name, node.lineno
        elif isinstance(node, ast.ImportFrom):
            target = importlib.util.resolve_name("." * node.level + (node.module or ""), package) if node.level else node.module or ""
            for alias in node.names:
                destination = target + "." + alias.name if target + "." + alias.name in modules else target
                if destination in modules and destination != target:
                    aliases[alias.asname or alias.name] = destination
                yield destination, alias.name, node.lineno
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr.startswith("_"):
            value = ast.unparse(node.value)
            destination = aliases.get(value, value)
            if destination in modules:
                yield destination, node.attr, node.lineno


def check_boundaries(root: Path):
    """Return static errors/counts; no target import, artifact rewrite or execution."""
    errors, edges, private = [], [], set()
    manifest = json.loads((root / "experiments/role_inventory.json").read_text())
    if manifest.get("format") != "experiment-role-inventory/1":
        raise ValueError("Unsupported experiment role inventory.")
    artifacts = manifest["artifacts"]
    by_path = {item["path"]: item for item in artifacts}
    if len(by_path) != len(artifacts):
        errors.append("duplicate inventory path")
    actual = {str(p.relative_to(root)) for p in (root / "experiments").rglob("*")
              if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"}
    for path in sorted(actual - by_path.keys()):
        errors.append("unclassified artifact: " + path)
    for path in sorted(by_path.keys() - actual):
        errors.append("missing classified artifact: " + path)
    roles = {"substrate", "composition", "runner", "reader", "compatibility_alias", "diagnostic",
             "protocol", "retained_data", "test", "component"}
    for family in manifest["families"].values():
        if not (root / family["owner"]).is_file():
            errors.append("missing family owner: " + family["owner"])
    for path, row in by_path.items():
        if (row["family"] not in manifest["families"] or not row["roles"]
            or set(row["roles"]) - roles or not row["maintenance"]):
            errors.append("incomplete role: " + path)
        if not (root / row["evidence"]).is_file():
            errors.append("missing role owner: " + path)
    modules = {_module(Path(path)): row for path, row in by_path.items() if path.endswith(".py")}
    graph = {name: set() for name in modules if not modules[name]["path"].startswith("experiments/tests/")}
    allowed_families = {tuple(pair) for pair in manifest["allowed_cross_family_dependencies"]}
    exceptions = {(row["source"], row["target"], name) for row in manifest["legacy_private_imports"] for name in row["names"]}
    used_exceptions = set()
    for name, row in modules.items():
        path = Path(row["path"])
        if str(path) not in actual:
            continue
        tree = ast.parse((root / path).read_bytes(), filename=str(path))
        is_test = "test" in row["roles"]
        if path.parts[:2] == ("experiments", "tests") and not is_test:
            errors.append("test location lacks test role: " + str(path))
        if is_test and path.parts[:2] != ("experiments", "tests"):
            errors.append("runtime location cannot use test exemption: " + str(path))
        for destination, imported, line in _imports(path, tree, modules):
            if not is_test and destination.startswith(("tests", "test_", "experiments.tests")):
                errors.append(f"runtime test dependency: {name}:{line} -> {destination}")
            if destination not in modules:
                continue
            edges.append((name, destination))
            target = modules[destination]
            if is_test:
                continue
            graph[name].add(destination)
            if row["family"] != target["family"] and (row["family"], target["family"]) not in allowed_families:
                errors.append(f"unadmitted cross-family dependency: {name} -> {destination}")
            if imported.startswith("_"):
                key = (name, destination, imported)
                private.add(key)
                if key not in exceptions:
                    errors.append(f"new private dependency: {name} -> {destination}.{imported}")
                else:
                    used_exceptions.add(key)
            if (row["family"] == "api_source" and "runner" in target["roles"]
                and not {"composition", "substrate"}.intersection(target["roles"])):
                errors.append(f"API dependency on runner: {name} -> {destination}")
    for key in sorted(exceptions - used_exceptions):
        errors.append("stale private exception: " + " -> ".join(key))
    visited, active = set(), set()
    def visit(name):
        if name in active:
            errors.append("runtime import cycle: " + name)
            return
        if name in visited:
            return
        visited.add(name)
        active.add(name)
        for destination in graph.get(name, ()):
            visit(destination)
        active.remove(name)
    for name in graph:
        visit(name)
    product_files = list((root / "src/upgradepilot").rglob("*.py"))
    for path in product_files:
        tree = ast.parse(path.read_bytes(), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                names = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module or ""]
                if any(n == "experiments" or n.startswith(("experiments.", "tests", "tools")) for n in names):
                    errors.append(f"product reverse dependency: {path.relative_to(root)}:{node.lineno}")
            elif isinstance(node, ast.Call):
                called = ast.unparse(node.func)
                leaf = called.rsplit(".", 1)[-1]
                if leaf in {"import_module", "__import__", "spec_from_file_location", "run_module", "run_path", "eval", "exec"} or called.startswith("sys.path."):
                    errors.append(f"product dynamic load needs boundary review: {path.relative_to(root)}:{node.lineno}")
    config = tomllib.loads((root / "pyproject.toml").read_text())
    package_roots = config.get("tool", {}).get("setuptools", {}).get("packages", {}).get("find", {}).get("where")
    if package_roots != ["src"]:
        errors.append("product package discovery must remain src-only")
    if any(value.startswith("experiments.") for value in config.get("project", {}).get("scripts", {}).values()):
        errors.append("product entry point depends on experiments")
    return dict(ok=not errors, errors=sorted(set(errors)), artifacts=len(actual), python_modules=len(modules),
                internal_import_edges=len(set(edges)), legacy_private_symbols=len(private), product_python_files=len(product_files))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    try:
        result = check_boundaries(args.root.resolve())
    except (OSError, ValueError, KeyError, TypeError, SyntaxError) as exc:
        result = {"ok": False, "errors": [type(exc).__name__ + ": " + str(exc)]}
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
