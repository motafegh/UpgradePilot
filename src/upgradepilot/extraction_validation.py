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
_INSTRUCTION_OVERRIDE_PATTERN = re.compile(
    r"\b(?:ignore|disregard|override|forget)\b.{0,120}"
    r"\b(?:instructions?|rules?|prompts?|directions?)\b",
    re.IGNORECASE,
)
_OUTPUT_DIRECTIVE_PATTERN = re.compile(
    r"(?:^|[.!?;:,]\s+|\b(?:please|then|and)\s+)"
    r"(?:report|return|output|emit|say|state|claim)\b.{0,160}"
    r"\bpython\s+[0-9]+\.[0-9]+\b",
    re.IGNORECASE,
)
_CLASSIFICATION_DIRECTIVE_PATTERN = re.compile(
    r"(?:^|[.!?;:,]\s+|\b(?:please|then|and)\s+)"
    r"(?:treat|classify|mark)\b.{0,120}"
    r"\bpython\s+[0-9]+\.[0-9]+\b",
    re.IGNORECASE,
)
_EXAMPLE_OUTPUT_PATTERN = re.compile(
    r"\b(?:example|sample|expected)\s+"
    r"(?:output|response|answer)\s*:",
    re.IGNORECASE,
)
_DEPRECATION_PATTERN = re.compile(
    r"\bdeprecat(?:e|ed|es|ing|ion)\b",
    re.IGNORECASE,
)
_FUTURE_CHANGE_PATTERN = re.compile(
    r"\b(?:may|might|could|will|planned|planning|expected)\b.{0,100}"
    r"\b(?:drop|dropped|remove|removed|end|ended|unsupported)\b",
    re.IGNORECASE,
)
_CONTINUED_SUPPORT_PATTERNS = (
    re.compile(
        r"\b(?:remains?|continues?|still)\b.{0,80}\bsupport(?:ed)?\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\bsupport(?:ed)?\b.{0,80}\b(?:remains?|continues?|still)\b",
        re.IGNORECASE,
    ),
)


def _source_line_for_unique_quote(source: str, quote: str) -> str | None:
    """Return the complete line containing a quote with one source occurrence."""

    quote_start = source.find(quote)
    if quote_start < 0 or source.find(quote, quote_start + 1) >= 0:
        return None

    line_start = source.rfind("\n", 0, quote_start) + 1
    quote_end = quote_start + len(quote)
    line_end = source.find("\n", quote_end)
    if line_end < 0:
        line_end = len(source)
    return source[line_start:line_end].strip()


def _is_instruction_like_context(context: str) -> bool:
    return any(
        pattern.search(context) is not None
        for pattern in (
            _INSTRUCTION_OVERRIDE_PATTERN,
            _OUTPUT_DIRECTIVE_PATTERN,
            _CLASSIFICATION_DIRECTIVE_PATTERN,
            _EXAMPLE_OUTPUT_PATTERN,
        )
    )


def _is_non_effective_support_context(context: str) -> bool:
    if _DEPRECATION_PATTERN.search(context):
        return True
    if _FUTURE_CHANGE_PATTERN.search(context):
        return True
    return any(pattern.search(context) for pattern in _CONTINUED_SUPPORT_PATTERNS)


def validate_python_support_extraction(
    *,
    evidence: EvidenceItem,
    candidates: CandidateExtractionResult,
    extractor_id: str,
) -> ExtractionResult:
    """Validate candidate facts against one accepted release-note evidence item.

    This validator proves structure, evidence eligibility, unique literal quote
    grounding, version grounding, duplicate consistency, and bounded source-line
    context exclusions. It does not prove universal semantic or prompt-injection
    correctness; that capability remains bounded by representative proof cases.
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

        source_context = _source_line_for_unique_quote(
            evidence.observation,
            candidate.source_quote,
        )
        if source_context is None:
            validation_errors.append(f"{prefix}: AMBIGUOUS_SOURCE_QUOTE")
            continue

        if _is_instruction_like_context(source_context):
            validation_errors.append(
                f"{prefix}: INSTRUCTION_LIKE_SOURCE_CONTEXT"
            )
            continue

        if _is_non_effective_support_context(source_context):
            validation_errors.append(
                f"{prefix}: NON_EFFECTIVE_SUPPORT_CONTEXT"
            )
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
