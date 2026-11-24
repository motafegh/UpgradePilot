"""Read selected source definitions with Griffe in the isolated tool environment."""

import argparse
import json
import logging
from pathlib import Path
from time import perf_counter

import griffe

COMPARISONS = {
    "httpx-public": ("av-tracer", "httpx", "", "httpx", "httpx/__init__.py", None),
    "httpx-client": (
        "av-tracer", "httpx", "", "httpx._client", "httpx/_client.py", "Client.__init__",
    ),
    "pytest-raises": (
        "glyphslib", "pytest", "src", "_pytest.raises", "src/_pytest/raises.py", "raises",
    ),
    "pytest-mark": (
        "glyphslib", "pytest", "src", "_pytest.mark.structures",
        "src/_pytest/mark/structures.py", "MarkDecorator.__call__",
    ),
}


def compare(packet, name):
    case, package, search_dir, module, defining_file, member = COMPARISONS[name]
    roots = [packet / case / f"{package}-{end}" for end in ("old", "new")]
    files = [root / defining_file for root in roots]
    relative_files = [str(file.relative_to(packet)) for file in files]
    start = perf_counter()
    if not all(file.is_file() for file in files):
        return {"status": "inconclusive_missing_definition", "files": relative_files}
    unresolved = []
    try:
        scopes = []
        for root, file in zip(roots, files, strict=True):
            if member is None:
                loader = griffe.GriffeLoader(
                    search_paths=[root / search_dir], allow_inspection=False,
                )
                obj = loader.load(module, try_relative_path=False)
                missing, _ = loader.resolve_aliases(external=False, implicit=False)
                unresolved.append(sorted(missing))
            else:
                obj = griffe.visit(module, file, file.read_text(encoding="utf-8"))
            if obj.filepath.resolve() != file.resolve():
                raise ValueError(f"Griffe resolved an unexpected source file: {obj.filepath}")
            if member is not None:
                obj[member]  # Refuse to interpret an absent selected definition as no change.
                owner, _, _ = member.rpartition(".")
                scopes.append(obj[owner] if owner else obj)
            else:
                scopes.append(obj)
        findings = []
        for finding in griffe.find_breaking_changes(*scopes):
            changed = finding.obj
            if member is not None and changed.path != f"{module}.{member}":
                continue
            changed_file = changed.filepath.resolve().relative_to(packet)
            findings.append({
                "kind": finding.kind.value,
                "object": changed.path,
                "parameter": getattr(finding.old_value, "name", None),
                "file": str(changed_file),
                "line": changed.lineno,
            })
    except (ImportError, KeyError, ValueError, SyntaxError, griffe.GriffeError) as error:
        return {
            "status": "inconclusive_tool_error", "files": relative_files,
            "reason": f"{type(error).__name__}: {error}",
            "unresolved_aliases": unresolved,
            "seconds": perf_counter() - start,
        }
    return {
        "status": "compared", "files": relative_files, "findings": findings,
        "unresolved_aliases": unresolved,
        "seconds": perf_counter() - start,
    }


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    parser.add_argument("comparisons", nargs="+", choices=sorted(COMPARISONS))
    args = parser.parse_args()
    print(json.dumps({key: compare(args.packet, key) for key in args.comparisons}, indent=2))
