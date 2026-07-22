"""Deterministic validation for untrusted semantic-extraction output."""

from __future__ import annotations

import re

from upgradepilot.evidence import EvidenceItem
from upgradepilot.extraction import (
    CandidateExtractionResult,
    ExtractionResult,
    GroundedPythonSupportClaim,
)


_PYTHON_VERSION_PATTERN = re.compile(r"^[0-9]+\.[0-9]+$")


def _has_unique_quote(source: str, quote: str) -> bool:
    """Return whether the exact quote has one unambiguous source occurrence."""

    quote_start = source.find(quote)
    return quote_start >= 0 and source.find(quote, quote_start + 1) < 0


def validate_python_support_extraction(
    *,
    evidence: EvidenceItem,
    candidates: CandidateExtractionResult,
    extractor_id: str,
) -> ExtractionResult:
    """Mechanically ground candidate claims in one release-note evidence item.

    This validator proves structure, evidence eligibility, unique literal quote
    grounding, version grounding, and candidate identity consistency. It does
    not prove source truth, semantic correctness,
    corroboration, or prompt-injection resistance.
    """

    normalized_extractor_id = extractor_id.strip()
    if not normalized_extractor_id:
        raise ValueError("extractor_id must not be empty")

    if evidence.state != "accepted":
        raise ValueError("semantic extraction requires accepted evidence")
    if evidence.kind != "upstream_release_notes":
        raise ValueError(
            "Python-support extraction currently supports upstream release notes only"
        )
    if evidence.observation is None:
        raise ValueError("accepted extraction evidence must contain source text")

    grounded: list[GroundedPythonSupportClaim] = []
    validation_errors: list[str] = []
    seen: set[tuple[str, str, str]] = set()

    for index, candidate in enumerate(candidates.claims):
        prefix = f"candidate[{index}]"

        if not _PYTHON_VERSION_PATTERN.fullmatch(candidate.python_version):
            validation_errors.append(
                f"{prefix}: INVALID_PYTHON_VERSION_FORMAT"
            )
            continue

        if candidate.source_quote not in evidence.observation:
            validation_errors.append(f"{prefix}: SOURCE_QUOTE_NOT_FOUND")
            continue

        if candidate.python_version not in candidate.source_quote:
            validation_errors.append(f"{prefix}: VERSION_NOT_IN_SOURCE_QUOTE")
            continue

        if not _has_unique_quote(
            evidence.observation,
            candidate.source_quote,
        ):
            validation_errors.append(f"{prefix}: AMBIGUOUS_SOURCE_QUOTE")
            continue

        identity = (
            candidate.change,
            candidate.python_version,
            candidate.source_quote,
        )
        if identity in seen:
            validation_errors.append(f"{prefix}: DUPLICATE_CANDIDATE")
            continue

        seen.add(identity)
        grounded.append(
            GroundedPythonSupportClaim(
                change=candidate.change,
                python_version=candidate.python_version,
                evidence_id=evidence.evidence_id,
                source_quote=candidate.source_quote,
                extractor_id=normalized_extractor_id,
                authority="model_derived",
            )
        )

    return ExtractionResult(
        grounded_claims=tuple(grounded),
        unresolved=candidates.unresolved,
        validation_errors=tuple(validation_errors),
    )
