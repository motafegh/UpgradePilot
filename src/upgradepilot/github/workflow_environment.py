"""Resolve bounded GitHub Actions env declarations without claiming process state.

This module owns only provider-declared workflow/job/step environment precedence. It preserves
literal, dynamic, absent, and ambiguous declaration states so later CI/shell composition can
reason about the exact process environment without treating static env declarations as
runtime truth.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .workflow_definition import (
    GitHubActionsStaticValue,
    RunStepDefinition,
    StaticMappingValue,
    StaticScalarValue,
    StepsJobDefinition,
    WorkflowDefinition,
)


type WorkflowEnvironmentScope = Literal["step", "job", "workflow"]
type WorkflowEnvironmentValueState = Literal["established", "not_declared", "unresolved"]
type WorkflowEnvironmentScopeDisposition = Literal[
    "decisive",
    "not_declared",
    "unresolved",
]


@dataclass(frozen=True, slots=True)
class WorkflowEnvironmentScopeInspection:
    """One checked declarative scope in GitHub's step > job > workflow precedence."""

    scope: WorkflowEnvironmentScope
    disposition: WorkflowEnvironmentScopeDisposition
    detail: str


@dataclass(frozen=True, slots=True)
class WorkflowEnvironmentValueObservation:
    """Static declaration result for one variable at one workflow run step."""

    state: WorkflowEnvironmentValueState
    variable_name: str
    value: str | None
    source_scope: WorkflowEnvironmentScope | None
    reason: str
    detail: str
    workflow_path: str
    workflow_revision: str
    job_key: str
    step_source_index: int
    inspected_scopes: tuple[WorkflowEnvironmentScopeInspection, ...]


def observe_workflow_environment_value(
    workflow: WorkflowDefinition,
    job: StepsJobDefinition,
    step: RunStepDefinition,
    variable_name: str,
) -> WorkflowEnvironmentValueObservation:
    """Resolve one provider-declared variable through step > job > workflow precedence.

    This deliberately stops at static workflow declarations. A positive literal declaration
    is not yet an exact-process value because shell-local assignments, earlier GITHUB_ENV
    writes, provider effects, or other admitted runtime sources may still be closer to the
    command process.
    """

    requested = variable_name.strip()
    if not requested:
        raise ValueError("workflow environment lookup requires a variable name")

    inspected: list[WorkflowEnvironmentScopeInspection] = []
    candidates: tuple[tuple[WorkflowEnvironmentScope, StaticMappingValue | None], ...] = (
        ("step", step.environment),
        ("job", job.environment),
        ("workflow", workflow.environment),
    )

    for scope, mapping in candidates:
        result = _inspect_scope(mapping, requested, scope=scope)
        inspected.append(result.inspection)

        if result.state == "unresolved":
            return _observation(
                workflow,
                job,
                step,
                requested,
                state="unresolved",
                source_scope=scope,
                reason=result.reason,
                detail=result.detail,
                inspected_scopes=tuple(inspected),
            )
        if result.state == "established":
            return _observation(
                workflow,
                job,
                step,
                requested,
                state="established",
                value=result.value,
                source_scope=scope,
                reason="workflow_environment_literal_established",
                detail=(
                    f"GitHub Actions {scope}-level env declares {requested!r} as a "
                    "literal value and shadows lower declarative scopes."
                ),
                inspected_scopes=tuple(inspected),
            )

    return _observation(
        workflow,
        job,
        step,
        requested,
        state="not_declared",
        source_scope=None,
        reason="workflow_environment_variable_not_declared",
        detail=(
            f"No workflow, job, or step env declaration for {requested!r} was found. "
            "This does not establish absence from the eventual command process."
        ),
        inspected_scopes=tuple(inspected),
    )


@dataclass(frozen=True, slots=True)
class _ScopeResult:
    state: Literal["established", "not_declared", "unresolved"]
    value: str | None
    reason: str
    detail: str
    inspection: WorkflowEnvironmentScopeInspection


def _inspect_scope(
    mapping: StaticMappingValue | None,
    variable_name: str,
    *,
    scope: WorkflowEnvironmentScope,
) -> _ScopeResult:
    if mapping is None:
        return _scope_result(
            scope,
            state="not_declared",
            reason="environment_scope_not_declared",
            detail=f"{scope}-level env is absent.",
        )

    dynamic_keys = tuple(
        entry for entry in mapping.entries if entry.key.contains_expression
    )
    exact = tuple(
        entry
        for entry in mapping.entries
        if not entry.key.contains_expression and entry.key.text == variable_name
    )

    if dynamic_keys:
        return _scope_result(
            scope,
            state="unresolved",
            reason="environment_variable_key_dynamic",
            detail=(
                f"{scope}-level env contains an expression-bearing key that could collide "
                f"with requested variable {variable_name!r}."
            ),
        )

    if len(exact) > 1:
        return _scope_result(
            scope,
            state="unresolved",
            reason="environment_variable_declared_multiple_times",
            detail=(
                f"{scope}-level env declares {variable_name!r} multiple times, so bounded "
                "static precedence cannot select one value safely."
            ),
        )

    if not exact:
        return _scope_result(
            scope,
            state="not_declared",
            reason="environment_variable_not_declared_in_scope",
            detail=f"{scope}-level env does not declare {variable_name!r}.",
        )

    value: GitHubActionsStaticValue = exact[0].value
    if not isinstance(value, StaticScalarValue):
        return _scope_result(
            scope,
            state="unresolved",
            reason="environment_variable_value_not_scalar",
            detail=(
                f"{scope}-level env value for {variable_name!r} is not a scalar in the "
                "bounded workflow representation."
            ),
        )
    if value.contains_expression:
        return _scope_result(
            scope,
            state="unresolved",
            reason="environment_variable_value_dynamic",
            detail=(
                f"{scope}-level env value for {variable_name!r} depends on a GitHub "
                "expression that this bounded static layer does not evaluate."
            ),
        )

    return _scope_result(
        scope,
        state="established",
        value=value.text,
        reason="environment_variable_literal_in_scope",
        detail=f"{scope}-level env declares a literal value for {variable_name!r}.",
    )


def _scope_result(
    scope: WorkflowEnvironmentScope,
    *,
    state: Literal["established", "not_declared", "unresolved"],
    reason: str,
    detail: str,
    value: str | None = None,
) -> _ScopeResult:
    disposition: WorkflowEnvironmentScopeDisposition = (
        "decisive" if state == "established" else state
    )
    return _ScopeResult(
        state=state,
        value=value,
        reason=reason,
        detail=detail,
        inspection=WorkflowEnvironmentScopeInspection(
            scope=scope,
            disposition=disposition,
            detail=detail,
        ),
    )


def _observation(
    workflow: WorkflowDefinition,
    job: StepsJobDefinition,
    step: RunStepDefinition,
    variable_name: str,
    *,
    state: WorkflowEnvironmentValueState,
    source_scope: WorkflowEnvironmentScope | None,
    reason: str,
    detail: str,
    inspected_scopes: tuple[WorkflowEnvironmentScopeInspection, ...],
    value: str | None = None,
) -> WorkflowEnvironmentValueObservation:
    return WorkflowEnvironmentValueObservation(
        state=state,
        variable_name=variable_name,
        value=value,
        source_scope=source_scope,
        reason=reason,
        detail=detail,
        workflow_path=workflow.source.path,
        workflow_revision=workflow.source.revision,
        job_key=job.key,
        step_source_index=step.source_index,
        inspected_scopes=inspected_scopes,
    )


__all__ = (
    "WorkflowEnvironmentScopeInspection",
    "WorkflowEnvironmentValueObservation",
    "observe_workflow_environment_value",
)
