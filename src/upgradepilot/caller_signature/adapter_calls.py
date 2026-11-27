"""Nominate an exact changed module from bounded, target-rooted analysis."""
from __future__ import annotations

import ast
from collections import defaultdict
from functools import lru_cache

from ..package_identity import normalize_package_name
from .analysis import SourceSpan
from .bindings import ImportFact, collect_imports
from .correspondence import lexical_body_calls
from .evidence import SourceAnalysisInput, SourceAnalysisResult
from .source_evidence import AdapterCallPath


PAIR_MODULE_ATTEMPTS = 2
# A tagged pair took six GitHub requests per version in the measured route.
# This prompts an earlier analysis pass while closure can still afford that route.
PAIR_GITHUB_REQUEST_HEADROOM = 12
ADAPTER_CALL_ANALYSIS_SCOPE = "adapter_call_preparation"


def nominate_adapter_call_paths(
    source: SourceAnalysisInput, result: SourceAnalysisResult, requested_modules: set[str],
) -> tuple[tuple[AdapterCallPath, ...], dict[str, ImportFact], bool]:
    """Return conditional path hypotheses and whether the path limit was reached.

    An unresolved call has no root in the existing gap layout. Anchor it to
    the lexical body of a declaration the worker already reached from a target
    root. The final worker must still establish the requested comparison.
    """
    catalog = source.catalog
    package = catalog.target.normalized_package
    files = {catalog.descriptor(file)["file_id"]: file for file in catalog.files}
    scopes = {scope.source_id: scope for scope in catalog.scopes}
    units = {unit.unit_id: unit.facts for unit in result.units if unit.facts}
    calls = {call.fact_id: call for facts in units.values() for call in facts.calls}
    signatures = {sig.fact_id: sig for facts in units.values() for sig in facts.signatures}
    unresolved = defaultdict(set)
    for gap in result.gaps:
        if gap.reason == "callable_relationship_unresolved":
            unresolved[gap.unit_id].add(gap.span)

    @lru_cache(maxsize=source.limits.max_files)
    def file_syntax(unit_id):
        file = files[unit_id]
        scope = scopes[file.source_id]
        identity = f"{scope.repository}@{scope.revision}:{file.path}"
        tree = ast.parse(file.content)
        definitions = {
            SourceSpan.of(node): node
            for node in ast.walk(tree)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        imports = defaultdict(list)
        for item in collect_imports(identity, tree):
            if (not item.relative_level and item.module not in requested_modules
                    and item.module and normalize_package_name(item.module.split(".")[0]) == package):
                origin = item.module if item.member is None else f"{item.module}.{item.member}"
                imports[item.line, origin].append(item)
        return definitions, imports

    @lru_cache(maxsize=source.limits.max_pairs)
    def missing_imported_calls(signature_id):
        signature = signatures[signature_id]
        unit_id = signature.unit_id
        if not unresolved[unit_id]:
            return ()
        definitions, imports = file_syntax(unit_id)
        definition = definitions.get(signature.span)
        if definition is None:
            return ()
        body = {SourceSpan.of(node) for node in lexical_body_calls(definition.body)} & unresolved[unit_id]
        matches = {}
        for call in units[unit_id].calls:
            if call.span not in body or call.binding is None:
                continue
            for step in call.binding.trace:
                if step.operation != "import" or step.source_id != unit_id:
                    continue
                for item in imports.get((step.line, step.origin), ()):
                    for binding in call.binding.possible_imports:
                        if binding == step.origin or binding.startswith(step.origin + "."):
                            matches[call.fact_id, item.module, item.line, binding] = (call, item, binding)
                            if len(matches) > source.limits.max_pairs:
                                return tuple(matches.values())
        return tuple(matches.values())

    paths = {}
    origins = {}
    for candidate in result.candidates:
        if candidate.callee_role.role != "constraint_sample" or candidate.comparison.outcome == "rejected":
            continue
        root = calls[candidate.root_call_id]
        for call, item, binding in missing_imported_calls(candidate.comparison.signature_id):
            key = (item.module, root.fact_id, call.fact_id, item.line, binding)
            if key in paths:
                continue
            if len(paths) >= source.limits.max_pairs:
                return tuple(paths.values()), origins, True
            paths[key] = AdapterCallPath(
                item.module, root.unit_id, root.span,
                call.unit_id, call.span, item.line, binding,
            )
            origins.setdefault(item.module, item)
    return tuple(paths.values()), origins, False
