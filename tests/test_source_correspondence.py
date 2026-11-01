"""Product source paths, explicit roles and atomic partial work admission."""
from unittest import TestCase

from upgradepilot.caller_signature.correspondence import (
    PythonSourceModule, discover_source_candidates, module_name, ANALYSIS_PROFILE,
)
from upgradepilot.caller_signature.evidence import AnalysisLimits
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.source_access import RetainedSourceCatalog, RetainedSourceFile, RetainedSourceScope


def material(target, old, proposed, package="vendor"):
    revision = "a" * 40
    rows = (("target", "target.py", target, "target_repository", "", "", (package,)),
            ("old", package + "/__init__.py", old, "old_dependency", package, "1.0", ()),
            ("new", package + "/__init__.py", proposed, "proposed_dependency", package, "2.0", ()))
    scopes, files, modules = [], [], []
    for sid, path, text, role, name, version, dependencies in rows:
        repository = "owner/target" if role == "target_repository" else "owner/" + package
        scopes.append(RetainedSourceScope(sid, repository, revision, "repository_text", "trusted local control", "supplied source only"))
        files.append(RetainedSourceFile(sid, path, text))
        modules.append(PythonSourceModule(sid, path, module_name(path), name, version, role, dependencies))
    target = ExactInvestigationTarget("owner/target", 7, "b" * 40, revision, package, "1.0", "2.0")
    return RetainedSourceCatalog(tuple(scopes), tuple(files), target=target), tuple(modules)


class NativeCorrespondenceTests(TestCase):
    def test_discovered_native_pairs_generalize_package_and_keyword_names(self):
        for package, keyword in (("vendor", "option"), ("channel", "certificate")):
            catalog, modules = material(f"from {package} import send\nsend({keyword}=1)\n",
                f"def send(*, {keyword}=None):\n pass\n", "def send():\n pass\n", package)
            discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits(), analysis_profile=ANALYSIS_PROFILE)
            outcomes = {c["callee_role"]["role"]: p["comparison"]["outcome"] for c, p in zip(discovery["candidates"], pairs)}
            self.assertEqual(outcomes, {"old_dependency": "bound", "proposed_dependency": "rejected"})
            self.assertEqual(len({c["root_call_id"] for c in discovery["candidates"]}), 1)
            self.assertTrue(all("installed_namespace_and_dispatch_not_established" in c["premises"]
                                for c in discovery["candidates"]))

    def test_atomic_native_group_refusal_preserves_explicit_unexamined_work(self):
        catalog, modules = material("from vendor import send\nsend(option=1)\n",
                                   "def send(*, option=None):\n pass\n", "def send():\n pass\n")
        discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits(max_facts=1), analysis_profile=ANALYSIS_PROFILE)
        states = {r["unit_id"]: (r["state"], r["reason"]) for r in discovery["analysis_admission"]["units"]}
        native = [states[catalog.descriptor(f)["file_id"]] for f in catalog.files if f.source_id != "target"]
        self.assertEqual(native, [("unexamined", "aggregate_fact_budget")] * 2)
        self.assertFalse(pairs)
        self.assertEqual(len(catalog.files), 3)
        self.assertGreater(discovery["analysis_admission"]["scanned_ast_nodes"], 0)

    def test_renamed_factory_protocol_retains_ordered_witnesses_and_uncertainty(self):
        def source(signature):
            return (f"class Handler:\n def __call__({signature}):\n  pass\n"
                    "class Proxy:\n def __getattr__(self, name):\n  return Handler()\n"
                    "INSTANCE = Proxy()\n")
        catalog, modules = material("from vendor import INSTANCE as I\nI.label(option=1)\n",
                                   source("self, **options"), source("self, value"))
        discovery, pairs, _ = discover_source_candidates(catalog, modules, AnalysisLimits(), analysis_profile=ANALYSIS_PROFILE)
        self.assertEqual({p["comparison"]["outcome"] for p in pairs}, {"bound", "rejected"})
        for candidate in discovery["candidates"]:
            operations = [s["operation"] for s in candidate["steps"]]
            positions = [operations.index(op) for op in ("allocation", "attribute_getter", "factory_return", "call_protocol")]
            self.assertEqual(positions, sorted(positions))
            self.assertIn("attribute_lookup_and_getattr_activation_not_established", candidate["premises"])
