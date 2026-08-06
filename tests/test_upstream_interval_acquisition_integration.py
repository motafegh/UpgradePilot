"""Prove that Step 5 acquisition records compose through the existing Step 1 authority.

This module intentionally adds no new production authority layer. It exercises the
already-separated responsibilities as one deterministic chain:

```text
PyPI release-index evidence
→ Step 5A crossed-release selection

Git tag-to-commit evidence
+ exact commit changelog-file evidence
→ Step 5C tagged-changelog composition

crossed releases + tagged changelog
→ Step 1 assemble_upstream_interval_authority(...)
→ AuthoritativeUpstreamIntervalEvidence
```

The tests use controlled records and make no network requests. Live S001 acquisition is
a separate proof obligation after this deterministic integration boundary is green.
"""

from __future__ import annotations

import unittest
from datetime import datetime, timezone

from upgradepilot.github.repository import ExactRepositoryTextFile
from upgradepilot.github.tag import GitHubTagCommitEvidence
from upgradepilot.pypi.release import PackageReleaseIndexEvidence
from upgradepilot.upstream.interval import (
    AuthoritativeUpstreamIntervalEvidence,
    DependencyReleaseInterval,
    TaggedChangelogEvidence,
    UpstreamIntervalAuthorityProblem,
    assemble_upstream_interval_authority,
)
from upgradepilot.upstream.interval_evidence import (
    SelectedCrossedReleaseIndex,
    build_tagged_changelog_evidence,
    select_crossed_release_index,
)

_REPOSITORY = "facelessuser/soupsieve"
_RETRIEVED_AT = datetime(2026, 8, 2, 12, 0, tzinfo=timezone.utc)
_TAG_COMMIT_SHA = "a" * 40
_BLOB_SHA = "b" * 40
_CHANGELOG_PATH = "docs/src/markdown/about/changelog.md"


def _interval(*, proposed_version: str = "2.8.4") -> DependencyReleaseInterval:
    return DependencyReleaseInterval(
        package="soupsieve",
        normalized_package="soupsieve",
        old_version="2.6",
        proposed_version=proposed_version,
    )


def _selected_crossed_releases(
    interval: DependencyReleaseInterval,
) -> SelectedCrossedReleaseIndex:
    raw_index = PackageReleaseIndexEvidence(
        requested_package="soupsieve",
        normalized_package="soupsieve",
        published_name="soupsieve",
        source_url="https://pypi.org/pypi/soupsieve/json",
        retrieved_at=_RETRIEVED_AT,
        last_serial=12345,
        release_versions=(
            "2.6",
            "2.7",
            "2.8",
            "2.8.1",
            "2.8.2",
            "2.8.3",
            "2.8.4",
            "2.9",
        ),
    )
    result = select_crossed_release_index(interval, _REPOSITORY, raw_index)
    if not isinstance(result, SelectedCrossedReleaseIndex):
        raise AssertionError(f"controlled crossed-release fixture failed: {result!r}")
    return result


def _tagged_changelog(interval: DependencyReleaseInterval) -> TaggedChangelogEvidence:
    tag = GitHubTagCommitEvidence(
        repository=_REPOSITORY,
        requested_tag=interval.proposed_version,
        tag_ref=f"refs/tags/{interval.proposed_version}",
        tag_object_type="commit",
        tag_object_sha=_TAG_COMMIT_SHA,
        resolved_commit_sha=_TAG_COMMIT_SHA,
        peeled_tag_object_shas=(),
        retrieved_at=_RETRIEVED_AT,
    )
    content = "## 2.8\n\nDrop Python 3.8 support.\n\n## 2.8.4\n\nFix release.\n"
    file_evidence = ExactRepositoryTextFile(
        repository=_REPOSITORY,
        path=_CHANGELOG_PATH,
        returned_path=_CHANGELOG_PATH,
        revision=_TAG_COMMIT_SHA,
        blob_sha=_BLOB_SHA,
        reported_byte_count=len(content.encode("utf-8")),
        decoded_byte_count=len(content.encode("utf-8")),
        content=content,
        retrieved_at=_RETRIEVED_AT,
    )
    result = build_tagged_changelog_evidence(interval, tag, file_evidence)
    if not isinstance(result, TaggedChangelogEvidence):
        raise AssertionError(f"controlled tagged-changelog fixture failed: {result!r}")
    return result


class UpstreamIntervalAcquisitionIntegrationTests(unittest.TestCase):
    def test_s001_shaped_minimum_path_establishes_tagged_changelog_authority(self) -> None:
        interval = _interval()
        selected = _selected_crossed_releases(interval)
        changelog = _tagged_changelog(interval)

        result = assemble_upstream_interval_authority(
            interval,
            _REPOSITORY,
            crossed_releases=selected.evidence,
            tagged_changelogs=(changelog,),
        )

        self.assertIsInstance(result, AuthoritativeUpstreamIntervalEvidence)
        assert isinstance(result, AuthoritativeUpstreamIntervalEvidence)
        self.assertEqual(result.authority_basis, "tagged_changelog")
        self.assertIs(result.crossed_releases, selected.evidence)
        self.assertIs(result.tagged_changelog, changelog)
        self.assertEqual(
            result.crossed_releases.ordered_versions,
            ("2.7", "2.8", "2.8.1", "2.8.2", "2.8.3", "2.8.4"),
        )
        self.assertEqual(result.release_bodies, ())
        self.assertEqual(result.source_problems, ())

    def test_individually_valid_evidence_from_different_intervals_cannot_be_joined(self) -> None:
        selected_interval = _interval(proposed_version="2.8.3")
        changelog_interval = _interval(proposed_version="2.8.4")
        selected = _selected_crossed_releases(selected_interval)
        changelog = _tagged_changelog(changelog_interval)

        result = assemble_upstream_interval_authority(
            selected_interval,
            _REPOSITORY,
            crossed_releases=selected.evidence,
            tagged_changelogs=(changelog,),
        )

        self.assertIsInstance(result, UpstreamIntervalAuthorityProblem)
        assert isinstance(result, UpstreamIntervalAuthorityProblem)
        self.assertEqual(result.state, "identity_mismatch")


if __name__ == "__main__":
    unittest.main()
