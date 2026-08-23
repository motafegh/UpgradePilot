"""Test the Step 7C local support-drop semantic adapter without live inference."""

from __future__ import annotations

import json
import unittest
from datetime import datetime, timezone
from unittest.mock import Mock

from requests.exceptions import Timeout

from upgradepilot.upstream.changelog import (
    CrossedReleaseSourceWindow,
    build_crossed_release_source_window,
)
from upgradepilot.upstream.claim import CandidateUpstreamClaimResult
from upgradepilot.upstream.interval import (
    CrossedReleaseIndexEvidence,
    DependencyReleaseInterval,
    TaggedChangelogEvidence,
)
from upgradepilot.upstream.support_drop_extractor import (
    ADOPTED_MODEL_ID,
    LM_STUDIO_BASE_URL,
    MAX_SOURCE_WINDOW_CHARACTERS,
    REQUEST_TIMEOUT_SECONDS,
    LocalSupportDropExtractor,
)

_NOW = datetime(2026, 8, 5, 10, 0, tzinfo=timezone.utc)
_REPOSITORY = "example/friendly-bard"


def _interval() -> DependencyReleaseInterval:
    return DependencyReleaseInterval(
        package="friendly-bard",
        normalized_package="friendly-bard",
        old_version="2.6",
        proposed_version="2.8.4",
    )


def _window(
    content: str,
    *,
    versions: tuple[str, ...] = ("2.7", "2.8", "2.8.4"),
    max_characters: int = MAX_SOURCE_WINDOW_CHARACTERS,
) -> CrossedReleaseSourceWindow:
    interval = _interval()
    crossed = CrossedReleaseIndexEvidence(
        repository=_REPOSITORY,
        interval=interval,
        ordered_versions=versions,
        source_url="https://pypi.org/pypi/friendly-bard/json",
        retrieved_at=_NOW,
    )
    changelog = TaggedChangelogEvidence(
        repository=_REPOSITORY,
        interval=interval,
        resolved_commit_sha="a" * 40,
        path="docs/changelog.md",
        content=content,
    )
    result = build_crossed_release_source_window(
        crossed,
        changelog,
        max_characters=max_characters,
    )
    self_check = isinstance(result, CrossedReleaseSourceWindow)
    if not self_check:
        raise AssertionError(f"Test fixture did not build a source window: {result!r}")
    return result


def _response(selection: object, *, status: int = 200, finish: str = "stop") -> Mock:
    response = Mock()
    response.status_code = status
    response.json.return_value = {
        "choices": [
            {
                "finish_reason": finish,
                "message": {"content": json.dumps(selection)},
            }
        ]
    }
    return response


def _positive_content() -> str:
    return (
        "## 2.8.4\n- Fix selector behavior.\n"
        "## 2.8\n- Drop support for Python 3.8.\n"
        "## 2.7\n- Add a selector.\n"
    )


class LocalSupportDropExtractorTests(unittest.TestCase):
    def test_positive_selection_recovers_exact_global_source_line(self) -> None:
        content = _positive_content()
        window = _window(content)
        post = Mock(
            return_value=_response(
                {
                    "candidates": [
                        {
                            "python_line": "3.8",
                            "introduced_in_version": "2.8",
                            "source_line_id": "L4",
                        }
                    ],
                    "unresolved_if_no_candidates": False,
                    "detail": "",
                }
            )
        )

        result = LocalSupportDropExtractor(post=post).extract(window)

        self.assertIsInstance(result, CandidateUpstreamClaimResult)
        self.assertEqual(result.state, "candidates_available")
        self.assertEqual(len(result.candidates), 1)
        candidate = result.candidates[0]
        expected_quote = "- Drop support for Python 3.8."
        self.assertEqual(candidate.python_line, "3.8")
        self.assertEqual(candidate.introduced_in_version, "2.8")
        self.assertEqual(candidate.source_kind, "tagged_changelog")
        self.assertIsNone(candidate.source_release_version)
        self.assertEqual(candidate.source_quote, expected_quote)
        self.assertEqual(candidate.quote_start, content.index(expected_quote))
        self.assertEqual(
            candidate.quote_end,
            content.index(expected_quote) + len(expected_quote),
        )

    def test_request_preserves_accepted_contract_and_trusted_version_order(self) -> None:
        window = _window(_positive_content())
        post = Mock(
            return_value=_response(
                {
                    "candidates": [],
                    "unresolved_if_no_candidates": False,
                    "detail": "",
                }
            )
        )

        LocalSupportDropExtractor(post=post).extract(window)

        post.assert_called_once()
        args, kwargs = post.call_args
        self.assertEqual(args, (f"{LM_STUDIO_BASE_URL}/v1/chat/completions",))
        self.assertEqual(kwargs["timeout"], REQUEST_TIMEOUT_SECONDS)
        payload = kwargs["json"]
        self.assertEqual(payload["model"], ADOPTED_MODEL_ID)
        self.assertEqual(payload["temperature"], 0)
        self.assertEqual(payload["seed"], 0)
        self.assertFalse(payload["stream"])
        self.assertEqual(payload["max_tokens"], 1024)
        self.assertTrue(payload["response_format"]["json_schema"]["strict"])
        schema = payload["response_format"]["json_schema"]["schema"]
        candidate_schema = schema["properties"]["candidates"]["items"]
        version_enum = candidate_schema["properties"]["introduced_in_version"]["enum"]
        self.assertEqual(version_enum, ["2.7", "2.8", "2.8.4"])
        self.assertIn("crossed_release_versions: 2.7, 2.8, 2.8.4", payload["messages"][1]["content"])
        self.assertIn("L4 | - Drop support for Python 3.8.", payload["messages"][1]["content"])

    def test_zero_candidate_clear_result_is_no_relevant_claim(self) -> None:
        post = Mock(
            return_value=_response(
                {
                    "candidates": [],
                    "unresolved_if_no_candidates": False,
                    "detail": "",
                }
            )
        )

        result = LocalSupportDropExtractor(post=post).extract(_window(_positive_content()))

        self.assertEqual(result.state, "no_relevant_claim")
        self.assertEqual(result.candidates, ())
        self.assertIsNone(result.detail)

    def test_zero_candidate_ambiguous_result_is_unresolved(self) -> None:
        post = Mock(
            return_value=_response(
                {
                    "candidates": [],
                    "unresolved_if_no_candidates": True,
                    "detail": "The wording does not identify the dropped line explicitly.",
                }
            )
        )

        result = LocalSupportDropExtractor(post=post).extract(_window(_positive_content()))

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.candidates, ())
        self.assertEqual(
            result.detail,
            "The wording does not identify the dropped line explicitly.",
        )

    def test_source_line_must_belong_to_model_selected_release(self) -> None:
        post = Mock(
            return_value=_response(
                {
                    "candidates": [
                        {
                            "python_line": "3.8",
                            "introduced_in_version": "2.7",
                            "source_line_id": "L4",
                        }
                    ],
                    "unresolved_if_no_candidates": False,
                    "detail": "",
                }
            )
        )

        result = LocalSupportDropExtractor(post=post).extract(_window(_positive_content()))

        self.assertEqual(result.state, "unresolved")
        self.assertIn("release identity did not match", result.detail or "")

    def test_python_line_must_be_explicit_in_bounded_source(self) -> None:
        post = Mock(
            return_value=_response(
                {
                    "candidates": [
                        {
                            "python_line": "3.9",
                            "introduced_in_version": "2.8",
                            "source_line_id": "L4",
                        }
                    ],
                    "unresolved_if_no_candidates": False,
                    "detail": "",
                }
            )
        )

        result = LocalSupportDropExtractor(post=post).extract(_window(_positive_content()))

        self.assertEqual(result.state, "unresolved")
        self.assertIn("not explicit in the source", result.detail or "")

    def test_no_explicit_python_token_forces_empty_candidate_schema(self) -> None:
        content = (
            "## 2.8.4\n- Fix selector behavior.\n"
            "## 2.8\n- Improve parser behavior.\n"
            "## 2.7\n- Add a selector.\n"
        )
        post = Mock(
            return_value=_response(
                {
                    "candidates": [],
                    "unresolved_if_no_candidates": False,
                    "detail": "",
                }
            )
        )

        result = LocalSupportDropExtractor(post=post).extract(_window(content))

        self.assertEqual(result.state, "no_relevant_claim")
        payload = post.call_args.kwargs["json"]
        candidates_schema = payload["response_format"]["json_schema"]["schema"]["properties"]["candidates"]
        self.assertEqual(candidates_schema["maxItems"], 0)

    def test_provider_timeout_is_unresolved_and_not_retried(self) -> None:
        post = Mock(side_effect=Timeout("slow"))

        result = LocalSupportDropExtractor(post=post).extract(_window(_positive_content()))

        self.assertEqual(result.state, "unresolved")
        self.assertIn("provider request failed", result.detail or "")
        post.assert_called_once()

    def test_unsuccessful_http_status_is_unresolved(self) -> None:
        post = Mock(return_value=_response({}, status=503))

        result = LocalSupportDropExtractor(post=post).extract(_window(_positive_content()))

        self.assertEqual(result.state, "unresolved")
        self.assertIn("503", result.detail or "")

    def test_malformed_outer_or_inner_json_is_unresolved(self) -> None:
        bad_outer = Mock()
        bad_outer.status_code = 200
        bad_outer.json.side_effect = ValueError("bad outer")

        bad_inner = Mock()
        bad_inner.status_code = 200
        bad_inner.json.return_value = {
            "choices": [
                {"finish_reason": "stop", "message": {"content": "not-json"}}
            ]
        }

        for response in (bad_outer, bad_inner):
            with self.subTest(response=response):
                result = LocalSupportDropExtractor(
                    post=Mock(return_value=response)
                ).extract(_window(_positive_content()))
                self.assertEqual(result.state, "unresolved")

    def test_contract_shape_violation_is_unresolved(self) -> None:
        post = Mock(
            return_value=_response(
                {
                    "candidates": [],
                    "unresolved_if_no_candidates": False,
                    "detail": "",
                    "extra": "not admitted",
                }
            )
        )

        result = LocalSupportDropExtractor(post=post).extract(_window(_positive_content()))

        self.assertEqual(result.state, "unresolved")
        self.assertIn("fields differed", result.detail or "")

    def test_completion_length_stop_is_unresolved(self) -> None:
        post = Mock(
            return_value=_response(
                {
                    "candidates": [],
                    "unresolved_if_no_candidates": False,
                    "detail": "",
                },
                finish="length",
            )
        )

        result = LocalSupportDropExtractor(post=post).extract(_window(_positive_content()))

        self.assertEqual(result.state, "unresolved")
        self.assertIn("length limit", result.detail or "")

    def test_runtime_character_guard_stops_before_provider_call(self) -> None:
        oversized = "x" * (MAX_SOURCE_WINDOW_CHARACTERS + 50)
        content = (
            f"## 2.8.4\n{oversized}\n"
            "## 2.8\nPython 3.8 support changed.\n"
            "## 2.7\nchange\n"
        )
        window = _window(
            content,
            max_characters=len(content) + 10,
        )
        post = Mock()

        result = LocalSupportDropExtractor(post=post).extract(window)

        self.assertEqual(result.state, "unresolved")
        self.assertIn("character guard", result.detail or "")
        post.assert_not_called()


if __name__ == "__main__":
    unittest.main()
