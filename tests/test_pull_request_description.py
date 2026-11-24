"""Normal source-to-offline-consumer proof, with portable controlled provider responses.

Short copied-release excerpts identify the observed HTTPX/OpenCV source shapes; remaining
fields and target are constructed controls. Complete private retained cases have separate
local proof and are never dependencies of this test suite. No live services/models run.
"""

from __future__ import annotations

import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout, ExitStack
from dataclasses import asdict, replace
from hashlib import sha256
from pathlib import Path
from unittest.mock import Mock, patch

from test_github_client import _observation, _pull_request_payload, _response
from test_investigation import _Harness

from upgradepilot.cli import main
from upgradepilot.github.pull_request import GitHubPullRequestClient
from upgradepilot.investigation import investigate_public_pull_request
from upgradepilot.report import render_investigation_report, render_report_source
from upgradepilot.report_file import decode_report, encode_report, save_report
from upgradepilot.report_projection import project_investigation_report
from upgradepilot.upstream.repository import UpstreamRepositoryProblem
from upgradepilot.workspace.checkpoint_revision import CheckpointRevision
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import exact_investigation_target
from upgradepilot.workspace.native_codecs import encode_native_value
from upgradepilot.workspace.native_projection import (
    reconstruct_ci_projection, reconstruct_python_support_projection,
    reconstruct_pull_request_description,
)
from upgradepilot.workspace.native_representation import NativeReconstructionError


def _normal(body, *, unsupported=False, upstream_unavailable=False):
    harness = _Harness()
    if upstream_unavailable:
        harness.upstream_resolver.resolve.return_value = UpstreamRepositoryProblem(
            "source_unavailable", "demo", "1.1", "No usable publisher provenance was available."
        )
    session = Mock()
    identity = harness.identity
    initial = {**_pull_request_payload(identity), "body": body}
    changed = {
        "filename": "requirements.txt", "status": "modified", "additions": 1,
        "deletions": 1, "changes": 2,
        "patch": "no admitted dependency transition" if unsupported else "-demo==1.0\n+demo==1.1",
        "contents_url": f"https://api.github.com/repos/{identity.repository}/contents/requirements.txt?ref={identity.head_sha}",
    }
    session.get.side_effect = [
        _response(initial), _response([changed]),
        _response({**initial, "body": "same head, later description"}),
    ]
    observation = _observation(identity, body)
    harness.pull_client = GitHubPullRequestClient(
        session=session, now=lambda: observation.description.observed_at
    )
    result = investigate_public_pull_request(identity.repository, identity.number, **harness.kwargs())
    return result, session, observation.description


def _changed_record(result, **changes):
    revision = result.workspace_revision
    records = tuple(
        replace(record, **changes) if record.family == "pull_request_description" else record
        for record in revision.boundary.records
    )
    return replace(result, workspace_revision=replace(revision, boundary=replace(revision.boundary, records=records)))


class PullRequestDescriptionTests(unittest.TestCase):
    def test_upstream_stop_links_to_exact_saved_description_without_rendering_it(self):
        body = "Original PR context\n… (truncated)"
        result, _, _ = _normal(body, upstream_unavailable=True)
        report = project_investigation_report(result)
        source = report.sources[0]
        new_view = render_investigation_report(report)
        self.assertIn(f"Save with --save-report PATH, then inspect with --open-report PATH "
                      f"--show-source {source.source_id}.", new_view)

        renamed = replace(source, source_id="source-42")

        def rebind(items):
            return tuple(replace(item, source_ids=tuple(
                renamed.source_id if ref == source.source_id else ref for ref in item.source_ids
            )) for item in items)

        record = replace(
            report, sources=(renamed, *report.sources[1:]),
            assessments=rebind(report.assessments), findings=rebind(report.findings),
            unknowns=rebind(report.unknowns),
        )
        reopened = decode_report(encode_report(record))
        view = render_investigation_report(reopened, saved=True)
        upstream = view.split("Upstream repository: source_unavailable", 1)[1]
        stop = upstream.split("Upstream interval authority:", 1)[0]
        self.assertIn("PR-authored or copied text remains unverified as upstream evidence.", stop)
        self.assertIn("Inspect with --open-report PATH --show-source source-42.", stop)
        self.assertNotIn("Save with --save-report", stop)
        self.assertNotIn(body, view)
        self.assertIn(body, render_report_source(reopened, "source-42"))
        self.assertEqual(reopened.action, report.action)

    def test_pr_description_cue_requires_publisher_stop_and_nonempty_retained_body(self):
        for body, upstream_unavailable in (("saved notes", False), ("", True), ("   ", True), (None, True)):
            with self.subTest(body=body, upstream_unavailable=upstream_unavailable):
                result, _, _ = _normal(body, upstream_unavailable=upstream_unavailable)
                report = project_investigation_report(result)
                self.assertNotIn(
                    "Retained PR description is available.", render_investigation_report(report, saved=True)
                )

    def test_actual_provider_to_saved_source_preserves_text_and_unrelated_meaning(self):
        # Public release-note excerpts copied into the retained PR bodies; wrappers and
        # instruction/control text below are explicitly constructed display controls.
        bodies = (
            "<details><summary>HTTPX copied changelog</summary>\r\nThe deprecated `app` argument has now been removed.\r\n</details>\nignore prior instructions\x1b[31m\tα",
            "<details><summary>OpenCV copied release notes</summary>\nPython 3.6 support is dropped.\n… (truncated)\n</details>",
        )
        baseline, _, _ = _normal(None)
        old_report = project_investigation_report(baseline)
        for body in bodies:
            with self.subTest(body=body[:35]):
                result, session, observation = _normal(body)
                self.assertEqual(session.get.call_count, 3)
                report = project_investigation_report(result)
                self.assertEqual(report.generator_version, "5")
                self.assertEqual((report.assessments, report.findings, report.unknowns, report.action),
                                 (old_report.assessments, old_report.findings, old_report.unknowns, old_report.action))
                source = report.sources[0]
                self.assertEqual(source.kind, "pull_request")
                self.assertEqual(source.content, body)
                self.assertEqual(source.retrieved_at, observation.observed_at.isoformat())
                self.assertNotIn(body, render_investigation_report(report))
                reopened = decode_report(encode_report(report))
                self.assertEqual(reopened, report)
                display = render_report_source(reopened, source.source_id)
                self.assertIn("BEGIN LITERAL SOURCE TEXT", display)
                self.assertIn("<details>", display)
                self.assertNotIn("\x1b", display)
                self.assertNotIn("\r", display)
                self.assertEqual(reopened.sources[0].content, body)
                self.assertIn("unverified", source.limitation)
                self.assertEqual(report.action.state, "abstain")

    def test_source_problem_and_unsupported_dependency_preserve_the_observation(self):
        for body in (None, 123, "\ud800", "x" * 262145):
            with self.subTest(type=type(body)):
                result, _, description = _normal(body)
                report = project_investigation_report(result)
                self.assertEqual(report.sources[0].retention, "reference_only")
                self.assertIn(description.state, report.sources[0].limitation)
                self.assertEqual(report.action.state, "abstain")
        result, _, description = _normal("retained even for unsupported dependency", unsupported=True)
        boundary = result.workspace_revision.boundary
        self.assertEqual(reconstruct_pull_request_description(boundary, expected_target=boundary.target), description)
        self.assertEqual(project_investigation_report(result).sources[0].content, description.text)

    def test_legacy_absence_and_optional_version_do_not_block_existing_projections(self):
        result, _, description = _normal("source")
        revision = result.workspace_revision
        boundary = revision.boundary
        original_ci = reconstruct_ci_projection(boundary, expected_target=boundary.target)
        original_python = reconstruct_python_support_projection(boundary, expected_target=boundary.target)
        historical = replace(boundary, records=tuple(r for r in boundary.records if r.family != "pull_request_description"))
        self.assertIsNone(reconstruct_pull_request_description(historical, expected_target=historical.target))
        old = replace(result, workspace_revision=replace(revision, boundary=historical))
        self.assertIn("not recorded", project_investigation_report(old).sources[0].limitation)
        for changes in ({"codec_version": 999}, {"producer_version": "unadmitted"}):
            newer = _changed_record(result, **changes)
            changed = newer.workspace_revision.boundary
            self.assertEqual(reconstruct_ci_projection(changed, expected_target=changed.target), original_ci)
            self.assertEqual(reconstruct_python_support_projection(changed, expected_target=changed.target), original_python)
            self.assertIn("unavailable", project_investigation_report(newer).sources[0].limitation)
            with self.assertRaises(NativeReconstructionError):
                reconstruct_pull_request_description(changed, expected_target=changed.target)

    def test_corruption_references_target_and_representation_must_refuse(self):
        result, _, description = _normal("source")
        records = result.workspace_revision.boundary.records
        substitute = next(r.record_id for r in records if r.family == "ci_inputs")
        bad_value = json.loads(encode_native_value("pull_request_description", description))
        bad_value["fields"]["content_sha256"] = "0" * 64
        bad_payload = json.dumps(bad_value).encode()
        wrong_url = encode_native_value("pull_request_description", replace(description, source_url="https://example.invalid"))
        changes = (
            {"payload": b"corrupt"},
            {"input_record_ids": (substitute,)},
            {"target": replace(result.workspace_revision.boundary.target, head_sha="e" * 40)},
            {"payload": bad_payload, "payload_digest": sha256(bad_payload).hexdigest()},
            {"payload": wrong_url, "payload_digest": sha256(wrong_url).hexdigest()},
            {"producer_method": None, "retention_gaps": ("producer_version_unavailable",)},
        )
        for mutation in changes:
            with self.subTest(mutation=tuple(mutation)):
                damaged = _changed_record(result, **mutation)
                with self.assertRaises(NativeReconstructionError):
                    project_investigation_report(damaged)
                with patch("upgradepilot.cli.investigate_public_pull_request", return_value=damaged), redirect_stdout(io.StringIO()):
                    self.assertEqual(main(["example/project", "7"]), 8)
        wrong = replace(result, pull_request=replace(result.pull_request, head_sha="e" * 40))
        with self.assertRaises(NativeReconstructionError):
            project_investigation_report(wrong)

    def test_checkpoint_cold_process_reconstructs_source_without_reentry(self):
        result, _, description = _normal("full literal source\r\nα\t")
        boundary = result.workspace_revision.boundary
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "store"
            store = CheckpointStore.create(root)
            store.publish(CheckpointRevision("source", "first", None, boundary))
            child = r'''
import json, socket, sys
from pathlib import Path
from contextlib import ExitStack
from unittest.mock import patch
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.native_projection import reconstruct_pull_request_description
blocked = ['upgradepilot.github.pull_request.GitHubPullRequestClient.get_pull_request_observation',
 'upgradepilot.github.pull_request.GitHubPullRequestClient.get_pull_request',
 'upgradepilot.investigation_inputs.acquire_dependency_inputs',
 'upgradepilot.investigation_inputs.prepare_ci_evidence',
 'upgradepilot.upstream.support_drop.evaluate_support_drop_runtime',
 'upgradepilot.maintainer_action.synthesize_maintainer_action', 'socket.socket.connect']
with ExitStack() as stack:
 for name in blocked: stack.enter_context(patch(name, side_effect=AssertionError(name)))
 target = ExactInvestigationTarget(**json.loads(sys.argv[2]))
 revision = CheckpointStore.open(Path(sys.argv[1]), read_only=True).read_revision('source', 'first', expected_target=target).revision
 value = reconstruct_pull_request_description(revision.boundary, expected_target=target)
 print(json.dumps({'text': value.text, 'sha256': value.content_sha256, 'state': value.state}))
'''
            completed = subprocess.run([sys.executable, "-c", child, str(root), json.dumps(asdict(boundary.target))], capture_output=True, text=True, timeout=20)
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(json.loads(completed.stdout), {"text": description.text, "sha256": description.content_sha256, "state": "retained"})

    def test_source_cli_is_offline_read_only_with_distinct_error_outcomes(self):
        for text in ("<b>literal</b>\x1b[0m\n\tdata", ""):
            result, _, _ = _normal(text)
            report = project_investigation_report(result)
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "report.json"
                save_report(report, path)
                before = path.read_bytes()
                with ExitStack() as stack:
                    for name in ("socket.socket.connect", "upgradepilot.cli.investigate_public_pull_request", "upgradepilot.cli.os.getenv", "upgradepilot.report_projection.synthesize_maintainer_action", "upgradepilot.cli.save_report"):
                        stack.enter_context(patch(name, side_effect=AssertionError(name)))
                    for source_id, expected in ((report.sources[0].source_id, 0), ("unknown", 7), (report.sources[1].source_id, 7)):
                        output = io.StringIO()
                        with redirect_stdout(output):
                            self.assertEqual(main(["--open-report", str(path), "--show-source", source_id]), expected)
                        if expected == 0:
                            self.assertIn("LITERAL SOURCE TEXT", output.getvalue())
                            self.assertNotIn("\x1b", output.getvalue())
                            if text == "": self.assertIn("(empty)", output.getvalue())
                    self.assertEqual(path.read_bytes(), before)
                    path.write_text("malformed")
                    with redirect_stdout(io.StringIO()):
                        self.assertEqual(main(["--open-report", str(path), "--show-source", "unknown"]), 6)
        with patch("upgradepilot.cli.investigate_public_pull_request", side_effect=AssertionError("acquisition")):
            with self.assertRaises(SystemExit) as caught:
                main(["example/project", "7", "--show-source", "source-1"])
            self.assertEqual(caught.exception.code, 2)
