"""Ordinary-input composition and saved producer-fact replay boundary controls."""

from unittest import TestCase
from unittest.mock import Mock

from experiments.api_adapter_context_replay import decode_adapter_seed
from experiments.api_adapter_exploration import AdapterExploration
from experiments.api_change_source_acquisition import (
    AcquisitionProblem,
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
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.github.repository import RepositoryTextFile

SHA = "a" * 40
BASE = "b" * 40


class PublicPRTests(TestCase):
    def run_trial(self):
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
        upstream = Mock()
        upstream.acquire.return_value = AcquisitionProblem(
            "upstream", "source_unavailable", "retained gap"
        )
        adapters = Mock()
        adapters.explore.return_value = AdapterExploration((), (), ())
        result = acquire_public_pr_context(
            "owner/target",
            7,
            pull_requests=pr,
            files=files,
            target=TargetContextAcquirer(inventory=inventory, files=files),
            upstream=upstream,
            adapters=adapters,
        )
        return result, pr, inventory

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
