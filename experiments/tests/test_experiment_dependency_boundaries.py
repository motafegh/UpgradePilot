"""Static boundary policy rejects regressions without importing inspected source."""

import json
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

CHECKER = Path(__file__).resolve().parents[2] / "tools/check_experiment_boundaries.py"


class ExperimentBoundaryTests(TestCase):
    def check(self, *, source="", target="", product="", mutation=None, classify=True):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "experiments").mkdir()
            (root / "src/upgradepilot").mkdir(parents=True)
            (root / "AGENTS.md").write_text("controlled ownership reference")
            (root / "pyproject.toml").write_text('[tool.setuptools.packages.find]\nwhere=["src"]\n')
            (root / "experiments/a.py").write_text(source)
            (root / "experiments/b.py").write_text(target)
            (root / "src/upgradepilot/app.py").write_text(product)
            artifacts = [dict(path=path, family="api_source", roles=["substrate"],
                              maintenance="control", evidence="AGENTS.md")
                         for path in ("experiments/role_inventory.json", "experiments/a.py", "experiments/b.py")]
            manifest = dict(format="experiment-role-inventory/1", artifacts=artifacts,
                families={"api_source": {"owner": "AGENTS.md"}, "other": {"owner": "AGENTS.md"}},
                allowed_cross_family_dependencies=[], legacy_private_imports=[])
            if not classify:
                artifacts.pop()
            if mutation:
                mutation(manifest)
            (root / "experiments/role_inventory.json").write_text(json.dumps(manifest))
            completed = subprocess.run([sys.executable, str(CHECKER), "--root", str(root)],
                capture_output=True, text=True, timeout=10)
            return completed.returncode, json.loads(completed.stdout)

    def test_source_is_not_imported_and_classified_forward_dependency_passes(self):
        status, result = self.check(source="from .b import public\nraise RuntimeError('must not run')\n")
        self.assertEqual(status, 0, result)
        self.assertTrue(result["ok"])

    def test_unclassified_artifact_and_runtime_test_exemption_are_rejected(self):
        status, result = self.check(classify=False)
        self.assertNotEqual(status, 0)
        self.assertTrue(any("unclassified" in e for e in result["errors"]))
        _, result = self.check(mutation=lambda m: m["artifacts"][1].update(roles=["test"]))
        self.assertTrue(any("test exemption" in e for e in result["errors"]))

    def test_product_static_and_dynamic_reverse_loads_are_rejected(self):
        for source in ("from experiments.a import value\n", "import importlib\nimportlib.import_module(name)\n"):
            with self.subTest(source=source):
                status, result = self.check(product=source)
                self.assertNotEqual(status, 0)
                self.assertTrue(any("product" in e for e in result["errors"]))

    def test_runtime_test_import_and_new_private_dependency_are_rejected(self):
        for source, error in (("from experiments.tests import fixture\n", "runtime test dependency"),
                              ("from .b import _private\n", "new private dependency"),
                              ("import experiments.b as old\nold._private()\n", "new private dependency")):
            with self.subTest(source=source):
                status, result = self.check(source=source)
                self.assertNotEqual(status, 0)
                self.assertTrue(any(error in e for e in result["errors"]))

    def test_closed_legacy_exception_is_exact_and_must_remain_used(self):
        exception = dict(source="experiments.a", target="experiments.b", names=["_private"], reason="controlled legacy protocol")
        configure = lambda m: m.update(legacy_private_imports=[exception])
        status, result = self.check(source="from .b import _private\n", mutation=configure)
        self.assertEqual(status, 0, result)
        _, result = self.check(mutation=configure)
        self.assertTrue(any("stale private exception" in e for e in result["errors"]))

    def test_cross_family_runner_inversion_and_cycles_are_rejected(self):
        for source, target, mutation, error in (
            ("from .b import public\n", "", lambda m: m["artifacts"][2].update(family="other"), "cross-family"),
            ("from .b import public\n", "", lambda m: m["artifacts"][2].update(roles=["runner"]), "dependency on runner"),
            ("from .b import public\n", "from .a import public\n", None, "cycle"),
        ):
            with self.subTest(error=error):
                status, result = self.check(source=source, target=target, mutation=mutation)
                self.assertNotEqual(status, 0)
                self.assertTrue(any(error in e for e in result["errors"]))
        status, result = self.check(source="from .b import public\n",
            mutation=lambda m: m["artifacts"][2].update(roles=["reader", "substrate", "runner"]))
        self.assertEqual(status, 0, result)
