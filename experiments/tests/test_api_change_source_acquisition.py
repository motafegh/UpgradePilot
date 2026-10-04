"""Deterministic trial proof: association boundaries and provider composition."""

import hashlib
import json
from contextlib import redirect_stdout
from dataclasses import replace
from datetime import UTC, datetime
from io import StringIO
from unittest import TestCase
from unittest.mock import Mock, patch

from experiments.api_change_source_acquisition import (
    AcquisitionProblem,
    DeclaredReleaseWindow,
    DeclaredReleaseWindowAcquirer,
    DeclaredSourceAssociation,
    IncompleteDeclaredReleaseWindow,
    PublisherProvenanceInspection,
    ReleaseWindowExamination,
    TrialPublicSession,
    associate_declared_source,
    select_release_sections,
)
from experiments.api_change_source_smoke import main as source_smoke_main
from experiments.api_release_window_manifest import release_window_manifest
from upgradepilot.github.changelog import DiscoveredChangelogPath
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.tag import GitHubTagCommitEvidence, GitHubTagCommitProblem
from upgradepilot.pypi.release import (
    PackageReleaseEvidence,
    PackageReleaseIndexEvidence,
    ProjectUrlCandidate,
)
from upgradepilot.upstream.interval import DependencyReleaseInterval

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
    return PublisherProvenanceInspection(state, "provider reason")


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

    def test_missing_versions_do_not_erase_later_available_evidence(self):
        text = "## 2.0\nremoved café\n"
        result = select_release_sections(self.file(text), ("1.5", "1.7", "2.0"))
        evidence = result.evidence
        self.assertIsInstance(evidence, ReleaseWindowExamination)
        self.assertEqual(evidence.required_versions, ("1.5", "1.7", "2.0"))
        self.assertEqual(evidence.missing_or_unsupported_versions, ("1.5", "1.7"))
        self.assertEqual(evidence.candidates[0].text, text)
        self.assertEqual(evidence.candidates[0].match_count, 1)
        self.assertEqual(
            evidence.full_source_sha256, hashlib.sha256(text.encode()).hexdigest()
        )
        self.assertEqual(
            (evidence.repository, evidence.revision, evidence.path),
            ("owner/demo", SHA, "CHANGELOG.md"),
        )

    def test_duplicate_candidates_are_all_retained_without_a_winner(self):
        text = "## 2.0\nfirst\n## 1.5\nunique\n## 2.0\nsecond\n"
        result = select_release_sections(self.file(text), ("1.5", "2.0"))
        self.assertIsInstance(result, AcquisitionProblem)
        self.assertEqual(result.evidence.ambiguous_versions, ("2.0",))
        candidates = result.evidence.candidates
        self.assertEqual([s.match_count for s in candidates], [2, 1, 2])
        self.assertEqual(
            [s.text for s in candidates],
            ["## 2.0\nfirst\n", "## 1.5\nunique\n", "## 2.0\nsecond\n"],
        )
        for candidate in candidates:
            recovered = text[candidate.start_offset : candidate.end_offset]
            self.assertEqual(candidate.text, recovered)
            self.assertEqual(
                candidate.sha256, hashlib.sha256(recovered.encode()).hexdigest()
            )

    def test_unsupported_heading_is_not_claimed_as_documentation_absence(self):
        result = select_release_sections(
            self.file("## 2.0 (2024-02-31)\nchange\n## 1.5\nknown\n"), ("1.5", "2.0")
        )
        self.assertEqual(result.evidence.missing_or_unsupported_versions, ("2.0",))
        self.assertEqual(result.evidence.candidates[0].version, "1.5")

    def test_inconsistent_ranges_and_order_keep_observations_not_admission(self):
        for text, versions in [
            ("# 2.0\nouter\n## 1.5\ninner\n", ("1.5", "2.0")),
            ("## 1.5\nx\n## 2.0\ny\n## 1.7\nz\n", ("1.5", "1.7", "2.0")),
        ]:
            with self.subTest(text=text):
                result = select_release_sections(self.file(text), versions)
                self.assertEqual(result.evidence.issues, ("section_order_or_overlap",))
                self.assertEqual(len(result.evidence.candidates), len(versions))
                self.assertTrue(
                    all(c.text is not None for c in result.evidence.candidates)
                )

    def test_budget_omits_text_but_recovers_exact_ranges_and_hashes(self):
        text = "## 2.0\nlong café\n## 1.5\nother\n"
        result = select_release_sections(
            self.file(text), ("1.5", "2.0"), max_characters=3
        )
        packet = json.loads(json.dumps(release_window_manifest(result)))
        examination = packet["section_examination"]
        self.assertFalse(packet["complete_window_eligible"])
        self.assertNotIn("window_sha256", packet)
        self.assertNotIn("coverage", packet)
        self.assertEqual(
            examination["text_omission_reason"],
            "candidate_text_exceeds_character_budget",
        )
        self.assertEqual(examination["max_characters"], 3)
        for candidate in examination["candidates"]:
            self.assertIsNone(candidate["text"])
            recovered = text[candidate["start_offset"] : candidate["end_offset"]]
            self.assertEqual(
                candidate["sha256"], hashlib.sha256(recovered.encode()).hexdigest()
            )

    def test_all_selection_issues_survive_a_single_incomplete_result(self):
        text = "# 2.0\nx\n## 2.0\ny\n"
        result = select_release_sections(
            self.file(text), ("1.5", "2.0"), max_characters=3
        )
        evidence = result.evidence
        self.assertEqual(evidence.missing_or_unsupported_versions, ("1.5",))
        self.assertEqual(evidence.ambiguous_versions, ("2.0",))
        self.assertEqual(
            evidence.issues,
            (
                "missing_or_duplicate_section",
                "section_order_or_overlap",
                "window_too_large",
            ),
        )
        self.assertEqual(len(evidence.candidates), 2)
        self.assertTrue(all(c.text is None for c in evidence.candidates))

    def test_exact_budget_boundary_keeps_whole_candidate_text(self):
        text = "## 2.0\nchange\n"
        result = select_release_sections(
            self.file(text), ("1.5", "2.0"), max_characters=len(text)
        )
        self.assertIsNone(result.evidence.text_omission_reason)
        self.assertEqual(result.evidence.candidates[0].text, text)


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

    def test_partial_acquisition_retains_source_chain_through_source_cli(self):
        runner = self.runner()
        file = replace(
            runner.files.get_exact_commit_text_file.return_value,
            content="## 2.0\nretained change\n",
        )
        runner.files.get_exact_commit_text_file.return_value = file
        result = runner.acquire(DependencyReleaseInterval("demo", "demo", "1.0", "2.0"))
        self.assertIsInstance(result, AcquisitionProblem)
        self.assertIsInstance(result.evidence, IncompleteDeclaredReleaseWindow)
        self.assertEqual(len(result.evidence.release_associations), 2)
        self.assertEqual(result.evidence.examination.required_versions, ("1.5", "2.0"))
        output = StringIO()
        # Exercise the actual writer and exit status, not only its shared helper.
        with (
            patch("sys.argv", ["source-smoke", "demo", "1.0", "2.0"]),
            patch(
                "experiments.api_change_source_smoke.DeclaredReleaseWindowAcquirer",
                return_value=runner,
            ),
            redirect_stdout(output),
        ):
            status = source_smoke_main()
        packet = json.loads(output.getvalue())
        self.assertEqual(status, 1)
        self.assertEqual(packet["state"], "incomplete")
        self.assertFalse(packet["complete_window_eligible"])
        self.assertEqual(
            packet["section_examination"]["candidates"][0]["text"], file.content
        )
        self.assertEqual(
            packet["source_context"]["release_metadata_urls"],
            [release("1.5").source_url, release("2.0").source_url],
        )
        self.assertEqual(
            packet["source_context"]["provenance_states"], ["source_unavailable"] * 2
        )
        self.assertEqual(
            packet["source_context"]["tags"][0]["resolved_commit_sha"], SHA
        )

    def test_complete_manifest_retains_original_window_hash_and_scoped_text(self):
        runner = self.runner()
        result = runner.acquire(DependencyReleaseInterval("demo", "demo", "1.0", "2.0"))
        packet = json.loads(json.dumps(release_window_manifest(result)))
        self.assertTrue(packet["complete_window_eligible"])
        self.assertEqual(packet["window_sha256"], result.window_sha256)
        self.assertEqual(
            [s["text"] for s in packet["sections"]], [s.text for s in result.sections]
        )
        self.assertEqual(packet["coverage"], result.coverage)
        output = StringIO()
        with (
            patch("sys.argv", ["source-smoke", "demo", "1.0", "2.0"]),
            patch(
                "experiments.api_change_source_smoke.DeclaredReleaseWindowAcquirer",
                return_value=runner,
            ),
            redirect_stdout(output),
        ):
            status = source_smoke_main()
        saved = json.loads(output.getvalue())
        self.assertEqual(status, 0)
        self.assertEqual(saved["commit"], result.file.revision)
        self.assertEqual(saved["crossed_versions"], list(result.ordered_versions))
        self.assertEqual(saved["full_source_sha256"], result.full_text_sha256)
        self.assertEqual(saved["window_sha256"], result.window_sha256)
        self.assertEqual(saved["sections"], packet["sections"])

    def test_file_transport_and_budget_failure_remain_typed_window_problems(self):
        from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError

        for error, reason in [
            (
                GitHubAcquisitionError("network failed", reason="transport_error"),
                "transport_error",
            ),
            (
                GitHubAcquisitionError("limit reached", reason="trial_request_limit"),
                "trial_request_limit",
            ),
            (GitHubResponseError("invalid response"), "malformed_response"),
        ]:
            with self.subTest(reason=reason):
                runner = self.runner()
                runner.files.get_exact_commit_text_file.side_effect = error
                result = runner.acquire(
                    DependencyReleaseInterval("demo", "demo", "1.0", "2.0")
                )
                self.assertIsInstance(result, AcquisitionProblem)
                self.assertEqual((result.stage, result.reason), ("file", reason))
                packet = release_window_manifest(result)
                self.assertFalse(packet["complete_window_eligible"])
                self.assertNotIn("section_examination", packet)
                self.assertNotIn("source_context", packet)

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
        from upgradepilot.github.api import GitHubAcquisitionError

        with self.assertRaises(GitHubAcquisitionError) as raised:
            session.get("https://api.github.com/repos/a/b")
        self.assertEqual(raised.exception.reason, "trial_request_limit")
        self.assertTrue(session.request_limit_reached)
        self.assertEqual(session.github_requests, 50)

    def test_provider_requests_disable_redirects(self):
        session = TrialPublicSession()
        with patch("requests.Session.request") as request:
            session.get("https://api.github.com/repos/a/b")
            self.assertFalse(request.call_args.kwargs["allow_redirects"])
            self.assertEqual(session.github_requests, 1)


class PublisherInspectionTests(TestCase):
    def test_publisher_inspection_is_independent_of_homepage_labels(self):
        from experiments.api_change_source_acquisition import (
            PublisherProvenanceInspector,
        )
        from upgradepilot.pypi.provenance import FileProvenanceProblem
        from upgradepilot.pypi.release import DistributionFile

        item = replace(
            release(
                links=[
                    ProjectUrlCandidate("Source", "https://github.com/owner/demo"),
                    ProjectUrlCandidate("Homepage", "https://example.org"),
                ]
            ),
            distribution_files=(
                DistributionFile(
                    "demo.whl",
                    "https://files.pythonhosted.org/demo.whl",
                    "a" * 64,
                    "bdist_wheel",
                ),
            ),
        )
        client = Mock()
        client.get_file_provenance.return_value = FileProvenanceProblem(
            "provenance_unavailable",
            "demo",
            "2.0",
            "demo.whl",
            "https://pypi.org/integrity/demo/2.0/demo.whl/provenance",
            "absent",
        )
        inspected = PublisherProvenanceInspector(client=client).resolve(item)
        result = associate_declared_source(item, inspected)
        self.assertIsInstance(result, DeclaredSourceAssociation)
        self.assertEqual(result.ignored_links[0].label, "Homepage")
        self.assertEqual(len(inspected.records), 1)

    def test_mixed_conflicting_and_malformed_publisher_evidence_blocks(self):
        from experiments.api_change_source_acquisition import (
            PublisherProvenanceInspector,
        )
        from upgradepilot.pypi.provenance import (
            FileProvenanceEvidence,
            PublisherIdentity,
        )
        from upgradepilot.pypi.release import DistributionFile

        item = replace(
            release(),
            distribution_files=(
                DistributionFile(
                    "demo.whl",
                    "https://files.pythonhosted.org/demo.whl",
                    "a" * 64,
                    "bdist_wheel",
                ),
            ),
        )
        for publishers in (
            (PublisherIdentity("GitHub", "wrong/repo", None),),
            (
                PublisherIdentity("GitHub", "owner/demo", None),
                PublisherIdentity("other", None, None),
            ),
            (PublisherIdentity("GitHub", None, None),),
        ):
            with self.subTest(publishers=publishers):
                client = Mock()
                client.get_file_provenance.return_value = FileProvenanceEvidence(
                    "demo",
                    "2.0",
                    "demo.whl",
                    "a" * 64,
                    "https://pypi.org/integrity/demo/2.0/demo.whl/provenance",
                    NOW,
                    1,
                    1,
                    publishers,
                )
                inspected = PublisherProvenanceInspector(client=client).resolve(item)
                self.assertIsInstance(
                    associate_declared_source(item, inspected), AcquisitionProblem
                )

    def test_explicit_token_never_reaches_pypi_or_redirects(self):
        session = TrialPublicSession(token="synthetic-test-value")
        with patch("requests.Session.request") as request:
            session.get("https://api.github.com/repos/a/b")
            self.assertIn("Authorization", request.call_args.kwargs["headers"])
            session.get("https://pypi.org/pypi/demo/json")
            self.assertNotIn("Authorization", request.call_args.kwargs["headers"])
            self.assertFalse(request.call_args.kwargs["allow_redirects"])
