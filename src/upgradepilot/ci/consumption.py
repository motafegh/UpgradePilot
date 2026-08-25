"""Compose dependency-owned project-selection facts into CI static consumption evidence.

CI owns the proposition "this static CI declaration consumes the changed dependency".
It does not interpret project-source environment membership or uv lock reachability.
Those facts arrive from dependency-owned evidence types and are composed here with the
exact workflow/job/step/segment that produced the visible selection.

For uv, ``supported`` means only that the static declaration selects explicit roots with
an unconditional exact-lock path to the changed dependency. It does not claim complete uv
environment formation, command execution, installation success, runtime version use,
direct package exercise, or behavioral compatibility.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..dependency.environment_membership import ProjectSourceEnvironmentMembership
from ..dependency.environment_selection import (
    ProjectEnvironmentSelectionDeclaration,
    ProjectEnvironmentSelectionObservation,
)
from ..dependency.uv_reachability import UvSelectedRootReachability


type StaticDependencyConsumptionState = Literal[
    "supported",
    "not_established",
    "unresolved",
]
type StaticDependencyConsumptionMechanism = Literal[
    "direct_requirements",
    "project_environment",
]
type StaticDependencyReachabilityKind = Literal["direct", "transitive"]
type ProjectEnvironmentDependencyEvidence = (
    ProjectSourceEnvironmentMembership | UvSelectedRootReachability
)


@dataclass(frozen=True, slots=True)
class StaticDependencyConsumptionEvidence:
    """One exact static CI declaration that may consume the changed dependency.

    ``supported`` is static consumption evidence only. ``reachability_kind`` and
    ``witness_path`` are populated when uv selected-root reachability established support.
    Conditional candidate paths remain diagnostic on ``unresolved`` results and never
    become supported consumption.
    """

    state: StaticDependencyConsumptionState
    mechanism: StaticDependencyConsumptionMechanism
    normalized_package: str
    workflow_path: str
    workflow_revision: str
    job_key: str
    step_source_index: int
    segment_index: int
    command: str
    reason: str
    detail: str
    source_path: str | None = None
    reachability_kind: StaticDependencyReachabilityKind | None = None
    witness_path: tuple[str, ...] = ()
    conditional_candidate_path: tuple[str, ...] = ()
    unresolved_conditions: tuple[str, ...] = ()


def compose_project_environment_consumption(
    *,
    workflow_path: str,
    workflow_revision: str,
    job_key: str,
    observation: ProjectEnvironmentSelectionObservation,
    declaration: ProjectEnvironmentSelectionDeclaration,
    dependency_evidence: ProjectEnvironmentDependencyEvidence,
) -> StaticDependencyConsumptionEvidence:
    """Compose one dependency-domain result with its exact static CI declaration.

    The dependency layer retains the meaning of optional extras, dependency groups, and
    uv graph reachability. This CI layer only verifies the composition identity it needs
    and maps the dependency result into the static-consumption proof axis.
    """

    if not workflow_path or not workflow_revision:
        raise ValueError("project environment consumption requires exact workflow identity")
    if observation.state != "observed":
        raise ValueError(
            "project environment consumption requires an observed selection declaration"
        )
    if declaration not in observation.declarations:
        raise ValueError(
            "project environment declaration is not owned by the supplied observation"
        )
    if not dependency_evidence.normalized_package:
        raise ValueError("dependency evidence must preserve normalized package identity")

    common = {
        "mechanism": "project_environment",
        "normalized_package": dependency_evidence.normalized_package,
        "workflow_path": workflow_path,
        "workflow_revision": workflow_revision,
        "job_key": job_key,
        "step_source_index": observation.step_source_index,
        "segment_index": declaration.segment_index,
        "command": observation.command,
    }

    if isinstance(dependency_evidence, UvSelectedRootReachability):
        return _compose_uv_reachability_consumption(
            dependency_evidence,
            declaration=declaration,
            common=common,
        )

    return _compose_project_source_membership_consumption(
        dependency_evidence,
        common=common,
    )


def _compose_uv_reachability_consumption(
    reachability: UvSelectedRootReachability,
    *,
    declaration: ProjectEnvironmentSelectionDeclaration,
    common: dict[str, object],
) -> StaticDependencyConsumptionEvidence:
    """Map R4 uv selected-root reachability without strengthening its proof state."""

    if reachability.project_root != declaration.project_root:
        raise ValueError("uv reachability project root does not match the declaration")
    if reachability.selectors != declaration.selectors:
        raise ValueError("uv reachability selectors do not match the declaration")

    # R4 may emit ``not_established`` only after exhausting the complete bounded-project
    # root domain. An all-workspace declaration has a larger negative proof obligation and
    # must never inherit that bounded negative result through CI composition.
    if (
        reachability.state == "not_established"
        and declaration.package_scope != "bound_project"
    ):
        raise ValueError(
            "uv not-established reachability cannot be rebound to all-workspace scope"
        )

    uv_common = {"source_path": reachability.lock_file_path, **common}

    if reachability.state == "reachable":
        return StaticDependencyConsumptionEvidence(
            state="supported",
            reason="selected_uv_roots_reach_changed_dependency",
            detail=(
                "Dependency-owned exact-lock evidence establishes an unconditional path "
                "from one explicit root selected by this static uv declaration to the "
                "changed dependency. Runtime execution and success are not established."
            ),
            reachability_kind=reachability.reachability_kind,
            witness_path=reachability.witness_path,
            **uv_common,
        )

    if reachability.state == "not_established":
        return StaticDependencyConsumptionEvidence(
            state="not_established",
            reason="selected_uv_root_reachability_not_established",
            detail=reachability.detail,
            **uv_common,
        )

    return StaticDependencyConsumptionEvidence(
        state="unresolved",
        reason=reachability.reason,
        detail=reachability.detail,
        conditional_candidate_path=reachability.conditional_candidate_path,
        unresolved_conditions=reachability.unresolved_conditions,
        **uv_common,
    )


def _compose_project_source_membership_consumption(
    membership: ProjectSourceEnvironmentMembership,
    *,
    common: dict[str, object],
) -> StaticDependencyConsumptionEvidence:
    """Preserve the separate S011-style source-environment membership proposition."""

    source_common = {"source_path": membership.project_file_path, **common}

    if membership.state == "member":
        return StaticDependencyConsumptionEvidence(
            state="supported",
            reason="selected_project_environment_contains_changed_dependency",
            detail=(
                "Dependency-owned project-source evidence establishes that this static "
                "selection includes the affected project environment containing the "
                "changed dependency. Runtime execution and success are not established."
            ),
            **source_common,
        )

    if membership.state == "not_established":
        return StaticDependencyConsumptionEvidence(
            state="not_established",
            reason="selected_environment_membership_not_established",
            detail=membership.detail,
            **source_common,
        )

    return StaticDependencyConsumptionEvidence(
        state="unresolved",
        reason=membership.reason,
        detail=membership.detail,
        **source_common,
    )


__all__ = (
    "ProjectEnvironmentDependencyEvidence",
    "StaticDependencyConsumptionEvidence",
    "StaticDependencyConsumptionMechanism",
    "StaticDependencyConsumptionState",
    "StaticDependencyReachabilityKind",
    "compose_project_environment_consumption",
)
