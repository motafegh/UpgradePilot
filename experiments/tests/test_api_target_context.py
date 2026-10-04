"""Protect inventory correspondence, static binding limits and conditional records."""

from unittest import TestCase
from unittest.mock import Mock

from experiments.api_change_source_acquisition import AcquisitionProblem
from experiments.api_target_context import (
    InventoryEntry,
    TargetContextAcquirer,
    TargetInventory,
    TrialRepositoryInventoryClient,
    extract_dependency_declarations,
    extract_python_facts,
)
from upgradepilot.github.repository import RepositoryTextFile, UnavailableRepositoryFile

SHA = "a" * 40
TREE = "b" * 40


def file(path, content):
    return RepositoryTextFile("owner/target", path, SHA, content)


class InventoryTests(TestCase):
    def test_exact_commit_tree_and_truncation_preserved(self):
        client = TrialRepositoryInventoryClient(session=Mock())
        client._get_json_object = Mock(
            side_effect=[
                {"sha": SHA, "tree": {"sha": TREE}},
                {
                    "sha": TREE,
                    "truncated": True,
                    "tree": [{"path": "x.py", "type": "blob", "mode": "100644"}],
                },
            ]
        )
        result = client.acquire("owner/target", SHA)
        self.assertIsInstance(result, TargetInventory)
        self.assertTrue(result.truncated)
        self.assertEqual(result.entries[0].path, "x.py")

    def test_mismatch_duplicate_malformed_path_and_missing_truncation_rejected(self):
        trees = [
            {"sha": "c" * 40, "tree": [], "truncated": False},
            {"sha": TREE, "tree": []},
            {
                "sha": TREE,
                "truncated": False,
                "tree": [{"path": "../x.py", "type": "blob", "mode": "100644"}],
            },
            {
                "sha": TREE,
                "truncated": False,
                "tree": [{"path": "x.py", "type": "blob", "mode": "100644"}] * 2,
            },
        ]
        for tree in trees:
            with self.subTest(tree=tree):
                client = TrialRepositoryInventoryClient(session=Mock())
                client._get_json_object = Mock(
                    side_effect=[{"sha": SHA, "tree": {"sha": TREE}}, tree]
                )
                self.assertIsInstance(
                    client.acquire("owner/target", SHA), AcquisitionProblem
                )

    def test_streamed_inventory_body_has_a_bound_before_json_parse(self):
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.iter_content.return_value = [b"x" * (8 * 1024 * 1024 + 1)]
        session.get.return_value = response
        result = TrialRepositoryInventoryClient(session=session).acquire(
            "owner/target", SHA
        )
        self.assertIsInstance(result, AcquisitionProblem)
        self.assertIn("8 MiB", result.detail)
        self.assertTrue(session.get.call_args.kwargs["stream"])
        response.close.assert_called_once()

    def test_streamed_complete_response_preserves_inventory_identity(self):
        import json

        session = Mock()
        responses = []
        for data in (
            {"sha": SHA, "tree": {"sha": TREE}},
            {
                "sha": TREE,
                "truncated": False,
                "tree": [{"path": "x.py", "type": "blob", "mode": "100644"}],
            },
        ):
            response = Mock()
            response.status_code = 200
            response.iter_content.return_value = [json.dumps(data).encode()]
            responses.append(response)
        session.get.side_effect = responses
        result = TrialRepositoryInventoryClient(session=session).acquire(
            "owner/target", SHA
        )
        self.assertIsInstance(result, TargetInventory)
        self.assertEqual(result.entries[0].path, "x.py")
        for response in responses:
            response.close.assert_called_once()


class SyntaxTests(TestCase):
    def test_import_alias_direct_call_and_class_base(self):
        imports, refs, gaps = extract_python_facts(
            file(
                "x.py",
                "import vendor.client as vc\nfrom framework.testing import Client as C\nx=C(app, mode=True)\nclass Adapted(vc.Base):\n pass\n",
            )
        )
        self.assertFalse(gaps)
        self.assertEqual(len(imports), 2)
        self.assertEqual(refs[0].lexical_import, "framework.testing.Client")
        self.assertEqual(refs[0].keyword_names, ("mode",))
        self.assertEqual(refs[0].positional_count, 1)
        self.assertEqual(refs[1].lexical_import, "vendor.client.Base")

    def test_unknown_conditional_and_unsupported_bindings_remain_limited(self):
        cases = [
            "from vendor import Client\nClient = custom\nClient()\n",
            "from vendor import Client\ndef f(Client):\n return Client()\n",
            "if condition:\n from vendor import Client\nClient()\n",
            "try:\n import vendor2 as vendor\nexcept ImportError:\n import vendor\nclass Client(vendor.Client):\n pass\n",
            'from vendor import Client\nmatch value:\n case {"x": x, **Client}:\n  pass\nClient()\n',
            "from vendor import Client\nfrom other import *\nClient()\n",
        ]
        for source in cases:
            with self.subTest(source=source):
                imports, refs, gaps = extract_python_facts(file("x.py", source))
                self.assertTrue(imports)
                self.assertFalse(gaps)
                self.assertIsNone(refs[0].lexical_import)
                self.assertTrue(refs[0].binding_limit)
                self.assertNotEqual(refs[0].binding.state, "established")

    def test_relative_import_and_syntax_failure_are_not_external_evidence(self):
        imports, _, _ = extract_python_facts(
            file("x.py", "from .client import Client\nClient()")
        )
        self.assertEqual(imports[0].relative_level, 1)
        _, _, gaps = extract_python_facts(file("x.py", "def nope("))
        self.assertEqual(gaps[0].reason, "python_parse_failed")


class DeclarationTests(TestCase):
    def test_requirement_constraints_extras_and_marker_retained(self):
        records, gaps = extract_dependency_declarations(
            file(
                "requirements-dev.txt",
                'Vendor[fast]>=1,<3; python_version < "3.12"\n-r requirements-more.txt\n',
            )
        )
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].package, "vendor")
        self.assertEqual(records[0].extras, ("fast",))
        self.assertEqual(records[0].marker, 'python_version < "3.12"')
        self.assertIn(">=1", records[0].specifier)
        self.assertTrue(gaps)

    def test_optional_group_is_preserved_not_activated(self):
        text = '[project]\ndependencies=["Framework[standard]"]\n[project.optional-dependencies]\ntest=["vendor==2; python_version < \'3.12\'"]\n'
        records, gaps = extract_dependency_declarations(file("pyproject.toml", text))
        self.assertFalse(gaps)
        self.assertEqual(records[0].extras, ("standard",))
        self.assertEqual(records[1].group, "optional:test")
        self.assertIsNotNone(records[1].marker)

    def test_dynamic_invalid_and_direct_url_forms_keep_gaps(self):
        for path, text in [
            ("requirements.txt", "demo @ https://token@example.org/demo.whl"),
            ("setup.cfg", "[options]\ninstall_requires=demo"),
            ("pyproject.toml", "[project]\ndependencies=3"),
            ("pyproject.toml", "[bad"),
        ]:
            with self.subTest(path=path):
                records, gaps = extract_dependency_declarations(file(path, text))
                self.assertFalse(records)
                self.assertTrue(gaps)


class AcquisitionTests(TestCase):
    def runner(self, entries, contents, truncated=False):
        inventory = Mock()
        inventory.acquire.return_value = TargetInventory(
            "owner/target", SHA, TREE, tuple(entries), truncated
        )
        files = Mock()
        files.get_exact_commit_text_file.side_effect = lambda repo, sha, path: contents[
            path
        ]
        return TargetContextAcquirer(inventory=inventory, files=files)

    def test_inventory_drives_paths_candidates_and_no_ci_dependency(self):
        entries = [
            InventoryEntry("arbitrary.py", "blob", "100644"),
            InventoryEntry("requirements.txt", "blob", "100644"),
            InventoryEntry(".venv/x.py", "blob", "100644"),
        ]
        runner = self.runner(
            entries,
            {
                "arbitrary.py": file(
                    "arbitrary.py",
                    "from framework.testing import Client as C\nC(app)\n",
                ),
                "requirements.txt": file(
                    "requirements.txt", "framework[standard]\nvendor==2\n"
                ),
            },
        )
        result = runner.acquire("owner/target", SHA)
        self.assertEqual(len(result.files), 2)
        self.assertEqual(result.candidates[0].imported_module, "framework.testing")
        self.assertEqual(result.excluded_paths, (".venv/x.py",))
        self.assertIn("constraints_not_resolved_versions", result.limitations)

    def test_truncation_read_failure_and_budget_omissions_visible(self):
        entries = [
            InventoryEntry("a.py", "blob", "100644"),
            InventoryEntry("b.py", "blob", "100644"),
            InventoryEntry("requirements.txt", "blob", "100644"),
        ]
        runner = self.runner(
            entries,
            {
                "a.py": file("a.py", "import demo"),
                "b.py": file("b.py", "import another"),
                "requirements.txt": UnavailableRepositoryFile(
                    "owner/target",
                    "requirements.txt",
                    SHA,
                    "not_found_or_inaccessible",
                    "missing",
                ),
            },
            True,
        )
        result = runner.acquire("owner/target", SHA, max_python_files=1)
        self.assertEqual(result.omitted_paths, ("b.py",))
        self.assertEqual(
            {g.reason for g in result.gaps},
            {
                "inventory_truncated",
                "input_budget_exhausted",
                "not_found_or_inaccessible",
            },
        )

    def test_later_file_exceptions_preserve_acquired_target_facts(self):
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
                runner = self.runner(
                    [
                        InventoryEntry("a.py", "blob", "100644"),
                        InventoryEntry("b.py", "blob", "100644"),
                    ],
                    {},
                )
                runner.files.get_exact_commit_text_file.side_effect = [
                    file("a.py", "import vendor"),
                    error,
                ]
                result = runner.acquire("owner/target", SHA)
                self.assertEqual([f.path for f in result.files], ["a.py"])
                self.assertEqual(result.imports[0].module, "vendor")
                self.assertEqual(
                    (result.gaps[0].path, result.gaps[0].reason), ("b.py", reason)
                )

    def test_local_namespace_does_not_become_distribution_candidate(self):
        entries = [
            InventoryEntry("framework.py", "blob", "100644"),
            InventoryEntry("requirements.txt", "blob", "100644"),
        ]
        runner = self.runner(
            entries,
            {
                "framework.py": file("framework.py", "import framework"),
                "requirements.txt": file("requirements.txt", "framework"),
            },
        )
        result = runner.acquire("owner/target", SHA)
        self.assertFalse(result.candidates)
        self.assertEqual(result.gaps[0].reason, "local_namespace_collision")
