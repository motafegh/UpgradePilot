"""LangGraph R4-B experiment for one bounded ``EvidenceGapPlanner`` workflow turn.

This module is experiment/evaluation code, not UpgradePilot product runtime code.

The graph keeps the accepted responsibility boundaries visible without mechanically copying the
R4-A A-number layout::

    START
      -> plan
         -> authorize   [action proposal]
         -> conclude    [no-action / provider problem]
      -> authorize
         -> investigate [authorized]
         -> conclude    [rejected]
      -> investigate
         -> conclude
      -> END

``plan`` owns the bounded model observation and untrusted proposal. ``authorize`` obtains one
coherent fresh T2 authority/consequence snapshot and performs deterministic admission.
``investigate`` owns the only admitted external repository effect. ``conclude`` is pure and owns
final budget/consumption/domain/continuation consequences.

The graph intentionally reuses the existing bounded model/provider seam and deterministic admission
semantics to hold those variables constant while R4-B evaluates LangGraph orchestration. Product-
owned repository acquisition and target/domain interpretation remain with their normal owners.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Callable, Literal, Protocol, TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.runtime import Runtime
from langgraph.types import Command

from experiments.b2_x1_evidence_gap_admission import (
    AdmittedInvestigationAction,
    EvidenceGapAdmissionProblem,
    EvidenceGapAdmissionResult,
    EvidenceGapAdmissionState,
    admit_selected_investigation_action,
)
from experiments.b2_x1_evidence_gap_composition import (
    compose_pre_target_python_support_planner_context,
)
from experiments.b2_x1_evidence_gap_model import (
    EvidenceGapModelInvocationProblem,
    EvidenceGapModelInvocationResult,
)
from experiments.b2_x1_evidence_gap_planner import (
    EvidenceGapDecision,
    EvidenceGapPlannerContext,
)
from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github.repository import RepositoryFileEvidence
from upgradepilot.impact.python_support import (
    PythonSupportDropImpactAssessment,
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
    """Fresh T2 authority state plus the matching semantic consequence baseline.

    ``authorize`` must not admit against one current view and later let ``conclude`` mutate a stale
    T1 view. The two values therefore travel together and are checked for the budget, consumption,
    and proposition relationships needed by this bounded responsibility.
    """

    admission_state: EvidenceGapAdmissionState
    baseline: EvidenceGapLangGraphBaseline

    def __post_init__(self) -> None:
        if self.baseline.continuation_status != "ACTIVE":
            raise ValueError("fresh authority snapshot requires an ACTIVE consequence baseline.")
        if self.admission_state.consumed_actions != self.baseline.consumed_actions:
            raise ValueError("authority and consequence snapshots must agree on consumed actions.")
        if (
            self.admission_state.remaining_investigations
            != self.baseline.remaining_investigations
        ):
            raise ValueError("authority and consequence snapshots must agree on remaining budget.")
        if self.admission_state.propositions != _assessment_propositions(
            self.baseline.python_support_assessment
        ):
            raise ValueError("authority and consequence snapshots must agree on proposition state.")


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
    """Framework-neutral observable result of one completed R4-B graph turn."""

    outcome_kind: EvidenceGapLangGraphOutcomeKind
    planner_outcome: EvidenceGapModelInvocationResult
    execution_authority_outcome: EvidenceGapAdmissionResult | None
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


class EvidenceGapPlannerPort(Protocol):
    def decide(
        self,
        context: EvidenceGapPlannerContext,
    ) -> EvidenceGapModelInvocationResult: ...


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
    planner: EvidenceGapPlannerPort
    authority_snapshot_supplier: EvidenceGapAuthoritySnapshotSupplier
    repository_reader: ExactRepositoryReader


class EvidenceGapLangGraphInput(TypedDict):
    start_input: EvidenceGapLangGraphStartInput


class EvidenceGapLangGraphOutput(TypedDict):
    final_result: EvidenceGapLangGraphResult


class EvidenceGapLangGraphState(TypedDict, total=False):
    start_input: EvidenceGapLangGraphStartInput
    planner_outcome: EvidenceGapModelInvocationResult
    authority_snapshot: EvidenceGapLangGraphAuthoritySnapshot
    execution_authority_outcome: EvidenceGapAdmissionResult
    investigation_outcome: EvidenceGapLangGraphInvestigationOutcome
    final_result: EvidenceGapLangGraphResult


def plan_evidence_gap(
    state: EvidenceGapLangGraphState,
    runtime: Runtime[EvidenceGapLangGraphRuntimeContext],
) -> Command[Literal["authorize", "conclude"]]:
    """Project the bounded T1 model observation and produce one untrusted planner outcome."""

    start_input = state["start_input"]
    planner_context = compose_pre_target_python_support_planner_context(
        start_input.investigation,
        planning_question=start_input.planning_question,
        consumed_actions=start_input.consumed_actions,
        remaining_investigations=start_input.remaining_investigations,
    )
    outcome = runtime.context["planner"].decide(planner_context)
    goto: Literal["authorize", "conclude"] = (
        "authorize"
        if isinstance(outcome, EvidenceGapDecision)
        and outcome.decision_kind == "ACTION_SELECTED"
        else "conclude"
    )
    return Command(update={"planner_outcome": outcome}, goto=goto)


def authorize_evidence_gap(
    state: EvidenceGapLangGraphState,
    runtime: Runtime[EvidenceGapLangGraphRuntimeContext],
) -> Command[Literal["investigate", "conclude"]]:
    """Obtain fresh T2 state and establish exact deterministic execution authority."""

    planner_outcome = state["planner_outcome"]
    if not isinstance(planner_outcome, EvidenceGapDecision) or (
        planner_outcome.decision_kind != "ACTION_SELECTED"
    ):
        raise ValueError("authorize requires an ACTION_SELECTED planner outcome.")

    snapshot = runtime.context["authority_snapshot_supplier"](state["start_input"])
    authority_outcome = admit_selected_investigation_action(
        snapshot.admission_state,
        planner_outcome,
    )
    goto: Literal["investigate", "conclude"] = (
        "investigate"
        if isinstance(authority_outcome, AdmittedInvestigationAction)
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
    """Perform the one exact admitted repository read and immediately interpret its meaning."""

    authority_outcome = state["execution_authority_outcome"]
    if not isinstance(authority_outcome, AdmittedInvestigationAction):
        raise ValueError("investigate requires an admitted investigation action.")

    action = authority_outcome.action
    try:
        repository_evidence = runtime.context[
            "repository_reader"
        ].get_exact_commit_text_file(
            action.repository,
            action.revision,
            action.path,
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

    if isinstance(planner_outcome, EvidenceGapModelInvocationProblem):
        return _result(
            "provider_problem",
            planner_outcome,
            baseline=initial_baseline,
        )

    if planner_outcome.decision_kind != "ACTION_SELECTED":
        continuation_by_decision: dict[
            str, EvidenceGapLangGraphContinuationStatus
        ] = {
            "QUESTION_SETTLED": "SETTLED",
            "KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY": "OUTSIDE_CURRENT_BOUNDARY",
            "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED": "NO_JUSTIFIED_INVESTIGATION",
        }
        try:
            continuation_status = continuation_by_decision[planner_outcome.decision_kind]
        except KeyError as exc:
            raise ValueError("unsupported no-action planner decision.") from exc
        return _result(
            "no_action",
            planner_outcome,
            baseline=replace(
                initial_baseline,
                continuation_status=continuation_status,
            ),
        )

    snapshot = state.get("authority_snapshot")
    authority_outcome = state.get("execution_authority_outcome")
    if snapshot is None or authority_outcome is None:
        raise ValueError("action proposal requires a recorded T2 authority outcome.")

    if isinstance(authority_outcome, EvidenceGapAdmissionProblem):
        return _result(
            "authority_rejected",
            planner_outcome,
            baseline=snapshot.baseline,
            execution_authority_outcome=authority_outcome,
        )

    if not isinstance(authority_outcome, AdmittedInvestigationAction):
        raise TypeError("execution authority outcome is unsupported.")

    investigation_outcome = state.get("investigation_outcome")
    if investigation_outcome is None:
        raise ValueError("admitted action requires an investigation outcome.")

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
            executed_action_id=authority_outcome.action.action_id,
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
            snapshot.baseline.consumed_actions
            + (authority_outcome.action.action_id,)
        ),
        remaining_investigations=snapshot.baseline.remaining_investigations - 1,
    )
    return _result(
        "semantic_result",
        planner_outcome,
        baseline=next_baseline,
        execution_authority_outcome=authority_outcome,
        investigation_outcome=investigation_outcome,
        executed_action_id=authority_outcome.action.action_id,
    )


def build_evidence_gap_langgraph():
    """Compile the first bounded R4-B ``StateGraph`` with explicit input/output schemas."""

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


def _assessment_propositions(
    assessment: PythonSupportDropImpactAssessment,
):
    return tuple(
        proposition
        for path in assessment.applicability.paths
        for proposition in path.propositions
    )


def _result(
    outcome_kind: EvidenceGapLangGraphOutcomeKind,
    planner_outcome: EvidenceGapModelInvocationResult,
    *,
    baseline: EvidenceGapLangGraphBaseline,
    execution_authority_outcome: EvidenceGapAdmissionResult | None = None,
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
    "EvidenceGapLangGraphAuthoritySnapshot",
    "EvidenceGapLangGraphBaseline",
    "EvidenceGapLangGraphInput",
    "EvidenceGapLangGraphInvestigationOutcome",
    "EvidenceGapLangGraphOperationalFailure",
    "EvidenceGapLangGraphOutcomeKind",
    "EvidenceGapLangGraphOutput",
    "EvidenceGapLangGraphResult",
    "EvidenceGapLangGraphRuntimeContext",
    "EvidenceGapLangGraphStartInput",
    "EvidenceGapLangGraphState",
    "ExactRepositoryReader",
    "EvidenceGapPlannerPort",
    "authorize_evidence_gap",
    "build_evidence_gap_langgraph",
    "conclude_evidence_gap",
    "derive_evidence_gap_langgraph_result",
    "investigate_evidence_gap",
    "plan_evidence_gap",
)
