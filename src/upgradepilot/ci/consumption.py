"""Compose dependency-owned environment facts into CI static consumption evidence.

CI owns the proposition "this static CI declaration consumes an environment containing
the changed dependency". It does not own what extras/groups mean or how uv lock
membership is established. Those facts arrive from dependency-owned Cluster-3/4 types.

This module therefore preserves source location, mechanism, and membership witness while
keeping execution/runtime success outside the static consumption result.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..dependency.environment_membership import ProjectSourceEnvironmentMembership
from ..dependency.environment_selection import (
    ProjectEnvironmentSelectionDeclaration,
    ProjectEnvironmentSelectionObservation,
)
from ..dependency.uv_membership import UvSelectedEnvironmentMembership


type StaticDependencyConsumptionState = Literal[
    "supported",
    "not_established",
    "unresolved",
]
type StaticDependencyConsumptionMechanism = Literal[
    "direct_requirements",
    "project_environment",
]
type StaticMembershipKind = Literal["direct", "transitive"]
type ProjectEnvironmentMembershipEvidence = (
    ProjectSourceEnvironmentMembership | UvSelectedEnvironmentMembership
)


@dataclass(frozen=True, slots=True)
class StaticDependencyConsumptionEvidence:
    """One static CI declaration that may consume the changed dependency.

    ``supported`` means only that dependency-owned evidence establishes membership in the
    statically selected environment. It does not mean the command executed, installation
    succeeded, or the changed package was directly invoked.
    """

    state: StaticDependencyConsumptionState
    mechanism: StaticDependencyConsumptionMechanism
    job_key: str
    step_source_index: int
    segment_index: int
    command: str
    reason: str
    detail: str
    source_path: str | None = None
    membership_kind: StaticMembershipKind | None = None
    witness_path: tuple[str, ...] = ()


def compose_project_environment_consumption(
    *,
    job_key: str,
    observation: ProjectEnvironmentSelectionObservation,
    declaration: ProjectEnvironmentSelectionDeclaration,
    membership: ProjectEnvironmentMembershipEvidence,
) -> StaticDependencyConsumptionEvidence:
    """Map one dependency-owned selection/membership pair into CI consumption evidence."""

    if observation.state != "observed":
        raise ValueError(
            "project environment consumption requires an observed selection declaration"
        )
    if declaration not in observation.declarations:
        raise ValueError(
            "project environment declaration is not owned by the supplied observation"
        )
    if membership.state == "member" and membership.normalized_package == "":
        raise ValueError("membership evidence must preserve normalized package identity")

    membership_selectors = getattr(membership, "selectors", declaration.selectors)
    if membership_selectors != declaration.selectors:
        raise ValueError(
            "project environment membership selectors do not match the declaration"
        )

    if membership.state == "member":
        kind = getattr(membership, "membership_kind", "direct") or "direct"
        witness = getattr(membership, "witness_path", ())
        return StaticDependencyConsumptionEvidence(
            state="supported",
            mechanism="project_environment",
            job_key=job_key,
            step_source_index=observation.step_source_index,
            segment_index=declaration.segment_index,
            command=observation.command,
            reason="selected_environment_contains_changed_dependency",
            detail=(
                "Dependency-owned evidence establishes that this static project "
                "environment selection includes the changed dependency. Runtime "
                "execution and success are not established."
            ),
            source_path=getattr(membership, "project_file_path", observation.project_file_path),
            membership_kind=kind,
            witness_path=witness,
        )

    if membership.state == "not_established":
        return StaticDependencyConsumptionEvidence(
            state="not_established",
            mechanism="project_environment",
            job_key=job_key,
            step_source_index=observation.step_source_index,
            segment_index=declaration.segment_index,
            command=observation.command,
            reason="selected_environment_membership_not_established",
            detail=membership.detail,
            source_path=getattr(membership, "project_file_path", observation.project_file_path),
        )

    return StaticDependencyConsumptionEvidence(
        state="unresolved",
        mechanism="project_environment",
        job_key=job_key,
        step_source_index=observation.step_source_index,
        segment_index=declaration.segment_index,
        command=observation.command,
        reason=membership.reason,
        detail=membership.detail,
        source_path=getattr(membership, "project_file_path", observation.project_file_path),
    )


__all__ = (
    "ProjectEnvironmentMembershipEvidence",
    "StaticDependencyConsumptionEvidence",
    "StaticDependencyConsumptionMechanism",
    "StaticDependencyConsumptionState",
    "StaticMembershipKind",
    "compose_project_environment_consumption",
)
