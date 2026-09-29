"""Compose bounded executable-selection evidence for exact CI command occurrences.

Static command syntax owns explicit-path observations. This CI layer may strengthen a bare
executable only when provider workflow semantics, source ordering, and exact-attempt runtime
step evidence jointly establish a trustworthy PATH relationship.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

from ..github.executable_selection import observe_command_executable_selection
from ..github.workflow_command_analysis import StaticCommandOccurrence
from ..github.workflow_command_location import StaticCommandLocation
from ..github.workflow_definition import (
    RunStepDefinition,
    StaticMappingValue,
    StaticScalarValue,
    StepsJobDefinition,
    UsesStepDefinition,
    WorkflowDefinition,
)
from ..github.workflow_environment import observe_workflow_environment_value
from .runtime_execution import assess_correlated_step_execution
from .workflow_runtime_correlation import WorkflowRuntimeCorrelationResult


type ExecutableSelectionState = Literal["established", "unresolved"]
type ExecutableSelectionSource = Literal[
    "explicit_path",
    "setup_python_path",
    "path_lookup_unresolved",
]


@dataclass(frozen=True, slots=True)
class ExecutableSelectionEvidence:
    """Bounded executable-selection evidence for one exact command occurrence."""

    state: ExecutableSelectionState
    source: ExecutableSelectionSource
    executable: str | None
    environment_reference: str | None
    reason: str
    detail: str
    command_location: StaticCommandLocation
    provider_step_source_index: int | None = None
    provider_reference: str | None = None


_SETUP_PYTHON_SUPPORTED_REF = re.compile(
    r"^actions/setup-python@v(?:4|5|6|7)(?:\.\d+(?:\.\d+)?)?$",
    re.IGNORECASE,
)
_FIRST_PROCESS_RELATIONS = frozenset(
    {
        "sole_ordinary_top_level_command",
        "first_ordinary_top_level_command_in_sequential_script",
    }
)


def establish_executable_selection(
    workflow: WorkflowDefinition,
    job: StepsJobDefinition,
    step: RunStepDefinition,
    occurrence: StaticCommandOccurrence,
    *,
    correlation: WorkflowRuntimeCorrelationResult | None = None,
) -> ExecutableSelectionEvidence:
    """Resolve the first admitted executable-selection families.

    Explicit executable paths are established directly from command syntax. Bare python
    is strengthened only for the bounded setup-python family: an immediately preceding
    supported setup-python step, environment updating enabled, successful exact-attempt step
    execution, no declared or command-local PATH override, and a first/sole command occurrence
    in the later run step.
    """

    static = observe_command_executable_selection(occurrence)
    if static.state == "established":
        return ExecutableSelectionEvidence(
            state="established",
            source="explicit_path",
            executable=static.executable,
            environment_reference=static.executable,
            reason=static.reason,
            detail=static.detail,
            command_location=static.command_location,
        )

    location = StaticCommandLocation.from_occurrence(occurrence)
    executable = static.executable
    if executable != "python":
        return _unresolved(
            location,
            executable=executable,
            reason=static.reason,
            detail=static.detail,
        )

    if occurrence.whole_step_relation not in _FIRST_PROCESS_RELATIONS:
        return _unresolved(
            location,
            executable=executable,
            reason="bare_python_not_first_process_in_step",
            detail=(
                "The bounded setup-python PATH relation is admitted only when bare python is "
                "the first or sole ordinary command in its run step; earlier shell commands "
                "could otherwise alter executable selection."
            ),
        )

    if any(assignment.name == "PATH" for assignment in occurrence.environment_assignments):
        return _unresolved(
            location,
            executable=executable,
            reason="command_local_path_override",
            detail=(
                "The exact command carries a command-local PATH assignment, which is closer "
                "than an earlier setup-python PATH contribution."
            ),
        )

    declared_path = observe_workflow_environment_value(workflow, job, step, "PATH")
    if declared_path.state != "not_declared":
        return _unresolved(
            location,
            executable=executable,
            reason="workflow_path_declaration_requires_composition",
            detail=(
                "Workflow/job/step PATH declarations are present or unresolved; the first "
                "setup-python executable-selection family does not compose those overrides."
            ),
        )

    if step.source_index <= 0 or step.source_index >= len(job.steps):
        return _unresolved(
            location,
            executable=executable,
            reason="setup_python_adjacent_predecessor_missing",
            detail=(
                "Bare python has no immediately preceding user step that can establish the "
                "first admitted setup-python PATH relation."
            ),
        )

    provider_step = job.steps[step.source_index - 1]
    if not isinstance(provider_step, UsesStepDefinition):
        return _unresolved(
            location,
            executable=executable,
            reason="setup_python_adjacent_predecessor_missing",
            detail="The immediately preceding user step is not a setup-python uses step.",
        )

    if provider_step.reference.contains_expression or not _SETUP_PYTHON_SUPPORTED_REF.fullmatch(
        provider_step.reference.text.strip()
    ):
        return _unresolved(
            location,
            executable=executable,
            reason="setup_python_reference_not_admitted",
            detail=(
                "The immediately preceding uses step is not a literal supported "
                "actions/setup-python v4-v7 reference."
            ),
            provider_step_source_index=provider_step.source_index,
            provider_reference=provider_step.reference.text,
        )

    update_environment = _setup_python_update_environment(provider_step.with_inputs)
    if update_environment is None:
        return _unresolved(
            location,
            executable=executable,
            reason="setup_python_update_environment_unresolved",
            detail=(
                "setup-python update-environment is dynamic, duplicated, or otherwise "
                "unresolved."
            ),
            provider_step_source_index=provider_step.source_index,
            provider_reference=provider_step.reference.text,
        )
    if not update_environment:
        return _unresolved(
            location,
            executable=executable,
            reason="setup_python_update_environment_disabled",
            detail=(
                "setup-python explicitly disables environment updating, so its selected "
                "Python is not established as a PATH selector for the later bare command."
            ),
            provider_step_source_index=provider_step.source_index,
            provider_reference=provider_step.reference.text,
        )

    if correlation is None or correlation.state != "correlated":
        return _unresolved(
            location,
            executable=executable,
            reason="setup_python_runtime_execution_unresolved",
            detail=(
                "The setup-python PATH effect requires exact-attempt correlated successful "
                "execution of the provider step."
            ),
            provider_step_source_index=provider_step.source_index,
            provider_reference=provider_step.reference.text,
        )

    provider_correlation = _find_step_correlation(
        correlation,
        job_key=job.key,
        step_source_index=provider_step.source_index,
    )
    if provider_correlation is None:
        return _unresolved(
            location,
            executable=executable,
            reason="setup_python_runtime_step_correlation_missing",
            detail=(
                "The workflow runtime bridge is correlated, but the setup-python provider "
                "step has no retained runtime-step correlation."
            ),
            provider_step_source_index=provider_step.source_index,
            provider_reference=provider_step.reference.text,
        )

    provider_execution = assess_correlated_step_execution(provider_correlation)
    if provider_execution.state != "supported":
        return _unresolved(
            location,
            executable=executable,
            reason="setup_python_runtime_execution_not_supported",
            detail=(
                "The setup-python provider step does not have unmasked completed-successful "
                f"runtime execution: {provider_execution.reason}: {provider_execution.detail}"
            ),
            provider_step_source_index=provider_step.source_index,
            provider_reference=provider_step.reference.text,
        )

    return ExecutableSelectionEvidence(
        state="established",
        source="setup_python_path",
        executable="python",
        environment_reference=(
            f"setup-python-step:{provider_step.source_index}:"
            f"{provider_step.reference.text.strip()}"
        ),
        reason="setup_python_path_selection_established",
        detail=(
            "A supported setup-python step immediately precedes the run step, environment "
            "updating is enabled, the provider step executed successfully in this exact "
            "attempt, and no closer PATH override is admitted before the first bare python "
            "command. The selected executable is therefore related to that setup-python "
            "environment without inventing an absolute path."
        ),
        command_location=location,
        provider_step_source_index=provider_step.source_index,
        provider_reference=provider_step.reference.text,
    )


def _setup_python_update_environment(mapping: StaticMappingValue | None) -> bool | None:
    if mapping is None:
        return True

    if any(entry.key.contains_expression for entry in mapping.entries):
        return None
    matches = tuple(
        entry for entry in mapping.entries if entry.key.text == "update-environment"
    )
    if len(matches) > 1:
        return None
    if not matches:
        return True

    value = matches[0].value
    if not isinstance(value, StaticScalarValue) or value.contains_expression:
        return None
    folded = value.text.strip().casefold()
    if folded == "true":
        return True
    if folded == "false":
        return False
    return None


def _find_step_correlation(
    correlation: WorkflowRuntimeCorrelationResult,
    *,
    job_key: str,
    step_source_index: int,
):
    for correlated_job in correlation.jobs:
        if correlated_job.static_job.key != job_key:
            continue
        return next(
            (
                item
                for item in correlated_job.steps
                if item.static_step.source_index == step_source_index
            ),
            None,
        )
    return None


def _unresolved(
    command_location: StaticCommandLocation,
    *,
    executable: str | None,
    reason: str,
    detail: str,
    provider_step_source_index: int | None = None,
    provider_reference: str | None = None,
) -> ExecutableSelectionEvidence:
    return ExecutableSelectionEvidence(
        state="unresolved",
        source="path_lookup_unresolved",
        executable=executable,
        environment_reference=None,
        reason=reason,
        detail=detail,
        command_location=command_location,
        provider_step_source_index=provider_step_source_index,
        provider_reference=provider_reference,
    )


__all__ = (
    "ExecutableSelectionEvidence",
    "establish_executable_selection",
)
