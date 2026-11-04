"""Explicit projection of owned investigation facts into the shared report contract.

Read ``project_investigation_report`` for full results, ``project_ci_report`` for
admitted CI-only inputs, or ``project_caller_signature_report`` for native source-only
evidence, then their shared evidence-family mapping. No dataclass
reflection, domain reparsing, network acquisition or new impact/action inference occurs.
Each assessment cites its producer result; retained upstream text has its own exact source.
Absent inputs stay explicit, and an empty candidate horizon never becomes absence of risk.
"""

from __future__ import annotations

from datetime import UTC, datetime
from hashlib import sha256
from importlib.metadata import PackageNotFoundError, version
from urllib.parse import quote
from uuid import uuid4

from .caller_signature.evidence import SourceAnalysisRun, SourceAnalysisResult
from .caller_signature.source_evidence import CallerSignatureSources
from .ci.dependency_exercise import DependencyCICoverageResult
from .ci.dependency_state import (
    RequirementSatisfiedAtCommandCompletion,
    RuntimeDependencyStateResult,
)
from .dependency.change import DependencyChangeProblem, DependencyVersionChange
from .dependency.package_manager_semantics import (
    DirectRequirementHandlingFact,
    InstallationDestinationFact,
    ManagerEnvironmentSelectionFact,
    PackageMutationModeFact,
)
from .github.actions import WorkflowJob, WorkflowRun
from .github.changelog import ChangelogPathDiscoveryProblem
from .github.pull_request import PullRequestIdentity
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
    CIReport,
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
from .workspace.native_boundary import CapturedNativeBoundary, exact_investigation_target
from .workspace.native_projection import (
    CallerSignatureNativeProjection, reconstruct_caller_signature_projection, reconstruct_pull_request_description,
)
from .workspace.native_representation import NativeReconstructionError


def _fact(name: str, label: str, value: object) -> ReportFact:
    return ReportFact(name, label, str(value) if value is not None else "not recorded")


class _ReportEvidence:
    """Shared invocation-local report accumulation, independent of application scope."""

    def __init__(self) -> None:
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


class _ReportProjection(_ReportEvidence):
    """Full-report context; the partial CI route never fabricates this application result."""

    def __init__(self, result: PublicPullRequestInvestigation) -> None:
        super().__init__()
        self.result = result


def project_ci_report(
    *,
    pull_request: PullRequestIdentity,
    dependency_result: DependencyVersionChange | DependencyChangeProblem,
    workflow_evidence: tuple[tuple[WorkflowRun, tuple[WorkflowJob, ...]], ...],
    ci_coverage_result: DependencyCICoverageResult | None,
    runtime_dependency_state_result: RuntimeDependencyStateResult | None,
) -> CIReport:
    """Copy admitted CI-native fields through the full report's single CI mapping.

    The normal partial caller is a validated CINativeProjection. Its reconstruction
    owns material/target validity; this function neither revalidates that boundary nor
    evaluates domains. None means no evaluated result, not absent risk. No full
    investigation, model interpretation or maintainer synthesis is needed or invented.
    """
    p = _ReportEvidence()
    _project_ci(
        p, pull_request=pull_request, workflow_evidence=workflow_evidence,
        ci_coverage_result=ci_coverage_result,
        runtime_dependency_state_result=runtime_dependency_state_result,
    )
    identity = _pull_request_identity(pull_request)
    if isinstance(dependency_result, DependencyVersionChange):
        identity += (
            _fact("package", "Dependency", dependency_result.normalized_package),
            _fact("old_version", "Old version", dependency_result.old_version),
            _fact("proposed_version", "Proposed version", dependency_result.proposed_version),
        )
    else:
        identity += (_fact("dependency_problem", "Dependency transition problem", dependency_result.reason),)
    return CIReport(
        identity, tuple(p.assessments), tuple(p.findings), tuple(p.unknowns),
        tuple(p.sources),
        (
            "Recorded CI owner results only; no live refresh or new domain evaluation.",
            "Static declarations, correlated execution and command-completion state retain different scopes.",
            "This view establishes neither whole-update compatibility nor maintainer-action permission.",
            "Source references do not retain original raw inputs; capture provenance/gaps belong to the supplying boundary.",
        ),
    )


def _pull_request_identity(pr: PullRequestIdentity) -> tuple[ReportFact, ...]:
    return (
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
    identity = _pull_request_identity(pr)
    pr_source = _project_pull_request_source(p, identity)
    _project_dependency(p, pr_source)
    _project_ci(
        p, pull_request=pr, workflow_evidence=result.workflow_evidence,
        ci_coverage_result=result.ci_coverage_result,
        runtime_dependency_state_result=result.runtime_dependency_state_result,
    )
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
        "2",
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


def _project_pull_request_source(
    p: _ReportProjection, identity: tuple[ReportFact, ...]
) -> str:
    """Attribute a source from Workspace without promoting copied text to a finding.

    Only unsupported decoding is optional unavailability. Corruption, substituted inputs
    and target mismatch must reach the caller as an integrity failure.
    """
    result = p.result
    description = None
    state = "not_recorded"
    limitation = "PR description was not recorded in this investigation."
    if result.workspace_revision is not None:
        try:
            description = reconstruct_pull_request_description(
                result.workspace_revision.boundary,
                expected_target=exact_investigation_target(
                    result.pull_request, result.dependency_result
                ),
            )
        except NativeReconstructionError as exc:
            if exc.reason not in {
                "unsupported_native_codec", "unsupported_native_semantic_version"
            }:
                raise
            state = "unsupported"
            limitation = f"PR description unavailable: {exc.reason}."
    if description is not None:
        state = description.state
        limitation = (
            f"Initial PR body observation: {state}; retention bound 262144 UTF-8 bytes. "
            "PR-authored/copied context is unverified; upstream coverage is unassessed. "
            "Later PR edits are not refreshed; this source grants no finding or action permission."
        )
        identity += (
            _fact("description_source_url", "Observed API source", description.source_url),
            _fact("description_utf8_bytes", "Description UTF-8 bytes", description.utf8_bytes),
            _fact("description_sha256", "Description SHA-256", description.content_sha256),
        )
    identity += (_fact("description_state", "PR description state", state),)
    return p.source(
        "pull_request",
        locator=f"https://github.com/{result.pull_request.repository}/pull/{result.pull_request.number}",
        identity=identity,
        method="exact PR base/head identity acquisition; initial PR body observation",
        content=description.text if description is not None else None,
        retrieved_at=description.observed_at.isoformat() if description is not None else None,
        limitation=limitation,
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


def _project_ci(
    p: _ReportEvidence, *, pull_request: PullRequestIdentity,
    workflow_evidence: tuple[tuple[WorkflowRun, tuple[WorkflowJob, ...]], ...],
    ci_coverage_result: DependencyCICoverageResult | None,
    runtime_dependency_state_result: RuntimeDependencyStateResult | None,
) -> None:
    run_refs = []
    for run, jobs in workflow_evidence:
        run_refs.append(
            p.source(
                "workflow_execution",
                method="exact-head run and captured-attempt jobs acquisition",
                locator=f"https://github.com/{pull_request.repository}/actions/runs/{run.run_id}/attempts/{run.run_attempt}",
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
    ci = ci_coverage_result
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
                    pull_request.repository,
                    pull_request.head_sha,
                    workflow.workflow_path,
                ),
                identity=(
                    _fact("path", "Workflow path", workflow.workflow_path),
                    _fact("revision", "Static revision", pull_request.head_sha),
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
                # These are retained diagnostics, not an unconditional witness or
                # evidence that the encountered conditions can hold together.
                if consumption.conditional_candidate_path:
                    facts.append(
                        _fact(
                            f"conditional_path_{j}",
                            "Conditional reachability candidate (diagnostic only)",
                            " -> ".join(consumption.conditional_candidate_path),
                        )
                    )
                facts.extend(
                    _fact(
                        f"unresolved_condition_{j}_{k}",
                        "Unevaluated reachability condition",
                        condition,
                    )
                    for k, condition in enumerate(consumption.unresolved_conditions, 1)
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
    runtime = runtime_dependency_state_result
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
                pull_request.repository, c.workflow_revision, c.workflow_path
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
        # An empty association result cannot mean the candidate branch was skipped.
        candidate_established = isinstance(
            candidate, ArtifactServiceabilityImpactCandidate
        )
        p.not_evaluated(
            "artifact-environments",
            "Target artifact environments",
            "target.artifact_environment",
            "not established" if candidate_established else "not activated",
            detail=(
                "An artifact capability-change candidate was established, but the "
                "investigation retains no supported target environment associations. "
                "Applicability to the target remains unresolved."
                if candidate_established
                else "This branch has no evaluated result in the recorded investigation."
            ),
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


def project_caller_signature_report(
    boundary: CapturedNativeBoundary, *, auth_mode: str = "anonymous",
    now: datetime | None = None,
) -> InvestigationReport:
    """Deliver recorded source comparisons with their exact text and unresolved premises.

    Native reconstruction owns source/result integrity. This mapping groups witnesses
    by their recorded root identities without discovering new paths or comparing
    arguments. Newly generated action remains owned by the abstention-only synthesis.
    Recovery decodes the retained report instead of calling this function.
    """
    if auth_mode not in {"anonymous", "token-env"}:
        raise ValueError("unsupported declared authentication mode")
    produced = now or datetime.now(UTC)
    if produced.tzinfo is None or produced.utcoffset() is None:
        raise ValueError("report generation time must be timezone-aware")
    native = reconstruct_caller_signature_projection(boundary, expected_target=boundary.target)
    p = _ReportEvidence()
    inputs = native.inputs
    description = reconstruct_pull_request_description(boundary, expected_target=boundary.target)
    pr_source = p.source(
        "pull_request", locator=f"https://github.com/{inputs.pull_request.repository}/pull/{inputs.pull_request.number}",
        identity=(
            _fact("description_state", "Description observation state", description.state),
            _fact("description_sha256", "Description SHA-256", description.content_sha256),
            _fact("description_bytes", "Description UTF-8 bytes", description.utf8_bytes),
        ) if description else (),
        method="initial exact PR observation",
        content=description.text if description else None,
        retrieved_at=description.observed_at.isoformat() if description else None,
        limitation="PR-authored context is unverified and later edits are not refreshed.",
    )
    dependency = inputs.dependency_result
    supported = isinstance(dependency, DependencyVersionChange)
    p.assess(
        "dependency", "Dependency change", "dependency.change",
        "supported" if supported else "unsupported",
        "One exact dependency transition was recorded." if supported else dependency.detail,
        status="available" if supported else "problem",
        reason="recorded_owner_result" if supported else dependency.reason,
        strength="recorded_fact" if supported else "unresolved",
        proposition="The dependency change describes source declarations, not installed state.",
        source_ids=(pr_source,),
        facts=tuple(_fact(name, name.replace("_", " ").capitalize(), getattr(dependency, name))
                    for name in ("package", "normalized_package", "old_version", "proposed_version")) if supported else (),
    )
    for identity, topic in (
        ("ci", "CI dependency coverage"), ("runtime", "Runtime dependency state"),
        ("package", "Package evidence"), ("old-package", "Old package artifact evidence"),
        ("upstream-repository", "Upstream repository"), ("upstream-interval", "Upstream interval"),
        ("support-drop", "Python support drop"), ("artifact-candidate", "Artifact serviceability candidate"),
        ("artifact-impact", "Artifact applicability"), ("target-python", "Target Python declaration"),
        ("python-relevance", "Python relevance"),
    ):
        p.not_evaluated(identity, topic, "caller-signature profile",
                        detail=f"The full {topic.lower()} branch was not evaluated by this source-only profile. "
                        "Source association receipts may retain separate package/repository premises.")

    file_sources, producer_sources = _project_caller_signature_text(p, boundary, native)
    refs = producer_sources or (pr_source,)
    _project_caller_signature_coverage(p, native.sources, refs, file_sources)
    _project_caller_signature_analysis(p, native.comparison, refs, file_sources)
    synthesis = synthesize_maintainer_action(native)
    try:
        product_version = version("upgradepilot")
    except PackageNotFoundError:
        product_version = None
    return InvestigationReport(
        str(uuid4()), produced.astimezone(UTC).isoformat(), "3", product_version, auth_mode,
        ("Explicit caller-signature profile uses bounded static source evidence.",
         "CI/runtime-state, semantic interpretation and applicability were not evaluated by this invocation."),
        _pull_request_identity(inputs.pull_request), tuple(p.assessments), tuple(p.findings), tuple(p.unknowns),
        ReportAction(synthesis.action, synthesis.decisive_reasons, synthesis.residual_uncertainty,
                     synthesis.limitations, synthesis.claim_limits), tuple(p.sources),
        ("Only admitted original source text is retained. Omitted or unavailable files cannot be opened.",
         "The native producer sources preserve full receipts, costs, paths, traces, gaps and admission limits.",
         "Report delivery and original source text do not establish installed behavior or authorize a maintainer action."),
    )


def _project_caller_signature_text(p: _ReportEvidence, boundary: CapturedNativeBoundary,
                                 native: CallerSignatureNativeProjection) -> tuple[dict[str, str], tuple[str, ...]]:
    # Exact native receipts/results are producer sources, with original text kept in
    # separate source entries. This preserves full costs, traces and gap details even
    # where the human summary is intentionally shorter than the native representation.
    producer_sources = tuple(
        p.source("producer_assessment", method=record.producer_method or record.owner,
                 content=record.payload.decode("utf-8"),
                 identity=(_fact("family", "Native family", record.family),
                           _fact("record_id", "Native record", record.record_id)),
                 limitation="Recorded native producer evidence, including its original limits and gaps.")
        for record in boundary.records
        if record.family in {"caller_signature_sources", "caller_signature_comparison"}
        and record.outcome == "recorded"
    )
    sources = native.sources
    file_sources: dict[str, str] = {}
    if sources and sources.catalog:
        catalog = sources.catalog
        scopes = {scope.source_id: scope for scope in catalog.scopes}
        modules = {(m.source_id, m.path): m for m in sources.modules}
        for file in catalog.files:
            descriptor = catalog.descriptor(file)
            scope = scopes[file.source_id]
            module = modules.get((file.source_id, file.path))
            file_sources[descriptor["file_id"]] = p.source(
                "target_source" if scope.repository == boundary.target.repository else "dependency_source",
                locator=_repository_file_locator(scope.repository, scope.revision, file.path),
                identity=tuple(_fact(name, label, value) for name, label, value in (
                    ("file_id", "File identity", descriptor["file_id"]),
                    ("source_id", "Catalog scope", file.source_id),
                    ("repository", "Repository", scope.repository), ("revision", "Revision", scope.revision),
                    ("path", "Path", file.path), ("sha256", "Content SHA-256", descriptor["content_sha256"]),
                    ("role", "Source role", module.role if module else "retained_non_python"),
                    ("package", "Package", module.package if module else None),
                    ("version", "Version", module.version if module else None),
                    ("coverage", "Coverage", scope.coverage_limit),
                    ("acquisition_snapshot_at", "Acquisition snapshot time",
                     sources.acquisition.observed_at.isoformat() if sources.acquisition.observed_at else None),
                )),
                method=scope.capture_basis, content=file.content,
                retrieved_at=None,
                limitation=scope.coverage_limit + " Retained text does not prove examination or runtime binding.",
            )
    return file_sources, producer_sources


def _project_caller_signature_coverage(p: _ReportEvidence, sources: CallerSignatureSources | None,
                                     refs: tuple[str, ...], file_sources: dict[str, str]) -> None:
    if sources is None:
        p.not_evaluated("caller-signature-coverage", "Caller/signature source coverage", "caller_signature.acquisition")
    else:
        receipt = sources.acquisition
        coverage_facts = [
            _fact("source_files", "Retained source files", len(file_sources)),
            _fact("module_receipts", "Module source receipts", len(receipt.module_requests)),
            _fact("unexamined_modules", "Unexamined acquisition modules", len(receipt.unexamined_modules)),
            _fact("material_omissions", "Material omissions", len(receipt.material_omissions)),
        ]
        if receipt.transport:
            transport = receipt.transport
            coverage_facts.extend((
                _fact("github_requests", "GitHub requests", transport.github_requests),
                _fact("provider_requests", "All-provider requests", transport.provider_requests),
                _fact("body_bytes", "Received body bytes", transport.decoded_body_bytes),
                _fact("elapsed_hex", "Acquisition seconds (exact float)", transport.elapsed.seconds_hex),
            ))
        p.assess("caller-signature-coverage", "Caller/signature source coverage", "caller_signature.acquisition",
                 receipt.state, "Coverage applies only to the admitted retained acquisition horizon.",
                 status="problem" if receipt.state == "failed" else "available",
                 proposition="Captured material and acquisition omissions are recorded, not exhaustive repository coverage.",
                 facts=tuple(coverage_facts), source_ids=refs,
                 limitations=receipt.retention_gaps + receipt.adapter_limitations,
                 question="Which omitted or unexamined source could change the candidate horizon?")


def _project_caller_signature_analysis(p: _ReportEvidence, run: SourceAnalysisRun | None,
                                     refs: tuple[str, ...], file_sources: dict[str, str]) -> None:
    if run is None:
        p.not_evaluated("caller-signature-analysis", "Caller/signature analysis", "caller_signature.worker")
    else:
        result = run.result
        facts = [_fact("elapsed_hex", "Worker seconds (exact float)", run.elapsed.seconds_hex),
                 _fact("input_sha256", "Exact analysis input", run.input_sha256)]
        if result:
            facts.extend((
                _fact("distinct_roots", "Distinct target roots", len({c.root_call_id for c in result.candidates})),
                _fact("witnesses", "Conditional comparison witnesses", len(result.candidates)),
                _fact("unexamined_units", "Unexamined retained units", sum(u.coverage == "unexamined" for u in result.units)),
                _fact("gaps", "Discovery gaps", len(result.gaps)),
                _fact("source_bytes", "Analyzed source bytes", result.work.source_bytes),
                _fact("states_examined", "Correspondence states examined", result.work.states_examined),
                _fact("gaps_omitted", "Omitted gap diagnostics", result.work.gaps_omitted),
            ))
        p.assess("caller-signature-analysis", "Caller/signature analysis", "caller_signature.worker",
                 run.state, run.problem_detail or "Recorded bounded source analysis completed with its original coverage.",
                 reason=run.reason or "recorded_owner_result", status="available" if result else "problem",
                 proposition="Completion records producer execution, independently of coverage or compatibility.",
                 facts=tuple(facts), source_ids=refs,
                 limitations=("Unexamined retained text and no candidates are not absence-of-exposure proof.",),
                 question="What installed version, import binding and runtime dispatch make these conditional witnesses applicable?")
        if result:
            _project_caller_signature_witnesses(p, result, refs, file_sources)


def _project_caller_signature_witnesses(p: _ReportEvidence, result: SourceAnalysisResult,
                                      refs: tuple[str, ...], file_sources: dict[str, str]) -> None:
    calls = {c.fact_id: c for u in result.units if u.facts for c in u.facts.calls}
    signatures = {s.fact_id: s for u in result.units if u.facts for s in u.facts.signatures}
    for candidate in result.candidates:
        comparison = candidate.comparison
        root, call, signature = calls[candidate.root_call_id], calls[comparison.call_id], signatures[comparison.signature_id]
        path_units = tuple(dict.fromkeys((root.unit_id, call.unit_id, signature.unit_id,
                                          *(step.unit_id for step in candidate.steps))))
        candidate_refs = tuple(file_sources[uid] for uid in path_units)
        witness = candidate.callee_role
        detail = (f"Root {candidate.root_call_id}, witness {candidate.candidate_id}: "
                  f"{witness.role} {witness.package}=={witness.version} receives {call.expression} "
                  f"at {signature.qualified_name}: {comparison.outcome}. Conditional source evidence.")
        candidate_facts = [
            _fact("root_call_id", "Target root", candidate.root_call_id),
            _fact("root_location", "Target root source", f"{file_sources[root.unit_id]} L{root.span.line} {root.expression}"),
            _fact("witness_id", "Witness", candidate.candidate_id),
            _fact("caller", "Compared call", f"{file_sources[call.unit_id]} L{call.span.line} {call.expression}"),
            _fact("callee", "Selected signature", f"{file_sources[signature.unit_id]} L{signature.span.line} {signature.qualified_name}"),
            _fact("role", "Callee role", witness.role), _fact("version", "Callee version", witness.version),
            _fact("receiver", "Receiver assumption", comparison.receiver_mode),
            _fact("checks_complete", "Local checks complete", comparison.checks_complete),
        ]
        if root.binding:
            binding = root.binding
            candidate_facts.extend((
                _fact("root_binding", "Root binding state", binding.state),
                _fact("root_origins", "Possible imported origins", ", ".join(binding.possible_imports)),
                _fact("root_unknown", "Unknown binding possible", binding.unknown_possible),
                _fact("root_unbound", "Unbound possible", binding.unbound_possible),
            ))
        candidate_facts.extend(_fact(f"path_{i}", "Path step",
            f"{file_sources[step.unit_id]} L{step.span.line}:{step.span.column} "
            f"{step.operation} {step.expression}") for i, step in enumerate(candidate.steps))
        candidate_facts.extend(_fact(f"keyword_{i}", "Keyword reception", f"{k.name}: {k.outcome}")
                               for i, k in enumerate(comparison.keyword_reception))
        candidate_facts.extend(_fact(f"violation_{i}", "Local violation", f"{v.reason}: {v.parameter}")
                               for i, v in enumerate(comparison.violations))
        p.assess("caller-signature-comparison-" + sha256(candidate.candidate_id.encode()).hexdigest(),
                 "Conditional caller/signature witness", "caller_signature.analysis", comparison.outcome,
                 detail, proposition="Only the selected source-level argument reception is established under recorded premises.",
                 facts=tuple(candidate_facts), source_ids=refs + candidate_refs,
                 limitations=candidate.premises + comparison.remaining_premises + comparison.unresolved_checks)
