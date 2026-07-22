"""Contracts and orchestration for bounded Python-support semantic extraction."""

from __future__ import annotations

from typing import Literal, Protocol

from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator

from upgradepilot.decision import AttributedPythonSupportClaim
from upgradepilot.evidence import EvidenceItem


PythonSupportClaimType = Literal["dropped", "added"]


def _normalize_required_text(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized


class CandidatePythonSupportClaim(BaseModel):
    """One untrusted Python-support claim proposed by an extractor."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    change: PythonSupportClaimType
    python_version: str
    source_quote: str

    @field_validator("python_version", "source_quote")
    @classmethod
    def normalize_required_text(cls, value: str, info: ValidationInfo) -> str:
        return _normalize_required_text(value, info.field_name)


class CandidateExtractionResult(BaseModel):
    """Untrusted structured output returned by one extraction method."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    claims: tuple[CandidatePythonSupportClaim, ...] = ()
    unresolved: tuple[str, ...] = ()

    @field_validator("unresolved")
    @classmethod
    def normalize_unresolved(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        return tuple(_normalize_required_text(value, "unresolved item") for value in values)


class GroundedPythonSupportClaim(BaseModel):
    """One model-derived claim that passed mechanical grounding controls."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    change: PythonSupportClaimType
    python_version: str
    evidence_id: str
    source_quote: str
    extractor_id: str
    authority: Literal["model_derived"]

    @field_validator(
        "python_version",
        "evidence_id",
        "source_quote",
        "extractor_id",
    )
    @classmethod
    def normalize_required_text(cls, value: str, info: ValidationInfo) -> str:
        return _normalize_required_text(value, info.field_name)

    def to_decision_claim(self) -> AttributedPythonSupportClaim:
        """Preserve model authority when crossing into the decision contract."""

        return AttributedPythonSupportClaim(
            change=self.change,
            python_version=self.python_version,
            evidence_ids=(self.evidence_id,),
            authority=self.authority,
            transformation_id=self.extractor_id,
        )


class ExtractionResult(BaseModel):
    """Validated application result for one evidence item's extraction attempt."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    grounded_claims: tuple[GroundedPythonSupportClaim, ...] = ()
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

    def to_decision_claims(self) -> tuple[AttributedPythonSupportClaim, ...]:
        """Convert grounded claims without erasing their model-derived authority."""

        return tuple(claim.to_decision_claim() for claim in self.grounded_claims)


class PythonSupportCandidateExtractor(Protocol):
    """Provider boundary required by the application orchestration service."""

    extractor_id: str

    def extract(self, text: str) -> CandidateExtractionResult: ...


class PythonSupportExtractionService:
    """Extract and mechanically ground claims from one evidence item."""

    def __init__(
        self,
        extractor: PythonSupportCandidateExtractor,
    ) -> None:
        self._extractor = extractor

    def extract(self, evidence: EvidenceItem) -> ExtractionResult:
        """Ground model claims without declaring their source statements true."""

        if evidence.observation is None:
            raise ValueError("extraction evidence must contain source text")

        candidates = self._extractor.extract(evidence.observation)

        # Local import avoids a module cycle: the validator consumes the contracts
        # defined in this module, while this service coordinates that validator.
        from upgradepilot.extraction_validation import validate_python_support_extraction

        extraction = validate_python_support_extraction(
            evidence=evidence,
            candidates=candidates,
            extractor_id=self._extractor.extractor_id,
        )
        return ExtractionResult(
            grounded_claims=extraction.grounded_claims,
            unresolved=extraction.unresolved,
            validation_errors=extraction.validation_errors,
        )
