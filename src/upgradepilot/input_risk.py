"""General pre-extraction risk assessment for untrusted natural-language evidence."""

from __future__ import annotations

import hashlib
import unicodedata
from typing import Literal, Protocol

from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator


InputRiskLevel = Literal["none_detected", "suspicious", "high"]
InputRiskSignalType = Literal[
    "instruction_override",
    "output_manipulation",
    "role_impersonation",
    "tool_request",
    "secret_request",
    "encoded_or_concealed_instruction",
    "other_instruction_like_content",
]
InputRiskRoute = Literal["proceed", "quarantine"]


def _normalize_required_text(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized


class CandidateInputRiskSignal(BaseModel):
    """One untrusted security signal proposed by a detector."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    signal_type: InputRiskSignalType
    source_quote: str
    explanation: str

    @field_validator("source_quote", "explanation")
    @classmethod
    def normalize_required_text(cls, value: str, info: ValidationInfo) -> str:
        return _normalize_required_text(value, info.field_name)


class CandidateInputRiskAssessment(BaseModel):
    """Untrusted structured result returned by an input-risk detector."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    risk_level: InputRiskLevel
    signals: tuple[CandidateInputRiskSignal, ...] = ()
    unresolved: tuple[str, ...] = ()

    @field_validator("unresolved")
    @classmethod
    def normalize_unresolved(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        return tuple(
            _normalize_required_text(value, "unresolved item") for value in values
        )


class PreparedUntrustedText(BaseModel):
    """Inspection view derived without mutating the preserved source evidence."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    inspection_text: str
    inspection_sha256: str
    preprocessing_findings: tuple[str, ...] = ()


class InputRiskAssessment(BaseModel):
    """Validated detector evidence plus the deterministic extraction route."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    detector_id: str
    risk_level: InputRiskLevel
    signals: tuple[CandidateInputRiskSignal, ...] = ()
    unresolved: tuple[str, ...] = ()
    validation_errors: tuple[str, ...] = ()
    preprocessing_findings: tuple[str, ...] = ()
    inspection_sha256: str
    route: InputRiskRoute
    limitation: str = (
        "Input-risk detection reduces exposure but does not establish that text is safe."
    )

    @field_validator(
        "detector_id",
        "inspection_sha256",
        "limitation",
    )
    @classmethod
    def normalize_required_text(cls, value: str, info: ValidationInfo) -> str:
        return _normalize_required_text(value, info.field_name)


class InputRiskDetectionError(RuntimeError):
    """Raised when a detector cannot produce a schema-valid assessment."""

    def __init__(self, message: str, *, raw_output: str | None = None) -> None:
        super().__init__(message)
        self.raw_output = raw_output


class InputRiskDetector(Protocol):
    """Provider boundary for general untrusted-input risk detection."""

    detector_id: str

    def assess(self, text: str) -> CandidateInputRiskAssessment: ...


def prepare_untrusted_text(text: str) -> PreparedUntrustedText:
    """Create a normalized inspection view and expose suspicious control data."""

    if not text.strip():
        raise ValueError("untrusted input text must not be empty")

    normalized_newlines = text.replace("\r\n", "\n").replace("\r", "\n")
    inspection_text = unicodedata.normalize("NFKC", normalized_newlines)
    findings: list[str] = []

    if inspection_text != normalized_newlines:
        findings.append("UNICODE_NORMALIZATION_APPLIED")

    for character in text:
        category = unicodedata.category(character)
        if category in {"Cc", "Cf"} and character not in {"\n", "\r", "\t"}:
            findings.append("SUSPICIOUS_CONTROL_CHARACTER")
            break

    return PreparedUntrustedText(
        inspection_text=inspection_text,
        inspection_sha256=hashlib.sha256(
            inspection_text.encode("utf-8")
        ).hexdigest(),
        preprocessing_findings=tuple(findings),
    )


def validate_input_risk_assessment(
    *,
    prepared: PreparedUntrustedText,
    candidate: CandidateInputRiskAssessment,
    detector_id: str,
) -> InputRiskAssessment:
    """Validate detector grounding and choose a fail-closed extraction route."""

    normalized_detector_id = detector_id.strip()
    if not normalized_detector_id:
        raise ValueError("detector_id must not be empty")

    validation_errors: list[str] = []
    if candidate.risk_level == "none_detected" and candidate.signals:
        validation_errors.append("NONE_DETECTED_WITH_SIGNALS")
    if candidate.risk_level in {"suspicious", "high"} and not candidate.signals:
        validation_errors.append("RISK_LEVEL_WITHOUT_SIGNALS")

    for index, signal in enumerate(candidate.signals):
        if signal.source_quote not in prepared.inspection_text:
            validation_errors.append(f"signal[{index}]: SOURCE_QUOTE_NOT_FOUND")

    route: InputRiskRoute = "proceed"
    if (
        candidate.risk_level != "none_detected"
        or candidate.unresolved
        or validation_errors
        or prepared.preprocessing_findings
    ):
        route = "quarantine"

    return InputRiskAssessment(
        detector_id=normalized_detector_id,
        risk_level=candidate.risk_level,
        signals=candidate.signals,
        unresolved=candidate.unresolved,
        validation_errors=tuple(validation_errors),
        preprocessing_findings=prepared.preprocessing_findings,
        inspection_sha256=prepared.inspection_sha256,
        route=route,
    )


def failed_input_risk_assessment(
    *,
    prepared: PreparedUntrustedText,
    detector_id: str,
    error: InputRiskDetectionError,
) -> InputRiskAssessment:
    """Represent a detector failure as explicit quarantine evidence."""

    return InputRiskAssessment(
        detector_id=detector_id,
        risk_level="high",
        unresolved=(f"INPUT_RISK_DETECTOR_ERROR: {error}",),
        preprocessing_findings=prepared.preprocessing_findings,
        inspection_sha256=prepared.inspection_sha256,
        route="quarantine",
    )
