"""Capture the initial native input/result closure from normal orchestration once.

``investigation.investigate_public_pull_request`` supplies material at its existing native
boundaries. Staging contains immutable encoded bytes, never a projection's live-value cache.
``snapshot`` seals one coherent native boundary; publication is a separate responsibility.
The current report return type remains unchanged until the selected consumer cutover.
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
from ..dependency.change import DependencyChangeProblem, DependencyVersionChange
from ..dependency.environment import DependencySourceContext
from ..github.pull_request import ChangedFile, PullRequestIdentity
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
from .native_codecs import FAMILY_CONTRACTS, encode_native_value


@dataclass(frozen=True, slots=True)
class _StagedCapture:
    record_id: str
    payload: bytes
    evaluated: bool
    producer_method: str | None
    retention_gaps: tuple[str, ...]


class NativeInvestigationCapture:
    """One opt-in investigation's encoded staging, sealed before consumer reconstruction.

    Native method versions unavailable in today's interfaces remain explicit gaps. Codec
    version 1 is representation support, not a fabricated semantic/model version. Capture
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

    def _record(
        self,
        family: str,
        value: object,
        *,
        method: str | None,
        evaluated: bool = True,
        gaps: tuple[str, ...] = (),
    ) -> None:
        if self._target is None or self._sealed is not None:
            raise ValueError("Capture must be started and remain unpublished staging.")
        retained_gaps = gaps
        if evaluated:
            retained_gaps += ("producer_version_unavailable",)
            if method is None:
                retained_gaps += ("producer_method_unavailable",)
        self._staged[family] = _StagedCapture(
            uuid4().hex,
            encode_native_value(family, value),
            evaluated,
            method,
            retained_gaps,
        )

    def capture_ci(
        self,
        inputs: tuple[WorkflowDependencyCoverageInput, ...],
        coverage: DependencyCICoverageResult,
        runtime: RuntimeDependencyStateResult,
    ) -> None:
        self._record(
            "ci_inputs", inputs, method="investigation.investigate_public_pull_request"
        )
        self._record(
            "ci_coverage",
            coverage,
            method="ci.dependency_exercise.evaluate_dependency_ci_coverage",
        )
        self._record(
            "runtime_dependency_state",
            runtime,
            method="ci.dependency_state.evaluate_runtime_dependency_state",
        )

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

    def snapshot(self) -> CapturedNativeBoundary:
        if self._sealed is not None:
            return self._sealed
        if self._target is None or not self._completed:
            raise ValueError(
                "No completed normal investigation has sealed this capture."
            )
        records = []
        for family, item in self._staged.items():
            contract = FAMILY_CONTRACTS[family]
            records.append(
                CapturedNativeRecord(
                    record_id=item.record_id,
                    family=family,
                    owner=contract.owner,
                    codec_version=1,
                    target=self._target,
                    input_record_ids=tuple(
                        self._staged[name].record_id for name in contract.inputs
                    ),
                    payload=item.payload,
                    payload_digest=sha256(item.payload).hexdigest(),
                    outcome="recorded" if item.evaluated else "not_evaluated",
                    producer_method=item.producer_method,
                    producer_version=None,
                    retention_gaps=item.retention_gaps,
                )
            )
        boundary = CapturedNativeBoundary(self._target, tuple(records))
        validate_native_boundary(boundary, expected_target=self._target)
        self._sealed = boundary
        return self._sealed

    def complete(self) -> None:
        """Seal only after normal orchestration completes; failed staging is not recovery."""
        self._completed = True
        self.snapshot()
