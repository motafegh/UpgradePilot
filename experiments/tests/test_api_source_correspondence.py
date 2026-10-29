"""Discovered source-path, ordinary composition and historical-consumer contracts."""

import hashlib
import json
import subprocess
import sys
from dataclasses import replace
from datetime import UTC, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import Mock, patch

from upgradepilot.github.pull_request import (
    ChangedFile, PullRequestIdentity, PullRequestObservation, PullRequestDescriptionObservation,
)
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.native_representation import json_bytes
from upgradepilot.workspace.source_access import (
    RetainedSourceCatalog, RetainedSourceFile, RetainedSourceScope,
)

from experiments.api_call_signature_trial import AnalysisLimits
from experiments.api_change_source_acquisition import AcquisitionProblem, TrialPublicSession
from experiments.api_ordinary_call_signature_trial import (
    acquire_ordinary_comparison_inputs, encode_ordinary_inputs, open_ordinary_comparison,
    prepare_ordinary_comparison, read_ordinary_comparison, render_ordinary_comparison,
    run_ordinary_comparison,
)
from experiments.api_source_correspondence import (
    PythonSourceModule, discover_source_candidates, module_name,
)
from experiments.api_target_context import (
    InventoryEntry, TargetContextAcquirer, TargetInventory,
)

SHA = "a" * 40
TARGET = ExactInvestigationTarget("owner/target", 7, "b" * 40, SHA, "vendor", "1.0", "2.0")


def source_inputs(target, old, proposed, *, additional=()):
    """Complete locally authored captures; no callable pair/expected result input."""
    scopes, files, modules = [], [], []
    rows = [("target", "target.py", target, "target", "", "", ("vendor",)),
            ("old", "vendor/__init__.py", old, "native_old_version", "vendor", "1.0", ()),
            ("new", "vendor/__init__.py", proposed, "native_proposed_version", "vendor", "2.0", ()),
            *additional]
    for sid, path, content, role, package, version, dependencies in rows:
        if sid not in {s.source_id for s in scopes}:
            scopes.append(RetainedSourceScope(sid, "owner/target" if role == "target" else "owner/" + package,
                SHA, "repository_text", "locally authored control", "complete supplied files, not runtime"))
        files.append(RetainedSourceFile(sid, path, content))
        modules.append(PythonSourceModule(sid, path, module_name(path), package, version, role, dependencies))
    return RetainedSourceCatalog(tuple(scopes), tuple(files), target=TARGET), tuple(modules)


def prepared(*args, **kwargs):
    catalog, modules = source_inputs(*args, **kwargs)
    return encode_ordinary_inputs(catalog, modules, {"control": "locally authored retained material"},
                                  proof_class="retained_component_discovery")


class SourcePathTests(TestCase):
    def test_direct_alias_change_is_discovered_for_both_roles_without_selectors(self):
        data = prepared("from vendor import send as deliver\ndeliver(app=1)\n",
                        "def send(*, app=None):\n pass\n", "def send():\n pass\n")
        result, companion = prepare_ordinary_comparison(data, AnalysisLimits())
        body, _ = read_ordinary_comparison(result, companion)
        outcomes = {c["callee_role"]["role"]: p["comparison"]["outcome"]
                    for c, p in zip(body["discovery"]["candidates"], body["pairs"])}
        self.assertEqual(outcomes, {"native_old_version": "bound", "native_proposed_version": "rejected"})
        self.assertEqual({c["callee_role"]["role"] for c in body["discovery"]["candidates"]},
                         {"native_old_version", "native_proposed_version"})
        self.assertTrue(all("installed_namespace_and_dispatch_not_established" in c["premises"]
                            for c in body["discovery"]["candidates"]))

    def test_relative_star_reexports_and_repeated_definitions_preserve_alternatives(self):
        catalog, modules = source_inputs("from vendor import send\nsend(app=1)\n",
            "from .impl import *\n", "from .impl import send\n", additional=(
                ("old", "vendor/impl.py", "def send(*, app=None):\n pass\ndef send():\n pass\n",
                 "native_old_version", "vendor", "1.0", ()),
                ("new", "vendor/impl.py", "def send():\n pass\n", "native_proposed_version", "vendor", "2.0", ()),
            ))
        discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits())
        self.assertEqual(len(pairs), 3)
        self.assertEqual(len({p["comparison"]["signature_id"] for p in pairs}), 3)
        self.assertTrue(any("star_export_membership_not_established" in c["premises"] for c in discovery["candidates"]))
        self.assertTrue(all(any(s["operation"] == "reexport" for s in c["steps"]) for c in discovery["candidates"]))

    def test_conditional_target_origin_is_not_promoted_by_source_success(self):
        data = prepared("if enabled:\n from vendor import send\nsend(app=1)\n",
                        "def send(*, app=None):\n pass\n", "def send():\n pass\n")
        result, companion = prepare_ordinary_comparison(data, AnalysisLimits())
        body, _ = read_ordinary_comparison(result, companion)
        self.assertEqual(len(body["pairs"]), 2)
        self.assertTrue(all("conditional_import_origin" in c["premises"] for c in body["discovery"]["candidates"]))
        target = next(u for u in body["files"] if u["descriptor"]["source_id"] == "target")
        self.assertEqual(target["facts"]["calls"][0]["binding"]["state"], "conditional")

    def test_initializer_parent_path_is_target_rooted_and_skips_nested_callback(self):
        catalog, modules = source_inputs("from facade import Client\nClient(app=1)\n",
            "class Base:\n def __init__(self, *, app=None):\n  pass\n",
            "class Base:\n def __init__(self):\n  pass\n", additional=(
                ("facade", "facade/__init__.py", "import vendor\nclass Client(vendor.Base):\n"
                 " def __init__(self, *, app=None):\n  def never_called():\n   vendor.Base(app=1)\n"
                 "  ignored = lambda: vendor.Base(app=1)\n  super().__init__(app=app)\n",
                 "constraint_sample", "facade", "5.0", ("vendor",)),
            ))
        # The normal target declaration admits the facade distribution; source
        # roles/declarations, rather than arbitrary repository mixing, join it.
        modules = tuple(PythonSourceModule(m.source_id, m.path, m.module, m.package, m.version,
                         m.role, ("facade",)) if m.role == "target" else m for m in modules)
        discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits())
        self.assertEqual(len(pairs), 3)
        self.assertEqual(pairs[0]["comparison"]["outcome"], "bound")
        self.assertEqual({c["callee_role"]["role"]: p["comparison"]["outcome"]
                         for c, p in zip(discovery["candidates"][1:], pairs[1:])},
                         {"native_old_version": "bound", "native_proposed_version": "rejected"})
        self.assertEqual(len({c["root_call_id"] for c in discovery["candidates"]}), 1)
        self.assertTrue(all(p["selection"]["caller"]["span"]["line"] == 7 for p in pairs[1:]))
        self.assertTrue(all("builtin_super_and_effective_mro_assumed" in c["premises"] for c in discovery["candidates"][1:]))

    def test_missing_side_cycle_and_bounded_paths_remain_gaps_not_absence_claim(self):
        catalog, modules = source_inputs("from vendor import send\nsend()\n", "", "from .loop import send\n",
            additional=(("new", "vendor/loop.py", "from . import send\n", "native_proposed_version", "vendor", "2.0", ()),))
        discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits())
        self.assertEqual(pairs, [])
        self.assertIn("source_relationship_cycle", {g["reason"] for g in discovery["gaps"]})
        self.assertIn("named_declaration_or_reexport_not_found", {g["reason"] for g in discovery["gaps"]})
        limited, _, _ = discover_source_candidates(catalog, modules, AnalysisLimits(), max_depth=1)
        self.assertIn("source_relationship_depth_limit", {g["reason"] for g in limited["gaps"]})

    def test_decorated_definition_and_candidate_cap_keep_premises_and_omissions(self):
        catalog, modules = source_inputs("from vendor import send\nsend()\n", "@decorator\ndef send():\n pass\n",
                                        "@decorator\ndef send():\n pass\n")
        discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits(max_pairs=1))
        self.assertEqual(len(pairs), 1)
        self.assertIn("effective_decorator_signature_not_established", pairs[0]["comparison"]["remaining_premises"])
        self.assertIn("comparison_candidate_limit", {g["reason"] for g in discovery["gaps"]})

    def test_renamed_distribution_and_src_layout_use_syntax_not_case_names(self):
        catalog, modules = source_inputs("from vendor import send as renamed\nrenamed(app=1)\n",
                                         "def send(*, app=None):\n pass\n", "def send():\n pass\n")
        files = tuple(RetainedSourceFile(f.source_id,
            f.path.replace("vendor/", "src/channel/"), f.content.replace("vendor", "channel").replace("send", "transmit"))
            for f in catalog.files)
        modules = tuple(replace(m, path=m.path.replace("vendor/", "src/channel/"),
            module=m.module.replace("vendor", "channel"), package=m.package.replace("vendor", "channel"),
            dependencies=tuple(d.replace("vendor", "channel") for d in m.dependencies)) for m in modules)
        renamed = RetainedSourceCatalog(catalog.scopes, files, target=replace(TARGET, normalized_package="channel"))
        discovery, pairs, _ = discover_source_candidates(renamed, modules, AnalysisLimits())
        self.assertEqual({p["comparison"]["outcome"] for p in pairs}, {"bound", "rejected"})
        self.assertTrue(all(c["callee_role"]["module"] == "channel" for c in discovery["candidates"]))


def ordinary_control():
    """Actual ordinary entry; fake public provider domain records, HTTP forbidden."""
    from experiments.tests.test_api_adapter_exploration import ChainTests
    explorer = ChainTests().explorer()
    from upgradepilot.github.tag import GitHubTagCommitEvidence
    explorer.tags.resolve_tag_to_commit.side_effect = lambda repo, tag: GitHubTagCommitEvidence(
        repo, tag, "refs/tags/" + tag, "commit", "b" * 40 if tag.lstrip("v") == "1.0" else SHA,
        "b" * 40 if tag.lstrip("v") == "1.0" else SHA, (), datetime(2026, 10, 29, tzinfo=UTC))
    original_inventory = explorer.inventory.acquire.side_effect
    explorer.inventory.acquire.side_effect = lambda repo, sha: TargetInventory(
        repo, sha, "c" * 40, original_inventory(repo, sha).entries + (
            InventoryEntry(repo.split("/")[1] + "/implementation.py", "blob", "100644"),), False)
    def library_file(repo, sha, path):
        package = repo.split("/")[1]
        if package == "bridge":
            content = "from mediator.testing import Client\n"
        elif package == "mediator":
            content = "import vendor\nclass Client(vendor.Base):\n def __init__(self, *, app=None):\n  super().__init__(app=app)\n"
        elif path.endswith("__init__.py"):
            content = "from .implementation import Base\n"
        else:
            content = "class Base:\n def __init__(self" + (", *, app=None" if sha == "b" * 40 else "") + "):\n  pass\n"
        return RepositoryTextFile(repo, path, sha, content)
    explorer.files.get_exact_commit_text_file.side_effect = library_file
    identity = PullRequestIdentity("owner/target", 7, "Bump vendor", "open", False,
                                  "bot", "main", "b" * 40, "update", SHA, 1)
    description = "Initial observation, retained without a second PR read"
    pulls = Mock()
    pulls.get_pull_request_observation.return_value = PullRequestObservation(identity,
        PullRequestDescriptionObservation("retained", description, "https://github.com/owner/target/pull/7",
            datetime(2026, 10, 29, tzinfo=UTC), hashlib.sha256(description.encode()).hexdigest(), len(description)))
    pulls.get_changed_files.return_value = (ChangedFile("requirements.txt", "modified", 1, 1, 2,
        "@@ -1 +1 @@\n-vendor==1.0\n+vendor==2.0"),)
    files = Mock()
    files.get_exact_commit_text_file.side_effect = lambda repo, sha, path: RepositoryTextFile(repo, path, sha,
        "from bridge.testing import Client as C\nC(app=1)\n" if path.endswith(".py") else "vendor==2.0\nbridge>=2\n")
    inventory = Mock()
    inventory.acquire.return_value = TargetInventory("owner/target", SHA, "c" * 40,
        (InventoryEntry("unusual.py", "blob", "100644"), InventoryEntry("requirements.txt", "blob", "100644")), False)
    upstream = Mock()
    upstream.acquire.return_value = AcquisitionProblem("upstream", "source_unavailable", "independent source gap")
    session = TrialPublicSession()
    with patch("requests.sessions.Session.request", side_effect=AssertionError("network forbidden")):
        result = acquire_ordinary_comparison_inputs("owner/target", 7, session=session, adapters=explorer,
            pull_requests=pulls, files=files, target=TargetContextAcquirer(files=files, inventory=inventory), upstream=upstream)
    return result, pulls, explorer


class OrdinaryRetentionTests(TestCase):
    def test_ordinary_entry_closes_reexport_sources_and_retains_initial_observation(self):
        (catalog, modules, acquisition), pulls, explorer = ordinary_control()
        self.assertEqual(pulls.get_pull_request_observation.call_count, 1)
        self.assertEqual(pulls.get_changed_files.call_count, 1)
        self.assertEqual(pulls.get_pull_request.call_count, 0)
        data = encode_ordinary_inputs(catalog, modules, acquisition, proof_class="controlled_ordinary_pr_composition")
        result, companion = prepare_ordinary_comparison(data, AnalysisLimits())
        body, _ = read_ordinary_comparison(result, companion)
        self.assertEqual(body["proof_class"], "controlled_ordinary_pr_composition")
        self.assertEqual(len(body["pairs"]), 3)
        self.assertEqual({c["callee_role"]["role"]: p["comparison"]["outcome"]
            for c, p in zip(body["discovery"]["candidates"], body["pairs"])},
            {"constraint_sample": "bound", "native_old_version": "bound", "native_proposed_version": "rejected"})
        self.assertTrue(any(f.path == "vendor/implementation.py" for f in catalog.files))
        self.assertIn("Initial observation", body["acquisition"]["native_inputs"]["description"]["text"])
        self.assertLessEqual(body["acquisition"]["source_work"]["module_attempts"], 12)

    def test_empty_discovery_round_trip_and_unsupported_history_refusal(self):
        result, companion = prepare_ordinary_comparison(prepared("unknown()\n", "", ""), AnalysisLimits())
        body, _ = read_ordinary_comparison(result, companion)
        self.assertEqual(body["pairs"], [])
        self.assertIn("does not establish no exposure", render_ordinary_comparison(body))
        body["correspondence_version"] = 999
        with self.assertRaisesRegex(ValueError, "Unsupported ordinary"):
            read_ordinary_comparison(json_bytes(body), companion)

    def test_path_role_and_companion_tampering_fail_without_reanalysis(self):
        result, companion = prepare_ordinary_comparison(prepared("from vendor import send\nsend()\n",
            "def send():\n pass\n", "def send():\n pass\n"), AnalysisLimits())
        for change in ("foreign_step", "wrong_role", "bad_source", "receiver"):
            body = json.loads(result)
            candidate = body["discovery"]["candidates"][0]
            if change == "foreign_step":
                candidate["steps"][0]["unit_id"] = "0" * 64
            elif change == "wrong_role":
                candidate["callee_role"]["role"] = "target"
            elif change == "bad_source":
                body["companion_sha256"] = "0" * 64
            else:
                candidate["receiver_mode"] = "one_receiver_assumed"
            with self.subTest(change=change), self.assertRaises(ValueError):
                read_ordinary_comparison(json_bytes(body), companion)

    def test_bounded_worker_immutable_attempt_and_cold_cli_open(self):
        data = prepared("from vendor import send\nsend(app=1)\n",
                        "def send(*, app=None):\n pass\n", "def send():\n pass\n")
        with TemporaryDirectory() as tmp:
            directory = Path(tmp) / "attempt"
            attempt = run_ordinary_comparison(data, directory)
            self.assertEqual(attempt["state"], "completed", attempt)
            with patch("ast.parse", side_effect=AssertionError("AST forbidden")), \
                 patch("requests.sessions.Session.request", side_effect=AssertionError("network forbidden")), \
                 patch("experiments.api_source_correspondence.discover_source_candidates", side_effect=AssertionError("discovery forbidden")), \
                 patch("experiments.api_call_signature.compare_arguments", side_effect=AssertionError("checker forbidden")):
                body, catalog = open_ordinary_comparison(directory)
                self.assertEqual(len(body["pairs"]), 2)
            completed = subprocess.run([sys.executable, "-m", "experiments.api_ordinary_call_signature_trial", "open",
                "--result", str(directory)], capture_output=True, text=True, timeout=10)
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertIn("DISCOVERED SOURCE PATHS", completed.stdout)
            with self.assertRaises(FileExistsError):
                run_ordinary_comparison(data, directory)
            (directory / "sources.json").write_bytes(b"{}")
            with self.assertRaisesRegex(ValueError, "digest mismatch"):
                open_ordinary_comparison(directory)

    def test_analysis_failure_retains_attempt_and_no_completed_result(self):
        with TemporaryDirectory() as tmp:
            directory = Path(tmp) / "failed"
            attempt = run_ordinary_comparison(prepared("unknown()\n", "", ""), directory,
                                               limits=AnalysisLimits(max_nodes_per_file=1))
            self.assertEqual(attempt["state"], "failed")
            self.assertTrue((directory / "attempt-started.json").exists())
            self.assertTrue((directory / "input.json").exists())
            with self.assertRaises(ValueError):
                open_ordinary_comparison(directory)

