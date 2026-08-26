"""Interpret bounded static CI dependency consumption and direct package invocation.

GitHub Actions YAML structure is owned by ``upgradepilot.github.workflow_definition``.
Dependency-source install semantics are owned by ``upgradepilot.dependency.direct_install``.
This CI module owns workflow-level composition: preserve static consumption locations,
direct changed-package invocation locations, source ordering within one static job, and the
bounded R3 -> dependency-domain -> R5 composition for exact readable run steps.

``derive_project_environment_consumptions`` is the R6 production seam for project-selection
commands. It does not choose a preferred command. Every readable run step is considered;
commands become positive only when their own selected roots/environment evidence supports the
changed dependency. Multiple supported commands are therefore retained independently.
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


@dataclass(frozen=True, slots=True)
class DirectPackageInvocationEvidence:
    """One static direct invocation of the changed package.

    This is source-location evidence only. It does not establish that the invocation ran
    or succeeded, and it becomes CI direct-exercise support only when ordered after a
    supported consumption in the same static job.
    """

    job_key: str
    step_source_index: int
    segment_index: int
    command: str


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

    The workflow is the exact admitted PR-head definition supplied by the GitHub provider.
    No selector, group, declaration, reachability result, or consumption is supplied by the
    caller. Each command is interpreted independently. A positive result from one command
    does not suppress other positive, negative-ish, or unresolved command results.

    R3 binds a command to a repository-relative project path; that binding is sound only when
    the workflow has statically established the changed repository at the GitHub workspace
    root before the command. R6 therefore tracks bounded ``actions/checkout`` provenance while
    walking each job. A root checkout of another repository prevents its later root commands
    from being rebound to the changed repository's project/lock evidence. Ambiguous or missing
    root provenance is preserved as unresolved evidence when a plausible project selector is
    visible, rather than being strengthened through R4/R5 or disappearing into negative-ish
    absence.

    Material R3 uncertainty is also preserved as unresolved CI-consumption evidence rather
    than being erased before coverage classification. ``not_observed`` still means this seam
    has no project-environment fact to contribute. When R3 locates a relevant selector using
    the required project's exact path but that project-root source is unavailable, R6 stops
    before dependency reachability/membership and preserves the source failure as unresolved.
    An unavailable uv lock can still reach R4 once project/root provenance is admitted, where
    it becomes explicit ``unresolved`` evidence.
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

                # An exact root checkout of another repository is positive evidence that a
                # root-relative project command belongs to that repository, not to the
                # changed repository. Do not manufacture current-repository CI evidence.
                if root_checkout_state == "other_repository":
                    continue

                # If root ownership is absent or ambiguous, the command may be relevant but
                # cannot soundly be bound to the current repository's project/lock evidence.
                # Preserve that uncertainty before any R4/R5 composition.
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

    R3 owns whether the project selection is readable. When that proposition is unresolved,
    there is no sound declaration to strengthen through reachability or membership. CI still
    needs to retain the uncertainty so coverage cannot later reinterpret absence of a derived
    item as ``not_established``. R3 currently reports this uncertainty at run-step scope; when
    it preserved declarations we use their first segment location, otherwise segment zero is
    the same conservative step-local placeholder already used for unresolved direct-install
    observations.
    """

    if observation.state != "unresolved":
        raise ValueError("unresolved project-selection preservation requires unresolved R3 evidence")

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
    """Preserve a relevant selector when its required project-root source is unavailable.

    Typed unavailability still supplies the exact repository-relative path needed to locate
    a static selector, but it does not establish an admitted project root. R6 therefore stops
    before reachability or project-source membership and carries the provider failure into CI
    coverage as unresolved evidence rather than letting absence become ``not_established``.
    """

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
            raise ValueError("uv project file is not the sibling project root of the changed lock")
        if project_source.lock_file is None:
            raise ValueError("uv project-environment source requires exact lock evidence")
        return

    if project_source.project_file.path != context.source_path:
        raise ValueError("project-source environment evidence must use its exact pyproject path")
    if project_source.lock_file is not None:
        raise ValueError("project-source environment evidence must not carry uv lock evidence")


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

    Requirements consumption is derived only from typed
    ``RequirementsFileDependencyContext`` values. Constraints, uv-lock, and pyproject
    source paths are never promoted into direct pip install evidence merely because they
    are files. Repository-relative requirements/invocation evidence is additionally bound
    to statically established current-repository workspace-root ownership, so commands from
    an explicitly checked-out different repository cannot be rebound to the changed source.
    Project-environment consumption arrives as typed R5 evidence and is rebound to this exact
    package/workflow/revision/job/step before acceptance.
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
    """Require project-environment composition to point back to this exact static step."""

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

    segments = _shell_segments(evidence.command)
    if evidence.segment_index < 0 or evidence.segment_index >= len(segments):
        return StaticWorkflowDependencyProblem(
            reason="project_environment_consumption_segment_identity_mismatch",
            detail=(
                "Supplied project-environment consumption references a command segment "
                "outside the bounded static command segmentation."
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

        for context in requirements_contexts:
            observation = observe_direct_installation_declaration(
                entry,
                dependency_source_path=context.source_path,
                workflow_defaults=definition.run_defaults,
                job_defaults=job.run_defaults,
            )
            if observation.state == "not_observed":
                continue

            if root_checkout_state == "other_repository":
                continue

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
                        segment_index=(
                            observation.matched_segment_index
                            if observation.matched_segment_index is not None
                            else 0
                        ),
                        command=entry.command.text,
                        reason="direct_requirements_checkout_provenance_unresolved",
                        detail=(
                            "A static direct-requirements declaration is visible, but the "
                            "workflow does not statically establish the changed repository "
                            "at the GitHub workspace root before this step "
                            f"(root checkout state: {root_checkout_state})."
                        ),
                        source_path=context.source_path,
                    )
                )
                continue

            if observation.state == "observed":
                assert observation.matched_segment_index is not None
                consumptions.append(
                    StaticDependencyConsumptionEvidence(
                        state="supported",
                        mechanism="direct_requirements",
                        normalized_package=context.normalized_package,
                        workflow_path=source.path,
                        workflow_revision=source.revision,
                        job_key=job.key,
                        step_source_index=entry.source_index,
                        segment_index=observation.matched_segment_index,
                        command=entry.command.text,
                        reason="direct_requirements_consumption_declared",
                        detail=(
                            "The static job directly declares installation from a trusted "
                            "requirements dependency source. Execution is not established."
                        ),
                        source_path=context.source_path,
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
                        segment_index=0,
                        command=entry.command.text,
                        reason=observation.reason,
                        detail=observation.detail,
                        source_path=context.source_path,
                    )
                )

        invocation_segment = _first_package_invocation_segment_index(
            entry.command.text,
            package,
            normalized_package,
        )
        if invocation_segment is not None and root_checkout_state == "current_repository":
            invocations.append(
                DirectPackageInvocationEvidence(
                    job_key=job.key,
                    step_source_index=entry.source_index,
                    segment_index=invocation_segment,
                    command=entry.command.text,
                )
            )


def _first_package_invocation_segment_index(
    command: str,
    package: str,
    normalized_package: str,
) -> int | None:
    """Return the first admitted static segment that directly invokes the package."""

    candidates = {
        candidate.lower()
        for candidate in (package, normalized_package)
        if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", candidate)
    }
    prefixes = (
        "",
        "python -m ",
        "python3 -m ",
        "uv run ",
        "poetry run ",
        "pipenv run ",
        "coverage run -m ",
    )

    for segment_index, raw_segment in enumerate(_shell_segments(command)):
        segment = re.sub(
            r"^(?:[A-Za-z_][A-Za-z0-9_]*=[^\s]+\s+)+",
            "",
            raw_segment.strip(),
        )
        for candidate in candidates:
            for prefix in prefixes:
                expected = f"{prefix}{candidate}"
                if re.match(
                    rf"^{re.escape(expected)}(?=\s|$)",
                    segment,
                    re.IGNORECASE,
                ):
                    return segment_index
    return None


def _shell_segments(command: str) -> tuple[str, ...]:
    """Split only the simple separators admitted by the current CI command rule."""

    return tuple(
        segment.strip()
        for segment in re.split(r"(?:&&|\|\||;|\n)", command)
        if segment.strip()
    )


__all__ = (
    "DirectPackageInvocationEvidence",
    "StaticWorkflowDependencyProblem",
    "WorkflowProjectEnvironmentSource",
    "WorkflowStaticDependencyEvidence",
    "derive_project_environment_consumptions",
    "inspect_workflow_dependency_evidence",
)
