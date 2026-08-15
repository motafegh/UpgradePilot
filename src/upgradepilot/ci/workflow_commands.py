"""Interpret the bounded static CI dependency path from the shared workflow IR.

This module no longer parses GitHub Actions YAML. Provider structure comes from
``upgradepilot.github.workflow_definition`` and direct requirements installation comes
from ``upgradepilot.dependency.direct_install``. CI keeps only the interpretation that
is genuinely CI-specific here: identifying a direct invocation of the changed package
and deciding whether the static install declaration precedes that invocation.

A ``supported`` result means only that the exact-head *static definition* declares an
ordered install/invocation path in one bounded job. It is not runtime step correlation,
execution, or success evidence.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

from ..dependency.direct_install import (
    DirectInstallDeclarationObservation,
    observe_direct_installation_declaration,
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

type WorkflowCommandStatus = Literal["supported", "unresolved"]


@dataclass(frozen=True, slots=True)
class WorkflowCommandEvidence:
    """Static CI path extracted from one exact workflow definition.

    Step and segment indices are source locators only. They deliberately do not claim a
    mapping to runtime ``WorkflowStep`` records; that correlation remains outside
    Tranche 1.
    """

    status: WorkflowCommandStatus
    reason: str
    detail: str
    job_count: int
    job_key: str | None = None
    install_command: str | None = None
    execution_command: str | None = None
    install_step_source_index: int | None = None
    execution_step_source_index: int | None = None


def inspect_workflow_commands(
    source: RepositoryTextFile,
    *,
    source_file: str,
    package: str,
    normalized_package: str,
) -> WorkflowCommandEvidence:
    """Read one bounded static install→package-invocation path.

    The current CI rule intentionally selects exactly one statically readable local
    steps job. Multiple jobs remain unresolved because this tranche does not correlate
    a particular static job with a runtime job or infer cross-job environment continuity.
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
                "The current CI rule requires one static job because static↔runtime "
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
                "separate workflow definition is outside the current CI rule."
            ),
            job_count=1,
            job_key=job.key,
        )

    assert isinstance(job, StepsJobDefinition)
    return _inspect_steps_job(
        definition,
        job,
        source_file=source_file,
        package=package,
        normalized_package=normalized_package,
    )


def _inspect_steps_job(
    definition: WorkflowDefinition,
    job: StepsJobDefinition,
    *,
    source_file: str,
    package: str,
    normalized_package: str,
) -> WorkflowCommandEvidence:
    """Find an ordered static install/invocation pair inside one steps job."""

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
                (
                    (entry.source_index, install.matched_segment_index),
                    entry,
                    install,
                )
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

    # Source-order comparison is intentionally static. It tells us only that the
    # workflow definition places an admitted install declaration before an invocation;
    # it does not establish either command ran in the successful runtime job.
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
        # Leading environment assignments are a bounded static form already admitted by
        # the prior CI rule. We do not interpret arbitrary shell syntax beyond this.
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
    "WorkflowCommandEvidence",
    "WorkflowCommandStatus",
    "inspect_workflow_commands",
)
