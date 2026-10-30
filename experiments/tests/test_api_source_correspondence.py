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

    def test_local_namespace_collision_retains_external_old_and_proposed_alternatives(self):
        catalog, modules = source_inputs("from vendor import send\nsend(app=1)\n",
            "def send(*, app=None):\n pass\n", "def send():\n pass\n", additional=(
                ("target", "vendor.py", "def send(**kwargs):\n pass\n", "target", "", "", ("vendor",)),))
        discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits())
        self.assertEqual(len(pairs), 3)
        self.assertEqual({c["callee_role"]["role"] for c in discovery["candidates"]},
                         {"target", "native_old_version", "native_proposed_version"})
        self.assertTrue(all("local_and_external_namespace_candidates" in c["premises"]
                            for c in discovery["candidates"]))

    def test_multiple_declared_bases_stay_alternatives_without_mro_selection(self):
        catalog, modules = source_inputs("from facade import Client\nClient()\n",
            "class A:\n def __init__(self):\n  pass\nclass B:\n def __init__(self, *, required):\n  pass\n",
            "", additional=(("facade", "facade/__init__.py", "import vendor\nclass Client(vendor.A, vendor.B):\n"
                " def __init__(self):\n  super().__init__()\n", "constraint_sample", "facade", "5.0", ("vendor",)),))
        modules = tuple(replace(m, dependencies=("facade",)) if m.role == "target" else m for m in modules)
        discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits())
        base_candidates = [c for c in discovery["candidates"] if c["callee_role"]["role"] == "native_old_version"]
        self.assertEqual(len(base_candidates), 2)
        self.assertEqual({p["comparison"]["outcome"] for p in pairs}, {"bound", "rejected"})
        self.assertTrue(all("builtin_super_and_effective_mro_assumed" in c["premises"] for c in base_candidates))

    def test_ambiguous_layout_and_invalid_syntax_do_not_become_removed_api(self):
        catalog, modules = source_inputs("from vendor import send\nsend()\n", "def send(:\n", "def send():\n pass\n",
            additional=(("new", "src/vendor/__init__.py", "def send():\n pass\n", "native_proposed_version", "vendor", "2.0", ()),))
        discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits())
        self.assertEqual(pairs, [])
        self.assertEqual({g["reason"] for g in discovery["gaps"]} & {"ambiguous_module_layout", "source_syntax_unavailable"},
                         {"ambiguous_module_layout", "source_syntax_unavailable"})

    def test_long_path_limit_keeps_explicit_omission_without_invalid_saved_path(self):
        catalog, modules = source_inputs("from vendor import Client\nClient()\n",
            "class Client:\n def __init__(self):\n  pass\n", "class Client:\n def __init__(self):\n  pass\n")
        discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits(), max_path_steps=3)
        self.assertEqual(pairs, [])
        self.assertIn("source_path_limit", {g["reason"] for g in discovery["gaps"]})

    def test_export_overwrite_stays_a_conditional_declaration_with_visible_gap(self):
        catalog, modules = source_inputs("from vendor import send\nsend(app=1)\n",
            "def send(*, app=None):\n pass\nsend = replacement\n", "def send():\n pass\ndel send\n")
        discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits())
        self.assertEqual(len(pairs), 2)
        self.assertEqual(sum(g["reason"] == "export_write_or_deletion_not_resolved" for g in discovery["gaps"]), 2)
        self.assertTrue(all("effective_export_binding_not_established" in c["premises"] for c in discovery["candidates"]))


def ordinary_control(*, protocol=False):
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
            content = "from mediator.testing import FACTORY\n" if protocol else "from mediator.testing import Client\n"
        elif package == "mediator":
            content = "from vendor import FACTORY\n" if protocol else "import vendor\nclass Client(vendor.Base):\n def __init__(self, *, app=None):\n  super().__init__(app=app)\n"
        elif path.endswith("__init__.py"):
            content = "from .implementation import FACTORY\n" if protocol else "from .implementation import Base\n"
        else:
            content = factory_source("self, **kwargs" if sha == "b" * 40 else "self") if protocol else "class Base:\n def __init__(self" + (", *, app=None" if sha == "b" * 40 else "") + "):\n  pass\n"
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
        ("from bridge.testing import FACTORY as F\nF.label(app=1)\n" if protocol else "from bridge.testing import Client as C\nC(app=1)\n")
        if path.endswith(".py") else "vendor==2.0\nbridge>=2\n")
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
    def test_current_ordinary_method_binds_support_without_curated_runner_dependency(self):
        result, companion = prepare_ordinary_comparison(prepared("from vendor import send\nsend()\n",
            "def send():\n pass\n", "def send():\n pass\n"), AnalysisLimits())
        body, _ = read_ordinary_comparison(result, companion)
        support = "experiments/api_signature_evidence.py"
        self.assertEqual(body["code_sha256"][support], hashlib.sha256(Path(support).read_bytes()).hexdigest())
        self.assertNotIn("experiments/api_call_signature_trial.py", body["code_sha256"])
        self.assertEqual(len(body["code_sha256"]), 12)
        body["code_sha256"]["experiments/unadmitted_support.py"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "method source closure"):
            read_ordinary_comparison(json_bytes(body), companion)

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
        for change in ("foreign_step", "wrong_role", "bad_source", "receiver", "path_text", "root", "receipt", "discovery_shape"):
            body = json.loads(result)
            candidate = body["discovery"]["candidates"][0]
            if change == "foreign_step":
                candidate["steps"][0]["unit_id"] = "0" * 64
            elif change == "wrong_role":
                candidate["callee_role"]["role"] = "target"
            elif change == "bad_source":
                body["companion_sha256"] = "0" * 64
            elif change == "path_text":
                candidate["steps"][0]["expression"] = "fabricated source text"
            elif change == "root":
                candidate["root_call_id"] = candidate["signature_id"]
            elif change == "receipt":
                body["acquisition"]["ordinary_acquisition"] = "invalid"
            elif change == "discovery_shape":
                body["discovery"] = []
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
            self.assertIn("\nProof: retained_component_discovery\n", completed.stdout)
            self.assertIn("\nCaller:", completed.stdout)
            unit_id = catalog.descriptor(catalog.files[0])["file_id"]
            viewed = subprocess.run([sys.executable, "-m", "experiments.api_ordinary_call_signature_trial", "open",
                "--result", str(directory), "--source", unit_id], capture_output=True, text=True, timeout=10)
            self.assertEqual(viewed.returncode, 0, viewed.stderr)
            self.assertIn("LITERAL RETAINED SOURCE", viewed.stdout)
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

    def test_worker_deadline_is_not_a_completed_unknown_result(self):
        with TemporaryDirectory() as tmp:
            directory = Path(tmp) / "timed-out"
            attempt = run_ordinary_comparison(prepared("unknown()\n", "", ""), directory,
                                               limits=AnalysisLimits(timeout_seconds=0.000001))
            self.assertEqual(attempt["state"], "timed_out")
            self.assertIsNone(attempt["result_sha256"])
            with self.assertRaises(ValueError):
                open_ordinary_comparison(directory)

    def test_nonimportable_target_filename_keeps_calls_and_receipt_gaps_visible(self):
        catalog, modules = source_inputs("from vendor import send\nsend()\n", "def send():\n pass\n", "def send():\n pass\n")
        files = tuple(replace(f, path="checks/test-with-dash.py") if f.source_id == "target" else f for f in catalog.files)
        modules = tuple(replace(m, path="checks/test-with-dash.py", module="") if m.role == "target" else m for m in modules)
        catalog = RetainedSourceCatalog(catalog.scopes, files, target=TARGET)
        receipt = {"ordinary_acquisition": {"target": {"omitted_paths": ["later.py"]}, "changed_package_sources": {
            "unexamined_modules": ["vendor.other"], "attempts": [{"state": "refused", "request": {
                "package": "vendor", "version": "2.0", "module": "vendor.other"}, "stage": "python_source_budget",
                "reason": "module_source_limit", "detail": "control refusal"}]}}, "material_omissions": [{
            "repository": "owner/target", "revision": SHA, "path": "large.py", "role": "target", "reason": "analysis_material_limit"}]}
        data = encode_ordinary_inputs(catalog, modules, receipt, proof_class="retained_component_discovery")
        result, companion = prepare_ordinary_comparison(data, AnalysisLimits())
        body, _ = read_ordinary_comparison(result, companion)
        self.assertEqual(len(body["pairs"]), 2)
        view = render_ordinary_comparison(body)
        for expected in ("Material omitted: target large.py", "Target source unexamined: later.py",
                         "Source refused: vendor 2.0 vendor.other", "Changed-package module unexamined: vendor.other"):
            self.assertIn(expected, view)

    def test_controlled_initial_observation_cannot_conflict_with_saved_target(self):
        (catalog, modules, acquisition), _, _ = ordinary_control()
        result, companion = prepare_ordinary_comparison(encode_ordinary_inputs(catalog, modules, acquisition,
            proof_class="controlled_ordinary_pr_composition"), AnalysisLimits())
        body = json.loads(result)
        body["acquisition"]["native_inputs"]["identity"]["head_sha"] = "c" * 40
        with self.assertRaisesRegex(ValueError, "observation/target mismatch"):
            read_ordinary_comparison(json_bytes(body), companion)


def factory_source(signature="self, *args, **kwargs", *, returns="return Decorator()", extra=""):
    """Locally authored syntax, not a pytest-name or known-callable mapping."""
    return ("class Decorator:\n def __call__(" + signature + "):\n  pass\n"
            "class Generator:\n def __getattr__(self, name):\n  " + returns.replace("\n", "\n  ") + "\n"
            "FACTORY = Generator()\n" + extra)


class FactorySourceTests(TestCase):
    def test_ordinary_pr_entry_retains_protocol_sources_and_worker_opens_offline(self):
        (catalog, modules, acquisition), pulls, _ = ordinary_control(protocol=True)
        data = encode_ordinary_inputs(catalog, modules, acquisition, proof_class="controlled_ordinary_pr_composition")
        with TemporaryDirectory() as tmp:
            directory = Path(tmp) / "protocol"
            attempt = run_ordinary_comparison(data, directory)
            self.assertEqual(attempt["state"], "completed", attempt)
            with patch("ast.parse", side_effect=AssertionError("AST forbidden")), \
                 patch("requests.sessions.Session.request", side_effect=AssertionError("HTTP forbidden")), \
                 patch("experiments.api_source_correspondence.discover_source_candidates", side_effect=AssertionError("discovery forbidden")):
                body, retained = open_ordinary_comparison(directory)
            outcomes = {c["callee_role"]["role"]: p["comparison"]["outcome"]
                        for c, p in zip(body["discovery"]["candidates"], body["pairs"])}
            self.assertEqual(outcomes, {"native_old_version": "bound", "native_proposed_version": "rejected"})
            self.assertEqual(pulls.get_pull_request_observation.call_count, 1)
            self.assertEqual(pulls.get_pull_request.call_count, 0)
            self.assertEqual(body["acquisition"]["source_work"]["module_attempts"], 6)
            self.assertTrue(any(f.path.endswith("implementation.py") for f in retained.files))

    def test_allocation_getter_return_call_protocol_reaches_old_and_proposed(self):
        data = prepared("from vendor import FACTORY as marks\nmarks.label(1, ids=lambda x: x)\n",
                        factory_source(), factory_source("self, value"))
        result, companion = prepare_ordinary_comparison(data, AnalysisLimits())
        body, _ = read_ordinary_comparison(result, companion)
        self.assertEqual(body["correspondence_version"], 2)
        outcomes = {c["callee_role"]["role"]: p["comparison"]["outcome"]
                    for c, p in zip(body["discovery"]["candidates"], body["pairs"])}
        self.assertEqual(outcomes, {"native_old_version": "bound", "native_proposed_version": "rejected"})
        for c, p in zip(body["discovery"]["candidates"], body["pairs"]):
            operations = [s["operation"] for s in c["steps"]]
            for required in ("allocation", "attribute_getter", "factory_return", "call_protocol"):
                self.assertIn(required, operations)
            self.assertEqual(p["comparison"]["receiver_mode"], "one_receiver_assumed")
            self.assertIn("factory_constructor_arguments_not_checked", c["premises"])
        view = render_ordinary_comparison(body)
        self.assertIn("factory_return", view)
        self.assertIn("attribute_lookup_and_getattr_activation_not_established", view)

    def test_renamed_annotated_allocation_and_relative_class_reexports_are_generic(self):
        caller = "from vendor import gateway\ngateway.operation(ids=[1])\n"
        root = "from .factory import Maker as Build\ngateway: object = Build()\n"
        other = "from .payload import Action\nclass Maker:\n def __getattr__(self, name):\n  return Action()\n"
        catalog, modules = source_inputs(caller, root, root, additional=tuple(
            (sid, path, text, role, "vendor", version, ())
            for sid, role, version in (("old", "native_old_version", "1.0"), ("new", "native_proposed_version", "2.0"))
            for path, text in (("vendor/factory.py", other), ("vendor/payload.py", "class Action:\n def __call__(self, **kwargs):\n  pass\n"))))
        discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits())
        self.assertEqual(len(pairs), 2)
        self.assertTrue(all(p["comparison"]["keyword_reception"][0]["outcome"] == "variadic_keyword" for p in pairs))
        self.assertTrue(all(any(s["operation"] == "reexport" for s in c["steps"]) for c in discovery["candidates"]))

    def test_getter_return_alternatives_keep_supported_and_unsupported_branches(self):
        source = factory_source(returns="if enabled:\n return Decorator()\nreturn unknown_value")
        result, companion = prepare_ordinary_comparison(prepared("from vendor import FACTORY\nFACTORY.label(ids=[])\n", source, source), AnalysisLimits())
        body, _ = read_ordinary_comparison(result, companion)
        self.assertEqual(len(body["pairs"]), 2)
        self.assertTrue(any(g["reason"] == "factory_return_expression_unsupported" for g in body["discovery"]["gaps"]))
        self.assertTrue(all("execution_reaches_factory_return_and_branch" in c["premises"] for c in body["discovery"]["candidates"]))

    def test_overloads_and_competing_allocations_are_not_first_match_selection(self):
        source = factory_source().replace(" def __call__(self, *args, **kwargs):",
            " @overload\n def __call__(self, item):\n  ...\n def __call__(self, *args, **kwargs):")
        source += "if flag:\n FACTORY = Generator()\n"
        catalog, modules = source_inputs("from vendor import FACTORY\nFACTORY.label(1, ids=[])\n", source, source)
        discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits())
        self.assertEqual(len(pairs), 8)
        self.assertEqual({p["comparison"]["outcome"] for p in pairs}, {"bound", "rejected"})
        self.assertEqual(len({(c["signature_id"], c["callee_role"]["role"]) for c in discovery["candidates"]}), 4)
        encoded = encode_ordinary_inputs(catalog, modules, {}, proof_class="retained_component_discovery")
        result, companion = prepare_ordinary_comparison(encoded, AnalysisLimits())
        body, _ = read_ordinary_comparison(result, companion)
        self.assertIn("Declared decorators (syntax only): overload", render_ordinary_comparison(body))

    def test_unsupported_factories_missing_protocol_and_nested_return_remain_gaps(self):
        for source, reason in (
            (factory_source(returns="value = Decorator()\nreturn value"), "factory_return_expression_unsupported"),
            (factory_source().replace("__call__", "other"), "inherited_or_missing_protocol_method"),
            (factory_source(returns="def hidden():\n return Decorator()\nraise Exception()"), "factory_getter_has_no_supported_return"),
            ("def create():\n return object()\nFACTORY = create()\n", "allocated_class_getter_unavailable"),
        ):
            with self.subTest(reason=reason):
                discovery, pairs, _ = discover_source_candidates(*source_inputs(
                    "from vendor import FACTORY\nFACTORY.label(ids=[])\n", source, source), AnalysisLimits())
                self.assertEqual(pairs, [])
                self.assertIn(reason, {g["reason"] for g in discovery["gaps"]})

    def test_protocol_paths_respect_caps_and_retain_export_mutation_limits(self):
        source = factory_source(extra="FACTORY = replacement\ndel FACTORY\n")
        catalog, modules = source_inputs("from vendor import FACTORY\nFACTORY.label(ids=[])\n", source, source)
        discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits(max_pairs=1))
        self.assertEqual(len(pairs), 1)
        self.assertIn("comparison_candidate_limit", {g["reason"] for g in discovery["gaps"]})
        self.assertIn("export_write_or_deletion_not_resolved", {g["reason"] for g in discovery["gaps"]})
        limited, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits(), max_path_steps=4)
        self.assertEqual(pairs, [])
        self.assertIn("source_path_limit", {g["reason"] for g in limited["gaps"]})

    def test_protocol_method1_downgrade_and_source_text_tampering_refuse(self):
        result, companion = prepare_ordinary_comparison(prepared("from vendor import FACTORY\nFACTORY.label(ids=[])\n",
            factory_source(), factory_source()), AnalysisLimits())
        body, _ = read_ordinary_comparison(result, companion)
        body["correspondence_version"] = 1
        with self.assertRaisesRegex(ValueError, "Foreign source path step"):
            read_ordinary_comparison(json_bytes(body), companion)
        body = json.loads(result)
        step = next(s for s in body["discovery"]["candidates"][0]["steps"] if s["operation"] == "factory_return")
        step["expression"] = "return unrelated()"
        with self.assertRaisesRegex(ValueError, "text/span mismatch"):
            read_ordinary_comparison(json_bytes(body), companion)
        for change in ("missing_step", "missing_premise"):
            altered = json.loads(result)
            candidate = altered["discovery"]["candidates"][0]
            if change == "missing_step":
                candidate["steps"] = [s for s in candidate["steps"] if s["operation"] != "attribute_getter"]
            else:
                candidate["premises"].remove("factory_returns_selected_declared_class_instance")
            with self.subTest(change=change), self.assertRaises(ValueError):
                read_ordinary_comparison(json_bytes(altered), companion)

    def test_residual_protocol_operations_require_whole_sequence_even_without_both_old_triggers(self):
        result, companion = prepare_ordinary_comparison(prepared(
            "from vendor import FACTORY\nFACTORY.label(ids=[])\n", factory_source(), factory_source()), AnalysisLimits())
        for remaining in ("getter_and_call", "getter_only", "call_only"):
            altered = json.loads(result)
            candidate = altered["discovery"]["candidates"][0]
            candidate["steps"] = [step for step in candidate["steps"]
                                  if step["operation"] not in {"allocation", "factory_return"}]
            if remaining == "getter_only":
                # Keep the literal final signature span/endpoint valid: corruption
                # must reach protocol admission, rather than an unrelated check.
                candidate["steps"][-1]["operation"] = "attribute_getter"
            elif remaining == "call_only":
                candidate["steps"] = [step for step in candidate["steps"]
                                      if step["operation"] != "attribute_getter"]
            with self.subTest(remaining=remaining), self.assertRaisesRegex(ValueError, "factory source path"):
                read_ordinary_comparison(json_bytes(altered), companion)

    def test_async_generator_getters_and_multi_attribute_access_are_not_instance_returns(self):
        for source in (factory_source().replace("def __getattr__", "async def __getattr__"),
                       factory_source(returns="yield 1\nreturn Decorator()")):
            with self.subTest(source=source):
                discovery, pairs, _ = discover_source_candidates(*source_inputs(
                    "from vendor import FACTORY\nFACTORY.label(ids=[])\n", source, source), AnalysisLimits())
                self.assertEqual(pairs, [])
                self.assertIn("async_or_generator_getter_unsupported", {g["reason"] for g in discovery["gaps"]})
        discovery, pairs, _ = discover_source_candidates(*source_inputs(
            "from vendor import FACTORY\nFACTORY.label.extra(ids=[])\n", factory_source(), factory_source()), AnalysisLimits())
        self.assertEqual(pairs, [])
        self.assertIn("factory_attribute_chain_unsupported", {g["reason"] for g in discovery["gaps"]})

    def test_star_arguments_keep_partial_keyword_evidence_without_full_binding(self):
        result, companion = prepare_ordinary_comparison(prepared(
            "from vendor import FACTORY\nFACTORY.label(*values, ids=[], **options)\n",
            factory_source(), factory_source()), AnalysisLimits())
        body, _ = read_ordinary_comparison(result, companion)
        self.assertEqual(len(body["pairs"]), 2)
        for pair in body["pairs"]:
            self.assertEqual(pair["comparison"]["outcome"], "undetermined")
            self.assertFalse(pair["comparison"]["checks_complete"])
            self.assertEqual(pair["comparison"]["keyword_reception"][0]["outcome"], "variadic_keyword")

