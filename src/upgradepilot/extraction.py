"""Contracts and orchestration for bounded Python-support semantic extraction."""

from __future__ import annotations

from typing import Literal, Protocol

from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator

from upgradepilot.decision import PythonSupportChange
from upgradepilot.evidence import EvidenceItem


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

    def to_decision_facts(self) -> tuple[PythonSupportChange, ...]:
        """Convert every accepted extracted fact into current decision facts."""

        return tuple(fact.to_decision_fact() for fact in self.accepted_facts)


class PythonSupportCandidateExtractor(Protocol):
    """Provider boundary required by the application orchestration service."""

    extractor_id: str

    def extract(self, text: str) -> CandidateExtractionResult: ...


class PythonSupportExtractionService:
    """Coordinate model extraction and deterministic validation for one evidence item."""

    def __init__(self, extractor: PythonSupportCandidateExtractor) -> None:
        self._extractor = extractor

    def extract(self, evidence: EvidenceItem) -> ExtractionResult:
        """Extract candidate meaning, then validate it before returning trusted facts."""

        if evidence.observation is None:
            raise ValueError("extraction evidence must contain source text")

        candidates = self._extractor.extract(evidence.observation)

        # Local import avoids a module cycle: the validator consumes the contracts
        # defined in this module, while this service coordinates that validator.
        from upgradepilot.extraction_validation import validate_python_support_extraction

        return validate_python_support_extraction(
            evidence=evidence,
            candidates=candidates,
            extractor_id=self._extractor.extractor_id,
        )
