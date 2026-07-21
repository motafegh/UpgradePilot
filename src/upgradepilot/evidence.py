"""Trusted normalized evidence contracts for the first automated slice."""

from __future__ import annotations

from typing import Literal, Self

from pydantic import (
    BaseModel,
    ConfigDict,
    ValidationInfo,
    field_validator,
    model_validator,
)

from upgradepilot.case_identity import InitialCaseRecord


EvidenceState = Literal["accepted", "missing"]
EvidenceKind = Literal[
    "dependency_diff",
    "upstream_release_notes",
    "automated_check",
    "repository_python_support",
]


def _normalize_required_text(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized


class EvidenceItem(BaseModel):
    """One normalized observation or one explicitly missing evidence need."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    evidence_id: str
    kind: EvidenceKind
    state: EvidenceState
    source: str
    observation: str | None = None
    limitations: tuple[str, ...] = ()

    @field_validator("evidence_id", "source")
    @classmethod
    def normalize_required_text(cls, value: str, info: ValidationInfo) -> str:
        return _normalize_required_text(value, info.field_name)

    @field_validator("observation")
    @classmethod
    def normalize_optional_observation(cls, value: str | None) -> str | None:
        if value is None:
            return None
        return _normalize_required_text(value, "observation")

    @field_validator("limitations")
    @classmethod
    def normalize_limitations(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        return tuple(
            _normalize_required_text(value, "limitation") for value in values
        )

    @model_validator(mode="after")
    def validate_state_content(self) -> Self:
        if self.state == "accepted" and self.observation is None:
            raise ValueError("accepted evidence must contain an observation")

        if self.state == "missing":
            if self.observation is not None:
                raise ValueError("missing evidence must not claim an observation")
            if not self.limitations:
                raise ValueError(
                    "missing evidence must explain the resulting limitation"
                )

        return self


class EvidenceSet(BaseModel):
    """Normalized evidence associated with one exact trusted case snapshot."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    case: InitialCaseRecord
    items: tuple[EvidenceItem, ...]

    @field_validator("items")
    @classmethod
    def validate_items(cls, items: tuple[EvidenceItem, ...]) -> tuple[EvidenceItem, ...]:
        if not items:
            raise ValueError("evidence set must contain at least one item")

        evidence_ids = [item.evidence_id for item in items]
        if len(evidence_ids) != len(set(evidence_ids)):
            raise ValueError("evidence_id values must be unique")

        return items
