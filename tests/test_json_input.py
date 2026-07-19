from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import unittest

from upgradepilot.adapters.json_input import InputError, load_analysis_input, parse_analysis_input
from upgradepilot.domain.models import EvidenceState


EXAMPLE_PATH = (
    Path(__file__).resolve().parents[1] / "examples" / "pydantic-13432.bootstrap.json"
)


def example_document() -> dict[str, object]:
    with EXAMPLE_PATH.open(encoding="utf-8") as stream:
        return json.load(stream)


class JsonInputTests(unittest.TestCase):
    def test_bootstrap_example_is_valid(self) -> None:
        analysis_input = load_analysis_input(EXAMPLE_PATH)

        self.assertEqual(analysis_input.case.pull_request_number, 13432)
        self.assertEqual(analysis_input.evidence[1].state, EvidenceState.MISSING)

    def test_unknown_root_key_is_rejected(self) -> None:
        document = example_document()
        document["unexpected"] = True

        with self.assertRaisesRegex(InputError, "unknown keys: unexpected"):
            parse_analysis_input(document)

    def test_duplicate_evidence_ids_are_rejected(self) -> None:
        document = example_document()
        evidence = document["evidence"]
        assert isinstance(evidence, list)
        duplicate = deepcopy(evidence[0])
        evidence.append(duplicate)

        with self.assertRaisesRegex(InputError, "evidence IDs must be unique"):
            parse_analysis_input(document)

    def test_observed_evidence_without_source_is_rejected(self) -> None:
        document = example_document()
        evidence = document["evidence"]
        assert isinstance(evidence, list)
        first = evidence[0]
        assert isinstance(first, dict)
        first["source"] = None

        with self.assertRaisesRegex(InputError, "requires a source"):
            parse_analysis_input(document)

    def test_source_timestamp_requires_timezone(self) -> None:
        document = example_document()
        evidence = document["evidence"]
        assert isinstance(evidence, list)
        first = evidence[0]
        assert isinstance(first, dict)
        source = first["source"]
        assert isinstance(source, dict)
        source["retrieved_at"] = "2026-07-19T12:00:00"

        with self.assertRaisesRegex(InputError, "must include a timezone"):
            parse_analysis_input(document)


if __name__ == "__main__":
    unittest.main()
