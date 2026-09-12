"""Correlate exact static workflow jobs/steps with exact-attempt runtime evidence.

GitHub provider modules own the factual static and runtime records. This CI module owns only
the deterministic relationship between those independently acquired records for the bounded
ordinary-workflow class admitted by the current design. Unsupported or ambiguous shapes stay
explicitly unresolved rather than being guessed into execution evidence.

Correlation answers identity only. Runtime status/conclusion is preserved on the matched
``WorkflowStep`` but is not interpreted here as dependency installation, exercise, or success.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from ..github.actions import WorkflowJob, WorkflowRun, WorkflowStep
from ..github.repository import RepositoryTextFile
from ..github.workflow_definition import (
    JobProblem,
    ReusableWorkflowJobDefinition,
    RunStepDefinition,
    StepProblem,
    StepsJobDefinition,
    UsesStepDefinition,
    WorkflowDefinition,
    WorkflowDefinitionProblem,
    parse_workflow_definition,
)


type CorrelatableWorkflowStep = RunStepDefinition | UsesStepDefinition
type WorkflowRuntimeCorrelationState = Literal["correlated", "unresolved"]


@dataclass(frozen=True, slots=True)
class WorkflowRuntimeStepCorrelation:
    """One user-declared static step matched to one factual runtime step record."""

    static_step: CorrelatableWorkflowStep
    runtime_step: WorkflowStep


@dataclass(frozen=True, slots=True)
class WorkflowRuntimeJobCorrelation:
    """One static steps job matched to one runtime job plus its user-step matches."""

    static_job: StepsJobDefinition
    runtime_job: WorkflowJob
    steps: tuple[WorkflowRuntimeStepCorrelation, ...]


@dataclass(frozen=True, slots=True)
class WorkflowRuntimeCorrelationResult:
    """Workflow-scoped correlation result with ambiguity preserved as unresolved."""

    state: WorkflowRuntimeCorrelationState
    reason: str
    detail: str
    jobs: tuple[WorkflowRuntimeJobCorrelation, ...] = ()


def correlate_workflow_runtime(
    source: RepositoryTextFile,
    run: WorkflowRun,
    jobs: Sequence[WorkflowJob],
) -> WorkflowRuntimeCorrelationResult:
    """Correlate the first admitted ordinary static workflow class to runtime evidence.

    Positive correlation requires an exact static/run revision match, ordinary non-strategy
    steps jobs with unique literal names, an exact static/runtime job-name bijection, and
    unique literal static step names that appear once and in order within each runtime job.
    Runtime-only setup/post/completion steps are allowed between those user-declared steps.
    """

    if source.revision != run.head_sha:
        return _unresolved(
            "workflow_revision_mismatch",
            "Static workflow revision does not match the runtime workflow head SHA.",
        )

    definition = parse_workflow_definition(source)
    if isinstance(definition, WorkflowDefinitionProblem):
        return _unresolved(
            "static_workflow_definition_unresolved",
            f"Static workflow definition is unresolved: {definition.reason}: {definition.detail}",
        )

    static_jobs: list[StepsJobDefinition] = []
    static_job_names: list[str] = []
    for job in definition.jobs:
        if isinstance(job, JobProblem):
            return _unresolved(
                "static_job_unresolved",
                f"Static job structure is unresolved: {job.reason}: {job.detail}",
            )
        if isinstance(job, ReusableWorkflowJobDefinition):
            return _unresolved(
                "reusable_workflow_job_unsupported",
                f"Reusable workflow job {job.key!r} is outside the first correlation class.",
            )
        assert isinstance(job, StepsJobDefinition)
        if job.strategy is not None:
            return _unresolved(
                "static_job_strategy_unsupported",
                f"Job {job.key!r} uses strategy/matrix expansion, which is not yet correlated.",
            )
        if job.name is None:
            return _unresolved(
                "static_job_name_missing",
                f"Job {job.key!r} has no explicit display name for bounded correlation.",
            )
        if job.name.contains_expression:
            return _unresolved(
                "static_job_name_dynamic",
                f"Job {job.key!r} has a dynamic display name that cannot be matched literally.",
            )
        job_name = job.name.text
        if not job_name.strip():
            return _unresolved(
                "static_job_name_empty",
                f"Job {job.key!r} has an empty display name.",
            )
        static_jobs.append(job)
        static_job_names.append(job_name)

    duplicate_static_job_name = _first_duplicate(static_job_names)
    if duplicate_static_job_name is not None:
        return _unresolved(
            "duplicate_static_job_name",
            f"Static job display name {duplicate_static_job_name!r} is not unique.",
        )

    runtime_job_names = [job.name for job in jobs]
    duplicate_runtime_job_name = _first_duplicate(runtime_job_names)
    if duplicate_runtime_job_name is not None:
        return _unresolved(
            "duplicate_runtime_job_name",
            f"Runtime job display name {duplicate_runtime_job_name!r} is not unique.",
        )

    if set(static_job_names) != set(runtime_job_names):
        return _unresolved(
            "static_runtime_job_name_set_mismatch",
            "Static and runtime job display-name sets do not form a one-to-one match.",
        )

    runtime_jobs_by_name = {job.name: job for job in jobs}
    correlations: list[WorkflowRuntimeJobCorrelation] = []
    for static_job, static_job_name in zip(static_jobs, static_job_names, strict=True):
        runtime_job = runtime_jobs_by_name[static_job_name]
        step_result = _correlate_job_steps(static_job, runtime_job)
        if isinstance(step_result, WorkflowRuntimeCorrelationResult):
            return step_result
        correlations.append(
            WorkflowRuntimeJobCorrelation(
                static_job=static_job,
                runtime_job=runtime_job,
                steps=step_result,
            )
        )

    return WorkflowRuntimeCorrelationResult(
        state="correlated",
        reason="workflow_jobs_and_steps_correlated",
        detail=(
            "Static ordinary jobs and user-declared steps were matched one-to-one to "
            "runtime jobs and ordered runtime step summaries."
        ),
        jobs=tuple(correlations),
    )


def _correlate_job_steps(
    static_job: StepsJobDefinition,
    runtime_job: WorkflowJob,
) -> tuple[WorkflowRuntimeStepCorrelation, ...] | WorkflowRuntimeCorrelationResult:
    static_steps: list[CorrelatableWorkflowStep] = []
    static_step_names: list[str] = []
    for step in static_job.steps:
        if isinstance(step, StepProblem):
            return _unresolved(
                "static_step_unresolved",
                (
                    f"Job {static_job.key!r} contains unresolved static step structure: "
                    f"{step.reason}: {step.detail}"
                ),
            )
        assert isinstance(step, (RunStepDefinition, UsesStepDefinition))
        if step.name is None:
            return _unresolved(
                "static_step_name_missing",
                (
                    f"Job {static_job.key!r} step {step.source_index} has no explicit "
                    "display name for bounded correlation."
                ),
            )
        if step.name.contains_expression:
            return _unresolved(
                "static_step_name_dynamic",
                (
                    f"Job {static_job.key!r} step {step.source_index} has a dynamic "
                    "display name that cannot be matched literally."
                ),
            )
        step_name = step.name.text
        if not step_name.strip():
            return _unresolved(
                "static_step_name_empty",
                f"Job {static_job.key!r} step {step.source_index} has an empty display name.",
            )
        static_steps.append(step)
        static_step_names.append(step_name)

    duplicate_static_step_name = _first_duplicate(static_step_names)
    if duplicate_static_step_name is not None:
        return _unresolved(
            "duplicate_static_step_name",
            (
                f"Job {static_job.key!r} repeats static step display name "
                f"{duplicate_static_step_name!r}."
            ),
        )

    if runtime_job.steps is None:
        return _unresolved(
            "runtime_steps_unavailable",
            f"Runtime job {runtime_job.name!r} did not provide step summaries.",
        )

    runtime_steps = runtime_job.steps
    runtime_numbers = [step.number for step in runtime_steps]
    if len(runtime_numbers) != len(set(runtime_numbers)):
        return _unresolved(
            "duplicate_runtime_step_number",
            f"Runtime job {runtime_job.name!r} contains duplicate step numbers.",
        )
    if any(current <= previous for previous, current in zip(runtime_numbers, runtime_numbers[1:])):
        return _unresolved(
            "runtime_step_numbers_not_ordered",
            f"Runtime job {runtime_job.name!r} step numbers are not strictly increasing.",
        )

    matched_indices: list[int] = []
    correlations: list[WorkflowRuntimeStepCorrelation] = []
    for static_step, static_step_name in zip(static_steps, static_step_names, strict=True):
        matches = [
            (index, runtime_step)
            for index, runtime_step in enumerate(runtime_steps)
            if runtime_step.name == static_step_name
        ]
        if not matches:
            return _unresolved(
                "runtime_step_match_missing",
                (
                    f"Runtime job {runtime_job.name!r} has no step matching static display "
                    f"name {static_step_name!r}."
                ),
            )
        if len(matches) != 1:
            return _unresolved(
                "runtime_step_match_ambiguous",
                (
                    f"Runtime job {runtime_job.name!r} has multiple steps matching static "
                    f"display name {static_step_name!r}."
                ),
            )
        runtime_index, runtime_step = matches[0]
        matched_indices.append(runtime_index)
        correlations.append(
            WorkflowRuntimeStepCorrelation(
                static_step=static_step,
                runtime_step=runtime_step,
            )
        )

    if any(current <= previous for previous, current in zip(matched_indices, matched_indices[1:])):
        return _unresolved(
            "static_runtime_step_order_mismatch",
            (
                f"Runtime job {runtime_job.name!r} does not preserve the declared user-step "
                "name order as an ordered subsequence."
            ),
        )

    return tuple(correlations)


def _first_duplicate(values: Sequence[str]) -> str | None:
    seen: set[str] = set()
    for value in values:
        if value in seen:
            return value
        seen.add(value)
    return None


def _unresolved(reason: str, detail: str) -> WorkflowRuntimeCorrelationResult:
    return WorkflowRuntimeCorrelationResult(
        state="unresolved",
        reason=reason,
        detail=detail,
    )


__all__ = (
    "CorrelatableWorkflowStep",
    "WorkflowRuntimeCorrelationResult",
    "WorkflowRuntimeCorrelationState",
    "WorkflowRuntimeJobCorrelation",
    "WorkflowRuntimeStepCorrelation",
    "correlate_workflow_runtime",
)
