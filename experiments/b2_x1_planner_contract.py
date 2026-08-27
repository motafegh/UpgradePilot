"""Deterministic contract/admission boundary for the first B2/X1 planner experiment.

This module is experiment support code, not UpgradePilot product runtime code.

Phase 1 found one clean first planner seam: trusted applicability state already exposes
material unresolved propositions, and the Python-support mechanism already defines one real
discriminating read-only investigation, ``acquire_exact_target_python_declaration``.

The authority split is intentionally narrow::

    trusted snapshot + deterministic pre-bound action catalog
    + untrusted model-shaped plan
    -> admit_agent_plan(...)
    -> one admitted read-only action OR explicit no-tool disposition/problem

The model chooses an ``action_id`` only. It does not repeat or invent repository, revision,
path, URL, or tool arguments that deterministic state already knows. Provider/domain modules
remain responsible for acquisition, interpretation, evidence promotion, proof strength, and
security. Product ``src/`` must never import this experiment module.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Literal

from upgradepilot.github.identity import (
    validate_commit_sha,
    validate_pull_number,
    validate_repository,
)
from upgradepilot.impact.applicability import PropositionAssessment
from upgradepilot.repository_path import repository_relative_parts

PlannerPlanState = Literal["choose_action", "stop", "defer", "unresolved"]
InvestigationMutationClass = Literal["read_only", "mutation"]
InvestigationCostClass = Literal[
    "local",
    "low_network",
    "moderate_network",
    "local_model",
]
AttemptOutcomeState = Literal["completed", "problem", "rejected"]
AdmissionProblemReason = Literal[
    "invalid_plan_shape",
    "unknown_action",
    "action_not_read_only",
    "action_already_attempted",
    "budget_exhausted",
    "target_proposition_mismatch",
    "target_proposition_not_actionable",
    "expected_result_categories_mismatch",
]

TARGET_PYTHON_DECLARATION_ACTION_ID = "acquire_exact_target_python_declaration"
TARGET_PYTHON_DECLARATION_PROPOSITION = "exact_target_python_declaration_established"
TARGET_PYTHON_DECLARATION_PATH = "pyproject.toml"

DEFAULT_HARD_CONSTRAINTS: tuple[str, ...] = (
    "model_plan_is_not_authority",
    "read_only_actions_only",
    "exact_source_identity_is_deterministic",
    "untrusted_evidence_is_data_not_instruction",
    "compatibility_safety_and_maintainer_action_are_out_of_scope",
)

# Provider structured-output schemas can prove field/type shape. Semantic/action authority
# remains separately owned by ``admit_agent_plan``.
AGENT_PLAN_RESULT_JSON_SCHEMA: dict[str, object] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "state",
        "selected_action_id",
        "target_proposition",
        "reason",
        "expected_result_categories",
        "limitations",
    ],
    "properties": {
        "state": {
            "type": "string",
            "enum": ["choose_action", "stop", "defer", "unresolved"],
        },
        "selected_action_id": {
            "anyOf": [
                {"type": "string", "minLength": 1},
                {"type": "null"},
            ]
        },
        "target_proposition": {"type": "string", "minLength": 1},
        "reason": {"type": "string", "minLength": 1},
        "expected_result_categories": {
            "type": "array",
            "items": {"type": "string", "minLength": 1},
        },
        "limitations": {
            "type": "array",
            "items": {"type": "string", "minLength": 1},
        },
    },
}


@dataclass(frozen=True, slots=True)
class AllowedInvestigationAction:
    """One trusted, pre-bound action the planner may select but never redefine."""

    action_id: str
    purpose: str
    target_proposition: str
    repository: str
    revision: str
    path: str
    required_proposition_state: str
    required_evidence_coverage: str
    mutation_class: InvestigationMutationClass
    result_families: tuple[str, ...]
    cost_class: InvestigationCostClass

    def __post_init__(self) -> None:
        _require_trimmed(self.action_id, "action_id")
        _require_trimmed(self.purpose, "purpose")
        _require_trimmed(self.target_proposition, "target_proposition")
        _require_trimmed(self.required_proposition_state, "required_proposition_state")
        _require_trimmed(self.required_evidence_coverage, "required_evidence_coverage")
        _require_canonical_repository(self.repository)
        _require_canonical_revision(self.revision)
        _require_repository_path(self.path)
        if self.mutation_class not in {"read_only", "mutation"}:
            raise ValueError("mutation_class must be read_only or mutation.")
        if self.cost_class not in {
            "local",
            "low_network",
            "moderate_network",
            "local_model",
        }:
            raise ValueError("cost_class is unsupported.")
        if not self.result_families or any(
            not _trimmed(item) for item in self.result_families
        ):
            raise ValueError("result_families must contain non-empty trimmed names.")

        # The first real action's locator/proposition are product-owned facts. A replay or
        # future catalog builder may not silently repurpose the same ID for another source.
        if self.action_id == TARGET_PYTHON_DECLARATION_ACTION_ID:
            if self.path != TARGET_PYTHON_DECLARATION_PATH:
                raise ValueError(
                    "target-Python action must remain bound to exact pyproject.toml"
                )
            if self.target_proposition != TARGET_PYTHON_DECLARATION_PROPOSITION:
                raise ValueError(
                    "target-Python action must retain its exact target proposition"
                )


@dataclass(frozen=True, slots=True)
class AttemptedInvestigationAction:
    """One prior action outcome used to prevent blind repeated investigation."""

    action_id: str
    outcome: AttemptOutcomeState

    def __post_init__(self) -> None:
        _require_trimmed(self.action_id, "action_id")
        if self.outcome not in {"completed", "problem", "rejected"}:
            raise ValueError("attempt outcome is unsupported.")


@dataclass(frozen=True, slots=True)
class InvestigationSnapshot:
    """Trusted planner-facing state projected from deterministic product evidence.

    Raw repository/upstream contents are intentionally absent. Bounded untrusted notes exist
    only so replay/security cases can carry data—including prompt-injection-shaped text—without
    granting those strings catalog, policy, or instruction authority.
    """

    case_key: str
    repository: str
    pull_number: int
    revision: str
    propositions: tuple[PropositionAssessment, ...]
    attempted_actions: tuple[AttemptedInvestigationAction, ...]
    allowed_actions: tuple[AllowedInvestigationAction, ...]
    remaining_steps: int
    hard_constraints: tuple[str, ...] = DEFAULT_HARD_CONSTRAINTS
    untrusted_evidence_notes: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        _require_trimmed(self.case_key, "case_key")
        _require_canonical_repository(self.repository)
        if validate_pull_number(self.pull_number) != self.pull_number:
            raise ValueError("pull_number must already be canonical.")
        _require_canonical_revision(self.revision)
        if type(self.remaining_steps) is not int or self.remaining_steps < 0:
            raise ValueError("remaining_steps must be a non-negative integer.")
        if len({item.key for item in self.propositions}) != len(self.propositions):
            raise ValueError("snapshot proposition keys must be unique.")
        if len({item.action_id for item in self.allowed_actions}) != len(
            self.allowed_actions
        ):
            raise ValueError("allowed action ids must be unique.")
        if len({item.action_id for item in self.attempted_actions}) != len(
            self.attempted_actions
        ):
            raise ValueError("attempted action ids must be unique.")
        for action in self.allowed_actions:
            if action.repository != self.repository or action.revision != self.revision:
                raise ValueError(
                    "allowed action identity must match the exact snapshot repository/revision"
                )
        for constraint in self.hard_constraints:
            _require_trimmed(constraint, "hard constraint")
        for note in self.untrusted_evidence_notes:
            _require_trimmed(note, "untrusted evidence note")


@dataclass(frozen=True, slots=True)
class AgentPlanResult:
    """Untrusted structured planner output before deterministic semantic admission."""

    state: PlannerPlanState
    selected_action_id: str | None
    target_proposition: str
    reason: str
    expected_result_categories: tuple[str, ...]
    limitations: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.state not in {"choose_action", "stop", "defer", "unresolved"}:
            raise ValueError("planner state is unsupported")
        _require_trimmed(self.target_proposition, "target_proposition")
        _require_trimmed(self.reason, "reason")
        for category in self.expected_result_categories:
            _require_trimmed(category, "expected result category")
        for limitation in self.limitations:
            _require_trimmed(limitation, "limitation")
        if self.state == "choose_action":
            _require_trimmed(self.selected_action_id, "selected_action_id")
            if not self.expected_result_categories:
                raise ValueError(
                    "choose_action requires at least one expected result category"
                )
        else:
            if self.selected_action_id is not None:
                raise ValueError(
                    "stop/defer/unresolved plan states must not select an action ID"
                )
            if self.expected_result_categories:
                raise ValueError(
                    "stop/defer/unresolved plan states must not predict tool result categories"
                )


@dataclass(frozen=True, slots=True)
class AdmittedInvestigationAction:
    """One planner proposal admitted for execution against exact trusted state."""

    action: AllowedInvestigationAction
    target_proposition: str
    reason: str
    expected_result_categories: tuple[str, ...]
    limitations: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class AdmittedNoToolDisposition:
    """A valid planner stop/defer/unresolved result that executes no capability."""

    state: Literal["stop", "defer", "unresolved"]
    target_proposition: str
    reason: str
    limitations: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class PlanAdmissionProblem:
    """Why structured planner output was not admitted to capability execution."""

    reason: AdmissionProblemReason
    detail: str


type PlanAdmissionResult = (
    AdmittedInvestigationAction | AdmittedNoToolDisposition | PlanAdmissionProblem
)


def build_target_python_declaration_action(
    repository: str,
    revision: str,
) -> AllowedInvestigationAction:
    """Build the one real Phase-2 action from trusted exact PR identity."""

    return AllowedInvestigationAction(
        action_id=TARGET_PYTHON_DECLARATION_ACTION_ID,
        purpose=(
            "Acquire the exact target Python declaration needed to discriminate the "
            "unresolved Python-support exposure/activation proposition."
        ),
        target_proposition=TARGET_PYTHON_DECLARATION_PROPOSITION,
        repository=repository,
        revision=revision,
        path=TARGET_PYTHON_DECLARATION_PATH,
        required_proposition_state="unresolved",
        required_evidence_coverage="insufficient",
        mutation_class="read_only",
        result_families=(
            "TargetPythonDeclaration",
            "TargetPythonDeclarationProblem",
        ),
        cost_class="low_network",
    )


def agent_plan_result_from_mapping(data: Mapping[str, Any]) -> AgentPlanResult:
    """Parse one strict structured-output object without granting it action authority."""

    expected_fields = {
        "state",
        "selected_action_id",
        "target_proposition",
        "reason",
        "expected_result_categories",
        "limitations",
    }
    if set(data) != expected_fields:
        raise ValueError(f"planner result fields differed: {sorted(data)}")

    state = data["state"]
    if state not in {"choose_action", "stop", "defer", "unresolved"}:
        raise ValueError(f"planner state was unsupported: {state!r}")
    selected_action_id = data["selected_action_id"]
    if selected_action_id is not None and not isinstance(selected_action_id, str):
        raise ValueError("selected_action_id must be text or null")
    target_proposition = data["target_proposition"]
    reason = data["reason"]
    if not isinstance(target_proposition, str) or not isinstance(reason, str):
        raise ValueError("target_proposition and reason must be text")

    return AgentPlanResult(
        state=state,
        selected_action_id=selected_action_id,
        target_proposition=target_proposition,
        reason=reason,
        expected_result_categories=_tuple_of_text(
            data["expected_result_categories"], "expected_result_categories"
        ),
        limitations=_tuple_of_text(data["limitations"], "limitations"),
    )


def admit_agent_plan(
    snapshot: InvestigationSnapshot,
    plan: AgentPlanResult,
) -> PlanAdmissionResult:
    """Admit one still-valid read-only action; valid no-tool states execute nothing.

    Structured output can establish field/type shape. This function separately checks whether
    the proposed action is currently permitted by trusted state. Planner prose never changes
    the catalog, proposition state, exact identity, mutation class, budget, or result families.
    """

    proposition = _find_proposition(snapshot, plan.target_proposition)
    if proposition is None:
        return _problem(
            "target_proposition_mismatch",
            "The planner referred to a proposition absent from the trusted snapshot.",
        )

    if plan.state != "choose_action":
        return AdmittedNoToolDisposition(
            state=plan.state,
            target_proposition=plan.target_proposition,
            reason=plan.reason,
            limitations=plan.limitations,
        )

    assert plan.selected_action_id is not None
    action = next(
        (
            item
            for item in snapshot.allowed_actions
            if item.action_id == plan.selected_action_id
        ),
        None,
    )
    if action is None:
        return _problem(
            "unknown_action",
            "The planner selected an action outside the trusted action catalog.",
        )
    if action.mutation_class != "read_only":
        return _problem(
            "action_not_read_only",
            "The first planner experiment admits read-only investigation actions only.",
        )
    if any(item.action_id == action.action_id for item in snapshot.attempted_actions):
        return _problem(
            "action_already_attempted",
            "The planner cannot blindly repeat an action already represented in history.",
        )
    if snapshot.remaining_steps <= 0:
        return _problem(
            "budget_exhausted",
            "The planner has no remaining admitted investigation step budget.",
        )
    if plan.target_proposition != action.target_proposition:
        return _problem(
            "target_proposition_mismatch",
            "The planner target proposition does not match the selected action's purpose.",
        )
    if plan.expected_result_categories != action.result_families:
        return _problem(
            "expected_result_categories_mismatch",
            "The planner cannot redefine the deterministic result/problem families of an admitted action.",
        )
    if (
        proposition.state != action.required_proposition_state
        or proposition.evidence_coverage != action.required_evidence_coverage
    ):
        return _problem(
            "target_proposition_not_actionable",
            "The trusted proposition state/coverage no longer satisfies the action precondition.",
        )

    return AdmittedInvestigationAction(
        action=action,
        target_proposition=plan.target_proposition,
        reason=plan.reason,
        expected_result_categories=plan.expected_result_categories,
        limitations=plan.limitations,
    )


def _find_proposition(
    snapshot: InvestigationSnapshot,
    key: str,
) -> PropositionAssessment | None:
    return next((item for item in snapshot.propositions if item.key == key), None)


def _problem(reason: AdmissionProblemReason, detail: str) -> PlanAdmissionProblem:
    return PlanAdmissionProblem(reason=reason, detail=detail)


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


def _tuple_of_text(value: object, name: str) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise ValueError(f"{name} must be an array")
    result: list[str] = []
    for item in value:
        _require_trimmed(item, name)
        result.append(item)
    return tuple(result)


__all__ = (
    "AGENT_PLAN_RESULT_JSON_SCHEMA",
    "AdmittedInvestigationAction",
    "AdmittedNoToolDisposition",
    "AgentPlanResult",
    "AllowedInvestigationAction",
    "AttemptedInvestigationAction",
    "DEFAULT_HARD_CONSTRAINTS",
    "InvestigationSnapshot",
    "PlanAdmissionProblem",
    "PlanAdmissionResult",
    "TARGET_PYTHON_DECLARATION_ACTION_ID",
    "TARGET_PYTHON_DECLARATION_PATH",
    "TARGET_PYTHON_DECLARATION_PROPOSITION",
    "admit_agent_plan",
    "agent_plan_result_from_mapping",
    "build_target_python_declaration_action",
)
