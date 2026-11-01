"""Native record meaning, trace integrity and exact measurement boundaries."""
from dataclasses import replace
import json
import math
import unittest
from unittest.mock import patch

from upgradepilot.caller_signature.analysis import (
    CallArguments, SourceFacts, SourceSpan, fact_identity, CallableSignature, ParameterFact,
)
from upgradepilot.caller_signature.bindings import BindingAssessment, BindingTraceStep
from upgradepilot.caller_signature.evidence import MeasuredDuration, AnalysisLimits
from upgradepilot.caller_signature.native_codec import (
    encode_source_facts, decode_source_facts, encode_duration, decode_duration,
)
from upgradepilot.workspace.native_representation import NativeReconstructionError


TEXT = "from pkg import f\nf(x=1)\nf(x=1)\n"
UNIT = "a" * 64


def facts():
    step = BindingTraceStep(UNIT, "module", 1, 0, 1, 17, "import", "f", "pkg.f")
    binding = BindingAssessment("established", ("pkg.f",), False, False, "module", (), (step,))
    calls = []
    for line in (2, 3):
        span = SourceSpan(line, 0, line, 6)
        calls.append(CallArguments(fact_identity("call", UNIT, span), UNIT, span, "f",
                     (), ("x",), (SourceSpan(line, 2, line, 5),), True, binding))
    return SourceFacts(UNIT, tuple(calls), (), (), 15)


class NativeSourceFactCodecTests(unittest.TestCase):
    def encode(self, value=None):
        return encode_source_facts(value or facts(), text=TEXT, coverage="complete_file")

    def decode(self, payload, **kwargs):
        return decode_source_facts(payload, unit_id=UNIT, text=TEXT,
                                   coverage="complete_file", **kwargs)

    def test_shared_trace_roundtrip_without_ast_or_network(self):
        payload = self.encode()
        wire = json.loads(payload)
        self.assertEqual(len(wire["facts"]["binding_trace_steps"]), 1)
        self.assertEqual([c["binding"]["trace"] for c in wire["facts"]["calls"]], [[0], [0]])
        with patch("ast.parse", side_effect=AssertionError("No derivation")), patch(
            "requests.sessions.Session.request", side_effect=AssertionError("No acquisition")
        ):
            self.assertEqual(self.decode(payload), facts())

    def test_trace_corruption_refuses(self):
        def duplicate(w):
            w["facts"]["binding_trace_steps"].append(w["facts"]["binding_trace_steps"][0].copy())
        def unused(w):
            extra = w["facts"]["binding_trace_steps"][0].copy()
            extra["operation"] = "other"
            w["facts"]["binding_trace_steps"].append(extra)
        corruptions = [duplicate, unused]
        for index in (True, -1, 1, "0"):
            corruptions.append(lambda w, i=index: w["facts"]["calls"][0]["binding"].update(trace=[i]))
        corruptions += [
            lambda w: w["facts"]["binding_trace_steps"][0].update(source_id="b" * 64),
            lambda w: w["facts"]["binding_trace_steps"][0].update(end_column=1000),
            lambda w: w["facts"]["calls"][0]["binding"].update(unknown_possible=True),
        ]
        for mutate in corruptions:
            wire = json.loads(self.encode())
            mutate(wire)
            with self.subTest(mutate=mutate), self.assertRaises(ValueError):
                self.decode(json.dumps(wire).encode())

    def test_identity_coverage_and_work_are_not_guessed(self):
        for mutate in (
            lambda w: w["facts"].update(unit_id="b" * 64),
            lambda w: w["facts"].update(ast_nodes=True),
            lambda w: w["facts"].update(ast_nodes=100001),
            lambda w: w["facts"]["calls"][0].update(fact_id="b" * 64),
            lambda w: w["facts"]["calls"].append(w["facts"]["calls"][0].copy()),
            lambda w: w["facts"].update(unexpected="field"),
            lambda w: w["facts"]["calls"][0].update(complete=False),
        ):
            wire = json.loads(self.encode())
            mutate(wire)
            with self.subTest(mutate=mutate), self.assertRaises(ValueError):
                self.decode(json.dumps(wire).encode())
        for version in (True, 2, "1"):
            wire = json.loads(self.encode()); wire["codec_version"] = version
            with self.subTest(version=version), self.assertRaises(NativeReconstructionError):
                self.decode(json.dumps(wire).encode())
        with self.assertRaises(ValueError):
            decode_source_facts(self.encode(), unit_id=UNIT, text=TEXT, coverage="unexamined")

    def test_conditional_alternatives_and_trace_order_survive(self):
        original = facts()
        first = original.calls[0]
        binding = replace(first.binding, state="conditional", possible_imports=("pkg.f", "pkg.g"),
                          unknown_possible=True, reasons=("branch",),
                          trace=first.binding.trace * 2)
        value = replace(original, calls=(replace(first, binding=binding),))
        self.assertEqual(self.decode(self.encode(value)), value)

    def test_signature_order_defaults_and_spans_remain_checked(self):
        text = "def f(x, *, y=1): pass\n"
        span = SourceSpan(1, 0, 1, len(text.rstrip()))
        signature = CallableSignature(fact_identity("signature", UNIT, span), UNIT, span,
            SourceSpan(1, 0, 1, 17), "f", "function",
            (ParameterFact("x", "positional_or_keyword", False), ParameterFact("y", "keyword_only", True)),
            True, (), (), ())
        value = SourceFacts(UNIT, (), (signature,), (), 12)
        payload = encode_source_facts(value, text=text, coverage="complete_file")
        self.assertEqual(decode_source_facts(payload, unit_id=UNIT, text=text, coverage="complete_file"), value)
        for mutate in (
            lambda s: s["parameters"].reverse(),
            lambda s: s["parameters"][0].update(kind="variadic_positional", has_default=True),
            lambda s: s["parameters"][1].update(name="x"),
            lambda s: s["header_span"].update(end_column=100),
        ):
            wire = json.loads(payload)
            mutate(wire["facts"]["signatures"][0])
            with self.subTest(mutate=mutate), self.assertRaises(ValueError):
                decode_source_facts(json.dumps(wire).encode(), unit_id=UNIT, text=text, coverage="complete_file")

    def test_codec_limits_and_utf8_boundaries_cannot_be_bypassed(self):
        with self.assertRaises(ValueError):
            self.decode(self.encode(), limits=AnalysisLimits(max_facts=1))
        raw = json.loads(self.encode())
        raw["facts"]["binding_trace_steps"][0].update(column=1, end_column=2)
        with self.assertRaises(ValueError):
            decode_source_facts(json.dumps(raw).encode(), unit_id=UNIT,
                                text="é" * 17 + "\nf(x=1)\nf(x=1)\n", coverage="complete_file")


class ExactDurationCodecTests(unittest.TestCase):
    def test_binary_measurements_survive_native_roundtrip_exactly(self):
        for seconds in (0.0, -0.0, 0.1, 18.991642, math.ulp(0.0), float.fromhex("0x1.fffffffffffffp+1023")):
            measured = MeasuredDuration.from_seconds(seconds, "worker elapsed")
            restored = decode_duration(encode_duration(measured))
            self.assertEqual(restored.seconds.hex(), seconds.hex())
            self.assertEqual(restored.scope, "worker elapsed")

    def test_unsupported_or_noncanonical_measurements_refuse(self):
        for text in ("0.1", "nan", "inf", "-0x1.0p+0", "0x1p+0", "x" * 65):
            with self.subTest(text=text), self.assertRaises(ValueError):
                MeasuredDuration(text, "worker elapsed")
        for value in (True, 1, None, float("nan"), float("inf"), -1.0):
            with self.subTest(value=value), self.assertRaises(ValueError):
                MeasuredDuration.from_seconds(value, "worker elapsed")


if __name__ == "__main__":
    unittest.main()
