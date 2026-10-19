"""Cohort admission, zero-generation preflight and hard-stop composition controls.

SDK/backend/retained-input substitutes are explicit test patches. Real model callbacks,
report packing, strict adapter publication, attempt accounting and driver cleanup execute.
No production alternate deployment or unqualified inference path is introduced.
"""

import json
from copy import deepcopy
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

from experiments import run_investigator_supplied_evidence as runner
from experiments.investigator_model_interface import digest
from experiments.investigator_run_control import PredictionDeadlineExceeded
from experiments.investigator_supplied_evidence import (
    SuppliedEvidenceLimits, SuppliedEvidenceTrial, mechanical_report,
)
from experiments.tests.test_investigator_model_interface import Binding, config
from experiments.tests.test_investigator_workspace_trial import fixture, request
from upgradepilot.workspace.native_representation import json_bytes


class CohortBinding(Binding):
    finalization_seconds = 50

    def __init__(self, defect=None):
        super().__init__()
        self.defect = defect
        self.inputs = []

    def predict(self, measured, timeout, *, visible_sink):
        role = json.loads(measured.packed.content)["task"]["case_label"]
        self.last_prediction_metadata = None
        self.last_prediction_control = {}
        self.inputs.append(measured.messages)
        self.response = mechanical_report(measured.packed)
        if role == "probe-report" and self.defect == "no_canary_citation":
            body = json.loads(self.response)
            body["claims"][0]["evidence"] = []
            self.response = json_bytes(body)
        if role == "packet-a" and self.defect == "foreign_citation":
            body = json.loads(self.response)
            body["claims"][0]["evidence"][0]["id"] = "foreign"
            self.response = json_bytes(body)
        if (role == "probe-cancel" and self.defect == "unknown_cancel") or (
            role == "probe-report" and self.defect == "operator_interrupt"
        ):
            self.calls += 1
            visible_sink(b'{"claims":')
            raise KeyboardInterrupt("operator primary") if self.defect == "operator_interrupt" else RuntimeError("missing terminal usage")
        content, metadata, reasoning = super().predict(measured, timeout, visible_sink=visible_sink)
        if role == "probe-cancel":
            self.last_prediction_metadata = metadata
            self.last_prediction_control = {
                "cancellation_requested": True, "terminal_received": True,
                "channel_released": True, "secondary_problems": [],
                "prediction_elapsed_seconds": .001, "finalization_elapsed_seconds": 0,
                "receive_ownership": {"receiver_stopped": True},
            }
            raise PredictionDeadlineExceeded("simulated controlled probe deadline")
        return content, metadata, reasoning


class RunnerTests(unittest.TestCase):
    def test_isolated_control_uses_fresh_five_role_cohort_with_strict_usage(self):
        with tempfile.TemporaryDirectory() as directory:
            root, binding = Path(directory), CohortBinding()
            stack, sdk, preparation, reviewer = self.environment(root, binding)
            external = {"path": "synthetic-isolated-control", "sdk_source_sha256": {"synthetic_sdk": "test"}}
            with stack, patch.object(runner, "closed_control_probe", return_value=external):
                runtime = root / "runtime"
                runner.prepare_runtime(sdk, preparation, reviewer, runtime,
                                       control_probe=Path("synthetic-isolated-control"))
                frozen = json.loads((runtime / "freeze.json").read_bytes())
                self.assertEqual(frozen["execution_roles"], list(runner.ROLES[1:]))
                self.assertEqual(frozen["execution_ceilings"]["attempts"], 5)
                self.assertEqual(frozen["execution_ceilings"]["input_tokens"], 73096)
                self.assertEqual(frozen["execution_ceilings"]["generated_tokens"], 40960)
                self.assertFalse(frozen["cancellation_probe"]["required"])
                h = digest((runtime / "freeze.json").read_bytes())
                result = runner.execute(sdk, runtime / "freeze.json", h, h, root / "execution")
                self.assertEqual([row["role"] for row in result["rows"]], list(runner.ROLES[1:]))
                self.assertTrue(all(row["execution"] == "completed" for row in result["rows"]))
                self.assertEqual(result["measured_known_usage"]["known_usage_attempts"], 5)
                self.assertEqual(result["measured_known_usage"]["unknown_usage_attempts"], 0)

    def test_closed_control_requires_original_artifacts_sources_terminal_and_cleanup(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run = root / "closed"
            (run / "probe-cancel").mkdir(parents=True)
            source = Path("experiments/investigator_model_interface.py").read_bytes()
            (root / "source.py").write_bytes(source)
            frozen = {"code_sha256": {
                "experiments/investigator_model_interface.py": digest(source),
                "experiments/investigator_run_control.py": digest(Path("experiments/investigator_run_control.py").read_bytes())},
                "sdk_source_sha256": {"synthetic": "pinned"},
                "capacity_contract": {"context": runner.CONTEXT, "input_caps": runner.INPUT_CAPS},
                "reference_profile_sha256": runner.REFERENCE_PROFILE_SHA256}
            receipt = {"problem": "PredictionDeadlineExceeded", "usage": {"stopReason": "userStopped"},
                "control": {"cancellation_requested": True, "terminal_received": True,
                    "channel_released": True, "secondary_problems": [],
                    "receive_ownership": {"receiver_stopped": True, "submitted": 1,
                                          "acknowledged": 1, "events": {"success": 1}}}}
            records = {"executed-freeze.json": frozen, "probe-cancel/call-01.receipt.json": receipt,
                "summary.json": {"rows": [{"role": "probe-cancel", "prediction_attempts": 1,
                    "execution": "failed", "model_receipts": [receipt], "usage_complete": False},
                    *[{"role": role, "execution": "unattempted"} for role in runner.ROLES[1:]]]},
                "cleanup.json": {"confirmed": True, "remaining_identifiers": []},
                "client-cleanup.json": {"confirmed": True}}
            for name, content in records.items():
                (run / name).write_bytes(json_bytes(content))
            def evidence():
                body = {"format": "investigator-closed-control-probe/1", "root": str(run),
                    "model_interface_source": str(root / "source.py"),
                    "unknown_usage_reservation": {"input": 4096, "generated": 8192},
                    "artifact_sha256": {str(p.relative_to(run)): digest(p.read_bytes())
                                        for p in run.rglob("*") if p.is_file()}}
                path = root / "evidence.json"
                path.write_bytes(json_bytes(body))
                return path
            path = evidence()
            self.assertIn("token usage unknown", runner.closed_control_probe(path)["scope"])
            for field in ("terminal_received", "channel_released", "cancellation_requested"):
                receipt["control"][field] = False
                (run / "probe-cancel/call-01.receipt.json").write_bytes(json_bytes(receipt))
                with self.subTest(field=field), self.assertRaises(ValueError):
                    runner.closed_control_probe(evidence())
                receipt["control"][field] = True
            (run / "probe-cancel/call-01.receipt.json").write_bytes(json_bytes(receipt))
            path = evidence()
            (run / "cleanup.json").write_bytes(b"{}")
            with self.assertRaisesRegex(ValueError, "artifact drift"):
                runner.closed_control_probe(path)
            with self.assertRaisesRegex(ValueError, "cleanup evidence incomplete"):
                runner.closed_control_probe(evidence())

    def environment(self, root, binding, *, cleanup_failure=False):
        preparation = root / "preparation"
        preparation.mkdir()
        (preparation / "preparation.json").write_text("{}")
        qualification = root / "qualified.json"
        qualification.write_text("{}")
        recipes = {"format": "investigator-supplied-evidence-recipes/1", "cases": [
            {"label": role, "case_id": "synthetic-test", "source_pair": False, "requests": []}
            for role in runner.ROLES[2:]
        ]}
        (preparation / "packet-recipes.json").write_text(json.dumps(recipes))
        manifest = {"qualified_input_path": str(qualification), "cases": []}
        reviewer = root / "reviewer.json"
        reviewer.write_text(json.dumps({
            "format": "investigator-source-aware-review-protocol/1",
            "reviewer": "PRIVATE_REVIEWER_ANSWER_NEVER_INPUT",
            "materiality": "All required material obligations; no semantic grading in runner",
            "obligations": {label: [{"id": str(n), "criterion": "Source-aware review", "source_locators": ["synthetic test only"]} for n in range(count)]
                for label, count in zip(runner.ROLES[2:], (6, 4, 6, 4))},
        }))
        loaded = []
        def unload():
            if cleanup_failure:
                raise OSError("model unload secondary")
            loaded.clear()
        model = SimpleNamespace(identifier="owned-test-instance", unload=unload)
        def load(client, profile):
            self.assertEqual(profile["requested_load"]["contextLength"], runner.CONTEXT)
            self.assertEqual(profile["identifier"], runner.CAPACITY_IDENTIFIER)
            loaded.append(model)
            return model
        class Client:
            llm = SimpleNamespace(list_loaded=lambda: list(loaded))
            def __enter__(self):
                return self
            def __exit__(self, *args):
                if cleanup_failure:
                    raise OSError("client close secondary")
        timeout = [60]
        sdk = SimpleNamespace(Client=lambda address: Client(),
            get_sync_api_timeout=lambda: timeout[0],
            set_sync_api_timeout=lambda value: timeout.__setitem__(0, value))
        parent_load = {"fields": [{"key": "llm.load.contextLength", "value": 32768},
            {"key": "synthetic.otherLoad", "value": "must not change"},
            {"key": "llm.load.llama.acceleration.offloadRatio", "value": .45}]}
        backend = {"executable": "synthetic-backend", "cpu_kv": True,
            "backend_template_sha256": "synthetic-template", "kv_unified_flag": False,
            "no_kv_unified_flag": True,
            "flags": {"ctx-size": "32768", "n-gpu-layers": "synthetic-placement"}}
        profile = {"prediction_configuration": config(), "prediction_base_sha256": "synthetic-base",
            "tokenizer_policy": {}, "requested_load": {"contextLength": 32768, "gpu": {"ratio": .45}},
            "model_key": "synthetic-model", "identifier": "synthetic-parent", "context": 32768,
            "initial_identity": {"model": {"instanceReference": "parent-instance",
                "identifier": "synthetic-parent", "contextLength": 32768, "modelKey": "synthetic-model"},
                "load": parent_load}, "backend_observation": backend}
        binding.current = deepcopy(profile["initial_identity"])
        binding.current["model"].update(instanceReference="test-capacity-instance",
            identifier=runner.CAPACITY_IDENTIFIER, contextLength=runner.CONTEXT)
        binding.current["load"]["fields"][0]["value"] = runner.CONTEXT
        binding.current["load"]["fields"][2]["value"] = runner.GPU_RATIO
        actual_backend = deepcopy(backend)
        actual_backend["flags"]["ctx-size"] = str(runner.CONTEXT)
        actual_backend["flags"]["n-gpu-layers"] = runner.GPU_LAYERS
        def new_trial(role, *args):
            limit = SuppliedEvidenceLimits(reads=2, references=2, operations=18, seconds=300) if role.startswith("probe-") else None
            trial = SuppliedEvidenceTrial(fixture(), [request("read_source", source_id="target", path="requirements.txt", line_count=1)],
                case_label=role, limits=limit)
            trial.prepare()
            return trial
        stack = ExitStack()
        stack.enter_context(patch.object(runner, "verify_prepared_packets", return_value=manifest))
        stack.enter_context(patch.object(runner, "reference_profile", return_value=profile))
        stack.enter_context(patch.object(runner, "asset_stats", return_value={"synthetic_stat": True}))
        stack.enter_context(patch.object(runner, "sdk_source_identity", return_value={"synthetic_sdk": "test"}))
        stack.enter_context(patch.object(runner, "private_root", side_effect=lambda output: output.mkdir()))
        stack.enter_context(patch.object(runner, "load_owned", side_effect=load))
        stack.enter_context(patch.object(runner, "validate_owned", return_value=binding.identity()))
        stack.enter_context(patch.object(runner, "observe_owned_backend", return_value=actual_backend))
        stack.enter_context(patch.object(runner, "SDKBinding", return_value=binding))
        stack.enter_context(patch.object(runner, "new_trial", side_effect=new_trial))
        return stack, sdk, preparation, reviewer

    def test_activation_refuses_before_loading_or_even_reading_missing_freeze(self):
        sdk = SimpleNamespace(Client=Mock())
        with self.assertRaisesRegex(ValueError, "activation required"):
            runner.execute(sdk, Path("absent"), "a" * 64, "b" * 64, Path("unused"))
        sdk.Client.assert_not_called()

    def test_capacity_delta_requires_actual_context_and_preserves_all_other_owners(self):
        with tempfile.TemporaryDirectory() as directory:
            binding = CohortBinding()
            stack, _, _, _ = self.environment(Path(directory), binding)
            with stack:
                parent = runner.reference_profile()
                saved = deepcopy(parent)
                backend = runner.observe_owned_backend(Path(directory))
                actual = runner.observed_capacity_profile(parent, binding.identity(), backend)
                self.assertEqual(parent, saved)
                self.assertEqual(actual["context"], 36864)
                self.assertEqual(actual["initial_identity"], binding.identity())
                self.assertEqual(actual["backend_observation"], backend)
                self.assertEqual(actual["requested_load"], {**parent["requested_load"], "contextLength": 36864,
                    "gpu": {**parent["requested_load"]["gpu"], "ratio": runner.GPU_RATIO}})
                self.assertEqual(actual["prediction_configuration"], parent["prediction_configuration"])
                self.assertEqual(sum(runner.INPUT_CAPS.values()), 77192)
                self.assertEqual([runner.model_limits(role).input_total for role in runner.ROLES],
                    [4096, 4096, 24000, 9000, 27000, 9000])
                for defect in ("old-context", "other-load", "placement", "template"):
                    identity, observation = binding.identity(), deepcopy(backend)
                    if defect == "old-context":
                        identity["model"]["contextLength"] = 32768
                    elif defect == "other-load":
                        identity["load"]["fields"][1]["value"] = "undeclared"
                    elif defect == "placement":
                        observation["flags"]["n-gpu-layers"] = "changed"
                    else:
                        observation["backend_template_sha256"] = "changed"
                    with self.subTest(defect=defect), self.assertRaises(ValueError):
                        runner.observed_capacity_profile(parent, identity, observation)

    def test_preflight_has_no_predictions_and_fit_source_drift_withholds_execution(self):
        with tempfile.TemporaryDirectory() as directory:
            root, binding = Path(directory), CohortBinding()
            stack, sdk, preparation, reviewer = self.environment(root, binding)
            with stack:
                output = root / "runtime"
                freeze = runner.prepare_runtime(sdk, preparation, reviewer, output)
                self.assertEqual(binding.calls, 0)
                self.assertEqual(freeze["prediction_attempts"], 0)
                self.assertEqual(len(freeze["fit"]), 6)
                self.assertTrue(all(fit["request_presentation"] == runner.SUPPLIED_REQUEST_PRESENTATION
                    for fit in freeze["fit"].values()))
                path = output / "freeze.json"
                checksum = digest(path.read_bytes())
                runner.verify_freeze(path, checksum)
                observed_path = output / "capacity-profile.json"
                observed = json.loads(observed_path.read_bytes())
                self.assertEqual(observed["initial_identity"], binding.identity())
                self.assertEqual(observed["context"], 36864)
                stale = json.loads(path.read_bytes())
                stale["fit"]["packet-a"]["request_presentation"] = "complete-supplied-evidence-report-only/1"
                stale_path = output / "stale-presentation-freeze.json"
                stale_path.write_bytes(json_bytes(stale))
                with self.assertRaisesRegex(ValueError, "presentation identity drift"):
                    runner.verify_freeze(stale_path, digest(stale_path.read_bytes()))
                (output / "packet-a/fit-rendered.txt").write_text("changed")
                with self.assertRaisesRegex(ValueError, "fit artifact drift"):
                    runner.verify_freeze(path, checksum)

    def test_capacity_profile_or_role_contract_drift_withholds_with_recomputed_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            root, binding = Path(directory), CohortBinding()
            stack, sdk, preparation, reviewer = self.environment(root, binding)
            with stack:
                output = root / "runtime"
                runner.prepare_runtime(sdk, preparation, reviewer, output)
                path = output / "freeze.json"
                original = json.loads(path.read_bytes())
                changed = deepcopy(original)
                changed["capacity_contract"]["input_caps"]["packet-a"] += 1
                path.write_bytes(json_bytes(changed))
                with self.assertRaisesRegex(ValueError, "drifted"):
                    runner.verify_freeze(path, digest(path.read_bytes()))
                profile_path = output / "capacity-profile.json"
                profile = json.loads(profile_path.read_bytes())
                profile["prediction_configuration"]["layers"][0]["config"]["fields"][0]["value"] = "undeclared"
                profile_path.write_bytes(json_bytes(profile))
                original["capacity_profile_sha256"] = digest(profile_path.read_bytes())
                path.write_bytes(json_bytes(original))
                with self.assertRaisesRegex(ValueError, "declared inheritance"):
                    runner.verify_freeze(path, digest(path.read_bytes()))

    def test_preflight_cap_failure_publishes_no_freeze_and_cleans_owned_runtime(self):
        with tempfile.TemporaryDirectory() as directory:
            root, binding = Path(directory), CohortBinding()
            binding.tokenize = lambda text: [1] * 5000
            stack, sdk, preparation, reviewer = self.environment(root, binding)
            with stack:
                output = root / "runtime"
                with self.assertRaisesRegex(ValueError, "input/context limits"):
                    runner.prepare_runtime(sdk, preparation, reviewer, output)
                self.assertEqual(binding.calls, 0)
                self.assertFalse((output / "freeze.json").exists())
                self.assertTrue(json.loads((output / "cleanup.json").read_bytes())["confirmed"])
                measurements = json.loads((output / "runtime-preflight.json").read_bytes())["fit"]
                self.assertEqual(len(measurements), 6)
                self.assertEqual(measurements["probe-cancel"]["rendered_tokens"], 5000)
                self.assertFalse(measurements["probe-cancel"]["input_cap_met"])

    def test_six_fixed_slots_run_once_without_reviewer_leakage_or_semantic_grading(self):
        with tempfile.TemporaryDirectory() as directory:
            root, binding = Path(directory), CohortBinding()
            stack, sdk, preparation, reviewer = self.environment(root, binding)
            with stack:
                runtime = root / "runtime"
                runner.prepare_runtime(sdk, preparation, reviewer, runtime)
                freeze = runtime / "freeze.json"
                checksum = digest(freeze.read_bytes())
                summary = runner.execute(sdk, freeze, checksum, checksum, root / "run")
            self.assertEqual(binding.calls, 6)
            self.assertEqual([row["role"] for row in summary["rows"]], list(runner.ROLES))
            self.assertEqual(summary["measured_known_usage"]["known_usage_attempts"], 6)
            self.assertEqual(summary["measured_known_usage"]["unknown_usage_attempts"], 0)
            self.assertEqual(summary["rows"][0]["execution"], "failed")
            self.assertEqual([row["execution"] for row in summary["rows"]][1:], ["completed"] * 5)
            self.assertTrue(all(row["semantic_acceptance"] == "not_evaluated" for row in summary["rows"]))
            self.assertNotIn("PRIVATE_REVIEWER_ANSWER", json.dumps(binding.inputs))

    def test_complete_overcontext_input_is_measured_without_omitting_required_events(self):
        with tempfile.TemporaryDirectory() as directory:
            root, binding = Path(directory), CohortBinding()
            binding.tokenize = lambda text: [1] * (30000 if "packet-a" in text else 10)
            stack, sdk, preparation, reviewer = self.environment(root, binding)
            with stack:
                output = root / "runtime"
                with self.assertRaisesRegex(ValueError, "input/context limits"):
                    runner.prepare_runtime(sdk, preparation, reviewer, output)
                evidence = json.loads((output / "runtime-preflight.json").read_bytes())
            self.assertEqual(binding.calls, 0)
            self.assertEqual(len(evidence["fit"]), 6)
            self.assertEqual(evidence["fit"]["packet-a"]["rendered_tokens"], 30000)
            self.assertFalse(evidence["fit"]["packet-a"]["context_reserve_met"])
            self.assertEqual(evidence["fit"]["packet-a"]["omitted_events"], [])
            self.assertTrue(evidence["fit"]["packet-a"]["reference_pairs"])
            self.assertTrue(evidence["fit"]["packet-d"]["preparation_termination_id"])

    def test_unknown_cancel_or_failed_reference_canary_withholds_every_later_slot(self):
        for defect, attempts in (("unknown_cancel", 1), ("no_canary_citation", 2), ("foreign_citation", 3)):
            with self.subTest(defect=defect), tempfile.TemporaryDirectory() as directory:
                root, binding = Path(directory), CohortBinding(defect)
                stack, sdk, preparation, reviewer = self.environment(root, binding)
                with stack:
                    runtime, output = root / "runtime", root / "run"
                    runner.prepare_runtime(sdk, preparation, reviewer, runtime)
                    freeze = runtime / "freeze.json"
                    checksum = digest(freeze.read_bytes())
                    with self.assertRaises(ValueError):
                        runner.execute(sdk, freeze, checksum, checksum, output)
                    summary = json.loads((output / "summary.json").read_bytes())
                self.assertEqual(binding.calls, attempts)
                self.assertTrue(all(row["execution"] == "unattempted" for row in summary["rows"][attempts:]))
                if defect == "unknown_cancel":
                    self.assertEqual(summary["measured_known_usage"]["unknown_usage_attempts"], 1)
                    self.assertEqual(summary["rows"][0]["unknown_usage_reservation"]["generated"], 8192)

    def test_operator_primary_survives_model_and_client_cleanup_failures_with_known_spend(self):
        with tempfile.TemporaryDirectory() as directory:
            root, binding = Path(directory), CohortBinding("operator_interrupt")
            stack, sdk, preparation, reviewer = self.environment(root, binding)
            with stack:
                runtime, output = root / "runtime", root / "run"
                runner.prepare_runtime(sdk, preparation, reviewer, runtime)
                freeze = runtime / "freeze.json"
                checksum = digest(freeze.read_bytes())
                # The preflight succeeded. Fail both cleanup owners only in execution.
                def unload_failure(model, *args, **kwargs):
                    raise OSError("model unload secondary")
                base_client = type(sdk.Client("test-only"))
                class NoisyClient(base_client):
                    def __exit__(self, *args):
                        raise OSError("client close secondary")
                with patch.object(runner, "finalize_owned_runtime", side_effect=unload_failure), patch.object(sdk, "Client", side_effect=lambda address: NoisyClient()):
                    with self.assertRaisesRegex(KeyboardInterrupt, "operator primary") as raised:
                        runner.execute(sdk, freeze, checksum, checksum, output)
                summary = json.loads((output / "summary.json").read_bytes())
            self.assertEqual(binding.calls, 2)
            self.assertIn("model unload secondary", " ".join(raised.exception.__notes__))
            self.assertIn("client close secondary", " ".join(raised.exception.__notes__))
            self.assertEqual(summary["measured_known_usage"]["known_usage_attempts"], 1)
            self.assertEqual(summary["measured_known_usage"]["unknown_usage_attempts"], 1)
            self.assertEqual(summary["measured_known_usage"]["input"], 10)
            self.assertIsNotNone(summary["rows"][1]["termination_id"])
