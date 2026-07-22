"""Run the retained experimental detector before normal claim extraction."""

from __future__ import annotations

import argparse
import json

from upgradepilot.evidence import EvidenceItem
from upgradepilot.extraction import PythonSupportExtractionService
from upgradepilot.input_risk import (
    InputRiskDetectionError,
    failed_input_risk_assessment,
    prepare_untrusted_text,
    validate_input_risk_assessment,
)
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

    prepared = prepare_untrusted_text(evidence.observation)
    try:
        candidate_risk = detector.assess(prepared.inspection_text)
        assessment = validate_input_risk_assessment(
            prepared=prepared,
            candidate=candidate_risk,
            detector_id=detector.detector_id,
        )
    except InputRiskDetectionError as exc:
        assessment = failed_input_risk_assessment(
            prepared=prepared,
            detector_id=detector.detector_id,
            error=exc,
        )

    # Screening remains measurable here without controlling the normal service.
    extraction = (
        PythonSupportExtractionService(extractor).extract(evidence)
        if assessment.route == "proceed"
        else None
    )
    print(
        json.dumps(
            {
                "experimental_input_risk": assessment.model_dump(),
                "extraction": (
                    extraction.model_dump() if extraction is not None else None
                ),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
