"""Protect Step 1 authority identity edges found during source review."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone

from upgradepilot.dependency.change import (
    DependencyFileEvidence,
    DependencyVersionChange,
)
from upgradepilot.github.release import GitHubReleaseEvidence
from upgradepilot.upstream.interval import (
    CrossedReleaseIndexEvidence,
    IntervalGitHubReleaseSource,
    TaggedChangelogEvidence,
    UpstreamAuthoritySourceProblem,
    UpstreamIntervalAuthorityProblem,
    assemble_upstream_interval_authority,
    release_interval_from_dependency_change,
)

_NOW = datetime(2026, 7, 31, 18, 45, tzinfo=timezone.utc)
_REPOSITORY = "example/friendly-bard"


def _interval():
    dependency = DependencyVersionChange(
        package="friendly-bard",
        normalized_package="friendly-bard",
        old_version="2.6",
        proposed_version="2.8.4",
        source_evidence=(
            DependencyFileEvidence(
                path="uv.lock",
                file_format="uv_lock",
                extraction_method="exact_base_head_files",
            ),
        ),
    )
    return release_interval_from_dependency_change(dependency)


def _index() -> CrossedReleaseIndexEvidence:
    return CrossedReleaseIndexEvidence(
        repository=_REPOSITORY,
        interval=_interval(),
        ordered_versions=("2.8", "2.8.4"),
        source_url="https://api.github.com/repos/example/friendly-bard/releases",
        retrieved_at=_NOW,
    )


def _release_source(
    release_version: str,
    *,
    requested_tag: str | None = None,
) -> IntervalGitHubReleaseSource:
    tag = requested_tag or release_version
    return IntervalGitHubReleaseSource(
        release_version=release_version,
        release=GitHubReleaseEvidence(
            repository=_REPOSITORY,
            requested_tag=tag,
            release_id=42,
            release_url=f"https://github.com/{_REPOSITORY}/releases/tag/{tag}",
            release_name=release_version,
            body="Exact release body",
            prerelease=False,
            published_at="2026-07-30T12:00:00Z",
            tag_ref=f"refs/tags/{tag}",
            tag_object_type="commit",
            tag_object_sha=f"sha-{release_version}",
            retrieved_at=_NOW,
        ),
    )


def _changelog() -> TaggedChangelogEvidence:
    return TaggedChangelogEvidence(
        repository=_REPOSITORY,
        interval=_interval(),
        resolved_commit_sha="resolved-commit-sha",
        path="docs/changelog.md",
        content="## 2.8\n- Drop Python 3.8 support.\n",
    )


class UpstreamIntervalAuthorityEdgeTests(unittest.TestCase):
    def test_release_tag_must_identify_declared_release_version(self) -> None:
        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            crossed_releases=_index(),
            release_bodies=[
                _release_source("2.8", requested_tag="9.0"),
                _release_source("2.8.4"),
            ],
        )

        self.assertIsInstance(result, UpstreamIntervalAuthorityProblem)
        assert isinstance(result, UpstreamIntervalAuthorityProblem)
        self.assertEqual(result.state, "identity_mismatch")

    def test_identity_mismatch_source_problem_cannot_be_hidden_by_changelog(self) -> None:
        source_problem = UpstreamAuthoritySourceProblem(
            source_kind="github_release_body",
            state="identity_mismatch",
            detail="The release belonged to another repository.",
            release_version="2.8",
        )

        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            crossed_releases=_index(),
            tagged_changelogs=[_changelog()],
            source_problems=[source_problem],
        )

        self.assertIsInstance(result, UpstreamIntervalAuthorityProblem)
        assert isinstance(result, UpstreamIntervalAuthorityProblem)
        self.assertEqual(result.state, "identity_mismatch")
        self.assertEqual(result.source_problems, (source_problem,))

    def test_malformed_source_problem_cannot_be_hidden_by_changelog(self) -> None:
        source_problem = UpstreamAuthoritySourceProblem(
            source_kind="tagged_changelog",
            state="malformed_source",
            detail="The tagged changelog source identity was malformed.",
            path="docs/changelog.md",
        )

        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            tagged_changelogs=[_changelog()],
            source_problems=[source_problem],
        )

        self.assertIsInstance(result, UpstreamIntervalAuthorityProblem)
        assert isinstance(result, UpstreamIntervalAuthorityProblem)
        self.assertEqual(result.state, "malformed_source")
        self.assertEqual(result.source_problems, (source_problem,))

    def test_source_problem_release_version_must_be_inside_bounded_interval(self) -> None:
        source_problem = UpstreamAuthoritySourceProblem(
            source_kind="github_release_body",
            state="source_unavailable",
            detail="A release body was unavailable.",
            release_version="9.0",
        )

        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            crossed_releases=_index(),
            tagged_changelogs=[_changelog()],
            source_problems=[source_problem],
        )

        self.assertIsInstance(result, UpstreamIntervalAuthorityProblem)
        assert isinstance(result, UpstreamIntervalAuthorityProblem)
        self.assertEqual(result.state, "identity_mismatch")


if __name__ == "__main__":
    unittest.main()
