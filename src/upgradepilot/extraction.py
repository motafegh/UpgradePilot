"""Contracts for bounded Python-support semantic extraction."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator

from upgradepilot.decision import PythonSupportChange


PythonSupportChangeType = Literal["dropped", "added"]


def _normalize_required_text(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized


class CandidatePythonSupportChange(BaseModel):
    """One untrusted Python-support fact proposed by an extractor."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    change: PythonSupportChangeType
    python_version: str
    source_quote: str

    @field_validator("python_version", "source_quote")
    @classmethod
    def normalize_required_text(cls, value: str, info: ValidationInfo) -> str:
        return _normalize_required_text(value, info.field_name)


class CandidateExtractionResult(BaseModel):
    """Untrusted structured output returned by one extraction method."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    facts: tuple[CandidatePythonSupportChange, ...] = ()
    unresolved: tuple[str, ...] = ()

    @field_validator("unresolved")
    @classmethod
    def normalize_unresolved(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        return tuple(_normalize_required_text(value, "unresolved item") for value in values)


class ExtractedPythonSupportChange(BaseModel):
    """One validated, source-grounded Python-support fact."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    change: PythonSupportChangeType
    python_version: str
    evidence_id: str
    source_quote: str
    extractor_id: str

    @field_validator(
        "python_version",
        "evidence_id",
        "source_quote",
        "extractor_id",
    )
    @classmethod
    def normalize_required_text(cls, value: str, info: ValidationInfo) -> str:
        return _normalize_required_text(value, info.field_name)

    def to_decision_fact(self) -> PythonSupportChange:
        """Convert the trusted extracted fact into the current decision contract."""

        return PythonSupportChange(
            change=self.change,
            python_version=self.python_version,
            evidence_ids=(self.evidence_id,),
        )


class ExtractionResult(BaseModel):
    """Validated application result for one evidence item's extraction attempt."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    accepted_facts: tuple[ExtractedPythonSupportChange, ...] = ()
    unresolved: tuple[str, ...] = ()
    validation_errors: tuple[str, ...] = ()

    @field_validator("unresolved", "validation_errors")
    @classmethod
    def normalize_messages(
        cls,
        values: tuple[str, ...],
        info: ValidationInfo,
    ) -> tuple[str, ...]:
        return tuple(_normalize_required_text(value, info.field_name) for value in values)
