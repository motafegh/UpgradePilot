"""EvidenceGapPlanner model-observation and structured-decision boundary.

This module is experiment support code, not UpgradePilot product runtime code.

It separates the full trusted orchestration state from the smaller observation an LLM needs for
bounded evidence-gap planning. It defines the planner-facing context, explicit request projection,
structured decision schema, and strict decision parser without calling a model or executing an
investigation::

    trusted UpgradePilot evidence/state
    -> explicit ``EvidenceGapPlannerContext`` projection
    -> local-model boundary
    -> untrusted ``EvidenceGapDecision``
    -> deterministic admission/execution

The model sees semantic planning information. Exact repository/revision/path identity, action
preconditions, mutation policy, result-class contracts, provider retry policy, and other execution
authority stay outside this module's request payload.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Literal, Mapping

from upgradepilot.impact.applicability import PropositionAssessment


EvidenceGapDecisionKind = Literal[
    "ACTION_SELECTED",
    "QUESTION_SETTLED",
    "KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY",
    "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED",
]

PlanningEvidenceValue = str | int | bool | tuple[str, ...]


# Provider schema validity proves only the outer wire shape. Cross-field semantics such as
# ACTION_SELECTED requiring an action ID remain deterministic parser/admission responsibilities.
EVIDENCE_GAP_DECISION_JSON_SCHEMA: dict[str, object] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["decision_kind", "action_id", "explanation"],
    "properties": {
        "decision_kind": {
            "type": "string",
            "enum": [
                "ACTION_SELECTED",
                "QUESTION_SETTLED",
                "KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY",
                "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED",
            ],
        },
        "action_id": {
            "anyOf": [
                {"type": "string", "minLength": 1},
                {"type": "null"},
            ]
        },
        "explanation": {"type": "string", "minLength": 1},
    },
}


@dataclass(frozen=True, slots=True)
class EvidenceGapDependencyTransition:
    """Canonical dependency transition exposed to the planner.

    ``normalized_package`` is the trusted cross-source package identity. Presentation spelling,
    source evidence, and dependency-change limitations remain with their existing product owners.
    """

    normalized_package: str
    old_version: str
    proposed_version: str

    def __post_init__(self) -> None:
        _require_trimmed(self.normalized_package, "normalized_package")
        _require_trimmed(self.old_version, "old_version")
        _require_trimmed(self.proposed_version, "proposed_version")


@dataclass(frozen=True, slots=True)
class PlanningEvidenceFact:
    """One bounded structured fact inside planner-facing supporting evidence.

    Values intentionally stay small and JSON-like. This is not an escape hatch for serializing
    arbitrary source objects or raw external text into the model request.
    """

    name: str
    value: PlanningEvidenceValue

    def __post_init__(self) -> None:
        _require_trimmed(self.name, "planning evidence fact name")
        _require_planning_evidence_value(self.value)


@dataclass(frozen=True, slots=True)
class PlanningEvidence:
    """Selected structured evidence whose shape can change investigation value.

    ``summary`` is project-authored interpreted context. ``facts`` preserve bounded structured
    details such as CI consumption state, reachability kind, witness paths, or unresolved
    conditions. Raw workflow YAML, logs, changelog prose, diffs, lockfiles, and source files are
    not represented here by default.
    """

    evidence_kind: str
    summary: str
    facts: tuple[PlanningEvidenceFact, ...] = ()

    def __post_init__(self) -> None:
        _require_trimmed(self.evidence_kind, "evidence_kind")
        _require_trimmed(self.summary, "planning evidence summary")
        names = tuple(fact.name for fact in self.facts)
        if len(set(names)) != len(names):
            raise ValueError("planning evidence fact names must be unique within one item.")


@dataclass(frozen=True, slots=True)
class EvidenceGapActionDescriptor:
    """Model-visible projection of one currently offered pre-bound investigation action.

    The descriptor explains what the planner can choose and what evidence the action may add.
    Trusted action locators, exact preconditions, mutation policy, result-class contracts, and
    provider/executor metadata remain outside the model-facing descriptor.
    """

    action_id: str
    purpose: str
    target_proposition: str
    evidence_yield: str

    def __post_init__(self) -> None:
        _require_trimmed(self.action_id, "action_id")
        _require_trimmed(self.purpose, "action purpose")
        _require_trimmed(self.target_proposition, "target_proposition")
        _require_trimmed(self.evidence_yield, "evidence_yield")


@dataclass(frozen=True, slots=True)
class EvidenceGapPlanningBudget:
    """Semantic investigation budget visible to the planner for the current responsibility."""

    remaining_investigations: int

    def __post_init__(self) -> None:
        if (
            type(self.remaining_investigations) is not int
            or self.remaining_investigations < 0
        ):
            raise ValueError("remaining_investigations must be a non-negative integer.")


@dataclass(frozen=True, slots=True)
class EvidenceGapPlannerContext:
    """Complete first-seam model observation for one bounded evidence-gap decision.

    This type is intentionally *not* the complete agent/orchestrator state. It contains only
    information justified as useful for model reasoning. Deterministic execution authority
    remains in separately owned trusted state and is rebound after the model chooses an action ID.
    """

    planning_question: str
    dependency_transition: EvidenceGapDependencyTransition
    propositions: tuple[PropositionAssessment, ...]
    planning_evidence: tuple[PlanningEvidence, ...]
    consumed_actions: tuple[str, ...]
    planning_budget: EvidenceGapPlanningBudget
    allowed_actions: tuple[EvidenceGapActionDescriptor, ...]

    def __post_init__(self) -> None:
        _require_trimmed(self.planning_question, "planning_question")
        if not self.propositions:
            raise ValueError("planner context requires at least one proposition.")

        proposition_keys = tuple(item.key for item in self.propositions)
        if len(set(proposition_keys)) != len(proposition_keys):
            raise ValueError("planner proposition keys must be unique.")

        for action_id in self.consumed_actions:
            _require_trimmed(action_id, "consumed action id")
        if len(set(self.consumed_actions)) != len(self.consumed_actions):
            raise ValueError("consumed action ids must be unique.")

        action_ids = tuple(action.action_id for action in self.allowed_actions)
        if len(set(action_ids)) != len(action_ids):
            raise ValueError("allowed action ids must be unique.")

        proposition_key_set = set(proposition_keys)
        for action in self.allowed_actions:
            if action.target_proposition not in proposition_key_set:
                raise ValueError(
                    "allowed action target proposition must exist in planner propositions."
                )

        overlap = set(action_ids).intersection(self.consumed_actions)
        if overlap:
            raise ValueError(
                "a consumed action must not also be offered as a current allowed action."
            )


@dataclass(frozen=True, slots=True)
class EvidenceGapDecision:
    """Untrusted structured planner decision before deterministic admission."""

    decision_kind: EvidenceGapDecisionKind
    action_id: str | None
    explanation: str

    def __post_init__(self) -> None:
        if self.decision_kind not in {
            "ACTION_SELECTED",
            "QUESTION_SETTLED",
            "KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY",
            "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED",
        }:
            raise ValueError("decision_kind is unsupported.")
        _require_trimmed(self.explanation, "explanation")

        if self.decision_kind == "ACTION_SELECTED":
            _require_trimmed(self.action_id, "action_id")
        elif self.action_id is not None:
            raise ValueError("no-action decisions must use action_id=None.")


def render_evidence_gap_planner_request(
    context: EvidenceGapPlannerContext,
) -> dict[str, object]:
    """Render the exact bounded payload admitted to the model call.

    Fields are enumerated explicitly rather than produced with ``dataclasses.asdict``. This is an
    authority boundary: adding a field to a trusted internal type must never automatically expose
    that field to the model.
    """

    return {
        "context": {
            "planning_question": context.planning_question,
            "dependency_transition": {
                "normalized_package": context.dependency_transition.normalized_package,
                "old_version": context.dependency_transition.old_version,
                "proposed_version": context.dependency_transition.proposed_version,
            },
            "propositions": [
                {
                    "key": proposition.key,
                    "state": proposition.state,
                    "evidence_coverage": proposition.evidence_coverage,
                    "evidence_owner": proposition.evidence_owner,
                    "detail": proposition.detail,
                }
                for proposition in context.propositions
            ],
            "planning_evidence": [
                {
                    "evidence_kind": evidence.evidence_kind,
                    "summary": evidence.summary,
                    "facts": [
                        {
                            "name": fact.name,
                            "value": _planning_evidence_value_payload(fact.value),
                        }
                        for fact in evidence.facts
                    ],
                }
                for evidence in context.planning_evidence
            ],
            "consumed_actions": list(context.consumed_actions),
            "planning_budget": {
                "remaining_investigations": (
                    context.planning_budget.remaining_investigations
                )
            },
            "allowed_actions": [
                {
                    "action_id": action.action_id,
                    "purpose": action.purpose,
                    "target_proposition": action.target_proposition,
                    "evidence_yield": action.evidence_yield,
                }
                for action in context.allowed_actions
            ],
        },
        "output_schema": deepcopy(EVIDENCE_GAP_DECISION_JSON_SCHEMA),
    }


def evidence_gap_decision_from_mapping(
    data: Mapping[str, Any],
) -> EvidenceGapDecision:
    """Parse one strict three-field model result without granting execution authority."""

    expected_fields = {"decision_kind", "action_id", "explanation"}
    if set(data) != expected_fields:
        raise ValueError(f"evidence-gap decision fields differed: {sorted(data)}")

    decision_kind = data["decision_kind"]
    action_id = data["action_id"]
    explanation = data["explanation"]

    if decision_kind not in {
        "ACTION_SELECTED",
        "QUESTION_SETTLED",
        "KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY",
        "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED",
    }:
        raise ValueError(f"decision_kind was unsupported: {decision_kind!r}")
    if action_id is not None and not isinstance(action_id, str):
        raise ValueError("action_id must be text or null.")
    if not isinstance(explanation, str):
        raise ValueError("explanation must be text.")

    return EvidenceGapDecision(
        decision_kind=decision_kind,
        action_id=action_id,
        explanation=explanation,
    )


def _planning_evidence_value_payload(value: PlanningEvidenceValue) -> object:
    if isinstance(value, tuple):
        return list(value)
    return value


def _require_planning_evidence_value(value: object) -> None:
    if type(value) in {int, bool}:
        return
    if isinstance(value, str):
        _require_trimmed(value, "planning evidence value")
        return
    if isinstance(value, tuple):
        if not value:
            raise ValueError("planning evidence tuple value must not be empty.")
        for item in value:
            _require_trimmed(item, "planning evidence tuple item")
        return
    raise ValueError(
        "planning evidence value must be trimmed text, int, bool, or tuple[str, ...]."
    )


def _trimmed(value: object) -> bool:
    return isinstance(value, str) and bool(value) and value == value.strip()


def _require_trimmed(value: object, name: str) -> None:
    if not _trimmed(value):
        raise ValueError(f"{name} must be non-empty trimmed text.")


__all__ = (
    "EVIDENCE_GAP_DECISION_JSON_SCHEMA",
    "EvidenceGapActionDescriptor",
    "EvidenceGapDecision",
    "EvidenceGapDecisionKind",
    "EvidenceGapDependencyTransition",
    "EvidenceGapPlannerContext",
    "EvidenceGapPlanningBudget",
    "PlanningEvidence",
    "PlanningEvidenceFact",
    "evidence_gap_decision_from_mapping",
    "render_evidence_gap_planner_request",
)
