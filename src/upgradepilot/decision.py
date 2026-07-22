"""Deterministic decision contracts and the first bounded UpgradePilot rule."""

from __future__ import annotations

from typing import Literal, Self

from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator, model_validator

from upgradepilot.evidence import EvidenceSet


DecisionOutcome = Literal["run_targeted_checks", "abstain"]
PythonSupportClaimType = Literal["dropped", "added"]
ClaimAuthorityLevel = Literal["model_derived"]


def _normalize_required_text(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized


def _normalize_text_tuple(
    values: tuple[str, ...],
    field_name: str,
) -> tuple[str, ...]:
    return tuple(_normalize_required_text(value, field_name) for value in values)


class AttributedPythonSupportClaim(BaseModel):
    """One decision claim with explicit source and transformation authority."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    change: PythonSupportClaimType
    python_version: str
    evidence_ids: tuple[str, ...]
    authority: ClaimAuthorityLevel
    transformation_id: str

    @field_validator("python_version")
    @classmethod
    def normalize_python_version(cls, value: str) -> str:
        return _normalize_required_text(value, "python_version")

    @field_validator("evidence_ids")
    @classmethod
    def validate_evidence_ids(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        normalized = _normalize_text_tuple(values, "evidence_id")
        if not normalized:
            raise ValueError("evidence_ids must contain at least one value")
        if len(normalized) != len(set(normalized)):
            raise ValueError("evidence_ids must be unique")
        return normalized

    @field_validator("transformation_id")
    @classmethod
    def normalize_transformation_id(cls, value: str) -> str:
        return _normalize_required_text(value, "transformation_id")


class DecisionInput(BaseModel):
    """Explicit evidence and authority-bearing claims consumed by one policy."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    evidence: EvidenceSet
    python_support_claims: tuple[AttributedPythonSupportClaim, ...]
    policy_version: str

    @field_validator("policy_version")
    @classmethod
    def normalize_policy_version(cls, value: str) -> str:
        return _normalize_required_text(value, "policy_version")

    @model_validator(mode="after")
    def validate_claim_references(self) -> Self:
        evidence_by_id = {
            item.evidence_id: item
            for item in self.evidence.items
        }

        for claim in self.python_support_claims:
            for evidence_id in claim.evidence_ids:
                evidence_item = evidence_by_id.get(evidence_id)
                if evidence_item is None:
                    raise ValueError(
                        f"python support claim references unknown evidence_id: "
                        f"{evidence_id}"
                    )
                if evidence_item.state != "accepted":
                    raise ValueError(
                        f"python support claim must reference accepted evidence: "
                        f"{evidence_id}"
                    )

        return self


class DecisionReason(BaseModel):
    """One traceable reason supporting a deterministic decision."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    reason_code: str
    summary: str
    evidence_ids: tuple[str, ...]

    @field_validator("reason_code", "summary")
    @classmethod
    def normalize_required_text(cls, value: str, info: ValidationInfo) -> str:
        return _normalize_required_text(value, info.field_name)

    @field_validator("evidence_ids")
    @classmethod
    def normalize_evidence_ids(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        return _normalize_text_tuple(values, "evidence_id")


class DecisionResult(BaseModel):
    """The bounded recommendation produced by one policy version."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    outcome: DecisionOutcome
    reasons: tuple[DecisionReason, ...]
    targeted_checks: tuple[str, ...]
    limitations: tuple[str, ...]
    policy_version: str

    @field_validator("reasons")
    @classmethod
    def validate_reasons(
        cls,
        values: tuple[DecisionReason, ...],
    ) -> tuple[DecisionReason, ...]:
        if not values:
            raise ValueError("decision result must contain at least one reason")
        return values

    @field_validator("targeted_checks")
    @classmethod
    def normalize_targeted_checks(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        return _normalize_text_tuple(values, "targeted_check")

    @field_validator("limitations")
    @classmethod
    def normalize_limitations(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        return _normalize_text_tuple(values, "limitation")

    @field_validator("policy_version")
    @classmethod
    def normalize_policy_version(cls, value: str) -> str:
        return _normalize_required_text(value, "policy_version")

    @model_validator(mode="after")
    def validate_outcome_content(self) -> Self:
        if self.outcome == "run_targeted_checks" and not self.targeted_checks:
            raise ValueError(
                "run_targeted_checks outcome must contain targeted checks"
            )
        return self


def evaluate_decision(decision_input: DecisionInput) -> DecisionResult:
    """Apply the first bounded deterministic UpgradePilot policy."""

    dropped_claims = tuple(
        claim
        for claim in decision_input.python_support_claims
        if claim.change == "dropped"
    )
    missing_repository_support = tuple(
        item
        for item in decision_input.evidence.items
        if (
            item.kind == "repository_python_support"
            and item.state == "missing"
        )
    )

    if dropped_claims and missing_repository_support:
        versions = ", ".join(
            sorted({claim.python_version for claim in dropped_claims})
        )
        supporting_ids = tuple(
            dict.fromkeys(
                evidence_id
                for claim in dropped_claims
                for evidence_id in claim.evidence_ids
            )
        ) + tuple(
            item.evidence_id
            for item in missing_repository_support
        )

        # Model-derived claims can increase scrutiny, but this policy exposes no
        # path for them to justify merge or otherwise reduce caution.
        return DecisionResult(
            outcome="run_targeted_checks",
            reasons=(
                DecisionReason(
                    reason_code="PYTHON_SUPPORT_DROP_UNRESOLVED",
                    summary=(
                        f"Grounded model-derived evidence reports dropped "
                        f"Python support for {versions}, "
                        "but repository Python-support evidence is missing."
                    ),
                    evidence_ids=supporting_ids,
                ),
            ),
            targeted_checks=(
                "Inspect the repository's declared Python support.",
                "Inspect the CI matrix for affected Python versions.",
                "Determine whether the dependency is used under those versions.",
            ),
            limitations=(
                "Repository compatibility has not been established.",
                "The Python-support claim is model-derived and not independently corroborated.",
                "The result does not prove that the update is safe or incompatible.",
            ),
            policy_version=decision_input.policy_version,
        )

    return DecisionResult(
        outcome="abstain",
        reasons=(
            DecisionReason(
                reason_code="NO_SUPPORTED_DECISION_RULE",
                summary=(
                    "The current bounded policy has no rule that supports "
                    "a stronger recommendation."
                ),
                evidence_ids=(),
            ),
        ),
        targeted_checks=(),
        limitations=(
            "Only the initial Python-support-drop rule is implemented.",
        ),
        policy_version=decision_input.policy_version,
    )
