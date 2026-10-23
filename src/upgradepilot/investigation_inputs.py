"""Shared dependency/CI preparation for normal investigation and bounded consumers.

``acquire_dependency_inputs`` validates the provider's complete PR change set before the
existing dependency owner runs. ``prepare_ci_evidence`` supplies actual workflow inputs to
the CI owners once. No upstream interpretation, model, synthesis or target execution occurs.
Provider failure propagates; it cannot masquerade as an observed empty workflow set.
"""

from __future__ import annotations

import posixpath
from dataclasses import dataclass

from .ci.dependency_exercise import (
    DependencyCICoverageResult,
    WorkflowDependencyCoverageInput,
    evaluate_dependency_ci_coverage,
)
from .ci.dependency_state import (
    RuntimeDependencyStateResult,
    evaluate_runtime_dependency_state,
)
from .ci.workflow_commands import WorkflowProjectEnvironmentSource
from .dependency.analysis import DependencyChangeAnalysis, analyze_dependency_change
from .dependency.change import DependencyChangeProblem, DependencyVersionChange
from .dependency.environment import (
    DependencySourceContext,
    PyprojectDependencyGroupContext,
    PyprojectOptionalExtraDependencyContext,
    UvLockDependencyContext,
)
from .github.actions import GitHubActionsClient, WorkflowJob, WorkflowRun
from .github.pull_request import (
    ChangedFile,
    GitHubPullRequestClient,
    PullRequestIdentity,
    PullRequestDescriptionObservation,
)
from .github.repository import GitHubRepositoryClient


@dataclass(frozen=True, slots=True)
class AcquiredDependencyInputs:
    identity: PullRequestIdentity
    changed_files: tuple[ChangedFile, ...]
    dependency: DependencyVersionChange | DependencyChangeProblem
    source_contexts: tuple[DependencySourceContext, ...]
    description: PullRequestDescriptionObservation


@dataclass(frozen=True, slots=True)
class PreparedCIEvidence:
    workflow_evidence: tuple[tuple[WorkflowRun, tuple[WorkflowJob, ...]], ...]
    inputs: tuple[WorkflowDependencyCoverageInput, ...]
    coverage: DependencyCICoverageResult
    runtime: RuntimeDependencyStateResult


def acquire_dependency_inputs(
    repository: str,
    pull_number: int,
    pull_client: GitHubPullRequestClient,
    repository_client: GitHubRepositoryClient,
    *,
    expected_base: str | None = None,
    expected_head: str | None = None,
) -> AcquiredDependencyInputs:
    observation = pull_client.get_pull_request_observation(repository, pull_number)
    identity = observation.identity
    if (expected_base is not None and identity.base_sha != expected_base) or (
        expected_head is not None and identity.head_sha != expected_head
    ):
        raise ValueError("Pull request differs from the frozen base/head.")
    changed = pull_client.get_changed_files(identity)
    analysis = analyze_dependency_change(identity, changed, repository_client)
    if isinstance(analysis, DependencyChangeAnalysis):
        return AcquiredDependencyInputs(
            identity, changed, analysis.dependency, analysis.source_contexts, observation.description
        )
    return AcquiredDependencyInputs(identity, changed, analysis, (), observation.description)


def prepare_ci_evidence(
    inputs: AcquiredDependencyInputs,
    actions_client: GitHubActionsClient,
    repository_client: GitHubRepositoryClient,
) -> PreparedCIEvidence:
    if not isinstance(inputs.dependency, DependencyVersionChange):
        raise TypeError(
            "CI preparation requires an established native dependency transition."
        )
    identity = inputs.identity
    runs = actions_client.get_exact_head_workflow_runs(identity)
    evidence = tuple(
        (run, actions_client.get_workflow_jobs(identity, run)) for run in runs
    )
    sources = (
        _acquire_project_environment_sources(
            identity, inputs.source_contexts, repository_client
        )
        if evidence
        else ()
    )
    workflow_inputs = tuple(
        WorkflowDependencyCoverageInput(
            run,
            jobs,
            repository_client.get_exact_head_workflow_file(identity, run),
            sources,
        )
        for run, jobs in evidence
    )
    coverage = evaluate_dependency_ci_coverage(
        inputs.dependency, workflow_inputs, source_contexts=inputs.source_contexts
    )
    runtime = evaluate_runtime_dependency_state(
        inputs.dependency,
        workflow_inputs,
        coverage,
        source_contexts=inputs.source_contexts,
    )
    return PreparedCIEvidence(evidence, workflow_inputs, coverage, runtime)


def _acquire_project_environment_sources(
    identity: PullRequestIdentity,
    source_contexts: tuple[DependencySourceContext, ...],
    repository_client: GitHubRepositoryClient,
) -> tuple[WorkflowProjectEnvironmentSource, ...]:
    """Acquire exact files needed to derive project-selection consumption in CI."""

    sources: list[WorkflowProjectEnvironmentSource] = []
    for context in source_contexts:
        if isinstance(context, UvLockDependencyContext):
            lock_root = posixpath.dirname(context.source_path)
            project_path = (
                f"{lock_root}/pyproject.toml" if lock_root else "pyproject.toml"
            )
            sources.append(
                WorkflowProjectEnvironmentSource(
                    context=context,
                    project_file=repository_client.get_exact_head_text_file(
                        identity,
                        project_path,
                    ),
                    lock_file=repository_client.get_exact_head_text_file(
                        identity,
                        context.source_path,
                    ),
                )
            )
            continue

        if isinstance(
            context,
            (PyprojectOptionalExtraDependencyContext, PyprojectDependencyGroupContext),
        ):
            sources.append(
                WorkflowProjectEnvironmentSource(
                    context=context,
                    project_file=repository_client.get_exact_head_text_file(
                        identity,
                        context.source_path,
                    ),
                )
            )

    return tuple(sources)
