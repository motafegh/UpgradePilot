"""Test bounded composition of proposed-tag and exact changelog-file evidence."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone

from upgradepilot.github.repository import RepositoryTextFile, UnavailableRepositoryFile
from upgradepilot.github.tag import GitHubTagCommitEvidence
from upgradepilot.upstream.interval import (
    DependencyReleaseInterval,
    TaggedChangelogEvidence,
    UpstreamAuthoritySourceProblem,
)
from upgradepilot.upstream.interval_evidence import build_tagged_changelog_evidence

_REPOSITORY = "example/project"
_TAG_OBJECT_SHA = "a" * 40
_COMMIT_SHA = "b" * 40
_PATH = "docs/changelog.md"
_NOW = datetime(2026, 8, 2, 12, 0, tzinfo=timezone.utc)


def _interval() -> DependencyReleaseInterval:
    return DependencyReleaseInterval(
        package="friendly-bard",
        normalized_package="friendly-bard",
        old_version="2.6",
        proposed_version="2.8.4",
    )


def _tag(
    *,
    requested_tag: str = "v2.8.4",
    repository: str = _REPOSITORY,
    tag_object_type: str = "tag",
    tag_object_sha: str = _TAG_OBJECT_SHA,
    resolved_commit_sha: str = _COMMIT_SHA,
) -> GitHubTagCommitEvidence:
    return GitHubTagCommitEvidence(
        repository=repository,
        requested_tag=requested_tag,
        tag_ref=f"refs/tags/{requested_tag}",
        tag_object_type=tag_object_type,  # type: ignore[arg-type]
        tag_object_sha=tag_object_sha,
        resolved_commit_sha=resolved_commit_sha,
        peeled_tag_object_shas=(tag_object_sha,) if tag_object_type == "tag" else (),
        retrieved_at=_NOW,
    )


def _file(
    *,
    repository: str = _REPOSITORY,
    revision: str = _COMMIT_SHA,
    content: str = "## 2.8\nDrop support for Python 3.8.\n",
) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=repository,
        path=_PATH,
        revision=revision,
        content=content,
    )


class TaggedChangelogAcquisitionTests(unittest.TestCase):
    """Protect minimal durable source packaging after normal tag/file orchestration."""

    def test_matching_tag_scoped_file_builds_minimal_exact_changelog(self) -> None:
        result = build_tagged_changelog_evidence(_interval(), _tag(), _file())

        self.assertIsInstance(result, TaggedChangelogEvidence)
        assert isinstance(result, TaggedChangelogEvidence)
        self.assertEqual(result.repository, _REPOSITORY)
        self.assertEqual(result.interval, _interval())
        self.assertEqual(result.resolved_commit_sha, _COMMIT_SHA)
        self.assertEqual(result.path, _PATH)
        self.assertIn("Python 3.8", result.content)

    def test_lightweight_tag_still_contributes_resolved_commit_identity(self) -> None:
        tag = _tag(
            requested_tag="2.8.4",
            tag_object_type="commit",
            tag_object_sha=_COMMIT_SHA,
            resolved_commit_sha=_COMMIT_SHA,
        )

        result = build_tagged_changelog_evidence(_interval(), tag, _file())

        self.assertIsInstance(result, TaggedChangelogEvidence)
        assert isinstance(result, TaggedChangelogEvidence)
        self.assertEqual(result.resolved_commit_sha, _COMMIT_SHA)

    def test_unavailable_exact_file_remains_source_unavailable(self) -> None:
        unavailable = UnavailableRepositoryFile(
            repository=_REPOSITORY,
            path=_PATH,
            revision=_COMMIT_SHA,
            reason="not_found_or_inaccessible",
            detail="No accessible repository-file resource was found.",
        )

        result = build_tagged_changelog_evidence(_interval(), _tag(), unavailable)

        assert isinstance(result, UpstreamAuthoritySourceProblem)
        self.assertEqual(result.state, "source_unavailable")
        self.assertEqual(result.path, _PATH)

    def test_empty_exact_file_is_not_promoted_to_changelog_authority(self) -> None:
        result = build_tagged_changelog_evidence(
            _interval(),
            _tag(),
            _file(content="   \n"),
        )

        assert isinstance(result, UpstreamAuthoritySourceProblem)
        self.assertEqual(result.state, "source_unavailable")

    def test_wrong_public_input_types_are_rejected(self) -> None:
        with self.assertRaises(TypeError):
            build_tagged_changelog_evidence("not-an-interval", _tag(), _file())  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            build_tagged_changelog_evidence(_interval(), "not-a-tag", _file())  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            build_tagged_changelog_evidence(_interval(), _tag(), "not-a-file")  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
