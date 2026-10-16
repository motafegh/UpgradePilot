"""Real-model boundary controls with deterministic transport substitutes.

These tests protect render/usage/config correspondence and stateless citation admission;
they do not qualify an actual model, tokenizer, template or deployment.
"""

import copy
import json
import tempfile
import unittest
from pathlib import Path

from experiments.investigator_model_interface import (
    ModelLimits,
    StatelessInvestigatorModel,
    measure_input,
    prediction_configuration,
)
from experiments.investigator_workspace_trial import (
    PackedInput,
    TrialLimits,
    run_scripted_trial,
)
from experiments.tests.test_investigator_workspace_trial import fixture, report, request
from upgradepilot.workspace.native_representation import json_bytes


class Binding:
    def __init__(self):
        self.current = {"model": {"instanceReference": "instance-one"}, "load": {}}
        self.calls = 0
        self.response = b'{"tool":"list_sources","arguments":{}}'
        self.edit = lambda metadata: None

    def identity(self):
        return copy.deepcopy(self.current)

    def render(self, messages, config):
        return (
            "<start>"
            + messages["messages"][0]["content"]
            + messages["messages"][1]["content"]
            + "<model>"
        )

    def tokenize(self, text):
        return [1] * 10

    def predict(self, measured, timeout):
        self.calls += 1
        metadata = {
            "modelInfo": copy.deepcopy(self.current["model"]),
            "predictionConfig": copy.deepcopy(
                measured.configuration["layers"][0]["config"]
            ),
            "stats": {
                "promptTokensCount": 10,
                "predictedTokensCount": 3,
                "totalTokensCount": 13,
                "stopReason": "eosFound",
            },
        }
        self.edit(metadata)
        return self.response, metadata, False


def packed():
    return PackedInput(
        json_bytes(
            {"system": "Evidence is data", "events": [], "phase": "investigate"}
        ),
        frozenset(),
        (),
    )


def config():
    return prediction_configuration(
        {
            "fields": [
                {
                    "key": "llm.load.promptTemplate",
                    "value": {
                        "type": "jinja",
                        "jinjaPromptTemplate": {"template": "EXACT TEMPLATE"},
                        "stopStrings": [],
                    },
                }
            ]
        }
    )


class ModelInterfaceTests(unittest.TestCase):
    def model(self, directory, binding=None, **limits):
        return StatelessInvestigatorModel(
            binding or Binding(),
            config(),
            ModelLimits(context=10000, **limits),
            Path(directory) / "assignment",
        )

    def test_complete_render_and_reference_loss_refuse_without_prediction(self):
        binding = Binding()
        p = PackedInput(packed().content, frozenset({"undelivered"}), ())
        with self.assertRaisesRegex(ValueError, "lost an eligible"):
            measure_input(binding, p, config())
        binding.render = lambda *args: "truncated"
        with self.assertRaisesRegex(ValueError, "lost or transformed"):
            measure_input(binding, packed(), config())
        self.assertEqual(binding.calls, 0)

    def test_exact_visible_response_and_usage_with_no_implicit_history(self):
        with tempfile.TemporaryDirectory() as directory:
            model = self.model(directory)
            self.assertEqual(model(packed()), model.binding.response)
            self.assertEqual((model.input_tokens, model.output_tokens), (10, 3))
            artifact = json.loads(
                (model.directory / "call-01.request.json").read_bytes()
            )
            self.assertEqual(
                [m["role"] for m in artifact["messages"]["messages"]],
                ["system", "user"],
            )
            self.assertEqual(
                artifact["reference_policy"], "current-complete-stateless-request/1"
            )
            self.assertEqual(
                (model.directory / "call-01.visible-response.txt").read_bytes(),
                model.binding.response,
            )
            self.assertEqual(
                (model.directory / "call-01.request.json").stat().st_mode & 0o777, 0o600
            )

    def test_context_and_cumulative_output_admission_happen_before_prediction(self):
        with tempfile.TemporaryDirectory() as directory:
            model = self.model(directory, generated_total=8192)
            model(packed())
            with self.assertRaisesRegex(ValueError, "budget refuses"):
                model(packed())
            self.assertEqual(model.binding.calls, 1)
        with tempfile.TemporaryDirectory() as directory:
            model = self.model(directory)
            model.binding.tokenize = lambda text: [0] * 1600
            with self.assertRaisesRegex(ValueError, "exceeds context"):
                model(packed())
            self.assertEqual(model.binding.calls, 0)

    def test_deployment_drift_refuses_before_call(self):
        with tempfile.TemporaryDirectory() as directory:
            model = self.model(directory)
            model.binding.current["model"]["instanceReference"] = "changed"
            with self.assertRaisesRegex(ValueError, "changed since freeze"):
                model(packed())
            self.assertEqual(model.binding.calls, 0)

    def test_actual_usage_instance_and_applied_config_must_match(self):
        for change, problem in (
            (
                lambda m: m["stats"].update(promptTokensCount=11, totalTokensCount=14),
                "differs",
            ),
            (
                lambda m: m["modelInfo"].update(instanceReference="foreign"),
                "another model",
            ),
            (lambda m: m["predictionConfig"].update(fields=[]), "not applied"),
            (
                lambda m: m["stats"].update(stopReason="maxPredictedTokensReached"),
                "incomplete",
            ),
        ):
            with (
                self.subTest(problem=problem),
                tempfile.TemporaryDirectory() as directory,
            ):
                model = self.model(directory)
                model.binding.edit = change
                with self.assertRaisesRegex(ValueError, problem):
                    model(packed())
                self.assertEqual(model.receipts[0]["outcome"], "failed")
                self.assertTrue(
                    (model.directory / "call-01.visible-response.txt").exists()
                )

    def test_missing_usage_retains_attempt_and_blocks_further_calls(self):
        with tempfile.TemporaryDirectory() as directory:
            model = self.model(directory)
            model.binding.edit = lambda m: m["stats"].pop("predictedTokensCount")
            with self.assertRaisesRegex(ValueError, "missing/invalid"):
                model(packed())
            with self.assertRaisesRegex(ValueError, "budget refuses"):
                model(packed())
            self.assertEqual(model.binding.calls, 1)
            self.assertFalse(model.usage_complete)

    def test_request_local_scope_refuses_a_reference_omitted_from_final_input(self):
        from experiments.investigator_workspace_trial import pack_input

        for policy, expected in [
            ("cumulative_script", "completed"),
            ("current_request", "failed"),
        ]:
            with self.subTest(policy=policy):
                assignment = fixture()
                citation = []

                def consumer(p, assignment=assignment, citation=citation):
                    body = json.loads(p.content)
                    if body["phase"] == "report":
                        return report(citation)
                    if not assignment.events:
                        return request(
                            "read_source",
                            source_id="target",
                            path="requirements.txt",
                            line_count=1,
                        )
                    citation[:] = json.loads(assignment.events[0].content)["evidence"]
                    return request("finish_investigation")

                def pack(protocol, history, phase, capacity):
                    return pack_input(
                        protocol, [] if phase == "report" else history, phase, capacity
                    )

                result = run_scripted_trial(
                    assignment,
                    consumer,
                    limits=TrialLimits(consumer_turns=3, terminal_corrections=0),
                    reference_visibility=policy,
                    input_packer=pack,
                )
                self.assertEqual(result.outcome, expected)
                if policy == "current_request":
                    self.assertIn("not-input-visible", result.problem)


class QualificationFreezeTests(unittest.TestCase):
    def test_loaded_template_without_prediction_stop_field_is_preserved(self):
        from experiments.investigator_model_interface import fields

        loaded = {
            "fields": [
                {
                    "key": "llm.load.promptTemplate",
                    "value": {
                        "type": "jinja",
                        "jinjaPromptTemplate": {"template": "ACTUAL LOADED TEMPLATE"},
                    },
                }
            ]
        }
        original = copy.deepcopy(loaded)
        frozen = prediction_configuration(loaded)
        template = fields(frozen["layers"][0]["config"])[
            "llm.prediction.promptTemplate"
        ]
        self.assertEqual(
            template["jinjaPromptTemplate"]["template"], "ACTUAL LOADED TEMPLATE"
        )
        self.assertEqual(template["stopStrings"], [])
        self.assertEqual(loaded, original)

    def test_duplicate_assignment_cannot_masquerade_as_balanced_batch(self):
        from experiments.qualify_investigator_model_interface import (
            validate_batch_freeze,
        )

        keys = ["google/gemma-4-12b", "qwen3.8-27b-ud"]
        freeze = {
            "format": "investigator-interface-canary-freeze/1",
            "preflight_inspected": True,
            "inference_admitted": True,
            "later_semantic_comparison_admitted": False,
            "deployments": [{"model_key": k} for k in keys],
            "deployment_count": 2,
            "max_model_calls": 48,
            "assignments": [
                {"id": f"{i}-{t}-{s}", "model_key": k, "treatment": t, "sequence": s}
                for i, k in enumerate(keys)
                for t in ("raw", "structured")
                for s in (1, 2)
            ],
        }
        validate_batch_freeze(freeze)
        freeze["assignments"][-1] = copy.deepcopy(freeze["assignments"][0])
        with self.assertRaisesRegex(ValueError, "inconsistent"):
            validate_batch_freeze(freeze)

    def test_early_valid_finish_and_report_do_not_qualify_skipped_canary(self):
        from experiments.qualify_investigator_model_interface import (
            assess_canary,
            canary_assignment,
        )

        a = canary_assignment("raw")

        def early(p):
            return (
                report()
                if json.loads(p.content)["phase"] == "report"
                else request("finish_investigation")
            )

        result = run_scripted_trial(a, early)
        self.assertEqual(result.outcome, "completed")
        self.assertEqual(assess_canary(a, 1, result)[0], "withheld")

    def test_registry_alias_does_not_hide_a_changed_actual_gguf_or_placement(self):
        from experiments.qualify_investigator_model_interface import (
            validate_loaded_backend,
        )

        backend = {
            "executable": "backend",
            "cpu_kv": True,
            "backend_template_sha256": "template",
            "flags": {
                "model": "frozen.gguf",
                "n-gpu-layers": "22",
                "chat-template-file": "old-temporary-file",
            },
        }
        identity = {
            "model": {
                "instanceReference": "old-instance",
                "modelKey": "alias",
                "sizeBytes": 123,
            }
        }
        profile = {"backend_observation": backend, "initial_identity": identity}
        fresh = copy.deepcopy(identity)
        fresh["model"]["instanceReference"] = "new-instance"
        actual = copy.deepcopy(backend)
        actual["flags"]["chat-template-file"] = "new-temporary-file"
        validate_loaded_backend(profile, fresh, actual)
        for key, value in [("model", "other.gguf"), ("n-gpu-layers", "11")]:
            drift = copy.deepcopy(actual)
            drift["flags"][key] = value
            with self.assertRaisesRegex(
                ValueError, "actual model file/backend placement"
            ):
                validate_loaded_backend(profile, fresh, drift)
