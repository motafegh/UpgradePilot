"""Synthetic independent adapter-chain, sample/constraint and identity controls."""

import json
from datetime import UTC, datetime
from unittest import TestCase
from unittest.mock import Mock

from experiments.api_adapter_context_replay import decode_adapter_seed
from experiments.api_adapter_exploration import (
    AdapterSourceExplorer,
    ExaminedPythonModule,
    PythonModuleSourceRequest,
    PackageDependencyMetadata,
    TrialDependencyMetadataClient,
    select_exploration_version,
)
from experiments.api_change_source_acquisition import (
    AcquisitionProblem,
    PublisherProvenanceInspection,
    TrialPublicSession,
)
from experiments.api_target_context import (
    DependencyDeclaration,
    ImportDependencyCandidate,
    InventoryEntry,
    TargetContext,
    TargetContextAcquirer,
    TargetInventory,
    extract_python_facts,
)
from experiments.api_target_context_smoke import context_manifest
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.tag import GitHubTagCommitEvidence
from upgradepilot.pypi.release import (
    PackageReleaseEvidence,
    PackageReleaseIndexEvidence,
    ProjectUrlCandidate,
)

SHA = "a" * 40
NOW = datetime(2026, 10, 4, tzinfo=UTC)


def declaration(package, source="requirements.txt", specifier=">=1", marker=None):
    return DependencyDeclaration(
        source,
        "L1",
        package + specifier,
        package,
        specifier,
        (),
        marker,
        "requirements",
    )


def index(package, versions=("1.0", "2.0")):
    return PackageReleaseIndexEvidence(
        package,
        package,
        package,
        "https://pypi.org/pypi/" + package + "/json",
        NOW,
        1,
        versions,
    )


class SamplingTests(TestCase):
    def test_latest_stable_constraint_is_sampling_not_resolved_version(self):
        result = select_exploration_version(
            index("bridge", ("1.0", "1.5", "2.0rc1", "2.0")),
            declaration("bridge", specifier="<2"),
        )
        self.assertEqual(result, "1.5")
        result = select_exploration_version(
            index("bridge", ("2", "2.0")), declaration("bridge")
        )
        self.assertIsInstance(result, AcquisitionProblem)


class MetadataTests(TestCase):
    def client(self, info):
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.headers = {}
        response.iter_content.return_value = [json.dumps({"info": info}).encode()]
        session.get.return_value = response
        return TrialDependencyMetadataClient(session=session)

    def test_conditions_and_extra_markers_remain_unresolved_declarations(self):
        result = self.client(
            {
                "name": "bridge",
                "version": "2.0",
                "requires_dist": [
                    'mediator>=2; python_version < "3.12"',
                    'vendor[fast]; extra == "standard"',
                ],
            }
        ).acquire("bridge", "2.0")
        self.assertEqual(result.requirements[0].marker, 'python_version < "3.12"')
        self.assertEqual(result.requirements[1].extras, ("fast",))
        self.assertEqual(result.requirements[1].marker, 'extra == "standard"')

    def test_wrong_identity_bad_array_and_direct_url_do_not_become_relations(self):
        cases = [
            {"name": "another", "version": "2.0", "requires_dist": []},
            {"name": "bridge", "version": "2.0", "requires_dist": "vendor"},
        ]
        for info in cases:
            self.assertIsInstance(
                self.client(info).acquire("bridge", "2.0"), AcquisitionProblem
            )
        result = self.client(
            {
                "name": "bridge",
                "version": "2.0",
                "requires_dist": ["vendor @ https://token@example.org/file.whl"],
            }
        ).acquire("bridge", "2.0")
        self.assertFalse(result.requirements)
        self.assertEqual(result.gaps[0].reason, "direct_url_not_followed")


class ChainTests(TestCase):
    def acquired_seed(self, source):
        """Normal target acquisition/serialization, controlled file providers only."""
        inventory = Mock()
        inventory.acquire.return_value = TargetInventory(
            "owner/target",
            SHA,
            "b" * 40,
            (
                InventoryEntry("unusual_test.py", "blob", "100644"),
                InventoryEntry("requirements.txt", "blob", "100644"),
            ),
            False,
        )
        files = Mock()
        files.get_exact_commit_text_file.side_effect = lambda repo, sha, path: (
            RepositoryTextFile(
                repo, path, sha, source if path.endswith(".py") else "bridge>=1\n"
            )
        )
        context = TargetContextAcquirer(inventory=inventory, files=files).acquire(
            "owner/target", SHA
        )
        packet = {
            "state": "context_acquired",
            "identity": {"repository": "owner/target", "head_sha": SHA},
            "target": context_manifest(context),
        }
        return decode_adapter_seed(json.loads(json.dumps(packet)))

    def test_restored_alias_reaches_adapter_chain_through_acquisition_and_replay(self):
        seed = self.acquired_seed(
            "from bridge.testing import Client as C\nS=C\nC=None\nC(app)\nC=S\nC(app)\n"
        )
        self.assertEqual(
            [r.lexical_import for r in seed.references], [None, "bridge.testing.Client"]
        )
        result = self.explorer().explore(seed)
        self.assertEqual(
            [s.candidate.declaration.package for s in result.samples],
            ["bridge", "mediator", "vendor"],
        )

    def test_conditional_possible_origin_does_not_trigger_positive_exploration(self):
        for source in (
            "if flag:\n from bridge.testing import Client as C\nelse:\n from other import Client as C\nC(app)\n",
            "from bridge.testing import Client as C\ndef f():\n return C(app)\n",
        ):
            with self.subTest(source=source):
                seed = self.acquired_seed(source)
                self.assertTrue(seed.candidates)
                self.assertIsNone(seed.references[0].lexical_import)
                self.assertIn(
                    "bridge.testing.Client", seed.references[0].binding.possible_imports
                )
                explorer = self.explorer()
                self.assertFalse(explorer.explore(seed).samples)
                explorer.index.get_release_index.assert_not_called()

    def test_agreeing_branches_reach_chain_without_selecting_branch_truth(self):
        seed = self.acquired_seed(
            "if flag:\n from bridge.testing import Client as C\nelse:\n from bridge.testing import Client as C\nC(app)\n"
        )
        self.assertEqual(
            [
                s.line
                for s in seed.references[0].binding.trace
                if s.operation == "import"
            ],
            [2, 4],
        )
        self.assertEqual(len(self.explorer().explore(seed).samples), 3)

    def context(self):
        file = RepositoryTextFile(
            "owner/target",
            "unusual_test.py",
            SHA,
            "from bridge.testing import Client as C\nC(app)\n",
        )
        imports, refs, _ = extract_python_facts(file)
        candidate = ImportDependencyCandidate(
            "bridge.testing", declaration("bridge"), imports[0].source_id, 1
        )
        inventory = TargetInventory("owner/target", SHA, "b" * 40, (), False)
        return TargetContext(
            inventory,
            (file,),
            imports,
            refs,
            (candidate.declaration,),
            (candidate,),
            (),
            (),
            (),
            len(file.content),
        )

    def explorer(self):
        indices = Mock()
        indices.get_release_index.side_effect = lambda package: index(package)
        releases = Mock()
        releases.get_release.side_effect = lambda package, version: (
            PackageReleaseEvidence(
                package,
                package,
                version,
                package,
                version,
                "https://pypi.org/pypi/" + package + "/" + version + "/json",
                NOW,
                1,
                (),
                (ProjectUrlCandidate("Source", "https://github.com/owner/" + package),),
            )
        )
        provenance = Mock()
        provenance.resolve.side_effect = lambda release: PublisherProvenanceInspection(
            "source_unavailable", "absent"
        )
        metadata = Mock()
        metadata.acquire.side_effect = lambda package, version: (
            PackageDependencyMetadata(
                package,
                version,
                "https://pypi.org/pypi/" + package + "/" + version + "/json",
                tuple(
                    [
                        declaration(
                            "mediator",
                            specifier=">=2",
                            marker='python_version < "3.12"',
                        )
                    ]
                    if package == "bridge"
                    else [declaration("vendor")]
                    if package == "mediator"
                    else []
                ),
                (),
            )
        )
        tags = Mock()
        tags.resolve_tag_to_commit.side_effect = lambda repo, tag: (
            GitHubTagCommitEvidence(
                repo, tag, "refs/tags/" + tag, "commit", SHA, SHA, (), NOW
            )
        )
        inventory = Mock()
        inventory.acquire.side_effect = lambda repo, sha: TargetInventory(
            repo,
            sha,
            "b" * 40,
            (
                InventoryEntry(repo.split("/")[1] + "/testing.py", "blob", "100644"),
                InventoryEntry(repo.split("/")[1] + "/__init__.py", "blob", "100644"),
            ),
            False,
        )
        files = Mock()
        files.get_exact_commit_text_file.side_effect = lambda repo, sha, path: (
            RepositoryTextFile(
                repo,
                path,
                sha,
                "from mediator.testing import Client\n"
                if repo == "owner/bridge"
                else "import vendor\nclass Client(vendor.Base):\n pass\n"
                if repo == "owner/mediator"
                else "",
            )
        )
        return AdapterSourceExplorer(
            index=indices,
            releases=releases,
            provenance=provenance,
            metadata=metadata,
            tags=tags,
            inventory=inventory,
            files=files,
        )

    def test_normal_chain_follows_acquired_imports_and_exact_metadata(self):
        result = self.explorer().explore(self.context())
        self.assertEqual(
            [s.candidate.declaration.package for s in result.samples],
            ["bridge", "mediator", "vendor"],
        )
        self.assertEqual([s.depth for s in result.samples], [0, 1, 2])
        self.assertIn(
            "exploration_samples_not_resolved_target_versions", result.limitations
        )
        self.assertEqual(
            result.samples[1].candidate.declaration.marker, 'python_version < "3.12"'
        )
        self.assertEqual(result.samples[1].references[0].lexical_import, "vendor.Base")

    def test_budgets_keep_unexamined_candidates_and_do_not_claim_coverage(self):
        result = self.explorer().explore(self.context(), max_hops=1)
        self.assertEqual(len(result.samples), 2)
        self.assertEqual(result.omitted_candidates[0].declaration.package, "vendor")
        result = self.explorer().explore(self.context(), max_samples=1)
        self.assertEqual(len(result.samples), 1)
        self.assertTrue(result.omitted_candidates)

    def test_missing_module_and_provenance_conflict_remain_problems(self):
        explorer = self.explorer()
        explorer.inventory.acquire.side_effect = lambda repo, sha: TargetInventory(
            repo, sha, "b" * 40, (), False
        )
        result = explorer.explore(self.context())
        self.assertEqual(result.problems[0].reason, "module_path_not_established")
        explorer = self.explorer()
        explorer.provenance.resolve.side_effect = lambda release: (
            PublisherProvenanceInspection("identity_mismatch", "conflict")
        )
        result = explorer.explore(self.context())
        self.assertEqual(result.problems[0].reason, "identity_mismatch")
        explorer.files.get_exact_commit_text_file.assert_not_called()

    def test_same_release_modules_share_registry_tag_tree_budget(self):
        from dataclasses import replace

        context = self.context()
        extra = replace(context.candidates[0], imported_module="bridge")
        reference = replace(context.references[0], lexical_import="bridge.Application")
        context = replace(
            context,
            candidates=context.candidates + (extra,),
            references=context.references + (reference,),
        )
        explorer = self.explorer()
        result = explorer.explore(context, max_samples=1, max_hops=0)
        self.assertEqual(len(result.samples), 2)
        self.assertEqual({s.version for s in result.samples}, {"2.0"})
        explorer.releases.get_release.assert_called_once_with("bridge", "2.0")
        self.assertEqual(explorer.tags.resolve_tag_to_commit.call_count, 2)
        self.assertEqual(explorer.inventory.acquire.call_count, 1)

    def test_later_adapter_exception_keeps_earlier_samples_and_limit_omissions(self):
        from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError

        for error, reason in [
            (
                GitHubAcquisitionError("limit reached", reason="trial_request_limit"),
                "trial_request_limit",
            ),
            (
                GitHubAcquisitionError("network failed", reason="transport_error"),
                "transport_error",
            ),
            (GitHubResponseError("invalid response"), "malformed_response"),
        ]:
            with self.subTest(reason=reason):
                explorer = self.explorer()
                original = explorer.files.get_exact_commit_text_file.side_effect

                def read(repo, sha, path, error=error, original=original):
                    if repo == "owner/mediator":
                        raise error
                    return original(repo, sha, path)

                explorer.files.get_exact_commit_text_file.side_effect = read
                result = explorer.explore(self.context())
                self.assertEqual(
                    [s.candidate.declaration.package for s in result.samples],
                    ["bridge"],
                )
                self.assertEqual(result.problems[0].reason, reason)
                if reason == "trial_request_limit":
                    self.assertEqual(
                        result.omitted_candidates[0].declaration.package, "mediator"
                    )

    def test_provider_wrapped_limit_still_stops_remaining_adapter_reads(self):
        explorer = self.explorer()
        explorer.session.request_limit_reached = True
        explorer._acquire = Mock(
            return_value=AcquisitionProblem(
                "adapter_tag", "acquisition_failed", "wrapped provider failure"
            )
        )
        result = explorer.explore(self.context())
        self.assertEqual(result.problems[0].reason, "trial_request_limit")
        self.assertEqual(result.omitted_candidates[0].declaration.package, "bridge")


class SourceRunTests(TestCase):
    """Exact and conditional questions share source work, never binding authority."""

    def question(self, module="bridge.testing", version="2.0", basis="native_proposed_version", origin=None):
        return PythonModuleSourceRequest("bridge", version, module, basis, origin)

    def budget_profile(self, precharged_target_requests):
        """Controlled request-charge model, not live endpoint/protocol timing proof.

        Direct tags cost one GET, inventory commit/tree two, module one. Typed
        provider controls still return the source records used by real owners.
        """
        from unittest.mock import patch

        controls = ChainTests()
        explorer = controls.explorer()
        session = TrialPublicSession()
        explorer.session = session
        trace = []

        def charge(host, label, count=1):
            for index in range(count):
                before = session.github_requests
                try:
                    session.request("GET", f"https://{host}/{label}/{index}")
                    trace.append({"stage": label, "host": host, "github_before": before,
                                  "github_after": session.github_requests, "state": "charged"})
                except Exception:
                    trace.append({"stage": label, "host": host, "github_before": before,
                                  "github_after": session.github_requests, "state": "refused"})
                    raise

        for method, host, label, count in (
            (explorer.tags.resolve_tag_to_commit, "api.github.com", "tag", 1),
            (explorer.inventory.acquire, "api.github.com", "commit_and_tree", 2),
            (explorer.files.get_exact_commit_text_file, "api.github.com", "module", 1),
            (explorer.index.get_release_index, "pypi.org", "index", 1),
            (explorer.releases.get_release, "pypi.org", "release", 1),
            (explorer.metadata.acquire, "pypi.org", "metadata", 1),
        ):
            original = method.side_effect
            def call(*args, original=original, host=host, label=label, count=count):
                charge(host, label, count)
                return original(*args)
            method.side_effect = call

        # Replace the lowest HTTP transport: no target/provider network is used.
        with patch("requests.sessions.Session.request", return_value=Mock()):
            charge("api.github.com", "pr_and_target", precharged_target_requests)
            run = explorer.source_run()
            samples = explorer.explore(controls.context(), source_run=run)
            discovered = samples.samples[-1].candidate
            old = run.examine(PythonModuleSourceRequest(discovered.declaration.package, "1.0",
                discovered.imported_module, "native_old_version"))
            proposed = run.examine(PythonModuleSourceRequest(discovered.declaration.package, "2.0",
                discovered.imported_module, "native_proposed_version"))
        return {
            "proof": "controlled provider request-charge allocation model; not live acquisition",
            "precharged_pr_target_requests": precharged_target_requests,
            "github_requests": session.github_requests,
            "request_limit_reached": session.request_limit_reached,
            "samples": len(samples.samples),
            "old_source": old.reason if isinstance(old, AcquisitionProblem) else "module_examined",
            "proposed_source": proposed.reason if isinstance(proposed, AcquisitionProblem) else "module_examined",
            "trace": trace,
        }

    def test_controlled_request_allocation_distinguishes_fitting_and_starved_sources(self):
        fitting = self.budget_profile(30)
        self.assertEqual(fitting["github_requests"], 50)
        self.assertFalse(fitting["request_limit_reached"])
        self.assertEqual(fitting["old_source"], "module_examined")
        self.assertEqual(fitting["proposed_source"], "module_examined")
        starved = self.budget_profile(31)
        self.assertEqual(starved["github_requests"], 50)
        self.assertTrue(starved["request_limit_reached"])
        self.assertEqual(starved["old_source"], "trial_request_limit")
        self.assertEqual(starved["proposed_source"], "module_examined")
        self.assertEqual(starved["samples"], 3)

    def test_exact_source_and_sample_share_work_but_keep_question_basis(self):
        controls = ChainTests()
        explorer = controls.explorer()
        run = explorer.source_run()
        exact = run.examine(self.question())
        self.assertIsInstance(exact, ExaminedPythonModule)
        explorer.index.get_release_index.assert_not_called()
        sampled = explorer.explore(controls.context(), max_hops=0, source_run=run)
        self.assertEqual(len(sampled.samples), 1)
        self.assertEqual(sampled.samples[0].version, "2.0")
        self.assertIn("exploration_samples_not_resolved_target_versions", sampled.limitations)
        self.assertEqual(exact.request.version_basis, "native_proposed_version")
        self.assertIs(sampled.samples[0].file, exact.file)
        self.assertEqual(run.module_attempts, 1)
        explorer.explore(controls.context(), max_hops=0, source_run=run)
        explorer.index.get_release_index.assert_called_once_with("bridge")
        explorer.releases.get_release.assert_called_once_with("bridge", "2.0")
        self.assertEqual(explorer.tags.resolve_tag_to_commit.call_count, 2)
        explorer.inventory.acquire.assert_called_once()
        explorer.files.get_exact_commit_text_file.assert_called_once()

    def test_native_deferral_does_not_bypass_external_hop_limit(self):
        controls = ChainTests()
        explorer = controls.explorer()
        result = explorer.explore(controls.context(), max_hops=1, stop_at_package="vendor")
        self.assertFalse(result.deferred_candidates)
        self.assertEqual(result.omitted_candidates[0].declaration.package, "vendor")
        self.assertEqual(len(result.samples), 2)

    def test_old_new_and_multiple_modules_have_separate_identity_with_shared_release_reads(self):
        explorer = ChainTests().explorer()
        run = explorer.source_run()
        old = run.examine(self.question(version="1.0", basis="native_old_version"))
        root = run.examine(self.question("bridge", version="1.0", basis="explicit_version"))
        new = run.examine(self.question())
        again = run.examine(self.question(version="1.0", basis="explicit_version"))
        self.assertEqual(old.metadata.version, "1.0")
        self.assertEqual(new.metadata.version, "2.0")
        self.assertEqual(root.file.path, "bridge/__init__.py")
        self.assertEqual(again.request.version_basis, "explicit_version")
        self.assertEqual(old.request.version_basis, "native_old_version")
        self.assertIs(old.file, again.file)
        self.assertEqual(run.release_identities, (("bridge", "1.0"), ("bridge", "2.0")))
        self.assertEqual(explorer.releases.get_release.call_count, 2)
        self.assertEqual(explorer.inventory.acquire.call_count, 2)
        self.assertEqual(explorer.files.get_exact_commit_text_file.call_count, 3)

    def test_explicit_conditional_question_keeps_original_binding_and_positive_explorer_refuses(self):
        controls = ChainTests()
        seed = controls.acquired_seed(
            "if flag:\n from bridge.testing import Client as C\n"
            "else:\n from other import Client as C\nC(app)\n"
        )
        reference = seed.references[0]
        self.assertEqual(reference.binding.state, "conditional")
        explorer = controls.explorer()
        run = explorer.source_run()
        self.assertFalse(explorer.explore(seed, source_run=run).samples)
        explorer.index.get_release_index.assert_not_called()
        examined = run.examine(self.question(basis="native_proposed_version", origin=reference))
        self.assertIsInstance(examined, ExaminedPythonModule)
        self.assertIs(examined.request.origin, reference)
        self.assertIsNone(reference.lexical_import)
        self.assertEqual(reference.binding.state, "conditional")
        self.assertFalse(explorer.explore(seed, source_run=run).samples)
        self.assertEqual(explorer.files.get_exact_commit_text_file.call_count, 1)

    def test_release_and_module_limits_refuse_unexamined_work_without_reading(self):
        explorer = ChainTests().explorer()
        run = explorer.source_run(max_releases=1)
        self.assertIsInstance(run.examine(self.question()), ExaminedPythonModule)
        problem = run.examine(self.question(version="1.0", basis="native_old_version"))
        self.assertEqual(problem.reason, "release_source_limit")
        explorer.releases.get_release.assert_called_once()
        limited = explorer.source_run(max_module_files=1)
        first = limited.examine(self.question())
        problem = limited.examine(self.question("bridge"))
        self.assertEqual(problem.reason, "module_source_limit")
        self.assertIs(limited.examine(self.question()).file, first.file)
        self.assertEqual(limited.module_attempts, 1)

    def test_byte_limit_preserves_refusal_without_truncation_or_implicit_retry(self):
        explorer = ChainTests().explorer()
        run = explorer.source_run(max_bytes=1)
        first = run.examine(self.question())
        self.assertEqual(first.reason, "source_text_limit")
        self.assertEqual(run.source_bytes, 0)
        self.assertIs(run.examine(self.question()), first)
        explorer.files.get_exact_commit_text_file.assert_called_once()

    def test_failed_release_and_file_observations_are_cached_only_within_one_run(self):
        from upgradepilot.github.api import GitHubAcquisitionError

        explorer = ChainTests().explorer()
        explorer.provenance.resolve.side_effect = lambda release: PublisherProvenanceInspection(
            "identity_mismatch", "conflicting publisher identity",
        )
        run = explorer.source_run()
        self.assertEqual(run.examine(self.question()).reason, "identity_mismatch")
        self.assertEqual(run.examine(self.question("bridge")).reason, "identity_mismatch")
        explorer.releases.get_release.assert_called_once()
        explorer.files.get_exact_commit_text_file.assert_not_called()
        fresh = explorer.source_run()
        fresh.examine(self.question())
        self.assertEqual(explorer.releases.get_release.call_count, 2)

        explorer = ChainTests().explorer()
        error = GitHubAcquisitionError("transport failed", reason="transport_error")
        explorer.files.get_exact_commit_text_file.side_effect = error
        run = explorer.source_run()
        first = run.examine(self.question())
        self.assertIs(first.evidence, error)
        self.assertEqual(first.reason, "transport_error")
        self.assertIs(run.examine(self.question()), first)
        explorer.files.get_exact_commit_text_file.assert_called_once()

    def test_ambiguous_tag_and_incomplete_or_ambiguous_inventory_do_not_choose_source(self):
        from dataclasses import replace

        for failure in ("tags", "truncated", "paths"):
            with self.subTest(failure=failure):
                explorer = ChainTests().explorer()
                if failure == "tags":
                    original = explorer.tags.resolve_tag_to_commit.side_effect
                    explorer.tags.resolve_tag_to_commit.side_effect = lambda repo, tag: replace(
                        original(repo, tag), resolved_commit_sha=("f" * 40 if tag.startswith("v") else SHA),
                    )
                else:
                    original = explorer.inventory.acquire.side_effect
                    def inventory(repo, sha):
                        value = original(repo, sha)
                        if failure == "truncated":
                            return replace(value, truncated=True)
                        return replace(value, entries=value.entries + (
                            InventoryEntry("src/bridge/testing.py", "blob", "100644"),
                        ))
                    explorer.inventory.acquire.side_effect = inventory
                problem = explorer.source_run().examine(self.question())
                self.assertEqual(problem.reason, {
                    "tags": "tag_not_established", "truncated": "inventory_truncated",
                    "paths": "module_path_not_established",
                }[failure])
                explorer.files.get_exact_commit_text_file.assert_not_called()

    def test_provider_limit_stops_new_questions_but_cached_evidence_remains_available(self):
        explorer = ChainTests().explorer()
        run = explorer.source_run()
        first = run.examine(self.question())
        explorer.session.request_limit_reached = True
        self.assertIs(run.examine(self.question()).file, first.file)
        self.assertEqual(run.examine(self.question("bridge")).reason, "trial_request_limit")
        explorer.files.get_exact_commit_text_file.assert_called_once()

    def test_wrapped_provider_quota_failure_retains_budget_cause_and_original_problem(self):
        from upgradepilot.github.repository import UnavailableRepositoryFile

        for stage in ("metadata", "file"):
            with self.subTest(stage=stage):
                explorer = ChainTests().explorer()
                problem = AcquisitionProblem("adapter_metadata", "acquisition_failed", "wrapped quota")
                def metadata(package, version):
                    explorer.session.request_limit_reached = True
                    return problem
                def file(repo, sha, path):
                    explorer.session.request_limit_reached = True
                    return UnavailableRepositoryFile(repo, path, sha, "acquisition_failed", "wrapped quota")
                if stage == "metadata":
                    explorer.metadata.acquire.side_effect = metadata
                else:
                    explorer.files.get_exact_commit_text_file.side_effect = file
                run = explorer.source_run()
                refused = run.examine(self.question())
                self.assertEqual(refused.reason, "trial_request_limit")
                self.assertIsInstance(refused.evidence, AcquisitionProblem)
                self.assertEqual(refused.evidence.reason, "acquisition_failed")
                self.assertIs(run.examine(self.question()), refused)

    def test_invalid_source_questions_and_expanded_budgets_refuse_before_provider_calls(self):
        explorer = ChainTests().explorer()
        for module in ("", "../bridge", "bridge/testing", ".bridge"):
            with self.subTest(module=module), self.assertRaises(ValueError):
                explorer.source_run().examine(self.question(module))
        with self.assertRaises(ValueError):
            explorer.source_run().examine(self.question(origin="invented origin"))
        for bounds in ({"max_releases": 5}, {"max_module_files": 13}, {"max_bytes": 2 * 1024 * 1024 + 1}):
            with self.subTest(bounds=bounds), self.assertRaises(ValueError):
                explorer.source_run(**bounds)
        explorer.releases.get_release.assert_not_called()
