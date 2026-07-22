"""Run one local pre-screened Python-support extraction demonstration."""

from __future__ import annotations

import argparse

from upgradepilot.evidence import EvidenceItem
from upgradepilot.extraction import PythonSupportExtractionService
from upgradepilot.llm_extractor import (
    LLMExtractorSettings,
    LMStudioPythonSupportExtractor,
)
from upgradepilot.llm_input_risk_detector import LMStudioInputRiskDetector


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    parser.add_argument(
        "--detector-model",
        default="qwen3-4b-instruct-2507",
    )
    parser.add_argument(
        "--extractor-model",
        default="gemma-4-e2b-it",
    )
    parser.add_argument("--base-url", default="http://localhost:12345/v1")
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--max-tokens", type=int, default=768)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    detector = LMStudioInputRiskDetector(
        LLMExtractorSettings(
            base_url=args.base_url,
            model=args.detector_model,
            timeout_seconds=args.timeout,
            max_tokens=args.max_tokens,
            seed=args.seed,
        )
    )
    extractor = LMStudioPythonSupportExtractor(
        LLMExtractorSettings(
            base_url=args.base_url,
            model=args.extractor_model,
            timeout_seconds=args.timeout,
            max_tokens=args.max_tokens,
            seed=args.seed,
        )
    )
    evidence = EvidenceItem(
        evidence_id="screened-demo-release-notes",
        kind="upstream_release_notes",
        state="accepted",
        source="Local screened-extraction demonstration",
        observation=args.text,
        limitations=("Demonstration input; upstream truth is not established.",),
    )

    result = PythonSupportExtractionService(
        extractor,
        detector,
    ).extract(evidence)
    print(result.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
