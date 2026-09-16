"""Interpret bounded static CI dependency consumption and direct package invocation.

GitHub Actions YAML structure is owned by ``upgradepilot.github.workflow_definition``.
Shared shell parsing and parser-neutral command occurrences are owned by
``upgradepilot.github.workflow_command_analysis``. Dependency-source and project-selection
semantics remain dependency-owned. This CI module owns the single workflow-level traversal,
checkout provenance, direct changed-package invocation meaning, and cross-evidence
composition.

Cycle 2 routes direct requirements, project-environment selection, and direct package
invocation through one parsed workflow traversal and one ``StaticCommandAnalysis`` per run
step in the normal coverage path. Standalone project-environment derivation is retained as a
bounded compatibility/test seam over the same internal collector rather than a second
implementation.
"""

from __future__ import annotations

import posixpath
import re
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from ..dependency.direct_install import observe_direct_installation_declaration
from ..dependency.environment import (
    DependencySourceContext,
    RequirementsFileDependencyContext,
    UvLockDependencyContext,
)
from ..dependency.environment_membership import (
    ProjectSourceEnvironmentContext,
    evaluate_project_source_environment_membership,
)
from ..dependency.environment_selection import (
    ProjectEnvironmentSelectionObservation,
    observe_project_environment_selection,
)
from ..dependency.uv_reachability import evaluate_uv_selected_root_reachability
from ..github.repository import (
    RepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)
from ..github.workflow_command_analysis import (
    StaticCommandAnalysis,
    StaticCommandAtom,
    StaticCommandOccurrence,
    StaticCommandStructure,
    analyze_run_step_commands,
)
from ..github.workflow_command_location import StaticCommandLocation
from ..github.workflow_definition import (
    JobProblem,
    ReusableWorkflowJobDefinition,
    RunStepDefinition,
    StaticScalarValue,
    StepsJobDefinition,
    UsesStepDefinition,
    WorkflowDefinition,
    WorkflowDefinitionProblem,
    parse_workflow_definition,
)
from .consumption import (
    StaticDependencyConsumptionEvidence,
    compose_project_environment_consumption,
)


type _RepositoryRootCheckoutState = Literal[
    "not_established",
    "current_repository",
    "other_repository",
    "unresolved",
]
type _CheckoutPathTarget = Literal["root", "subpath", "unresolved"]
type DirectPackageInvocationState = Literal["observed", "unresolved"]


@dataclass(frozen=True, slots=True)
class DirectPackageInvocationEvidence:
    """One parsed static candidate for direct invocation of the changed package."""

    job_key: str
    step_source_index: int
    command: str
    state: DirectPackageInvocationState = "observed"
    reason: str = "direct_package_invocation_observed"
    detail: str = (
        "A real parsed static command occurrence directly invokes the changed package."
    )
    command_location: StaticCommandLocation | None = None
    structural_context: tuple[StaticCommandStructure, ...] = ()


@dataclass(frozen=True, slots=True)
class StaticWorkflowDependencyProblem:
    """One material static structure/source problem preserved without erasing other jobs."""

    reason: str
    detail: str
    job_key: str | None = None


@dataclass(frozen=True, slots=True)
class WorkflowStaticDependencyEvidence:
    """Multi-job static CI evidence with consumption and invocation kept separate."""

    job_count: int
    consumptions: tuple[StaticDependencyConsumptionEvidence, ...]
    invocations: tuple[DirectPackageInvocationEvidence, ...]
    problems: tuple[StaticWorkflowDependencyProblem, ...]


@dataclass(frozen=True, slots=True)
class WorkflowProjectEnvironmentSource:
    """Exact sources needed to derive project-environment consumption for one context."""

    context: ProjectSourceEnvironmentContext | UvLockDependencyContext
    project_file: RepositoryFileEvidence
    lock_file: RepositoryFileEvidence | None = None


def derive_project_environment_consumptions(
    source: RepositoryTextFile,
    *,
    sources: Sequence[WorkflowProjectEnvironmentSource],
    normalized_package: str,
) -> tuple[StaticDependencyConsumptionEvidence, ...]:
    """Compatibility/test seam over the shared one-traversal static evidence collector."""

    if not normalized_package:
        raise ValueError("project-environment derivation requires normalized package identity")

    static = _inspect_workflow_dependency_evidence(
        source,
        source_contexts=(),
        package="",
        normalized_package=normalized_package,
        project_environment_sources=sources,
        project_environment_consumptions=(),
        collect_invocations=False,
    )
    return tuple(
        item
        for item in static.consumptions
        if item.mechanism == "project_environment"
    )


def inspect_workflow_dependency_evidence(
    source: RepositoryTextFile,
    *,
    source_contexts: Sequence[DependencySourceContext],
    package: str,
    normalized_package: str,
    project_environment_sources: Sequence[WorkflowProjectEnvironmentSource] = (),
    project_environment_consumptions: Sequence[StaticDependencyConsumptionEvidence] = (),
) -> WorkflowStaticDependencyEvidence:
    """Collect all admitted static CI dependency evidence in one workflow traversal.

    In the normal production path, exact project-environment source bundles are supplied and
    project selection is interpreted from the same per-step ``StaticCommandAnalysis`` used by
    direct requirements and direct package invocation. Precomposed project-environment
    consumptions remain a focused-test seam, but must preserve canonical parsed command
    identity; callers may not mix the two project-environment input modes.
    """

    return _inspect_workflow_dependency_evidence(
        source,
        source_contexts=source_contexts,
        package=package,
        normalized_package=normalized_package,
        project_environment_sources=project_environment_sources,
        project_environment_consumptions=project_environment_consumptions,
        collect_invocations=True,
    )


def _inspect_workflow_dependency_evidence(
    source: RepositoryTextFile,
    *,
    source_contexts: Sequence[DependencySourceContext],
    package: str,
    normalized_package: str,
    project_environment_sources: Sequence[WorkflowProjectEnvironmentSource],
    project_environment_consumptions: Sequence[StaticDependencyConsumptionEvidence],
    collect_invocations: bool,
) -> WorkflowStaticDependencyEvidence:
    if project_environment_sources and project_environment_consumptions:
        raise ValueError(
            "project-environment sources and precomposed consumptions are mutually exclusive"
        )

    definition = parse_workflow_definition(source)
    if isinstance(definition, WorkflowDefinitionProblem):
        return WorkflowStaticDependencyEvidence(
            job_count=0,
            consumptions=(),
            invocations=(),
            problems=(
                StaticWorkflowDependencyProblem(
                    reason="workflow_definition_unreadable",
                    detail=(
                        "The shared GitHub Actions definition could not establish the "
                        f"bounded CI structure: {definition.reason}: {definition.detail}"
                    ),
                ),
            ),
        )

    assert isinstance(definition, WorkflowDefinition)
    requirements_contexts = tuple(
        context
        for context in source_contexts
        if isinstance(context, RequirementsFileDependencyContext)
    )

    consumptions: list[StaticDependencyConsumptionEvidence] = []
    invocations: list[DirectPackageInvocationEvidence] = []
    problems: list[StaticWorkflowDependencyProblem] = []
    readable_jobs: dict[str, StepsJobDefinition] = {}

    for context in requirements_contexts:
        if (
            context.revision != source.revision
            or context.normalized_package != normalized_package
        ):
            problems.append(
                StaticWorkflowDependencyProblem(
                    reason="dependency_source_context_identity_mismatch",
                    detail=(
                        "A typed requirements source context did not match the exact "
                        "workflow revision or changed normalized package under evaluation."
                    ),
                )
            )

    requirements_contexts = tuple(
        context
        for context in requirements_contexts
        if context.revision == source.revision
        and context.normalized_package == normalized_package
    )

    valid_project_sources: list[WorkflowProjectEnvironmentSource] = []
    for project_source in project_environment_sources:
        _validate_project_environment_source(
            source,
            project_source,
            normalized_package=normalized_package,
        )
        valid_project_sources.append(project_source)

    for job in definition.jobs:
        if isinstance(job, JobProblem):
            problems.append(
                StaticWorkflowDependencyProblem(
                    reason="workflow_job_unreadable",
                    detail=(
                        "A static job is structurally unresolved: "
                        f"{job.reason}: {job.detail}"
                    ),
                    job_key=job.key,
                )
            )
            continue
        if isinstance(job, ReusableWorkflowJobDefinition):
            problems.append(
                StaticWorkflowDependencyProblem(
                    reason="reusable_workflow_job_unsupported",
                    detail=(
                        "A static job delegates to a reusable workflow. Following that "
                        "separate definition is outside the current CI consumption rule."
                    ),
                    job_key=job.key,
                )
            )
            continue

        assert isinstance(job, StepsJobDefinition)
        readable_jobs[job.key] = job
        _inspect_steps_job_evidence(
            source,
            definition,
            job,
            requirements_contexts=requirements_contexts,
            project_environment_sources=tuple(valid_project_sources),
            package=package,
            normalized_package=normalized_package,
            consumptions=consumptions,
            invocations=invocations,
            collect_invocations=collect_invocations,
        )

    for project_environment_consumption in project_environment_consumptions:
        source_problem = _validate_project_environment_consumption_source(
            source,
            definition,
            readable_jobs,
            project_environment_consumption,
            normalized_package=normalized_package,
        )
        if source_problem is not None:
            problems.append(source_problem)
            continue
        consumptions.append(project_environment_consumption)

    return WorkflowStaticDependencyEvidence(
        job_count=len(definition.jobs),
        consumptions=tuple(consumptions),
        invocations=tuple(invocations),
        problems=tuple(problems),
    )


def _inspect_steps_job_evidence(
    source: RepositoryTextFile,
    definition: WorkflowDefinition,
    job: StepsJobDefinition,
    *,
    requirements_contexts: tuple[RequirementsFileDependencyContext, ...],
    project_environment_sources: tuple[WorkflowProjectEnvironmentSource, ...],
    package: str,
    normalized_package: str,
    consumptions: list[StaticDependencyConsumptionEvidence],
    invocations: list[DirectPackageInvocationEvidence],
    collect_invocations: bool,
) -> None:
    root_checkout_state: _RepositoryRootCheckoutState = "not_established"
    for entry in job.steps:
        if isinstance(entry, UsesStepDefinition):
            root_checkout_state = _advance_repository_root_checkout_state(
                source,
                entry,
                current_state=root_checkout_state,
            )
            continue
        if not isinstance(entry, RunStepDefinition):
            continue

        command_analysis = analyze_run_step_commands(definition, job, entry)

        _append_direct_requirements_consumptions(
            source,
            definition,
            job,
            entry,
            command_analysis=command_analysis,
            root_checkout_state=root_checkout_state,
            requirements_contexts=requirements_contexts,
            consumptions=consumptions,
        )
        _append_project_environment_consumptions(
            source,
            definition,
            job,
            entry,
            command_analysis=command_analysis,
            root_checkout_state=root_checkout_state,
            project_environment_sources=project_environment_sources,
            consumptions=consumptions,
        )

        if collect_invocations and root_checkout_state == "current_repository":
            invocations.extend(
                _package_invocations_from_analysis(
                    command_analysis,
                    job_key=job.key,
                    step_source_index=entry.source_index,
                    command=entry.command.text,
                    package=package,
                    normalized_package=normalized_package,
                )
            )


def _append_direct_requirements_consumptions(
    source: RepositoryTextFile,
    definition: WorkflowDefinition,
    job: StepsJobDefinition,
    entry: RunStepDefinition,
    *,
    command_analysis: StaticCommandAnalysis,
    root_checkout_state: _RepositoryRootCheckoutState,
    requirements_contexts: tuple[RequirementsFileDependencyContext, ...],
    consumptions: list[StaticDependencyConsumptionEvidence],
) -> None:
    for context in requirements_contexts:
        observation = observe_direct_installation_declaration(
            entry,
            dependency_source_path=context.source_path,
            command_analysis=command_analysis,
            workflow_defaults=definition.run_defaults,
            job_defaults=job.run_defaults,
        )
        if observation.state == "not_observed":
            continue
        if root_checkout_state == "other_repository":
            continue

        occurrence = _occurrence_for_location(
            command_analysis,
            observation.command_location,
        )
        structural_context = occurrence.structural_context if occurrence is not None else ()

        if root_checkout_state != "current_repository":
            consumptions.append(
                StaticDependencyConsumptionEvidence(
                    state="unresolved",
                    mechanism="direct_requirements",
                    normalized_package=context.normalized_package,
                    workflow_path=source.path,
                    workflow_revision=source.revision,
                    job_key=job.key,
                    step_source_index=entry.source_index,
                    command=entry.command.text,
                    reason="direct_requirements_checkout_provenance_unresolved",
                    detail=(
                        "A static direct-requirements declaration is visible or materially "
                        "unresolved, but the workflow does not statically establish the "
                        "changed repository at the GitHub workspace root before this step "
                        f"(root checkout state: {root_checkout_state})."
                    ),
                    source_path=context.source_path,
                    command_location=observation.command_location,
                    structural_context=structural_context,
                )
            )
            continue

        if observation.state == "observed":
            assert observation.command_location is not None
            assert occurrence is not None
            consumptions.append(
                StaticDependencyConsumptionEvidence(
                    state="supported",
                    mechanism="direct_requirements",
                    normalized_package=context.normalized_package,
                    workflow_path=source.path,
                    workflow_revision=source.revision,
                    job_key=job.key,
                    step_source_index=entry.source_index,
                    command=entry.command.text,
                    reason="direct_requirements_consumption_declared",
                    detail=(
                        "The static job directly declares installation from a trusted "
                        "requirements dependency source. Execution is not established."
                    ),
                    source_path=context.source_path,
                    command_location=observation.command_location,
                    structural_context=occurrence.structural_context,
                )
            )
            continue

        consumptions.append(
            StaticDependencyConsumptionEvidence(
                state="unresolved",
                mechanism="direct_requirements",
                normalized_package=context.normalized_package,
                workflow_path=source.path,
                workflow_revision=source.revision,
                job_key=job.key,
                step_source_index=entry.source_index,
                command=entry.command.text,
                reason=observation.reason,
                detail=observation.detail,
                source_path=context.source_path,
                command_location=observation.command_location,
                structural_context=structural_context,
            )
        )


def _append_project_environment_consumptions(
    source: RepositoryTextFile,
    definition: WorkflowDefinition,
    job: StepsJobDefinition,
    entry: RunStepDefinition,
    *,
    command_analysis: StaticCommandAnalysis,
    root_checkout_state: _RepositoryRootCheckoutState,
    project_environment_sources: tuple[WorkflowProjectEnvironmentSource, ...],
    consumptions: list[StaticDependencyConsumptionEvidence],
) -> None:
    for project_source in project_environment_sources:
        observation = observe_project_environment_selection(
            entry,
            project_file_path=project_source.project_file.path,
            command_analysis=command_analysis,
            workflow_defaults=definition.run_defaults,
            job_defaults=job.run_defaults,
        )
        if observation.state == "not_observed":
            continue
        if root_checkout_state == "other_repository":
            continue

        if root_checkout_state != "current_repository":
            consumptions.append(
                _preserve_unresolved_checkout_provenance(
                    source,
                    job,
                    project_source,
                    observation,
                    root_checkout_state=root_checkout_state,
                )
            )
            continue

        if isinstance(project_source.project_file, UnavailableRepositoryFile):
            consumptions.append(
                _preserve_unresolved_required_project_root_source(
                    source,
                    job,
                    project_source,
                    observation,
                )
            )
            continue

        if observation.state == "unresolved":
            consumptions.append(
                _preserve_unresolved_project_environment_selection(
                    source,
                    job,
                    project_source,
                    observation,
                )
            )
            continue

        for declaration in observation.declarations:
            context = project_source.context
            if isinstance(context, UvLockDependencyContext):
                if declaration.manager != "uv":
                    continue
                assert project_source.lock_file is not None
                dependency_evidence = evaluate_uv_selected_root_reachability(
                    context,
                    declaration,
                    lock_file=project_source.lock_file,
                )
            else:
                dependency_evidence = evaluate_project_source_environment_membership(
                    context,
                    declaration,
                )

            consumptions.append(
                compose_project_environment_consumption(
                    workflow_path=source.path,
                    workflow_revision=source.revision,
                    job_key=job.key,
                    observation=observation,
                    declaration=declaration,
                    dependency_evidence=dependency_evidence,
                )
            )


def _advance_repository_root_checkout_state(
    source: RepositoryTextFile,
    step: UsesStepDefinition,
    *,
    current_state: _RepositoryRootCheckoutState,
) -> _RepositoryRootCheckoutState:
    """Track the bounded declared owner of ``GITHUB_WORKSPACE`` root within one job."""

    if step.reference.contains_expression or not step.reference.text.casefold().startswith(
        "actions/checkout@"
    ):
        return current_state

    path_target = _checkout_path_target(step)
    if path_target == "subpath":
        return current_state
    if path_target == "unresolved" or step.condition is not None:
        return "unresolved"

    repository_value, repository_ambiguous = _static_checkout_input(step, "repository")
    if repository_ambiguous:
        return "unresolved"
    if repository_value is None:
        return "current_repository"

    repository_text = repository_value.text.strip()
    if repository_value.contains_expression:
        compact = re.sub(r"\s+", "", repository_text).casefold()
        if compact == "${{github.repository}}":
            return "current_repository"
        return "unresolved"

    if repository_text.casefold() == source.repository.casefold():
        return "current_repository"
    return "other_repository"


def _checkout_path_target(step: UsesStepDefinition) -> _CheckoutPathTarget:
    path_value, path_ambiguous = _static_checkout_input(step, "path")
    if path_ambiguous:
        return "unresolved"
    if path_value is None:
        return "root"
    if path_value.contains_expression:
        return "unresolved"

    raw_path = path_value.text.strip()
    normalized = posixpath.normpath(raw_path or ".")
    if normalized == ".":
        return "root"
    if normalized.startswith("/") or normalized == ".." or normalized.startswith("../"):
        return "unresolved"
    return "subpath"


def _static_checkout_input(
    step: UsesStepDefinition,
    name: str,
) -> tuple[StaticScalarValue | None, bool]:
    if step.with_inputs is None:
        return None, False

    matches = tuple(
        entry.value
        for entry in step.with_inputs.entries
        if entry.key.text == name
    )
    if not matches:
        return None, False
    if len(matches) != 1 or not isinstance(matches[0], StaticScalarValue):
        return None, True
    return matches[0], False


def _project_environment_observation_identity(
    observation: ProjectEnvironmentSelectionObservation,
) -> tuple[StaticCommandLocation | None, tuple[StaticCommandStructure, ...]]:
    identities = tuple(
        (declaration.command_location, declaration.structural_context)
        for declaration in observation.declarations
        if declaration.command_location is not None
    )
    unique = tuple(dict.fromkeys(identities))
    if len(unique) == 1:
        return unique[0]
    return None, ()


def _preserve_unresolved_checkout_provenance(
    source: RepositoryTextFile,
    job: StepsJobDefinition,
    project_source: WorkflowProjectEnvironmentSource,
    observation: ProjectEnvironmentSelectionObservation,
    *,
    root_checkout_state: _RepositoryRootCheckoutState,
) -> StaticDependencyConsumptionEvidence:
    location, structural_context = _project_environment_observation_identity(observation)
    context = project_source.context
    return StaticDependencyConsumptionEvidence(
        state="unresolved",
        mechanism="project_environment",
        normalized_package=context.normalized_package,
        workflow_path=source.path,
        workflow_revision=source.revision,
        job_key=job.key,
        step_source_index=observation.step_source_index,
        command=observation.command,
        reason="project_environment_checkout_provenance_unresolved",
        detail=(
            "A static project-selection command is visible, but the workflow does not "
            "statically establish the changed repository at the GitHub workspace root "
            f"before this step (root checkout state: {root_checkout_state})."
        ),
        source_path=context.source_path,
        command_location=location,
        structural_context=structural_context,
    )


def _preserve_unresolved_project_environment_selection(
    source: RepositoryTextFile,
    job: StepsJobDefinition,
    project_source: WorkflowProjectEnvironmentSource,
    observation: ProjectEnvironmentSelectionObservation,
) -> StaticDependencyConsumptionEvidence:
    if observation.state != "unresolved":
        raise ValueError(
            "unresolved project-selection preservation requires unresolved R3 evidence"
        )

    location, structural_context = _project_environment_observation_identity(observation)
    context = project_source.context
    return StaticDependencyConsumptionEvidence(
        state="unresolved",
        mechanism="project_environment",
        normalized_package=context.normalized_package,
        workflow_path=source.path,
        workflow_revision=source.revision,
        job_key=job.key,
        step_source_index=observation.step_source_index,
        command=observation.command,
        reason=observation.reason,
        detail=observation.detail,
        source_path=context.source_path,
        command_location=location,
        structural_context=structural_context,
    )


def _preserve_unresolved_required_project_root_source(
    source: RepositoryTextFile,
    job: StepsJobDefinition,
    project_source: WorkflowProjectEnvironmentSource,
    observation: ProjectEnvironmentSelectionObservation,
) -> StaticDependencyConsumptionEvidence:
    project_file = project_source.project_file
    if not isinstance(project_file, UnavailableRepositoryFile):
        raise ValueError(
            "required project-root source preservation requires unavailable file evidence"
        )

    location, structural_context = _project_environment_observation_identity(observation)
    context = project_source.context
    return StaticDependencyConsumptionEvidence(
        state="unresolved",
        mechanism="project_environment",
        normalized_package=context.normalized_package,
        workflow_path=source.path,
        workflow_revision=source.revision,
        job_key=job.key,
        step_source_index=observation.step_source_index,
        command=observation.command,
        reason="required_project_root_source_unavailable",
        detail=(
            f"Required project-root source {project_file.path!r} is unavailable "
            f"({project_file.reason}): {project_file.detail} Dependency reachability or "
            "project-source membership was not evaluated."
        ),
        source_path=context.source_path,
        command_location=location,
        structural_context=structural_context,
    )


def _validate_project_environment_source(
    workflow_source: RepositoryTextFile,
    project_source: WorkflowProjectEnvironmentSource,
    *,
    normalized_package: str,
) -> None:
    context = project_source.context
    if (
        context.repository != workflow_source.repository
        or context.revision != workflow_source.revision
        or context.normalized_package != normalized_package
    ):
        raise ValueError(
            "project-environment source context does not match workflow/package identity"
        )

    if (
        project_source.project_file.repository != context.repository
        or project_source.project_file.revision != context.revision
    ):
        raise ValueError("project file does not match dependency context repository/revision")

    if isinstance(context, UvLockDependencyContext):
        expected_project_path = _uv_project_file_path(context.source_path)
        if project_source.project_file.path != expected_project_path:
            raise ValueError(
                "uv project file is not the sibling project root of the changed lock"
            )
        if project_source.lock_file is None:
            raise ValueError("uv project-environment source requires exact lock evidence")
        if (
            project_source.lock_file.repository != context.repository
            or project_source.lock_file.revision != context.revision
            or project_source.lock_file.path != context.source_path
        ):
            raise ValueError("uv lock evidence does not match the dependency source context")
        return

    if project_source.project_file.path != context.source_path:
        raise ValueError(
            "project-source environment evidence must use its exact pyproject path"
        )
    if project_source.lock_file is not None:
        raise ValueError(
            "project-source environment evidence must not carry uv lock evidence"
        )


def _uv_project_file_path(lock_path: str) -> str:
    lock_root = posixpath.dirname(lock_path)
    return f"{lock_root}/pyproject.toml" if lock_root else "pyproject.toml"


def _validate_project_environment_consumption_source(
    source: RepositoryTextFile,
    definition: WorkflowDefinition,
    readable_jobs: dict[str, StepsJobDefinition],
    evidence: StaticDependencyConsumptionEvidence,
    *,
    normalized_package: str,
) -> StaticWorkflowDependencyProblem | None:
    """Validate focused precomposed project evidence against canonical parsed identity."""

    if evidence.normalized_package != normalized_package:
        return StaticWorkflowDependencyProblem(
            reason="project_environment_consumption_package_identity_mismatch",
            detail=(
                "Supplied project-environment consumption was established for a "
                "different normalized package than the dependency under evaluation."
            ),
            job_key=evidence.job_key,
        )
    if (
        evidence.workflow_path != source.path
        or evidence.workflow_revision != source.revision
    ):
        return StaticWorkflowDependencyProblem(
            reason="project_environment_consumption_workflow_identity_mismatch",
            detail=(
                "Supplied project-environment consumption was composed for a different "
                "workflow path or revision."
            ),
            job_key=evidence.job_key,
        )

    job = readable_jobs.get(evidence.job_key)
    if job is None:
        return StaticWorkflowDependencyProblem(
            reason="project_environment_consumption_job_unresolved",
            detail=(
                "A supplied project-environment consumption refers to a static job "
                f"{evidence.job_key!r} that is not a readable local steps job in this "
                "exact workflow definition."
            ),
            job_key=evidence.job_key,
        )

    matching_step = next(
        (
            step
            for step in job.steps
            if isinstance(step, RunStepDefinition)
            and step.source_index == evidence.step_source_index
        ),
        None,
    )
    if matching_step is None or matching_step.command.text != evidence.command:
        return StaticWorkflowDependencyProblem(
            reason="project_environment_consumption_step_identity_mismatch",
            detail=(
                "Supplied project-environment consumption does not match the exact run "
                "step source index/command in the referenced static job."
            ),
            job_key=evidence.job_key,
        )

    if evidence.command_location is None:
        return StaticWorkflowDependencyProblem(
            reason="project_environment_consumption_command_identity_mismatch",
            detail=(
                "Supplied project-environment consumption does not retain canonical parsed "
                "command identity."
            ),
            job_key=evidence.job_key,
        )

    analysis = analyze_run_step_commands(definition, job, matching_step)
    occurrence = _occurrence_for_location(analysis, evidence.command_location)
    if occurrence is None or occurrence.structural_context != evidence.structural_context:
        return StaticWorkflowDependencyProblem(
            reason="project_environment_consumption_command_identity_mismatch",
            detail=(
                "Supplied project-environment consumption does not match one exact parsed "
                "command occurrence and structural context in the referenced step."
            ),
            job_key=evidence.job_key,
        )
    return None


def _occurrence_for_location(
    analysis: StaticCommandAnalysis,
    location: StaticCommandLocation | None,
) -> StaticCommandOccurrence | None:
    if location is None:
        return None
    return next(
        (
            occurrence
            for occurrence in analysis.command_occurrences
            if StaticCommandLocation.from_occurrence(occurrence) == location
        ),
        None,
    )


def _package_invocations_from_analysis(
    analysis: StaticCommandAnalysis,
    *,
    job_key: str,
    step_source_index: int,
    command: str,
    package: str,
    normalized_package: str,
) -> tuple[DirectPackageInvocationEvidence, ...]:
    if analysis.state != "analyzable":
        return ()

    candidates = {
        candidate.casefold()
        for candidate in (package, normalized_package)
        if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", candidate)
    }
    if not candidates:
        return ()

    evidence: list[DirectPackageInvocationEvidence] = []
    for occurrence in analysis.command_occurrences:
        state = _package_invocation_state(occurrence, candidates)
        if state is None:
            continue

        location = StaticCommandLocation.from_occurrence(occurrence)
        if state == "observed":
            evidence.append(
                DirectPackageInvocationEvidence(
                    state="observed",
                    job_key=job_key,
                    step_source_index=step_source_index,
                    command=command,
                    reason="direct_package_invocation_observed",
                    detail=(
                        "A real parsed static command occurrence directly invokes the "
                        "changed package through an admitted command shape."
                    ),
                    command_location=location,
                    structural_context=occurrence.structural_context,
                )
            )
        else:
            evidence.append(
                DirectPackageInvocationEvidence(
                    state="unresolved",
                    job_key=job_key,
                    step_source_index=step_source_index,
                    command=command,
                    reason="direct_package_invocation_target_unresolved",
                    detail=(
                        "An admitted direct-invocation wrapper/prefix is visible, but a "
                        "material prefix or package-target atom is dynamic or unsupported."
                    ),
                    command_location=location,
                    structural_context=occurrence.structural_context,
                )
            )
    return tuple(evidence)


def _package_invocation_state(
    occurrence: StaticCommandOccurrence,
    candidates: set[str],
) -> DirectPackageInvocationState | None:
    executable = _literal_casefold(occurrence.executable)
    if executable is None:
        return None

    if executable in candidates:
        return "observed"

    arguments = occurrence.arguments
    if executable in {"python", "python3"}:
        return _prefixed_target_state(arguments, prefix=("-m",), candidates=candidates)
    if executable in {"uv", "poetry", "pipenv"}:
        return _prefixed_target_state(arguments, prefix=("run",), candidates=candidates)
    if executable == "coverage":
        return _prefixed_target_state(
            arguments,
            prefix=("run", "-m"),
            candidates=candidates,
        )
    return None


def _prefixed_target_state(
    arguments: tuple[StaticCommandAtom, ...],
    *,
    prefix: tuple[str, ...],
    candidates: set[str],
) -> DirectPackageInvocationState | None:
    if not arguments:
        return None

    for index, expected in enumerate(prefix):
        if index >= len(arguments):
            return None
        value = _literal_casefold(arguments[index])
        if value is None:
            return "unresolved"
        if value != expected:
            return None

    target_index = len(prefix)
    if target_index >= len(arguments):
        return None
    target = _literal_casefold(arguments[target_index])
    if target is None:
        return "unresolved"
    if target in candidates:
        return "observed"
    return None


def _literal_casefold(atom: StaticCommandAtom) -> str | None:
    if atom.state != "literal" or atom.literal_value is None:
        return None
    return atom.literal_value.casefold()


__all__ = (
    "DirectPackageInvocationEvidence",
    "DirectPackageInvocationState",
    "StaticWorkflowDependencyProblem",
    "WorkflowProjectEnvironmentSource",
    "WorkflowStaticDependencyEvidence",
    "derive_project_environment_consumptions",
    "inspect_workflow_dependency_evidence",
)
