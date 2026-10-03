"""Explicit projection of owned investigation facts into the shared report contract.

Read ``project_investigation_report`` then its evidence-family helpers. No dataclass
reflection, domain reparsing, network acquisition or new impact/action inference occurs.
Each assessment cites its producer result; retained upstream text has its own exact source.
Absent inputs stay explicit, and an empty candidate horizon never becomes absence of risk.
"""

from __future__ import annotations

from datetime import UTC, datetime
from importlib.metadata import PackageNotFoundError, version
from urllib.parse import quote
from uuid import uuid4

from .ci.dependency_state import RequirementSatisfiedAtCommandCompletion
from .dependency.change import DependencyVersionChange
from .dependency.package_manager_semantics import (
    DirectRequirementHandlingFact,
    InstallationDestinationFact,
    ManagerEnvironmentSelectionFact,
    PackageMutationModeFact,
)
from .github.changelog import ChangelogPathDiscoveryProblem
from .github.tag import GitHubTagCommitProblem
from .impact.artifact_serviceability import (
    ArtifactServiceabilityEvidenceProblem,
    ArtifactServiceabilityImpactCandidate,
    TargetWheelCompatibilityEvidence,
)
from .investigation import PublicPullRequestInvestigation
from .maintainer_action import synthesize_maintainer_action
from .pypi.release import PackageReleaseEvidence, PackageReleaseIndexProblem
from .report import (
    InvestigationReport,
    ReportAction,
    ReportAssessment,
    ReportFact,
    ReportFinding,
    ReportSource,
    ReportUnknown,
)
from .target.artifact_environment import TargetArtifactEnvironmentEvidence
from .target.python import TargetPythonDeclaration
from .upstream.claim import GroundedPythonSupportDropClaim
from .upstream.interval import (
    AuthoritativeUpstreamIntervalEvidence,
    TaggedChangelogEvidence,
    UpstreamAuthoritySourceProblem,
)
from .upstream.interval_evidence import CrossedReleaseIndexSelectionProblem
from .upstream.repository import UpstreamRepositoryEvidence


def _fact(name: str, label: str, value: object) -> ReportFact:
    return ReportFact(name, label, str(value) if value is not None else "not recorded")


class _ReportProjection:
    """Invocation-local accumulation; never retained as agent/orchestration state."""

    def __init__(self, result: PublicPullRequestInvestigation) -> None:
        self.result = result
        self.assessments: list[ReportAssessment] = []
        self.sources: list[ReportSource] = []
        self.findings: list[ReportFinding] = []
        self.unknowns: list[ReportUnknown] = []

    def source(
        self,
        kind: str,
        *,
        locator: str | None = None,
        identity: tuple[ReportFact, ...] = (),
        method: str,
        content: str | None = None,
        retrieved_at: str | None = None,
        limitation: str = "Original input content is not retained in this report.",
    ) -> str:
        source_id = f"source-{len(self.sources) + 1}"
        retention = (
            "producer_result"
            if kind == "producer_assessment"
            else "retained_text"
            if content is not None
            else "selected_facts"
            if kind
            in {
                "package_metadata",
                "workflow_execution",
                "artifact_capabilities",
                "publisher_provenance",
            }
            else "reference_only"
        )
        self.sources.append(
            ReportSource(
                source_id,
                kind,
                locator,
                identity,
                method,
                retrieved_at,
                retention,
                content,
                limitation,
            )
        )
        return source_id

    def assess(
        self,
        assessment_id: str,
        topic: str,
        owner: str,
        state: str,
        detail: str,
        *,
        reason: str = "recorded_owner_result",
        status: str = "available",
        strength: str = "recorded_fact",
        proposition: str,
        facts: tuple[ReportFact, ...] = (),
        source_ids: tuple[str, ...] = (),
        limitations: tuple[str, ...] = (),
        question: str | None = None,
        consequence: str = "A maintainer-action consequence is not established.",
    ) -> None:
        producer = self.source(
            "producer_assessment",
            method=owner,
            identity=(
                _fact("assessment_id", "Assessment", assessment_id),
                _fact("state", "Recorded state", state),
                _fact("reason", "Recorded reason", reason),
            )
            + facts,
            content=detail,
            limitation="Retained producer assessment, not the original raw input.",
        )
        refs = (producer,) + source_ids
        self.assessments.append(
            ReportAssessment(
                assessment_id,
                topic,
                owner,
                state,
                status,
                reason,
                detail,
                proposition,
                strength,
                refs,
                facts,
                limitations,
            )
        )
        if status == "available":
            self.findings.append(ReportFinding(assessment_id, detail, strength, refs))
        if question is not None:
            self.unknowns.append(
                ReportUnknown(assessment_id, question, detail, refs, consequence)
            )

    def not_evaluated(
        self,
        assessment_id: str,
        topic: str,
        owner: str,
        state: str = "not evaluated",
        *,
        detail: str = "This branch has no evaluated result in the recorded investigation.",
        source_ids: tuple[str, ...] = (),
    ) -> None:
        self.assess(
            assessment_id,
            topic,
            owner,
            state,
            detail,
            reason="not_evaluated",
            status="not_evaluated",
            strength="unresolved",
            proposition="No positive or negative conclusion was established.",
            source_ids=source_ids,
            question=f"What does the {topic.lower()} branch establish?",
        )


def project_investigation_report(
    result: PublicPullRequestInvestigation,
    *,
    auth_mode: str = "anonymous",
    now: datetime | None = None,
) -> InvestigationReport:
    """Copy available evidence and explicitly scoped unknowns; do not rerun analysis."""
    if auth_mode not in {"anonymous", "token-env"}:
        raise ValueError("unsupported declared authentication mode")
    produced = now or datetime.now(UTC)
    if produced.tzinfo is None or produced.utcoffset() is None:
        raise ValueError("report generation time must be timezone-aware")
    p = _ReportProjection(result)
    pr = result.pull_request
    identity = (
        _fact("repository", "Repository", pr.repository),
        _fact("pull_number", "PR", pr.number),
        _fact("title", "Title", pr.title),
        _fact("author", "Author", pr.author),
        _fact("state", "State", pr.state),
        _fact("merged", "Merged", str(pr.merged).lower()),
        _fact("base_ref", "Base ref", pr.base_ref),
        _fact("base_sha", "Base", pr.base_sha),
        _fact("head_ref", "Head ref", pr.head_ref),
        _fact("head_sha", "Head", pr.head_sha),
    )
    pr_source = p.source(
        "pull_request",
        locator=f"https://github.com/{pr.repository}/pull/{pr.number}",
        identity=identity,
        method="exact PR base/head identity acquisition",
    )
    _project_dependency(p, pr_source)
    _project_ci(p)
    _project_packages(p)
    _project_upstream(p)
    _project_artifact(p)
    _project_python_target(p)
    synthesis = synthesize_maintainer_action(result)
    action = ReportAction(
        synthesis.action,
        synthesis.decisive_reasons,
        synthesis.residual_uncertainty,
        synthesis.limitations,
        synthesis.claim_limits,
    )
    try:
        product_version = version("upgradepilot")
    except PackageNotFoundError:
        product_version = None
    return InvestigationReport(
        str(uuid4()),
        produced.astimezone(UTC).isoformat(),
        "1",
        product_version,
        auth_mode,
        (
            "Code revision, model/prompt/config identity and complete operation history are not recorded.",
            "Generation time identifies report production; unavailable acquisition times remain unavailable.",
        ),
        identity,
        tuple(p.assessments),
        tuple(p.findings),
        tuple(p.unknowns),
        action,
        tuple(p.sources),
        (
            "Original workflow files/logs, dependency source files and arbitrary target code are not fully retained.",
            "Source references are availability-dependent; opening does not retrieve them.",
            "This record cannot replay analysis, resume an agent, or establish compatibility.",
            "A file digest detects corruption, not authenticity or evidence truth.",
        ),
    )


def _project_dependency(p: _ReportProjection, pr_source: str) -> None:
    result = p.result
    dependency = result.dependency_result
    changed = tuple(
        _fact(f"changed_file_{i}", "Changed file", f"{f.filename} ({f.status})")
        for i, f in enumerate(result.changed_files, 1)
    )
    if not isinstance(dependency, DependencyVersionChange):
        p.assess(
            "dependency",
            "Dependency change",
            "dependency.change",
            "unsupported",
            dependency.detail,
            reason=dependency.reason,
            status="problem",
            strength="unresolved",
            proposition="One supported exact dependency transition was not established.",
            facts=changed,
            source_ids=(pr_source,),
            question="What exact dependency transition is supported?",
        )
        return
    refs = []
    for evidence in dependency.source_evidence:
        refs.append(
            p.source(
                "dependency_source",
                method=evidence.extraction_method,
                locator=_repository_file_locator(
                    result.pull_request.repository,
                    result.pull_request.head_sha,
                    evidence.path,
                ),
                identity=(
                    _fact("path", "Dependency evidence", evidence.path),
                    _fact("format", "Format", evidence.file_format),
                    _fact("base_sha", "Base", result.pull_request.base_sha),
                    _fact("head_sha", "Head", result.pull_request.head_sha),
                ),
            )
        )
    p.assess(
        "dependency",
        "Dependency change",
        "dependency.change",
        "supported",
        "One supported exact dependency version transition was established.",
        proposition="Exact version transition only, not installation or compatibility.",
        facts=(
            _fact("package", "Package", dependency.package),
            _fact(
                "normalized_package",
                "Normalized package",
                dependency.normalized_package,
            ),
            _fact("old_version", "Old version", dependency.old_version),
            _fact("proposed_version", "Proposed version", dependency.proposed_version),
        )
        + changed,
        source_ids=(pr_source, *refs),
        limitations=dependency.limitations,
    )


def _project_ci(p: _ReportProjection) -> None:
    result = p.result
    run_refs = []
    for run, jobs in result.workflow_evidence:
        run_refs.append(
            p.source(
                "workflow_execution",
                method="exact-head run and captured-attempt jobs acquisition",
                locator=f"https://github.com/{result.pull_request.repository}/actions/runs/{run.run_id}/attempts/{run.run_attempt}",
                identity=(
                    _fact("run_id", "Run", run.run_id),
                    _fact("run_attempt", "Attempt", run.run_attempt),
                    _fact("head_sha", "Execution revision", run.head_sha),
                    _fact("status", "Status", run.status),
                    _fact("conclusion", "Conclusion", run.conclusion),
                )
                + tuple(
                    fact
                    for job in jobs
                    for fact in (
                        _fact(f"job_{job.job_id}_name", "Job", job.name),
                        _fact(
                            f"job_{job.job_id}_head_sha",
                            "Job execution revision",
                            job.head_sha,
                        ),
                        _fact(f"job_{job.job_id}_status", "Job status", job.status),
                        _fact(
                            f"job_{job.job_id}_conclusion",
                            "Job conclusion",
                            job.conclusion,
                        ),
                        _fact(
                            f"job_{job.job_id}_steps",
                            "Job steps",
                            "not retained" if job.steps is None else len(job.steps),
                        ),
                    )
                ),
            )
        )
    ci = result.ci_coverage_result
    if ci is None:
        p.not_evaluated("ci", "CI dependency coverage", "ci.dependency_exercise")
    else:
        unresolved = ci.state != "supported_runtime_correlated"
        p.assess(
            "ci",
            "CI dependency coverage",
            "ci.dependency_exercise",
            ci.state,
            ci.detail,
            reason=ci.reason,
            proposition="Static consumption and exact-attempt command correlation; not changed-version use or compatibility.",
            source_ids=tuple(run_refs),
            question="Was static dependency consumption correlated to successful exact-attempt execution?"
            if unresolved
            else None,
        )
        for i, workflow in enumerate(ci.workflows, 1):
            workflow_ref = p.source(
                "workflow_source",
                method="static workflow interpretation",
                locator=_repository_file_locator(
                    result.pull_request.repository,
                    result.pull_request.head_sha,
                    workflow.workflow_path,
                ),
                identity=(
                    _fact("path", "Workflow path", workflow.workflow_path),
                    _fact("revision", "Static revision", result.pull_request.head_sha),
                ),
            )
            facts = [
                _fact(
                    "static_consumption",
                    "Static consumption",
                    workflow.consumption_state,
                ),
                _fact(
                    "static_exercise",
                    "Static direct exercise",
                    workflow.direct_exercise_state,
                ),
                _fact(
                    "runtime_consumption",
                    "Runtime consumption correlation",
                    workflow.runtime_consumption_state,
                ),
                _fact(
                    "runtime_exercise",
                    "Runtime direct exercise correlation",
                    workflow.runtime_direct_exercise_state,
                ),
            ]
            for j, consumption in enumerate(workflow.consumptions, 1):
                facts.extend(
                    (
                        _fact(
                            f"command_{j}", "Consumption command", consumption.command
                        ),
                        _fact(f"job_{j}", "Static job", consumption.job_key),
                        _fact(f"state_{j}", "Consumption state", consumption.state),
                        _fact(f"reason_{j}", "Consumption reason", consumption.reason),
                        _fact(f"detail_{j}", "Consumption detail", consumption.detail),
                        _fact(
                            f"witness_{j}",
                            "Reachability witness",
                            " -> ".join(consumption.witness_path),
                        ),
                    )
                )
            p.assess(
                f"ci-workflow-{i}",
                f"Dependency coverage workflow {workflow.workflow_name}",
                "ci.dependency_exercise",
                workflow.state,
                workflow.detail,
                reason=workflow.reason,
                proposition="Workflow-scoped static/runtime relationships only.",
                facts=tuple(facts),
                source_ids=(workflow_ref, *run_refs),
                limitations=(
                    workflow.consumption_detail,
                    workflow.direct_exercise_detail,
                    workflow.runtime_consumption_detail,
                    workflow.runtime_direct_exercise_detail,
                ),
            )
    runtime = result.runtime_dependency_state_result
    if runtime is None:
        p.not_evaluated("runtime", "Runtime dependency state", "ci.dependency_state")
        return
    p.assess(
        "runtime",
        "Runtime dependency state",
        "ci.dependency_state",
        runtime.evaluation_state,
        runtime.detail,
        reason=runtime.reason,
        proposition="First admitted direct-requirements/pip command-completion family only.",
        question="Is the changed requirement satisfied at an admitted command-completion boundary?"
        if not runtime.assessments
        else None,
    )
    for i, assessment in enumerate(runtime.assessments, 1):
        c = assessment.consumption
        facts = [
            _fact("workflow", "Workflow", c.workflow_path),
            _fact("revision", "Workflow revision", c.workflow_revision),
            _fact("job", "Job", c.job_key),
            _fact("step_source_index", "Static step index", c.step_source_index),
            _fact("command", "Command", c.command),
        ]
        outcome = assessment.result
        positive = isinstance(outcome, RequirementSatisfiedAtCommandCompletion)
        if positive:
            facts.extend(
                (
                    _fact(
                        "observation_boundary",
                        "Observation boundary",
                        outcome.observation_boundary,
                    ),
                    _fact(
                        "execution_state", "Execution state", outcome.execution.state
                    ),
                    _fact(
                        "execution_basis", "Execution basis", outcome.execution.basis
                    ),
                    _fact(
                        "runtime_step_number",
                        "Runtime step number",
                        outcome.execution.runtime_step_number,
                    ),
                    _fact(
                        "runtime_status",
                        "Runtime status",
                        outcome.execution.runtime_status,
                    ),
                    _fact(
                        "runtime_conclusion",
                        "Runtime conclusion",
                        outcome.execution.runtime_conclusion,
                    ),
                )
            )
        else:
            facts.append(
                _fact(
                    "blocking_dimension",
                    "Blocking semantic dimension",
                    outcome.blocking_dimension,
                )
            )
        if c.command_location is not None:
            location = c.command_location
            facts.extend(
                (
                    _fact(
                        "command_source_order",
                        "Command source order",
                        location.source_order,
                    ),
                    _fact(
                        "command_start_byte",
                        "Command start byte",
                        location.source_span.start_byte,
                    ),
                    _fact(
                        "command_end_byte",
                        "Command end byte",
                        location.source_span.end_byte,
                    ),
                )
            )
        if positive:
            for name, value in (
                ("manager_environment", outcome.semantics.manager_environment),
                (
                    "installation_destination",
                    outcome.semantics.installation_destination,
                ),
                ("package_mutation_mode", outcome.semantics.package_mutation_mode),
                (
                    "direct_requirement_handling",
                    outcome.semantics.direct_requirement_handling,
                ),
            ):
                facts.extend(_project_semantic_fact(name, value))
        elif outcome.blocking_semantic_evidence is not None:
            facts.extend(
                _project_semantic_fact(
                    "blocking_evidence", outcome.blocking_semantic_evidence
                )
            )
        source = p.source(
            "workflow_source",
            method="scoped command assessment",
            identity=tuple(facts),
            locator=_repository_file_locator(
                result.pull_request.repository, c.workflow_revision, c.workflow_path
            ),
        )
        p.assess(
            f"runtime-command-{i}",
            "Command-completion requirement state",
            "ci.dependency_state",
            "satisfied_at_command_completion" if positive else outcome.state,
            "The proposed direct requirement is satisfied at successful command completion."
            if positive
            else outcome.detail,
            reason="command_completion_witness" if positive else outcome.reason,
            status="available" if positive else "problem",
            strength="recorded_fact" if positive else "unresolved",
            proposition="Command-completion satisfaction only; fresh installation, later use and behavior are not established.",
            facts=tuple(facts),
            source_ids=(source, *run_refs),
            limitations=outcome.limitations if positive else (),
            question="What requirement state was established at this exact command?"
            if not positive
            else None,
        )


def _project_packages(p: _ReportProjection) -> None:
    for key, topic, package in (
        ("package", "Package evidence", p.result.package_result),
        ("old-package", "Old package artifact evidence", p.result.old_package_result),
    ):
        if package is None:
            p.not_evaluated(key, topic, "pypi.release")
            continue
        available = isinstance(package, PackageReleaseEvidence)
        facts = (
            _fact("requested_package", "Requested package", package.requested_package),
            _fact("requested_version", "Requested version", package.requested_version),
        )
        if available:
            facts += (
                _fact(
                    "published_package",
                    "Published package"
                    if key == "package"
                    else "Old published package",
                    f"{package.published_name}=={package.published_version}",
                ),
                _fact(
                    "distribution_count",
                    "Distribution files"
                    if key == "package"
                    else "Old distribution files",
                    package.distribution_file_count,
                ),
            )
        source = p.source(
            "package_metadata",
            locator=package.source_url,
            method="exact package-release metadata acquisition",
            identity=facts
            + (
                tuple(
                    fact
                    for i, f in enumerate(package.distribution_files, 1)
                    for fact in (
                        _fact(f"file_{i}_filename", "Distribution file", f.filename),
                        _fact(f"file_{i}_type", "Distribution type", f.package_type),
                        _fact(f"file_{i}_sha256", "Distribution SHA-256", f.sha256),
                        _fact(f"file_{i}_url", "Distribution URL", f.url),
                    )
                )
                if available
                else ()
            ),
            retrieved_at=package.retrieved_at.isoformat() if available else None,
            limitation="Selected metadata retained as identity facts; raw provider JSON is not retained.",
        )
        p.assess(
            key,
            topic,
            "pypi.release",
            "available" if available else package.state,
            "Exact published package metadata is available."
            if available
            else package.detail,
            status="available" if available else "problem",
            strength="recorded_fact" if available else "unresolved",
            proposition="Published release metadata and files, not observed target installation.",
            facts=facts,
            source_ids=(source,),
            question="What exact published release evidence is available?"
            if not available
            else None,
        )


def _project_upstream(p: _ReportProjection) -> None:
    result = p.result
    repository = result.upstream_repository_result
    if repository is None:
        p.not_evaluated(
            "upstream-repository", "Upstream repository", "upstream.repository"
        )
    elif isinstance(repository, UpstreamRepositoryEvidence):
        provenance_refs = []
        for evidence in repository.provenance:
            facts = (
                _fact("package", "Package", evidence.package),
                _fact("version", "Version", evidence.version),
                _fact("filename", "Distribution file", evidence.filename),
                _fact("sha256", "Distribution SHA-256", evidence.sha256),
                _fact("api_version", "Provenance API version", evidence.api_version),
                _fact(
                    "attestation_count", "Attestation count", evidence.attestation_count
                ),
            )
            facts += tuple(
                fact
                for i, publisher in enumerate(evidence.publishers, 1)
                for fact in (
                    _fact(f"publisher_{i}_kind", "Publisher kind", publisher.kind),
                    _fact(
                        f"publisher_{i}_repository",
                        "Publisher repository",
                        publisher.repository,
                    ),
                    _fact(
                        f"publisher_{i}_workflow",
                        "Publisher workflow",
                        publisher.workflow,
                    ),
                )
            )
            provenance_refs.append(
                p.source(
                    "publisher_provenance",
                    locator=evidence.source_url,
                    retrieved_at=evidence.retrieved_at.isoformat(),
                    method="PyPI file publisher provenance acquisition",
                    identity=facts,
                    limitation="Selected publisher/file identity facts retained; full attestation input is not retained.",
                )
            )
        p.assess(
            "upstream-repository",
            "Upstream repository",
            "upstream.repository",
            "available",
            "Upstream repository identity was resolved from package provenance.",
            proposition="Resolved upstream source identity, not semantic correctness.",
            source_ids=tuple(provenance_refs),
            facts=(
                _fact(
                    "repository", "Upstream repository identity", repository.repository
                ),
                _fact(
                    "unavailable_files",
                    "Provenance unavailable files",
                    ", ".join(repository.provenance_unavailable_files) or "none",
                ),
            ),
        )
    else:
        p.assess(
            "upstream-repository",
            "Upstream repository",
            "upstream.repository",
            repository.state,
            repository.detail,
            status="problem",
            strength="unresolved",
            proposition="Repository identity remains unresolved.",
            question="Which upstream repository has applicable authority?",
        )
    # Preserve branch-stopping problems even when no interval/claim was produced. These
    # typed intermediate states explain why later authority could not be evaluated.
    for key, topic, owner, value in (
        (
            "release-index",
            "Package release index",
            "pypi.release",
            result.release_index_result,
        ),
        (
            "crossed-release",
            "Crossed release selection",
            "upstream.interval_evidence",
            result.crossed_release_result,
        ),
        ("tag", "Proposed-version tag", "github.tag", result.tag_commit_result),
        (
            "changelog-path",
            "Changelog discovery",
            "github.changelog",
            result.changelog_path_result,
        ),
        (
            "tagged-changelog",
            "Tagged changelog composition",
            "upstream.interval_evidence",
            result.tagged_changelog_result,
        ),
    ):
        # Successful intermediate records are represented by the authoritative interval;
        # typed problems carry state/detail and must remain independently inspectable.
        if isinstance(
            value,
            (
                PackageReleaseIndexProblem,
                CrossedReleaseIndexSelectionProblem,
                GitHubTagCommitProblem,
                ChangelogPathDiscoveryProblem,
                UpstreamAuthoritySourceProblem,
            ),
        ):
            p.assess(
                key,
                topic,
                owner,
                value.state,
                value.detail,
                status="problem",
                strength="unresolved",
                proposition="Recorded upstream acquisition/composition problem.",
                question=f"What establishes {topic.lower()}?",
            )

    problems = [
        a
        for a in p.assessments
        if a.status == "problem"
        and a.assessment_id
        in {
            "package",
            "upstream-repository",
            "release-index",
            "crossed-release",
            "tag",
            "changelog-path",
            "tagged-changelog",
        }
    ]
    prerequisite_detail = (
        (
            "Recorded upstream prerequisites are unavailable: "
            + "; ".join(f"{a.topic}: {a.state}: {a.detail}" for a in problems)
        )
        if problems
        else "This branch has no evaluated result in the recorded investigation."
    )
    prerequisite_refs = tuple(ref for a in problems for ref in a.source_ids)
    interval = result.upstream_interval_result
    authority_refs = []
    if isinstance(
        result.tagged_changelog_result, TaggedChangelogEvidence
    ) and not isinstance(interval, AuthoritativeUpstreamIntervalEvidence):
        source = result.tagged_changelog_result
        authority_refs.append(
            p.source(
                "tagged_changelog",
                method="exact proposed-tag text acquisition",
                locator=_repository_file_locator(
                    source.repository, source.resolved_commit_sha, source.path
                ),
                identity=(
                    _fact("repository", "Repository", source.repository),
                    _fact("revision", "Revision", source.resolved_commit_sha),
                    _fact("path", "Path", source.path),
                ),
                content=source.content,
                limitation="Retained exact source text; interval authority was not established.",
            )
        )
    if isinstance(interval, AuthoritativeUpstreamIntervalEvidence):
        if interval.tagged_changelog is not None:
            source = interval.tagged_changelog
            authority_refs.append(
                p.source(
                    "tagged_changelog",
                    method="exact tagged changelog authority",
                    locator=_repository_file_locator(
                        source.repository, source.resolved_commit_sha, source.path
                    ),
                    identity=(
                        _fact("repository", "Repository", source.repository),
                        _fact("revision", "Revision", source.resolved_commit_sha),
                        _fact("path", "Path", source.path),
                    ),
                    content=source.content,
                    limitation="Complete already-retained changelog text; no acquisition time was retained.",
                )
            )
        for source in interval.release_bodies:
            release = source.release
            authority_refs.append(
                p.source(
                    "github_release_body",
                    method="exact release authority",
                    locator=release.release_url,
                    content=release.body,
                    retrieved_at=release.retrieved_at.isoformat(),
                    identity=(
                        _fact("version", "Release version", source.release_version),
                        _fact("repository", "Repository", release.repository),
                        _fact("tag_ref", "Tag ref", release.tag_ref),
                        _fact("tag_object_sha", "Tag object", release.tag_object_sha),
                    ),
                    limitation="Retained release-body text when present; not a complete provider response.",
                )
            )
        for metadata in interval.package_metadata:
            authority_refs.append(
                p.source(
                    "package_metadata",
                    method="package metadata corroboration record",
                    locator=metadata.source_url,
                    retrieved_at=metadata.retrieved_at.isoformat(),
                    identity=(
                        _fact("package", "Package", metadata.package),
                        _fact("version", "Release version", metadata.release_version),
                        _fact(
                            "requires_python",
                            "Requires Python",
                            metadata.requires_python,
                        ),
                    ),
                    limitation="Selected metadata retained; metadata does not replace authoritative release text.",
                )
            )
        p.assess(
            "upstream-interval",
            "Upstream interval authority",
            "upstream.interval",
            "available",
            "An authoritative source covers the selected dependency release interval.",
            proposition="Source authority for the evaluated interval, not corroboration of model interpretation.",
            facts=(
                _fact(
                    "authority_basis",
                    "Upstream interval authority basis",
                    interval.authority_basis,
                ),
                _fact(
                    "crossed_versions",
                    "Crossed releases",
                    ", ".join(interval.crossed_releases.ordered_versions)
                    if interval.crossed_releases
                    else "not established",
                ),
            ),
            source_ids=tuple(authority_refs),
        )
    elif interval is None:
        p.not_evaluated(
            "upstream-interval",
            "Upstream interval authority",
            "upstream.interval",
            "not established",
            detail=prerequisite_detail,
            source_ids=prerequisite_refs,
        )
    else:
        p.assess(
            "upstream-interval",
            "Upstream interval authority",
            "upstream.interval",
            interval.state,
            interval.detail,
            status="problem",
            strength="unresolved",
            proposition="Interval authority remains unresolved.",
            source_ids=tuple(authority_refs),
            question="Which authoritative source covers this release interval?",
        )
    claim = result.upstream_support_drop_result
    if isinstance(claim, GroundedPythonSupportDropClaim):
        quotes = []
        refs = list(authority_refs)
        for i, evidence in enumerate(claim.source_evidence, 1):
            source = evidence.source
            if isinstance(source, TaggedChangelogEvidence):
                locator = _repository_file_locator(
                    source.repository, source.resolved_commit_sha, source.path
                )
            else:
                locator = source.release.release_url
            refs.append(
                p.source(
                    "grounded_quote",
                    locator=locator,
                    method="exact source-quote offset grounding",
                    content=evidence.source_quote,
                    identity=(
                        _fact("offset_unit", "Quote offset unit", "unicode_codepoints"),
                        _fact("quote_start", "Quote start", evidence.quote_start),
                        _fact("quote_end", "Quote end", evidence.quote_end),
                        _fact("source_kind", "Source kind", evidence.source_kind),
                        _fact(
                            "introduced_in_version",
                            "Introduced in release",
                            evidence.introduced_in_version,
                        ),
                    ),
                    limitation="Exact excerpt with source offsets; omitted context is not represented by this excerpt.",
                )
            )
            quotes.append(_fact(f"quote_{i}", "Grounded quote", evidence.source_quote))
        p.assess(
            "support-drop",
            "Upstream support-drop result",
            "upstream.claim",
            "grounded",
            "A proposed Python support-drop interpretation was grounded to exact authoritative source text.",
            strength="grounded_interpretation",
            proposition="Grounding establishes source correspondence, not independent semantic corroboration.",
            facts=(
                _fact("python_line", "Dropped Python line", claim.python_line),
                _fact(
                    "introduced_in_version",
                    "Introduced in upstream release",
                    claim.introduced_in_version,
                ),
                *quotes,
            ),
            source_ids=tuple(refs),
        )
    elif claim is None:
        prerequisite = next(
            a for a in p.assessments if a.assessment_id == "upstream-interval"
        )
        p.not_evaluated(
            "support-drop",
            "Upstream support-drop result",
            "upstream.claim",
            detail=prerequisite.detail,
            source_ids=prerequisite.source_ids,
        )
    else:
        p.assess(
            "support-drop",
            "Upstream support-drop result",
            "upstream.claim",
            claim.state,
            claim.detail,
            status="problem",
            strength="unresolved",
            proposition="Only the bounded Python-support-drop candidate horizon was evaluated; no global absence of impact follows.",
            source_ids=tuple(authority_refs),
            question="What Python-support-drop interpretation can be established in the evaluated interval?",
        )


def _project_artifact(p: _ReportProjection) -> None:
    result = p.result
    candidate = result.artifact_serviceability_candidate_result
    if candidate is None:
        compared = isinstance(
            result.package_result, PackageReleaseEvidence
        ) and isinstance(result.old_package_result, PackageReleaseEvidence)
        if compared:
            p.assess(
                "artifact-candidate",
                "Artifact serviceability candidate",
                "impact.artifact_serviceability",
                "not observed",
                "Exact old/proposed release comparison completed without a bounded published-wheel capability loss.",
                proposition="No candidate within the evaluated published-wheel capability horizon; source builds and all other impacts remain unproven.",
            )
        else:
            p.not_evaluated(
                "artifact-candidate",
                "Artifact serviceability candidate",
                "impact.artifact_serviceability",
            )
    elif isinstance(candidate, ArtifactServiceabilityEvidenceProblem):
        p.assess(
            "artifact-candidate",
            "Artifact serviceability candidate",
            "impact.artifact_serviceability",
            "evidence problem",
            candidate.detail,
            status="problem",
            strength="unresolved",
            proposition="Comparison failed; no absence-of-candidate conclusion follows.",
            facts=(
                _fact("problem_state", "Artifact candidate problem", candidate.state),
                _fact(
                    "release", "Artifact candidate release", candidate.release_version
                ),
                _fact("filename", "Artifact candidate file", candidate.filename),
            ),
            question="Can the published artifact capabilities be compared?",
        )
    else:
        assert isinstance(candidate, ArtifactServiceabilityImpactCandidate)
        capabilities = p.source(
            "artifact_capabilities",
            method="exact old/proposed published wheel capability comparison",
            identity=(
                _fact(
                    "old_version",
                    "Old version",
                    candidate.old_release.published_version,
                ),
                _fact(
                    "proposed_version",
                    "Proposed version",
                    candidate.proposed_release.published_version,
                ),
            )
            + tuple(
                _fact(f"removed_tag_{i}", "Removed wheel tag", str(tag))
                for i, tag in enumerate(
                    sorted(candidate.removed_wheel_tags, key=str), 1
                )
            )
            + tuple(
                _fact(f"added_tag_{i}", "Added wheel tag", str(tag))
                for i, tag in enumerate(sorted(candidate.added_wheel_tags, key=str), 1)
            ),
            limitation="Selected capability facts retained; target installation and source-build results are not established.",
        )
        p.assess(
            "artifact-candidate",
            "Artifact serviceability candidate",
            "impact.artifact_serviceability",
            "established",
            "Published wheel-tag capabilities were removed across the exact release transition.",
            strength="candidate",
            proposition="Published artifact capability change, not target installation failure.",
            facts=(
                _fact(
                    "removed_count",
                    "Removed published wheel-tag capabilities",
                    len(candidate.removed_wheel_tags),
                ),
                _fact(
                    "added_count",
                    "Added published wheel-tag capabilities",
                    len(candidate.added_wheel_tags),
                ),
                _fact(
                    "source_distribution",
                    "Proposed source distribution",
                    "available"
                    if candidate.proposed_source_distribution_available
                    else "unavailable",
                ),
            ),
            source_ids=(
                capabilities,
                *tuple(s.source_id for s in p.sources if s.kind == "package_metadata"),
            ),
        )
    if result.target_artifact_environment_results:
        p.assess(
            "artifact-environments",
            "Target artifact environments",
            "target.artifact_environment",
            str(len(result.target_artifact_environment_results)),
            "Scoped target environment associations are retained.",
            proposition="Association count does not establish exact wheel compatibility.",
        )
    if not result.target_artifact_environment_results:
        p.not_evaluated(
            "artifact-environments",
            "Target artifact environments",
            "target.artifact_environment",
            "not activated",
        )
    for i, association in enumerate(result.target_artifact_environment_results, 1):
        target = association.target_environment
        available = isinstance(target, TargetArtifactEnvironmentEvidence)
        facts = (
            _fact(
                "dependency_source",
                f"Target artifact environment {i} source",
                association.dependency_source.source_path,
            ),
            _fact(
                "workflow", "Workflow", f"{target.workflow_path} @ {target.revision}"
            ),
            _fact("job", "Job", target.job),
        )
        if available:
            facts += (
                _fact(
                    "runner",
                    "Runner",
                    target.runner.value if target.runner else "unresolved",
                ),
                _fact(
                    "python",
                    "Python",
                    target.python_version.value
                    if target.python_version
                    else "unresolved",
                ),
                _fact(
                    "installation_declaration",
                    "Dependency installation declaration",
                    target.dependency_installation_declaration,
                ),
                _fact(
                    "wheel_compatibility",
                    "Exact wheel compatibility",
                    target.exact_wheel_compatibility_state,
                ),
            )
        source = p.source(
            "workflow_source",
            method="static target environment interpretation",
            identity=facts,
            locator=_repository_file_locator(
                target.repository or result.pull_request.repository,
                target.revision,
                target.workflow_path,
            ),
        )
        p.assess(
            f"artifact-environment-{i}",
            f"Target artifact environment {i}",
            "target.artifact_environment",
            "available" if available else target.state,
            "Scoped static target environment evidence is available."
            if available
            else target.detail,
            status="available" if available else "problem",
            strength="recorded_fact" if available else "unresolved",
            proposition="Static target environment declaration, not observed installation or source-build success.",
            facts=facts,
            source_ids=(source,),
            limitations=target.limitations if available else (),
            question="Which exact target environment is applicable?"
            if not available
            else None,
        )
    impact = result.artifact_serviceability_impact_result
    if impact is None:
        p.not_evaluated(
            "artifact-impact",
            "Artifact applicability",
            "impact.artifact_serviceability",
        )
        return
    target = impact.target_evidence
    if isinstance(target, TargetWheelCompatibilityEvidence):
        facts = (
            _fact(
                "target_compatibility", "Exact target wheel compatibility", "available"
            ),
            _fact(
                "target_source",
                "Exact target wheel compatibility source",
                target.source,
            ),
            _fact(
                "supported_tags",
                "Supported target wheel-tag capabilities",
                len(target.supported_tags),
            ),
        )
    elif target is not None:
        facts = (
            _fact(
                "target_compatibility", "Exact target wheel compatibility", target.state
            ),
            _fact(
                "target_source",
                "Exact target wheel compatibility source",
                target.source,
            ),
            _fact(
                "target_detail",
                "Exact target wheel compatibility detail",
                target.detail,
            ),
        )
    else:
        facts = (
            _fact(
                "target_compatibility",
                "Exact target wheel compatibility",
                "not established",
            ),
        )
    p.assess(
        "artifact-impact",
        "Artifact applicability",
        "impact.artifact_serviceability",
        impact.applicability.state,
        impact.applicability.detail,
        proposition="Technical applicability only, not maintainer-action authority or installation outcome.",
        facts=facts,
        question="Is this artifact capability loss applicable to the exact target?"
        if impact.applicability.state in {"unresolved", "conflicted"}
        else None,
    )
    if (
        isinstance(candidate, ArtifactServiceabilityImpactCandidate)
        and candidate.proposed_source_distribution_available
    ):
        p.unknowns.append(
            ReportUnknown(
                "artifact-impact",
                "Does building the proposed source distribution succeed in the target environment?",
                "A published source distribution is available, but a target source-build outcome was not observed.",
                p.assessments[-1].source_ids,
                "Target installation success or failure through source fallback is not established.",
            )
        )


def _project_python_target(p: _ReportProjection) -> None:
    result = p.result
    target = result.target_python_result
    if target is None:
        p.not_evaluated(
            "target-python",
            "Target Python declaration",
            "target.python",
            "not activated",
        )
    else:
        available = isinstance(target, TargetPythonDeclaration)
        facts = (
            _fact(
                "source", "Target Python source", f"{target.path} @ {target.revision}"
            ),
        )
        if available:
            facts += (
                _fact(
                    "requires_python", "Target requires-python", target.requires_python
                ),
            )
        source = p.source(
            "target_source",
            method="target Python declaration interpretation",
            identity=facts,
            locator=_repository_file_locator(
                result.pull_request.repository, target.revision, target.path
            ),
        )
        p.assess(
            "target-python",
            "Target Python declaration",
            "target.python",
            "available" if available else target.state,
            "A static target Python declaration is available."
            if available
            else target.detail,
            status="available" if available else "problem",
            strength="recorded_fact" if available else "unresolved",
            proposition="Declared Python support, not execution or installation.",
            facts=facts,
            source_ids=(source,),
            question="Which Python versions does the exact target declare?"
            if not available
            else None,
        )
    relevance = result.target_python_relevance_result
    if relevance is None:
        p.not_evaluated(
            "python-relevance", "Target Python relevance", "target.relevance"
        )
    else:
        p.assess(
            "python-relevance",
            "Target Python relevance",
            "target.relevance",
            relevance.state,
            relevance.detail,
            strength="grounded_interpretation"
            if isinstance(
                result.upstream_support_drop_result, GroundedPythonSupportDropClaim
            )
            else "recorded_fact",
            source_ids=tuple(
                ref
                for a in p.assessments
                if a.assessment_id in {"support-drop", "target-python"}
                for ref in a.source_ids
            ),
            proposition="Target declaration overlap with the recorded support-drop interpretation.",
            question="Is the dropped Python line relevant to this target?"
            if relevance.state
            not in {"declared_python_overlap", "outside_declared_python_range"}
            else None,
        )
    impact = result.python_support_drop_impact_result
    if impact is not None:
        p.assess(
            "python-impact",
            "Python support-drop applicability",
            "impact.python_support",
            impact.applicability.state,
            impact.applicability.detail,
            strength="grounded_interpretation",
            source_ids=tuple(
                ref
                for a in p.assessments
                if a.assessment_id
                in {"support-drop", "target-python", "python-relevance"}
                for ref in a.source_ids
            ),
            proposition="Applicability of a grounded interpretation, not independent corroboration or permission to block or merge.",
            question="Is the support-drop interpretation applicable to this target?"
            if impact.applicability.state in {"unresolved", "conflicted"}
            else None,
        )


def _project_semantic_fact(name: str, value: object) -> tuple[ReportFact, ...]:
    """Preserve the selected semantic state at the command scope; do not resolve it again."""
    if isinstance(value, ManagerEnvironmentSelectionFact):
        detail = f"{value.environment.kind}: {value.environment.value}"
    elif isinstance(value, InstallationDestinationFact):
        detail = f"{value.destination.kind}: {value.destination.value}"
    elif isinstance(value, PackageMutationModeFact):
        detail = value.mode
    elif isinstance(value, DirectRequirementHandlingFact):
        detail = value.handling
    else:
        from .dependency.package_manager_semantics import PackageManagerSemanticProblem

        assert isinstance(value, PackageManagerSemanticProblem)
        return (
            _fact(name + "_state", name + " state", value.state),
            _fact(name + "_reason", name + " reason", value.reason),
            _fact(name + "_detail", name + " detail", value.detail),
        )
    return (
        _fact(name, name.replace("_", " ").capitalize(), detail),
        _fact(
            name + "_source", name + " winning source", value.provenance.winning_source
        ),
    )


def _repository_file_locator(repository: str, revision: str, path: str) -> str:
    """Preserve exact file identity when GitHub paths contain URL-significant characters."""
    return f"https://github.com/{repository}/blob/{revision}/{quote(path, safe='/')}"
