"""Interpret static workflow declarations as partial Target artifact-environment evidence.

This module is a Target consumer of the provider-owned GitHub Actions static IR. It
extracts only Target-relevant declarations (runner, setup-python version, and direct
installation of the independently established dependency source) while preserving the
proof boundary between static configuration and runtime execution.

The module intentionally does not parse YAML itself, infer exact wheel tags, evaluate
GitHub Actions expressions/matrices, execute reusable workflows, or claim that a visible
installation declaration formed a runtime environment.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..dependency.direct_install import observe_direct_installation_declaration
from ..github.repository import RepositoryFileEvidence, RepositoryTextFile, UnavailableRepositoryFile
from ..github.workflow_command_analysis import analyze_run_step_commands
from ..github.workflow_definition import (
    JobProblem,
    ReusableWorkflowJobDefinition,
    RunStepDefinition,
    StaticMappingValue,
    StaticScalarValue,
    StepsJobDefinition,
    UsesStepDefinition,
    WorkflowDefinition,
    WorkflowDefinitionProblem,
    parse_workflow_definition,
)
from ..repository_path import repository_relative_parts


type TargetDependencyInstallationDeclarationState = Literal[
    "observed",
    "not_observed",
    "unresolved",
]
type TargetArtifactEnvironmentProblemState = Literal[
    "file_unavailable",
    "workflow_definition_unreadable",
    "ambiguous_target_job_selection",
    "selected_target_job_not_found",
    "unsupported_target_job",
]


@dataclass(frozen=True, slots=True)
class TargetArtifactEnvironmentFact:
    """One literal Target-relevant fact preserved with a human-readable source locator."""

    value: str
    source: str


@dataclass(frozen=True, slots=True)
class TargetArtifactEnvironmentEvidence:
    """Partial static Target evidence for one safely selected workflow job.

    ``repository`` + immutable ``revision`` + ``workflow_path`` identify the exact source
    from which these Target facts were interpreted. Provider transport metadata is not
    propagated because it does not establish a separate Target proposition.

    ``dependency_installation_declaration`` is deliberately declaration-strength only.
    ``observed`` means a static run step visibly names the dependency source through the
    shared dependency observer; it does not mean that command executed or succeeded.
    """

    repository: str
    revision: str
    workflow_path: str
    job: str
    runner: TargetArtifactEnvironmentFact | None
    python_version: TargetArtifactEnvironmentFact | None
    dependency_installation_declaration: TargetDependencyInstallationDeclarationState
    installation_declaration_source: str | None
    limitations: tuple[str, ...]
    exact_wheel_compatibility_state: Literal["unresolved"] = "unresolved"


@dataclass(frozen=True, slots=True)
class TargetArtifactEnvironmentProblem:
    """Target-level abstention when the current proposition cannot be interpreted safely."""

    state: TargetArtifactEnvironmentProblemState
    revision: str
    workflow_path: str
    detail: str
    repository: str | None = None
    job: str | None = None


type TargetArtifactEnvironmentResult = (
    TargetArtifactEnvironmentEvidence | TargetArtifactEnvironmentProblem
)


def interpret_target_artifact_environment(
    evidence: RepositoryFileEvidence,
    *,
    dependency_source_file: str,
    consuming_job_key: str | None = None,
) -> TargetArtifactEnvironmentResult:
    """Interpret one exact-revision job's partial Target declarations.

    ``consuming_job_key`` is an already-established static workflow job ID supplied by
    the CI/application composition boundary. When provided, select only that exact job;
    do not independently guess a job from the workflow's other declarations. Omission
    preserves the existing direct-caller, one-job-only interpretation contract.
    """

    if repository_relative_parts(dependency_source_file) is None:
        raise ValueError(
            "dependency_source_file must be a normalized repository-relative POSIX path"
        )
    if consuming_job_key is not None and not consuming_job_key.strip():
        raise ValueError("consuming_job_key must be a non-empty workflow job ID")

    if isinstance(evidence, UnavailableRepositoryFile):
        return TargetArtifactEnvironmentProblem(
            state="file_unavailable",
            repository=evidence.repository,
            revision=evidence.revision,
            workflow_path=evidence.path,
            detail=evidence.detail,
            job=consuming_job_key,
        )

    assert isinstance(evidence, RepositoryTextFile)

    definition_result = parse_workflow_definition(evidence)
    if isinstance(definition_result, WorkflowDefinitionProblem):
        return _problem(
            evidence,
            "workflow_definition_unreadable",
            f"{definition_result.reason}: {definition_result.detail}",
            job=consuming_job_key,
        )

    assert isinstance(definition_result, WorkflowDefinition)
    job_result = _select_target_job(
        definition_result,
        evidence,
        consuming_job_key=consuming_job_key,
    )
    if isinstance(job_result, TargetArtifactEnvironmentProblem):
        return job_result

    job = job_result
    limitations: list[str] = []

    # The IR preserves richer runner forms, but this Target slice establishes only one
    # literal scalar runner. Dynamic/sequence/mapping forms remain partial evidence.
    runner = _interpret_runner(job, limitations)
    python_version, setup_problem = _interpret_setup_python(job, limitations)
    if setup_problem is not None:
        return _problem(
            evidence,
            "unsupported_target_job",
            setup_problem,
            job=job.key,
        )

    if job.strategy is not None:
        limitations.append("strategy_context_not_interpreted")
    if job.container is not None:
        limitations.append("container_context_not_interpreted")

    declaration_state, declaration_source = _interpret_dependency_installation(
        definition_result,
        job,
        dependency_source_file=dependency_source_file,
        limitations=limitations,
    )

    return TargetArtifactEnvironmentEvidence(
        repository=evidence.repository,
        revision=evidence.revision,
        workflow_path=evidence.path,
        job=job.key,
        runner=runner,
        python_version=python_version,
        dependency_installation_declaration=declaration_state,
        installation_declaration_source=declaration_source,
        limitations=tuple(limitations),
    )


def _select_target_job(
    definition: WorkflowDefinition,
    evidence: RepositoryTextFile,
    *,
    consuming_job_key: str | None,
) -> StepsJobDefinition | TargetArtifactEnvironmentProblem:
    """Select only an explicitly identified job, or the legacy sole-job case.

    CI owns evidence that a job statically consumes a changed dependency. Target owns
    interpretation of that exact job's declared environment, not CI job-selection policy.
    An absent selected key remains unresolved rather than selecting another job.
    """

    if consuming_job_key is None:
        if len(definition.jobs) != 1:
            return _problem(
                evidence,
                "ambiguous_target_job_selection",
                (
                    "The workflow definition is structurally readable, but the current "
                    f"Target interpreter requires one job and observed {len(definition.jobs)}."
                ),
            )
        job = definition.jobs[0]
    else:
        matching_jobs = tuple(
            job for job in definition.jobs if job.key == consuming_job_key
        )
        if not matching_jobs:
            return _problem(
                evidence,
                "selected_target_job_not_found",
                "The CI-selected consuming job was not found in the exact workflow definition.",
                job=consuming_job_key,
            )
        # The provider rejects duplicate workflow job IDs; a defensive check prevents
        # a future parser change from silently choosing between ambiguous matches.
        if len(matching_jobs) != 1:
            return _problem(
                evidence,
                "ambiguous_target_job_selection",
                "The selected consuming job ID is not unique in the workflow definition.",
                job=consuming_job_key,
            )
        job = matching_jobs[0]

    if isinstance(job, JobProblem):
        return _problem(
            evidence,
            "unsupported_target_job",
            f"{job.reason}: {job.detail}",
            job=job.key,
        )
    if isinstance(job, ReusableWorkflowJobDefinition):
        return _problem(
            evidence,
            "unsupported_target_job",
            (
                "The workflow job delegates to a reusable workflow; resolving that "
                "separate workflow source is outside this Target slice."
            ),
            job=job.key,
        )

    assert isinstance(job, StepsJobDefinition)
    return job


def _interpret_runner(
    job: StepsJobDefinition,
    limitations: list[str],
) -> TargetArtifactEnvironmentFact | None:
    """Establish a runner fact only from one literal scalar ``runs-on`` declaration."""

    value = job.runs_on
    if value is None:
        limitations.append("runner_not_statically_identified")
        return None
    if not isinstance(value, StaticScalarValue) or value.contains_expression:
        limitations.append("runner_not_single_literal")
        return None

    return TargetArtifactEnvironmentFact(
        value=value.text,
        source=f"runs-on declaration at line {value.span.start_line}",
    )


def _interpret_setup_python(
    job: StepsJobDefinition,
    limitations: list[str],
) -> tuple[TargetArtifactEnvironmentFact | None, str | None]:
    """Read one literal ``actions/setup-python`` ``python-version`` input when present."""

    setup_steps = [
        step
        for step in job.steps
        if isinstance(step, UsesStepDefinition)
        and not step.reference.contains_expression
        and step.reference.text.lower().startswith("actions/setup-python@")
    ]

    if len(setup_steps) > 1:
        return None, "Multiple setup-python steps remain ambiguous for this Target slice."
    if not setup_steps:
        limitations.append("setup_python_version_not_observed")
        return None, None

    step = setup_steps[0]
    python_values = _mapping_values(step.with_inputs, "python-version")
    if len(python_values) > 1:
        return None, "Multiple python-version inputs were declared for setup-python."
    if not python_values:
        limitations.append("setup_python_version_not_observed")
        return None, None

    value = python_values[0]
    if not isinstance(value, StaticScalarValue) or value.contains_expression:
        limitations.append("setup_python_version_not_literal")
        return None, None

    return (
        TargetArtifactEnvironmentFact(
            value=value.text,
            source=f"setup-python python-version at line {value.span.start_line}",
        ),
        None,
    )


def _mapping_values(
    mapping: StaticMappingValue | None,
    key: str,
) -> tuple[object, ...]:
    """Return all values for a material input key without silently collapsing duplicates."""

    if mapping is None:
        return ()
    return tuple(entry.value for entry in mapping.entries if entry.key.text == key)


def _interpret_dependency_installation(
    definition: WorkflowDefinition,
    job: StepsJobDefinition,
    *,
    dependency_source_file: str,
    limitations: list[str],
) -> tuple[TargetDependencyInstallationDeclarationState, str | None]:
    """Compose run-step observations without upgrading them beyond static declaration proof."""

    observations = [
        observe_direct_installation_declaration(
            step,
            dependency_source_path=dependency_source_file,
            command_analysis=analyze_run_step_commands(definition, job, step),
            workflow_defaults=definition.run_defaults,
            job_defaults=job.run_defaults,
        )
        for step in job.steps
        if isinstance(step, RunStepDefinition)
    ]

    observed = next((item for item in observations if item.state == "observed"), None)
    if observed is not None:
        return "observed", observed.command

    # Unresolved path context has stronger significance than a simple non-observation:
    # the source contains a potentially relevant declaration we cannot resolve safely.
    if any(item.state == "unresolved" for item in observations):
        limitations.append("changed_dependency_installation_declaration_unresolved")
        return "unresolved", None

    limitations.append("changed_dependency_installation_declaration_not_observed")
    return "not_observed", None


def _problem(
    evidence: RepositoryTextFile,
    state: TargetArtifactEnvironmentProblemState,
    detail: str,
    *,
    job: str | None = None,
) -> TargetArtifactEnvironmentProblem:
    """Build a provenance-carrying Target abstention result."""

    return TargetArtifactEnvironmentProblem(
        state=state,
        repository=evidence.repository,
        revision=evidence.revision,
        workflow_path=evidence.path,
        detail=detail,
        job=job,
    )


__all__ = (
    "TargetArtifactEnvironmentEvidence",
    "TargetArtifactEnvironmentFact",
    "TargetArtifactEnvironmentProblem",
    "TargetArtifactEnvironmentProblemState",
    "TargetArtifactEnvironmentResult",
    "TargetDependencyInstallationDeclarationState",
    "interpret_target_artifact_environment",
)
