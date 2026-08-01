"""Ground untrusted upstream support-drop candidates against exact authority.

This module is intentionally pure. It does not call a model, acquire network data,
parse PEP 440 versions, compare target Python declarations, or make compatibility,
safety, merge, and recommendation decisions.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Literal

from .dependency_change import normalize_package_name
from .upstream_interval import (
    AuthoritativeUpstreamIntervalEvidence,
    DependencyReleaseInterval,
    IntervalGitHubReleaseSource,
    TaggedChangelogEvidence,
)


type CandidateUpstreamClaimState = Literal[
    "candidates_available",
    "no_relevant_claim",
    "unresolved",
]
type GroundableUpstreamClaimSourceKind = Literal[
    "github_release_body",
    "tagged_changelog",
]
type UpstreamSupportDropClaimProblemState = Literal[
    "no_support_drop_claim",
    "candidate_unresolved",
    "identity_mismatch",
    "malformed_candidate",
    "unsupported_claim_category",
    "unsupported_change_state",
    "invalid_python_line",
    "source_not_admitted",
    "source_identity_unresolved",
    "source_quote_not_grounded",
    "release_interval_unresolved",
    "claim_outside_interval",
    "multiple_support_drop_claims",
]

_PYTHON_LINE = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\Z")
_CANDIDATE_STATES = {
    "candidates_available",
    "no_relevant_claim",
    "unresolved",
}


@dataclass(frozen=True, slots=True)
class CandidateUpstreamClaim:
    """One fully untrusted structured semantic candidate."""

    category: str
    change_state: str
    python_line: str
    introduced_in_version: str
    source_kind: str
    source_release_version: str | None
    source_quote: str
    quote_start: int
    quote_end: int


@dataclass(frozen=True, slots=True)
class CandidateUpstreamClaimResult:
    """Untrusted extraction output with echoed dependency context."""

    state: CandidateUpstreamClaimState
    package: str
    normalized_package: str
    old_version: str
    proposed_version: str
    candidates: tuple[CandidateUpstreamClaim, ...]
    detail: str | None


@dataclass(frozen=True, slots=True)
class GroundedUpstreamClaimSource:
    """One exact admitted source span that independently grounds the claim."""

    source_kind: GroundableUpstreamClaimSourceKind
    introduced_in_version: str
    source: IntervalGitHubReleaseSource | TaggedChangelogEvidence
    source_quote: str
    quote_start: int
    quote_end: int


@dataclass(frozen=True, slots=True)
class GroundedPythonSupportDropClaim:
    """Trusted support-drop evidence admitted for later target relevance work."""

    python_line: str
    introduced_in_version: str
    interval: DependencyReleaseInterval
    source_evidence: tuple[GroundedUpstreamClaimSource, ...]
    category: Literal["support_boundary_change"] = field(
        init=False,
        default="support_boundary_change",
    )
    change_state: Literal["support_dropped"] = field(
        init=False,
        default="support_dropped",
    )


@dataclass(frozen=True, slots=True)
class UpstreamSupportDropClaimProblem:
    """Normal stopping result when no single trusted support-drop claim exists."""

    state: UpstreamSupportDropClaimProblemState
    interval: DependencyReleaseInterval
    detail: str


type UpstreamSupportDropClaimResult = (
    GroundedPythonSupportDropClaim | UpstreamSupportDropClaimProblem
)


def validate_support_drop_candidates(
    authority: AuthoritativeUpstreamIntervalEvidence,
    candidate_result: CandidateUpstreamClaimResult,
) -> UpstreamSupportDropClaimResult:
    """Ground one candidate result against exact Step 1 interval authority."""

    if not isinstance(authority, AuthoritativeUpstreamIntervalEvidence):
        raise TypeError("authority must be AuthoritativeUpstreamIntervalEvidence.")
    if not isinstance(candidate_result, CandidateUpstreamClaimResult):
        raise TypeError("candidate_result must be CandidateUpstreamClaimResult.")

    interval = authority.interval
    identity_problem = _validate_echoed_identity(candidate_result, interval)
    if identity_problem is not None:
        return _problem("identity_mismatch", interval, identity_problem)

    state_problem = _validate_result_state(candidate_result)
    if state_problem is not None:
        return _problem("malformed_candidate", interval, state_problem)

    if candidate_result.state == "no_relevant_claim":
        return _problem(
            "no_support_drop_claim",
            interval,
            "The candidate result reported no relevant Python support-drop claim.",
        )
    if candidate_result.state == "unresolved":
        assert candidate_result.detail is not None
        return _problem("candidate_unresolved", interval, candidate_result.detail)

    crossed_releases = authority.crossed_releases
    if crossed_releases is None or crossed_releases.interval != interval:
        return _problem(
            "release_interval_unresolved",
            interval,
            (
                "Grounding an introduced release requires one trusted complete "
                "crossed-release index for the selected dependency interval."
            ),
        )

    grouped: dict[
        tuple[str, str],
        list[GroundedUpstreamClaimSource],
    ] = {}
    for candidate in candidate_result.candidates:
        grounded = _ground_candidate(authority, candidate)
        if isinstance(grounded, UpstreamSupportDropClaimProblem):
            return grounded
        key = (candidate.python_line, candidate.introduced_in_version)
        records = grouped.setdefault(key, [])
        if grounded not in records:
            records.append(grounded)

    if len(grouped) != 1:
        identities = ", ".join(
            f"Python {python_line} at {release_version}"
            for python_line, release_version in sorted(grouped)
        )
        return _problem(
            "multiple_support_drop_claims",
            interval,
            (
                "The candidate result established several distinct support-drop "
                f"claim identities: {identities}."
            ),
        )

    (python_line, introduced_in_version), records = next(iter(grouped.items()))
    return GroundedPythonSupportDropClaim(
        python_line=python_line,
        introduced_in_version=introduced_in_version,
        interval=interval,
        source_evidence=tuple(sorted(records, key=_source_sort_key)),
    )


def _validate_echoed_identity(
    result: CandidateUpstreamClaimResult,
    interval: DependencyReleaseInterval,
) -> str | None:
    if (
        not _trimmed(result.package)
        or not _trimmed(result.normalized_package)
        or normalize_package_name(result.package) != result.normalized_package
    ):
        return "The candidate result contained an invalid package identity."
    if (
        result.package != interval.package
        or result.normalized_package != interval.normalized_package
        or result.old_version != interval.old_version
        or result.proposed_version != interval.proposed_version
    ):
        return "The candidate result did not match the trusted dependency interval."
    return None


def _validate_result_state(result: CandidateUpstreamClaimResult) -> str | None:
    if result.state not in _CANDIDATE_STATES:
        return "The candidate result used an unsupported state."
    if not isinstance(result.candidates, tuple):
        return "Candidate claims must be represented as a tuple."
    if result.detail is not None and not _trimmed(result.detail):
        return "Candidate result detail must be non-empty trimmed text when present."

    if result.state == "candidates_available":
        if not result.candidates:
            return "The available state requires at least one candidate claim."
        return None
    if result.candidates:
        return "A non-available candidate result cannot contain candidate claims."
    if result.state == "unresolved" and result.detail is None:
        return "The unresolved candidate state requires a detail."
    return None


def _ground_candidate(
    authority: AuthoritativeUpstreamIntervalEvidence,
    candidate: CandidateUpstreamClaim,
) -> GroundedUpstreamClaimSource | UpstreamSupportDropClaimProblem:
    interval = authority.interval
    structure_problem = _validate_candidate_structure(candidate)
    if structure_problem is not None:
        return _problem("malformed_candidate", interval, structure_problem)

    if candidate.category != "support_boundary_change":
        return _problem(
            "unsupported_claim_category",
            interval,
            (
                "Only the support_boundary_change category is admitted for the "
                "first target-relevance slice."
            ),
        )
    if candidate.change_state != "support_dropped":
        return _problem(
            "unsupported_change_state",
            interval,
            "Only support_dropped claims are admitted for this slice.",
        )
    if _PYTHON_LINE.fullmatch(candidate.python_line) is None:
        return _problem(
            "invalid_python_line",
            interval,
            "The candidate Python line was not canonical major/minor text.",
        )

    crossed_releases = authority.crossed_releases
    assert crossed_releases is not None
    if candidate.introduced_in_version not in crossed_releases.ordered_versions:
        return _problem(
            "claim_outside_interval",
            interval,
            (
                f"Release {candidate.introduced_in_version!r} was not a member of "
                "the trusted crossed-release interval."
            ),
        )

    source_result = _resolve_source(authority, candidate)
    if isinstance(source_result, UpstreamSupportDropClaimProblem):
        return source_result
    source_kind, source, source_text = source_result

    if (
        candidate.quote_start < 0
        or candidate.quote_end <= candidate.quote_start
        or candidate.quote_end > len(source_text)
        or source_text[candidate.quote_start : candidate.quote_end]
        != candidate.source_quote
    ):
        return _problem(
            "source_quote_not_grounded",
            interval,
            "The candidate quote and span did not match the exact admitted source text.",
        )
    if not _quote_contains_python_line(
        candidate.source_quote,
        candidate.python_line,
    ):
        return _problem(
            "source_quote_not_grounded",
            interval,
            (
                "The grounded source quote did not contain the candidate Python line "
                "as an exact major/minor token."
            ),
        )

    return GroundedUpstreamClaimSource(
        source_kind=source_kind,
        introduced_in_version=candidate.introduced_in_version,
        source=source,
        source_quote=candidate.source_quote,
        quote_start=candidate.quote_start,
        quote_end=candidate.quote_end,
    )


def _validate_candidate_structure(candidate: object) -> str | None:
    if not isinstance(candidate, CandidateUpstreamClaim):
        return "A candidate claim had an unsupported type."
    if (
        not _trimmed(candidate.category)
        or not _trimmed(candidate.change_state)
        or not _trimmed(candidate.python_line)
        or not _trimmed(candidate.introduced_in_version)
        or not _trimmed(candidate.source_kind)
    ):
        return "Candidate identity and semantic fields must be non-empty trimmed text."
    if (
        candidate.source_release_version is not None
        and not _trimmed(candidate.source_release_version)
    ):
        return "Candidate source release identity must be trimmed text when present."
    if not isinstance(candidate.source_quote, str) or not candidate.source_quote:
        return "Candidate source quote must be non-empty exact text."
    if (
        type(candidate.quote_start) is not int
        or type(candidate.quote_end) is not int
    ):
        return "Candidate quote offsets must be integers."
    return None


def _resolve_source(
    authority: AuthoritativeUpstreamIntervalEvidence,
    candidate: CandidateUpstreamClaim,
) -> (
    tuple[
        GroundableUpstreamClaimSourceKind,
        IntervalGitHubReleaseSource | TaggedChangelogEvidence,
        str,
    ]
    | UpstreamSupportDropClaimProblem
):
    interval = authority.interval
    if candidate.source_kind == "github_release_body":
        if (
            candidate.source_release_version is None
            or candidate.source_release_version != candidate.introduced_in_version
        ):
            return _problem(
                "source_identity_unresolved",
                interval,
                (
                    "A GitHub Release candidate must identify the exact same release "
                    "as its introduced-in version."
                ),
            )
        matches = tuple(
            source
            for source in authority.release_bodies
            if source.release_version == candidate.source_release_version
        )
        if len(matches) != 1:
            return _problem(
                "source_identity_unresolved",
                interval,
                "The exact candidate GitHub Release body was not uniquely resolved.",
            )
        source = matches[0]
        body = source.release.body
        if body is None or not body:
            return _problem(
                "source_identity_unresolved",
                interval,
                "The resolved GitHub Release source had no admitted body text.",
            )
        return "github_release_body", source, body

    if candidate.source_kind == "tagged_changelog":
        if candidate.source_release_version is not None:
            return _problem(
                "source_identity_unresolved",
                interval,
                (
                    "A tagged-changelog candidate must use the one exact authority "
                    "record rather than inventing a release-body selector."
                ),
            )
        source = authority.tagged_changelog
        if source is None:
            return _problem(
                "source_identity_unresolved",
                interval,
                "The authority bundle contained no exact tagged changelog.",
            )
        return "tagged_changelog", source, source.content

    return _problem(
        "source_not_admitted",
        interval,
        (
            f"Source kind {candidate.source_kind!r} is not admitted to ground "
            "support-drop prose."
        ),
    )


def _quote_contains_python_line(quote: str, python_line: str) -> bool:
    token = re.compile(
        rf"(?<![0-9.]){re.escape(python_line)}(?![0-9]|\.[0-9])"
    )
    return token.search(quote) is not None


def _source_sort_key(source: GroundedUpstreamClaimSource) -> tuple[object, ...]:
    if source.source_kind == "github_release_body":
        assert isinstance(source.source, IntervalGitHubReleaseSource)
        identity = source.source.release_version
        rank = 0
    else:
        assert isinstance(source.source, TaggedChangelogEvidence)
        identity = source.source.path
        rank = 1
    return (
        rank,
        identity,
        source.quote_start,
        source.quote_end,
        source.source_quote,
    )


def _trimmed(value: object) -> bool:
    return isinstance(value, str) and bool(value) and value == value.strip()


def _problem(
    state: UpstreamSupportDropClaimProblemState,
    interval: DependencyReleaseInterval,
    detail: str,
) -> UpstreamSupportDropClaimProblem:
    return UpstreamSupportDropClaimProblem(
        state=state,
        interval=interval,
        detail=detail,
    )
