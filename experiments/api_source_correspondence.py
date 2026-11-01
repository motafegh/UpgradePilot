"""Historical role/format adapter around the single native correspondence owner.

Old envelopes keep target/native_old_version/native_proposed_version labels.
Product owners use target_repository/old_dependency/proposed_dependency. Only
those labels are mapped; facts, IDs, paths, premises, work and omissions remain
unchanged. This module performs no independent analysis or native capture.
"""
from dataclasses import dataclass
from upgradepilot.caller_signature import correspondence as native
from upgradepilot.caller_signature.correspondence import (
    CORRESPONDENCE_VERSION, MAX_PATH_STEPS, MAX_DISCOVERY_DEPTH, MAX_DISCOVERY_GAPS,
    ANALYSIS_PROFILE, PARTIAL_ANALYSIS_COVERAGE, ANALYSIS_OMISSION_REASONS,
    FACT_STRUCTURE_BUDGET, COMPARISON_STRUCTURE_BUDGET,
    SourceRelationshipStep, module_name, absolute_import,
)

ROLE_TO_NATIVE = {"target": "target_repository", "native_old_version": "old_dependency",
                  "native_proposed_version": "proposed_dependency", "constraint_sample": "constraint_sample"}
ROLE_TO_HISTORICAL = {value: key for key, value in ROLE_TO_NATIVE.items()}

@dataclass(frozen=True)
class PythonSourceModule:
    """Acquired module role, not a claim about the installed import namespace."""

    source_id: str
    path: str
    module: str
    package: str
    version: str
    role: str
    dependencies: tuple[str, ...]


def native_module(module):
    return native.PythonSourceModule(module.source_id, module.path, module.module,
        module.package, module.version, ROLE_TO_NATIVE[module.role], module.dependencies)


def analysis_group_key(module):
    return native.analysis_group_key(native_module(module))


def discover_source_candidates(catalog, modules, limits, **kwargs):
    discovery, pairs, units = native.discover_source_candidates(
        catalog, tuple(native_module(module) for module in modules), limits, **kwargs)
    for candidate in discovery["candidates"]:
        role = candidate["callee_role"]
        role["role"] = ROLE_TO_HISTORICAL[role["role"]]
    return discovery, pairs, units
