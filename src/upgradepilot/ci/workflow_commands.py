"""Interpret bounded static CI dependency consumption and direct package invocation.

GitHub Actions YAML structure is owned by ``upgradepilot.github.workflow_definition``.
Dependency-source install semantics are owned by ``upgradepilot.dependency.direct_install``.
This CI module owns only workflow-level composition: preserve static consumption
locations, direct changed-package invocation locations, and source ordering within one
static job.

The legacy ``inspect_workflow_commands`` function remains temporarily for the ordinary
application path until Cluster 6 migrates it. New Cluster-5 code uses
``inspect_workflow_dependency_evidence`` and does not require a one-job workflow.
"""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from ..dependency.direct_install import (
    DirectInstallDeclarationObservation,
    observe_direct_installation_declaration,
)
from ..dependency.environment import (
    DependencySourceContext,
    RequirementsFileDependencyContext,
)
from ..github.repository import RepositoryTextFile
from ..github.workflow_definition import (
    JobProblem,
    ReusableWorkflowJobDefinition,
    RunStepDefinition,
    StepsJobDefinition,
    WorkflowDefinition,
    WorkflowDefinitionProblem,
    parse_workflow_definition,
)
from .consumption import StaticDependencyConsumptionEvidence


type WorkflowCommandStatus = Literal["supported", "unresolved"]


@dataclass(frozen=True, slots=True)
class WorkflowCommandEvidence:
    """Legacy combined install→invocation evidence retained through Cluster 5."""

    status: WorkflowCommandStatus
    reason: str
    detail: str
    job_count: int
    job_key: str | None = None
    install_command: str | None = None
    execution_command: str | None = None
    install_step_source_index: int | None = None
    execution_step_source_index: int | None = None


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


def inspect_workflow_dependency_evidence(
    source: RepositoryTextFile,
    *,
    source_contexts: Sequence[DependencySourceContext],
    package: str,
    normalized_package: str,
    external_consumptions: Sequence[StaticDependencyConsumptionEvidence] = (),
) -> WorkflowStaticDependencyEvidence:
    """Preserve static consumption/invocation evidence across all readable steps jobs.

    Requirements consumption is derived only from typed
    ``RequirementsFileDependencyContext`` values. Constraints, uv-lock, and pyproject
    source paths are never promoted into direct pip install evidence merely because they
    are files. Project-environment consumption must arrive as already-composed typed CI
    evidence and is rebound to this exact package/workflow/revision/job/step before
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

    for external in external_consumptions:
        source_problem = _validate_external_consumption_source(
            source,
            readable_jobs,
            external,
            normalized_package=normalized_package,
        )
        if source_problem is not None:
            problems.append(source_problem)
            continue
        consumptions.append(external)

    return WorkflowStaticDependencyEvidence(
        job_count=len(definition.jobs),
        consumptions=tuple(consumptions),
        invocations=tuple(invocations),
        problems=tuple(problems),
    )


def _validate_external_consumption_source(
    source: RepositoryTextFile,
    readable_jobs: dict[str, StepsJobDefinition],
    evidence: StaticDependencyConsumptionEvidence,
    *,
    normalized_package: str,
) -> StaticWorkflowDependencyProblem | None:
    """Require external dependency composition to point back to this exact static step."""

    if evidence.normalized_package != normalized_package:
        return StaticWorkflowDependencyProblem(
            reason="external_consumption_package_identity_mismatch",
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
            reason="external_consumption_workflow_identity_mismatch",
            detail=(
                "Supplied project-environment consumption was composed for a different "
                "workflow path or revision."
            ),
            job_key=evidence.job_key,
        )

    job = readable_jobs.get(evidence.job_key)
    if job is None:
        return StaticWorkflowDependencyProblem(
            reason="external_consumption_job_unresolved",
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
            reason="external_consumption_step_identity_mismatch",
            detail=(
                "Supplied project-environment consumption does not match the exact run "
                "step source index/command in the referenced static job."
            ),
            job_key=evidence.job_key,
        )

    segments = _shell_segments(evidence.command)
    if evidence.segment_index < 0 or evidence.segment_index >= len(segments):
        return StaticWorkflowDependencyProblem(
            reason="external_consumption_segment_identity_mismatch",
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

    for entry in job.steps:
        if not isinstance(entry, RunStepDefinition):
            continue

        for context in requirements_contexts:
            observation = observe_direct_installation_declaration(
                entry,
                dependency_source_path=context.source_path,
                workflow_defaults=definition.run_defaults,
                job_defaults=job.run_defaults,
            )
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
            elif observation.state == "unresolved":
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
        if invocation_segment is not None:
            invocations.append(
                DirectPackageInvocationEvidence(
                    job_key=job.key,
                    step_source_index=entry.source_index,
                    segment_index=invocation_segment,
                    command=entry.command.text,
                )
            )


def inspect_workflow_commands(
    source: RepositoryTextFile,
    *,
    source_file: str,
    package: str,
    normalized_package: str,
) -> WorkflowCommandEvidence:
    """Read the legacy one-job direct install→package-invocation path.

    Retained only so Cluster 5 does not force ordinary application/CLI migration before
    Cluster 6. The proof semantics are intentionally unchanged.
    """

    definition = parse_workflow_definition(source)
    if isinstance(definition, WorkflowDefinitionProblem):
        return WorkflowCommandEvidence(
            status="unresolved",
            reason="workflow_definition_unreadable",
            detail=(
                "The shared GitHub Actions definition could not establish the bounded "
                f"CI structure: {definition.reason}: {definition.detail}"
            ),
            job_count=0,
        )

    assert isinstance(definition, WorkflowDefinition)
    if len(definition.jobs) != 1:
        return WorkflowCommandEvidence(
            status="unresolved",
            reason="multiple_or_zero_workflow_jobs",
            detail=(
                "The legacy CI rule requires one static job because static↔runtime "
                f"job correlation is not implemented; observed {len(definition.jobs)} jobs."
            ),
            job_count=len(definition.jobs),
        )

    job = definition.jobs[0]
    if isinstance(job, JobProblem):
        return WorkflowCommandEvidence(
            status="unresolved",
            reason="workflow_job_unreadable",
            detail=f"The selected static job is structurally unresolved: {job.reason}: {job.detail}",
            job_count=1,
            job_key=job.key,
        )
    if isinstance(job, ReusableWorkflowJobDefinition):
        return WorkflowCommandEvidence(
            status="unresolved",
            reason="reusable_workflow_job_unsupported",
            detail=(
                "The selected job delegates to a reusable workflow. Following that "
                "separate workflow definition is outside the legacy CI rule."
            ),
            job_count=1,
            job_key=job.key,
        )

    assert isinstance(job, StepsJobDefinition)
    return _inspect_legacy_steps_job(
        definition,
        job,
        source_file=source_file,
        package=package,
        normalized_package=normalized_package,
    )


def _inspect_legacy_steps_job(
    definition: WorkflowDefinition,
    job: StepsJobDefinition,
    *,
    source_file: str,
    package: str,
    normalized_package: str,
) -> WorkflowCommandEvidence:
    """Preserve the accepted legacy install-before-invocation rule unchanged."""

    installs: list[tuple[tuple[int, int], RunStepDefinition, DirectInstallDeclarationObservation]] = []
    invocations: list[tuple[tuple[int, int], RunStepDefinition]] = []
    first_unresolved_install: DirectInstallDeclarationObservation | None = None

    for entry in job.steps:
        if not isinstance(entry, RunStepDefinition):
            continue

        install = observe_direct_installation_declaration(
            entry,
            dependency_source_path=source_file,
            workflow_defaults=definition.run_defaults,
            job_defaults=job.run_defaults,
        )
        if install.state == "observed":
            assert install.matched_segment_index is not None
            installs.append(
                ((entry.source_index, install.matched_segment_index), entry, install)
            )
        elif install.state == "unresolved" and first_unresolved_install is None:
            first_unresolved_install = install

        invocation_segment = _first_package_invocation_segment_index(
            entry.command.text,
            package,
            normalized_package,
        )
        if invocation_segment is not None:
            invocations.append(((entry.source_index, invocation_segment), entry))

    for install_location, install_step, _install in installs:
        later_invocation = next(
            (
                (location, step)
                for location, step in invocations
                if install_location < location
            ),
            None,
        )
        if later_invocation is not None:
            invocation_location, invocation_step = later_invocation
            return WorkflowCommandEvidence(
                status="supported",
                reason="ordered_static_dependency_path_declared",
                detail=(
                    "The shared static workflow definition declares a direct install "
                    "from the supplied dependency source before a direct package "
                    "invocation in one job. Runtime correlation is not established."
                ),
                job_count=1,
                job_key=job.key,
                install_command=install_step.command.text,
                execution_command=invocation_step.command.text,
                install_step_source_index=install_location[0],
                execution_step_source_index=invocation_location[0],
            )

    if installs and invocations:
        return WorkflowCommandEvidence(
            status="unresolved",
            reason="static_install_not_before_invocation",
            detail=(
                "The static job declares both the dependency install and package "
                "invocation, but no admitted install declaration precedes an invocation."
            ),
            job_count=1,
            job_key=job.key,
            install_command=installs[0][1].command.text,
            execution_command=invocations[0][1].command.text,
            install_step_source_index=installs[0][0][0],
            execution_step_source_index=invocations[0][0][0],
        )

    if not installs and first_unresolved_install is not None:
        return WorkflowCommandEvidence(
            status="unresolved",
            reason=first_unresolved_install.reason,
            detail=first_unresolved_install.detail,
            job_count=1,
            job_key=job.key,
            install_command=first_unresolved_install.command,
            install_step_source_index=first_unresolved_install.step_source_index,
            execution_command=invocations[0][1].command.text if invocations else None,
            execution_step_source_index=invocations[0][0][0] if invocations else None,
        )

    missing: list[str] = []
    if not installs:
        missing.append(f"a direct installation declaration for {source_file!r}")
    if not invocations:
        missing.append(f"a direct invocation of {package!r}")

    return WorkflowCommandEvidence(
        status="unresolved",
        reason="static_dependency_path_incomplete",
        detail="The static workflow did not establish " + " and ".join(missing) + ".",
        job_count=1,
        job_key=job.key,
        install_command=installs[0][1].command.text if installs else None,
        execution_command=invocations[0][1].command.text if invocations else None,
        install_step_source_index=installs[0][0][0] if installs else None,
        execution_step_source_index=invocations[0][0][0] if invocations else None,
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
    "WorkflowCommandEvidence",
    "WorkflowCommandStatus",
    "WorkflowStaticDependencyEvidence",
    "inspect_workflow_commands",
    "inspect_workflow_dependency_evidence",
)
