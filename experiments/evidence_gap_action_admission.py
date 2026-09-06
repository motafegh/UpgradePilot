"""Fresh deterministic action admission for the bounded ``EvidenceGapPlanner`` experiment.

This module is experiment support code, not UpgradePilot product runtime code.

The planner model boundary defines the smaller model-visible observation and the untrusted
``EvidenceGapDecision``. This module owns the next authority boundary: a model-selected action ID
is only a proposal. Before execution, deterministic code must rebind that ID to the current trusted
exact action definition and re-check the latest trusted state::

    T1 model-visible context
    -> EvidenceGapDecision(ACTION_SELECTED, action_id)

    T2 fresh trusted admission state
    + exact pre-bound action catalog
    -> admit_selected_investigation_action(...)
    -> one admitted exact action OR a typed admission problem

The model never supplies repository, revision, path, action preconditions, mutation policy, or
result-family authority. Those values remain in ``BoundInvestigationAction`` and are recovered
only after the selected ID is accepted against current trusted state.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from experiments.evidence_gap_planner_model_boundary import (
    EvidenceGapActionDescriptor,
    EvidenceGapDecision,
)
from upgradepilot.github.identity import validate_commit_sha, validate_repository
from upgradepilot.impact.applicability import PropositionAssessment
from upgradepilot.repository_path import repository_relative_parts


InvestigationMutationClass = Literal["read_only", "mutation"]
EvidenceGapAdmissionProblemReason = Literal[
    "unknown_action",
    "action_consumed",
    "budget_exhausted",
    "action_identity_stale",
    "action_not_allowed_by_policy",
    "action_not_currently_actionable",
]

TARGET_PYTHON_DECLARATION_ACTION_ID = "acquire_exact_target_python_declaration"
TARGET_PYTHON_DECLARATION_PROPOSITION = "exact_target_python_declaration_established"
TARGET_PYTHON_DECLARATION_PATH = "pyproject.toml"
TARGET_PYTHON_DECLARATION_REQUIRED_STATE = "unresolved"
TARGET_PYTHON_DECLARATION_REQUIRED_COVERAGE = "insufficient"
TARGET_PYTHON_DECLARATION_RESULT_FAMILIES = (
    "TargetPythonDeclaration",
    "TargetPythonDeclarationProblem",
)


@dataclass(frozen=True, slots=True)
class BoundInvestigationAction:
    """One exact trusted investigation action that a model may select but never redefine.

    ``purpose`` and ``evidence_yield`` can be projected into the model-visible action descriptor.
    Exact source identity, preconditions, mutation policy, and result-family contract stay hidden
    and become available only after deterministic rebinding by ``action_id``.
    """

    action_id: str
    purpose: str
    target_proposition: str
    evidence_yield: str
    repository: str
    revision: str
    path: str
    required_proposition_state: str
    required_evidence_coverage: str
    mutation_class: InvestigationMutationClass
    result_families: tuple[str, ...]

    def __post_init__(self) -> None:
        _require_trimmed(self.action_id, "action_id")
        _require_trimmed(self.purpose, "purpose")
        _require_trimmed(self.target_proposition, "target_proposition")
        _require_trimmed(self.evidence_yield, "evidence_yield")
        _require_trimmed(self.required_proposition_state, "required_proposition_state")
        _require_trimmed(self.required_evidence_coverage, "required_evidence_coverage")
        _require_canonical_repository(self.repository)
        _require_canonical_revision(self.revision)
        _require_repository_path(self.path)
        if self.mutation_class not in {"read_only", "mutation"}:
            raise ValueError("mutation_class must be read_only or mutation.")
        if not self.result_families or any(
            not _trimmed(item) for item in self.result_families
        ):
            raise ValueError("result_families must contain non-empty trimmed names.")

        # The first real action ID represents one exact executable contract. Since the model
        # boundary removed echoes of preconditions/result families, construction of this trusted
        # binding is the narrow owner that prevents the same ID from being silently repurposed.
        if self.action_id == TARGET_PYTHON_DECLARATION_ACTION_ID:
            if self.target_proposition != TARGET_PYTHON_DECLARATION_PROPOSITION:
                raise ValueError(
                    "target-Python action must retain its exact target proposition"
                )
            if self.path != TARGET_PYTHON_DECLARATION_PATH:
                raise ValueError(
                    "target-Python action must remain bound to exact pyproject.toml"
                )
            if (
                self.required_proposition_state
                != TARGET_PYTHON_DECLARATION_REQUIRED_STATE
                or self.required_evidence_coverage
                != TARGET_PYTHON_DECLARATION_REQUIRED_COVERAGE
            ):
                raise ValueError(
                    "target-Python action must retain its exact proposition preconditions"
                )
            if self.mutation_class != "read_only":
                raise ValueError("target-Python action must remain read-only")
            if self.result_families != TARGET_PYTHON_DECLARATION_RESULT_FAMILIES:
                raise ValueError(
                    "target-Python action must retain its exact result-family contract"
                )


@dataclass(frozen=True, slots=True)
class EvidenceGapAdmissionState:
    """Latest trusted state used immediately before selected-action execution.

    This is intentionally different from ``EvidenceGapPlannerContext``. The planner context is
    the bounded observation rendered at decision time T1. Admission state is the deterministic
    current-state view at T2, so consumed history, budget, proposition state, source identity, or
    the current action catalog may have changed while the model was reasoning.

    ``actions`` may intentionally still contain an action that is now consumed or stale. Fresh
    admission must defend against those changes rather than assuming a perfectly pre-pruned
    catalog.
    """

    repository: str
    revision: str
    propositions: tuple[PropositionAssessment, ...]
    consumed_actions: tuple[str, ...]
    remaining_investigations: int
    actions: tuple[BoundInvestigationAction, ...]

    def __post_init__(self) -> None:
        _require_canonical_repository(self.repository)
        _require_canonical_revision(self.revision)
        if type(self.remaining_investigations) is not int or self.remaining_investigations < 0:
            raise ValueError("remaining_investigations must be a non-negative integer.")

        proposition_keys = tuple(item.key for item in self.propositions)
        if len(set(proposition_keys)) != len(proposition_keys):
            raise ValueError("admission proposition keys must be unique.")

        for action_id in self.consumed_actions:
            _require_trimmed(action_id, "consumed action id")
        if len(set(self.consumed_actions)) != len(self.consumed_actions):
            raise ValueError("consumed action ids must be unique.")

        action_ids = tuple(action.action_id for action in self.actions)
        if len(set(action_ids)) != len(action_ids):
            raise ValueError("bound action ids must be unique.")


@dataclass(frozen=True, slots=True)
class AdmittedInvestigationAction:
    """Exact bound action authorized by the current deterministic admission state.

    ``explanation`` remains untrusted model rationale carried for traceability. It does not
    modify the exact bound action or any execution parameter.
    """

    action: BoundInvestigationAction
    explanation: str


@dataclass(frozen=True, slots=True)
class EvidenceGapAdmissionProblem:
    """Why a selected action must not execute under the latest trusted state."""

    reason: EvidenceGapAdmissionProblemReason
    action_id: str
    detail: str


# A small union alias keeps the caller honest: selected-action admission has exactly two outcome
# families in this increment—an exact admitted action or an explicit deterministic problem.
type EvidenceGapAdmissionResult = AdmittedInvestigationAction | EvidenceGapAdmissionProblem


def build_target_python_declaration_action(
    repository: str,
    revision: str,
) -> BoundInvestigationAction:
    """Build the first real exact action binding from trusted target identity."""

    return BoundInvestigationAction(
        action_id=TARGET_PYTHON_DECLARATION_ACTION_ID,
        purpose=(
            "Acquire the exact target Python declaration needed to advance the unresolved "
            "Python-support question."
        ),
        target_proposition=TARGET_PYTHON_DECLARATION_PROPOSITION,
        evidence_yield=(
            "Exact target Python declaration evidence or a typed target-declaration problem."
        ),
        repository=repository,
        revision=revision,
        path=TARGET_PYTHON_DECLARATION_PATH,
        required_proposition_state=TARGET_PYTHON_DECLARATION_REQUIRED_STATE,
        required_evidence_coverage=TARGET_PYTHON_DECLARATION_REQUIRED_COVERAGE,
        mutation_class="read_only",
        result_families=TARGET_PYTHON_DECLARATION_RESULT_FAMILIES,
    )


def project_action_descriptor(
    action: BoundInvestigationAction,
) -> EvidenceGapActionDescriptor:
    """Project one exact action into the smaller model-visible action descriptor."""

    return EvidenceGapActionDescriptor(
        action_id=action.action_id,
        purpose=action.purpose,
        target_proposition=action.target_proposition,
        evidence_yield=action.evidence_yield,
    )


def admit_selected_investigation_action(
    state: EvidenceGapAdmissionState,
    decision: EvidenceGapDecision,
) -> EvidenceGapAdmissionResult:
    """Rebind and admit one model-selected action against latest trusted state.

    Calling this function for a no-action decision is an orchestration/programmer error rather
    than an admission problem: a no-action decision is already a valid branch that executes no
    capability. For ``ACTION_SELECTED``, every executable fact is recovered from trusted state.
    """

    if decision.decision_kind != "ACTION_SELECTED":
        raise ValueError(
            "selected-action admission requires an ACTION_SELECTED decision."
        )
    assert decision.action_id is not None

    action = _find_action(state, decision.action_id)
    if action is None:
        return _problem(
            "unknown_action",
            decision.action_id,
            "The selected ID is absent from the current trusted bound-action catalog.",
        )

    # The request projection normally prunes consumed actions, but consumption can change after
    # T1 or a stale/concurrent catalog may still carry the binding. Admission therefore repeats
    # this check deliberately as defense in depth.
    if action.action_id in state.consumed_actions:
        return _problem(
            "action_consumed",
            action.action_id,
            "The selected investigation is already represented in trusted consumed history.",
        )

    if state.remaining_investigations <= 0:
        return _problem(
            "budget_exhausted",
            action.action_id,
            "No semantic investigation budget remains at the current admission boundary.",
        )

    # Exact repository/revision binding protects source-identity freshness separately from
    # proposition/evidence freshness. The model never receives or echoes either value.
    if action.repository != state.repository or action.revision != state.revision:
        return _problem(
            "action_identity_stale",
            action.action_id,
            "The bound action source identity no longer matches the current trusted target identity.",
        )

    if action.mutation_class != "read_only":
        return _problem(
            "action_not_allowed_by_policy",
            action.action_id,
            "The current EvidenceGapPlanner experiment admits read-only investigations only.",
        )

    proposition = _find_proposition(state, action.target_proposition)
    if proposition is None:
        return _problem(
            "action_not_currently_actionable",
            action.action_id,
            "The action target proposition is absent from the current trusted state.",
        )
    if (
        proposition.state != action.required_proposition_state
        or proposition.evidence_coverage != action.required_evidence_coverage
    ):
        return _problem(
            "action_not_currently_actionable",
            action.action_id,
            "The latest trusted proposition state/coverage no longer satisfies the action precondition.",
        )

    return AdmittedInvestigationAction(
        action=action,
        explanation=decision.explanation,
    )


def _find_action(
    state: EvidenceGapAdmissionState,
    action_id: str,
) -> BoundInvestigationAction | None:
    return next((item for item in state.actions if item.action_id == action_id), None)


def _find_proposition(
    state: EvidenceGapAdmissionState,
    key: str,
) -> PropositionAssessment | None:
    return next((item for item in state.propositions if item.key == key), None)


def _problem(
    reason: EvidenceGapAdmissionProblemReason,
    action_id: str,
    detail: str,
) -> EvidenceGapAdmissionProblem:
    return EvidenceGapAdmissionProblem(
        reason=reason,
        action_id=action_id,
        detail=detail,
    )


def _trimmed(value: object) -> bool:
    return isinstance(value, str) and bool(value) and value == value.strip()


def _require_trimmed(value: object, name: str) -> None:
    if not _trimmed(value):
        raise ValueError(f"{name} must be non-empty trimmed text.")


def _require_canonical_repository(repository: str) -> None:
    if validate_repository(repository) != repository:
        raise ValueError("repository must already be canonical.")


def _require_canonical_revision(revision: str) -> None:
    if validate_commit_sha(revision) != revision:
        raise ValueError("revision must already be canonical lowercase hex.")


def _require_repository_path(path: str) -> None:
    parts = repository_relative_parts(path)
    if parts is None or "/".join(parts) != path:
        raise ValueError("path must be a normalized repository-relative POSIX path.")


__all__ = (
    "AdmittedInvestigationAction",
    "BoundInvestigationAction",
    "EvidenceGapAdmissionProblem",
    "EvidenceGapAdmissionProblemReason",
    "EvidenceGapAdmissionResult",
    "EvidenceGapAdmissionState",
    "TARGET_PYTHON_DECLARATION_ACTION_ID",
    "TARGET_PYTHON_DECLARATION_PATH",
    "TARGET_PYTHON_DECLARATION_PROPOSITION",
    "TARGET_PYTHON_DECLARATION_REQUIRED_COVERAGE",
    "TARGET_PYTHON_DECLARATION_REQUIRED_STATE",
    "TARGET_PYTHON_DECLARATION_RESULT_FAMILIES",
    "admit_selected_investigation_action",
    "build_target_python_declaration_action",
    "project_action_descriptor",
)
