import unittest

from scripts.evaluate_python_support_models import (
    _native_models_url,
    _select_model_metadata,
)


class ModelEvaluatorMetadataTests(unittest.TestCase):
    def test_derives_native_metadata_endpoint_from_openai_base_url(self):
        self.assertEqual(
            _native_models_url("http://localhost:12345/v1"),
            "http://localhost:12345/api/v1/models",
        )

    def test_selects_requested_model_and_bounded_metadata(self):
        selected = _select_model_metadata(
            {
                "models": [
                    {
                        "key": "gemma-4-e2b-it",
                        "display_name": "Gemma",
                        "architecture": "gemma4",
                        "quantization": {
                            "name": "Q4_K_M",
                            "bits_per_weight": 4,
                        },
                        "max_context_length": 131072,
                        "capabilities": {"reasoning": True},
                        "loaded_instances": [],
                        "unrelated_server_field": "not preserved",
                    }
                ]
            },
            "gemma-4-e2b-it",
        )

        self.assertEqual(selected["key"], "gemma-4-e2b-it")
        self.assertEqual(selected["architecture"], "gemma4")
        self.assertEqual(selected["quantization"]["name"], "Q4_K_M")
        self.assertNotIn("unrelated_server_field", selected)

    def test_rejects_missing_requested_model(self):
        with self.assertRaisesRegex(ValueError, "expected one metadata entry"):
            _select_model_metadata({"models": []}, "missing-model")

    def test_rejects_invalid_base_url(self):
        with self.assertRaisesRegex(ValueError, "scheme and host"):
            _native_models_url("localhost:12345/v1")


if __name__ == "__main__":
    unittest.main()
