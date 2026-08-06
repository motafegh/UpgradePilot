"""Compose bounded upstream support-drop runtime evaluation.

This module owns the Step 7D upstream-domain bridge only:

AuthoritativeUpstreamIntervalEvidence
→ deterministic crossed-release source window
→ bounded semantic candidate extraction
→ deterministic support-drop candidate validation
→ UpstreamSupportDropClaimResult

It does not acquire upstream evidence, inspect target repository files, evaluate target
Python relevance, make compatibility/safety claims, or recommend maintainer actions.
"""

from __future__ import annotations

from typing import Protocol

from .changelog import (
    CrossedReleaseSourceWindow,
    CrossedReleaseSourceWindowProblem,
    build_crossed_release_source_window,
)
from .claim import (
    CandidateUpstreamClaimResult,
    UpstreamSupportDropClaimResult,
    validate_support_drop_candidates,
)
from .interval import AuthoritativeUpstreamIntervalEvidence
from .support_drop_extractor import (
    MAX_SOURCE_WINDOW_CHARACTERS,
    LocalSupportDropExtractor,
)


class SupportDropCandidateExtractor(Protocol):
    """Minimal Step 7D dependency boundary for candidate extraction."""

    def extract(
        self,
        window: CrossedReleaseSourceWindow,
    ) -> CandidateUpstreamClaimResult: ...


def evaluate_support_drop_runtime(
    authority: AuthoritativeUpstreamIntervalEvidence,
    *,
    extractor: SupportDropCandidateExtractor | None = None,
    max_characters: int = MAX_SOURCE_WINDOW_CHARACTERS,
) -> UpstreamSupportDropClaimResult:
    """Build, extract, and deterministically admit one bounded support-drop result."""

    if not isinstance(authority, AuthoritativeUpstreamIntervalEvidence):
        raise TypeError("authority must be AuthoritativeUpstreamIntervalEvidence.")
    if type(max_characters) is not int or max_characters <= 0:
        raise ValueError("max_characters must be a positive integer.")

    crossed_releases = authority.crossed_releases
    if crossed_releases is None:
        return validate_support_drop_candidates(
            authority,
            _unresolved_candidate(
                authority,
                (
                    "Step 7D could not build a bounded source window because the "
                    "authority bundle contained no trusted crossed-release index."
                ),
            ),
        )

    changelog = authority.tagged_changelog
    if changelog is None:
        return validate_support_drop_candidates(
            authority,
            _unresolved_candidate(
                authority,
                (
                    "Step 7D could not build a bounded source window because the "
                    "authority bundle contained no exact tagged changelog."
                ),
            ),
        )

    window_result = build_crossed_release_source_window(
        crossed_releases,
        changelog,
        max_characters=max_characters,
    )
    if isinstance(window_result, CrossedReleaseSourceWindowProblem):
        return validate_support_drop_candidates(
            authority,
            _unresolved_candidate(
                authority,
                (
                    "Step 7D source-window construction stopped as "
                    f"{window_result.state}: {window_result.detail}"
                ),
            ),
        )
    if not isinstance(window_result, CrossedReleaseSourceWindow):
        raise TypeError(
            "build_crossed_release_source_window returned an unsupported result type."
        )

    selected_extractor = extractor or LocalSupportDropExtractor()
    candidate_result = selected_extractor.extract(window_result)
    if not isinstance(candidate_result, CandidateUpstreamClaimResult):
        raise TypeError("extractor must return CandidateUpstreamClaimResult.")

    return validate_support_drop_candidates(authority, candidate_result)


def _unresolved_candidate(
    authority: AuthoritativeUpstreamIntervalEvidence,
    detail: str,
) -> CandidateUpstreamClaimResult:
    interval = authority.interval
    return CandidateUpstreamClaimResult(
        state="unresolved",
        package=interval.package,
        normalized_package=interval.normalized_package,
        old_version=interval.old_version,
        proposed_version=interval.proposed_version,
        candidates=(),
        detail=detail,
    )


__all__ = (
    "SupportDropCandidateExtractor",
    "evaluate_support_drop_runtime",
)
