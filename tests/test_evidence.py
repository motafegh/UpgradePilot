import json
import unittest

from pydantic import ValidationError

from upgradepilot.case_identity import build_initial_case_record
from upgradepilot.evidence import EvidenceItem, EvidenceSet


BASE_SHA = "652a61ce4f9d7d76eaada31535807a485ece0e21"
HEAD_SHA = "aa2dc024d33f61cdef50bf1973ab5adf0a974f5a"


def _real_case():
    return build_initial_case_record(
        {
            "repository": "pydantic/pydantic",
            "pr_number": 13432,
            "base_sha": BASE_SHA,
            "head_sha": HEAD_SHA,
            "dependency": "soupsieve",
            "old_version": "2.6",
            "new_version": "2.8.4",
            "changed_files": ["uv.lock"],
        }
    )


def _accepted_release_notes() -> EvidenceItem:
    return EvidenceItem(
        evidence_id=" release-notes-001 ",
        kind="upstream_release_notes",
        state="accepted",
        source=" Dependabot-provided upstream release notes ",
        observation=(
            " Soup Sieve 2.8 reports dropping Python 3.8 support "
            "and adding Python 3.14 support. "
        ),
        limitations=(
            " Repository Python support has not been compared. ",
            " Release notes are not repository-specific compatibility proof. ",
        ),
    )


class EvidenceItemTests(unittest.TestCase):
    def test_builds_normalized_accepted_evidence(self) -> None:
        item = _accepted_release_notes()

        self.assertEqual(item.evidence_id, "release-notes-001")
        self.assertEqual(item.source, "Dependabot-provided upstream release notes")
        self.assertEqual(
            item.observation,
            "Soup Sieve 2.8 reports dropping Python 3.8 support "
            "and adding Python 3.14 support.",
        )
        self.assertEqual(
            item.limitations,
            (
                "Repository Python support has not been compared.",
                "Release notes are not repository-specific compatibility proof.",
            ),
        )

    def test_requires_observation_for_accepted_evidence(self) -> None:
        with self.assertRaises(ValidationError) as raised:
            EvidenceItem(
                evidence_id="diff-001",
                kind="dependency_diff",
                state="accepted",
                source="GitHub pull request diff",
            )

        self.assertIn(
            "accepted evidence must contain an observation",
            raised.exception.errors(include_url=False)[0]["msg"],
        )

    def test_represents_missing_evidence_without_inventing_observation(self) -> None:
        item = EvidenceItem(
            evidence_id="python-support-001",
            kind="repository_python_support",
            state="missing",
            source="Repository Python support configuration",
            limitations=(
                "Repository supported Python versions were not collected.",
            ),
        )

        self.assertIsNone(item.observation)
        self.assertEqual(item.state, "missing")

    def test_rejects_missing_evidence_that_claims_an_observation(self) -> None:
        with self.assertRaises(ValidationError) as raised:
            EvidenceItem(
                evidence_id="python-support-001",
                kind="repository_python_support",
                state="missing",
                source="Repository Python support configuration",
                observation="The repository supports Python 3.8.",
                limitations=("Support evidence was not collected.",),
            )

        self.assertIn(
            "missing evidence must not claim an observation",
            raised.exception.errors(include_url=False)[0]["msg"],
        )


class EvidenceSetTests(unittest.TestCase):
    def test_associates_evidence_with_exact_case_and_serializes(self) -> None:
        evidence_set = EvidenceSet(
            case=_real_case(),
            items=(
                _accepted_release_notes(),
                EvidenceItem(
                    evidence_id="python-support-001",
                    kind="repository_python_support",
                    state="missing",
                    source="Repository Python support configuration",
                    limitations=(
                        "Possible Python 3.8 compatibility impact remains unresolved.",
                    ),
                ),
            ),
        )

        serialized = json.loads(evidence_set.model_dump_json())

        self.assertEqual(
            serialized["case"]["snapshot_identity"]["head_sha"],
            HEAD_SHA,
        )
        self.assertEqual(serialized["items"][0]["evidence_id"], "release-notes-001")
        self.assertEqual(serialized["items"][1]["state"], "missing")

    def test_rejects_duplicate_evidence_ids(self) -> None:
        item = _accepted_release_notes()

        with self.assertRaises(ValidationError) as raised:
            EvidenceSet(case=_real_case(), items=(item, item))

        self.assertIn(
            "evidence_id values must be unique",
            raised.exception.errors(include_url=False)[0]["msg"],
        )

    def test_requires_immutable_tuple_of_items(self) -> None:
        with self.assertRaises(ValidationError) as raised:
            EvidenceSet(
                case=_real_case(),
                items=[_accepted_release_notes()],  # type: ignore[arg-type]
            )

        self.assertEqual(
            raised.exception.errors(include_url=False)[0]["type"],
            "tuple_type",
        )


if __name__ == "__main__":
    unittest.main()
