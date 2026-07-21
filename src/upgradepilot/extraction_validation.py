"""Deterministic validation for untrusted semantic-extraction output."""

from __future__ import annotations

import re

from upgradepilot.evidence import EvidenceItem
from upgradepilot.extraction import (
    CandidateExtractionResult,
    ExtractedPythonSupportChange,
    ExtractionResult,
)


_PYTHON_VERSION_PATTERN = re.compile(r"^[0-9]+\.[0-9]+$")


def validate_python_support_extraction(
    *,
    evidence: EvidenceItem,
    candidates: CandidateExtractionResult,
    extractor_id: str,
) -> ExtractionResult:
    """Validate candidate facts against one accepted release-note evidence item.

    This validator proves structure, evidence eligibility, literal quote grounding,
    version grounding, and duplicate consistency. It does not independently prove
    that the extractor interpreted every sentence correctly; that capability is
    evaluated through representative semantic test cases.
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

    accepted: list[ExtractedPythonSupportChange] = []
    validation_errors: list[str] = []
    seen: set[tuple[str, str, str]] = set()
    direction_by_version: dict[str, str] = {}

    for index, candidate in enumerate(candidates.facts):
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

        identity = (
            candidate.change,
            candidate.python_version,
            candidate.source_quote,
        )
        if identity in seen:
            validation_errors.append(f"{prefix}: DUPLICATE_CANDIDATE")
            continue

        previous_direction = direction_by_version.get(candidate.python_version)
        if previous_direction is not None and previous_direction != candidate.change:
            validation_errors.append(
                f"{prefix}: CONTRADICTORY_CHANGE_FOR_VERSION"
            )
            continue

        seen.add(identity)
        direction_by_version[candidate.python_version] = candidate.change
        accepted.append(
            ExtractedPythonSupportChange(
                change=candidate.change,
                python_version=candidate.python_version,
                evidence_id=evidence.evidence_id,
                source_quote=candidate.source_quote,
                extractor_id=normalized_extractor_id,
            )
        )

    return ExtractionResult(
        accepted_facts=tuple(accepted),
        unresolved=candidates.unresolved,
        validation_errors=tuple(validation_errors),
    )
