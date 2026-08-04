"""Test Step 7D bounded upstream support-drop runtime composition."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone

from upgradepilot.upstream.changelog import CrossedReleaseSourceWindow
from upgradepilot.upstream.claim import (
    CandidateUpstreamClaim,
    CandidateUpstreamClaimResult,
    GroundedPythonSupportDropClaim,
    UpstreamSupportDropClaimProblem,
)
from upgradepilot.upstream.interval import (
    AuthoritativeUpstreamIntervalEvidence,
    CrossedReleaseIndexEvidence,
    DependencyReleaseInterval,
    TaggedChangelogEvidence,
)
from upgradepilot.upstream.support_drop import evaluate_support_drop_runtime

_NOW = datetime(2026, 8, 5, 22, 0, tzinfo=timezone.utc)
_REPOSITORY = "example/friendly-bard"
_CONTENT = (
    "## 2.8.4\n- Fix selector behavior.\n"
    "## 2.8\n- Drop support for Python 3.8.\n"
    "## 2.7\n- Add a selector.\n"
)


def _interval() -> DependencyReleaseInterval:
    return DependencyReleaseInterval(
        package="friendly-bard",
        normalized_package="friendly-bard",
        old_version="2.6",
        proposed_version="2.8.4",
    )


def _crossed(
    interval: DependencyReleaseInterval,
    *,
    versions: tuple[str, ...] = ("2.7", "2.8", "2.8.4"),
) -> CrossedReleaseIndexEvidence:
    return CrossedReleaseIndexEvidence(
        repository=_REPOSITORY,
        interval=interval,
        ordered_versions=versions,
        source_url="https://pypi.org/pypi/friendly-bard/json",
        retrieved_at=_NOW,
    )


def _changelog(
    interval: DependencyReleaseInterval,
    *,
    content: str = _CONTENT,
) -> TaggedChangelogEvidence:
    encoded = content.encode("utf-8")
    return TaggedChangelogEvidence(
        repository=_REPOSITORY,
        interval=interval,
        requested_tag="2.8.4",
        tag_ref="refs/tags/2.8.4",
        tag_object_type="commit",
        tag_object_sha="a" * 40,
        resolved_commit_sha="a" * 40,
        path="docs/changelog.md",
        returned_path="docs/changelog.md",
        blob_sha="b" * 40,
        reported_byte_count=len(encoded),
        decoded_byte_count=len(encoded),
        content=content,
        retrieved_at=_NOW,
    )


def _authority(
    *,
    crossed: bool = True,
    changelog: bool = True,
    content: str = _CONTENT,
    versions: tuple[str, ...] = ("2.7", "2.8", "2.8.4"),
) -> AuthoritativeUpstreamIntervalEvidence:
    interval = _interval()
    crossed_evidence = _crossed(interval, versions=versions) if crossed else None
    changelog_evidence = _changelog(interval, content=content) if changelog else None
    return AuthoritativeUpstreamIntervalEvidence(
        interval=interval,
        repository=_REPOSITORY,
        crossed_releases=crossed_evidence,
        release_bodies=(),
        tagged_changelog=changelog_evidence,
        package_metadata=(),
        source_problems=(),
        authority_basis="tagged_changelog",
    )


class _RecordingExtractor:
    def __init__(self, state: str = "positive") -> None:
        self.state = state
        self.calls: list[CrossedReleaseSourceWindow] = []

    def extract(
        self,
        window: CrossedReleaseSourceWindow,
    ) -> CandidateUpstreamClaimResult:
        self.calls.append(window)
        interval = window.interval

        if self.state == "no_claim":
            return CandidateUpstreamClaimResult(
                state="no_relevant_claim",
                package=interval.package,
                normalized_package=interval.normalized_package,
                old_version=interval.old_version,
                proposed_version=interval.proposed_version,
                candidates=(),
                detail=None,
            )
        if self.state == "unresolved":
            return CandidateUpstreamClaimResult(
                state="unresolved",
                package=interval.package,
                normalized_package=interval.normalized_package,
                old_version=interval.old_version,
                proposed_version=interval.proposed_version,
                candidates=(),
                detail="Semantic meaning remained ambiguous.",
            )

        section = next(item for item in window.sections if item.release_version == "2.8")
        line = next(item for item in section.source_lines if "Python 3.8" in item.text)
        candidate = CandidateUpstreamClaim(
            category="support_boundary_change",
            change_state="support_dropped",
            python_line="3.8",
            introduced_in_version="2.8",
            source_kind="tagged_changelog",
            source_release_version=None,
            source_quote=line.text,
            quote_start=line.start_offset,
            quote_end=line.end_offset,
        )
        return CandidateUpstreamClaimResult(
            state="candidates_available",
            package=interval.package,
            normalized_package=interval.normalized_package,
            old_version=interval.old_version,
            proposed_version=interval.proposed_version,
            candidates=(candidate,),
            detail=None,
        )


class UpstreamSupportDropRuntimeTests(unittest.TestCase):
    def test_positive_candidate_is_grounded_only_after_validator(self) -> None:
        extractor = _RecordingExtractor()

        result = evaluate_support_drop_runtime(
            _authority(),
            extractor=extractor,
        )

        self.assertIsInstance(result, GroundedPythonSupportDropClaim)
        assert isinstance(result, GroundedPythonSupportDropClaim)
        self.assertEqual(result.python_line, "3.8")
        self.assertEqual(result.introduced_in_version, "2.8")
        self.assertEqual(len(result.source_evidence), 1)
        self.assertEqual(len(extractor.calls), 1)
        self.assertEqual(
            extractor.calls[0].trusted_ordered_versions,
            ("2.7", "2.8", "2.8.4"),
        )

    def test_no_claim_remains_explicit_problem(self) -> None:
        result = evaluate_support_drop_runtime(
            _authority(),
            extractor=_RecordingExtractor("no_claim"),
        )

        self.assertIsInstance(result, UpstreamSupportDropClaimProblem)
        assert isinstance(result, UpstreamSupportDropClaimProblem)
        self.assertEqual(result.state, "no_support_drop_claim")

    def test_semantic_unresolved_remains_explicit_problem(self) -> None:
        result = evaluate_support_drop_runtime(
            _authority(),
            extractor=_RecordingExtractor("unresolved"),
        )

        self.assertIsInstance(result, UpstreamSupportDropClaimProblem)
        assert isinstance(result, UpstreamSupportDropClaimProblem)
        self.assertEqual(result.state, "candidate_unresolved")
        self.assertIn("ambiguous", result.detail)

    def test_missing_crossed_release_index_stops_before_extractor(self) -> None:
        extractor = _RecordingExtractor()

        result = evaluate_support_drop_runtime(
            _authority(crossed=False),
            extractor=extractor,
        )

        self.assertIsInstance(result, UpstreamSupportDropClaimProblem)
        assert isinstance(result, UpstreamSupportDropClaimProblem)
        self.assertEqual(result.state, "candidate_unresolved")
        self.assertIn("no trusted crossed-release index", result.detail)
        self.assertEqual(extractor.calls, [])

    def test_missing_tagged_changelog_stops_before_extractor(self) -> None:
        extractor = _RecordingExtractor()

        result = evaluate_support_drop_runtime(
            _authority(changelog=False),
            extractor=extractor,
        )

        self.assertIsInstance(result, UpstreamSupportDropClaimProblem)
        assert isinstance(result, UpstreamSupportDropClaimProblem)
        self.assertEqual(result.state, "candidate_unresolved")
        self.assertIn("no exact tagged changelog", result.detail)
        self.assertEqual(extractor.calls, [])

    def test_incomplete_markdown_window_stops_before_extractor(self) -> None:
        extractor = _RecordingExtractor()
        content = "## 2.8.4\nfix\n## 2.8\nPython 3.8 change\n"

        result = evaluate_support_drop_runtime(
            _authority(content=content),
            extractor=extractor,
        )

        self.assertIsInstance(result, UpstreamSupportDropClaimProblem)
        assert isinstance(result, UpstreamSupportDropClaimProblem)
        self.assertEqual(result.state, "candidate_unresolved")
        self.assertIn("missing_release_section", result.detail)
        self.assertEqual(extractor.calls, [])

    def test_window_size_overflow_stops_before_extractor(self) -> None:
        extractor = _RecordingExtractor()

        result = evaluate_support_drop_runtime(
            _authority(),
            extractor=extractor,
            max_characters=20,
        )

        self.assertIsInstance(result, UpstreamSupportDropClaimProblem)
        assert isinstance(result, UpstreamSupportDropClaimProblem)
        self.assertEqual(result.state, "candidate_unresolved")
        self.assertIn("window_too_large", result.detail)
        self.assertEqual(extractor.calls, [])

    def test_invalid_character_bound_is_rejected(self) -> None:
        for value in (0, -1, True):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    evaluate_support_drop_runtime(
                        _authority(),
                        extractor=_RecordingExtractor(),
                        max_characters=value,
                    )

    def test_extractor_must_return_candidate_result(self) -> None:
        class BadExtractor:
            def extract(self, window: CrossedReleaseSourceWindow) -> object:
                return object()

        with self.assertRaises(TypeError):
            evaluate_support_drop_runtime(
                _authority(),
                extractor=BadExtractor(),  # type: ignore[arg-type]
            )


if __name__ == "__main__":
    unittest.main()
