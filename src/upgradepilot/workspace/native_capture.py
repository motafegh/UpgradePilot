"""Capture the initial native input/result closure from normal orchestration once.

``investigation.investigate_public_pull_request`` supplies material at its existing native
boundaries. Staging contains immutable encoded bytes, never a projection's live-value cache.
``partial_snapshot`` declares unfinished native progress; ``snapshot`` requires completion.
The generic lifecycle host publishes those boundaries without rerunning native processing.
Legacy report facts remain during the selected consumer migration.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from uuid import uuid4

from ..ci.dependency_exercise import (
    DependencyCICoverageResult,
    WorkflowDependencyCoverageInput,
)
from ..ci.dependency_state import RuntimeDependencyStateResult
from ..ci.job_log_diagnostic import CIJobLogDiagnostic
from ..caller_signature.evidence import SourceAnalysisRun
from ..caller_signature.source_evidence import CallerSignatureSources
from ..caller_signature.source_codec import source_codec_version
from ..dependency.change import DependencyChangeProblem, DependencyVersionChange
from ..dependency.environment import DependencySourceContext
from ..github.pull_request import (
    ChangedFile, PullRequestIdentity, PullRequestDescriptionObservation,
)
from ..github.repository import RepositoryFileEvidence
from ..impact.python_support import (
    PythonSupportDropImpactAssessment,
    PythonSupportDropInvestigationSelection,
)
from ..target.python import TargetPythonEvidence
from ..target.relevance import TargetPythonRelevanceResult
from ..upstream.claim import UpstreamSupportDropClaimResult
from ..upstream.interval import UpstreamIntervalAuthorityResult
from .native_boundary import (
    CapturedNativeBoundary,
    CapturedNativeRecord,
    ExactInvestigationTarget,
    exact_investigation_target,
    validate_native_boundary,
)
from .native_codecs import FAMILY_CONTRACTS, decode_native_value, encode_native_value, family_contract


@dataclass(frozen=True, slots=True)
class _StagedCapture:
    record_id: str
    payload: bytes
    evaluated: bool
    producer_method: str | None
    producer_version: str | None
    retention_gaps: tuple[str, ...]
    input_record_ids: tuple[str, ...]
    codec_version: int


class NativeInvestigationCapture:
    """One opt-in investigation's encoded staging, sealed before consumer reconstruction.

    Native method versions unavailable in older interfaces remain explicit gaps. The
    caller/signature capture methods expose their tested version separately. A codec
    version describes representation support. Capture
    never acquires evidence, invokes an evaluator, retries work or publishes a checkpoint.
    """

    def __init__(self) -> None:
        self._target: ExactInvestigationTarget | None = None
        self._staged: dict[str, _StagedCapture] = {}
        self._sealed: CapturedNativeBoundary | None = None
        self._completed = False

    def start(
        self,
        pull_request: PullRequestIdentity,
        changed_files: tuple[ChangedFile, ...],
        dependency: DependencyVersionChange | DependencyChangeProblem,
        source_contexts: tuple[DependencySourceContext, ...],
        *,
        description: PullRequestDescriptionObservation | None = None,
    ) -> None:
        if self._target is not None:
            raise ValueError(
                "A native capture belongs to one investigation invocation."
            )
        self._target = exact_investigation_target(pull_request, dependency)
        self._record(
            "investigation_inputs",
            {
                "pull_request": pull_request,
                "changed_files": changed_files,
                "dependency_result": dependency,
                "source_contexts": source_contexts,
            },
            method="workspace.native_capture.NativeInvestigationCapture.start",
            gaps=(
                "dependency_analysis_call_metadata_and_unsupplied_source_content_not_retained",
            ),
        )
        # Explicit non-execution differs from a missing record and from an executed selector
        # returning None. These placeholders describe the normal branch's initial state.
        for family in FAMILY_CONTRACTS:
            if family == "investigation_inputs":
                continue
            value = () if family == "ci_inputs" else None
            if family == "target_python":
                value = {"source": None, "result": None}
            self._record(family, value, method=None, evaluated=False)
        if description is not None:
            self._record(
                "pull_request_description", description,
                method="github.pull_request.GitHubPullRequestClient.get_pull_request_observation",
            )

    def _record(
        self,
        family: str,
        value: object,
        *,
        method: str | None,
        evaluated: bool = True,
        gaps: tuple[str, ...] = (),
        version: str | None = None,
        codec_version: int = 1,
    ) -> None:
        if self._target is None or self._sealed is not None:
            raise ValueError("Capture must be started and remain unpublished staging.")
        self._refresh_pending_inputs()
        retained_gaps = gaps
        if evaluated:
            if version is None:
                retained_gaps += ("producer_version_unavailable",)
            if method is None:
                retained_gaps += ("producer_method_unavailable",)
        sources = None
        if family == "caller_signature_comparison":
            source = self._staged["caller_signature_sources"]
            sources = decode_native_value("caller_signature_sources", source.codec_version, source.payload)
        self._staged[family] = _StagedCapture(
            uuid4().hex,
            encode_native_value(family, value, version=codec_version, sources=sources),
            evaluated,
            method,
            version,
            retained_gaps,
            tuple(
                self._staged[name].record_id for name in family_contract(family).inputs
            ),
            codec_version,
        )

    def capture_ci(
        self,
        inputs: tuple[WorkflowDependencyCoverageInput, ...],
        coverage: DependencyCICoverageResult,
        runtime: RuntimeDependencyStateResult,
    ) -> None:
        self._record(
            "ci_inputs", inputs, method="investigation_inputs.prepare_ci_evidence"
        )
        self._record(
            "ci_coverage",
            coverage,
            method="ci.dependency_exercise.evaluate_dependency_ci_coverage",
            codec_version=2,
        )
        self._record(
            "runtime_dependency_state",
            runtime,
            method="ci.dependency_state.evaluate_runtime_dependency_state",
        )

    def capture_ci_job_log(self, observation: CIJobLogDiagnostic) -> None:
        """Record one opt-in typed job-log observation at the existing PR target."""
        assert self._target is not None
        if (
            observation.repository != self._target.repository
            or observation.head_sha != self._target.head_sha
        ):
            raise ValueError("CI job-log observation belongs to a different target.")
        contract = family_contract("ci_job_log_diagnostic")
        self._record(
            "ci_job_log_diagnostic", observation,
            method=contract.producer_method, version=contract.producer_version,
            gaps=("full_raw_job_log_not_retained", "same_process_module_identity_not_observed"),
        )

    def capture_caller_signature_sources(self, sources: CallerSignatureSources) -> None:
        """Capture actual retained acquisition progress, independently of analysis."""
        codec_version = source_codec_version(sources)
        contract = family_contract("caller_signature_sources", codec_version)
        self._record("caller_signature_sources", sources,
                     method=contract.producer_method, version=contract.producer_version,
                     codec_version=codec_version)

    def capture_caller_signature_comparison(self, run: SourceAnalysisRun) -> None:
        """Retain the observed run state; failed analysis is still a recorded operation."""
        contract = FAMILY_CONTRACTS["caller_signature_comparison"]
        self._record("caller_signature_comparison", run,
                     method=contract.producer_method, version=contract.producer_version)

    def capture_upstream_authority(
        self, authority: UpstreamIntervalAuthorityResult
    ) -> None:
        self._record(
            "upstream_authority",
            authority,
            method="upstream.interval.assemble_upstream_interval_authority",
        )

    def capture_upstream_claim(
        self, claim: UpstreamSupportDropClaimResult, evaluator: object
    ) -> None:
        module = getattr(evaluator, "__module__", None)
        name = getattr(evaluator, "__qualname__", None)
        method = (
            f"{module}.{name}" if type(module) is str and type(name) is str else None
        )
        self._record(
            "upstream_support_drop",
            claim,
            method=method,
            gaps=("interpretation_call_metadata_not_retained",),
        )

    def capture_python_pre(
        self,
        assessment: PythonSupportDropImpactAssessment,
        selection: PythonSupportDropInvestigationSelection | None,
    ) -> None:
        self._record(
            "python_support_pre_assessment",
            assessment,
            method="impact.python_support.evaluate_python_support_drop_impact",
        )
        self._record(
            "python_support_selection",
            selection,
            method="impact.python_support.select_python_support_drop_investigation",
        )

    def capture_target(
        self, source: RepositoryFileEvidence, result: TargetPythonEvidence
    ) -> None:
        self._record(
            "target_python",
            {"source": source, "result": result},
            method="target.python.interpret_target_python_declaration",
        )

    def capture_relevance(self, result: TargetPythonRelevanceResult) -> None:
        self._record(
            "target_relevance",
            result,
            method="target.relevance.evaluate_target_python_relevance",
        )

    def capture_python_post(
        self, result: PythonSupportDropImpactAssessment, *, reevaluated: bool
    ) -> None:
        method = (
            "impact.python_support.evaluate_python_support_drop_impact"
            if reevaluated
            else "investigation.investigate_public_pull_request"
        )
        self._record("python_support_post_assessment", result, method=method)

    def _refresh_pending_inputs(self) -> None:
        for family in self._staged:
            item = self._staged[family]
            inputs = tuple(
                self._staged[name].record_id for name in family_contract(family).inputs
            )
            if inputs != item.input_record_ids and not item.evaluated:
                self._staged[family] = _StagedCapture(
                    uuid4().hex,
                    item.payload,
                    False,
                    None,
                    None,
                    item.retention_gaps,
                    inputs,
                    item.codec_version,
                )

    def partial_snapshot(self) -> CapturedNativeBoundary:
        """Declare current coherent progress without completing or sealing the invocation.

        Unperformed placeholders follow current input identities and receive new identities
        when those references change. Executed results keep their actual captured inputs;
        replacing those inputs requires an owner-supplied successor result, never rebinding.
        """
        if self._sealed is not None:
            return self._sealed
        if self._target is None:
            raise ValueError("Capture has not started.")
        self._refresh_pending_inputs()
        records = []
        for family in self._staged:
            item = self._staged[family]
            contract = family_contract(family)
            records.append(
                CapturedNativeRecord(
                    record_id=item.record_id,
                    family=family,
                    owner=contract.owner,
                    codec_version=item.codec_version,
                    target=self._target,
                    input_record_ids=item.input_record_ids,
                    payload=item.payload,
                    payload_digest=sha256(item.payload).hexdigest(),
                    outcome="recorded" if item.evaluated else "not_evaluated",
                    producer_method=item.producer_method,
                    producer_version=item.producer_version,
                    retention_gaps=item.retention_gaps,
                )
            )
        boundary = CapturedNativeBoundary(self._target, tuple(records))
        validate_native_boundary(boundary, expected_target=self._target)
        return boundary

    def snapshot(self) -> CapturedNativeBoundary:
        """Return only the completed sealed capture; partial publication is explicit."""
        if not self._completed:
            raise ValueError(
                "No completed normal investigation has sealed this capture."
            )
        if self._sealed is None:
            self._sealed = self.partial_snapshot()
        return self._sealed

    def complete(self) -> None:
        """Seal only after normal orchestration completes; failed staging is not recovery."""
        self._completed = True
        self.snapshot()
