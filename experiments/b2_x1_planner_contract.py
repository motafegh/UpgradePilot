"""Deterministic contract/admission boundary for the B2/X1 planner experiment.

This module is experiment support code, not UpgradePilot product runtime code.

Phase 1 found one clean first planner seam: typed candidate-applicability state already
contains unresolved propositions, and the Python-support mechanism already defines one
real discriminating read-only investigation, ``acquire_exact_target_python_declaration``.

The planner is deliberately weaker than the deterministic application around it:

``trusted snapshot + deterministic action catalog + untrusted model-shaped plan``
    -> ``admit_agent_plan(...)``
    -> one admitted read-only action OR an explicit no-tool disposition/problem

This module does **not** execute the action, acquire repository data, interpret target
Python evidence, promote evidence state, call a model, or authorize product mutation.
Those responsibilities remain with their existing owners.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

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
    "action_identity_mismatch",
    "action_arguments_mismatch",
    "target_proposition_mismatch",
    "target_proposition_not_actionable",
]

TARGET_PYTHON_DECLARATION_ACTION_ID = "acquire_exact_target_python_declaration"
TARGET_PYTHON_DECLARATION_PROPOSITION = "exact_target_python_declaration_established"
TARGET_PYTHON_DECLARATION_PATH = "pyproject.toml"


@dataclass(frozen=True, slots=True)
class InvestigationActionArguments:
    """Exact model-supplied locator arguments that deterministic admission must bind."""

    repository: str
    revision: str
    path: str


@dataclass(frozen=True, slots=True)
class AllowedInvestigationAction:
    """One deterministically constructed action the planner may propose, never authorize."""

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
            not isinstance(item, str) or not item.strip() or item != item.strip()
            for item in self.result_families
        ):
            raise ValueError("result_families must contain non-empty trimmed names.")


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

    ``propositions`` are already evaluated by product/domain code. The planner may use
    their state and coverage to choose a useful investigation; it may not rewrite them.
    ``allowed_actions`` is also application-owned and therefore part of trusted state,
    not a model-generated tool list.
    """

    repository: str
    pull_number: int
    revision: str
    propositions: tuple[PropositionAssessment, ...]
    attempted_actions: tuple[AttemptedInvestigationAction, ...]
    allowed_actions: tuple[AllowedInvestigationAction, ...]
    remaining_steps: int

    def __post_init__(self) -> None:
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


@dataclass(frozen=True, slots=True)
class AgentPlanResult:
    """Untrusted structured planner output before deterministic admission.

    The dataclass intentionally does not grant authority merely because fields are typed.
    ``admit_agent_plan`` validates state/action/identity/argument coherence against the
    trusted snapshot.
    """

    state: PlannerPlanState | str
    selected_action_id: str | None
    arguments: InvestigationActionArguments | None
    target_proposition: str
    reason: str
    expected_result_categories: tuple[str, ...]
    limitations: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class AdmittedInvestigationAction:
    """One read-only action proven admissible for the exact trusted snapshot."""

    action: AllowedInvestigationAction
    arguments: InvestigationActionArguments
    target_proposition: str


@dataclass(frozen=True, slots=True)
class AdmittedNoToolDisposition:
    """A planner stop/defer/unresolved result that authorizes no capability execution."""

    state: Literal["stop", "defer", "unresolved"]
    target_proposition: str
    reason: str


@dataclass(frozen=True, slots=True)
class PlanAdmissionProblem:
    """Why untrusted planner output was not admitted to an investigation action."""

    reason: AdmissionProblemReason
    detail: str


type PlanAdmissionResult = (
    AdmittedInvestigationAction | AdmittedNoToolDisposition | PlanAdmissionProblem
)


def build_target_python_declaration_action(
    repository: str,
    revision: str,
) -> AllowedInvestigationAction:
    """Build the one real Phase-2 action from trusted exact PR identity.

    The path and target proposition are fixed by the existing Python-support mechanism;
    the planner is not allowed to choose an arbitrary repository file.
    """

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


def admit_agent_plan(
    snapshot: InvestigationSnapshot,
    plan: AgentPlanResult,
) -> PlanAdmissionResult:
    """Admit one model-shaped plan without granting the model evidence/tool authority."""

    if plan.state in {"stop", "defer", "unresolved"}:
        if plan.selected_action_id is not None or plan.arguments is not None:
            return _problem(
                "invalid_plan_shape",
                "A no-tool planner disposition cannot include an action or arguments.",
            )
        if not _trimmed(plan.reason) or not _trimmed(plan.target_proposition):
            return _problem(
                "invalid_plan_shape",
                "A no-tool disposition requires a non-empty reason and target proposition.",
            )
        if _find_proposition(snapshot, plan.target_proposition) is None:
            return _problem(
                "target_proposition_mismatch",
                "The planner disposition refers to a proposition absent from the trusted snapshot.",
            )
        return AdmittedNoToolDisposition(
            state=plan.state,
            target_proposition=plan.target_proposition,
            reason=plan.reason,
        )

    if plan.state != "choose_action":
        return _problem("invalid_plan_shape", "The planner result state is unsupported.")
    if (
        not _trimmed(plan.selected_action_id)
        or plan.arguments is None
        or not _trimmed(plan.reason)
        or not _trimmed(plan.target_proposition)
    ):
        return _problem(
            "invalid_plan_shape",
            "choose_action requires an action id, arguments, reason, and target proposition.",
        )

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
            "The planner cannot blindly repeat an action already represented in attempt history.",
        )
    if snapshot.remaining_steps <= 0:
        return _problem(
            "budget_exhausted",
            "The planner has no remaining admitted investigation step budget.",
        )

    # The deterministic catalog itself must remain bound to the exact case. This prevents
    # a stale/misconstructed catalog from becoming authority merely because the model chose it.
    if action.repository != snapshot.repository or action.revision != snapshot.revision:
        return _problem(
            "action_identity_mismatch",
            "The selected catalog action is not bound to the snapshot repository/revision.",
        )

    arguments = plan.arguments
    if (
        arguments.repository != action.repository
        or arguments.revision != action.revision
        or arguments.path != action.path
    ):
        return _problem(
            "action_arguments_mismatch",
            "Planner arguments must exactly match the trusted action locator; arbitrary source selection is not admitted.",
        )
    if plan.target_proposition != action.target_proposition:
        return _problem(
            "target_proposition_mismatch",
            "The planner target proposition does not match the selected action's purpose.",
        )

    proposition = _find_proposition(snapshot, action.target_proposition)
    if proposition is None:
        return _problem(
            "target_proposition_mismatch",
            "The selected action's target proposition is absent from the trusted snapshot.",
        )
    if (
        proposition.state != action.required_proposition_state
        or proposition.evidence_coverage != action.required_evidence_coverage
    ):
        return _problem(
            "target_proposition_not_actionable",
            "The trusted proposition state/coverage no longer satisfies this action's precondition.",
        )

    return AdmittedInvestigationAction(
        action=action,
        arguments=arguments,
        target_proposition=plan.target_proposition,
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


__all__ = (
    "AdmittedInvestigationAction",
    "AdmittedNoToolDisposition",
    "AgentPlanResult",
    "AllowedInvestigationAction",
    "AttemptedInvestigationAction",
    "InvestigationActionArguments",
    "InvestigationSnapshot",
    "PlanAdmissionProblem",
    "PlanAdmissionResult",
    "TARGET_PYTHON_DECLARATION_ACTION_ID",
    "TARGET_PYTHON_DECLARATION_PATH",
    "TARGET_PYTHON_DECLARATION_PROPOSITION",
    "admit_agent_plan",
    "build_target_python_declaration_action",
)
