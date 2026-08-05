"""Application orchestration for one read-only public pull-request investigation.

The application boundary coordinates already-defined provider/domain modules and
returns typed evidence for presentation. Step 7E keeps CI dependency-exercise evidence
independent while making target-Python acquisition conditional on one grounded upstream
Python support-drop claim.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from .ci.dependency_exercise import (
    DependencyCIExerciseResult,
    WorkflowDependencyExerciseInput,
    evaluate_dependency_ci_exercise,
)
from .dependency.analysis import DependencyChangeAnalysis, analyze_dependency_change
from .dependency.change import DependencyChangeProblem, DependencyVersionChange
from .github.actions import GitHubActionsClient, WorkflowJob, WorkflowRun
from .github.changelog import (
    ChangelogPathDiscoveryResult,
    DiscoveredChangelogPath,
    GitHubChangelogPathClient,
)
from .github.pull_request import ChangedFile, GitHubPullRequestClient, PullRequestIdentity
from .github.repository import GitHubRepositoryClient
from .github.tag import (
    GitHubTagCommitClient,
    GitHubTagCommitEvidence,
    GitHubTagCommitProblem,
    GitHubTagCommitResult,
)
from .pypi.release import (
    PackageReleaseEvidence,
    PackageReleaseIndexEvidence,
    PackageReleaseIndexResult,
    PackageReleaseResult,
    PyPIReleaseClient,
)
from .target.python import TargetPythonEvidence, interpret_target_python_declaration
from .target.relevance import (
    TargetPythonRelevanceResult,
    evaluate_target_python_relevance,
)
from .upstream.claim import (
    GroundedPythonSupportDropClaim,
    UpstreamSupportDropClaimResult,
)
from .upstream.interval import (
    AuthoritativeUpstreamIntervalEvidence,
    UpstreamIntervalAuthorityResult,
    assemble_upstream_interval_authority,
    release_interval_from_dependency_change,
)
from .upstream.interval_evidence import (
    CrossedReleaseIndexSelectionResult,
    SelectedCrossedReleaseIndex,
    TaggedChangelogCompositionResult,
    build_tagged_changelog_evidence,
    select_crossed_release_index,
)
from .upstream.repository import (
    UpstreamRepositoryEvidence,
    UpstreamRepositoryResolver,
    UpstreamRepositoryResult,
)
from .upstream.support_drop import evaluate_support_drop_runtime

SupportDropEvaluator = Callable[
    [AuthoritativeUpstreamIntervalEvidence],
    UpstreamSupportDropClaimResult,
]


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
    release_index_result: PackageReleaseIndexResult | None = None
    crossed_release_result: CrossedReleaseIndexSelectionResult | None = None
    tag_commit_result: GitHubTagCommitResult | None = None
    changelog_path_result: ChangelogPathDiscoveryResult | None = None
    tagged_changelog_result: TaggedChangelogCompositionResult | None = None
    upstream_interval_result: UpstreamIntervalAuthorityResult | None = None
    upstream_support_drop_result: UpstreamSupportDropClaimResult | None = None
    target_python_relevance_result: TargetPythonRelevanceResult | None = None


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
    tag_client: GitHubTagCommitClient | None = None,
    changelog_client: GitHubChangelogPathClient | None = None,
    support_drop_evaluator: SupportDropEvaluator | None = None,
) -> PublicPullRequestInvestigation:
    """Run the current evidence graph without presentation or exit-policy logic."""

    pull_client = pull_client or GitHubPullRequestClient(token=token)
    actions_client = actions_client or GitHubActionsClient(token=token)
    repository_client = repository_client or GitHubRepositoryClient(token=token)
    package_client = package_client or PyPIReleaseClient()
    upstream_repository_resolver = (
        upstream_repository_resolver or UpstreamRepositoryResolver()
    )
    tag_client = tag_client or GitHubTagCommitClient(token=token)
    changelog_client = changelog_client or GitHubChangelogPathClient(token=token)
    support_drop_evaluator = support_drop_evaluator or evaluate_support_drop_runtime

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
    release_index_result: PackageReleaseIndexResult | None = None
    crossed_release_result: CrossedReleaseIndexSelectionResult | None = None
    tag_commit_result: GitHubTagCommitResult | None = None
    changelog_path_result: ChangelogPathDiscoveryResult | None = None
    tagged_changelog_result: TaggedChangelogCompositionResult | None = None
    upstream_interval_result: UpstreamIntervalAuthorityResult | None = None
    upstream_support_drop_result: UpstreamSupportDropClaimResult | None = None
    target_python_relevance_result: TargetPythonRelevanceResult | None = None

    if isinstance(dependency_result, DependencyVersionChange):
        # CI remains an independent evidence branch. Its current narrow proof method is
        # neither gated by nor used to gate upstream semantic investigation.
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

        # The upstream branch first preserves the already-established exact package and
        # repository evidence. Later semantic/target stops do not erase these results.
        package_result = package_client.get_release(
            dependency_result.package,
            dependency_result.proposed_version,
        )
        if isinstance(package_result, PackageReleaseEvidence):
            upstream_repository_result = upstream_repository_resolver.resolve(
                package_result
            )

        if isinstance(upstream_repository_result, UpstreamRepositoryEvidence):
            interval = release_interval_from_dependency_change(dependency_result)
            release_index_result = package_client.get_release_index(
                dependency_result.package
            )

            if isinstance(release_index_result, PackageReleaseIndexEvidence):
                crossed_release_result = select_crossed_release_index(
                    interval,
                    upstream_repository_result.repository,
                    release_index_result,
                )

            if isinstance(crossed_release_result, SelectedCrossedReleaseIndex):
                tag_commit_result = _resolve_proposed_version_tag(
                    tag_client,
                    upstream_repository_result.repository,
                    dependency_result.proposed_version,
                )

            if isinstance(tag_commit_result, GitHubTagCommitEvidence):
                changelog_path_result = changelog_client.discover(
                    upstream_repository_result.repository,
                    tag_commit_result.resolved_commit_sha,
                )

            if isinstance(changelog_path_result, DiscoveredChangelogPath):
                changelog_file = repository_client.get_exact_commit_text_file(
                    upstream_repository_result.repository,
                    tag_commit_result.resolved_commit_sha,  # type: ignore[union-attr]
                    changelog_path_result.path,
                )
                tagged_changelog_result = build_tagged_changelog_evidence(
                    interval,
                    tag_commit_result,  # type: ignore[arg-type]
                    changelog_file,
                )

                if isinstance(crossed_release_result, SelectedCrossedReleaseIndex):
                    if hasattr(tagged_changelog_result, "content"):
                        upstream_interval_result = assemble_upstream_interval_authority(
                            interval,
                            upstream_repository_result.repository,
                            crossed_releases=crossed_release_result.evidence,
                            tagged_changelogs=(tagged_changelog_result,),  # type: ignore[arg-type]
                        )
                    else:
                        upstream_interval_result = assemble_upstream_interval_authority(
                            interval,
                            upstream_repository_result.repository,
                            crossed_releases=crossed_release_result.evidence,
                            source_problems=(tagged_changelog_result,),  # type: ignore[arg-type]
                        )

            if isinstance(
                upstream_interval_result,
                AuthoritativeUpstreamIntervalEvidence,
            ):
                upstream_support_drop_result = support_drop_evaluator(
                    upstream_interval_result
                )

                if isinstance(
                    upstream_support_drop_result,
                    GroundedPythonSupportDropClaim,
                ):
                    target_python_result = interpret_target_python_declaration(
                        repository_client.get_exact_head_text_file(
                            pull_request,
                            "pyproject.toml",
                        )
                    )
                    target_python_relevance_result = evaluate_target_python_relevance(
                        upstream_support_drop_result,
                        target_python_result,
                    )
                else:
                    target_python_relevance_result = evaluate_target_python_relevance(
                        upstream_support_drop_result,
                        None,
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
        release_index_result=release_index_result,
        crossed_release_result=crossed_release_result,
        tag_commit_result=tag_commit_result,
        changelog_path_result=changelog_path_result,
        tagged_changelog_result=tagged_changelog_result,
        upstream_interval_result=upstream_interval_result,
        upstream_support_drop_result=upstream_support_drop_result,
        target_python_relevance_result=target_python_relevance_result,
    )


def _resolve_proposed_version_tag(
    client: GitHubTagCommitClient,
    repository: str,
    proposed_version: str,
) -> GitHubTagCommitResult:
    """Resolve one of the two admitted canonical version-tag spellings."""

    direct = client.resolve_tag_to_commit(repository, proposed_version)
    if isinstance(direct, GitHubTagCommitEvidence):
        return direct
    if direct.state != "source_unavailable":
        return direct

    prefixed_tag = f"v{proposed_version}"
    prefixed = client.resolve_tag_to_commit(repository, prefixed_tag)
    if isinstance(prefixed, GitHubTagCommitEvidence):
        return prefixed
    if prefixed.state != "source_unavailable":
        return prefixed

    return GitHubTagCommitProblem(
        state="source_unavailable",
        repository=repository,
        requested_tag=proposed_version,
        detail=(
            "Neither admitted canonical proposed-version tag spelling was available: "
            f"{proposed_version!r} or {prefixed_tag!r}."
        ),
    )


__all__ = (
    "PublicPullRequestInvestigation",
    "SupportDropEvaluator",
    "investigate_public_pull_request",
)
