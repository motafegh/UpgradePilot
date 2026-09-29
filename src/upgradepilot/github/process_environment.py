"""Bounded exact-command process-environment evidence for GitHub Actions run steps.

The first admitted producer is a Bash command-local environment assignment because it
directly controls the environment of that exact command process. Workflow/job/step env
observations are retained as provenance pressure but are not promoted to exact-process
truth until closer shell/runtime sources such as earlier exports and GITHUB_ENV writes are
modeled.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .workflow_command_analysis import StaticCommandOccurrence
from .workflow_command_location import StaticCommandLocation
from .workflow_command_shell import resolve_effective_shell_context
from .workflow_definition import RunStepDefinition, StepsJobDefinition, WorkflowDefinition
from .workflow_environment import observe_workflow_environment_value


type ProcessEnvironmentValueState = Literal["established", "unresolved"]
type ProcessEnvironmentValueSource = Literal[
    "command_local_assignment",
    "workflow_declaration",
    "ambient_or_runtime",
]


@dataclass(frozen=True, slots=True)
class ProcessEnvironmentValueEvidence:
    """Value evidence for one variable at one exact static command occurrence."""

    state: ProcessEnvironmentValueState
    variable_name: str
    value: str | None
    source: ProcessEnvironmentValueSource
    reason: str
    detail: str
    command_location: StaticCommandLocation
    workflow_path: str
    workflow_revision: str
    job_key: str
    step_source_index: int


def observe_exact_process_environment_value(
    workflow: WorkflowDefinition,
    job: StepsJobDefinition,
    step: RunStepDefinition,
    occurrence: StaticCommandOccurrence,
    variable_name: str,
) -> ProcessEnvironmentValueEvidence:
    """Establish one exact process value only when current evidence is decisive."""

    requested = variable_name.strip()
    if not requested:
        raise ValueError("process environment lookup requires a variable name")

    location = StaticCommandLocation.from_occurrence(occurrence)
    shell = resolve_effective_shell_context(workflow, job, step)
    if shell.state != "resolved" or shell.syntax_family != "bash":
        return _result(
            workflow,
            job,
            step,
            location,
            requested,
            state="unresolved",
            source="ambient_or_runtime",
            reason="process_environment_shell_not_admitted",
            detail=(
                "The first exact-process environment producer admits Bash command-local "
                "assignments only; this command's shell family is not positively admitted."
            ),
        )

    unknown_names = tuple(
        assignment
        for assignment in occurrence.environment_assignments
        if assignment.name is None
    )
    if unknown_names:
        return _result(
            workflow,
            job,
            step,
            location,
            requested,
            state="unresolved",
            source="command_local_assignment",
            reason="process_environment_assignment_name_unresolved",
            detail=(
                "A command-local environment assignment has an unsupported name and could "
                f"conflict with requested variable {requested!r}."
            ),
        )

    matches = tuple(
        assignment
        for assignment in occurrence.environment_assignments
        if assignment.name == requested
    )
    if len(matches) > 1:
        return _result(
            workflow,
            job,
            step,
            location,
            requested,
            state="unresolved",
            source="command_local_assignment",
            reason="process_environment_multiple_command_local_assignments",
            detail=(
                f"The exact command declares {requested!r} more than once; duplicate "
                "assignment composition is outside the first admitted producer."
            ),
        )
    if matches:
        assignment = matches[0]
        if assignment.state != "literal" or assignment.value.literal_value is None:
            return _result(
                workflow,
                job,
                step,
                location,
                requested,
                state="unresolved",
                source="command_local_assignment",
                reason="process_environment_command_local_value_unresolved",
                detail=(
                    f"The exact command locally assigns {requested!r}, but its value is "
                    "dynamic or unsupported."
                ),
            )
        return _result(
            workflow,
            job,
            step,
            location,
            requested,
            state="established",
            value=assignment.value.literal_value,
            source="command_local_assignment",
            reason="process_environment_command_local_value_established",
            detail=(
                f"A literal Bash command-local assignment establishes {requested!r} for "
                "this exact command process and overrides inherited values."
            ),
        )

    declared = observe_workflow_environment_value(workflow, job, step, requested)
    if declared.state == "unresolved":
        return _result(
            workflow,
            job,
            step,
            location,
            requested,
            state="unresolved",
            source="workflow_declaration",
            reason="process_environment_workflow_declaration_unresolved",
            detail=(
                f"The closest workflow env declaration for {requested!r} is unresolved; "
                "the exact process value therefore remains unresolved."
            ),
        )
    if declared.state == "established":
        return _result(
            workflow,
            job,
            step,
            location,
            requested,
            state="unresolved",
            source="workflow_declaration",
            reason="process_environment_closer_runtime_sources_unmodeled",
            detail=(
                f"A literal {declared.source_scope}-level env declaration exists for "
                f"{requested!r}, but command-local absence alone does not rule out closer "
                "same-step shell state or prior runtime propagation such as GITHUB_ENV."
            ),
        )

    return _result(
        workflow,
        job,
        step,
        location,
        requested,
        state="unresolved",
        source="ambient_or_runtime",
        reason="process_environment_ambient_sources_unresolved",
        detail=(
            f"No admitted declarative or command-local value establishes {requested!r}; "
            "runner ambient state and other runtime producers have not been ruled out."
        ),
    )


def _result(
    workflow: WorkflowDefinition,
    job: StepsJobDefinition,
    step: RunStepDefinition,
    command_location: StaticCommandLocation,
    variable_name: str,
    *,
    state: ProcessEnvironmentValueState,
    source: ProcessEnvironmentValueSource,
    reason: str,
    detail: str,
    value: str | None = None,
) -> ProcessEnvironmentValueEvidence:
    return ProcessEnvironmentValueEvidence(
        state=state,
        variable_name=variable_name,
        value=value,
        source=source,
        reason=reason,
        detail=detail,
        command_location=command_location,
        workflow_path=workflow.source.path,
        workflow_revision=workflow.source.revision,
        job_key=job.key,
        step_source_index=step.source_index,
    )


__all__ = (
    "ProcessEnvironmentValueEvidence",
    "observe_exact_process_environment_value",
)
