"""Bounded static ordering relations for CI command evidence.

This module owns only the proposition that one static package invocation is ordered after one
static dependency-consumption declaration in the same job. It does not establish execution,
success, or runtime command identity.

Same-step ordering uses only canonical parsed command locations plus parser-neutral structural
context. Different user-defined run steps retain GitHub Actions source order through
``step_source_index``.
"""

from __future__ import annotations

from typing import Literal

from .consumption import StaticDependencyConsumptionEvidence
from .workflow_commands import DirectPackageInvocationEvidence


type StaticCommandOrderRelation = Literal[
    "ordered_after",
    "not_after",
    "unresolved",
]


_PATH_DEPENDENT_STRUCTURES = frozenset(
    {
        "short_circuit",
        "conditional",
        "loop",
        "pipeline",
        "function_or_block",
        "nested_or_subshell",
    }
)


def relate_invocation_after_consumption(
    consumption: StaticDependencyConsumptionEvidence,
    invocation: DirectPackageInvocationEvidence,
) -> StaticCommandOrderRelation:
    """Classify the bounded static order between one consumption and invocation."""

    if consumption.job_key != invocation.job_key:
        return "not_after"

    if invocation.step_source_index > consumption.step_source_index:
        return "ordered_after"
    if invocation.step_source_index < consumption.step_source_index:
        return "not_after"

    if consumption.command_location is None or invocation.command_location is None:
        return "unresolved"

    consumption_order = consumption.command_location.source_order
    invocation_order = invocation.command_location.source_order
    if invocation_order <= consumption_order:
        return "not_after"
    if _path_dependent(consumption.structural_context):
        return "unresolved"
    if _path_dependent(invocation.structural_context):
        return "unresolved"
    return "ordered_after"


def _path_dependent(structural_context: tuple[str, ...]) -> bool:
    return any(item in _PATH_DEPENDENT_STRUCTURES for item in structural_context)


__all__ = (
    "StaticCommandOrderRelation",
    "relate_invocation_after_consumption",
)
