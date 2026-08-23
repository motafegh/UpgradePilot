"""Validate the frozen Step 6 semantic oracle against the existing Step 2 trust boundary.

This test does not call a model. Its job is to prove that the corpus we will later score
models against is internally coherent and that its expected semantic outcomes map to the
already behavior-validated candidate/grounding contracts.
"""

from __future__ import annotations

import json
import unittest
from datetime import datetime, timezone
from pathlib import Path

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
    TaggedChangelogEvidence,
)

_CORPUS_PATH = (
    Path(__file__).resolve().parents[2]
    / "experiments"
    / "step6_support_drop_semantic_corpus.json"
)
_RETRIEVED_AT = datetime(2026, 8, 3, tzinfo=timezone.utc)
_TAG_COMMIT_SHA = "a" * 40
_CHANGELOG_PATH = "docs/changelog.md"


def _load_corpus() -> dict[str, object]:
    return json.loads(_CORPUS_PATH.read_text(encoding="utf-8"))


def _authority(context: dict[str, object], text: str) -> AuthoritativeUpstreamIntervalEvidence:
    interval = DependencyReleaseInterval(
        package=str(context["package"]),
        normalized_package=str(context["normalized_package"]),
        old_version=str(context["old_version"]),
        proposed_version=str(context["proposed_version"]),
    )
    repository = str(context["repository"])
    crossed_versions = tuple(str(item) for item in context["crossed_versions"])

    crossed = CrossedReleaseIndexEvidence(
        repository=repository,
        interval=interval,
        ordered_versions=crossed_versions,
        source_url="https://example.invalid/release-index",
        retrieved_at=_RETRIEVED_AT,
    )
    changelog = TaggedChangelogEvidence(
        repository=repository,
        interval=interval,
        resolved_commit_sha=_TAG_COMMIT_SHA,
        path=_CHANGELOG_PATH,
        content=text,
    )
    return AuthoritativeUpstreamIntervalEvidence(
        interval=interval,
        repository=repository,
        crossed_releases=crossed,
        release_bodies=(),
        tagged_changelog=changelog,
        package_metadata=(),
        source_problems=(),
        authority_basis="tagged_changelog",
    )


def _candidate_result(
    context: dict[str, object],
    case: dict[str, object],
) -> CandidateUpstreamClaimResult:
    text = str(case["text"])
    candidates: list[CandidateUpstreamClaim] = []

    for oracle in case["candidates"]:
        assert isinstance(oracle, dict)
        quote = str(oracle["source_quote"])
        if text.count(quote) != 1:
            raise AssertionError(
                f"case {case['id']!r} must contain oracle quote exactly once: {quote!r}"
            )
        start = text.index(quote)
        candidates.append(
            CandidateUpstreamClaim(
                category="support_boundary_change",
                change_state="support_dropped",
                python_line=str(oracle["python_line"]),
                introduced_in_version=str(oracle["introduced_in_version"]),
                source_kind=str(context["source_kind"]),
                source_release_version=None,
                source_quote=quote,
                quote_start=start,
                quote_end=start + len(quote),
            )
        )

    detail = case.get("detail")
    return CandidateUpstreamClaimResult(
        state=str(case["expected_candidate_state"]),  # type: ignore[arg-type]
        package=str(context["package"]),
        normalized_package=str(context["normalized_package"]),
        old_version=str(context["old_version"]),
        proposed_version=str(context["proposed_version"]),
        candidates=tuple(candidates),
        detail=None if detail is None else str(detail),
    )


class Step6SupportDropSemanticCorpusTests(unittest.TestCase):
    def test_corpus_has_unique_ids_and_required_critical_controls(self) -> None:
        corpus = _load_corpus()
        self.assertEqual(corpus["schema_version"], 1)
        cases = corpus["cases"]
        self.assertIsInstance(cases, list)
        assert isinstance(cases, list)

        ids = [str(case["id"]) for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(
            {
                "drop_direct",
                "support_added_control",
                "negated_drop_control",
                "future_drop_control",
                "raised_minimum_without_explicit_dropped_line",
                "multiple_distinct_dropped_lines",
                "instruction_shaped_documentation_near_valid_drop",
                "s001_exact_excerpt",
            }.issubset(set(ids))
        )

    def test_positive_oracle_quotes_explicitly_contain_the_python_line(self) -> None:
        corpus = _load_corpus()
        cases = corpus["cases"]
        assert isinstance(cases, list)

        for case in cases:
            assert isinstance(case, dict)
            for candidate in case["candidates"]:
                assert isinstance(candidate, dict)
                self.assertIn(
                    str(candidate["python_line"]),
                    str(candidate["source_quote"]),
                    case["id"],
                )

    def test_every_oracle_outcome_maps_through_step2_validator(self) -> None:
        corpus = _load_corpus()
        context = corpus["context"]
        cases = corpus["cases"]
        assert isinstance(context, dict)
        assert isinstance(cases, list)

        for case in cases:
            assert isinstance(case, dict)
            with self.subTest(case=case["id"]):
                authority = _authority(context, str(case["text"]))
                candidate_result = _candidate_result(context, case)
                result = validate_support_drop_candidates(authority, candidate_result)
                expected_state = str(case["expected_validator_state"])

                if expected_state == "grounded":
                    self.assertIsInstance(result, GroundedPythonSupportDropClaim)
                    assert isinstance(result, GroundedPythonSupportDropClaim)
                    self.assertEqual(len(case["candidates"]), 1)
                    oracle = case["candidates"][0]
                    self.assertEqual(result.python_line, oracle["python_line"])
                    self.assertEqual(
                        result.introduced_in_version,
                        oracle["introduced_in_version"],
                    )
                else:
                    self.assertIsInstance(result, UpstreamSupportDropClaimProblem)
                    assert isinstance(result, UpstreamSupportDropClaimProblem)
                    self.assertEqual(result.state, expected_state)


if __name__ == "__main__":
    unittest.main()
