"""Run one read-only public pull-request evidence investigation.

This module owns application sequencing. Provider clients acquire evidence; domain
modules interpret it; the CLI remains responsible only for arguments, rendering, and
exit-status policy.

The sequencing here intentionally preserves the pre-Step-7 behavior. Conditional
target-Python activation belongs to the later Step 7 runtime-integration work, not this
source-structure reconciliation.
"""

from __future__ import annotations

from dataclasses import dataclass

from .ci.dependency_exercise import (
    DependencyCIExerciseResult,
    WorkflowDependencyExerciseInput,
    evaluate_dependency_ci_exercise,
)
from .dependency.analysis import DependencyChangeAnalysis, analyze_dependency_change
from .dependency.change import DependencyChangeProblem, DependencyVersionChange
from .github.actions import GitHubActionsClient, WorkflowJob, WorkflowRun
from .github.pull_request import ChangedFile, GitHubPullRequestClient, PullRequestIdentity
from .github.release import GitHubReleaseClient
from .github.repository import GitHubRepositoryClient
from .pypi.release import (
    PackageReleaseEvidence,
    PackageReleaseResult,
    PyPIReleaseClient,
)
from .target.python import TargetPythonEvidence, interpret_target_python_declaration
from .upstream_source import UpstreamSourceResolver, UpstreamSourceResult


@dataclass(frozen=True, slots=True)
class PublicPullRequestInvestigation:
    """All evidence/results produced by the current read-only application flow."""

    pull_request: PullRequestIdentity
    changed_files: tuple[ChangedFile, ...]
    dependency_result: DependencyVersionChange | DependencyChangeProblem
    direct_requirements_install_path: str | None
    target_python_result: TargetPythonEvidence | None
    workflow_evidence: tuple[tuple[WorkflowRun, tuple[WorkflowJob, ...]], ...]
    ci_exercise_result: DependencyCIExerciseResult | None
    package_result: PackageReleaseResult | None
    upstream_result: UpstreamSourceResult | None


def investigate_public_pull_request(
    repository: str,
    pull_number: int,
    *,
    github_token: str | None = None,
) -> PublicPullRequestInvestigation:
    """Acquire and interpret the current bounded public-PR evidence path."""

    pull_client = GitHubPullRequestClient(token=github_token)
    actions_client = GitHubActionsClient(token=github_token)
    repository_client = GitHubRepositoryClient(token=github_token)
    package_client = PyPIReleaseClient()
    upstream_resolver = UpstreamSourceResolver(
        github_release_client=GitHubReleaseClient(token=github_token)
    )

    pull_request = pull_client.get_pull_request(repository, pull_number)
    changed_files = pull_client.get_changed_files(pull_request)

    analysis_result = analyze_dependency_change(
        pull_request,
        changed_files,
        repository_client,
    )
    if isinstance(analysis_result, DependencyChangeAnalysis):
        dependency_result: DependencyVersionChange | DependencyChangeProblem = (
            analysis_result.dependency
        )
        direct_requirements_install_path = analysis_result.direct_requirements_install_path
    else:
        dependency_result = analysis_result
        direct_requirements_install_path = None

    target_python_result: TargetPythonEvidence | None = None
    workflow_evidence: tuple[tuple[WorkflowRun, tuple[WorkflowJob, ...]], ...] = ()
    ci_exercise_result: DependencyCIExerciseResult | None = None
    package_result: PackageReleaseResult | None = None
    upstream_result: UpstreamSourceResult | None = None

    if isinstance(dependency_result, DependencyVersionChange):
        target_python_result = interpret_target_python_declaration(
            repository_client.get_exact_head_text_file(
                pull_request,
                "pyproject.toml",
            )
        )

        workflow_runs = actions_client.get_exact_head_workflow_runs(pull_request)
        workflow_evidence = tuple(
            (run, actions_client.get_workflow_jobs(pull_request, run))
            for run in workflow_runs
        )
        exercise_inputs = tuple(
            WorkflowDependencyExerciseInput(
                run=run,
                jobs=jobs,
                definition=repository_client.get_exact_head_workflow_file(
                    pull_request,
                    run,
                ),
            )
            for run, jobs in workflow_evidence
        )
        ci_exercise_result = evaluate_dependency_ci_exercise(
            dependency_result,
            exercise_inputs,
            direct_requirements_install_path=direct_requirements_install_path,
        )

        package_result = package_client.get_release(
            dependency_result.package,
            dependency_result.proposed_version,
        )
        if isinstance(package_result, PackageReleaseEvidence):
            upstream_result = upstream_resolver.resolve(package_result)

    return PublicPullRequestInvestigation(
        pull_request=pull_request,
        changed_files=changed_files,
        dependency_result=dependency_result,
        direct_requirements_install_path=direct_requirements_install_path,
        target_python_result=target_python_result,
        workflow_evidence=workflow_evidence,
        ci_exercise_result=ci_exercise_result,
        package_result=package_result,
        upstream_result=upstream_result,
    )


__all__ = ("PublicPullRequestInvestigation", "investigate_public_pull_request")
