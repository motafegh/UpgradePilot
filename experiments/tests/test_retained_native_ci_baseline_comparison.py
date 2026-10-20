"""Comparison input isolation, literal translation and retained-native seam proof.

All executable fixtures are synthetic or existing mocked product capture fixtures.
No retained comparison row, model, public acquisition or target code is run here.
"""

import dataclasses
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from experiments import retained_native_ci_baseline_comparison as comparison
from upgradepilot.workspace.checkpoint_revision import CheckpointRevision, CheckpointStorageError
from upgradepilot.workspace.checkpoint_store import CheckpointStore


class TransparentBaselineTests(unittest.TestCase):
    def test_first_matching_rule_precedence_and_residual_uncertainty(self):
        cases = (
            ("major", "mixed", "unknown", "removed", "B01", "investigate_or_block"),
            ("major", "missing", "unknown", "removed", "B02", "run_targeted_checks"),
            ("major", "passing", "unknown", "removed", "B03", "run_targeted_checks"),
            ("major", "passing", "direct", "", "B04", "run_targeted_checks"),
            ("pre_release", "passing", "direct", "", "B04", "run_targeted_checks"),
            ("replacement_or_unknown", "passing", "direct", "", "B04", "run_targeted_checks"),
            ("minor", "passing", "direct", "No breaking changes", "B04", "run_targeted_checks"),
            ("patch", "passing", "transitive", "", "B05", "merge_after_normal_review"),
            ("unclassifiable", "passing", "direct", "", "B06", "abstain"),
        )
        for category, ci, directness, text, rule, outcome in cases:
            with self.subTest(rule=rule, category=category):
                result = comparison.evaluate_baseline(comparison.BaselineInputs(category, ci, directness, text))
                self.assertEqual((result["matched_rule_id"], result["outcome"]), (rule, outcome))

    def test_benefit_keywords_are_literal_and_cannot_change_action(self):
        for ci in ("failing", "missing", "passing"):
            plain = comparison.BaselineInputs("patch", ci, "direct", "")
            favorable = dataclasses.replace(plain, release_note_text="CVE Security FIXED bugfix")
            a, b = map(comparison.evaluate_baseline, (plain, favorable))
            self.assertEqual(a["outcome"], b["outcome"])
            self.assertEqual(b["keyword_matches"]["benefit"], ["security", "cve", "fixed", "bugfix"])

    def test_baseline_has_no_access_to_native_or_raw_source(self):
        with (
            patch.object(comparison, "read_json", side_effect=AssertionError("raw input leak")),
            patch.object(comparison, "reconstruct_ci_projection", side_effect=AssertionError("native leak")),
        ):
            result = comparison.evaluate_baseline(comparison.BaselineInputs("minor", "passing", "direct", ""))
        self.assertEqual(result["matched_rule_id"], "B05")
        self.assertEqual(result["full_investigation_outcome"]["status"], "unavailable")


class LiteralTranslationTests(unittest.TestCase):
    def test_unique_release_section_preserves_whitespace_entities_and_exact_span(self):
        block = "<details>\n<summary>Release notes</summary>\n<p>Fix &amp; <code>foo</code>\nbar</p>\n</details>"
        body = "Caution breaking outside\n" + block + "\n<details><summary>Commands</summary>removed</details>"
        text, identity = comparison.extract_release_notes(body)
        self.assertEqual(text, "\nFix & foo\nbar\n")
        start, end = identity["section_character_span"]
        self.assertEqual(body[start:end], block)
        self.assertEqual(identity["raw_section_sha256"], hashlib.sha256(block.encode()).hexdigest())
        self.assertNotIn("breaking", text)
        self.assertNotIn("removed", text)

    def test_missing_duplicate_unclosed_or_nested_release_sections_refuse(self):
        block = "<details><summary>Release notes</summary>fixed</details>"
        for body in ("fixed", block + block, block[:-10], "<details>" + block + "</details>"):
            with self.subTest(body=body), self.assertRaises(comparison.InputUnavailable):
                comparison.extract_release_notes(body)

    def test_translation_uses_exact_captured_pr_query_and_requirement_patch(self):
        target = {
            'repository': 'owner/repo',
            'pull_number': 7,
            'base_sha': 'base',
            'head_sha': 'head',
            'normalized_package': 'demo',
            'old_version': '1.2.3',
            'proposed_version': '1.2.4',
        }
        selection = {"directory": "case", "target": target}
        prefix = "https://api.github.com/repos/owner/repo"
        pr_url = prefix + "/pulls/7"
        records = [
            {
                'url': pr_url,
                'status': 200,
                'body': json.dumps({'number': 7, 'base': {'sha': 'base', 'repo': {'full_name': 'owner/repo'}}, 'head': {'sha': 'head'}, 'body': '<details><summary>Release notes</summary>fixed</details>'}),
            },
            {
                'url': pr_url + '/files?per_page=100&page=1',
                'status': 200,
                'body': json.dumps([{'filename': 'requirements-dev.txt', 'patch': '@@\n-demo==1.2.3\n+demo==1.2.4'}]),
            },
            {
                'url': prefix + '/actions/runs?event=pull_request&head_sha=head&per_page=100&page=1',
                'status': 200,
                'body': json.dumps({'total_count': 0, 'workflow_runs': []}),
            },
        ]
        with patch.object(comparison, "read_json", return_value=records):
            inputs, identity = comparison.translate_case(Path("unused"), selection)
            self.assertEqual((inputs.ci_conclusion, inputs.dependency_directness, inputs.version_category), ("missing", "direct", "patch"))
            self.assertIn("not historical CI absence", identity["ci_source"]["limit"])
            wrong = dict(selection, target=dict(target, base_sha="other"))
            with self.assertRaises(comparison.InputUnavailable):
                comparison.translate_case(Path("unused"), wrong)

    def test_changed_hash_and_size_refuse(self):
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "input"
            source.write_bytes(b"original")
            expected = comparison.digest(source.read_bytes())
            source.write_bytes(b"replaced")
            with self.assertRaises(comparison.InputUnavailable):
                comparison.require_hash(source, expected)
            with self.assertRaises(comparison.InputUnavailable):
                comparison.require_hash(source, comparison.digest(b"replaced"), 99)


class NativeCopyTests(unittest.TestCase):
    def test_changed_frozen_identity_refuses_before_any_arm_or_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            freeze = root / "freeze.json"
            freeze.write_text(json.dumps({"root": str(root), "identity": "accepted"}))
            with (
                patch.object(comparison, "prepare", return_value={"identity": "changed"}),
                patch.object(comparison.subprocess, "run", side_effect=AssertionError("arm ran")),
                self.assertRaises(comparison.InputUnavailable),
            ):
                comparison.run(freeze, root / "output", root / "private")
            self.assertFalse((root / "output").exists())

    def test_failed_row_is_retained_once_and_other_row_can_complete(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            frozen = {
                'root': str(root),
                'cases': [
                    {'case_id': 'first', 'directory': 'case-1'},
                    {'case_id': 'second', 'directory': 'case-2'},
                ],
            }
            freeze = root / "freeze.json"
            freeze.write_bytes(comparison.json_bytes(frozen))
            first = subprocess.CompletedProcess([], 2, b"", b"unsupported retained input")
            second = subprocess.CompletedProcess([], 0, b'{"case_id":"second","status":"completed"}', b"")
            with (
                patch.object(comparison, "prepare", return_value=frozen),
                patch.object(comparison, "verify_inputs"),
                patch.object(comparison.subprocess, "run", side_effect=[first, second]) as children,
            ):
                result = comparison.run(freeze, root / "output", root / "private")
            self.assertEqual(children.call_count, 2)
            self.assertEqual(result["counts"]["input_unavailable"], 1)
            self.assertEqual(result["counts"]["completed"], 1)
            self.assertIn("unsupported retained input", result["rows"][0]["stderr"])
            self.assertEqual(result, comparison.read_json(root / "output/results.json"))

    def test_unresolved_native_state_survives_copy_without_rederivation_or_original_mutation(self):
        # Existing product proof fixture uses mocked acquisition, not retained case inputs.
        from test_workspace_native_reconstruction import captured_case

        _, _, boundary, expected, _ = captured_case(command_variant="ambient")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            store = CheckpointStore.create(root / "source")
            revision = CheckpointRevision("lineage", "selected", None, boundary)
            store.publish(revision)
            selection = {
                'lineage_id': 'lineage',
                'revision_id': 'selected',
                'target': dataclasses.asdict(boundary.target),
                'checkpoint_digest': revision.digest(),
            }
            before = (store.directory / "workspace.sqlite3").read_bytes()
            with (
                patch("upgradepilot.ci.dependency_exercise.evaluate_dependency_ci_coverage", side_effect=AssertionError("fresh CI evaluation")),
                patch("upgradepilot.ci.dependency_state.evaluate_runtime_dependency_state", side_effect=AssertionError("fresh runtime evaluation")),
            ):
                projection, retention = comparison.reconstruct_on_copy(store.directory, root / "copy", selection)
            self.assertEqual(projection, expected)
            summary = comparison.summarize_projection(projection)
            self.assertTrue(any(a["state"] == "unresolved" for a in summary["runtime_dependency_state"]["assessments"]))
            self.assertEqual(summary["maintainer_action"]["status"], "unavailable")
            self.assertEqual(before, (store.directory / "workspace.sqlite3").read_bytes())
            self.assertEqual(retention["original_sha256"], retention["copy_sha256_after"])
            wrong = dict(selection, target=dict(selection["target"], head_sha="other"))
            with self.assertRaises(CheckpointStorageError):
                comparison.reconstruct_on_copy(store.directory, root / "wrong-copy", wrong)

    def test_actual_network_and_process_entry_are_blocked_in_child(self):
        program = '''
import socket, subprocess, sys
from experiments.retained_native_ci_baseline_comparison import _offline_audit
sys.addaudithook(_offline_audit)
for action in (lambda: socket.socket(), lambda: subprocess.run([sys.executable, '-c', 'pass'])):
    try: action()
    except RuntimeError as error: assert 'Offline comparison forbids' in str(error)
    else: raise AssertionError('guard inactive')
print('blocked')
'''
        child = subprocess.run([sys.executable, "-c", program], capture_output=True, text=True, timeout=10)
        self.assertEqual(child.returncode, 0, child.stderr)
        self.assertEqual(child.stdout.strip(), "blocked")


if __name__ == "__main__":
    unittest.main()
