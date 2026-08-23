"""Test Step 1 upstream interval identity and deterministic source authority."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone

from upgradepilot.dependency.change import (
    DependencyFileEvidence,
    DependencyVersionChange,
)
from upgradepilot.github.release import GitHubReleaseEvidence
from upgradepilot.upstream.interval import (
    UPSTREAM_SOURCE_AUTHORITY_ORDER,
    AuthoritativeUpstreamIntervalEvidence,
    CrossedReleaseIndexEvidence,
    DependencyReleaseInterval,
    IntervalGitHubReleaseSource,
    PackageMetadataCorroboration,
    TaggedChangelogEvidence,
    UpstreamAuthoritySourceProblem,
    UpstreamIntervalAuthorityProblem,
    assemble_upstream_interval_authority,
    release_interval_from_dependency_change,
    upstream_source_role,
)

_NOW = datetime(2026, 7, 31, 18, 30, tzinfo=timezone.utc)
_REPOSITORY = "example/friendly-bard"
_TAGGED_COMMIT = "c" * 40


def _dependency(
    *,
    package: str = "friendly-bard",
    old: str = "2.6",
    proposed: str = "2.8.4",
) -> DependencyVersionChange:
    return DependencyVersionChange(
        package=package,
        normalized_package=package,
        old_version=old,
        proposed_version=proposed,
        source_evidence=(
            DependencyFileEvidence(
                path="uv.lock",
                file_format="uv_lock",
                extraction_method="exact_base_head_files",
            ),
        ),
    )


def _interval() -> DependencyReleaseInterval:
    return release_interval_from_dependency_change(_dependency())


def _index(
    versions: tuple[str, ...],
    *,
    repository: str = _REPOSITORY,
    interval: DependencyReleaseInterval | None = None,
) -> CrossedReleaseIndexEvidence:
    return CrossedReleaseIndexEvidence(
        repository=repository,
        interval=interval or _interval(),
        ordered_versions=versions,
        source_url="https://api.github.com/repos/example/friendly-bard/releases",
        retrieved_at=_NOW,
    )


def _github_release(
    version: str,
    *,
    repository: str = _REPOSITORY,
    body: str | None = "Exact release body",
    release_id: int = 42,
    tag_object_sha: str | None = None,
) -> GitHubReleaseEvidence:
    tag = version
    return GitHubReleaseEvidence(
        repository=repository,
        requested_tag=tag,
        release_id=release_id,
        release_url=f"https://github.com/{repository}/releases/tag/{tag}",
        release_name=version,
        body=body,
        prerelease=False,
        published_at="2026-07-30T12:00:00Z",
        tag_ref=f"refs/tags/{tag}",
        tag_object_type="commit",
        tag_object_sha=tag_object_sha or f"sha-{version}",
        retrieved_at=_NOW,
    )


def _release_source(
    version: str,
    **kwargs: object,
) -> IntervalGitHubReleaseSource:
    return IntervalGitHubReleaseSource(
        release_version=version,
        release=_github_release(version, **kwargs),
    )


def _changelog(
    *,
    repository: str = _REPOSITORY,
    interval: DependencyReleaseInterval | None = None,
    resolved_commit_sha: str = _TAGGED_COMMIT,
    path: str = "docs/changelog.md",
    content: str = "## 2.8\n- Drop Python 3.8 support.\n",
) -> TaggedChangelogEvidence:
    return TaggedChangelogEvidence(
        repository=repository,
        interval=interval or _interval(),
        resolved_commit_sha=resolved_commit_sha,
        path=path,
        content=content,
    )


def _metadata(version: str = "2.8.4") -> PackageMetadataCorroboration:
    return PackageMetadataCorroboration(
        package="friendly-bard",
        normalized_package="friendly-bard",
        release_version=version,
        source_url=f"https://pypi.org/pypi/friendly-bard/{version}/json",
        requires_python=">=3.9",
        retrieved_at=_NOW,
    )


class UpstreamIntervalAuthorityTests(unittest.TestCase):
    def test_dependency_change_becomes_old_exclusive_proposed_inclusive_interval(
        self,
    ) -> None:
        interval = release_interval_from_dependency_change(_dependency())

        self.assertEqual(interval.package, "friendly-bard")
        self.assertEqual(interval.normalized_package, "friendly-bard")
        self.assertEqual(interval.old_version, "2.6")
        self.assertEqual(interval.proposed_version, "2.8.4")
        self.assertFalse(interval.lower_bound_inclusive)
        self.assertTrue(interval.upper_bound_inclusive)

    def test_source_roles_and_authority_order_are_fixed(self) -> None:
        self.assertEqual(
            UPSTREAM_SOURCE_AUTHORITY_ORDER,
            (
                "github_release_body",
                "tagged_changelog",
                "package_metadata",
            ),
        )
        self.assertEqual(upstream_source_role("github_release_body"), "release_authority")
        self.assertEqual(upstream_source_role("tagged_changelog"), "interval_authority")
        self.assertEqual(upstream_source_role("package_metadata"), "corroboration")
        for unsupported in (
            "dependabot_release_note_copy",
            "arbitrary_documentation",
            "model_selected_text",
        ):
            with self.subTest(source_kind=unsupported):
                self.assertEqual(upstream_source_role(unsupported), "unsupported")

    def test_proposed_release_body_without_complete_interval_is_rejected(self) -> None:
        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            release_bodies=[_release_source("2.8.4")],
        )

        self.assertIsInstance(result, UpstreamIntervalAuthorityProblem)
        assert isinstance(result, UpstreamIntervalAuthorityProblem)
        self.assertEqual(result.state, "interval_incomplete")

    def test_single_release_complete_series_is_accepted(self) -> None:
        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            crossed_releases=_index(("2.8.4",)),
            release_bodies=[_release_source("2.8.4")],
        )

        self.assertIsInstance(result, AuthoritativeUpstreamIntervalEvidence)
        assert isinstance(result, AuthoritativeUpstreamIntervalEvidence)
        self.assertEqual(result.authority_basis, "complete_release_series")
        self.assertEqual(
            tuple(item.release_version for item in result.release_bodies),
            ("2.8.4",),
        )

    def test_complete_multi_release_series_is_ordered_by_trusted_index(self) -> None:
        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            crossed_releases=_index(("2.7", "2.8", "2.8.4")),
            release_bodies=[
                _release_source("2.8.4"),
                _release_source("2.7"),
                _release_source("2.8"),
            ],
        )

        self.assertIsInstance(result, AuthoritativeUpstreamIntervalEvidence)
        assert isinstance(result, AuthoritativeUpstreamIntervalEvidence)
        self.assertEqual(result.authority_basis, "complete_release_series")
        self.assertEqual(
            tuple(item.release_version for item in result.release_bodies),
            ("2.7", "2.8", "2.8.4"),
        )

    def test_missing_intermediate_release_body_cannot_hide_behind_proposed_body(
        self,
    ) -> None:
        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            crossed_releases=_index(("2.7", "2.8", "2.8.4")),
            release_bodies=[
                _release_source("2.7"),
                _release_source("2.8.4"),
            ],
        )

        self.assertIsInstance(result, UpstreamIntervalAuthorityProblem)
        assert isinstance(result, UpstreamIntervalAuthorityProblem)
        self.assertEqual(result.state, "interval_incomplete")
        self.assertIn("2.8", result.detail)

    def test_exact_tagged_changelog_independently_establishes_authority(self) -> None:
        changelog = _changelog()

        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            tagged_changelogs=[changelog],
        )

        self.assertIsInstance(result, AuthoritativeUpstreamIntervalEvidence)
        assert isinstance(result, AuthoritativeUpstreamIntervalEvidence)
        self.assertEqual(result.authority_basis, "tagged_changelog")
        self.assertEqual(result.tagged_changelog, changelog)
        assert result.tagged_changelog is not None
        self.assertEqual(result.tagged_changelog.resolved_commit_sha, _TAGGED_COMMIT)
        self.assertEqual(result.tagged_changelog.path, "docs/changelog.md")

    def test_changelog_covers_partial_series_and_preserves_source_problem(self) -> None:
        problem = UpstreamAuthoritySourceProblem(
            source_kind="github_release_body",
            state="source_unavailable",
            detail="Release body for 2.8 was unavailable.",
            release_version="2.8",
        )

        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            crossed_releases=_index(("2.7", "2.8", "2.8.4")),
            release_bodies=[
                _release_source("2.7"),
                _release_source("2.8.4"),
            ],
            tagged_changelogs=[_changelog()],
            source_problems=[problem],
        )

        self.assertIsInstance(result, AuthoritativeUpstreamIntervalEvidence)
        assert isinstance(result, AuthoritativeUpstreamIntervalEvidence)
        self.assertEqual(result.authority_basis, "tagged_changelog")
        self.assertEqual(result.source_problems, (problem,))
        self.assertEqual(
            tuple(item.release_version for item in result.release_bodies),
            ("2.7", "2.8.4"),
        )

    def test_package_metadata_alone_cannot_establish_interval_authority(self) -> None:
        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            package_metadata=[_metadata()],
        )

        self.assertIsInstance(result, UpstreamIntervalAuthorityProblem)
        assert isinstance(result, UpstreamIntervalAuthorityProblem)
        self.assertEqual(result.state, "no_interval_authority")

    def test_complete_series_and_changelog_are_both_preserved(self) -> None:
        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            crossed_releases=_index(("2.7", "2.8", "2.8.4")),
            release_bodies=[
                _release_source("2.7"),
                _release_source("2.8"),
                _release_source("2.8.4"),
            ],
            tagged_changelogs=[_changelog()],
            package_metadata=[_metadata()],
        )

        self.assertIsInstance(result, AuthoritativeUpstreamIntervalEvidence)
        assert isinstance(result, AuthoritativeUpstreamIntervalEvidence)
        self.assertEqual(
            result.authority_basis,
            "complete_release_series_and_tagged_changelog",
        )
        self.assertEqual(len(result.release_bodies), 3)
        self.assertIsNotNone(result.tagged_changelog)
        self.assertEqual(result.package_metadata, (_metadata(),))

    def test_conflicting_release_identity_for_same_version_stops(self) -> None:
        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            crossed_releases=_index(("2.8.4",)),
            release_bodies=[
                _release_source("2.8.4", release_id=42),
                _release_source("2.8.4", release_id=99),
            ],
        )

        self.assertIsInstance(result, UpstreamIntervalAuthorityProblem)
        assert isinstance(result, UpstreamIntervalAuthorityProblem)
        self.assertEqual(result.state, "conflicting_source_identity")

    def test_distinct_tagged_changelog_identities_are_ambiguous(self) -> None:
        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            tagged_changelogs=[
                _changelog(path="CHANGELOG.md"),
                _changelog(path="docs/changelog.md"),
            ],
        )

        self.assertIsInstance(result, UpstreamIntervalAuthorityProblem)
        assert isinstance(result, UpstreamIntervalAuthorityProblem)
        self.assertEqual(result.state, "ambiguous_source")

    def test_repository_or_interval_identity_mismatch_stops(self) -> None:
        other_interval = release_interval_from_dependency_change(
            _dependency(old="1.0", proposed="2.0")
        )
        cases = (
            {"crossed_releases": _index(("2.8.4",), repository="other/project")},
            {"tagged_changelogs": [_changelog(interval=other_interval)]},
            {"release_bodies": [_release_source("2.8.4", repository="other/project")]},
        )

        for kwargs in cases:
            with self.subTest(kwargs=kwargs):
                result = assemble_upstream_interval_authority(
                    _interval(),
                    _REPOSITORY,
                    **kwargs,
                )
                self.assertIsInstance(result, UpstreamIntervalAuthorityProblem)
                assert isinstance(result, UpstreamIntervalAuthorityProblem)
                self.assertEqual(result.state, "identity_mismatch")

    def test_tagged_changelog_intrinsic_source_invariants_are_constructor_owned(self) -> None:
        invalid_kwargs = (
            {"resolved_commit_sha": "not-a-git-object-id"},
            {"path": "docs/../changelog.md"},
            {"content": ""},
        )

        for kwargs in invalid_kwargs:
            with self.subTest(kwargs=kwargs):
                with self.assertRaises((TypeError, ValueError)):
                    _changelog(**kwargs)

    def test_crossed_release_index_structural_invariants_are_enforced(self) -> None:
        invalid_indexes = (
            _index(()),
            _index(("2.6", "2.8.4")),
            _index(("2.8.4", "2.8")),
            _index(("2.8", "2.8", "2.8.4")),
        )

        for index in invalid_indexes:
            with self.subTest(index=index):
                result = assemble_upstream_interval_authority(
                    _interval(),
                    _REPOSITORY,
                    crossed_releases=index,
                    tagged_changelogs=[_changelog()],
                )
                self.assertIsInstance(result, UpstreamIntervalAuthorityProblem)
                assert isinstance(result, UpstreamIntervalAuthorityProblem)
                self.assertEqual(result.state, "malformed_source")

    def test_package_metadata_is_bounded_to_old_or_crossed_versions(self) -> None:
        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            crossed_releases=_index(("2.7", "2.8.4")),
            tagged_changelogs=[_changelog()],
            package_metadata=[_metadata("9.0")],
        )

        self.assertIsInstance(result, UpstreamIntervalAuthorityProblem)
        assert isinstance(result, UpstreamIntervalAuthorityProblem)
        self.assertEqual(result.state, "identity_mismatch")

    def test_bodyless_release_is_preserved_as_problem_when_changelog_covers(self) -> None:
        result = assemble_upstream_interval_authority(
            _interval(),
            _REPOSITORY,
            crossed_releases=_index(("2.8", "2.8.4")),
            release_bodies=[
                _release_source("2.8", body=None),
                _release_source("2.8.4"),
            ],
            tagged_changelogs=[_changelog()],
        )

        self.assertIsInstance(result, AuthoritativeUpstreamIntervalEvidence)
        assert isinstance(result, AuthoritativeUpstreamIntervalEvidence)
        self.assertEqual(result.authority_basis, "tagged_changelog")
        self.assertEqual(len(result.release_bodies), 1)
        self.assertEqual(len(result.source_problems), 1)
        self.assertEqual(result.source_problems[0].state, "source_unavailable")
        self.assertEqual(result.source_problems[0].release_version, "2.8")


if __name__ == "__main__":
    unittest.main()