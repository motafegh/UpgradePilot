"""Proposal boundaries; controlled replies prove mechanics, never API meaning."""

import json
from dataclasses import replace
from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

import requests

from experiments.api_change_interpretation import (
    LOCAL_ENDPOINT,
    OUTPUT_TOKENS,
    LocalInterpretationProvider,
    ProviderReply,
    RequestCapacityEvidence,
    interpret_projection,
    packet_hash,
    prepare_request,
    source_input_from_projection,
    text_hash,
)

INTERVAL = {
    "package": "vendor",
    "normalized_package": "vendor",
    "old_version": "1.0",
    "proposed_version": "2.0",
    "lower_bound_inclusive": False,
    "upper_bound_inclusive": True,
}


def projection(text="## 2.0\r\nThe option was removed.\r\nOther change.\n"):
    return {
        "state": "available",
        "complete_window_eligible": True,
        "basis": "exact_release_publisher_declared_repository",
        "repository": "owner/vendor",
        "revision": "a" * 40,
        "path": "CHANGELOG.md",
        "sha256": text_hash(text),
        "versions": ["2.0"],
        "sections": [
            {
                "version": "2.0",
                "start_line": 1,
                "start_offset": 0,
                "end_offset": len(text),
                "text": text,
                "sha256": text_hash(text),
            }
        ],
    }


def observation(**changes):
    return {
        "kind": "removal",
        "subject": "option",
        "summary": "The option was removed.",
        "assertion": "affirmed",
        "timing": "current",
        "effective_version": "2.0",
        "source_spans": [{"start_line_id": "S1:L2", "end_line_id": "S1:L2"}],
        "reason": None,
        **changes,
    }


class ControlledProvider:
    identity = {"kind": "controlled_test", "semantic_acceptance": False}

    def __init__(self, output=None, *, reply=None):
        self.reply = reply or ProviderReply(
            json.dumps(
                output
                if output is not None
                else {"observations": [observation()], "unassessed": []}
            )
        )
        self.requests = []

    def complete(self, request):
        self.requests.append(request)
        return self.reply


class InterpretationTests(TestCase):
    def test_output_budget_binds_request_without_changing_semantic_input(self):
        source = source_input_from_projection(projection(), INTERVAL)
        pilot = prepare_request(source, max_output_tokens=1536)
        extended = prepare_request(source)
        self.assertEqual(extended.payload["max_tokens"], 8192)
        self.assertEqual(pilot.payload["messages"], extended.payload["messages"])
        self.assertEqual(
            pilot.payload["response_format"], extended.payload["response_format"]
        )
        self.assertNotEqual(
            pilot.method["request_sha256"], extended.method["request_sha256"]
        )
        for invalid in (0, -1, True, "8192"):
            with self.assertRaises(ValueError):
                prepare_request(source, max_output_tokens=invalid)

    def run_output(self, output):
        return interpret_projection(projection(), INTERVAL, ControlledProvider(output))

    def test_complete_source_mapping_preserves_endings_ranges_and_request_identity(
        self,
    ):
        source = projection()
        source["sections"][0]["start_line"] = 20
        source["sections"][0]["start_offset"] = 100
        source["sections"][0]["end_offset"] += 100
        provider = ControlledProvider()
        result = interpret_projection(source, INTERVAL, provider)
        self.assertEqual(result["state"], "observations_returned")
        citation = result["observations"][0]["evidence"][0]
        self.assertEqual(citation["quote"], "The option was removed.\r\n")
        self.assertEqual(citation["start_line"], 21)
        self.assertEqual(citation["start_offset"], 108)
        self.assertEqual(citation["end_offset"], 133)
        self.assertEqual(citation["quote_sha256"], text_hash(citation["quote"]))
        request = provider.requests[0]
        self.assertEqual(
            result["method"]["request_sha256"], packet_hash(request.payload)
        )
        user = request.payload["messages"][1]["content"]
        self.assertIn("Other change.", user)
        self.assertIn("S1:L3", user)
        self.assertNotIn("target", request.source_input)
        self.assertEqual(
            set(result["method"]["asset_sha256"]),
            {"prompt-template-v1.md", "output-schema-v1.json"},
        )

    def test_partial_and_duplicate_candidates_remain_separate_scopes(self):
        complete = projection()
        first = complete["sections"][0]
        second = {
            **first,
            "start_line": 8,
            "start_offset": 100,
            "end_offset": 100 + len(first["text"]),
        }
        source = {
            "state": "incomplete",
            "stage": "sections",
            "reason": "ambiguous",
            "detail": "gap",
            "source_context": {"interval": INTERVAL, "basis": complete["basis"]},
            "section_examination": {
                "repository": complete["repository"],
                "revision": complete["revision"],
                "path": complete["path"],
                "full_source_sha256": complete["sha256"],
                "required_versions": ["2.0", "1.5"],
                "ambiguous_versions": ["2.0"],
                "missing_or_unsupported_versions": ["1.5"],
                "candidates": [second, first],
            },
        }
        output = {
            "observations": [
                observation(
                    source_spans=[
                        {"start_line_id": "S1:L2", "end_line_id": "S1:L2"},
                        {"start_line_id": "S2:L2", "end_line_id": "S2:L2"},
                    ]
                )
            ],
            "unassessed": [],
        }
        result = interpret_projection(source, INTERVAL, ControlledProvider(output))
        self.assertEqual(result["state"], "observations_returned")
        coverage = result["source_input"]["source_coverage"]
        self.assertFalse(coverage["complete_window_eligible"])
        self.assertEqual(coverage["ambiguous_versions"], ["2.0"])
        self.assertEqual(coverage["missing_or_unsupported_versions"], ["1.5"])
        self.assertEqual(
            [e["start_line"] for e in result["observations"][0]["evidence"]], [2, 9]
        )

    def test_no_source_text_or_corrupt_range_never_calls_provider(self):
        for mutate in (
            lambda p: p.update(sections=[]),
            lambda p: p["sections"][0].update(end_offset=999),
            lambda p: p["sections"][0].update(sha256="wrong"),
            lambda p: p.update(revision=None),
        ):
            source = projection()
            mutate(source)
            provider = ControlledProvider()
            self.assertEqual(
                interpret_projection(source, INTERVAL, provider)["state"],
                "input_problem",
            )
            self.assertEqual(provider.requests, [])
        source = {
            "state": "incomplete",
            "reason": "text_omitted",
            "section_examination": {
                "required_versions": ["2.0"],
                "candidates": [{"version": "2.0", "text": None}],
                "text_omission_reason": "over_limit",
            },
        }
        result = interpret_projection(source, INTERVAL, ControlledProvider())
        self.assertEqual(result["problem"]["reason"], "no_retained_source_text")
        self.assertEqual(
            result["source_input"]["source_coverage"]["text_omission_reason"],
            "over_limit",
        )

    def test_shape_adversaries_are_not_salvaged(self):
        mutations = [
            lambda o: o.update(compatibility="safe"),
            lambda o: o.pop("unassessed"),
            lambda o: o["observations"][0].update(kind="safe"),
            lambda o: o["observations"][0].update(subject=42),
            lambda o: o["observations"][0].update(summary=""),
            lambda o: o["observations"][0].update(summary="x" * 1025),
            lambda o: o["observations"][0].update(source_spans=[]),
            lambda o: o.update(observations=[observation()] * 65),
            lambda o: o["observations"][0].update(quote="invented"),
            lambda o: o["observations"][0].update(subject=None),
            lambda o: o["observations"][0].update(assertion="uncertain", reason="  "),
            lambda o: o["observations"][0].update(timing="unspecified"),
            lambda o: o["observations"][0].update(kind="unclear"),
            lambda o: o.update(
                unassessed=[
                    {"source_spans": observation()["source_spans"], "reason": " "}
                ]
            ),
        ]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                output = {"observations": [observation()], "unassessed": []}
                mutate(output)
                result = self.run_output(output)
                self.assertEqual(result["state"], "contract_problem")
                self.assertEqual(result["observations"], [])
        for raw in (
            '{"observations":[],"observations":[],"unassessed":[]}',
            '{"observations":NaN,"unassessed":[]}',
            "{",
            "x" * 262145,
        ):
            result = interpret_projection(
                projection(), INTERVAL, ControlledProvider(reply=ProviderReply(raw))
            )
            self.assertEqual(result["state"], "contract_problem")

    def test_absent_reversed_and_cross_section_references_fail(self):
        source = projection()
        source["versions"].append("1.5")
        source["sections"].append(
            {
                **source["sections"][0],
                "version": "1.5",
                "start_offset": 100,
                "end_offset": 100 + len(source["sections"][0]["text"]),
            }
        )
        for start, end in (
            ("S1:L99", "S1:L99"),
            ("S1:L3", "S1:L2"),
            ("S1:L2", "S2:L2"),
        ):
            output = {
                "observations": [
                    observation(
                        source_spans=[{"start_line_id": start, "end_line_id": end}]
                    )
                ],
                "unassessed": [],
            }
            result = interpret_projection(source, INTERVAL, ControlledProvider(output))
            self.assertEqual(result["state"], "grounding_problem")
            self.assertEqual(result["observations"], [])

    def test_meaning_is_not_deterministic_acceptance_and_empty_is_not_negative_claim(
        self,
    ):
        output = {
            "observations": [
                observation(
                    subject=None,
                    kind="unclear",
                    assertion="uncertain",
                    timing="unspecified",
                    effective_version=None,
                    reason="Source does not identify the subject.",
                ),
                observation(
                    assertion="negated",
                    timing="planned",
                    effective_version="9.0",
                    summary="Deliberately wrong interpretation of a real quote.",
                ),
            ],
            "unassessed": [
                {
                    "source_spans": [
                        {"start_line_id": "S1:L3", "end_line_id": "S1:L3"}
                    ],
                    "reason": "Other change unclear.",
                }
            ],
        }
        result = self.run_output(output)
        self.assertEqual(result["state"], "observations_returned")
        self.assertEqual(result["observations"][1]["effective_version"], "9.0")
        self.assertEqual(
            result["observations"][1]["evidence"][0]["reported_in_version"], "2.0"
        )
        empty = self.run_output({"observations": [], "unassessed": []})
        self.assertEqual(empty["state"], "no_observations_returned")
        self.assertNotIn("no_impact", empty)

    def test_provider_failure_and_truncation_never_decode_or_retry(self):
        for reply, state in (
            (
                ProviderReply('{"observations":[],"unassessed":[]}', "length"),
                "provider_problem",
            ),
            (ProviderReply("{}", "tool_calls"), "provider_problem"),
            (
                ProviderReply(problem=("context_problem", "capacity_unverified")),
                "context_problem",
            ),
        ):
            provider = ControlledProvider(reply=reply)
            result = interpret_projection(projection(), INTERVAL, provider)
            self.assertEqual(result["state"], state)
            self.assertEqual(len(provider.requests), 1)
            self.assertEqual(result["observations"], [])
        broken = Mock(identity={"kind": "controlled_test"})
        broken.complete.side_effect = RuntimeError("raw private provider detail")
        result = interpret_projection(projection(), INTERVAL, broken)
        self.assertEqual(result["problem"]["reason"], "RuntimeError")
        self.assertNotIn("raw private", json.dumps(result))

    def test_unavailable_frozen_assets_preserve_input_without_provider_call(self):
        provider = ControlledProvider()
        with patch(
            "experiments.api_change_interpretation.prepare_request",
            side_effect=OSError("missing asset"),
        ):
            result = interpret_projection(projection(), INTERVAL, provider)
        self.assertEqual(result["state"], "contract_problem")
        self.assertEqual(result["problem"]["reason"], "frozen_producer_assets_invalid")
        self.assertTrue(result["source_input"]["sections"])
        self.assertIsNone(result["method"])
        self.assertEqual(provider.requests, [])


class LocalProviderTests(TestCase):
    def setUp(self):
        self.request = prepare_request(
            source_input_from_projection(projection(), INTERVAL)
        )
        self.capacity = RequestCapacityEvidence(
            self.request.method["request_sha256"],
            self.request.payload["model"],
            "controlled-deployment",
            "controlled-tokenizer",
            "controlled-template",
            "controlled full request accounting; not live measurement",
            16384,
            500,
            OUTPUT_TOKENS,
        )
        self.session = MagicMock()

    def test_no_http_without_capacity_and_exact_binding(self):
        for capacity in (
            None,
            replace(self.capacity, request_sha256="stale"),
            replace(self.capacity, input_tokens=16384),
            replace(self.capacity, reserved_output_tokens=1000),
            replace(self.capacity, tokenizer_identity=""),
            replace(self.capacity, model="another-model"),
        ):
            reply = LocalInterpretationProvider(
                capacity=capacity, session=self.session
            ).complete(self.request)
            self.assertEqual(reply.problem[0], "context_problem")
        self.session.post.assert_not_called()

    def response(self, envelope=None, *, raw=None, status=200):
        response = self.session.post.return_value.__enter__.return_value
        response.status_code = status
        response.iter_content.return_value = [
            raw if raw is not None else json.dumps(envelope).encode()
        ]

    def test_direct_session_single_bounded_request(self):
        envelope = {
            "choices": [
                {
                    "finish_reason": "stop",
                    "message": {"content": '{"observations":[],"unassessed":[]}'},
                }
            ]
        }
        self.response(envelope)
        reply = LocalInterpretationProvider(
            capacity=self.capacity, session=self.session
        ).complete(self.request)
        self.assertIsNone(reply.problem)
        self.assertEqual(reply.finish_reason, "stop")
        self.session.post.assert_called_once_with(
            LOCAL_ENDPOINT,
            json=self.request.payload,
            timeout=180,
            allow_redirects=False,
            stream=True,
        )
        self.assertFalse(self.session.trust_env)
        with patch(
            "experiments.api_change_interpretation.build_lm_studio_session",
            return_value=self.session,
        ) as factory:
            LocalInterpretationProvider()
        factory.assert_called_once_with()

    def test_provider_envelope_and_transport_failures(self):
        for envelope in (
            {"choices": []},
            {"choices": [{"message": {"content": None}}]},
            {"choices": [{"message": {"refusal": "no"}}]},
        ):
            self.response(envelope)
            reply = LocalInterpretationProvider(
                capacity=self.capacity, session=self.session
            ).complete(self.request)
            self.assertEqual(reply.problem[0], "provider_problem")
        for raw in (b"{", b"x" * 262145, b"\xff"):
            self.response(raw=raw)
            self.assertIsNotNone(
                LocalInterpretationProvider(
                    capacity=self.capacity, session=self.session
                )
                .complete(self.request)
                .problem
            )
        self.response(status=302)
        self.assertEqual(
            LocalInterpretationProvider(capacity=self.capacity, session=self.session)
            .complete(self.request)
            .problem[1],
            "http_status_302",
        )
        self.session.post.side_effect = requests.Timeout("private details")
        self.assertEqual(
            LocalInterpretationProvider(capacity=self.capacity, session=self.session)
            .complete(self.request)
            .problem[1],
            "Timeout",
        )

    def test_bounded_observer_does_not_bypass_provider_admission(self):
        observer = Mock()
        self.response(raw=b'{"error":"unsupported schema"}', status=400)
        reply = LocalInterpretationProvider(
            capacity=self.capacity, session=self.session, response_observer=observer
        ).complete(self.request)
        self.assertEqual(reply.problem[1], "http_status_400")
        observer.assert_called_once_with(400, b'{"error":"unsupported schema"}')
        observer.reset_mock()
        self.response(raw=b"x" * 262145)
        reply = LocalInterpretationProvider(
            capacity=self.capacity, session=self.session, response_observer=observer
        ).complete(self.request)
        self.assertEqual(reply.problem[1], "response_byte_limit")
        observer.assert_not_called()
