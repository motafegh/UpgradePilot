"""Synthetic independent adapter-chain, sample/constraint and identity controls."""

import json
from datetime import UTC, datetime
from unittest import TestCase
from unittest.mock import Mock

from experiments.api_adapter_exploration import (
    AdapterSourceExplorer,
    PackageDependencyMetadata,
    TrialDependencyMetadataClient,
    select_exploration_version,
)
from experiments.api_change_source_acquisition import (
    AcquisitionProblem,
    PublisherProvenanceInspection,
)
from experiments.api_target_context import (
    DependencyDeclaration,
    ImportDependencyCandidate,
    InventoryEntry,
    TargetContext,
    TargetInventory,
    extract_python_facts,
)
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
