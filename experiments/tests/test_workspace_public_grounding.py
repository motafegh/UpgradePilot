"""Known public-data lifecycle/closure regressions; development evidence only."""

import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch

from experiments.run_workspace_public_grounding import (
    BASE,
    HEAD,
    exact_target_token,
    restore_input_tape,
    run,
)
from experiments.workspace_public_input_tape import PublicInputTape
from experiments.workspace_revision_representation import (
    decode_checkpoint,
    material_closure,
)
from upgradepilot.github.pull_request import GitHubPullRequestClient

INPUTS = (
    Path(__file__).parents[2]
    / "working-memory/evidence/2026-10-08-workspace-experiment3-grounding/public-inputs"
)


class PublicGroundingTests(unittest.TestCase):
    def test_exact_target_ignores_descriptive_metadata_and_distinguishes_new_head(self):
        with patch(
            "requests.sessions.Session.send",
            side_effect=AssertionError("Offline test attempted network"),
        ):
            pr = GitHubPullRequestClient(
                session=PublicInputTape(INPUTS, offline=True)
            ).get_pull_request("pydantic/pydantic", 13432)
        self.assertEqual(
            exact_target_token(pr), exact_target_token(replace(pr, title="New title"))
        )
        self.assertNotEqual(
            exact_target_token(pr), exact_target_token(replace(pr, head_sha="b" * 40))
        )

    def test_known_native_slice_scope_outcome_and_complete_source_basis(self):
        with (
            tempfile.TemporaryDirectory() as directory,
            patch(
                "requests.sessions.Session.send",
                side_effect=AssertionError("Offline test attempted network"),
            ),
        ):
            tape = PublicInputTape(INPUTS, offline=True)
            summary, checkpoint, ledger = run(
                tape, backend="memory", store_root=Path(directory) / "unused"
            )
        self.assertEqual(summary["target"]["base_sha"], BASE)
        self.assertEqual(summary["target"]["head_sha"], HEAD)
        self.assertEqual(summary["native_before"], "unresolved")
        self.assertEqual(summary["native_after"], "established_not_applicable")
        self.assertEqual(summary["requires_python"], ">=3.10")
        self.assertIsNone(summary["native_next_need"])
        self.assertEqual(summary["adequacy"], "unsupported_no_admitted_evaluator")
        revision = decode_checkpoint(checkpoint)
        scopes = {
            record.scope
            for record in revision.records.values()
            if record.kind == "source_text"
        }
        self.assertIn(f"pydantic/pydantic@{BASE}:uv.lock", scopes)
        self.assertIn(f"pydantic/pydantic@{HEAD}:uv.lock", scopes)
        self.assertIn(f"pydantic/pydantic@{HEAD}:pyproject.toml", scopes)
        self.assertFalse(any("example/project" in scope for scope in scopes))
        self.assertEqual(len(ledger.files), 4)
        closure = set(material_closure(revision))
        self.assertTrue({f"http:{i}" for i in range(14)} <= closure)
        self.assertTrue(
            {
                "capture:manifest:before",
                "capture:manifest:complete",
                "method:known-source",
            }
            <= closure
        )
        for key in ledger.files:
            self.assertTrue(revision.records[key].dependencies, key)

    def test_sqlite_recovery_reconstructs_native_inputs_without_external_tape(self):
        with (
            tempfile.TemporaryDirectory() as directory,
            patch(
                "requests.sessions.Session.send",
                side_effect=AssertionError("Offline test attempted network"),
            ),
        ):
            root = Path(directory)
            expected, checkpoint, _ = run(
                PublicInputTape(INPUTS, offline=True),
                backend="sqlite",
                store_root=root / "store",
            )
            restore_input_tape(checkpoint, root / "recovered-inputs")
            actual, replayed, _ = run(
                PublicInputTape(root / "recovered-inputs", offline=True),
                backend="memory",
                store_root=root / "unused",
            )
            self.assertEqual(actual, expected)
            self.assertEqual(replayed, checkpoint)

    def test_missing_captured_body_does_not_become_source_absence_or_network_fallback(
        self,
    ):
        with (
            tempfile.TemporaryDirectory() as directory,
            patch(
                "requests.sessions.Session.send",
                side_effect=AssertionError("Unexpected network"),
            ),
        ):
            root = Path(directory)
            (root / "manifest.json").write_bytes(
                (INPUTS / "manifest.json").read_bytes()
            )
            tape = PublicInputTape(root, offline=True)
            url = tape.entries[0]["url"]
            with self.assertRaises(FileNotFoundError):
                tape.get(url)
            self.assertEqual(tape.cursor, 0)

    def test_wrong_url_authentication_and_external_action_refused_before_egress(self):
        with patch(
            "requests.sessions.Session.send",
            side_effect=AssertionError("Unexpected network"),
        ):
            for method, url, headers in (
                ("GET", "https://api.github.com/repos/wrong/target/pulls/1", {}),
                (
                    "POST",
                    "https://api.github.com/repos/pydantic/pydantic/issues/13432/comments",
                    {},
                ),
                ("GET", "https://example.invalid/unknown", {}),
                (
                    "GET",
                    "https://api.github.com/repos/pydantic/pydantic/pulls/13432",
                    {"Authorization": "Bearer synthetic-test-value"},
                ),
            ):
                tape = PublicInputTape(INPUTS, offline=True)
                with (
                    self.subTest(method=method, url=url),
                    self.assertRaises(ValueError),
                ):
                    tape.request(method, url, headers=headers)
                self.assertEqual(tape.cursor, 0)

    def test_content_digest_mismatch_refuses_native_reexecution(self):
        with (
            tempfile.TemporaryDirectory() as directory,
            patch(
                "requests.sessions.Session.send",
                side_effect=AssertionError("Unexpected network"),
            ),
        ):
            root = Path(directory)
            manifest = json.loads((INPUTS / "manifest.json").read_text())
            (root / "manifest.json").write_text(json.dumps(manifest))
            (root / manifest["requests"][0]["body"]).write_bytes(
                b'{"substituted":true}'
            )
            tape = PublicInputTape(root, offline=True)
            with self.assertRaisesRegex(ValueError, "digest mismatch"):
                tape.get(tape.entries[0]["url"])
            self.assertEqual(tape.cursor, 0)


if __name__ == "__main__":
    unittest.main()
