"""Native LangGraph workflow for one bounded EvidenceGapPlanner turn.

This module owns the LangGraph-side workflow communication model. It deliberately does not import
ordinary-Python planner/admission representations. The ordinary-Python implementation may be used
behind narrow comparison adapters, but those adapters must map into the LangGraph-owned outcomes
defined here.

Product/domain owners remain reusable directly: real investigation state, Python-support impact,
exact repository acquisition contracts, target declaration interpretation, and target relevance.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Callable, Literal, Protocol, TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.runtime import Runtime
from langgraph.types import Command

from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github.repository import RepositoryFileEvidence
from upgradepilot.impact.python_support import (
    PythonSupportDropImpactAssessment,
    PythonSupportDropInvestigationSelection,
    evaluate_python_support_drop_impact,
)
from upgradepilot.investigation import PublicPullRequestInvestigation
from upgradepilot.target.python import TargetPythonEvidence, interpret_target_python_declaration
from upgradepilot.target.relevance import evaluate_target_python_relevance


EvidenceGapLangGraphContinuationStatus = Literal[
    "ACTIVE",
    "SETTLED",
    "OUTSIDE_CURRENT_BOUNDARY",
    "NO_JUSTIFIED_INVESTIGATION",
]
EvidenceGapLangGraphNoActionKind = Literal[
    "QUESTION_SETTLED",
    "KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY",
    "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED",
]
EvidenceGapLangGraphProviderProblemReason = Literal[
    "provider_request_failed",
    "provider_http_error",
    "provider_response_malformed",
    "completion_truncated",
    "structured_output_invalid",
]
EvidenceGapLangGraphAuthorityRejectionReason = Literal[
    "unknown_action",
    "action_consumed",
    "budget_exhausted",
    "action_identity_stale",
    "action_not_allowed_by_policy",
    "action_not_currently_actionable",
]
EvidenceGapLangGraphOutcomeKind = Literal[
    "no_action",
    "provider_problem",
    "authority_rejected",
    "semantic_result",
    "operational_failure",
]
EvidenceGapLangGraphOperationalFailureType = Literal[
    "GitHubAcquisitionError",
    "GitHubResponseError",
]


@dataclass(frozen=True, slots=True)
class EvidenceGapLangGraphStartInput:
    """Trusted caller input for one bounded graph turn before model invocation."""

    investigation: PublicPullRequestInvestigation
    planning_question: str
    consumed_actions: tuple[str, ...] = ()
    remaining_investigations: int = 1
    continuation_status: EvidenceGapLangGraphContinuationStatus = "ACTIVE"

    def __post_init__(self) -> None:
        if not isinstance(self.investigation, PublicPullRequestInvestigation):
            raise TypeError("investigation must be PublicPullRequestInvestigation.")
        _require_trimmed(self.planning_question, "planning_question")
        _validate_orchestration_values(
            self.consumed_actions,
            self.remaining_investigations,
            self.continuation_status,
        )
        if self.continuation_status != "ACTIVE":
            raise ValueError("a new bounded graph turn requires ACTIVE continuation status.")


@dataclass(frozen=True, slots=True)
class EvidenceGapLangGraphActionProposal:
    """Untrusted model proposal expressed in LangGraph workflow language."""

    action_id: str
    explanation: str

    def __post_init__(self) -> None:
        _require_trimmed(self.action_id, "action_id")
        _require_trimmed(self.explanation, "explanation")


@dataclass(frozen=True, slots=True)
class EvidenceGapLangGraphNoAction:
    """One explicit bounded planner outcome where no investigation should execute."""

    decision_kind: EvidenceGapLangGraphNoActionKind
    explanation: str

    def __post_init__(self) -> None:
        if self.decision_kind not in {
            "QUESTION_SETTLED",
            "KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY",
            "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED",
        }:
            raise ValueError("no-action decision kind is unsupported.")
        _require_trimmed(self.explanation, "explanation")


@dataclass(frozen=True, slots=True)
class EvidenceGapLangGraphProviderProblem:
    """Expected provider/structured-output problem before a usable planner outcome exists."""

    reason: EvidenceGapLangGraphProviderProblemReason
    detail: str

    def __post_init__(self) -> None:
        if self.reason not in {
            "provider_request_failed",
            "provider_http_error",
            "provider_response_malformed",
            "completion_truncated",
            "structured_output_invalid",
        }:
            raise ValueError("provider problem reason is unsupported.")
        _require_trimmed(self.detail, "provider problem detail")


type EvidenceGapLangGraphPlannerOutcome = (
    EvidenceGapLangGraphActionProposal
    | EvidenceGapLangGraphNoAction
    | EvidenceGapLangGraphProviderProblem
)


@dataclass(frozen=True, slots=True)
class EvidenceGapLangGraphBaseline:
    """One coherent semantic baseline from which final turn consequences are applied."""

    python_support_assessment: PythonSupportDropImpactAssessment
    consumed_actions: tuple[str, ...]
    remaining_investigations: int
    continuation_status: EvidenceGapLangGraphContinuationStatus = "ACTIVE"

    def __post_init__(self) -> None:
        if not isinstance(self.python_support_assessment, PythonSupportDropImpactAssessment):
            raise TypeError(
                "python_support_assessment must be PythonSupportDropImpactAssessment."
            )
        _validate_orchestration_values(
            self.consumed_actions,
            self.remaining_investigations,
            self.continuation_status,
        )


@dataclass(frozen=True, slots=True)
class EvidenceGapLangGraphAuthoritySnapshot:
    """Current post-planner product/orchestration snapshot used for authority and consequences.

    The graph owns this communication value. It carries product-owned current selection and impact
    state rather than embedding the ordinary-Python ``EvidenceGapAdmissionState`` representation.
    """

    baseline: EvidenceGapLangGraphBaseline
    current_selection: PythonSupportDropInvestigationSelection | None

    def __post_init__(self) -> None:
        if self.baseline.continuation_status != "ACTIVE":
            raise ValueError("fresh authority snapshot requires an ACTIVE consequence baseline.")
        if self.current_selection is not None and not isinstance(
            self.current_selection,
            PythonSupportDropInvestigationSelection,
        ):
            raise TypeError(
                "current_selection must be PythonSupportDropInvestigationSelection or None."
            )


@dataclass(frozen=True, slots=True)
class EvidenceGapLangGraphAuthorizedAction:
    """Exact read-only action authorized for the effect boundary."""

    action_id: str
    repository: str
    revision: str
    path: str
    explanation: str

    def __post_init__(self) -> None:
        for name, value in (
            ("action_id", self.action_id),
            ("repository", self.repository),
            ("revision", self.revision),
            ("path", self.path),
            ("explanation", self.explanation),
        ):
            _require_trimmed(value, name)


@dataclass(frozen=True, slots=True)
class EvidenceGapLangGraphAuthorityRejection:
    """Why the proposed action must not execute under the current authority snapshot."""

    reason: EvidenceGapLangGraphAuthorityRejectionReason
    action_id: str
    detail: str

    def __post_init__(self) -> None:
        if self.reason not in {
            "unknown_action",
            "action_consumed",
            "budget_exhausted",
            "action_identity_stale",
            "action_not_allowed_by_policy",
            "action_not_currently_actionable",
        }:
            raise ValueError("authority rejection reason is unsupported.")
        _require_trimmed(self.action_id, "action_id")
        _require_trimmed(self.detail, "authority rejection detail")


type EvidenceGapLangGraphAuthorityOutcome = (
    EvidenceGapLangGraphAuthorizedAction | EvidenceGapLangGraphAuthorityRejection
)


@dataclass(frozen=True, slots=True)
class EvidenceGapLangGraphOperationalFailure:
    """Expected repository acquisition failure before valid target evidence exists."""

    exception_type: EvidenceGapLangGraphOperationalFailureType
    detail: str
    reason: str | None = None
    status_code: int | None = None

    def __post_init__(self) -> None:
        if self.exception_type not in {"GitHubAcquisitionError", "GitHubResponseError"}:
            raise ValueError("operational failure exception_type is unsupported.")
        _require_trimmed(self.detail, "operational failure detail")
        if self.reason is not None:
            _require_trimmed(self.reason, "operational failure reason")
        if self.status_code is not None and type(self.status_code) is not int:
            raise ValueError("operational failure status_code must be int or None.")


type EvidenceGapLangGraphInvestigationOutcome = (
    TargetPythonEvidence | EvidenceGapLangGraphOperationalFailure
)


@dataclass(frozen=True, slots=True)
class EvidenceGapLangGraphResult:
    """Framework-neutral observable result of one completed LangGraph workflow turn."""

    outcome_kind: EvidenceGapLangGraphOutcomeKind
    planner_outcome: EvidenceGapLangGraphPlannerOutcome
    execution_authority_outcome: EvidenceGapLangGraphAuthorityOutcome | None
    investigation_outcome: EvidenceGapLangGraphInvestigationOutcome | None
    python_support_assessment: PythonSupportDropImpactAssessment
    consumed_actions: tuple[str, ...]
    remaining_investigations: int
    continuation_status: EvidenceGapLangGraphContinuationStatus
    executed_action_id: str | None

    def __post_init__(self) -> None:
        _validate_orchestration_values(
            self.consumed_actions,
            self.remaining_investigations,
            self.continuation_status,
        )
        if self.outcome_kind in {"semantic_result", "operational_failure"}:
            _require_trimmed(self.executed_action_id, "executed_action_id")
        elif self.executed_action_id is not None:
            raise ValueError("non-execution outcomes must use executed_action_id=None.")


class EvidenceGapLangGraphPlannerPort(Protocol):
    def plan(
        self,
        start_input: EvidenceGapLangGraphStartInput,
    ) -> EvidenceGapLangGraphPlannerOutcome: ...


class EvidenceGapLangGraphAuthorityPort(Protocol):
    def authorize(
        self,
        snapshot: EvidenceGapLangGraphAuthoritySnapshot,
        proposal: EvidenceGapLangGraphActionProposal,
    ) -> EvidenceGapLangGraphAuthorityOutcome: ...


class ExactRepositoryReader(Protocol):
    def get_exact_commit_text_file(
        self,
        repository: str,
        commit_sha: str,
        path: str,
    ) -> RepositoryFileEvidence: ...


type EvidenceGapAuthoritySnapshotSupplier = Callable[
    [EvidenceGapLangGraphStartInput], EvidenceGapLangGraphAuthoritySnapshot
]


class EvidenceGapLangGraphRuntimeContext(TypedDict):
    planner: EvidenceGapLangGraphPlannerPort
    authority_snapshot_supplier: EvidenceGapAuthoritySnapshotSupplier
    authority: EvidenceGapLangGraphAuthorityPort
    repository_reader: ExactRepositoryReader


class EvidenceGapLangGraphInput(TypedDict):
    start_input: EvidenceGapLangGraphStartInput


class EvidenceGapLangGraphOutput(TypedDict):
    final_result: EvidenceGapLangGraphResult


class EvidenceGapLangGraphState(TypedDict, total=False):
    start_input: EvidenceGapLangGraphStartInput
    planner_outcome: EvidenceGapLangGraphPlannerOutcome
    authority_snapshot: EvidenceGapLangGraphAuthoritySnapshot
    execution_authority_outcome: EvidenceGapLangGraphAuthorityOutcome
    investigation_outcome: EvidenceGapLangGraphInvestigationOutcome
    final_result: EvidenceGapLangGraphResult


def plan_evidence_gap(
    state: EvidenceGapLangGraphState,
    runtime: Runtime[EvidenceGapLangGraphRuntimeContext],
) -> Command[Literal["authorize", "conclude"]]:
    """Produce one planner outcome and route from that outcome."""

    outcome = runtime.context["planner"].plan(state["start_input"])
    goto: Literal["authorize", "conclude"] = (
        "authorize"
        if isinstance(outcome, EvidenceGapLangGraphActionProposal)
        else "conclude"
    )
    return Command(update={"planner_outcome": outcome}, goto=goto)


def authorize_evidence_gap(
    state: EvidenceGapLangGraphState,
    runtime: Runtime[EvidenceGapLangGraphRuntimeContext],
) -> Command[Literal["investigate", "conclude"]]:
    """Obtain current post-planner state and establish deterministic execution authority."""

    planner_outcome = state["planner_outcome"]
    if not isinstance(planner_outcome, EvidenceGapLangGraphActionProposal):
        raise ValueError("authorize requires an action proposal.")

    snapshot = runtime.context["authority_snapshot_supplier"](state["start_input"])
    authority_outcome = runtime.context["authority"].authorize(snapshot, planner_outcome)
    goto: Literal["investigate", "conclude"] = (
        "investigate"
        if isinstance(authority_outcome, EvidenceGapLangGraphAuthorizedAction)
        else "conclude"
    )
    return Command(
        update={
            "authority_snapshot": snapshot,
            "execution_authority_outcome": authority_outcome,
        },
        goto=goto,
    )


def investigate_evidence_gap(
    state: EvidenceGapLangGraphState,
    runtime: Runtime[EvidenceGapLangGraphRuntimeContext],
) -> dict[str, EvidenceGapLangGraphInvestigationOutcome]:
    """Perform the one exact authorized repository read and immediately interpret its meaning."""

    authority_outcome = state["execution_authority_outcome"]
    if not isinstance(authority_outcome, EvidenceGapLangGraphAuthorizedAction):
        raise ValueError("investigate requires an authorized action.")

    try:
        repository_evidence = runtime.context[
            "repository_reader"
        ].get_exact_commit_text_file(
            authority_outcome.repository,
            authority_outcome.revision,
            authority_outcome.path,
        )
    except GitHubAcquisitionError as exc:
        outcome: EvidenceGapLangGraphInvestigationOutcome = (
            EvidenceGapLangGraphOperationalFailure(
                exception_type="GitHubAcquisitionError",
                detail=str(exc),
                reason=exc.reason,
                status_code=exc.status_code,
            )
        )
    except GitHubResponseError as exc:
        outcome = EvidenceGapLangGraphOperationalFailure(
            exception_type="GitHubResponseError",
            detail=str(exc),
        )
    else:
        outcome = interpret_target_python_declaration(repository_evidence)

    return {"investigation_outcome": outcome}


def conclude_evidence_gap(
    state: EvidenceGapLangGraphState,
) -> dict[str, EvidenceGapLangGraphResult]:
    """Apply pure deterministic final consequences without model or repository I/O."""

    return {"final_result": derive_evidence_gap_langgraph_result(state)}


def derive_evidence_gap_langgraph_result(
    state: EvidenceGapLangGraphState,
) -> EvidenceGapLangGraphResult:
    """Reconstruct the final semantic result from already-recorded bounded graph outcomes."""

    start_input = state["start_input"]
    planner_outcome = state["planner_outcome"]
    initial_baseline = _baseline_from_start_input(start_input)

    if isinstance(planner_outcome, EvidenceGapLangGraphProviderProblem):
        return _result(
            "provider_problem",
            planner_outcome,
            baseline=initial_baseline,
        )

    if isinstance(planner_outcome, EvidenceGapLangGraphNoAction):
        continuation_by_decision: dict[
            EvidenceGapLangGraphNoActionKind, EvidenceGapLangGraphContinuationStatus
        ] = {
            "QUESTION_SETTLED": "SETTLED",
            "KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY": "OUTSIDE_CURRENT_BOUNDARY",
            "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED": "NO_JUSTIFIED_INVESTIGATION",
        }
        return _result(
            "no_action",
            planner_outcome,
            baseline=replace(
                initial_baseline,
                continuation_status=continuation_by_decision[
                    planner_outcome.decision_kind
                ],
            ),
        )

    if not isinstance(planner_outcome, EvidenceGapLangGraphActionProposal):
        raise TypeError("planner outcome is unsupported.")

    snapshot = state.get("authority_snapshot")
    authority_outcome = state.get("execution_authority_outcome")
    if snapshot is None or authority_outcome is None:
        raise ValueError("action proposal requires a recorded current authority outcome.")

    if isinstance(authority_outcome, EvidenceGapLangGraphAuthorityRejection):
        return _result(
            "authority_rejected",
            planner_outcome,
            baseline=snapshot.baseline,
            execution_authority_outcome=authority_outcome,
        )

    if not isinstance(authority_outcome, EvidenceGapLangGraphAuthorizedAction):
        raise TypeError("execution authority outcome is unsupported.")

    investigation_outcome = state.get("investigation_outcome")
    if investigation_outcome is None:
        raise ValueError("authorized action requires an investigation outcome.")

    if isinstance(investigation_outcome, EvidenceGapLangGraphOperationalFailure):
        next_baseline = replace(
            snapshot.baseline,
            remaining_investigations=snapshot.baseline.remaining_investigations - 1,
        )
        return _result(
            "operational_failure",
            planner_outcome,
            baseline=next_baseline,
            execution_authority_outcome=authority_outcome,
            investigation_outcome=investigation_outcome,
            executed_action_id=authority_outcome.action_id,
        )

    target_relevance = evaluate_target_python_relevance(
        snapshot.baseline.python_support_assessment.candidate.upstream_claim,
        investigation_outcome,
    )
    next_assessment = evaluate_python_support_drop_impact(
        snapshot.baseline.python_support_assessment.candidate,
        target_relevance,
    )
    next_baseline = replace(
        snapshot.baseline,
        python_support_assessment=next_assessment,
        consumed_actions=(
            snapshot.baseline.consumed_actions + (authority_outcome.action_id,)
        ),
        remaining_investigations=snapshot.baseline.remaining_investigations - 1,
    )
    return _result(
        "semantic_result",
        planner_outcome,
        baseline=next_baseline,
        execution_authority_outcome=authority_outcome,
        investigation_outcome=investigation_outcome,
        executed_action_id=authority_outcome.action_id,
    )


def build_evidence_gap_langgraph():
    """Compile the bounded ``StateGraph`` with explicit input/output schemas."""

    builder = StateGraph(
        EvidenceGapLangGraphState,
        context_schema=EvidenceGapLangGraphRuntimeContext,
        input_schema=EvidenceGapLangGraphInput,
        output_schema=EvidenceGapLangGraphOutput,
    )
    builder.add_node("plan", plan_evidence_gap)
    builder.add_node("authorize", authorize_evidence_gap)
    builder.add_node("investigate", investigate_evidence_gap)
    builder.add_node("conclude", conclude_evidence_gap)
    builder.add_edge(START, "plan")
    builder.add_edge("investigate", "conclude")
    builder.add_edge("conclude", END)
    return builder.compile()


def _baseline_from_start_input(
    start_input: EvidenceGapLangGraphStartInput,
) -> EvidenceGapLangGraphBaseline:
    assessment = start_input.investigation.python_support_drop_pre_investigation_result
    if not isinstance(assessment, PythonSupportDropImpactAssessment):
        raise ValueError(
            "LangGraph start input requires the product pre-target Python-support assessment."
        )
    return EvidenceGapLangGraphBaseline(
        python_support_assessment=assessment,
        consumed_actions=start_input.consumed_actions,
        remaining_investigations=start_input.remaining_investigations,
        continuation_status=start_input.continuation_status,
    )


def _result(
    outcome_kind: EvidenceGapLangGraphOutcomeKind,
    planner_outcome: EvidenceGapLangGraphPlannerOutcome,
    *,
    baseline: EvidenceGapLangGraphBaseline,
    execution_authority_outcome: EvidenceGapLangGraphAuthorityOutcome | None = None,
    investigation_outcome: EvidenceGapLangGraphInvestigationOutcome | None = None,
    executed_action_id: str | None = None,
) -> EvidenceGapLangGraphResult:
    return EvidenceGapLangGraphResult(
        outcome_kind=outcome_kind,
        planner_outcome=planner_outcome,
        execution_authority_outcome=execution_authority_outcome,
        investigation_outcome=investigation_outcome,
        python_support_assessment=baseline.python_support_assessment,
        consumed_actions=baseline.consumed_actions,
        remaining_investigations=baseline.remaining_investigations,
        continuation_status=baseline.continuation_status,
        executed_action_id=executed_action_id,
    )


def _validate_orchestration_values(
    consumed_actions: tuple[str, ...],
    remaining_investigations: int,
    continuation_status: EvidenceGapLangGraphContinuationStatus,
) -> None:
    if type(remaining_investigations) is not int or remaining_investigations < 0:
        raise ValueError("remaining_investigations must be a non-negative integer.")
    if len(set(consumed_actions)) != len(consumed_actions):
        raise ValueError("consumed action ids must be unique.")
    for action_id in consumed_actions:
        _require_trimmed(action_id, "consumed action id")
    if continuation_status not in {
        "ACTIVE",
        "SETTLED",
        "OUTSIDE_CURRENT_BOUNDARY",
        "NO_JUSTIFIED_INVESTIGATION",
    }:
        raise ValueError("continuation_status is unsupported.")


def _require_trimmed(value: object, name: str) -> None:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{name} must be non-empty trimmed text.")


__all__ = (
    "EvidenceGapAuthoritySnapshotSupplier",
    "EvidenceGapLangGraphActionProposal",
    "EvidenceGapLangGraphAuthorityOutcome",
    "EvidenceGapLangGraphAuthorityPort",
    "EvidenceGapLangGraphAuthorityRejection",
    "EvidenceGapLangGraphAuthorityRejectionReason",
    "EvidenceGapLangGraphAuthoritySnapshot",
    "EvidenceGapLangGraphAuthorizedAction",
    "EvidenceGapLangGraphBaseline",
    "EvidenceGapLangGraphInput",
    "EvidenceGapLangGraphInvestigationOutcome",
    "EvidenceGapLangGraphNoAction",
    "EvidenceGapLangGraphNoActionKind",
    "EvidenceGapLangGraphOperationalFailure",
    "EvidenceGapLangGraphOutcomeKind",
    "EvidenceGapLangGraphOutput",
    "EvidenceGapLangGraphPlannerOutcome",
    "EvidenceGapLangGraphPlannerPort",
    "EvidenceGapLangGraphProviderProblem",
    "EvidenceGapLangGraphProviderProblemReason",
    "EvidenceGapLangGraphResult",
    "EvidenceGapLangGraphRuntimeContext",
    "EvidenceGapLangGraphStartInput",
    "EvidenceGapLangGraphState",
    "ExactRepositoryReader",
    "authorize_evidence_gap",
    "build_evidence_gap_langgraph",
    "conclude_evidence_gap",
    "derive_evidence_gap_langgraph_result",
    "investigate_evidence_gap",
    "plan_evidence_gap",
)
