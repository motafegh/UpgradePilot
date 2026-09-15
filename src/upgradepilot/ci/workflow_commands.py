"""Interpret bounded static CI dependency consumption and direct package invocation.

GitHub Actions YAML structure is owned by ``upgradepilot.github.workflow_definition``.
Shared shell parsing and parser-neutral command occurrences are owned by
``upgradepilot.github.workflow_command_analysis``. Dependency-source install semantics are
owned by ``upgradepilot.dependency.direct_install``. This CI module owns workflow traversal,
checkout provenance, direct changed-package invocation meaning, and cross-evidence composition.

Cycle 2 is migrating consumers incrementally. Direct-requirements and direct-package
invocation now consume the same ``StaticCommandAnalysis`` produced once per run step in the
normal workflow evidence pass. Project-environment selection remains on its legacy command
segmentation contract until the next bounded migration slice.
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
    """One parsed static candidate for direct invocation of the changed package.

    ``observed`` means the admitted direct/wrapper shape and package identity are literal in
    one real parsed command occurrence. ``unresolved`` means an admitted wrapper/prefix is
    visible but a material target/prefix atom is dynamic or unsupported.

    ``command_location`` and ``structural_context`` are static source facts only. They do not
    establish execution or success. ``segment_index`` is retained only as a temporary
    compatibility surface for callers/tests while Cycle 2 finishes; parser-backed invocation
    evidence leaves it unset.
    """

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
    segment_index: int | None = None


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
    """Exact sources needed to derive project-environment consumption for one context.

    ``project_file`` supplies the exact project-root locator consumed by R3. For a
    pyproject-owned dependency context it is the dependency source itself. For a uv-lock
    context it is the exact sibling ``pyproject.toml`` at the lock/workspace root; R4 does
    not parse that file's content. Typed project-file unavailability is retained so R6 can
    preserve a relevant selector as unresolved instead of erasing the missing required
    source. ``lock_file`` is required only for uv reachability and may likewise preserve
    typed unavailability so R4 can remain conservative.
    """

    context: ProjectSourceEnvironmentContext | UvLockDependencyContext
    project_file: RepositoryFileEvidence
    lock_file: RepositoryFileEvidence | None = None


def derive_project_environment_consumptions(
    source: RepositoryTextFile,
    *,
    sources: Sequence[WorkflowProjectEnvironmentSource],
    normalized_package: str,
) -> tuple[StaticDependencyConsumptionEvidence, ...]:
    """Derive R3 -> dependency-domain -> R5 evidence from every readable run step.

    This is still the pre-migration project-environment seam. It remains behaviorally stable
    during the direct-requirements/direct-invocation slice and is the next Cycle 2 migration
    target.
    """

    if not normalized_package:
        raise ValueError("project-environment derivation requires normalized package identity")

    for project_source in sources:
        _validate_project_environment_source(
            source,
            project_source,
            normalized_package=normalized_package,
        )

    definition = parse_workflow_definition(source)
    if isinstance(definition, WorkflowDefinitionProblem):
        return ()

    assert isinstance(definition, WorkflowDefinition)
    consumptions: list[StaticDependencyConsumptionEvidence] = []

    for job in definition.jobs:
        if not isinstance(job, StepsJobDefinition):
            continue

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

            for project_source in sources:
                observation = observe_project_environment_selection(
                    entry,
                    project_file_path=project_source.project_file.path,
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

                if isinstance(
                    project_source.project_file,
                    UnavailableRepositoryFile,
                ):
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

    return tuple(consumptions)


def _advance_repository_root_checkout_state(
    source: RepositoryTextFile,
    step: UsesStepDefinition,
    *,
    current_state: _RepositoryRootCheckoutState,
) -> _RepositoryRootCheckoutState:
    """Track the bounded declared owner of ``GITHUB_WORKSPACE`` root within one job.

    This is deliberately not a checkout simulator. It consumes only explicit static
    ``actions/checkout`` declarations already preserved by the workflow provider IR. A
    literal checkout into a subpath cannot replace workspace-root ownership and therefore
    leaves the current root state unchanged. A dynamic path can target root, so it makes root
    provenance unresolved. Conditional root checkout is likewise unresolved because the
    bounded static rule cannot establish that the rebinding occurs.
    """

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
    """Classify whether one checkout declaration can replace workspace-root ownership."""

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
    """Return one unique scalar checkout input and whether its shape is ambiguous."""

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


def _preserve_unresolved_checkout_provenance(
    source: RepositoryTextFile,
    job: StepsJobDefinition,
    project_source: WorkflowProjectEnvironmentSource,
    observation: ProjectEnvironmentSelectionObservation,
    *,
    root_checkout_state: _RepositoryRootCheckoutState,
) -> StaticDependencyConsumptionEvidence:
    """Preserve a plausible selector when current-repository root ownership is unproven."""

    segment_index = (
        observation.declarations[0].segment_index if observation.declarations else 0
    )
    context = project_source.context
    return StaticDependencyConsumptionEvidence(
        state="unresolved",
        mechanism="project_environment",
        normalized_package=context.normalized_package,
        workflow_path=source.path,
        workflow_revision=source.revision,
        job_key=job.key,
        step_source_index=observation.step_source_index,
        segment_index=segment_index,
        command=observation.command,
        reason="project_environment_checkout_provenance_unresolved",
        detail=(
            "A static project-selection command is visible, but the workflow does not "
            "statically establish the changed repository at the GitHub workspace root "
            f"before this step (root checkout state: {root_checkout_state})."
        ),
        source_path=context.source_path,
    )


def _preserve_unresolved_project_environment_selection(
    source: RepositoryTextFile,
    job: StepsJobDefinition,
    project_source: WorkflowProjectEnvironmentSource,
    observation: ProjectEnvironmentSelectionObservation,
) -> StaticDependencyConsumptionEvidence:
    """Carry material R3 command uncertainty forward without invoking R4/R5 semantics.

    The project-environment path still owns its legacy segment placeholder during this
    intermediate slice. That placeholder is not reused by migrated direct-requirements
    evidence and will be removed when this path moves onto shared command analysis.
    """

    if observation.state != "unresolved":
        raise ValueError(
            "unresolved project-selection preservation requires unresolved R3 evidence"
        )

    segment_index = (
        observation.declarations[0].segment_index if observation.declarations else 0
    )
    context = project_source.context
    return StaticDependencyConsumptionEvidence(
        state="unresolved",
        mechanism="project_environment",
        normalized_package=context.normalized_package,
        workflow_path=source.path,
        workflow_revision=source.revision,
        job_key=job.key,
        step_source_index=observation.step_source_index,
        segment_index=segment_index,
        command=observation.command,
        reason=observation.reason,
        detail=observation.detail,
        source_path=context.source_path,
    )


def _preserve_unresolved_required_project_root_source(
    source: RepositoryTextFile,
    job: StepsJobDefinition,
    project_source: WorkflowProjectEnvironmentSource,
    observation: ProjectEnvironmentSelectionObservation,
) -> StaticDependencyConsumptionEvidence:
    """Preserve a relevant selector when its required project-root source is unavailable."""

    project_file = project_source.project_file
    if not isinstance(project_file, UnavailableRepositoryFile):
        raise ValueError(
            "required project-root source preservation requires unavailable file evidence"
        )

    segment_index = (
        observation.declarations[0].segment_index if observation.declarations else 0
    )
    context = project_source.context
    return StaticDependencyConsumptionEvidence(
        state="unresolved",
        mechanism="project_environment",
        normalized_package=context.normalized_package,
        workflow_path=source.path,
        workflow_revision=source.revision,
        job_key=job.key,
        step_source_index=observation.step_source_index,
        segment_index=segment_index,
        command=observation.command,
        reason="required_project_root_source_unavailable",
        detail=(
            f"Required project-root source {project_file.path!r} is unavailable "
            f"({project_file.reason}): {project_file.detail} Dependency reachability or "
            "project-source membership was not evaluated."
        ),
        source_path=context.source_path,
    )


def _validate_project_environment_source(
    workflow_source: RepositoryTextFile,
    project_source: WorkflowProjectEnvironmentSource,
    *,
    normalized_package: str,
) -> None:
    """Protect the exact cross-branch identity relation used by R6 composition."""

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
    """Return the uv workspace-root pyproject path paired with one normalized uv.lock path."""

    lock_root = posixpath.dirname(lock_path)
    return f"{lock_root}/pyproject.toml" if lock_root else "pyproject.toml"


def inspect_workflow_dependency_evidence(
    source: RepositoryTextFile,
    *,
    source_contexts: Sequence[DependencySourceContext],
    package: str,
    normalized_package: str,
    project_environment_consumptions: Sequence[StaticDependencyConsumptionEvidence] = (),
) -> WorkflowStaticDependencyEvidence:
    """Preserve static consumption/invocation evidence across all readable steps jobs.

    Direct-requirements and direct-package invocation now share one parser-backed command
    analysis per run step. Project-environment consumption is still supplied by the
    separately composed legacy path and is rebound to this exact workflow/job/step before
    acceptance.
    """

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
            package=package,
            normalized_package=normalized_package,
            consumptions=consumptions,
            invocations=invocations,
        )

    for project_environment_consumption in project_environment_consumptions:
        source_problem = _validate_project_environment_consumption_source(
            source,
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


def _validate_project_environment_consumption_source(
    source: RepositoryTextFile,
    readable_jobs: dict[str, StepsJobDefinition],
    evidence: StaticDependencyConsumptionEvidence,
    *,
    normalized_package: str,
) -> StaticWorkflowDependencyProblem | None:
    """Require legacy project-environment composition to point to this exact static step."""

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

    if evidence.segment_index is None:
        return StaticWorkflowDependencyProblem(
            reason="project_environment_consumption_segment_identity_mismatch",
            detail=(
                "Legacy project-environment consumption did not retain its temporary "
                "segment identity."
            ),
            job_key=evidence.job_key,
        )
    segments = _legacy_project_environment_shell_segments(evidence.command)
    if evidence.segment_index < 0 or evidence.segment_index >= len(segments):
        return StaticWorkflowDependencyProblem(
            reason="project_environment_consumption_segment_identity_mismatch",
            detail=(
                "Supplied project-environment consumption references a command segment "
                "outside the temporary bounded project-environment segmentation."
            ),
            job_key=evidence.job_key,
        )
    return None


def _inspect_steps_job_evidence(
    source: RepositoryTextFile,
    definition: WorkflowDefinition,
    job: StepsJobDefinition,
    *,
    requirements_contexts: tuple[RequirementsFileDependencyContext, ...],
    package: str,
    normalized_package: str,
    consumptions: list[StaticDependencyConsumptionEvidence],
    invocations: list[DirectPackageInvocationEvidence],
) -> None:
    """Collect typed static premises from one local steps job without aggregating them."""

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
            structural_context = (
                occurrence.structural_context if occurrence is not None else ()
            )

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
                        segment_index=None,
                        command=entry.command.text,
                        reason="direct_requirements_checkout_provenance_unresolved",
                        detail=(
                            "A static direct-requirements declaration is visible or "
                            "materially unresolved, but the workflow does not statically "
                            "establish the changed repository at the GitHub workspace root "
                            "before this step "
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
                        segment_index=None,
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
            else:
                consumptions.append(
                    StaticDependencyConsumptionEvidence(
                        state="unresolved",
                        mechanism="direct_requirements",
                        normalized_package=context.normalized_package,
                        workflow_path=source.path,
                        workflow_revision=source.revision,
                        job_key=job.key,
                        step_source_index=entry.source_index,
                        segment_index=None,
                        command=entry.command.text,
                        reason=observation.reason,
                        detail=observation.detail,
                        source_path=context.source_path,
                        command_location=observation.command_location,
                        structural_context=structural_context,
                    )
                )

        if root_checkout_state == "current_repository":
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
    """Interpret direct changed-package invocation from real parsed occurrences only."""

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
        return _prefixed_target_state(
            arguments,
            prefix=("-m",),
            candidates=candidates,
        )
    if executable in {"uv", "poetry", "pipenv"}:
        return _prefixed_target_state(
            arguments,
            prefix=("run",),
            candidates=candidates,
        )
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


def _legacy_project_environment_shell_segments(command: str) -> tuple[str, ...]:
    """Temporary segment splitter retained only for unmigrated project-environment evidence."""

    return tuple(
        segment.strip()
        for segment in re.split(r"(?:&&|\|\||;|\n)", command)
        if segment.strip()
    )


__all__ = (
    "DirectPackageInvocationEvidence",
    "DirectPackageInvocationState",
    "StaticWorkflowDependencyProblem",
    "WorkflowProjectEnvironmentSource",
    "WorkflowStaticDependencyEvidence",
    "derive_project_environment_consumptions",
    "inspect_workflow_dependency_evidence",
)
