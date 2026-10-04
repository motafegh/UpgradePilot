"""Ordinary-input composition and saved producer-fact replay boundary controls."""

import hashlib
import json
from contextlib import redirect_stdout
from datetime import UTC, datetime
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import Mock, patch

from experiments.api_adapter_context_replay import decode_adapter_seed
from experiments.api_adapter_context_replay import main as replay_main
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
    def run_trial(self, *, upstream=None, python_source=None):
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
                (
                    python_source
                    if python_source is not None
                    else "from bridge.testing import Client as C\nC(app)"
                )
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

    def test_ordered_alias_results_survive_ordinary_pr_json_and_cli_recovery(self):
        source = (
            "from bridge.testing import Client as C\nS=C\nC=None\nC(app)\nC=S\nC(app)\n"
        )
        result, _, _ = self.run_trial(python_source=source)
        packet = json.loads(json.dumps(trial_manifest(result, TrialPublicSession())))
        seed = decode_adapter_seed(packet)
        self.assertEqual(seed.binding_analysis_version, 2)
        self.assertEqual(seed.references, result.target.references)
        self.assertEqual(
            [r.lexical_import for r in seed.references], [None, "bridge.testing.Client"]
        )
        # Actual CLI input/read/decode/output; acquisition is separately controlled.
        output = StringIO()
        explorer = Mock()
        explorer.explore.return_value = AdapterExploration((), (), ())
        with TemporaryDirectory() as directory:
            path = Path(directory) / "normal-context.json"
            path.write_text(json.dumps(packet))
            with (
                patch("sys.argv", ["adapter-replay", str(path)]),
                patch(
                    "experiments.api_adapter_context_replay.AdapterSourceExplorer",
                    return_value=explorer,
                ),
                redirect_stdout(output),
            ):
                status = replay_main()
        self.assertEqual(status, 0)
        self.assertEqual(explorer.explore.call_args.args[0], seed)
        self.assertEqual(
            json.loads(output.getvalue())["input_binding_analysis_version"], 2
        )

    def test_shared_trace_steps_are_interned_without_losing_native_facts(self):
        result, _, _ = self.run_trial(
            python_source="from bridge.testing import Client as C\nC()\nC()\nC()\n"
        )
        packet = json.loads(json.dumps(trial_manifest(result, TrialPublicSession())))
        trace = packet["target"]["binding_trace_steps"]
        self.assertEqual(sum(s["operation"] == "import" for s in trace), 1)
        self.assertTrue(
            all(
                type(i) is int
                for r in packet["target"]["references"]
                for i in r["binding"]["trace"]
            )
        )
        self.assertEqual(
            decode_adapter_seed(packet).references, result.target.references
        )

    def test_legacy_packets_remain_legacy_and_unknown_versions_are_rejected(self):
        result, _, _ = self.run_trial()
        packet = json.loads(json.dumps(trial_manifest(result, TrialPublicSession())))
        for version in (False, 3, "2"):
            packet["target"]["binding_analysis_version"] = version
            with self.subTest(version=version), self.assertRaises(ValueError):
                decode_adapter_seed(packet)
        del packet["target"]["binding_analysis_version"]
        packet["target"].pop("binding_trace_steps")
        # New assessments cannot be silently downgraded to a legacy packet.
        with self.assertRaises(ValueError):
            decode_adapter_seed(packet)
        for ref in packet["target"]["references"]:
            ref.pop("binding")
        seed = decode_adapter_seed(packet)
        self.assertEqual(seed.binding_analysis_version, 1)
        self.assertIsNone(seed.references[0].binding)
        self.assertEqual(seed.references[0].lexical_import, "bridge.testing.Client")

    def test_conditional_origins_cannot_be_promoted_by_saved_input(self):
        result, _, _ = self.run_trial(
            python_source="if flag:\n from bridge.testing import Client as C\nelse:\n from other import Client as C\nC(app)\n"
        )
        packet = json.loads(json.dumps(trial_manifest(result, TrialPublicSession())))
        self.assertEqual(
            decode_adapter_seed(packet).references[0].binding.state, "conditional"
        )
        packet["target"]["references"][0]["lexical_import"] = "bridge.testing.Client"
        packet["target"]["references"][0]["binding_limit"] = None
        with self.assertRaises(ValueError):
            decode_adapter_seed(packet)

    def test_saved_binding_trace_sources_ranges_indices_and_shapes_are_checked(self):
        result, _, _ = self.run_trial()
        original = trial_manifest(result, TrialPublicSession())
        for mutation in (
            "foreign",
            "negative_range",
            "reversed_range",
            "bad_index",
            "boolean_index",
            "origin_shape",
            "bad_flag",
            "wrong_state",
            "empty_trace",
            "empty_limit",
            "reference_line",
            "table_shape",
            "nonstring_source",
            "kind_shape",
            "missing_field",
        ):
            packet = json.loads(json.dumps(original))
            ref = packet["target"]["references"][0]
            binding = ref["binding"]
            step = packet["target"]["binding_trace_steps"][0]
            if mutation == "foreign":
                step["source_id"] = "foreign/source"
            elif mutation == "negative_range":
                step["column"] = -1
            elif mutation == "reversed_range":
                step["end_line"] = 0
            elif mutation == "bad_index":
                binding["trace"] = [-1]
            elif mutation == "boolean_index":
                binding["trace"] = [True]
            elif mutation == "origin_shape":
                binding["possible_imports"] = "ABC"
            elif mutation == "bad_flag":
                binding["unknown_possible"] = 0
            elif mutation == "wrong_state":
                binding["state"] = "unknown"
            elif mutation == "empty_trace":
                binding["trace"] = []
            elif mutation == "empty_limit":
                ref["binding_limit"] = ""
            elif mutation == "reference_line":
                ref["line"] = True
            elif mutation == "table_shape":
                packet["target"]["binding_trace_steps"] = False
            elif mutation == "nonstring_source":
                step["source_id"] = []
            elif mutation == "kind_shape":
                ref["kind"] = []
            elif mutation == "missing_field":
                ref.pop("expression")
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                decode_adapter_seed(packet)
