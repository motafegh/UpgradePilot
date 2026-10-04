"""Ordinary-input composition and saved producer-fact replay boundary controls."""

import hashlib
import json
from datetime import UTC, datetime
from unittest import TestCase
from unittest.mock import Mock

from experiments.api_adapter_context_replay import decode_adapter_seed
from experiments.api_adapter_exploration import AdapterExploration
from experiments.api_change_source_acquisition import (
    AcquisitionProblem,
    DeclaredReleaseWindowAcquirer,
    PublisherProvenanceInspection,
    TrialPublicSession,
)
from experiments.api_target_context import (
    InventoryEntry,
    TargetContextAcquirer,
    TargetInventory,
)
from experiments.api_target_context_smoke import (
    PublicPRContextTrial,
    acquire_public_pr_context,
    trial_manifest,
)
from upgradepilot.github.changelog import DiscoveredChangelogPath
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.tag import GitHubTagCommitEvidence
from upgradepilot.pypi.release import (
    PackageReleaseEvidence,
    PackageReleaseIndexEvidence,
    ProjectUrlCandidate,
)

SHA = "a" * 40
BASE = "b" * 40


class PublicPRTests(TestCase):
    def run_trial(self, *, upstream=None):
        identity = PullRequestIdentity(
            "owner/target",
            7,
            "Bump vendor",
            "open",
            False,
            "bot",
            "main",
            BASE,
            "update",
            SHA,
            1,
        )
        pr = Mock()
        pr.get_pull_request.return_value = identity
        pr.get_changed_files.return_value = (
            ChangedFile(
                "requirements.txt",
                "modified",
                1,
                1,
                2,
                "@@ -1 +1 @@\n-vendor==1.0\n+vendor==2.0",
            ),
        )
        inventory = Mock()
        inventory.acquire.return_value = TargetInventory(
            "owner/target",
            SHA,
            "c" * 40,
            (
                InventoryEntry("different.py", "blob", "100644"),
                InventoryEntry("requirements.txt", "blob", "100644"),
            ),
            False,
        )
        files = Mock()
        files.get_exact_commit_text_file.side_effect = lambda repo, sha, path: (
            RepositoryTextFile(
                repo,
                path,
                sha,
                "from bridge.testing import Client as C\nC(app)"
                if path == "different.py"
                else 'vendor==2.0\nbridge[standard]; python_version < "3.12"\n',
            )
        )
        if upstream is None:
            upstream = Mock()
            upstream.acquire.return_value = AcquisitionProblem(
                "upstream", "source_unavailable", "retained gap"
            )
        adapters = Mock()
        adapters.explore.return_value = AdapterExploration(
            (),
            (
                AcquisitionProblem(
                    "adapter", "source_unavailable", "independent adapter gap"
                ),
            ),
            (),
        )
        result = acquire_public_pr_context(
            "owner/target",
            7,
            pull_requests=pr,
            files=files,
            target=TargetContextAcquirer(inventory=inventory, files=files),
            upstream=upstream,
            adapters=adapters,
        )
        adapters.explore.assert_called_once_with(result.target)
        return result, pr, inventory

    def upstream_runner(self, text):
        """Provider responses only; normal PR analysis still supplies the interval."""
        now = datetime(2026, 10, 4, tzinfo=UTC)
        releases = Mock()
        releases.get_release.side_effect = lambda package, version: (
            PackageReleaseEvidence(
                package,
                package,
                version,
                package,
                version,
                f"https://pypi.org/pypi/{package}/{version}/json",
                now,
                1,
                (),
                (ProjectUrlCandidate("Source", "https://github.com/owner/vendor"),),
            )
        )
        index = Mock()
        index.get_release_index.return_value = PackageReleaseIndexEvidence(
            "vendor",
            "vendor",
            "vendor",
            "https://pypi.org/pypi/vendor/json",
            now,
            1,
            ("1.0", "1.5", "2.0"),
        )
        provenance = Mock()
        provenance.resolve.return_value = PublisherProvenanceInspection(
            "source_unavailable", "no publisher records"
        )
        tags = Mock()
        tags.resolve_tag_to_commit.side_effect = lambda repo, tag: (
            GitHubTagCommitEvidence(
                repo, tag, "refs/tags/" + tag, "commit", SHA, SHA, (), now
            )
        )
        paths = Mock()
        paths.discover.return_value = DiscoveredChangelogPath(
            "owner/vendor", SHA, "c" * 40, "CHANGELOG.md", ("CHANGELOG.md",)
        )
        files = Mock()
        files.get_exact_commit_text_file.return_value = RepositoryTextFile(
            "owner/vendor", "CHANGELOG.md", SHA, text
        )
        return DeclaredReleaseWindowAcquirer(
            releases=releases,
            index=index,
            provenance=provenance,
            tags=tags,
            paths=paths,
            files=files,
        )

    def test_partial_source_survives_normal_pr_manifest_and_target_replay(self):
        text = "## 2.0\nretained café\n"
        runner = self.upstream_runner(text)
        result, _, _ = self.run_trial(upstream=runner)
        packet = json.loads(json.dumps(trial_manifest(result, TrialPublicSession())))
        self.assertEqual(packet["state"], "context_acquired")
        source = packet["upstream"]
        self.assertEqual(source["state"], "incomplete")
        self.assertFalse(source["complete_window_eligible"])
        self.assertNotIn("window_sha256", source)
        examination = source["section_examination"]
        self.assertEqual(examination["required_versions"], ["1.5", "2.0"])
        self.assertEqual(examination["missing_or_unsupported_versions"], ["1.5"])
        self.assertEqual(examination["candidates"][0]["text"], text)
        self.assertEqual(
            examination["full_source_sha256"], hashlib.sha256(text.encode()).hexdigest()
        )
        self.assertEqual(source["source_context"]["interval"]["package"], "vendor")
        runner.paths.discover.assert_called_once_with("owner/vendor", SHA)
        seed = decode_adapter_seed(packet)
        self.assertEqual(seed.references, result.target.references)
        self.assertEqual(seed.candidates, result.target.candidates)
        self.assertEqual(
            packet["adapter_exploration"]["problems"][0]["detail"],
            "independent adapter gap",
        )

    def test_ambiguous_source_in_normal_composition_is_never_complete(self):
        text = "## 2.0\nfirst\n## 1.5\nknown\n## 2.0\nsecond\n"
        result, _, _ = self.run_trial(upstream=self.upstream_runner(text))
        packet = json.loads(json.dumps(trial_manifest(result, TrialPublicSession())))
        source = packet["upstream"]
        self.assertFalse(source["complete_window_eligible"])
        self.assertEqual(source["section_examination"]["ambiguous_versions"], ["2.0"])
        self.assertEqual(
            [c["match_count"] for c in source["section_examination"]["candidates"]],
            [2, 1, 2],
        )

    def test_oversize_source_keeps_recovery_in_normal_pr_manifest(self):
        text = "## 2.0\n" + "x" * 20000 + "\n## 1.5\nknown\n"
        result, _, _ = self.run_trial(upstream=self.upstream_runner(text))
        packet = json.loads(json.dumps(trial_manifest(result, TrialPublicSession())))
        source = packet["upstream"]
        self.assertFalse(source["complete_window_eligible"])
        self.assertEqual(source["reason"], "window_too_large")
        examination = source["section_examination"]
        self.assertEqual(examination["required_versions"], ["1.5", "2.0"])
        self.assertEqual(examination["max_characters"], 20000)
        for candidate in examination["candidates"]:
            self.assertIsNone(candidate["text"])
            recovered = text[candidate["start_offset"] : candidate["end_offset"]]
            self.assertEqual(
                candidate["sha256"], hashlib.sha256(recovered.encode()).hexdigest()
            )
        self.assertEqual(
            decode_adapter_seed(packet).candidates, result.target.candidates
        )

    def test_ordinary_pr_changes_drive_dependency_and_inventory_with_no_known_path(
        self,
    ):
        result, pr, inventory = self.run_trial()
        self.assertIsInstance(result, PublicPRContextTrial)
        self.assertEqual(result.analysis.dependency.normalized_package, "vendor")
        self.assertEqual(result.analysis.dependency.proposed_version, "2.0")
        inventory.acquire.assert_called_once_with("owner/target", SHA)
        pr.get_changed_files.assert_called_once_with(result.identity)
        self.assertEqual(result.target.candidates[0].imported_module, "bridge.testing")
        self.assertIsNotNone(result.target.candidates[0].declaration.marker)
        self.assertEqual(result.upstream.reason, "source_unavailable")

    def test_retained_producer_seed_roundtrip_and_foreign_source_rejection(self):
        result, _, _ = self.run_trial()
        packet = trial_manifest(result, TrialPublicSession())
        seed = decode_adapter_seed(packet)
        self.assertEqual(seed.candidates, result.target.candidates)
        self.assertEqual(seed.references, result.target.references)
        packet["target"]["candidates"][0]["import_source_id"] = "foreign/source"
        with self.assertRaises(ValueError):
            decode_adapter_seed(packet)

    def test_replay_does_not_accept_absent_normal_context_or_revision_mismatch(self):
        with self.assertRaises(ValueError):
            decode_adapter_seed({"state": "incomplete"})
        result, _, _ = self.run_trial()
        packet = trial_manifest(result, TrialPublicSession())
        packet["identity"]["head_sha"] = "d" * 40
        with self.assertRaises(ValueError):
            decode_adapter_seed(packet)
