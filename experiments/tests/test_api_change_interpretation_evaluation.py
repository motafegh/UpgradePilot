"""Measured evaluation boundaries; no live inference or semantic oracle."""

import copy
import json
from dataclasses import replace
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import Mock, patch

from experiments.api_change_interpretation import (
    ASSETS,
    LOCAL_MODEL,
    OUTPUT_TOKENS,
    ProviderReply,
    prepare_request,
)
from experiments.api_change_interpretation_evaluation import (
    HISTORICAL_CONTEXT,
    calibration_source_input,
    execute_evaluation,
    measured_capacity,
    prepare_evaluation,
)


class EvaluationTests(TestCase):
    def setUp(self):
        self.inputs = json.loads((ASSETS / "source-inputs-v1.json").read_text())[
            "inputs"
        ]
        self.context = json.loads(HISTORICAL_CONTEXT.read_text())
        self.model = Mock()
        self.model.get_info.return_value.to_dict.return_value = {
            "identifier": LOCAL_MODEL,
            "modelKey": LOCAL_MODEL,
            "instanceReference": "controlled-instance",
            "path": "controlled-model.gguf",
        }
        self.model.get_context_length.return_value = 16384
        self.model.apply_prompt_template.return_value = "controlled formatted chat"
        self.model.tokenize.side_effect = lambda text: list(
            range(100 if text == "controlled formatted chat" else 30)
        )
        self.chat_factory = lambda history: history

    def test_all_frozen_maps_keep_source_scope_without_evaluator_answers(self):
        cases = json.loads((ASSETS / "evaluation-cases-v1.json").read_text())["cases"]
        for item, case in zip(self.inputs, cases, strict=True):
            mapped = calibration_source_input(item, self.context)
            self.assertEqual(bool(mapped["sections"]), case["inference_allowed"])
            for actual, frozen in zip(
                mapped["sections"], item["sections"], strict=True
            ):
                self.assertEqual(actual["lines"], frozen["lines"])
                self.assertEqual(actual["text"], frozen["text"])
            request = prepare_request(mapped)
            self.assertNotIn("required_propositions", json.dumps(request.payload))
            self.assertNotIn("forbidden_propositions", json.dumps(request.payload))
            if item["scope"]["mode"] != "acquired_window":
                self.assertFalse(mapped["source_coverage"]["complete_window_eligible"])
                self.assertIsNone(mapped["interval"]["proposed_version"])

    def test_corrupt_calibration_and_false_acquisition_are_rejected(self):
        for key, value in (
            ("sha256", "wrong"),
            ("end_offset", -1),
            ("section_id", "foreign"),
        ):
            item = copy.deepcopy(self.inputs[1])
            item["sections"][0][key] = value
            with self.assertRaises(ValueError):
                calibration_source_input(item, self.context)
        item = copy.deepcopy(self.inputs[1])
        item["scope"]["complete_window_eligible"] = True
        with self.assertRaises(ValueError):
            calibration_source_input(item, self.context)
        context = copy.deepcopy(self.context)
        context["upstream"]["revision"] = "wrong"
        with self.assertRaises(ValueError):
            calibration_source_input(self.inputs[0], context)

    def test_loaded_tokenizer_template_schema_and_reserve_measurement(self):
        request = prepare_request(
            calibration_source_input(self.inputs[0], self.context)
        )
        capacity, counts = measured_capacity(
            request,
            self.model,
            self.chat_factory,
            template_identity="controlled-template",
        )
        self.assertEqual(capacity.input_tokens, 130)
        self.assertEqual(capacity.reserved_output_tokens, OUTPUT_TOKENS)
        self.assertEqual(capacity.request_sha256, request.method["request_sha256"])
        self.assertEqual(capacity.deployment_identity, "controlled-instance")
        self.assertTrue(counts["fits"])
        self.assertEqual(self.model.tokenize.call_count, 2)
        pilot = prepare_request(request.source_input, max_output_tokens=1536)
        pilot_capacity, _ = measured_capacity(
            pilot,
            self.model,
            self.chat_factory,
            template_identity="controlled-template",
        )
        self.assertEqual(pilot_capacity.reserved_output_tokens, 1536)
        self.model.get_context_length.return_value = 1600
        _, counts = measured_capacity(
            request,
            self.model,
            self.chat_factory,
            template_identity="controlled-template",
        )
        self.assertFalse(counts["fits"])
        self.model.get_info.return_value.to_dict.return_value["modelKey"] = "different"
        with self.assertRaises(ValueError):
            measured_capacity(
                request,
                self.model,
                self.chat_factory,
                template_identity="controlled-template",
            )

    def prepared(self, output):
        return prepare_evaluation(
            output,
            self.model,
            self.chat_factory,
            template_identity="controlled-template",
        )

    def test_freeze_precedes_inference_and_does_not_overwrite_runs(self):
        with TemporaryDirectory() as root:
            path = Path(root) / "run"
            with patch(
                "experiments.api_change_interpretation_evaluation.LocalInterpretationProvider"
            ) as provider:
                cases, manifest, _ = self.prepared(path)
            provider.assert_not_called()
            self.assertEqual(len(cases), 19)
            self.assertFalse(manifest["model_outputs_seen"])
            self.assertTrue((path / "before-inference.json").exists())
            self.assertIsNone(cases[-1]["capacity"])
            with self.assertRaises(FileExistsError):
                self.prepared(path)

    def test_capacity_failure_never_enters_provider(self):
        with TemporaryDirectory() as root:
            cases, _, context = self.prepared(Path(root) / "run")
            cases[0]["counts"]["fits"] = False
            with patch(
                "experiments.api_change_interpretation_evaluation.LocalInterpretationProvider"
            ) as provider:
                result = execute_evaluation(
                    cases, Path(root) / "run", self.model, context
                )
            provider.assert_not_called()
            self.assertEqual(result["inference_attempts"], 0)
            self.assertEqual(result["state"], "capacity_problem")

    def test_changed_deployment_is_rejected_before_inference(self):
        with TemporaryDirectory() as root:
            path = Path(root) / "run"
            cases, _, context = self.prepared(path)
            cases[0]["capacity"] = replace(
                cases[0]["capacity"], deployment_identity="stale-instance"
            )
            with (
                patch(
                    "experiments.api_change_interpretation_evaluation.LocalInterpretationProvider"
                ) as provider,
                self.assertRaises(ValueError),
            ):
                execute_evaluation(cases, path, self.model, context)
            provider.assert_not_called()

    def test_provider_usage_over_allowance_stops_remaining_cases(self):
        with TemporaryDirectory() as root:
            path = Path(root) / "run"
            cases, _, context = self.prepared(path)
            fake = Mock(identity={"kind": "controlled_test"})
            fake.complete.return_value = ProviderReply(
                '{"observations":[],"unassessed":[]}'
            )

            def factory(**kwargs):
                kwargs["response_observer"](
                    200,
                    json.dumps(
                        {
                            "usage": {"prompt_tokens": 9999},
                            "choices": [{"finish_reason": "stop"}],
                        }
                    ).encode(),
                )
                return fake

            with patch(
                "experiments.api_change_interpretation_evaluation.LocalInterpretationProvider",
                side_effect=factory,
            ) as provider:
                result = execute_evaluation(cases, path, self.model, context)
            provider.assert_called_once()
            self.assertEqual(result["state"], "capacity_accounting_problem")
            self.assertEqual(len(result["results"]), 1)
            self.assertTrue(result["results"][0]["saved_recovery_equal"])
