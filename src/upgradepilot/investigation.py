"""Application orchestration for one read-only public pull-request investigation.

The application boundary coordinates already-defined provider/domain modules and returns
typed evidence for presentation. R6 now routes the normal CI branch through coverage-oriented
static consumption: exact admitted workflow definitions are combined with exact dependency
source context, R3 project selection, dependency-domain reachability/membership, and R5 CI
consumption before CI coverage is classified.
"""

from __future__ import annotations

import posixpath
from collections.abc import Callable
from dataclasses import dataclass

from .ci.dependency_exercise import (
    DependencyCICoverageResult,
    WorkflowDependencyCoverageInput,
    evaluate_dependency_ci_coverage,
)
from .ci.workflow_commands import (
    WorkflowProjectEnvironmentSource,
    derive_project_environment_consumptions,
)
from .dependency.analysis import DependencyChangeAnalysis, analyze_dependency_change
from .dependency.change import DependencyChangeProblem, DependencyVersionChange
from .dependency.environment import (
    DependencySourceContext,
    PyprojectDependencyGroupContext,
    PyprojectOptionalExtraDependencyContext,
    UvLockDependencyContext,
)
from .github.actions import GitHubActionsClient, WorkflowJob, WorkflowRun
from .github.changelog import (
    ChangelogPathDiscoveryResult,
    DiscoveredChangelogPath,
    GitHubChangelogPathClient,
)
from .github.pull_request import ChangedFile, GitHubPullRequestClient, PullRequestIdentity
from .github.repository import GitHubRepositoryClient, RepositoryTextFile
from .github.tag import (
    GitHubTagCommitClient,
    GitHubTagCommitEvidence,
    GitHubTagCommitProblem,
    GitHubTagCommitResult,
)
from .impact.artifact_serviceability import (
    ArtifactServiceabilityCandidateResult,
    ArtifactServiceabilityImpactAssessment,
)
from .impact.python_support import (
    PythonSupportDropImpactAssessment,
    PythonSupportDropInvestigationSelection,
    build_python_support_drop_impact_candidate,
    evaluate_python_support_drop_impact,
    select_python_support_drop_investigation,
)
from .pypi.release import (
    PackageReleaseEvidence,
    PackageReleaseIndexEvidence,
    PackageReleaseIndexResult,
    PackageReleaseResult,
    PyPIReleaseClient,
    PyPIReleaseIndexClient,
)
from .target.artifact_environment import TargetArtifactEnvironmentResult
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
    TaggedChangelogEvidence,
    UpstreamAuthoritySourceProblem,
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
class DependencySourceArtifactEnvironmentResult:
    """Associate one dependency source with one static target-environment result.

    The application layer preserves this relationship because one investigation can contain
    several dependency sources and several exact workflow definitions. The nested Target
    result remains the semantic owner and does not imply that the workflow executed.
    """

    dependency_source: DependencySourceContext
    target_environment: TargetArtifactEnvironmentResult


@dataclass(frozen=True, slots=True)
class PublicPullRequestInvestigation:
    """Typed result of the current read-only evidence and reasoning sequence."""

    pull_request: PullRequestIdentity
    changed_files: tuple[ChangedFile, ...]
    dependency_result: DependencyVersionChange | DependencyChangeProblem
    target_python_result: TargetPythonEvidence | None
    workflow_evidence: tuple[tuple[WorkflowRun, tuple[WorkflowJob, ...]], ...]
    ci_coverage_result: DependencyCICoverageResult | None
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
    python_support_drop_pre_investigation_result: PythonSupportDropImpactAssessment | None = None
    python_support_drop_investigation_selection: PythonSupportDropInvestigationSelection | None = None
    python_support_drop_impact_result: PythonSupportDropImpactAssessment | None = None
    old_package_result: PackageReleaseResult | None = None
    artifact_serviceability_candidate_result: ArtifactServiceabilityCandidateResult = None
    target_artifact_environment_results: tuple[
        DependencySourceArtifactEnvironmentResult, ...
    ] = ()
    artifact_serviceability_impact_result: ArtifactServiceabilityImpactAssessment | None = None


def investigate_public_pull_request(
    repository: str,
    pull_number: int,
    *,
    token: str | None = None,
    pull_client: GitHubPullRequestClient | None = None,
    actions_client: GitHubActionsClient | None = None,
    repository_client: GitHubRepositoryClient | None = None,
    package_client: PyPIReleaseClient | None = None,
    release_index_client: PyPIReleaseIndexClient | None = None,
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
    release_index_client = release_index_client or PyPIReleaseIndexClient()
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
        source_contexts: tuple[DependencySourceContext, ...] = analysis_result.source_contexts
    else:
        dependency_result = analysis_result
        source_contexts = ()

    target_python_result: TargetPythonEvidence | None = None
    workflow_evidence: tuple[tuple[WorkflowRun, tuple[WorkflowJob, ...]], ...] = ()
    ci_coverage_result: DependencyCICoverageResult | None = None
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
    python_support_drop_pre_investigation_result: PythonSupportDropImpactAssessment | None = None
    python_support_drop_investigation_selection: PythonSupportDropInvestigationSelection | None = None
    python_support_drop_impact_result: PythonSupportDropImpactAssessment | None = None

    if isinstance(dependency_result, DependencyVersionChange):
        # CI is an independent evidence branch. Exact workflow definitions remain provider-
        # admitted first; only then do R3/R4/R5 derive static changed-dependency consumption.
        workflow_runs = actions_client.get_exact_head_workflow_runs(pull_request)
        workflow_evidence = tuple(
            (run, actions_client.get_workflow_jobs(pull_request, run))
            for run in workflow_runs
        )
        project_environment_sources = (
            _acquire_project_environment_sources(
                pull_request,
                source_contexts,
                repository_client,
            )
            if workflow_evidence
            else ()
        )

        coverage_inputs: list[WorkflowDependencyCoverageInput] = []
        for run, jobs in workflow_evidence:
            definition = repository_client.get_exact_head_workflow_file(
                pull_request,
                run,
            )
            project_environment_consumptions = (
                derive_project_environment_consumptions(
                    definition,
                    sources=project_environment_sources,
                    normalized_package=dependency_result.normalized_package,
                )
                if isinstance(definition, RepositoryTextFile)
                else ()
            )
            coverage_inputs.append(
                WorkflowDependencyCoverageInput(
                    run=run,
                    jobs=jobs,
                    definition=definition,
                    project_environment_consumptions=(
                        project_environment_consumptions
                    ),
                )
            )

        ci_coverage_result = evaluate_dependency_ci_coverage(
            dependency_result,
            coverage_inputs,
            source_contexts=source_contexts,
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
            release_index_result = release_index_client.get_release_index(
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

            if (
                isinstance(tag_commit_result, GitHubTagCommitEvidence)
                and isinstance(changelog_path_result, DiscoveredChangelogPath)
            ):
                changelog_file = repository_client.get_exact_commit_text_file(
                    upstream_repository_result.repository,
                    tag_commit_result.resolved_commit_sha,
                    changelog_path_result.path,
                )
                tagged_changelog_result = build_tagged_changelog_evidence(
                    interval,
                    tag_commit_result,
                    changelog_file,
                )

                assert isinstance(crossed_release_result, SelectedCrossedReleaseIndex)
                if isinstance(tagged_changelog_result, TaggedChangelogEvidence):
                    upstream_interval_result = assemble_upstream_interval_authority(
                        interval,
                        upstream_repository_result.repository,
                        crossed_releases=crossed_release_result.evidence,
                        tagged_changelogs=(tagged_changelog_result,),
                    )
                else:
                    assert isinstance(
                        tagged_changelog_result,
                        UpstreamAuthoritySourceProblem,
                    )
                    upstream_interval_result = assemble_upstream_interval_authority(
                        interval,
                        upstream_repository_result.repository,
                        crossed_releases=crossed_release_result.evidence,
                        source_problems=(tagged_changelog_result,),
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
                    impact_candidate = build_python_support_drop_impact_candidate(
                        pull_request,
                        dependency_result,
                        upstream_support_drop_result,
                    )
                    python_support_drop_pre_investigation_result = (
                        evaluate_python_support_drop_impact(impact_candidate)
                    )
                    python_support_drop_investigation_selection = (
                        select_python_support_drop_investigation(
                            python_support_drop_pre_investigation_result
                        )
                    )
                    python_support_drop_impact_result = (
                        python_support_drop_pre_investigation_result
                    )

                    if python_support_drop_investigation_selection is not None:
                        if (
                            python_support_drop_investigation_selection.repository
                            != pull_request.repository
                            or python_support_drop_investigation_selection.revision
                            != pull_request.head_sha
                        ):
                            raise ValueError(
                                "selected Python-support investigation must preserve the "
                                "exact pull-request repository and head revision."
                            )

                        target_python_result = interpret_target_python_declaration(
                            repository_client.get_exact_head_text_file(
                                pull_request,
                                python_support_drop_investigation_selection.path,
                            )
                        )
                        target_python_relevance_result = evaluate_target_python_relevance(
                            upstream_support_drop_result,
                            target_python_result,
                        )
                        python_support_drop_impact_result = (
                            evaluate_python_support_drop_impact(
                                impact_candidate,
                                target_python_relevance_result,
                            )
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
        target_python_result=target_python_result,
        workflow_evidence=workflow_evidence,
        ci_coverage_result=ci_coverage_result,
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
        python_support_drop_pre_investigation_result=(
            python_support_drop_pre_investigation_result
        ),
        python_support_drop_investigation_selection=(
            python_support_drop_investigation_selection
        ),
        python_support_drop_impact_result=python_support_drop_impact_result,
    )


def _acquire_project_environment_sources(
    identity: PullRequestIdentity,
    source_contexts: tuple[DependencySourceContext, ...],
    repository_client: GitHubRepositoryClient,
) -> tuple[WorkflowProjectEnvironmentSource, ...]:
    """Acquire exact files needed to derive project-selection consumption in CI.

    For uv, the changed exact lock remains the reachability source while the exact sibling
    ``pyproject.toml`` establishes the project-root path consumed by the existing R3
    observer. Its content is deliberately not used by R4. For pyproject-owned affected
    environments, the already-known dependency-source path is the project-root source.
    Requirements/constraints remain owned by the direct-install path and need no bundle.
    """

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
    "DependencySourceArtifactEnvironmentResult",
    "PublicPullRequestInvestigation",
    "SupportDropEvaluator",
    "investigate_public_pull_request",
)
