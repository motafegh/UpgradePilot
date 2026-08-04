"""Application orchestration for one read-only public pull-request investigation.

The application boundary coordinates already-defined provider/domain modules and
returns typed evidence for presentation. It deliberately preserves the pre-Step-7
execution order; conditional target-Python activation and semantic model integration
remain future work after source reconciliation.
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
from .github.repository import GitHubRepositoryClient
from .pypi.release import (
    PackageReleaseEvidence,
    PackageReleaseResult,
    PyPIReleaseClient,
)
from .target.python import TargetPythonEvidence, interpret_target_python_declaration
from .upstream.repository import (
    UpstreamRepositoryResolver,
    UpstreamRepositoryResult,
)


@dataclass(frozen=True, slots=True)
class PublicPullRequestInvestigation:
    """Typed result of the current read-only evidence sequence."""

    pull_request: PullRequestIdentity
    changed_files: tuple[ChangedFile, ...]
    dependency_result: DependencyVersionChange | DependencyChangeProblem
    direct_requirements_install_path: str | None
    target_python_result: TargetPythonEvidence | None
    workflow_evidence: tuple[tuple[WorkflowRun, tuple[WorkflowJob, ...]], ...]
    ci_exercise_result: DependencyCIExerciseResult | None
    package_result: PackageReleaseResult | None
    upstream_repository_result: UpstreamRepositoryResult | None


def investigate_public_pull_request(
    repository: str,
    pull_number: int,
    *,
    token: str | None = None,
    pull_client: GitHubPullRequestClient | None = None,
    actions_client: GitHubActionsClient | None = None,
    repository_client: GitHubRepositoryClient | None = None,
    package_client: PyPIReleaseClient | None = None,
    upstream_repository_resolver: UpstreamRepositoryResolver | None = None,
) -> PublicPullRequestInvestigation:
    """Run the current evidence pipeline without presentation or exit-policy logic."""

    pull_client = pull_client or GitHubPullRequestClient(token=token)
    actions_client = actions_client or GitHubActionsClient(token=token)
    repository_client = repository_client or GitHubRepositoryClient(token=token)
    package_client = package_client or PyPIReleaseClient()
    upstream_repository_resolver = (
        upstream_repository_resolver or UpstreamRepositoryResolver()
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
        direct_requirements_install_path = (
            analysis_result.direct_requirements_install_path
        )
    else:
        dependency_result = analysis_result
        direct_requirements_install_path = None

    target_python_result: TargetPythonEvidence | None = None
    workflow_evidence: tuple[tuple[WorkflowRun, tuple[WorkflowJob, ...]], ...] = ()
    ci_exercise_result: DependencyCIExerciseResult | None = None
    package_result: PackageReleaseResult | None = None
    upstream_repository_result: UpstreamRepositoryResult | None = None

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
            upstream_repository_result = upstream_repository_resolver.resolve(
                package_result
            )

    return PublicPullRequestInvestigation(
        pull_request=pull_request,
        changed_files=changed_files,
        dependency_result=dependency_result,
        direct_requirements_install_path=direct_requirements_install_path,
        target_python_result=target_python_result,
        workflow_evidence=workflow_evidence,
        ci_exercise_result=ci_exercise_result,
        package_result=package_result,
        upstream_repository_result=upstream_repository_result,
    )


__all__ = (
    "PublicPullRequestInvestigation",
    "investigate_public_pull_request",
)
