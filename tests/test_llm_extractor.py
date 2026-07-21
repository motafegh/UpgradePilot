import json
import os
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from upgradepilot.llm_extractor import (
    LLMExtractionError,
    LLMExtractorSettings,
    LMStudioPythonSupportExtractor,
)


class _FakeCompletions:
    def __init__(self, response=None, error=None):
        self.response = response
        self.error = error
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        if self.error is not None:
            raise self.error
        return self.response


class _FakeClient:
    def __init__(self, response=None, error=None):
        self.completions = _FakeCompletions(response=response, error=error)
        self.chat = SimpleNamespace(completions=self.completions)


def _response(payload):
    return SimpleNamespace(
        choices=(
            SimpleNamespace(
                message=SimpleNamespace(content=json.dumps(payload)),
            ),
        )
    )


class LLMExtractorSettingsTests(unittest.TestCase):
    def test_loads_required_model_and_runtime_settings(self):
        with patch.dict(
            os.environ,
            {
                "UPGRADEPILOT_LLM_BASE_URL": " http://localhost:12345/v1 ",
                "UPGRADEPILOT_LLM_MODEL": " qwen3-4b-instruct-2507 ",
                "UPGRADEPILOT_LLM_TIMEOUT": "45",
                "UPGRADEPILOT_LLM_MAX_TOKENS": "300",
                "UPGRADEPILOT_LLM_RESPONSE_FORMAT": "json_object",
            },
            clear=True,
        ):
            settings = LLMExtractorSettings.from_environment()

        self.assertEqual(settings.base_url, "http://localhost:12345/v1")
        self.assertEqual(settings.model, "qwen3-4b-instruct-2507")
        self.assertEqual(settings.timeout_seconds, 45.0)
        self.assertEqual(settings.max_tokens, 300)
        self.assertEqual(settings.response_format_mode, "json_object")

    def test_requires_model_identity(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(ValueError, "UPGRADEPILOT_LLM_MODEL"):
                LLMExtractorSettings.from_environment()

    def test_rejects_non_positive_runtime_limits(self):
        with patch.dict(
            os.environ,
            {
                "UPGRADEPILOT_LLM_MODEL": "gemma-4-e2b-it",
                "UPGRADEPILOT_LLM_TIMEOUT": "0",
            },
            clear=True,
        ):
            with self.assertRaisesRegex(ValueError, "greater than zero"):
                LLMExtractorSettings.from_environment()

    def test_rejects_unknown_response_format(self):
        with patch.dict(
            os.environ,
            {
                "UPGRADEPILOT_LLM_MODEL": "gemma-4-e2b-it",
                "UPGRADEPILOT_LLM_RESPONSE_FORMAT": "yaml",
            },
            clear=True,
        ):
            with self.assertRaisesRegex(ValueError, "json_schema or json_object"):
                LLMExtractorSettings.from_environment()


class LMStudioPythonSupportExtractorTests(unittest.TestCase):
    def setUp(self):
        self.settings = LLMExtractorSettings(
            base_url="http://localhost:12345/v1",
            model="qwen3-4b-instruct-2507",
            timeout_seconds=30,
            max_tokens=250,
        )

    def test_returns_untrusted_candidate_result(self):
        client = _FakeClient(
            response=_response(
                {
                    "facts": [
                        {
                            "change": "dropped",
                            "python_version": "3.8",
                            "source_quote": "drops Python 3.8 support",
                        }
                    ],
                    "unresolved": [],
                }
            )
        )
        extractor = LMStudioPythonSupportExtractor(self.settings, client=client)

        result = extractor.extract("Soup Sieve 2.8 drops Python 3.8 support.")

        self.assertEqual(result.facts[0].change, "dropped")
        self.assertEqual(result.facts[0].python_version, "3.8")
        self.assertEqual(
            extractor.extractor_id,
            "lm-studio:qwen3-4b-instruct-2507:json_schema",
        )

        call = client.completions.calls[0]
        self.assertEqual(call["model"], "qwen3-4b-instruct-2507")
        self.assertEqual(call["temperature"], 0)
        self.assertEqual(call["max_tokens"], 250)
        self.assertEqual(call["response_format"]["type"], "json_schema")
        self.assertIn("<release_notes>", call["messages"][1]["content"])

    def test_uses_json_object_compatibility_mode(self):
        settings = LLMExtractorSettings(
            base_url="http://localhost:12345/v1",
            model="gemma-4-e2b-it",
            response_format_mode="json_object",
        )
        client = _FakeClient(response=_response({"facts": [], "unresolved": []}))
        extractor = LMStudioPythonSupportExtractor(settings, client=client)

        extractor.extract("Documentation was updated.")

        call = client.completions.calls[0]
        self.assertEqual(call["response_format"], {"type": "json_object"})
        self.assertEqual(
            extractor.extractor_id,
            "lm-studio:gemma-4-e2b-it:json_object",
        )

    def test_preserves_no_fact_result(self):
        client = _FakeClient(response=_response({"facts": [], "unresolved": []}))
        extractor = LMStudioPythonSupportExtractor(self.settings, client=client)

        result = extractor.extract("Documentation was updated.")

        self.assertEqual(result.facts, ())
        self.assertEqual(result.unresolved, ())

    def test_rejects_empty_input_before_model_call(self):
        client = _FakeClient(response=_response({"facts": [], "unresolved": []}))
        extractor = LMStudioPythonSupportExtractor(self.settings, client=client)

        with self.assertRaisesRegex(ValueError, "text must not be empty"):
            extractor.extract("   ")

        self.assertEqual(client.completions.calls, [])

    def test_wraps_endpoint_failure(self):
        client = _FakeClient(error=TimeoutError("model stalled"))
        extractor = LMStudioPythonSupportExtractor(self.settings, client=client)

        with self.assertRaisesRegex(LLMExtractionError, "request failed"):
            extractor.extract("Python 3.8 is no longer supported.")

    def test_rejects_malformed_json(self):
        response = SimpleNamespace(
            choices=(SimpleNamespace(message=SimpleNamespace(content="not-json")),)
        )
        extractor = LMStudioPythonSupportExtractor(
            self.settings,
            client=_FakeClient(response=response),
        )

        with self.assertRaisesRegex(LLMExtractionError, "malformed"):
            extractor.extract("Python 3.8 is no longer supported.")

    def test_rejects_schema_invalid_json(self):
        extractor = LMStudioPythonSupportExtractor(
            self.settings,
            client=_FakeClient(
                response=_response(
                    {
                        "facts": [
                            {
                                "change": "removed-later",
                                "python_version": "3.8",
                                "source_quote": "Python 3.8",
                            }
                        ],
                        "unresolved": [],
                    }
                )
            ),
        )

        with self.assertRaisesRegex(LLMExtractionError, "malformed"):
            extractor.extract("Python 3.8 may be removed later.")


if __name__ == "__main__":
    unittest.main()
