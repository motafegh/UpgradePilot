"""Test deterministic grounding of untrusted upstream support-drop candidates."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone

from upgradepilot.github.release import GitHubReleaseEvidence
from upgradepilot.upstream.claim import (
    CandidateUpstreamClaim,
    CandidateUpstreamClaimResult,
    GroundedPythonSupportDropClaim,
    UpstreamSupportDropClaimProblem,
    validate_support_drop_candidates,
)
from upgradepilot.upstream.interval import (
    AuthoritativeUpstreamIntervalEvidence,
    CrossedReleaseIndexEvidence,
    DependencyReleaseInterval,
    IntervalGitHubReleaseSource,
    TaggedChangelogEvidence,
    assemble_upstream_interval_authority,
)

_NOW = datetime(2026, 7, 31, 18, 0, tzinfo=timezone.utc)
_REPOSITORY = "example/project"
_TAGGED_COMMIT = "c" * 40


def _interval() -> DependencyReleaseInterval:
    return DependencyReleaseInterval(
        package="friendly-bard",
        normalized_package="friendly-bard",
        old_version="2.6",
        proposed_version="2.8.4",
    )


def _index() -> CrossedReleaseIndexEvidence:
    return CrossedReleaseIndexEvidence(
        repository=_REPOSITORY,
        interval=_interval(),
        ordered_versions=("2.7", "2.8", "2.8.4"),
        source_url="https://example.invalid/releases",
        retrieved_at=_NOW,
    )


def _release(version: str, body: str) -> IntervalGitHubReleaseSource:
    return IntervalGitHubReleaseSource(
        release_version=version,
        release=GitHubReleaseEvidence(
            repository=_REPOSITORY,
            requested_tag=version,
            release_id={"2.7": 27, "2.8": 28, "2.8.4": 284}[version],
            release_url=f"https://github.com/{_REPOSITORY}/releases/tag/{version}",
            release_name=version,
            body=body,
            prerelease=False,
            published_at="2026-07-01T00:00:00Z",
            tag_ref=f"refs/tags/{version}",
            tag_object_type="commit",
            tag_object_sha=f"commit-{version}",
            retrieved_at=_NOW,
        ),
    )


def _changelog(content: str) -> TaggedChangelogEvidence:
    return TaggedChangelogEvidence(
        repository=_REPOSITORY,
        interval=_interval(),
        resolved_commit_sha=_TAGGED_COMMIT,
        path="docs/changelog.md",
        content=content,
    )


def _authority(
    *,
    release_bodies: tuple[IntervalGitHubReleaseSource, ...] = (),
    changelog: TaggedChangelogEvidence | None = None,
    with_index: bool = True,
) -> AuthoritativeUpstreamIntervalEvidence:
    result = assemble_upstream_interval_authority(
        _interval(),
        _REPOSITORY,
        crossed_releases=_index() if with_index else None,
        release_bodies=release_bodies,
        tagged_changelogs=() if changelog is None else (changelog,),
    )
    assert isinstance(result, AuthoritativeUpstreamIntervalEvidence)
    return result


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


def _candidate(
    *,
    quote: str,
    source_kind: str = "tagged_changelog",
    introduced_in_version: str = "2.8",
    source_release_version: str | None = None,
    category: str = "support_boundary_change",
    change_state: str = "support_dropped",
    python_line: str = "3.8",
    source_text: str,
) -> CandidateUpstreamClaim:
    start = source_text.index(quote)
    return CandidateUpstreamClaim(
        category=category,
        change_state=change_state,
        python_line=python_line,
        introduced_in_version=introduced_in_version,
        source_kind=source_kind,
        source_release_version=source_release_version,
        source_quote=quote,
        quote_start=start,
        quote_end=start + len(quote),
    )


class UpstreamClaimTests(unittest.TestCase):
    def test_valid_tagged_changelog_candidate_becomes_grounded_claim(self) -> None:
        text = "## 2.8\nDrop support for Python 3.8.\n"
        authority = _authority(changelog=_changelog(text))
        candidate = _candidate(quote="Drop support for Python 3.8.", source_text=text)
        grounded = validate_support_drop_candidates(authority, _result(candidate))
        self.assertIsInstance(grounded, GroundedPythonSupportDropClaim)
        assert isinstance(grounded, GroundedPythonSupportDropClaim)
        self.assertEqual(grounded.python_line, "3.8")
        self.assertEqual(grounded.introduced_in_version, "2.8")
        self.assertEqual(len(grounded.source_evidence), 1)
        self.assertEqual(grounded.source_evidence[0].source_kind, "tagged_changelog")

    def test_valid_release_body_candidate_becomes_grounded_claim(self) -> None:
        body = "Maintenance changes. Drop support for Python 3.8."
        releases = (_release("2.7", "Earlier changes."), _release("2.8", body), _release("2.8.4", "Final fixes."))
        authority = _authority(release_bodies=releases)
        candidate = _candidate(quote="Drop support for Python 3.8.", source_kind="github_release_body", source_release_version="2.8", source_text=body)
        grounded = validate_support_drop_candidates(authority, _result(candidate))
        self.assertIsInstance(grounded, GroundedPythonSupportDropClaim)
        assert isinstance(grounded, GroundedPythonSupportDropClaim)
        self.assertEqual(grounded.source_evidence[0].source_kind, "github_release_body")

    def test_no_relevant_claim_is_explicit(self) -> None:
        authority = _authority(changelog=_changelog("## 2.8\nNo support change.\n"))
        result = CandidateUpstreamClaimResult(state="no_relevant_claim", package="friendly-bard", normalized_package="friendly-bard", old_version="2.6", proposed_version="2.8.4", candidates=(), detail=None)
        problem = validate_support_drop_candidates(authority, result)
        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "no_support_drop_claim")

    def test_unresolved_candidate_result_is_explicit(self) -> None:
        authority = _authority(changelog=_changelog("## 2.8\nText.\n"))
        result = CandidateUpstreamClaimResult(state="unresolved", package="friendly-bard", normalized_package="friendly-bard", old_version="2.6", proposed_version="2.8.4", candidates=(), detail="The extraction adapter could not produce a bounded result.")
        problem = validate_support_drop_candidates(authority, result)
        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "candidate_unresolved")

    def test_echoed_dependency_identity_must_match_authority(self) -> None:
        text = "Drop support for Python 3.8."
        authority = _authority(changelog=_changelog(text))
        result = CandidateUpstreamClaimResult(state="candidates_available", package="other-package", normalized_package="other-package", old_version="2.6", proposed_version="2.8.4", candidates=(_candidate(quote=text, source_text=text),), detail=None)
        problem = validate_support_drop_candidates(authority, result)
        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "identity_mismatch")

    def test_wrong_category_is_rejected(self) -> None:
        text = "Drop support for Python 3.8."
        authority = _authority(changelog=_changelog(text))
        candidate = _candidate(quote=text, source_text=text, category="compatibility_assurance")
        problem = validate_support_drop_candidates(authority, _result(candidate))
        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "unsupported_claim_category")

    def test_wrong_direction_is_rejected(self) -> None:
        text = "Add support for Python 3.8."
        authority = _authority(changelog=_changelog(text))
        candidate = _candidate(quote=text, source_text=text, change_state="support_added")
        problem = validate_support_drop_candidates(authority, _result(candidate))
        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "unsupported_change_state")

    def test_python_line_must_be_canonical_major_minor(self) -> None:
        text = "Drop support for Python 3.8.1."
        authority = _authority(changelog=_changelog(text))
        candidate = _candidate(quote=text, source_text=text, python_line="3.8.1")
        problem = validate_support_drop_candidates(authority, _result(candidate))
        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "invalid_python_line")

    def test_package_metadata_cannot_ground_prose_claim(self) -> None:
        text = "Drop support for Python 3.8."
        authority = _authority(changelog=_changelog(text))
        candidate = _candidate(quote=text, source_text=text, source_kind="package_metadata")
        problem = validate_support_drop_candidates(authority, _result(candidate))
        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "source_not_admitted")

    def test_release_candidate_must_resolve_exact_release_source(self) -> None:
        body = "Drop support for Python 3.8."
        authority = _authority(release_bodies=(_release("2.7", "Earlier."), _release("2.8", body), _release("2.8.4", "Final.")))
        candidate = _candidate(quote=body, source_kind="github_release_body", introduced_in_version="2.8", source_release_version="2.7", source_text=body)
        problem = validate_support_drop_candidates(authority, _result(candidate))
        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "source_identity_unresolved")

    def test_exact_quote_span_must_match_authoritative_text(self) -> None:
        text = "Drop support for Python 3.8."
        authority = _authority(changelog=_changelog(text))
        candidate = CandidateUpstreamClaim(category="support_boundary_change", change_state="support_dropped", python_line="3.8", introduced_in_version="2.8", source_kind="tagged_changelog", source_release_version=None, source_quote="Drop support for Python 3.9.", quote_start=0, quote_end=len(text))
        problem = validate_support_drop_candidates(authority, _result(candidate))
        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "source_quote_not_grounded")

    def test_trusted_crossed_release_index_is_required(self) -> None:
        text = "## 2.8\nDrop support for Python 3.8.\n"
        authority = _authority(changelog=_changelog(text), with_index=False)
        candidate = _candidate(quote="Drop support for Python 3.8.", source_text=text)
        problem = validate_support_drop_candidates(authority, _result(candidate))
        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "release_interval_unresolved")

    def test_introduced_version_must_belong_to_crossed_interval(self) -> None:
        text = "## 2.9\nDrop support for Python 3.8.\n"
        authority = _authority(changelog=_changelog(text))
        candidate = _candidate(quote="Drop support for Python 3.8.", introduced_in_version="2.9", source_text=text)
        problem = validate_support_drop_candidates(authority, _result(candidate))
        self.assertIsInstance(problem, UpstreamSupportDropClaimProblem)
        assert isinstance(problem, UpstreamSupportDropClaimProblem)
        self.assertEqual(problem.state, "claim_outside_interval")

    def test_equivalent_release_and_changelog_candidates_combine_sources(self) -> None:
        quote = "Drop support for Python 3.8."
        release_body = f"Release details. {quote}"
        changelog_text = f"## 2.8\n{quote}\n"
        authority = _authority(release_bodies=(_release("2.7", "Earlier."), _release("2.8", release_body), _release("2.8.4", "Final.")), changelog=_changelog(changelog_text))
        release_candidate = _candidate(quote=quote, source_kind="github_release_body", source_release_version="2.8", source_text=release_body)
        changelog_candidate = _candidate(quote=quote, source_text=changelog_text)
        grounded = validate_support_drop_candidates(authority, _result(changelog_candidate, release_candidate))
        self.assertIsInstance(grounded, GroundedPythonSupportDropClaim)
        assert isinstance(grounded, GroundedPythonSupportDropClaim)
        self.assertEqual(tuple(item.source_kind for item in grounded.source_evidence), ("github_release_body", "tagged_changelog"))

    def test_duplicate_candidate_is_deduplicated(self) -> None:
        text = "Drop support for Python 3.8."
        authority = _authority(changelog=_changelog(text))
        candidate = _candidate(quote=text, source_text=text)
        grounded = validate_support_drop_candidates(authority, _result(candidate, candidate))
        self.assertIsInstance(grounded, GroundedPythonSupportDropClaim)
        assert isinstance(grounded, GroundedPythonSupportDropClaim)
        self.assertEqual(len(grounded.source_evidence), 1)


if __name__ == "__main__":
    unittest.main()
