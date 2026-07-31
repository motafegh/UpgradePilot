"""Test aggregate and malformed edge behavior for support-drop grounding."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone

from upgradepilot.upstream_claim import (
    CandidateUpstreamClaim,
    CandidateUpstreamClaimResult,
    UpstreamSupportDropClaimProblem,
    validate_support_drop_candidates,
)
from upgradepilot.upstream_interval import (
    AuthoritativeUpstreamIntervalEvidence,
    CrossedReleaseIndexEvidence,
    DependencyReleaseInterval,
    TaggedChangelogEvidence,
    assemble_upstream_interval_authority,
)

_NOW = datetime(2026, 7, 31, 18, 0, tzinfo=timezone.utc)
_TEXT = (
    "## 2.7\nDrop support for Python 3.7.\n"
    "## 2.8\nDrop support for Python 3.8.\n"
)


def _interval() -> DependencyReleaseInterval:
    return DependencyReleaseInterval(
        package="friendly-bard",
        normalized_package="friendly-bard",
        old_version="2.6",
        proposed_version="2.8.4",
    )


def _authority() -> AuthoritativeUpstreamIntervalEvidence:
    interval = _interval()
    changelog = TaggedChangelogEvidence(
        repository="example/project",
        interval=interval,
        requested_tag="2.8.4",
        tag_ref="refs/tags/2.8.4",
        tag_object_type="commit",
        tag_object_sha="commit-2.8.4",
        resolved_commit_sha="commit-2.8.4",
        path="CHANGELOG.md",
        returned_path="CHANGELOG.md",
        blob_sha="blob-changelog",
        reported_byte_count=len(_TEXT.encode("utf-8")),
        decoded_byte_count=len(_TEXT.encode("utf-8")),
        content=_TEXT,
        retrieved_at=_NOW,
    )
    result = assemble_upstream_interval_authority(
        interval,
        "example/project",
        crossed_releases=CrossedReleaseIndexEvidence(
            repository="example/project",
            interval=interval,
            ordered_versions=("2.7", "2.8", "2.8.4"),
            source_url="https://example.invalid/releases",
            retrieved_at=_NOW,
        ),
        tagged_changelogs=(changelog,),
    )
    assert isinstance(result, AuthoritativeUpstreamIntervalEvidence)
    return result


def _candidate(
    python_line: str,
    introduced_in_version: str,
    *,
    quote: str | None = None,
    category: str = "support_boundary_change",
) -> CandidateUpstreamClaim:
    quote = quote or f"Drop support for Python {python_line}."
    start = _TEXT.index(quote) if quote in _TEXT else 0
    return CandidateUpstreamClaim(
        category=category,
        change_state="support_dropped",
        python_line=python_line,
        introduced_in_version=introduced_in_version,
        source_kind="tagged_changelog",
        source_release_version=None,
        source_quote=quote,
        quote_start=start,
        quote_end=start + len(quote),
    )


def _result(*candidates: CandidateUpstreamClaim) -> CandidateUpstreamClaimResult:
    return CandidateUpstreamClaimResult(
        state="candidates_available",
        package="friendly-bard",
        normalized_package="friendly-bard",
        old_version="2.6",
        proposed_version="2.8.4",
        candidates=candidates,
        detail=None,
    )


class UpstreamClaimEdgeTests(unittest.TestCase):
    def test_available_state_requires_candidates(self) -> None:
        problem = validate_support_drop_candidates(_authority(), _result())

        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "malformed_candidate")

    def test_no_relevant_state_rejects_attached_candidates(self) -> None:
        candidate = _candidate("3.8", "2.8")
        result = CandidateUpstreamClaimResult(
            state="no_relevant_claim",
            package="friendly-bard",
            normalized_package="friendly-bard",
            old_version="2.6",
            proposed_version="2.8.4",
            candidates=(candidate,),
            detail=None,
        )

        problem = validate_support_drop_candidates(_authority(), result)

        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "malformed_candidate")

    def test_unresolved_state_requires_nonempty_detail(self) -> None:
        result = CandidateUpstreamClaimResult(
            state="unresolved",
            package="friendly-bard",
            normalized_package="friendly-bard",
            old_version="2.6",
            proposed_version="2.8.4",
            candidates=(),
            detail=None,
        )

        problem = validate_support_drop_candidates(_authority(), result)

        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "malformed_candidate")

    def test_distinct_python_lines_are_not_silently_selected(self) -> None:
        problem = validate_support_drop_candidates(
            _authority(),
            _result(
                _candidate("3.7", "2.7"),
                _candidate("3.8", "2.8"),
            ),
        )

        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "multiple_support_drop_claims")

    def test_same_python_line_at_distinct_releases_is_not_silently_selected(self) -> None:
        first_quote = "Drop support for Python 3.7."
        second = CandidateUpstreamClaim(
            category="support_boundary_change",
            change_state="support_dropped",
            python_line="3.7",
            introduced_in_version="2.8",
            source_kind="tagged_changelog",
            source_release_version=None,
            source_quote=first_quote,
            quote_start=_TEXT.index(first_quote),
            quote_end=_TEXT.index(first_quote) + len(first_quote),
        )

        problem = validate_support_drop_candidates(
            _authority(),
            _result(_candidate("3.7", "2.7"), second),
        )

        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "multiple_support_drop_claims")

    def test_invalid_candidate_blocks_valid_candidate(self) -> None:
        valid = _candidate("3.8", "2.8")
        invalid = _candidate(
            "3.7",
            "2.7",
            category="security_fix",
        )

        problem = validate_support_drop_candidates(
            _authority(),
            _result(valid, invalid),
        )

        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "unsupported_claim_category")

    def test_python_line_must_be_present_as_exact_quote_token(self) -> None:
        quote = "Drop support for Python 3.8."
        start = _TEXT.index(quote)
        candidate = CandidateUpstreamClaim(
            category="support_boundary_change",
            change_state="support_dropped",
            python_line="3.9",
            introduced_in_version="2.8",
            source_kind="tagged_changelog",
            source_release_version=None,
            source_quote=quote,
            quote_start=start,
            quote_end=start + len(quote),
        )

        problem = validate_support_drop_candidates(_authority(), _result(candidate))

        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "source_quote_not_grounded")

    def test_boolean_quote_offsets_are_rejected_as_malformed(self) -> None:
        candidate = CandidateUpstreamClaim(
            category="support_boundary_change",
            change_state="support_dropped",
            python_line="3.8",
            introduced_in_version="2.8",
            source_kind="tagged_changelog",
            source_release_version=None,
            source_quote="Drop support for Python 3.8.",
            quote_start=False,
            quote_end=True,
        )

        problem = validate_support_drop_candidates(_authority(), _result(candidate))

        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "malformed_candidate")


if __name__ == "__main__":
    unittest.main()
