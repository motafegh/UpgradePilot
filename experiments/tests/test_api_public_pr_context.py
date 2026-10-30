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
from experiments.api_adapter_exploration import AdapterExploration, PythonSourceAcquisitionWork
from experiments.api_change_source_acquisition import (
    AcquisitionProblem,
    DeclaredReleaseWindowAcquirer,
    PublisherProvenanceInspection,
    TrialPublicSession,
)
from experiments.api_change_interpretation import (
    ProviderReply,
    ROLE,
    ROLE_V2,
    LOCAL_MODEL,
    COMPARISON_MODEL,
    interpret_projection,
    packet_hash,
    prepare_request,
    source_input_from_projection,
)
from experiments.api_change_interpretation_trial import (
    PACKET_KIND,
    decode_saved_trial,
    dependency_interval,
    read_saved_trial,
    run_interpretation_trial,
    save_trial,
)
from experiments.api_change_interpretation_trial import main as interpretation_main
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
from upgradepilot.github.pull_request import (
    ChangedFile, PullRequestIdentity, PullRequestObservation, PullRequestDescriptionObservation,
)
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
    def test_examination_question_cap_keeps_unexamined_changed_modules_visible(self):
        from experiments.tests.test_api_adapter_exploration import ChainTests

        result, _, _ = self.run_trial(source_explorer=ChainTests().explorer(),
            python_source="\n".join(f"import vendor.module{i}" for i in range(8)))
        self.assertEqual(len(result.changed_sources), 12)
        self.assertEqual(result.unexamined_changed_modules, ("vendor.module6", "vendor.module7"))
        packet = trial_manifest(result, TrialPublicSession())
        self.assertEqual(packet["changed_package_sources"]["unexamined_modules"], result.unexamined_changed_modules)
        self.assertTrue(all(attempt.outcome.reason == "module_path_not_established"
                            for attempt in result.changed_sources))

    def test_ordinary_pr_derives_exact_changed_module_sources_through_acquired_adapter_imports(self):
        from experiments.tests.test_api_adapter_exploration import ChainTests

        explorer = ChainTests().explorer()
        result, _, _ = self.run_trial(source_explorer=explorer)
        self.assertEqual([sample.candidate.declaration.package for sample in result.adapters.samples],
                         ["bridge", "mediator"])
        self.assertEqual([candidate.declaration.package for candidate in result.adapters.deferred_candidates], ["vendor"])
        attempts = result.changed_sources
        self.assertEqual([attempt.request.version for attempt in attempts], ["1.0", "2.0"])
        self.assertEqual([attempt.request.version_basis for attempt in attempts],
                         ["native_old_version", "native_proposed_version"])
        self.assertEqual({attempt.request.module for attempt in attempts}, {"vendor"})
        self.assertTrue(all("vendor" in attempt.request.origin.expression for attempt in attempts))
        self.assertEqual(result.source_work.release_identities,
                         (("bridge", "2.0"), ("mediator", "2.0"), ("vendor", "1.0"), ("vendor", "2.0")))
        self.assertEqual(result.source_work.module_attempts, 4)
        self.assertEqual(explorer.releases.get_release.call_count, 4)
        self.assertEqual(explorer.files.get_exact_commit_text_file.call_count, 4)
        packet = json.loads(json.dumps(trial_manifest(result, TrialPublicSession())))
        self.assertEqual([attempt["state"] for attempt in packet["changed_package_sources"]["attempts"]],
                         ["module_examined", "module_examined"])
        self.assertEqual(packet["changed_package_sources"]["attempts"][0]["request"]["version"], "1.0")
        self.assertEqual(decode_adapter_seed(packet).references, result.target.references)

    def test_changed_package_is_not_sampled_at_an_unrelated_latest_version(self):
        from experiments.tests.test_api_adapter_exploration import ChainTests, index

        explorer = ChainTests().explorer()
        explorer.index.get_release_index.side_effect = lambda package: index(package, ("1.0", "2.0", "3.0"))
        result, _, _ = self.run_trial(source_explorer=explorer)
        self.assertEqual({a.request.version for a in result.changed_sources}, {"1.0", "2.0"})
        self.assertTrue(all(a.outcome.metadata.version == a.request.version for a in result.changed_sources))
        self.assertEqual({call.args[0] for call in explorer.index.get_release_index.call_args_list},
                         {"bridge", "mediator"})
        self.assertEqual(len(result.source_work.release_identities), 4)

    def test_conditional_target_import_can_be_examined_without_becoming_positive_exploration(self):
        from experiments.tests.test_api_adapter_exploration import ChainTests

        explorer = ChainTests().explorer()
        result, _, _ = self.run_trial(source_explorer=explorer,
            python_source="if flag:\n import vendor\nelse:\n import other as vendor\nvendor.run()\n")
        self.assertFalse(result.adapters.samples)
        self.assertEqual(result.target.references[0].binding.state, "conditional")
        self.assertIsNone(result.target.references[0].lexical_import)
        self.assertEqual(len(result.changed_sources), 2)
        self.assertEqual({attempt.request.version_basis for attempt in result.changed_sources},
                         {"native_old_version", "native_proposed_version"})
        self.assertTrue(all(attempt.request.origin.binding.state == "conditional" for attempt in result.changed_sources))
        self.assertTrue(all(attempt.request.origin.lexical_import is None for attempt in result.changed_sources))
        explorer.index.get_release_index.assert_not_called()

    def test_shared_prefix_evaluates_transition_once_without_ci_preparation(self):
        from upgradepilot import investigation_inputs

        with patch(
            "upgradepilot.investigation_inputs.analyze_dependency_change",
            wraps=investigation_inputs.analyze_dependency_change,
        ) as analyze, patch(
            "upgradepilot.investigation_inputs.prepare_ci_evidence",
            side_effect=AssertionError("source acquisition must not prepare CI"),
        ):
            result, pr, _ = self.run_trial()
        analyze.assert_called_once()
        pr.get_pull_request_observation.assert_called_once_with("owner/target", 7)
        self.assertEqual(result.inputs.description.text, "Initial dependency PR description")
        self.assertEqual(result.analysis.source_contexts, result.inputs.source_contexts)

    def test_native_identity_guard_stops_before_changed_files_and_source_reads(self):
        result, original_pr, _ = self.run_trial()
        for guard in ({"expected_head": "f" * 40}, {"expected_base": "f" * 40}):
            with self.subTest(guard=guard):
                pr, files, target = Mock(), Mock(), Mock()
                pr.get_pull_request_observation.return_value = original_pr.get_pull_request_observation.return_value
                with self.assertRaisesRegex(ValueError, "frozen base/head"):
                    acquire_public_pr_context("owner/target", 7, pull_requests=pr,
                                              files=files, target=target, **guard)
                pr.get_changed_files.assert_not_called()
                files.get_exact_commit_text_file.assert_not_called()
                target.acquire.assert_not_called()

    def test_changed_file_acquisition_refusal_keeps_problem_and_stops_sources(self):
        from upgradepilot.github.api import GitHubAcquisitionError

        _, original_pr, _ = self.run_trial()
        pr, target = Mock(), Mock()
        pr.get_pull_request_observation.return_value = original_pr.get_pull_request_observation.return_value
        error = GitHubAcquisitionError("Incomplete PR change set", reason="incomplete_changed_files")
        pr.get_changed_files.side_effect = error
        result = acquire_public_pr_context("owner/target", 7, pull_requests=pr,
                                           files=Mock(), target=target)
        self.assertIsInstance(result, AcquisitionProblem)
        self.assertEqual(result.reason, "incomplete_changed_files")
        self.assertIs(result.evidence, error)
        target.acquire.assert_not_called()

    def run_trial(
        self,
        *,
        upstream=None,
        python_source=None,
        interpretation_provider=None,
        role_version=ROLE,
        model_identifier=LOCAL_MODEL,
        source_explorer=None,
        session=None,
    ):
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
        description_text = "Initial dependency PR description"
        pr.get_pull_request_observation.return_value = PullRequestObservation(
            identity,
            PullRequestDescriptionObservation(
                "retained", description_text, "https://github.com/owner/target/pull/7",
                datetime(2026, 10, 29, tzinfo=UTC),
                hashlib.sha256(description_text.encode()).hexdigest(), len(description_text),
            ),
        )
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
        adapters = source_explorer
        if adapters is None:
            adapters = Mock()
            adapters.source_run.return_value.max_module_files = 12
            adapters.source_run.return_value.work = PythonSourceAcquisitionWork((), 0, 0)
            adapters.source_run.return_value.examine.return_value = AcquisitionProblem(
                "python_source", "source_unavailable", "controlled exact-source gap",
            )
            adapters.explore.return_value = AdapterExploration(
                (), (AcquisitionProblem("adapter", "source_unavailable", "independent adapter gap"),), (),
            )
        entry = (
            acquire_public_pr_context
            if interpretation_provider is None
            else run_interpretation_trial
        )
        options = (
            {}
            if interpretation_provider is None
            else {
                "provider": interpretation_provider,
                "role_version": role_version,
                "model_identifier": model_identifier,
            }
        )
        if session is not None:
            options["session"] = session
        result = entry(
            "owner/target",
            7,
            pull_requests=pr,
            files=files,
            target=TargetContextAcquirer(inventory=inventory, files=files),
            upstream=upstream,
            adapters=adapters,
            **options,
        )
        if interpretation_provider is None and source_explorer is None:
            adapters.explore.assert_called_once_with(
                result.target, source_run=adapters.source_run.return_value, stop_at_package="vendor",
            )
        elif source_explorer is None:
            adapters.explore.assert_called_once()
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

    def interpreted_trial(
        self, *, text=None, reply=None, role_version=ROLE, model_identifier=LOCAL_MODEL
    ):
        if text is None:
            text = "## 2.0\nThe old option was removed. café\n## 1.5\nAn unrelated addition.\n"
        provider = Mock(
            identity={"kind": "controlled_integration", "semantic_acceptance": False}
        )
        provider.complete.return_value = reply or ProviderReply(
            json.dumps(
                {
                    "observations": [
                        {
                            "kind": "removal",
                            "subject": "old option",
                            "summary": "The old option was removed.",
                            "assertion": "affirmed",
                            "timing": "current",
                            "effective_version": "2.0",
                            "source_spans": [
                                {"start_line_id": "S1:L2", "end_line_id": "S1:L2"}
                            ],
                            "reason": "The cited text states a removal in the current release."
                            if role_version == ROLE_V2
                            else None,
                        }
                    ],
                    "unassessed": [
                        {
                            "source_spans": [
                                {"start_line_id": "S2:L2", "end_line_id": "S2:L2"}
                            ],
                            "reason": "Controlled provider did not interpret this addition.",
                        }
                    ],
                }
            )
        )
        packet, _, _ = self.run_trial(
            upstream=self.upstream_runner(text),
            interpretation_provider=provider,
            role_version=role_version,
            model_identifier=model_identifier,
        )
        return packet, provider, text

    def test_versioned_normal_entry_recovery_and_role_relabelling_rejection(self):
        for role, model_identifier in (
            (ROLE, LOCAL_MODEL),
            (ROLE_V2, LOCAL_MODEL),
            (ROLE_V2, COMPARISON_MODEL),
        ):
            packet, provider, _ = self.interpreted_trial(
                role_version=role, model_identifier=model_identifier
            )
            self.assertEqual(packet["interpretation"]["state"], "observations_returned")
            self.assertEqual(packet["interpretation"]["role_version"], role)
            self.assertEqual(
                packet["interpretation"]["method"]["model"], model_identifier
            )
            self.assertEqual(
                provider.complete.call_args.args[0].method["role_version"], role
            )
            with patch(
                "experiments.api_change_interpretation_trial.LocalInterpretationProvider"
            ) as local:
                self.assertEqual(
                    packet_hash(decode_saved_trial(json.dumps(packet))),
                    packet_hash(packet),
                )
            local.assert_not_called()
            packet["interpretation"]["role_version"] = ROLE_V2 if role == ROLE else ROLE
            packet["packet_sha256"] = packet_hash(
                {k: v for k, v in packet.items() if k != "packet_sha256"}
            )
            with self.assertRaises(ValueError):
                decode_saved_trial(json.dumps(packet))

    def test_ordinary_acquisition_to_proposal_to_offline_saved_recovery(self):
        packet, provider, text = self.interpreted_trial()
        self.assertEqual(packet["interpretation"]["state"], "observations_returned")
        provider.complete.assert_called_once()
        self.assertEqual(packet["context"]["dependency"]["package"], "vendor")
        self.assertEqual(packet["context"]["target"]["revision"], SHA)
        self.assertEqual(len(packet["interpretation"]["source_input"]["sections"]), 2)
        with TemporaryDirectory() as root:
            path = Path(root) / "trial.json"
            save_trial(packet, path)
            with (
                patch(
                    "experiments.api_change_interpretation_trial.LocalInterpretationProvider"
                ) as local,
                patch(
                    "experiments.api_change_interpretation_trial.acquire_public_pr_context"
                ) as acquire,
            ):
                recovered = read_saved_trial(path)
            local.assert_not_called()
            acquire.assert_not_called()
            self.assertEqual(packet_hash(recovered), packet_hash(packet))
            citation = recovered["interpretation"]["observations"][0]["evidence"][0]
            self.assertEqual(
                text[citation["start_offset"] : citation["end_offset"]],
                citation["quote"],
            )
            self.assertEqual(citation["source_identity"]["revision"], SHA)
            with self.assertRaises(FileExistsError):
                save_trial(packet, path)

    def test_saved_pilot_output_budget_survives_default_extension(self):
        packet, _, _ = self.interpreted_trial()
        interpretation = packet["interpretation"]
        historical = prepare_request(
            interpretation["source_input"], max_output_tokens=1536
        )
        interpretation["method"] = {
            **historical.method,
            "provider": interpretation["method"]["provider"],
        }
        packet["packet_sha256"] = packet_hash(
            {k: v for k, v in packet.items() if k != "packet_sha256"}
        )
        self.assertEqual(
            packet_hash(decode_saved_trial(json.dumps(packet))), packet_hash(packet)
        )
        # Changing the recorded setting without reconstructing its request is rejected.
        interpretation["method"]["max_output_tokens"] = 8192
        packet["packet_sha256"] = packet_hash(
            {k: v for k, v in packet.items() if k != "packet_sha256"}
        )
        with self.assertRaises(ValueError):
            decode_saved_trial(json.dumps(packet))

    def test_interpretation_failures_preserve_target_adapters_and_save_readback(self):
        for reply in (
            ProviderReply("{}"),
            ProviderReply("{}", "length"),
            ProviderReply(problem=("context_problem", "effective_capacity_unverified")),
        ):
            packet, _, _ = self.interpreted_trial(reply=reply)
            result = packet["interpretation"]
            self.assertNotEqual(result["state"], "observations_returned")
            self.assertTrue(packet["context"]["target"]["references"])
            self.assertEqual(
                packet["context"]["adapter_exploration"]["problems"][0]["detail"],
                "independent adapter gap",
            )
            self.assertEqual(result["observations"], [])
            self.assertEqual(
                packet_hash(decode_saved_trial(json.dumps(packet))), packet_hash(packet)
            )
        packet, provider, _ = self.interpreted_trial(
            text="## 2.0\n" + "x" * 20000 + "\n## 1.5\nknown\n"
        )
        self.assertEqual(packet["interpretation"]["state"], "input_problem")
        provider.complete.assert_not_called()
        decode_saved_trial(json.dumps(packet))

    def test_partial_source_can_propose_without_becoming_complete(self):
        reply = ProviderReply(
            json.dumps(
                {
                    "observations": [
                        {
                            "kind": "removal",
                            "subject": "old option",
                            "summary": "Removed.",
                            "assertion": "affirmed",
                            "timing": "current",
                            "effective_version": "2.0",
                            "source_spans": [
                                {"start_line_id": "S1:L2", "end_line_id": "S1:L2"}
                            ],
                            "reason": None,
                        }
                    ],
                    "unassessed": [],
                }
            )
        )
        packet, _, _ = self.interpreted_trial(
            text="## 2.0\nThe old option was removed.\n", reply=reply
        )
        self.assertEqual(packet["interpretation"]["state"], "observations_returned")
        scope = packet["interpretation"]["source_input"]["source_coverage"]
        self.assertFalse(scope["complete_window_eligible"])
        self.assertEqual(scope["missing_or_unsupported_versions"], ["1.5"])
        decode_saved_trial(json.dumps(packet))

    def test_saved_reader_rejects_tampering_even_with_recomputed_outer_digest(self):
        original, _, _ = self.interpreted_trial()
        mutations = (
            lambda p: p.update(packet_version=2),
            lambda p: p["interpretation"]["observations"][0]["evidence"][0].update(
                quote="invented"
            ),
            lambda p: p["interpretation"]["observations"][0]["evidence"][0].update(
                start_offset=0
            ),
            lambda p: p["interpretation"]["observations"][0]["source_spans"][0].update(
                end_line_id="S2:L2"
            ),
            lambda p: p["interpretation"]["source_input"]["sections"][0]["lines"][
                1
            ].update(text="changed"),
            lambda p: p["interpretation"]["source_input"]["source_coverage"].update(
                complete_window_eligible=False
            ),
            lambda p: p["interpretation"]["method"].update(request_sha256="wrong"),
            lambda p: p["context"]["target"].update(revision="b" * 40),
            lambda p: p["interpretation"].update(state="no_observations_returned"),
            lambda p: p["interpretation"]["observations"][0].update(
                compatibility="safe"
            ),
        )
        for mutate in mutations:
            packet = json.loads(json.dumps(original))
            mutate(packet)
            packet["packet_sha256"] = packet_hash(
                {k: v for k, v in packet.items() if k != "packet_sha256"}
            )
            with self.subTest(mutation=mutate), self.assertRaises(ValueError):
                decode_saved_trial(json.dumps(packet))
        original["packet_sha256"] = "wrong"
        with self.assertRaises(ValueError):
            decode_saved_trial(json.dumps(original))
        for raw in ("{}", "[]", "null", '{"a":1,"a":2}', "x" * (8 * 1024 * 1024 + 1)):
            with self.assertRaises(ValueError):
                decode_saved_trial(raw)

    def test_opt_in_cli_run_and_offline_open_preserve_controlled_proof(self):
        packet, _, _ = self.interpreted_trial()
        with TemporaryDirectory() as root:
            path = Path(root) / "trial.json"
            with (
                patch(
                    "sys.argv",
                    ["trial", "run", "owner/target", "7", "--save", str(path)],
                ),
                patch(
                    "experiments.api_change_interpretation_trial.run_interpretation_trial",
                    return_value=packet,
                ) as run,
                redirect_stdout(StringIO()) as output,
            ):
                self.assertEqual(interpretation_main(), 0)
            self.assertEqual(run.call_args.args, ("owner/target", 7))
            self.assertEqual(
                json.loads(output.getvalue())["interpretation"]["method"]["provider"][
                    "kind"
                ],
                "controlled_integration",
            )
            with (
                patch("sys.argv", ["trial", "open", str(path)]),
                patch(
                    "experiments.api_change_interpretation_trial.run_interpretation_trial"
                ) as run,
                redirect_stdout(StringIO()) as output,
            ):
                self.assertEqual(interpretation_main(), 0)
            run.assert_not_called()
            self.assertEqual(
                json.loads(output.getvalue())["packet_sha256"], packet["packet_sha256"]
            )

    def test_acquisition_failure_is_saved_without_inference(self):
        provider = Mock(identity={"kind": "controlled_integration"})
        problem = AcquisitionProblem(
            "public_pr", "source_unavailable", "PR unavailable"
        )
        with patch(
            "experiments.api_change_interpretation_trial.acquire_public_pr_context",
            return_value=problem,
        ):
            packet = run_interpretation_trial("owner/target", 7, provider=provider)
        provider.complete.assert_not_called()
        self.assertIsNone(packet["interpretation"])
        self.assertEqual(packet["context"]["reason"], "source_unavailable")
        decode_saved_trial(json.dumps(packet))

    def test_saved_failure_state_must_agree_with_source_and_request(self):
        original, _, _ = self.interpreted_trial(reply=ProviderReply("{}", "length"))
        for state, reason, remove_method in (
            ("input_problem", "no_retained_source_text", False),
            ("input_problem", "no_retained_source_text", True),
            ("provider_problem", "output_truncated", True),
            ("contract_problem", "invalid_structured_output", True),
        ):
            packet = json.loads(json.dumps(original))
            result = packet["interpretation"]
            result["state"] = state
            result["problem"] = {"stage": state, "reason": reason}
            if remove_method:
                result["method"] = None
            packet["packet_sha256"] = packet_hash(
                {k: v for k, v in packet.items() if k != "packet_sha256"}
            )
            with (
                self.subTest(state=state, remove_method=remove_method),
                self.assertRaises(ValueError),
            ):
                decode_saved_trial(json.dumps(packet))

    def test_saved_window_cannot_be_relabelled_as_a_different_interval(self):
        original, _, _ = self.interpreted_trial()
        packet = json.loads(json.dumps(original))
        packet["context"]["dependency"]["proposed_version"] = "3.0"
        result = packet["interpretation"]
        result["source_input"]["interval"]["proposed_version"] = "3.0"
        result["method"] = {
            **prepare_request(result["source_input"]).method,
            "provider": result["method"]["provider"],
        }
        packet["packet_sha256"] = packet_hash(
            {k: v for k, v in packet.items() if k != "packet_sha256"}
        )
        with self.assertRaisesRegex(ValueError, "source relationships"):
            decode_saved_trial(json.dumps(packet))

    def test_retained_real_httpx_window_recovers_exact_quote_with_controlled_proposal(
        self,
    ):
        # Historical ordinary acquisition + fresh interpretation mechanics.
        # This test neither reacquires the PR nor measures live-model meaning.
        path = (
            Path(__file__).resolve().parents[2]
            / "working-memory/evidence/2026-10-04-ordered-scoped-bindings/live-pr-context.json"
        )
        context = json.loads(path.read_text())
        interval = dependency_interval(context["dependency"])
        source_input = source_input_from_projection(context["upstream"], interval)
        provider = Mock(
            identity={
                "kind": "controlled_historical_source",
                "semantic_acceptance": False,
            }
        )
        provider.complete.return_value = ProviderReply(
            json.dumps(
                {
                    "observations": [
                        {
                            "kind": "removal",
                            "subject": "proxies argument",
                            "summary": "The deprecated proxies argument was removed.",
                            "assertion": "affirmed",
                            "timing": "current",
                            "effective_version": "0.28.0",
                            "source_spans": [
                                {"start_line_id": "S2:L18", "end_line_id": "S2:L18"}
                            ],
                            "reason": None,
                        }
                    ],
                    "unassessed": [],
                }
            )
        )
        result = interpret_projection(context["upstream"], interval, provider)
        self.assertEqual(result["state"], "observations_returned")
        self.assertEqual(sum(len(s["text"]) for s in source_input["sections"]), 1367)
        body = {
            "artifact_kind": PACKET_KIND,
            "packet_version": 1,
            "proof": "historical acquisition and controlled proposal, not fresh acquisition or semantic acceptance",
            "context": context,
            "interpretation": result,
        }
        packet = {**body, "packet_sha256": packet_hash(body)}
        recovered = decode_saved_trial(json.dumps(packet))
        citation = recovered["interpretation"]["observations"][0]["evidence"][0]
        self.assertEqual(
            citation["quote"],
            "* The deprecated `proxies` argument has now been removed.\n",
        )
        self.assertEqual(citation["reported_in_version"], "0.28.0")
        self.assertEqual(citation["source_identity"]["repository"], "encode/httpx")
        self.assertEqual(recovered["context"]["target"], context["target"])

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
        pr.get_pull_request_observation.assert_called_once_with("owner/target", 7)
        pr.get_pull_request.assert_not_called()
        self.assertIs(result.inputs.identity, result.identity)
        self.assertIs(result.inputs.description, pr.get_pull_request_observation.return_value.description)
        self.assertEqual(result.inputs.changed_files, pr.get_changed_files.return_value)
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


def staged_http_control(policy, *, noise=24):
    """Authored public HTTP responses; all normal acquisition clients stay real.

    No live network, known source path selector or callable answer enters the
    ordinary producer. Inventory/import text deliberately contains distracting files.
    """
    import base64
    from io import BytesIO
    from urllib.parse import unquote, urlsplit
    from requests import Response
    from experiments.api_adapter_exploration import AdapterSourceExplorer
    from experiments.api_ordinary_call_signature_trial import acquire_ordinary_comparison_inputs

    session = TrialPublicSession(policy=policy)
    pull = dict(number=7, title='Bump vendor', state='open', merged=False, user={'login': 'bot'},
                base={'ref': 'main', 'sha': BASE}, head={'ref': 'update', 'sha': SHA}, changed_files=2,
                body='Authored control description')
    target_paths = [f'a_noise{i:02}.py' for i in range(noise)] + ['z_case.py', 'requirements.txt']
    library_paths = [f'vendor/noise{i:02}.py' for i in range(noise)] + [
        'vendor/__init__.py', 'vendor/factory.py', 'vendor/payload.py']
    responses = []

    def transport(method, url, **kwargs):
        parsed = urlsplit(url)
        path = unquote(parsed.path)
        data, status = None, 200
        if parsed.hostname == 'pypi.org':
            if path == '/pypi/vendor/json':
                # A legitimate separate upstream-window gap, not source absence.
                data, status = {}, 404
            else:
                version = path.split('/')[3]
                data = dict(info={'name': 'vendor', 'version': version, 'requires_dist': [],
                                  'project_urls': {'Source': 'https://github.com/owner/vendor'}},
                            last_serial=1, urls=[])
        elif path == '/repos/owner/target/pulls/7':
            data = pull
        elif path.endswith('/pulls/7/files'):
            data = [dict(filename=name, status='modified', additions=1, deletions=1, changes=2,
                         patch='@@ -1 +1 @@\n-vendor==1.0\n+vendor==2.0' if name.endswith('.txt') else '@@ -1 +1 @@\n-pass\n+pass',
                         contents_url=f'https://api.github.com/repos/owner/target/contents/{name}?ref={SHA}')
                    for name in ('requirements.txt', 'z_case.py')]
        elif '/git/ref/tags/' in path:
            tag = path.rsplit('/', 1)[1]
            commit = BASE if tag.lstrip('v') == '1.0' else SHA
            data = {'ref': 'refs/tags/' + tag, 'object': {'type': 'commit', 'sha': commit}}
        elif '/git/commits/' in path:
            data = {'sha': path.rsplit('/', 1)[1], 'tree': {'sha': 'c' * 40}}
        elif '/git/trees/' in path:
            paths = target_paths if '/owner/target/' in path else library_paths
            data = dict(sha='c' * 40, truncated=False,
                        tree=[dict(path=p, type='blob', mode='100644') for p in paths])
        elif '/contents/' in path:
            name = path.split('/contents/', 1)[1]
            revision = kwargs.get('params', {}).get('ref')
            if name == 'requirements.txt':
                text = 'vendor==' + ('1.0' if revision == BASE else '2.0') + '\n'
            elif name == 'z_case.py':
                text = 'from vendor import FACTORY as marks\nmarks.operation(ids=[1])\n'
            elif name == 'vendor/__init__.py':
                text = ''.join(f'from .noise{i:02} import unused{i}\n' for i in range(noise))
                text += 'from .factory import FACTORY\n'
            elif name == 'vendor/factory.py':
                text = 'from .payload import Decorator\nclass Generator:\n def __getattr__(self, name):\n  return Decorator()\nFACTORY = Generator()\n'
            elif name == 'vendor/payload.py':
                text = 'class Decorator:\n def __call__(self' + (', **kwargs' if revision == BASE else '') + '):\n  pass\n'
            else:
                text = 'unused = 1\n'
            data = dict(type='file', path=name, encoding='base64', content=base64.b64encode(text.encode()).decode())
        else:
            raise AssertionError('Unexpected controlled provider endpoint: ' + path)
        response = Response()
        response.status_code = status
        response.raw = BytesIO(json.dumps(data, separators=(',', ':')).encode())
        response.url = url
        responses.append(response)
        return response

    with patch('requests.Session.request', side_effect=transport):
        result = acquire_ordinary_comparison_inputs('owner/target', 7, session=session,
                    adapters=AdapterSourceExplorer(session=session))
    return result, session


class StagedOrdinaryHTTPTests(TestCase):
    def test_direct_native_sides_survive_exploration_noise_and_omissions_reach_view(self):
        from experiments.tests.test_api_adapter_exploration import ChainTests
        from experiments.api_adapter_exploration import ExaminedPythonModule
        from experiments.api_change_source_acquisition import TrialAcquisitionPolicy
        from experiments.api_ordinary_call_signature_trial import (
            prepare_ordinary_inputs, encode_ordinary_inputs, prepare_ordinary_comparison,
            read_ordinary_comparison, render_ordinary_comparison)
        from experiments.api_signature_evidence import AnalysisLimits
        text = 'import vendor\nvendor.send()\n' + ''.join(
            f'import bridge.noise{i} as b{i}\nb{i}.Client()\n' for i in range(20))
        legacy, _, _ = PublicPRTests().run_trial(source_explorer=ChainTests().explorer(), python_source=text)
        self.assertTrue(all(a.outcome.reason == 'module_source_limit' for a in legacy.changed_sources))
        session = TrialPublicSession(policy=TrialAcquisitionPolicy())
        explorer = ChainTests().explorer()
        explorer.session = session
        result, _, _ = PublicPRTests().run_trial(source_explorer=explorer, python_source=text, session=session)
        self.assertTrue(all(isinstance(a.outcome, ExaminedPythonModule) for a in result.changed_sources))
        self.assertEqual(len(result.adapters.omitted_candidates), 18)
        self.assertEqual(result.source_work.module_attempts, 4)
        captured = prepare_ordinary_inputs(result, session, explorer._source_run)
        data = encode_ordinary_inputs(*captured, proof_class='controlled_ordinary_pr_composition')
        encoded, companion = prepare_ordinary_comparison(data, AnalysisLimits())
        body, _ = read_ordinary_comparison(encoded, companion)
        view = render_ordinary_comparison(body)
        self.assertIn('Adapter candidate unexamined: bridge bridge.noise', view)
        self.assertIn('Adapter source unavailable:', view)

    def test_real_clients_prioritize_and_retain_protocol_paths_under_same_module_ceiling(self):
        from experiments.api_change_source_acquisition import TrialAcquisitionPolicy
        from experiments.api_ordinary_call_signature_trial import (
            encode_ordinary_inputs, run_ordinary_comparison, open_ordinary_comparison, render_ordinary_comparison)
        from experiments.api_signature_evidence import AnalysisLimits
        result, session = staged_http_control(TrialAcquisitionPolicy())
        self.assertIsInstance(result, tuple, result)
        catalog, modules, acquisition = result
        data = encode_ordinary_inputs(catalog, modules, acquisition, proof_class='controlled_ordinary_pr_composition')
        with TemporaryDirectory() as tmp:
            directory = Path(tmp) / 'staged'
            attempt = run_ordinary_comparison(data, directory)
            self.assertEqual(attempt['state'], 'completed', attempt)
            with patch('ast.parse', side_effect=AssertionError('AST forbidden')), \
                 patch('requests.Session.request', side_effect=AssertionError('network forbidden')), \
                 patch('experiments.api_call_signature.compare_arguments', side_effect=AssertionError('checker forbidden')):
                body, _ = open_ordinary_comparison(directory)
        outcomes = {c['callee_role']['role']: p['comparison']['outcome']
                    for c, p in zip(body['discovery']['candidates'], body['pairs'])}
        self.assertEqual(outcomes, {'native_old_version': 'bound', 'native_proposed_version': 'rejected'})
        self.assertEqual(acquisition['source_work']['module_attempts'], 12)
        target_reads = [r['path'] for r in session.receipts if r['stage'] == 'target_context' and '/contents/' in r['path']]
        self.assertEqual(target_reads[:2], ['/repos/owner/target/contents/requirements.txt', '/repos/owner/target/contents/z_case.py'])
        self.assertEqual(len(target_reads), 16)
        self.assertEqual(sum(r['path'] == '/repos/owner/target/pulls/7' for r in session.receipts), 2)
        self.assertLessEqual(session.github_requests, 50)
        self.assertTrue(any(g['reason'] == 'module_source_limit' for g in acquisition['internal_module_requests'] if g['state'] != 'module_examined'))
        view = render_ordinary_comparison(body)
        self.assertIn('local policy, independent of GitHub account quota', view)
        self.assertIn('Target source unexamined:', view)
        self.assertIn('module_source_limit', view)
        self.assertNotEqual(acquisition['ordinary_acquisition']['upstream']['state'], 'complete')

    def test_actual_stage_refusal_preserves_target_gap_and_later_source_work(self):
        from experiments.api_change_source_acquisition import TrialAcquisitionPolicy
        from experiments.api_ordinary_call_signature_trial import (
            encode_ordinary_inputs, prepare_ordinary_comparison, read_ordinary_comparison, render_ordinary_comparison)
        from experiments.api_signature_evidence import AnalysisLimits
        result, session = staged_http_control(TrialAcquisitionPolicy(github_requests=30, source_request_reserve=20))
        self.assertIsInstance(result, tuple, result)
        encoded, companion = prepare_ordinary_comparison(
            encode_ordinary_inputs(*result, proof_class='controlled_ordinary_pr_composition'), AnalysisLimits())
        body, _ = read_ordinary_comparison(encoded, companion)
        self.assertTrue(body['pairs'])
        self.assertEqual(session.github_requests, 30)
        view = render_ordinary_comparison(body)
        self.assertIn('trial_stage_request_limit', view)
        self.assertIn('Target acquisition gap:', view)

    def test_legacy_target_scan_can_starve_where_staged_policy_preserves_source(self):
        from experiments.api_change_source_acquisition import TrialAcquisitionPolicy
        legacy, legacy_session = staged_http_control(None, noise=60)
        staged, session = staged_http_control(TrialAcquisitionPolicy(), noise=60)
        self.assertTrue(legacy_session.request_limit_reached)
        self.assertIsInstance(staged, tuple, staged)
        self.assertFalse(session.request_limit_reached)
        self.assertTrue(any(m.path == 'vendor/payload.py' for m in staged[1]))

    def test_saved_transport_accounting_tampering_refuses(self):
        from experiments.api_change_source_acquisition import TrialAcquisitionPolicy
        from experiments.api_ordinary_call_signature_trial import (
            encode_ordinary_inputs, prepare_ordinary_comparison, read_ordinary_comparison)
        from experiments.api_signature_evidence import AnalysisLimits
        result, _ = staged_http_control(TrialAcquisitionPolicy())
        data = encode_ordinary_inputs(*result, proof_class='controlled_ordinary_pr_composition')
        encoded, companion = prepare_ordinary_comparison(data, AnalysisLimits())
        body = json.loads(encoded)
        body['acquisition']['ordinary_acquisition']['transport']['decoded_body_bytes'] += 1
        with self.assertRaisesRegex(ValueError, 'accounting mismatch'):
            read_ordinary_comparison(json.dumps(body).encode(), companion)
