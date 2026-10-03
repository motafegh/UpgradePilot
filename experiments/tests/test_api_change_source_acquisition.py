"""Deterministic trial proof: association boundaries and provider composition."""

from dataclasses import replace
from datetime import UTC, datetime
from unittest import TestCase
from unittest.mock import Mock, patch

from experiments.api_change_source_acquisition import (
    AcquisitionProblem,
    DeclaredReleaseWindow,
    DeclaredReleaseWindowAcquirer,
    DeclaredSourceAssociation,
    TrialPublicSession,
    associate_declared_source,
    select_release_sections,
)
from upgradepilot.github.changelog import DiscoveredChangelogPath
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.tag import GitHubTagCommitEvidence, GitHubTagCommitProblem
from upgradepilot.pypi.release import (
    PackageReleaseEvidence,
    PackageReleaseIndexEvidence,
    ProjectUrlCandidate,
)
from upgradepilot.upstream.interval import DependencyReleaseInterval
from upgradepilot.upstream.repository import UpstreamRepositoryProblem

NOW = datetime(2026, 10, 4, tzinfo=UTC)
SHA = "a" * 40


def release(version="2.0", links=None):
    return PackageReleaseEvidence(
        "demo",
        "demo",
        version,
        "demo",
        version,
        "https://pypi.org/pypi/demo/" + version + "/json",
        NOW,
        1,
        (),
        tuple(
            links
            if links is not None
            else [ProjectUrlCandidate("Source Code", "https://github.com/owner/demo")]
        ),
    )


def absent(state="source_unavailable"):
    return UpstreamRepositoryProblem(state, "demo", "2.0", "provider reason")


class AssociationTests(TestCase):
    def test_explicit_declaration_retains_ignored_links_and_absence(self):
        item = release(
            links=[
                ProjectUrlCandidate("Source Code", "https://github.com/owner/demo.git"),
                ProjectUrlCandidate("Homepage", "https://example.com"),
            ]
        )
        result = associate_declared_source(item, absent())
        self.assertIsInstance(result, DeclaredSourceAssociation)
        self.assertEqual(result.repository, "owner/demo")
        self.assertEqual(result.ignored_links, (item.project_urls[1],))
        self.assertEqual(result.provenance_result.state, "source_unavailable")

    def test_adverse_provenance_never_falls_back(self):
        for state in [
            "identity_mismatch",
            "ambiguous_source",
            "malformed_response",
            "acquisition_failed",
            "unsupported_source",
        ]:
            with self.subTest(state=state):
                result = associate_declared_source(release(), absent(state))
                self.assertEqual(result.reason, state)
                self.assertEqual(result.evidence.state, state)

    def test_homepage_and_unsafe_declarations_do_not_enable_examination(self):
        cases = [
            ("Homepage", "https://github.com/owner/demo"),
            ("Source", "http://github.com/owner/demo"),
            ("Source", "https://token@github.com/owner/demo"),
            ("Source", "https://github.com/owner/demo/tree/main"),
            ("Source", "https://127.0.0.1/owner/demo"),
            ("Source", "https://github.com/owner/demo?x=1"),
        ]
        for label, url in cases:
            with self.subTest(url=url):
                self.assertIsInstance(
                    associate_declared_source(
                        release(links=[ProjectUrlCandidate(label, url)]), absent()
                    ),
                    AcquisitionProblem,
                )

    def test_conflicting_declarations_retained(self):
        result = associate_declared_source(
            release(
                links=[
                    ProjectUrlCandidate("Source", "https://github.com/a/b"),
                    ProjectUrlCandidate("Repository", "https://github.com/c/d"),
                ]
            ),
            absent(),
        )
        self.assertEqual(result.reason, "conflicting_declarations")
        self.assertEqual(len(result.evidence[0]), 2)


class WindowTests(TestCase):
    def file(self, text):
        return RepositoryTextFile("owner/demo", "CHANGELOG.md", SHA, text)

    def test_whole_sections_keep_all_observations_and_ignore_fenced_headings(self):
        text = "# Changelog\n## 2.0\nremoved argument\n### Details\nother change\n```md\n## 2.0\n```\n## 1.5\ndeprecated something\n## 1.0\nold\n"
        sections = select_release_sections(self.file(text), ("1.5", "2.0"))
        self.assertEqual(tuple(s.version for s in sections), ("2.0", "1.5"))
        self.assertIn("other change", sections[0].text)
        self.assertNotIn("old", "".join(s.text for s in sections))
        for section in sections:
            self.assertEqual(
                text[section.start_offset : section.end_offset], section.text
            )

    def test_calendar_dates_are_structural_only_and_invalid_suffixes_fail(self):
        for suffix in ("2024-12-06", "6th December, 2024"):
            result = select_release_sections(
                self.file(f"## 2.0 ({suffix})\nall changes\n"), ("2.0",)
            )
            self.assertEqual(result[0].version, "2.0")
        for suffix in ("removed app", "2024-02-31", "next release"):
            self.assertIsInstance(
                select_release_sections(
                    self.file(f"## 2.0 ({suffix})\ntext\n"), ("2.0",)
                ),
                AcquisitionProblem,
            )

    def test_missing_duplicate_overlap_order_and_budget_fail_closed(self):
        cases = [
            ("## 2.0\nx\n", ("1.5", "2.0"), 20000),
            ("## 2.0\nx\n## 2.0\ny\n", ("2.0",), 20000),
            ("# 2.0\nx\n## 1.5\ny\n", ("1.5", "2.0"), 20000),
            ("## 1.5\nx\n## 2.0\ny\n## 1.7\nz\n", ("1.5", "1.7", "2.0"), 20000),
            ("## 2.0\nlong\n", ("2.0",), 3),
        ]
        for text, versions, budget in cases:
            with self.subTest(text=text):
                self.assertIsInstance(
                    select_release_sections(
                        self.file(text), versions, max_characters=budget
                    ),
                    AcquisitionProblem,
                )


class CompositionTests(TestCase):
    def runner(self):
        releases = Mock()
        releases.get_release.side_effect = lambda package, version: release(version)
        index = Mock()
        index.get_release_index.return_value = PackageReleaseIndexEvidence(
            "demo",
            "demo",
            "demo",
            "https://pypi.org/pypi/demo/json",
            NOW,
            1,
            ("1.0", "1.5", "2.0", "legacy"),
        )
        provenance = Mock()
        provenance.resolve.return_value = absent()
        tags = Mock()
        tags.resolve_tag_to_commit.side_effect = lambda repo, tag: (
            GitHubTagCommitEvidence(
                repo, tag, "refs/tags/" + tag, "commit", SHA, SHA, (), NOW
            )
        )
        paths = Mock()
        paths.discover.return_value = DiscoveredChangelogPath(
            "owner/demo", SHA, "b" * 40, "CHANGELOG.md", ("CHANGELOG.md",)
        )
        files = Mock()
        files.get_exact_commit_text_file.return_value = RepositoryTextFile(
            "owner/demo",
            "CHANGELOG.md",
            SHA,
            "## 2.0\nremoved foo\n## 1.5\nother change\n## 1.0\nold\n",
        )
        return DeclaredReleaseWindowAcquirer(
            releases=releases,
            index=index,
            provenance=provenance,
            tags=tags,
            paths=paths,
            files=files,
        )

    def test_normal_acquisition_composes_without_trusted_interval_or_known_path_input(
        self,
    ):
        runner = self.runner()
        result = runner.acquire(DependencyReleaseInterval("demo", "demo", "1.0", "2.0"))
        self.assertIsInstance(result, DeclaredReleaseWindow)
        self.assertEqual(result.ordered_versions, ("1.5", "2.0"))
        self.assertEqual(result.ignored_index_versions, ("legacy",))
        self.assertEqual(len(result.release_associations), 2)
        runner.paths.discover.assert_called_once_with("owner/demo", SHA)
        runner.files.get_exact_commit_text_file.assert_called_once_with(
            "owner/demo", SHA, "CHANGELOG.md"
        )
        self.assertEqual(len(result.window_sha256), 64)

    def test_tag_conflict_transport_and_budget_do_not_produce_window(self):
        for failure in ["conflict", "transport", "budget", "move"]:
            with self.subTest(failure=failure):
                runner = self.runner()
                if failure == "conflict":
                    original = runner.tags.resolve_tag_to_commit.side_effect
                    runner.tags.resolve_tag_to_commit.side_effect = (
                        lambda repo, tag, original=original: replace(
                            original(repo, tag),
                            resolved_commit_sha=(
                                "c" * 40 if tag.startswith("v") else SHA
                            ),
                        )
                    )
                if failure == "transport":
                    runner.tags.resolve_tag_to_commit.side_effect = lambda repo, tag: (
                        GitHubTagCommitProblem(
                            "acquisition_failed", repo, tag, "rate limit", 429
                        )
                    )
                if failure == "move":
                    runner.releases.get_release.side_effect = lambda package, version: (
                        release(
                            version,
                            [
                                ProjectUrlCandidate(
                                    "Source",
                                    "https://github.com/"
                                    + (
                                        "old/demo" if version == "1.5" else "owner/demo"
                                    ),
                                )
                            ],
                        )
                    )
                result = runner.acquire(
                    DependencyReleaseInterval("demo", "demo", "1.0", "2.0"),
                    max_releases=1 if failure == "budget" else 10,
                )
                self.assertIsInstance(result, AcquisitionProblem)
                runner.files.get_exact_commit_text_file.assert_not_called()


class TransportTests(TestCase):
    def test_scope_and_budget_reject_before_network(self):
        from requests.exceptions import RequestException

        session = TrialPublicSession()
        for url in (
            "https://127.0.0.1/x",
            "https://token@api.github.com/x",
            "http://api.github.com/x",
        ):
            with self.assertRaises(RequestException):
                session.get(url)
        session.github_requests = 50
        with self.assertRaises(RequestException):
            session.get("https://api.github.com/repos/a/b")

    def test_provider_requests_disable_redirects(self):
        session = TrialPublicSession()
        with patch("requests.Session.request") as request:
            session.get("https://api.github.com/repos/a/b")
            self.assertFalse(request.call_args.kwargs["allow_redirects"])
            self.assertEqual(session.github_requests, 1)
