"""Real-model boundary controls with deterministic transport substitutes.

These tests protect render/usage/config correspondence and stateless citation admission;
they do not qualify an actual model, tokenizer, template or deployment.
"""

import copy
import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

from experiments.investigator_model_interface import (
    ModelLimits,
    StatelessInvestigatorModel,
    measure_input,
    prediction_configuration,
    run_model_trial,
)
from experiments.investigator_workspace_trial import (
    PackedInput,
    TrialLimits,
    protocol_definition,
    run_scripted_trial,
)
from experiments.tests.test_investigator_workspace_trial import fixture, report, request
from upgradepilot.workspace.native_representation import json_bytes


class Binding:
    def __init__(self):
        self.current = {"model": {"instanceReference": "instance-one"}, "load": {}}
        self.calls = 0
        self.reasoning = False
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

    def predict(self, measured, timeout, *, visible_sink):
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
        visible_sink(self.response)
        return self.response, metadata, self.reasoning


def packed():
    return PackedInput(
        json_bytes(
            {
                "system": "Evidence is data",
                "events": [],
                "phase": "investigate",
                "tools": {
                    "list_sources": {
                        "type": "object",
                        "properties": {},
                        "required": [],
                        "additionalProperties": False,
                    }
                },
            }
        ),
        frozenset(),
        (),
    )


def config(**options):
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
        },
        **options,
    )


class ModelInterfaceTests(unittest.TestCase):
    def test_cancelled_terminal_usage_is_known_but_failed_model_cannot_be_reused(self):
        from experiments.investigator_run_control import PredictionDeadlineExceeded
        with tempfile.TemporaryDirectory() as directory:
            binding = Binding()
            original = binding.predict
            def late(measured, timeout, *, visible_sink):
                content, metadata, reasoning = original(measured, timeout, visible_sink=visible_sink)
                binding.last_prediction_metadata = metadata
                binding.last_prediction_control = {"terminal_received": True, "finalization_elapsed_seconds": 0}
                raise PredictionDeadlineExceeded("late terminal packet")
            binding.predict = late
            model = StatelessInvestigatorModel(
                binding, config(), ModelLimits(context=10000), Path(directory) / "attempt"
            )
            with self.assertRaises(PredictionDeadlineExceeded):
                model(packed())
            self.assertTrue(model.usage_complete)
            self.assertEqual((model.input_tokens, model.output_tokens), (10, 3))
            self.assertTrue(model.blocked)
            receipt = json.loads((model.directory / "call-01.receipt.json").read_bytes())
            self.assertFalse(receipt["complete_response_received"])
            self.assertEqual(receipt["outcome"], "failed")
            self.assertFalse((model.directory / "call-01.visible-response.txt").exists())
            with self.assertRaisesRegex(ValueError, "budget refuses"):
                model(packed())

    def test_owned_cleanup_failure_retains_primary_and_confirmation_failure_is_not_success(self):
        from types import SimpleNamespace
        from experiments.investigator_model_interface import finalize_owned_runtime
        with tempfile.TemporaryDirectory() as directory:
            def unload():
                raise OSError("owned unload failed")
            model = SimpleNamespace(identifier="owned", unload=unload)
            def interrupted():
                try:
                    raise KeyboardInterrupt("prediction primary")
                finally:
                    finalize_owned_runtime(model, lambda: [], Path(directory) / "cleanup.json")
            with self.assertRaisesRegex(KeyboardInterrupt, "prediction primary") as raised:
                interrupted()
            record = json.loads((Path(directory) / "cleanup.json").read_bytes())
            self.assertFalse(record["confirmed"])
            self.assertIn("owned unload failed", raised.exception.__notes__[0])
            model.unload = lambda: None
            with self.assertRaisesRegex(ValueError, "unconfirmed"):
                finalize_owned_runtime(model, lambda: [model], Path(directory) / "unconfirmed.json")

    def test_keyboard_interrupt_keeps_unknown_attempt_and_primary_after_fsync_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            binding = Binding()
            def interrupted(measured, timeout, *, visible_sink):
                visible_sink(b'{"claims":')
                raise KeyboardInterrupt("operator stop")
            binding.predict = interrupted
            model = StatelessInvestigatorModel(
                binding, config(), ModelLimits(context=10000), Path(directory) / "attempt"
            )
            with patch("experiments.investigator_model_interface.os.fsync", side_effect=OSError("fsync failed")):
                with self.assertRaisesRegex(KeyboardInterrupt, "operator stop"):
                    model(packed())
            receipt = json.loads((model.directory / "call-01.receipt.json").read_bytes())
            self.assertIn("KeyboardInterrupt", receipt["problem"])
            self.assertIn("OSError: fsync failed", receipt["secondary_problems"])
            self.assertIsNone(receipt["usage"])
            self.assertEqual(receipt["reserved_generated_tokens"], 8192)
            self.assertFalse(model.usage_complete)
            with self.assertRaisesRegex(ValueError, "budget refuses"):
                model(packed())

    def test_missing_receipt_keeps_reservation_and_does_not_mask_primary(self):
        from experiments.investigator_model_interface import private_write
        with tempfile.TemporaryDirectory() as directory:
            model = StatelessInvestigatorModel(
                Binding(), config(), ModelLimits(context=10000), Path(directory) / "attempt"
            )
            def interrupted(*args, **kwargs):
                raise KeyboardInterrupt("primary")
            def write(path, content):
                if path.name.endswith(".receipt.json"):
                    raise OSError("receipt disk failed")
                return private_write(path, content)
            model.binding.predict = interrupted
            with patch("experiments.investigator_model_interface.private_write", side_effect=write):
                with self.assertRaisesRegex(KeyboardInterrupt, "primary"):
                    model(packed())
            self.assertTrue((model.directory / "call-01.attempt.json").exists())
            self.assertFalse((model.directory / "call-01.receipt.json").exists())
            self.assertIn("OSError: receipt disk failed", model.receipts[0]["secondary_problems"])
            self.assertTrue(model.blocked)

    def test_nonempty_citation_schema_is_exact_in_runtime_configuration(self):
        from experiments.investigator_model_interface import fields
        from experiments.investigator_workspace_trial import pack_input
        from experiments.tests.test_investigator_workspace_trial import schema_pairs

        for treatment in ("raw", "structured"):
            a = fixture(treatment)
            e = a.invoke(
                request("read_source", source_id="target", path="requirements.txt")
            )
            problem = a.invoke(
                request("read_source", source_id="target", path="missing.txt")
            )
            for phase in ("investigate", "report"):
                p = pack_input(
                    protocol_definition(a, TrialLimits()),
                    [e, problem],
                    phase,
                    128 * 1024,
                )
                measured = measure_input(Binding(), p, config())
                schema = fields(measured.configuration["layers"][0]["config"])[
                    "llm.prediction.structured"
                ]["jsonSchema"]
                if phase == "report":
                    self.assertEqual(
                        schema_pairs(schema["properties"]["recommendation_evidence"]),
                        p.reference_pairs,
                    )
                else:
                    note = next(
                        b
                        for b in schema["anyOf"]
                        if b["properties"]["tool"]["enum"] == ["record_note"]
                    )
                    self.assertEqual(
                        schema_pairs(
                            note["properties"]["arguments"]["properties"]["evidence"]
                        ),
                        p.reference_pairs,
                    )

    def test_token_repacking_keeps_one_budget_snapshot_and_drops_omitted_authority(
        self,
    ):
        from experiments.investigator_workspace_trial import protocol_definition

        assignment = fixture()
        event = assignment.invoke(
            request("read_source", source_id="target", path="requirements.txt")
        )
        ticks = iter([0, 1])
        with tempfile.TemporaryDirectory() as directory:
            binding = Binding()
            binding.tokenize = lambda text: (
                [0] * (2000 if "pytest==9.0.3" in text else 10)
            )
            model = StatelessInvestigatorModel(
                binding,
                config(),
                ModelLimits(context=10000),
                Path(directory) / "assignment",
                clock=lambda: next(ticks),
            )
            packed = model.pack(
                protocol_definition(assignment, TrialLimits()),
                [event],
                "report",
                128 * 1024,
            )
            self.assertEqual(packed.omitted_event_ids, (event.event_id,))
            self.assertFalse(packed.reference_ids)
            budget = json.loads(packed.content)["budget_observation"]
            self.assertEqual(
                budget["model"]["remaining_before_this_request"]["seconds_at_snapshot"],
                14399,
            )
            self.assertEqual(binding.calls, 0)

    def test_live_budgets_follow_refused_calls_and_override_frozen_task_counters(self):
        assignment = fixture()
        snapshots = []

        class BudgetBinding(Binding):
            def predict(binding, measured, timeout, *, visible_sink):
                body = json.loads(measured.packed.content)
                snapshots.append(body["budget_observation"])
                if len(snapshots) == 1:
                    binding.response = request("unoffered_tool")
                elif len(snapshots) == 2:
                    binding.response = request(
                        "read_source", source_id="target", path="requirements.txt"
                    )
                elif len(snapshots) == 3:
                    binding.response = request("finish_investigation")
                else:
                    refs = [
                        assignment.references[r].wire()
                        for r in measured.packed.reference_ids
                    ]
                    binding.response = report(refs)
                return super().predict(measured, timeout, visible_sink=visible_sink)

        with tempfile.TemporaryDirectory() as directory:
            model = self.model(directory, binding=BudgetBinding(), calls=4)
            frozen = protocol_definition(assignment, TrialLimits())
            frozen["budget_observation"]["trial_remaining"]["operation_units"] = 99999
            result = run_model_trial(
                assignment, model, limits=TrialLimits(consumer_turns=4), protocol=frozen
            )
            self.assertEqual(result.outcome, "completed")
            self.assertEqual(
                [s["trial_remaining"]["operation_units"] for s in snapshots],
                [48, 47, 43, 40],
            )
            self.assertEqual(
                [
                    s["trial_remaining"]["invocations_including_this_request"]
                    for s in snapshots
                ],
                [4, 3, 2, 1],
            )
            self.assertEqual(snapshots[1]["trial_remaining"]["corrections"], 1)
            self.assertEqual(
                [
                    s["model"]["remaining_before_this_request"][
                        "calls_including_this_request"
                    ]
                    for s in snapshots
                ],
                [4, 3, 2, 1],
            )
            self.assertEqual(
                [
                    s["model"]["remaining_before_this_request"]["input_tokens"]
                    for s in snapshots
                ],
                [524288, 524278, 524268, 524258],
            )
            self.assertEqual(result.charges["admission_operations"], 14)
            saved = json.loads(
                (model.directory / "call-04.packed-input.json").read_bytes()
            )
            self.assertEqual(saved["budget_observation"], snapshots[-1])
            other = protocol_definition(fixture(), TrialLimits())
            self.assertEqual(
                other["budget_observation"]["trial_remaining"]["operation_units"], 48
            )

    def model(self, directory, binding=None, **limits):
        return StatelessInvestigatorModel(
            binding or Binding(),
            config(),
            ModelLimits(context=10000, **limits),
            Path(directory) / "assignment",
        )

    def test_complete_render_and_reference_loss_refuse_without_prediction(self):
        binding = Binding()
        p = PackedInput(
            packed().content, frozenset({("source_line", "undelivered")}), ()
        )
        with self.assertRaisesRegex(ValueError, "lost an eligible"):
            measure_input(binding, p, config())
        binding.render = lambda *args: "truncated"
        with self.assertRaisesRegex(ValueError, "lost or transformed"):
            measure_input(binding, packed(), config())
        self.assertEqual(binding.calls, 0)

    def test_reasoning_fragments_require_explicit_and_applied_on_mode(self):
        for enabled in (False, True):
            with (
                self.subTest(enabled=enabled),
                tempfile.TemporaryDirectory() as directory,
            ):
                binding = Binding()
                binding.reasoning = True
                model = StatelessInvestigatorModel(
                    binding,
                    config(reasoning=enabled),
                    ModelLimits(context=10000),
                    Path(directory) / "assignment",
                )
                if enabled:
                    self.assertEqual(model(packed()), binding.response)
                    receipt = json.loads(
                        (model.directory / "call-01.receipt.json").read_bytes()
                    )
                    self.assertTrue(receipt["reasoning_fragment_observed"])
                else:
                    with self.assertRaisesRegex(ValueError, "reasoning-off"):
                        model(packed())
        with tempfile.TemporaryDirectory() as directory:
            binding = Binding()
            binding.reasoning = True

            def mismatch(metadata):
                for setting in metadata["predictionConfig"]["fields"]:
                    if setting["key"] == "llm.prediction.reasoning.enableThinking":
                        setting["value"] = False

            binding.edit = mismatch
            model = StatelessInvestigatorModel(
                binding,
                config(reasoning=True),
                ModelLimits(context=10000),
                Path(directory) / "assignment",
            )
            with self.assertRaisesRegex(ValueError, "not applied"):
                model(packed())

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
                artifact["reference_policy"], "current-complete-stateless-request/2"
            )
            self.assertEqual(
                (model.directory / "call-01.visible-response.txt").read_bytes(),
                model.binding.response,
            )
            self.assertEqual(
                (model.directory / "call-01.packed-input.json").read_bytes(),
                packed().content,
            )
            self.assertEqual(
                (model.directory / "call-01.request.json").stat().st_mode & 0o777, 0o600
            )

    def test_exact_observation_text_is_visible_once_after_fixed_task(self):
        from experiments.investigator_workspace_trial import (
            pack_input,
            protocol_definition,
        )

        assignment = fixture("raw")
        protocol = protocol_definition(assignment, TrialLimits())
        protocol["task"]["goal"] = 'Inspect the quoted "version" without changing it.'
        event = assignment.invoke(
            request("read_source", source_id="target", path="requirements.txt")
        )
        p = pack_input(protocol, [event], "investigate", 128 * 1024)
        measured = measure_input(Binding(), p, config())
        user = measured.messages["messages"][1]["content"]
        observation = event.content.decode()
        # Protect model-visible readability and exact retained bytes, not one JSON
        # indentation or header spelling. The old doubly escaped envelope fails here.
        self.assertIn(observation, user)
        self.assertEqual(user.count(observation), 1)
        self.assertLess(
            user.index(json_bytes(protocol["task"]).decode()), user.index(observation)
        )
        self.assertTrue(all(ref in user for ref in p.reference_ids))
        self.assertEqual(json.loads(p.content)["events"][0]["content"], observation)

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

    def test_stateless_history_keeps_actual_arguments_without_granting_requested_evidence(
        self,
    ):
        from experiments.investigator_workspace_trial import (
            pack_input,
            protocol_definition,
        )
        from experiments.qualify_investigator_model_interface import canary_assignment

        a = canary_assignment("raw")
        action = request("read_source", source_id="canary", path="missing.txt")
        missing = a.invoke(action)
        # The actual problem observation does not identify the requested path.
        # Complete stateless history must retain the original intent separately.
        self.assertNotIn("missing.txt", missing.content.decode())
        self.assertEqual(missing.request_text, action.decode())
        forged = a.invoke(
            request(
                "read_source",
                source_id="canary",
                path="probe.txt",
                evidence=[{"id": "forged-reference", "kind": "source_line"}],
            )
        )
        self.assertEqual(forged.outcome, "refused")
        p = pack_input(
            protocol_definition(a, TrialLimits()),
            [missing, forged],
            "investigate",
            128 * 1024,
        )
        user = measure_input(Binding(), p, config()).messages["messages"][1]["content"]
        self.assertIn(action.decode(), user)
        self.assertIn(missing.content.decode(), user)
        self.assertIn("forged-reference", user)
        self.assertNotIn("forged-reference", p.reference_ids)
        self.assertEqual(
            json.loads(p.content)["events"][0]["request_text"], action.decode()
        )

    def test_final_turn_report_refusal_keeps_its_reason_without_another_request(self):
        a = fixture("raw")
        responses = iter([request("finish_investigation"), b"{}"])
        result = run_scripted_trial(
            a, lambda p: next(responses), limits=TrialLimits(consumer_turns=2)
        )
        self.assertIsNone(result.report_publication)
        self.assertEqual(result.charges["report_refusals"][0]["consumer_attempt"], 2)
        self.assertTrue(result.charges["report_refusals"][0]["detail"])
        self.assertEqual(result.charges["terminal_corrections"], 1)

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
            assignment = fixture()
            observed = model.pack(
                protocol_definition(assignment, TrialLimits()), [], "report", 128 * 1024
            )
            budget = json.loads(observed.content)["budget_observation"]["model"]
            self.assertIsNone(budget["remaining_before_this_request"]["input_tokens"])
            self.assertIsNone(
                budget["remaining_before_this_request"]["generated_tokens"]
            )

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
    def test_unknown_usage_stops_the_entire_frozen_qualification_cohort(self):
        from types import SimpleNamespace
        from unittest.mock import patch

        from experiments.qualify_investigator_model_interface import (
            code_hashes,
            digest,
            execute_frozen,
        )

        loaded = []
        binding = Binding()
        binding.edit = lambda meta: meta["stats"].pop("predictedTokensCount")
        keys = ["gemma-4-e2b-it", "gemma-4-e4b-it-ud"]

        class Download:
            def __init__(self, key):
                self.model_key = key

            def load_new_instance(self, **kwargs):
                loaded.append(self.model_key)
                return SimpleNamespace(unload=lambda: None)

        class Client:
            def __init__(self, *args):
                self.llm = SimpleNamespace(
                    list_loaded=list,
                    list_downloaded=lambda: [Download(k) for k in keys],
                )

            def __enter__(self):
                return self

            def __exit__(self, *args):
                return False

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            deployments = []
            for n, k in enumerate(keys):
                profile = {
                    "model_key": k,
                    "identifier": str(n),
                    "requested_load": {},
                    "prediction_configuration": config(),
                    "tokenizer_policy": {},
                    "context": 10000,
                    "initial_identity": binding.identity(),
                }
                content = json_bytes(profile)
                path = root / f"profile-{n}.json"
                path.write_bytes(content)
                deployments.append(
                    {
                        "model_key": k,
                        "profile_path": str(path),
                        "profile_sha256": digest(content),
                    }
                )
            freeze = {
                "format": "investigator-interface-canary-freeze/2",
                "reference_schema_policy": "investigator-request-local-reference-schema/1",
                "preflight_inspected": True,
                "inference_admitted": True,
                "later_semantic_comparison_admitted": False,
                "deployments": deployments,
                "deployment_count": 2,
                "max_model_calls": 48,
                "calls_per_sequence": 6,
                "prior_spent_calls": 0,
                "cycle_call_ceiling": 48,
                "assignments": [
                    {
                        "id": f"{n}-{t}-{s}",
                        "model_key": k,
                        "treatment": t,
                        "sequence": s,
                    }
                    for n, k in enumerate(keys)
                    for s in (1, 2)
                    for t in ("raw", "structured")
                ],
                "code_sha256": code_hashes(),
                "immutable_files": [],
                "continue_independent_sequences_after_failure": True,
            }
            content = json_bytes(freeze)
            path = root / "freeze.json"
            path.write_bytes(content)
            with (
                patch(
                    "experiments.qualify_investigator_model_interface.SDKBinding",
                    return_value=binding,
                ),
                patch(
                    "experiments.qualify_investigator_model_interface.observe_owned_backend",
                    return_value={},
                ),
                patch(
                    "experiments.qualify_investigator_model_interface.validate_loaded_backend"
                ),
            ):
                rows = execute_frozen(
                    SimpleNamespace(Client=Client),
                    path,
                    digest(content),
                    root / "results",
                )
            self.assertEqual(loaded, [keys[0]])
            self.assertEqual(binding.calls, 1)
            self.assertEqual(sum(r["model_attempts"] for r in rows), 1)
            self.assertFalse(rows[0]["usage_complete"])
            self.assertTrue(
                all(r["disposition"] == "withheld_before_call" for r in rows[1:])
            )

    def test_all_pair_first_patterns_enforce_inverse_case_balance(self):
        from itertools import product

        from experiments.run_investigator_semantic_comparison import (
            validate_case_balance,
            validate_schedule,
        )

        accepted = []
        for bits in product((False, True), repeat=6):
            rows = []
            for m in range(3):
                for c in range(2):
                    first = "raw" if bits[2 * m + c] else "structured"
                    for t in (first, "structured" if first == "raw" else "raw"):
                        rows.append(
                            {
                                "id": f"{m}-{c}-{t}",
                                "model_key": str(m),
                                "case_id": str(c),
                                "treatment": t,
                            }
                        )
            valid = all(bits[2 * m] != bits[2 * m + 1] for m in range(3)) and sum(
                bits[2 * m] for m in range(3)
            ) in (1, 2)
            if valid:
                validate_schedule(rows, ["0", "1", "2"], ["0", "1"])
                counts = {
                    str(c): sum(bits[2 * m + c] for m in range(3)) for c in range(2)
                }
                balance = {
                    "format": "investigator-semantic-treatment-first-balance/1",
                    "raw_first_by_case": counts,
                }
                validate_case_balance(rows, ["0", "1"], balance)
                with self.assertRaisesRegex(ValueError, "named-case"):
                    validate_case_balance(
                        rows,
                        ["0", "1"],
                        {
                            **balance,
                            "raw_first_by_case": {
                                "0": 3 - counts["0"],
                                "1": 3 - counts["1"],
                            },
                        },
                    )
                accepted.append(bits)
            else:
                with self.assertRaises(ValueError):
                    validate_schedule(rows, ["0", "1", "2"], ["0", "1"])
        self.assertEqual(len(accepted), 6)

    def test_semantic_schedule_requires_every_pair_and_balanced_first_treatments(self):
        from experiments.run_investigator_semantic_comparison import validate_schedule

        assignments = []
        for m in range(3):
            for c in range(2):
                first = "raw" if (m + c) % 2 == 0 else "structured"
                for t in (first, "structured" if first == "raw" else "raw"):
                    assignments.append(
                        {
                            "id": f"m{m}-c{c}-{t}",
                            "model_key": str(m),
                            "case_id": str(c),
                            "treatment": t,
                        }
                    )
        validate_schedule(assignments, ["0", "1", "2"], ["0", "1"])
        with self.assertRaisesRegex(ValueError, "incomplete/duplicate"):
            validate_schedule(
                assignments[:-1] + [assignments[0]], ["0", "1", "2"], ["0", "1"]
            )
        biased = sorted(assignments, key=lambda a: a["treatment"] != "raw")
        with self.assertRaisesRegex(ValueError, "unbalanced"):
            validate_schedule(biased, ["0", "1", "2"], ["0", "1"])

    def test_semantic_admission_binds_original_calls_results_profiles_and_receipt(self):
        from unittest.mock import patch

        from experiments.qualify_investigator_model_interface import code_hashes, digest
        from experiments.run_investigator_semantic_comparison import (
            create_admission_receipt,
            require_qualification,
        )

        policy = "investigator-request-local-reference-schema/1"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            results = root / "results"
            results.mkdir()
            assignment = {"id": "new-raw-short", "model_key": "point"}
            deployments = [{"model_key": "point", "profile_sha256": "exact"}]
            content = json_bytes(
                {
                    "format": "investigator-interface-canary-freeze/2",
                    "reference_schema_policy": policy,
                    "code_sha256": code_hashes(),
                    "assignments": [assignment],
                    "deployments": deployments,
                }
            )
            (root / "freeze.json").write_bytes(content)
            freeze = {
                "deployments": deployments,
                "reference_schema_policy": policy,
                "admission_receipt": {
                    "path": str(root / "admit.json"),
                    "index_path": str(root / "index.json"),
                },
                "interface_qualification": {
                    "freeze_path": str(root / "freeze.json"),
                    "freeze_sha256": digest(content),
                    "results_root": str(results),
                },
            }
            row = {"assignment": assignment, "disposition": "withheld"}

            def write_summary():
                (results / "summary.json").write_bytes(
                    json_bytes({"assignments": [row]})
                )

            write_summary()
            with self.assertRaisesRegex(ValueError, "matrix did not qualify"):
                require_qualification(freeze, "semantic-hash")
            binding = Binding()
            model = StatelessInvestigatorModel(
                binding,
                config(),
                ModelLimits(context=10000),
                results / assignment["id"],
            )
            model(packed())
            row.update(
                disposition="qualified",
                usage_complete=True,
                outcome="completed",
                model_attempts=1,
                known_input_tokens=10,
                known_generated_tokens=3,
            )
            write_summary()
            with self.assertRaises(FileNotFoundError):
                require_qualification(freeze, "semantic-hash")
            with patch(
                "experiments.run_investigator_semantic_comparison.verify_freeze",
                return_value=(freeze, {}),
            ):
                self.assertEqual(
                    create_admission_receipt(root / "semantic.json", "semantic-hash")[
                        "disposition"
                    ],
                    "permitted",
                )
                with self.assertRaises(FileExistsError):
                    create_admission_receipt(root / "semantic.json", "semantic-hash")
            require_qualification(freeze, "semantic-hash")
            with self.assertRaisesRegex(ValueError, "receipt/artifact mismatch"):
                require_qualification(freeze, "foreign-freeze-hash")
            (results / "unexpected.txt").write_text("new artifact")
            with self.assertRaisesRegex(ValueError, "receipt/artifact mismatch"):
                require_qualification(freeze, "semantic-hash")
            (results / "unexpected.txt").unlink()
            freeze["deployments"] = [
                {"model_key": "point", "profile_sha256": "different"}
            ]
            with self.assertRaisesRegex(ValueError, "profile/configuration mismatch"):
                require_qualification(freeze, "semantic-hash")
            freeze["deployments"] = deployments
            mp = results / assignment["id"] / "call-01.metadata.json"
            meta = json.loads(mp.read_bytes())
            meta["modelInfo"]["instanceReference"] = "foreign"
            mp.write_bytes(json_bytes(meta))
            with self.assertRaisesRegex(ValueError, "artifact/configuration mismatch"):
                require_qualification(freeze, "semantic-hash")
            from types import SimpleNamespace

            from experiments.run_investigator_semantic_comparison import (
                execute_comparison,
            )

            with (
                patch(
                    "experiments.run_investigator_semantic_comparison.verify_freeze",
                    return_value=(freeze, {}),
                ),
                self.assertRaises(ValueError),
            ):
                execute_comparison(
                    SimpleNamespace(
                        Client=lambda *args: self.fail("must not load before admission")
                    ),
                    root / "semantic.json",
                    "semantic-hash",
                    root / "semantic-output",
                )
            self.assertFalse((root / "semantic-output").exists())

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
            CANDIDATES,
            validate_batch_freeze,
        )

        keys = list(CANDIDATES)
        freeze = {
            "format": "investigator-interface-canary-freeze/2",
            "reference_schema_policy": "investigator-request-local-reference-schema/1",
            "preflight_inspected": True,
            "inference_admitted": True,
            "later_semantic_comparison_admitted": False,
            "deployments": [{"model_key": k} for k in keys],
            "deployment_count": 6,
            "max_model_calls": 144,
            "calls_per_sequence": 6,
            "prior_spent_calls": 0,
            "cycle_call_ceiling": 144,
            "assignments": [
                {"id": f"{i}-{t}-{s}", "model_key": k, "treatment": t, "sequence": s}
                for i, k in enumerate(keys)
                for t in ("raw", "structured")
                for s in (1, 2)
            ],
        }
        validate_batch_freeze(freeze)
        freeze["prior_spent_calls"] = 5
        with self.assertRaisesRegex(ValueError, "inconsistent"):
            validate_batch_freeze(freeze)
        freeze["prior_spent_calls"] = 0
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

    def test_refused_request_remains_charged_but_one_correction_can_complete_canary(
        self,
    ):
        from experiments.qualify_investigator_model_interface import (
            assess_canary,
            canary_assignment,
            canary_protocol,
        )

        a = canary_assignment("raw")
        responses = iter(
            [
                b"not json",
                request("read_source", source_id="canary", path="probe.txt"),
                request(
                    "search_sources",
                    source_id="canary",
                    query="NO_SUCH_CANARY_MARKER_91",
                ),
                request("read_source", source_id="canary", path="empty.txt"),
                request("finish_investigation"),
            ]
        )

        def consumer(p):
            body = json.loads(p.content)
            evidence = [
                ref
                for event in body["events"]
                for ref in json.loads(event["content"]).get("evidence", [])
            ]
            return report(evidence) if body["phase"] == "report" else next(responses)

        result = run_scripted_trial(a, consumer, limits=TrialLimits(consumer_turns=6))
        self.assertEqual(result.outcome, "completed", result.problem)
        self.assertEqual(result.charges["corrections"], 1)
        self.assertEqual(result.charges["consumer_invocation_attempts"], 6)
        self.assertEqual(assess_canary(a, 1, result)[0], "qualified")
        self.assertEqual(canary_protocol(a, 1, 0)["limits"]["consumer_turns"], 6)

    def test_load_failure_is_retained_and_does_not_suppress_independent_candidate(self):
        from types import SimpleNamespace

        from experiments.qualify_investigator_model_interface import (
            code_hashes,
            digest,
            execute_frozen,
        )

        attempted = []

        class Download:
            def __init__(self, key):
                self.model_key = key

            def load_new_instance(self, **kwargs):
                attempted.append(self.model_key)
                raise ValueError("controlled load refusal")

        class Client:
            def __init__(self, address):
                self.llm = SimpleNamespace(
                    list_loaded=list,
                    list_downloaded=lambda: [Download(key) for key in keys],
                )

            def __enter__(self):
                return self

            def __exit__(self, *args):
                return False

        keys = ["gemma-4-e2b-it", "gemma-4-e4b-it-ud"]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            deployments = []
            for i, key in enumerate(keys):
                content = json_bytes(
                    {"model_key": key, "identifier": f"owned-{i}", "requested_load": {}}
                )
                path = root / f"profile-{i}.json"
                path.write_bytes(content)
                deployments.append(
                    {
                        "model_key": key,
                        "profile_path": str(path),
                        "profile_sha256": digest(content),
                    }
                )
            freeze = {
                "format": "investigator-interface-canary-freeze/2",
                "reference_schema_policy": "investigator-request-local-reference-schema/1",
                "preflight_inspected": True,
                "inference_admitted": True,
                "later_semantic_comparison_admitted": False,
                "deployments": deployments,
                "deployment_count": 2,
                "max_model_calls": 48,
                "calls_per_sequence": 6,
                "prior_spent_calls": 19,
                "cycle_call_ceiling": 67,
                "assignments": [
                    {
                        "id": f"{i}-{t}-{s}",
                        "model_key": k,
                        "treatment": t,
                        "sequence": s,
                    }
                    for i, k in enumerate(keys)
                    for t in ("raw", "structured")
                    for s in (1, 2)
                ],
                "code_sha256": code_hashes(),
                "immutable_files": [],
            }
            content = json_bytes(freeze)
            path = root / "freeze.json"
            path.write_bytes(content)
            output = root / "results"
            results = execute_frozen(
                SimpleNamespace(Client=Client), path, digest(content), output
            )
            self.assertEqual(attempted, keys)
            self.assertEqual(sum(item["model_attempts"] for item in results), 0)
            self.assertEqual(len(list(output.glob("deployment-*-failure.json"))), 2)
            self.assertEqual(len(results), 8)

    def test_registry_alias_does_not_hide_a_changed_actual_gguf_or_placement(self):
        from experiments.qualify_investigator_model_interface import (
            validate_loaded_backend,
        )

        backend = {
            "executable": "backend",
            "cpu_kv": True,
            "kv_unified_flag": True,
            "no_kv_unified_flag": False,
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
        for key in ("kv_unified_flag", "no_kv_unified_flag"):
            drift = copy.deepcopy(actual)
            drift[key] = not drift[key]
            with self.assertRaisesRegex(ValueError, "backend/template/cache changed"):
                validate_loaded_backend(profile, fresh, drift)
        for key, value in [("model", "other.gguf"), ("n-gpu-layers", "11")]:
            drift = copy.deepcopy(actual)
            drift["flags"][key] = value
            with self.assertRaisesRegex(
                ValueError, "actual model file/backend placement"
            ):
                validate_loaded_backend(profile, fresh, drift)

    def test_backend_bos_is_measured_once_from_actual_token_identity(self):
        from experiments.investigator_model_interface import include_tokenizer_bos

        policy = {"add_bos": True, "bos_token": "<bos>", "bos_id": 2}

        def tokenize(text):
            if text == "<bos>":
                return [2]
            return [2, 10] if text.startswith("<bos>") else [10]

        self.assertEqual(include_tokenizer_bos("body", policy, tokenize), "<bos>body")
        self.assertEqual(
            include_tokenizer_bos("<bos>body", policy, tokenize), "<bos>body"
        )
        with self.assertRaisesRegex(ValueError, "actual tokenizer"):
            include_tokenizer_bos("body", policy, lambda text: [99])
        self.assertEqual(
            include_tokenizer_bos("body", {"add_bos": False}, tokenize), "body"
        )

    def test_runtime_grammar_uses_only_offered_tools_then_the_exact_report_schema(self):
        from experiments.investigator_model_interface import fields
        from experiments.investigator_workspace_trial import (
            pack_input,
            protocol_definition,
        )

        for treatment in ("raw", "structured"):
            assignment = fixture(treatment)
            protocol = protocol_definition(assignment, TrialLimits())
            for phase in ("investigate", "report"):
                measured = measure_input(
                    Binding(), pack_input(protocol, [], phase, 128 * 1024), config()
                )
                schema = fields(measured.configuration["layers"][0]["config"])[
                    "llm.prediction.structured"
                ]["jsonSchema"]
                if phase == "report":
                    self.assertEqual(
                        schema, json.loads(measured.packed.content)["report_schema"]
                    )
                else:
                    menus = {
                        v["properties"]["tool"]["enum"][0]: v["properties"]["arguments"]
                        for v in schema["anyOf"]
                    }
                    self.assertEqual(
                        menus, json.loads(measured.packed.content)["tools"]
                    )
                    self.assertEqual("read_native" in menus, treatment == "structured")
        self.assertNotIn(
            "llm.prediction.structured", fields(config()["layers"][0]["config"])
        )

    def test_native_sampling_and_mode_override_only_declared_fields(self):
        from experiments.investigator_model_interface import fields

        frozen = fields(
            config(
                reasoning=True,
                temperature=0.6,
                top_k=20,
                top_p=0.95,
                output_tokens=8192,
            )["layers"][0]["config"]
        )
        self.assertTrue(frozen["llm.prediction.reasoning.enableThinking"])
        self.assertEqual(frozen["llm.prediction.temperature"], 0.6)
        self.assertEqual(frozen["llm.prediction.topKSampling"], 20)
        self.assertEqual(
            frozen["llm.prediction.topPSampling"], {"checked": True, "value": 0.95}
        )
        self.assertFalse(frozen["llm.prediction.minPSampling"]["checked"])
        self.assertFalse(frozen["llm.prediction.repeatPenalty"]["checked"])
        old = fields(config()["layers"][0]["config"])
        self.assertFalse(old["llm.prediction.reasoning.enableThinking"])
        self.assertEqual(old["llm.prediction.temperature"], 0.2)
        self.assertNotIn("llm.prediction.topKSampling", old)

    def test_actual_sampler_defaults_are_pinned_without_inheriting_prior_grammar(self):
        from experiments.investigator_model_interface import fields

        loaded = {
            "fields": [
                {
                    "key": "llm.load.promptTemplate",
                    "value": {"jinjaPromptTemplate": {"template": "EXACT"}},
                }
            ]
        }
        actual = {
            "fields": [
                {"key": "llm.prediction.topKSampling", "value": 64},
                {"key": "llm.prediction.reasoning.enableThinking", "value": True},
                {"key": "llm.prediction.structured", "value": {"old": "grammar"}},
            ]
        }
        original = copy.deepcopy(actual)
        frozen = fields(
            prediction_configuration(loaded, applied_base=actual)["layers"][0]["config"]
        )
        self.assertEqual(frozen["llm.prediction.topKSampling"], 64)
        self.assertFalse(frozen["llm.prediction.reasoning.enableThinking"])
        self.assertNotIn("llm.prediction.structured", frozen)
        self.assertEqual(actual, original)

    def test_interrupted_stream_keeps_visible_prefix_and_unknown_usage_without_salvage(
        self,
    ):
        from experiments.investigator_model_interface import retain_visible_fragment

        with tempfile.TemporaryDirectory() as directory:
            model = StatelessInvestigatorModel(
                Binding(),
                config(),
                ModelLimits(context=10000),
                Path(directory) / "assignment",
            )

            def terminated(measured, timeout, *, visible_sink):
                retain_visible_fragment(
                    {"content": '{"claims":', "reasoningType": "none"}, visible_sink
                )
                retain_visible_fragment(
                    {
                        "content": "DO NOT RETAIN HIDDEN TEXT",
                        "reasoningType": "reasoning",
                    },
                    visible_sink,
                )
                raise RuntimeError("prediction terminated before success metadata")

            model.binding.predict = terminated
            with self.assertRaisesRegex(RuntimeError, "terminated"):
                model(packed())
            self.assertEqual(
                (model.directory / "call-01.visible-fragments.txt").read_bytes(),
                b'{"claims":',
            )
            self.assertFalse(
                (model.directory / "call-01.visible-response.txt").exists()
            )
            receipt = json.loads(
                (model.directory / "call-01.receipt.json").read_bytes()
            )
            self.assertEqual(receipt["visible_fragment_bytes"], 10)
            self.assertIsNone(receipt["usage"])
            self.assertFalse(receipt["complete_response_received"])
            self.assertFalse(model.usage_complete)
            with self.assertRaisesRegex(ValueError, "budget refuses"):
                model(packed())
