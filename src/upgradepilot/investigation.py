"""Application orchestration for one read-only public pull-request investigation.

The application boundary coordinates already-defined provider/domain modules and returns
typed evidence for presentation. The normal CI branch now supplies exact project-environment
source bundles to the coverage/static-evidence owner so one workflow parse/traversal derives
direct requirements, project-environment consumption, and direct invocation together.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from .ci.dependency_exercise import (
    DependencyCICoverageResult,
    WorkflowDependencyCoverageInput,
)
from .ci.dependency_state import (
    RuntimeDependencyStateResult,
)
from .dependency.change import DependencyChangeProblem, DependencyVersionChange
from .dependency.environment import (
    DependencySourceContext,
    RequirementsFileDependencyContext,
)
from .github.actions import GitHubActionsClient, WorkflowJob, WorkflowRun
from .github.changelog import (
    ChangelogPathDiscoveryResult,
    DiscoveredChangelogPath,
    GitHubChangelogPathClient,
)
from .github.pull_request import (
    ChangedFile,
    GitHubPullRequestClient,
    PullRequestIdentity,
)
from .github.repository import GitHubRepositoryClient
from .github.tag import (
    GitHubTagCommitClient,
    GitHubTagCommitEvidence,
    GitHubTagCommitProblem,
    GitHubTagCommitResult,
)
from .impact.artifact_serviceability import (
    ArtifactServiceabilityCandidateResult,
    ArtifactServiceabilityImpactAssessment,
    ArtifactServiceabilityImpactCandidate,
    build_artifact_serviceability_impact_candidate,
    evaluate_artifact_serviceability_impact,
)
from .impact.python_support import (
    PythonSupportDropImpactAssessment,
    PythonSupportDropInvestigationSelection,
    build_python_support_drop_impact_candidate,
    evaluate_python_support_drop_impact,
    select_python_support_drop_investigation,
)
from .investigation_inputs import acquire_dependency_inputs, prepare_ci_evidence
from .pypi.release import (
    PackageReleaseEvidence,
    PackageReleaseIndexEvidence,
    PackageReleaseIndexResult,
    PackageReleaseResult,
    PyPIReleaseClient,
    PyPIReleaseIndexClient,
)
from .target.artifact_environment import (
    TargetArtifactEnvironmentResult,
    interpret_target_artifact_environment,
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
from .workspace.checkpoint_revision import CheckpointRevision
from .workspace.lifecycle_host import ExecutionAuthority, InvestigationWorkspaceHost
from .workspace.lifecycle_records import (
    InvestigationNeed,
    LifecycleMethodIdentity,
    RequestAdmission,
)
from .workspace.material_validity import native_material_closure
from .workspace.native_capture import NativeInvestigationCapture
from .workspace.repository_read_capability import (
    REPOSITORY_READ_CAPABILITY,
    repository_read_capability,
)

SupportDropEvaluator = Callable[
    [AuthoritativeUpstreamIntervalEvidence],
    UpstreamSupportDropClaimResult,
]


@dataclass(frozen=True, slots=True)
class DependencySourceArtifactEnvironmentResult:
    """Associate one dependency source with one static target-environment result."""

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
    runtime_dependency_state_result: RuntimeDependencyStateResult | None
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
    python_support_drop_pre_investigation_result: (
        PythonSupportDropImpactAssessment | None
    ) = None
    python_support_drop_investigation_selection: (
        PythonSupportDropInvestigationSelection | None
    ) = None
    python_support_drop_impact_result: PythonSupportDropImpactAssessment | None = None
    old_package_result: PackageReleaseResult | None = None
    artifact_serviceability_candidate_result: ArtifactServiceabilityCandidateResult = (
        None
    )
    target_artifact_environment_results: tuple[
        DependencySourceArtifactEnvironmentResult, ...
    ] = ()
    artifact_serviceability_impact_result: (
        ArtifactServiceabilityImpactAssessment | None
    ) = None
    workspace_revision: CheckpointRevision | None = None


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
    native_capture: NativeInvestigationCapture | None = None,
    workspace_host: InvestigationWorkspaceHost | None = None,
) -> PublicPullRequestInvestigation:
    """Run the current evidence graph without presentation or exit-policy logic.

    Native owners run once. A generic synchronous Workspace host publishes coherent native
    progress and selected-capability lifecycle; supply a host with a schema-2 store for
    durable publication. Default publication is volatile and chooses no filesystem location.
    The legacy report fields remain during later consumer migration; workspace_revision is
    the immutable canonical boundary, not a new evaluation or a resumable report.
    """

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

    acquired_inputs = acquire_dependency_inputs(
        repository, pull_number, pull_client, repository_client
    )
    pull_request = acquired_inputs.identity
    changed_files = acquired_inputs.changed_files
    dependency_result = acquired_inputs.dependency
    source_contexts = acquired_inputs.source_contexts

    native_capture = native_capture or NativeInvestigationCapture()
    workspace_host = workspace_host or InvestigationWorkspaceHost()
    native_capture.start(
        pull_request, changed_files, dependency_result, source_contexts
    )
    initial_boundary = native_capture.partial_snapshot()
    native_evaluation_method = LifecycleMethodIdentity(
        "impact.python_support",
        "impact.python_support.evaluate_python_support_drop_impact",
        None,
        None,
        "native-python-impact-caller/1",
        None,
        ("producer_version_unavailable",),
    )
    native_selection_method = LifecycleMethodIdentity(
        "impact.python_support",
        "impact.python_support.select_python_support_drop_investigation",
        None,
        None,
        "native-investigation-selection/1",
        None,
        ("producer_version_unavailable",),
    )
    workspace_host.bind_native_callers(
        authority=ExecutionAuthority(
            initial_boundary.target,
            frozenset({REPOSITORY_READ_CAPABILITY}),
            frozenset({"repository_read"}),
        ),
        capabilities=(repository_read_capability(pull_request, repository_client),),
        methods=(native_evaluation_method, native_selection_method),
    )
    workspace_host.initialize(initial_boundary)

    target_python_result: TargetPythonEvidence | None = None
    workflow_evidence: tuple[tuple[WorkflowRun, tuple[WorkflowJob, ...]], ...] = ()
    ci_coverage_result: DependencyCICoverageResult | None = None
    runtime_dependency_state_result: RuntimeDependencyStateResult | None = None
    package_result: PackageReleaseResult | None = None
    old_package_result: PackageReleaseResult | None = None
    artifact_serviceability_candidate_result: ArtifactServiceabilityCandidateResult = (
        None
    )
    target_artifact_environment_results: tuple[
        DependencySourceArtifactEnvironmentResult, ...
    ] = ()
    artifact_serviceability_impact_result: (
        ArtifactServiceabilityImpactAssessment | None
    ) = None
    upstream_repository_result: UpstreamRepositoryResult | None = None
    release_index_result: PackageReleaseIndexResult | None = None
    crossed_release_result: CrossedReleaseIndexSelectionResult | None = None
    tag_commit_result: GitHubTagCommitResult | None = None
    changelog_path_result: ChangelogPathDiscoveryResult | None = None
    tagged_changelog_result: TaggedChangelogCompositionResult | None = None
    upstream_interval_result: UpstreamIntervalAuthorityResult | None = None
    upstream_support_drop_result: UpstreamSupportDropClaimResult | None = None
    target_python_relevance_result: TargetPythonRelevanceResult | None = None
    python_support_drop_pre_investigation_result: (
        PythonSupportDropImpactAssessment | None
    ) = None
    python_support_drop_investigation_selection: (
        PythonSupportDropInvestigationSelection | None
    ) = None
    python_support_drop_impact_result: PythonSupportDropImpactAssessment | None = None

    if isinstance(dependency_result, DependencyVersionChange):
        prepared_ci = prepare_ci_evidence(
            acquired_inputs, actions_client, repository_client
        )
        workflow_evidence = prepared_ci.workflow_evidence
        coverage_inputs = list(prepared_ci.inputs)
        ci_coverage_result = prepared_ci.coverage
        runtime_dependency_state_result = prepared_ci.runtime
        native_capture.capture_ci(
            prepared_ci.inputs, ci_coverage_result, runtime_dependency_state_result
        )

        package_result = package_client.get_release(
            dependency_result.package,
            dependency_result.proposed_version,
        )
        if isinstance(package_result, PackageReleaseEvidence):
            old_package_result = package_client.get_release(
                dependency_result.package,
                dependency_result.old_version,
            )
            if isinstance(old_package_result, PackageReleaseEvidence):
                artifact_serviceability_candidate_result = (
                    build_artifact_serviceability_impact_candidate(
                        pull_request,
                        dependency_result,
                        old_package_result,
                        package_result,
                    )
                )
                if isinstance(
                    artifact_serviceability_candidate_result,
                    ArtifactServiceabilityImpactCandidate,
                ):
                    artifact_serviceability_impact_result = (
                        evaluate_artifact_serviceability_impact(
                            artifact_serviceability_candidate_result
                        )
                    )
                    target_artifact_environment_results = (
                        _compose_target_artifact_environments(
                            ci_coverage_result,
                            coverage_inputs,
                            source_contexts,
                        )
                    )

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

            if isinstance(tag_commit_result, GitHubTagCommitEvidence) and isinstance(
                changelog_path_result, DiscoveredChangelogPath
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

            if upstream_interval_result is not None:
                native_capture.capture_upstream_authority(upstream_interval_result)

            if isinstance(
                upstream_interval_result,
                AuthoritativeUpstreamIntervalEvidence,
            ):
                upstream_support_drop_result = support_drop_evaluator(
                    upstream_interval_result
                )
                native_capture.capture_upstream_claim(
                    upstream_support_drop_result, support_drop_evaluator
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
                    native_capture.capture_python_pre(
                        python_support_drop_pre_investigation_result,
                        python_support_drop_investigation_selection,
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

                        basis = native_capture.partial_snapshot()
                        workspace_host.publish_native_progress(basis)
                        selection_record = next(
                            record
                            for record in basis.records
                            if record.family == "python_support_selection"
                        )
                        need_id = workspace_host.add_purpose(
                            InvestigationNeed(
                                python_support_drop_investigation_selection.proposition_key,
                                python_support_drop_investigation_selection.detail,
                                python_support_drop_investigation_selection.path,
                            ),
                            native_record_ids=native_material_closure(
                                basis, (selection_record.record_id,)
                            ),
                            method=native_selection_method,
                        )
                        request_id = workspace_host.request_capability(
                            need_id,
                            REPOSITORY_READ_CAPABILITY,
                            python_support_drop_investigation_selection.path,
                        )
                        admission_id = workspace_host.admit_request(request_id)
                        admission = workspace_host.lifecycle_value(admission_id)
                        assert isinstance(admission, RequestAdmission)
                        if admission.outcome == "admitted":
                            observation_id, acquisition = (
                                workspace_host.execute_admission(admission_id)
                            )

                            # The generic host retains the actual provider response first.
                            # This existing native owner receives its full inputs, not a
                            # model's proposal/citation subset or a host interpretation.
                            def reassess_native():
                                nonlocal target_python_result
                                nonlocal target_python_relevance_result
                                nonlocal python_support_drop_impact_result
                                target_python_source = acquisition.value
                                target_python_result = (
                                    interpret_target_python_declaration(
                                        target_python_source
                                    )
                                )
                                native_capture.capture_target(
                                    target_python_source, target_python_result
                                )
                                target_python_relevance_result = (
                                    evaluate_target_python_relevance(
                                        upstream_support_drop_result,
                                        target_python_result,
                                    )
                                )
                                native_capture.capture_relevance(
                                    target_python_relevance_result
                                )
                                python_support_drop_impact_result = (
                                    evaluate_python_support_drop_impact(
                                        impact_candidate,
                                        target_python_relevance_result,
                                    )
                                )
                                native_capture.capture_python_post(
                                    python_support_drop_impact_result, reevaluated=True
                                )
                                boundary = native_capture.partial_snapshot()
                                assessment = next(
                                    record
                                    for record in boundary.records
                                    if record.family == "python_support_post_assessment"
                                )
                                return boundary, assessment.record_id

                            workspace_host.evaluate_native(
                                observation_id,
                                method=native_evaluation_method,
                                evaluate=reassess_native,
                            )
                    if (
                        target_python_relevance_result is not None
                        and python_support_drop_investigation_selection is None
                    ):
                        native_capture.capture_relevance(target_python_relevance_result)
                    if target_python_relevance_result is None:
                        native_capture.capture_python_post(
                            python_support_drop_impact_result, reevaluated=False
                        )
                else:
                    target_python_relevance_result = evaluate_target_python_relevance(
                        upstream_support_drop_result,
                        None,
                    )
                    native_capture.capture_relevance(target_python_relevance_result)

    native_capture.complete()
    workspace_host.publish_native_progress(native_capture.snapshot())
    workspace_host.terminate(
        workspace_host.lineage_id,
        "completed",
        "Normal procedural completion; investigation adequacy is not established.",
    )
    return PublicPullRequestInvestigation(
        workspace_revision=workspace_host.current,
        pull_request=pull_request,
        changed_files=changed_files,
        dependency_result=dependency_result,
        target_python_result=target_python_result,
        workflow_evidence=workflow_evidence,
        ci_coverage_result=ci_coverage_result,
        runtime_dependency_state_result=runtime_dependency_state_result,
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
        old_package_result=old_package_result,
        artifact_serviceability_candidate_result=(
            artifact_serviceability_candidate_result
        ),
        target_artifact_environment_results=target_artifact_environment_results,
        artifact_serviceability_impact_result=artifact_serviceability_impact_result,
    )


def _compose_target_artifact_environments(
    ci_coverage_result: DependencyCICoverageResult,
    coverage_inputs: list[WorkflowDependencyCoverageInput],
    source_contexts: tuple[DependencySourceContext, ...],
) -> tuple[DependencySourceArtifactEnvironmentResult, ...]:
    """Interpret only CI-supported direct-requirements source/workflow/job relationships."""

    if len(ci_coverage_result.workflows) != len(coverage_inputs):
        raise ValueError(
            "CI workflow results must preserve one-to-one ordering with coverage inputs"
        )

    results: list[DependencySourceArtifactEnvironmentResult] = []
    seen_relationships: set[tuple[str, str, str, str]] = set()

    for workflow_result, workflow_input in zip(
        ci_coverage_result.workflows,
        coverage_inputs,
        strict=True,
    ):
        definition = workflow_input.definition
        if workflow_result.workflow_path != definition.path:
            raise ValueError(
                "CI workflow result path does not match its exact workflow definition"
            )

        for consumption in workflow_result.consumptions:
            if (
                consumption.state != "supported"
                or consumption.mechanism != "direct_requirements"
                or consumption.source_path is None
            ):
                continue
            if (
                consumption.workflow_path != definition.path
                or consumption.workflow_revision != definition.revision
            ):
                raise ValueError(
                    "supported CI consumption does not match exact workflow identity"
                )
            if not consumption.job_key:
                raise ValueError(
                    "supported CI consumption must identify one consuming job"
                )

            matching_contexts = tuple(
                context
                for context in source_contexts
                if isinstance(context, RequirementsFileDependencyContext)
                and context.repository == definition.repository
                and context.source_path == consumption.source_path
                and context.revision == consumption.workflow_revision
                and context.normalized_package == consumption.normalized_package
            )
            if len(matching_contexts) != 1:
                raise ValueError(
                    "supported direct-requirements consumption must map to one exact "
                    "dependency source context"
                )
            source_context = matching_contexts[0]

            relationship = (
                consumption.workflow_revision,
                consumption.workflow_path,
                source_context.source_path,
                consumption.job_key,
            )
            if relationship in seen_relationships:
                continue
            seen_relationships.add(relationship)

            target_result = interpret_target_artifact_environment(
                definition,
                dependency_source_file=source_context.source_path,
                consuming_job_key=consumption.job_key,
            )
            if target_result.job != consumption.job_key:
                raise ValueError("Target result must retain the exact CI consuming job")
            results.append(
                DependencySourceArtifactEnvironmentResult(
                    dependency_source=source_context,
                    target_environment=target_result,
                )
            )

    return tuple(results)


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
