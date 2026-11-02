"""Native result closure and bounded product-worker execution controls."""
from contextlib import ExitStack
from dataclasses import replace
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
from unittest import TestCase
from unittest.mock import patch

from test_source_correspondence import material
from upgradepilot.caller_signature.evidence import AnalysisLimits, SourceAnalysisInput
from upgradepilot.caller_signature.result_codec import (
    decode_analysis_input, decode_analysis_result, encode_analysis_input, encode_analysis_result,
)
from upgradepilot.caller_signature.worker import produce_source_analysis, run_source_analysis
from upgradepilot.workspace.native_representation import json_bytes, parse_json
from upgradepilot.workspace.source_access import RetainedSourceCatalog, RetainedSourceFile


def prepared(**limits):
    catalog, modules = material("from vendor import send\nsend(option=1)\n",
        "def send(*, option=None):\n pass\n", "def send():\n pass\n")
    return SourceAnalysisInput(catalog, modules, AnalysisLimits(**limits))


class NativeAnalysisResultTests(TestCase):
    def test_fixed_cold_result_preserves_source_roles_outcomes_and_partiality(self):
        source = prepared()
        # Real retained text outside the static component must stay navigable,
        # with no invented analyzed facts. This is a trusted local control.
        extra = RetainedSourceFile("target", "unrelated.py", "value = 1\n")
        catalog = RetainedSourceCatalog(source.catalog.scopes, source.catalog.files + (extra,), target=source.catalog.target)
        module = replace(source.modules[0], path=extra.path, module="unrelated")
        source = replace(source, catalog=catalog, modules=source.modules + (module,))
        result = produce_source_analysis(source)
        payload = encode_analysis_result(result, source)
        with ExitStack() as stack:
            for hook in ("ast.parse", "upgradepilot.caller_signature.worker.produce_source_analysis",
                         "upgradepilot.caller_signature.correspondence.discover_source_candidates",
                         "upgradepilot.caller_signature.analysis.compare_arguments",
                         "requests.sessions.Session.request", "socket.socket.connect"):
                stack.enter_context(patch(hook, side_effect=AssertionError("Forbidden on cold read")))
            cold_source = decode_analysis_input(encode_analysis_input(source))
            self.assertEqual(cold_source.catalog.identity, source.catalog.identity)
            self.assertEqual(cold_source.modules, source.modules)
            restored = decode_analysis_result(payload, cold_source)
        self.assertEqual(restored, result)
        self.assertEqual({c.callee_role.role: c.comparison.outcome for c in result.candidates},
                         {"old_dependency": "bound", "proposed_dependency": "rejected"})
        extra_uid = catalog.descriptor(extra)["file_id"]
        self.assertEqual([(u.coverage, u.facts) for u in restored.units if u.unit_id == extra_uid], [("unexamined", None)])
        self.assertIn(extra, cold_source.catalog.files)
        self.assertNotIn("content", parse_json(payload))

    def test_input_requires_exact_source_classification_transition_and_limits(self):
        source = prepared()
        payload = encode_analysis_input(source)
        def refuse(change):
            row = parse_json(payload)
            change(row)
            with self.assertRaises(ValueError):
                decode_analysis_input(json_bytes(row))
        refuse(lambda r: r["modules"].pop())
        refuse(lambda r: r["modules"][1].update(version="99"))
        refuse(lambda r: r["modules"][0].update(module="invented"))
        refuse(lambda r: r["limits"].update(max_facts=True))
        refuse(lambda r: r["limits"].update(timeout_seconds_hex="1.0"))
        refuse(lambda r: r.update(analysis_profile="unknown"))

    def test_result_refuses_substituted_inputs_missing_facts_work_and_unknown_method(self):
        source = prepared()
        payload = encode_analysis_result(produce_source_analysis(source), source)
        changes = [
            lambda r: r.update(producer_version="2"),
            lambda r: r.update(binding_version=True),
            lambda r: r.update(input_sha256="0" * 64),
            lambda r: r["units"][0].update(facts=None),
            lambda r: r["units"].pop(),
            lambda r: r["work"].update(scanned_ast_nodes=r["work"]["scanned_ast_nodes"] + 1),
            lambda r: r["admission"][0].update(state="unexamined", reason="aggregate_fact_budget"),
            lambda r: r["candidates"][0]["callee_role"].update(role="constraint_sample"),
            lambda r: r["candidates"][0].update(root_call_id="0" * 64),
            lambda r: r["candidates"][0]["steps"][-1].update(expression="wrong source text"),
        ]
        for i, change in enumerate(changes):
            with self.subTest(corruption=i):
                row = parse_json(payload)
                change(row)
                with self.assertRaises(ValueError):
                    decode_analysis_result(json_bytes(row), source)
        with self.assertRaises(ValueError):
            decode_analysis_result(payload, replace(source, limits=AnalysisLimits(max_pairs=128)))

    def test_protocol_residue_requires_complete_order_and_premises(self):
        def implementation(signature):
            return (f"class Handler:\n def __call__({signature}):\n  pass\n"
                    "class Proxy:\n def __getattr__(self, name):\n  return Handler()\nINSTANCE = Proxy()\n")
        catalog, modules = material("from vendor import INSTANCE\nINSTANCE.label(option=1)\n",
                                   implementation("self, **options"), implementation("self, value"))
        source = SourceAnalysisInput(catalog, modules)
        result = produce_source_analysis(source)
        self.assertTrue(result.candidates)
        payload = encode_analysis_result(result, source)
        for corruption in ("remove_both_former_triggers", "remove_premise", "reorder"):
            row = parse_json(payload)
            candidate = row["candidates"][0]
            if corruption == "remove_both_former_triggers":
                candidate["steps"] = [s for s in candidate["steps"] if s["operation"] not in {"allocation", "factory_return"}]
            elif corruption == "remove_premise":
                candidate["premises"].remove("attribute_lookup_and_getattr_activation_not_established")
            else:
                steps = candidate["steps"]
                a, b = [next(i for i, s in enumerate(steps) if s["operation"] == op) for op in ("allocation", "factory_return")]
                steps[a], steps[b] = steps[b], steps[a]
            with self.subTest(corruption=corruption), self.assertRaisesRegex(ValueError, "factory"):
                decode_analysis_result(json_bytes(row), source)

    def test_whole_file_refusal_retains_text_and_cannot_become_analyzed(self):
        source = prepared(max_facts=1)
        result = produce_source_analysis(source)
        payload = encode_analysis_result(result, source)
        restored = decode_analysis_result(payload, source)
        self.assertFalse(restored.candidates)
        self.assertEqual(len(source.catalog.files), 3)
        self.assertEqual([r.state for r in restored.admission].count("unexamined"), 2)
        row = parse_json(payload)
        omitted = next(u for u in row["units"] if u["coverage"] == "unexamined")
        omitted["coverage"] = "complete_file"
        with self.assertRaises(ValueError):
            decode_analysis_result(json_bytes(row), source)


class NativeAnalysisWorkerTests(TestCase):
    def test_real_child_completes_with_same_input_and_explicit_coverage(self):
        source = prepared()
        run = run_source_analysis(source)
        self.assertEqual((run.state, run.reason, run.worker_returncode), ("completed", None, 0))
        self.assertEqual(run.result, produce_source_analysis(source))
        self.assertEqual(run.result.input_sha256, run.input_sha256)
        self.assertTrue(run.worker_module_origin.endswith("upgradepilot/caller_signature/worker.py"))
        self.assertGreater(run.elapsed.seconds, 0)

    def test_real_child_analysis_limit_is_failure_not_successful_empty_result(self):
        source = prepared(max_nodes=1)
        run = run_source_analysis(source)
        self.assertEqual((run.state, run.reason, run.worker_returncode), ("failed", "analysis_limit", 0))
        self.assertEqual(run.problem_detail, "source_scan_ast_node_limit")
        self.assertIsNone(run.result)
        self.assertEqual(len(source.catalog.files), 3)

    def test_deadline_kills_and_reaps_real_child_without_admitting_a_result(self):
        source = prepared(timeout_seconds=.1)
        real_run = subprocess.run
        pid = None
        with tempfile.TemporaryDirectory() as tmp:
            marker = Path(tmp) / "pid"
            def slow_child(command, **kwargs):
                # Trusted test code only. Exercise the parent's actual subprocess
                # timeout/kill/wait, independent of machine-dependent AST speed.
                return real_run([sys.executable, "-c", "import os,sys,time; open(sys.argv[1], 'w').write(str(os.getpid())); time.sleep(30)", str(marker)], **kwargs)
            with patch("upgradepilot.caller_signature.worker.subprocess.run", side_effect=slow_child):
                run = run_source_analysis(source)
            if marker.exists():
                pid = int(marker.read_text())
        self.assertEqual((run.state, run.reason), ("timed_out", "bounded_worker_deadline"))
        self.assertIsNone(run.result)
        self.assertIsNotNone(pid)
        with self.assertRaises(ProcessLookupError):
            import os
            os.kill(pid, 0)

    def test_interrupt_and_nonzero_exit_do_not_admit_results(self):
        for action, expected in ((KeyboardInterrupt(), ("interrupted", "caller_interrupt")),
                                 (SimpleNamespace(returncode=7), ("failed", "bounded_worker_exit"))):
            with self.subTest(expected=expected):
                args = {"side_effect": action} if isinstance(action, BaseException) else {"return_value": action}
                with patch("upgradepilot.caller_signature.worker.subprocess.run", **args):
                    run = run_source_analysis(prepared())
                self.assertEqual((run.state, run.reason), expected)
                self.assertIsNone(run.result)

    def test_cross_input_worker_exchange_is_refused(self):
        source = prepared()
        foreign = replace(source, limits=AnalysisLimits(max_pairs=128))
        payload = parse_json(encode_analysis_result(produce_source_analysis(foreign), foreign))
        def substitute(command, **kwargs):
            Path(command[-2]).write_bytes(json_bytes(dict(state="completed", reason=None, problem_detail=None,
                worker_module_origin="trusted-test-origin", result=payload)))
            return SimpleNamespace(returncode=0)
        with patch("upgradepilot.caller_signature.worker.subprocess.run", side_effect=substitute):
            run = run_source_analysis(source)
        self.assertEqual((run.state, run.reason), ("failed", "invalid_worker_exchange"))
        self.assertIsNone(run.result)
