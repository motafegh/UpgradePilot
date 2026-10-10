"""Production native capture/cold projection proofs with controlled external evidence.

Reuse the normal investigation harness's typed extraction answer, disclosed as controlled.
CI/runtime and target/impact owners execute normally once. Independent test-only rendering
compares every native field; it is not a product serialization/reconstruction mechanism.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from dataclasses import fields, is_dataclass, replace
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch

from packaging.version import Version
from test_investigation import _dependency, _Harness

from upgradepilot.ci.dependency_exercise import WorkflowDependencyCoverageInput
from upgradepilot.ci.native_codec import LAYOUTS as CI_LAYOUTS
from upgradepilot.dependency.analysis import DependencyChangeAnalysis
from upgradepilot.dependency.change import DependencyChangeProblem
from upgradepilot.dependency.environment import RequirementsFileDependencyContext
from upgradepilot.github.actions import WorkflowStep
from upgradepilot.github.repository import UnavailableRepositoryFile
from upgradepilot.impact.python_support_codec import LAYOUTS as IMPACT_LAYOUTS
from upgradepilot.investigation import investigate_public_pull_request
from upgradepilot.upstream.claim import GroundedPythonSupportDropClaim
from upgradepilot.upstream.interval import release_interval_from_dependency_change
from upgradepilot.workspace.native_boundary import (
    encode_native_boundary,
    read_native_boundary,
)
from upgradepilot.workspace.native_capture import NativeInvestigationCapture
from upgradepilot.workspace.native_codecs import encode_native_value
from upgradepilot.workspace.native_inputs_codec import LAYOUTS as INPUT_LAYOUTS
from upgradepilot.workspace.native_projection import (
    CINativeProjection,
    NativeInvestigationInputs,
    PythonSupportNativeProjection,
    reconstruct_ci_projection,
    reconstruct_python_support_projection,
)
from upgradepilot.workspace.native_representation import NativeReconstructionError
from upgradepilot.workspace import native_representation

_WORKFLOW = """name: CI
jobs:
  test:
    name: Test
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Install
        run: PIP_DRY_RUN=0 PIP_CONFIG_FILE=/dev/null PIP_TARGET= PIP_PREFIX= PIP_ROOT= PIP_ONLY_DEPS=0 PIP_ONLY_DEPENDENCIES=0 /opt/bootstrap/bin/python -m pip --python /opt/target/bin/python install --no-user --no-deps -r requirements.txt
"""


def independent_native_values(value):
    """Complete test-only comparison oracle, independent of the admitted codec layouts."""
    if is_dataclass(value) and not isinstance(value, type):
        return {
            "native_type": type(value).__name__,
            "fields": {
                field.name: independent_native_values(getattr(value, field.name))
                for field in fields(value)
            },
        }
    if isinstance(value, tuple):
        return {"tuple": [independent_native_values(item) for item in value]}
    if isinstance(value, datetime):
        return {"datetime": value.isoformat(), "fold": value.fold}
    if isinstance(value, Version):
        return {"version": str(value)}
    if value is None or type(value) in (str, int, bool):
        return value
    raise AssertionError(f"Unhandled independent native value: {type(value)}")


def captured_case(
    *, command_variant="positive", python_variant="outside", dependency_problem=False
):
    h = _Harness()
    dependency = _dependency()
    context = RequirementsFileDependencyContext(
        repository=h.identity.repository,
        revision=h.identity.head_sha,
        normalized_package=dependency.normalized_package,
        source_evidence=dependency.source_evidence[0],
    )
    workflow = _WORKFLOW
    if command_variant == "dry_run":
        workflow = workflow.replace("PIP_DRY_RUN=0", "PIP_DRY_RUN=1")
    elif command_variant == "ambient":
        workflow = workflow.replace("PIP_CONFIG_FILE=/dev/null ", "")
    h.set_workflow(workflow, job_names=("Test",))
    jobs = h.actions_client.get_workflow_jobs.return_value
    h.actions_client.get_workflow_jobs.return_value = tuple(
        replace(
            job,
            steps=(
                WorkflowStep(
                    number=1, name="Checkout", status="completed", conclusion="success"
                ),
                WorkflowStep(
                    number=2, name="Install", status="completed", conclusion="success"
                ),
            ),
        )
        for job in jobs
    )
    if python_variant != "no_claim":
        h.support_drop_evaluator.return_value = GroundedPythonSupportDropClaim(
            python_line="3.9",
            introduced_in_version=dependency.proposed_version,
            interval=release_interval_from_dependency_change(dependency),
            source_evidence=(),
        )
    source = h.repository_client.get_exact_head_text_file.return_value
    if python_variant == "overlap":
        source = replace(source, content='[project]\nrequires-python = ">=3.9"\n')
    elif python_variant == "unresolved":
        source = replace(source, content='[project]\nname = "demo"\n')
    elif python_variant == "unavailable":
        source = UnavailableRepositoryFile(
            source.repository,
            source.path,
            source.revision,
            "file_unavailable",
            "Controlled acquisition failure.",
        )
    h.repository_client.get_exact_head_text_file.return_value = source
    analysis = DependencyChangeAnalysis(dependency, (context,))
    if dependency_problem:
        analysis = DependencyChangeProblem(
            "no_supported_dependency_file", "No supported dependency source."
        )
    capture = NativeInvestigationCapture()
    with patch(
        "upgradepilot.investigation.analyze_dependency_change", return_value=analysis
    ):
        original = investigate_public_pull_request(
            "example/project", 7, native_capture=capture, **h.kwargs()
        )
    boundary = capture.snapshot()
    inputs = NativeInvestigationInputs(
        original.pull_request,
        original.changed_files,
        original.dependency_result,
        () if dependency_problem else (context,),
    )
    expected_workflows = (
        ()
        if dependency_problem
        else (
            WorkflowDependencyCoverageInput(
                run=h.workflow_run,
                jobs=h.actions_client.get_workflow_jobs.return_value,
                definition=h.repository_client.get_exact_head_workflow_file.return_value,
            ),
        )
    )
    expected_ci = CINativeProjection(
        inputs,
        expected_workflows,
        original.ci_coverage_result,
        original.runtime_dependency_state_result,
    )
    expected_python = PythonSupportNativeProjection(
        inputs,
        original.upstream_interval_result,
        original.upstream_support_drop_result,
        source if original.target_python_result is not None else None,
        original.target_python_result,
        original.target_python_relevance_result,
        original.python_support_drop_pre_investigation_result,
        original.python_support_drop_investigation_selection,
        original.python_support_drop_impact_result,
    )
    return h, original, boundary, expected_ci, expected_python


def altered_record(boundary, family, **changes):
    records = tuple(
        replace(record, **changes) if record.family == family else record
        for record in boundary.records
    )
    return replace(boundary, records=records)


_RECOVERY_CHILD = r"""
import json, socket, sys
from pathlib import Path
from unittest.mock import patch
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget, read_native_boundary
from upgradepilot.workspace.native_projection import reconstruct_ci_projection, reconstruct_python_support_projection
from upgradepilot.ci.dependency_state import evaluate_runtime_dependency_state
from upgradepilot.github.repository import GitHubRepositoryClient
from upgradepilot.upstream.support_drop import evaluate_support_drop_runtime
from upgradepilot.maintainer_action import synthesize_maintainer_action
from upgradepilot.workspace.native_representation import NativeReconstructionError
from test_workspace_native_reconstruction import independent_native_values

# The guard watches actual Python re-entry, independent of injected clients/call counters.
# Generated native constructors/equality are representation operations, not evaluations.
forbidden = {
    'upgradepilot.investigation', 'upgradepilot.dependency.analysis',
    'upgradepilot.ci.dependency_state', 'upgradepilot.ci.dependency_exercise',
    'upgradepilot.impact.python_support', 'upgradepilot.impact.applicability',
    'upgradepilot.target.python', 'upgradepilot.target.relevance',
    'upgradepilot.target.python_specifier', 'upgradepilot.upstream.support_drop',
    'upgradepilot.upstream.claim', 'upgradepilot.upstream.interval',
    'upgradepilot.maintainer_action', 'upgradepilot.github.api',
    'upgradepilot.github.repository', 'upgradepilot.github.actions',
    'upgradepilot.pypi.release',
}
def guard(frame, event, arg):
    if event == 'call':
        module = frame.f_globals.get('__name__') or ''
        name = frame.f_code.co_name
        # Existing RepositoryTextFile constructors enforce representation-only path/revision
        # and bounded UTF-8 invariants. These two inspected helpers do not fetch or interpret.
        representation_helpers = {
            ('upgradepilot.github.repository', '_validate_exact_file_locator'),
            ('upgradepilot.github.repository', '_validate_bounded_utf8_text'),
        }
        if (module in forbidden and not name.startswith('__') and (module, name) not in representation_helpers) or module.startswith(('openai.', 'httpx.')):
            raise RuntimeError('forbidden recovery re-entry: ' + module + '.' + name)

target = ExactInvestigationTarget(**json.loads(sys.argv[2]))
sys.setprofile(guard)
with patch.object(socket.socket, 'connect', side_effect=AssertionError('network forbidden')):
    boundary = read_native_boundary(Path(sys.argv[1]).read_bytes(), expected_target=target)
    ci = reconstruct_ci_projection(boundary, expected_target=target)
    if len(sys.argv) > 3:
        try:
            reconstruct_python_support_projection(boundary, expected_target=target)
        except NativeReconstructionError as error:
            assert error.reason == sys.argv[3], error
            result = {'ci': independent_native_values(ci), 'refusal': error.reason}
        else:
            raise AssertionError('substituted Python material was accepted')
    else:
        python = reconstruct_python_support_projection(boundary, expected_target=target)
        result = {'ci': independent_native_values(ci), 'python': independent_native_values(python)}
sys.setprofile(None)

# Negative controls prove provider, model-bound evaluator, native evaluator and synthesis
# guards can fail on actual entry points; none of these controls execute their body.
blocked = []
for call in (
    lambda: GitHubRepositoryClient.get_exact_head_text_file(None, None, None),
    lambda: evaluate_support_drop_runtime(None),
    lambda: evaluate_runtime_dependency_state(None, None, None, source_contexts=()),
    lambda: synthesize_maintainer_action(None),
):
    sys.setprofile(guard)
    try:
        call()
    except RuntimeError as error:
        assert str(error).startswith('forbidden recovery re-entry:'), error
        blocked.append(str(error))
    finally:
        sys.setprofile(None)
assert len(blocked) == 4, blocked
result['blocked_controls'] = len(blocked)
print(json.dumps(result, sort_keys=True))
"""


class WorkspaceNativeReconstructionTests(unittest.TestCase):
    def test_json_resource_refusals_precede_parser_allocation(self):
        cases = (
            ("MAX_NATIVE_JSON_BYTES", 8, b"[]       "),
            ("MAX_NATIVE_JSON_DEPTH", 2, b"[[[0]]]"),
            ("MAX_NATIVE_JSON_STRUCTURAL_TOKENS", 4, b"[0,1,2,3]"),
        )
        for limit, maximum, payload in cases:
            with (
                self.subTest(limit=limit),
                patch.object(native_representation, limit, maximum),
                patch.object(native_representation.json, "loads") as parser,
            ):
                with self.assertRaisesRegex(
                    NativeReconstructionError, "native_resource_limit"
                ):
                    native_representation.parse_json(payload)
                parser.assert_not_called()

    def test_json_exact_capacity_and_escaped_source_punctuation_are_supported(self):
        with patch.object(native_representation, "MAX_NATIVE_JSON_BYTES", 8):
            self.assertEqual(native_representation.parse_json(b"[]      "), [])
        with (
            patch.object(native_representation, "MAX_NATIVE_JSON_DEPTH", 2),
            patch.object(native_representation, "MAX_NATIVE_JSON_STRUCTURAL_TOKENS", 4),
        ):
            self.assertEqual(native_representation.parse_json(b"[[0]]"), [[0]])
            content = '[{}],: "quoted" \\ escaped'
            # Escaped quotes/backslashes and punctuation in retained source are not nodes.
            payload = native_representation.json_bytes({"source": content})
            self.assertEqual(
                native_representation.parse_json(payload), {"source": content}
            )

    def test_encoder_refuses_material_outside_decoder_capacity(self):
        for limit, maximum, value in (
            ("MAX_NATIVE_JSON_BYTES", 8, {"content": "oversized"}),
            ("MAX_NATIVE_JSON_DEPTH", 2, [[[0]]]),
            ("MAX_NATIVE_JSON_STRUCTURAL_TOKENS", 4, [0, 1, 2, 3]),
        ):
            with (
                self.subTest(limit=limit),
                patch.object(native_representation, limit, maximum),
            ):
                with self.assertRaisesRegex(
                    NativeReconstructionError, "native_resource_limit"
                ):
                    native_representation.json_bytes(value)

    def test_v1_layouts_cannot_silently_fill_new_native_fields_from_defaults(self):
        # A new field on a reused constructor requires a reviewed codec compatibility
        # decision. This independent schema check catches drift even in unexercised variants.
        for layout in INPUT_LAYOUTS + CI_LAYOUTS + IMPACT_LAYOUTS:
            with self.subTest(variant=layout.variant):
                self.assertEqual(
                    tuple(name for name, _ in layout.fields),
                    tuple(field.name for field in fields(layout.constructor)),
                )

    def test_normal_path_retains_hidden_inputs_and_complete_native_meanings(self):
        h, original, boundary, expected_ci, expected_python = captured_case()
        before = [
            client.mock_calls[:]
            for client in (
                h.pull_client,
                h.actions_client,
                h.repository_client,
                h.package_client,
                h.support_drop_evaluator,
            )
        ]
        restored = read_native_boundary(
            encode_native_boundary(boundary), expected_target=boundary.target
        )
        self.assertEqual(restored, boundary)
        ci = reconstruct_ci_projection(restored, expected_target=boundary.target)
        python = reconstruct_python_support_projection(
            restored, expected_target=boundary.target
        )
        self.assertEqual(ci.inputs, expected_ci.inputs)
        self.assertEqual(ci.ci_coverage_result, original.ci_coverage_result)
        self.assertEqual(
            ci.runtime_dependency_state_result, original.runtime_dependency_state_result
        )
        self.assertEqual(python, expected_python)
        self.assertEqual(
            tuple((item.run, item.jobs) for item in ci.workflow_inputs),
            original.workflow_evidence,
        )
        self.assertEqual(
            ci.workflow_inputs[0].definition,
            h.repository_client.get_exact_head_workflow_file.return_value,
        )
        self.assertIn(
            "PIP_CONFIG_FILE=/dev/null", ci.workflow_inputs[0].definition.content
        )
        self.assertFalse(hasattr(original, "source_contexts"))
        self.assertFalse(hasattr(original, "coverage_inputs"))
        witness = ci.runtime_dependency_state_result.assessments[0].result
        self.assertEqual(
            witness.semantics.manager_environment.environment.value,
            "/opt/target/bin/python",
        )
        self.assertEqual(witness.observation_boundary, "successful_command_completion")
        self.assertIn(
            "Does not establish behavioral compatibility.", witness.limitations
        )
        self.assertEqual(
            before,
            [
                client.mock_calls[:]
                for client in (
                    h.pull_client,
                    h.actions_client,
                    h.repository_client,
                    h.package_client,
                    h.support_drop_evaluator,
                )
            ],
        )
        h.support_drop_evaluator.assert_called_once()
        for record in boundary.records:
            if record.outcome == "recorded":
                self.assertIsNone(record.producer_version)
                self.assertIn("producer_version_unavailable", record.retention_gaps)

    def test_fresh_process_complete_native_parity_with_independent_reentry_controls(
        self,
    ):
        for command, python, problem in (
            ("positive", "outside", False),
            ("dry_run", "overlap", False),
            ("ambient", "unresolved", False),
            ("positive", "unavailable", False),
            ("positive", "no_claim", False),
            ("positive", "outside", True),
        ):
            with self.subTest(
                command=command, python=python, dependency_problem=problem
            ):
                self._assert_cold_case(command, python, problem)

    def _assert_cold_case(self, command, python, problem):
        _, _, boundary, expected_ci, expected_python = captured_case(
            command_variant=command, python_variant=python, dependency_problem=problem
        )
        # The expected input bundle comes from independently supplied client evidence, not
        # the encoder's field list. Complete native comparison uses the test-only renderer.
        expected = {
            "ci": independent_native_values(expected_ci),
            "python": independent_native_values(expected_python),
            "blocked_controls": 4,
        }
        self.assertEqual(self._cold_reconstruction(boundary), expected)

    def _cold_reconstruction(self, boundary, expected_refusal=None):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "native.json"
            path.write_bytes(encode_native_boundary(boundary))
            target = {
                field.name: getattr(boundary.target, field.name)
                for field in fields(boundary.target)
            }
            env = dict(
                os.environ,
                PYTHONPATH=os.pathsep.join(
                    [
                        str(Path(__file__).resolve().parent),
                        os.environ.get("PYTHONPATH", ""),
                    ]
                ),
            )
            arguments = [
                sys.executable,
                "-c",
                _RECOVERY_CHILD,
                str(path),
                json.dumps(target),
            ]
            if expected_refusal is not None:
                arguments.append(expected_refusal)
            result = subprocess.run(
                arguments,
                env=env,
                capture_output=True,
                text=True,
                timeout=20,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_substituted_selected_source_refuses_with_valid_digests_in_cold_process(
        self,
    ):
        for variant in ("outside", "unavailable"):
            with self.subTest(source=variant):
                _, _, boundary, expected_ci, expected_python = captured_case(
                    python_variant=variant
                )
                # Keep every downstream source/result relationship coherent. Only the
                # requested-selection -> acquired-path relationship is contradicted.
                substituted_path = "substituted/pyproject.toml"
                source = replace(
                    expected_python.target_python_source, path=substituted_path
                )
                result = replace(
                    expected_python.target_python_result, path=substituted_path
                )
                relevance = replace(
                    expected_python.target_python_relevance_result,
                    target_evidence=result,
                )
                post = replace(
                    expected_python.impact_result, target_relevance=relevance
                )
                changed = {
                    "target_python": {"source": source, "result": result},
                    "target_relevance": relevance,
                    "python_support_post_assessment": post,
                }
                for family, value in changed.items():
                    payload = encode_native_value(family, value)
                    boundary = altered_record(
                        boundary,
                        family,
                        payload=payload,
                        payload_digest=sha256(payload).hexdigest(),
                    )
                actual = self._cold_reconstruction(boundary, "invalid_native_material")
                self.assertEqual(
                    actual,
                    {
                        "ci": independent_native_values(expected_ci),
                        "refusal": "invalid_native_material",
                        "blocked_controls": 4,
                    },
                )

    def _pending_selected_acquisition(self, *, python_variant="outside"):
        _, _, boundary, expected_ci, expected_python = captured_case(
            python_variant=python_variant
        )
        self.assertIsNotNone(expected_python.investigation_selection)
        self.assertIsNotNone(expected_python.target_python_source)
        self.assertIsNotNone(expected_python.target_python_result)
        # Retain the actual pre-assessment/selection, with later processing explicitly
        # unexecuted. This tests future intermediate-state decoding, not publication.
        for family, value in (
            ("target_python", {"source": None, "result": None}),
            ("target_relevance", None),
            ("python_support_post_assessment", None),
        ):
            payload = encode_native_value(family, value)
            boundary = altered_record(
                boundary,
                family,
                payload=payload,
                payload_digest=sha256(payload).hexdigest(),
                outcome="not_evaluated",
                producer_method=None,
                retention_gaps=(),
            )
        pending_python = replace(
            expected_python,
            target_python_source=None,
            target_python_result=None,
            target_python_relevance_result=None,
            impact_result=None,
        )
        return boundary, expected_ci, pending_python

    def test_recorded_selected_acquisition_cannot_disappear_with_valid_digest(self):
        for variant in ("outside", "unavailable"):
            with self.subTest(original_source=variant):
                boundary, expected_ci, _ = self._pending_selected_acquisition(
                    python_variant=variant
                )
                # Contents/digests/reference closure remain valid. Claiming this empty
                # acquisition was recorded is the sole contradicted outcome relationship.
                recorded_empty = altered_record(
                    boundary,
                    "target_python",
                    outcome="recorded",
                    producer_method="target.python.interpret_target_python_declaration",
                    retention_gaps=("producer_version_unavailable",),
                )
                self.assertEqual(
                    self._cold_reconstruction(
                        recorded_empty, "missing_native_material"
                    ),
                    {
                        "ci": independent_native_values(expected_ci),
                        "refusal": "missing_native_material",
                        "blocked_controls": 4,
                    },
                )

    def test_selected_not_evaluated_acquisition_remains_explicit_in_cold_projection(
        self,
    ):
        boundary, expected_ci, pending_python = self._pending_selected_acquisition()
        self.assertEqual(
            self._cold_reconstruction(boundary),
            {
                "ci": independent_native_values(expected_ci),
                "python": independent_native_values(pending_python),
                "blocked_controls": 4,
            },
        )
        restored = read_native_boundary(
            encode_native_boundary(boundary), expected_target=boundary.target
        )
        record = next(
            item for item in restored.records if item.family == "target_python"
        )
        self.assertEqual(record.outcome, "not_evaluated")
        self.assertIsNone(record.producer_method)

    def test_problem_unresolved_not_applicable_and_not_evaluated_variants(self):
        for command, python, dependency_problem in (
            ("dry_run", "overlap", False),
            ("ambient", "unresolved", False),
            ("positive", "unavailable", False),
            ("positive", "no_claim", False),
            ("positive", "outside", True),
        ):
            with self.subTest(
                command=command, python=python, dependency_problem=dependency_problem
            ):
                _, original, boundary, _, expected_python = captured_case(
                    command_variant=command,
                    python_variant=python,
                    dependency_problem=dependency_problem,
                )
                restored = read_native_boundary(
                    encode_native_boundary(boundary), expected_target=boundary.target
                )
                ci = reconstruct_ci_projection(
                    restored, expected_target=boundary.target
                )
                self.assertEqual(ci.ci_coverage_result, original.ci_coverage_result)
                self.assertEqual(
                    ci.runtime_dependency_state_result,
                    original.runtime_dependency_state_result,
                )
                self.assertEqual(
                    reconstruct_python_support_projection(
                        restored, expected_target=boundary.target
                    ),
                    expected_python,
                )

    def test_missing_hidden_input_refuses_even_when_retained_outputs_round_trip(self):
        _, _, boundary, _, _ = captured_case()
        missing = replace(
            boundary,
            records=tuple(
                record for record in boundary.records if record.family != "ci_inputs"
            ),
        )
        with self.assertRaisesRegex(
            NativeReconstructionError, "missing_native_material"
        ):
            reconstruct_ci_projection(missing, expected_target=boundary.target)

    def test_valid_digest_unsupported_codec_refuses_only_affected_projection(self):
        _, _, boundary, _, expected_python = captured_case()
        unsupported = altered_record(
            boundary, "runtime_dependency_state", codec_version=999
        )
        restored = read_native_boundary(
            encode_native_boundary(unsupported), expected_target=boundary.target
        )
        self.assertEqual(
            reconstruct_python_support_projection(
                restored, expected_target=boundary.target
            ),
            expected_python,
        )
        with self.assertRaisesRegex(
            NativeReconstructionError, "unsupported_native_codec"
        ):
            reconstruct_ci_projection(restored, expected_target=boundary.target)

    def test_declared_semantic_version_does_not_inherit_representation_support(self):
        _, _, boundary, _, expected_python = captured_case()
        unsupported = altered_record(
            boundary, "runtime_dependency_state", producer_version="future-method-99"
        )
        with self.assertRaisesRegex(
            NativeReconstructionError, "unsupported_native_semantic_version"
        ):
            reconstruct_ci_projection(unsupported, expected_target=boundary.target)
        self.assertEqual(
            reconstruct_python_support_projection(
                unsupported, expected_target=boundary.target
            ),
            expected_python,
        )

    def test_corrupt_wrong_target_and_inconsistent_owner_refuse(self):
        _, _, boundary, _, _ = captured_case()
        cases = (
            (
                altered_record(boundary, "ci_coverage", payload=b"{}"),
                "invalid_native_material",
            ),
            (
                altered_record(
                    boundary,
                    "ci_coverage",
                    target=replace(boundary.target, head_sha="f" * 40),
                ),
                "wrong_target",
            ),
            (
                altered_record(boundary, "ci_coverage", owner="impact.python_support"),
                "invalid_native_material",
            ),
        )
        for invalid, reason in cases:
            with (
                self.subTest(reason=reason),
                self.assertRaisesRegex(NativeReconstructionError, reason),
            ):
                reconstruct_ci_projection(invalid, expected_target=boundary.target)
        with self.assertRaisesRegex(NativeReconstructionError, "wrong_target"):
            read_native_boundary(
                encode_native_boundary(boundary),
                expected_target=replace(boundary.target, head_sha="f" * 40),
            )

    def test_missing_optional_field_and_injected_variant_do_not_use_defaults_or_imports(
        self,
    ):
        _, _, boundary, _, _ = captured_case()
        original = next(
            record
            for record in boundary.records
            if record.family == "runtime_dependency_state"
        )
        value = json.loads(original.payload)
        del value["fields"]["assessments"]
        for value in (value, {"variant": "__import__:os.system", "fields": {}}):
            payload = json.dumps(value).encode()
            invalid = altered_record(
                boundary,
                original.family,
                payload=payload,
                payload_digest=sha256(payload).hexdigest(),
            )
            with self.assertRaisesRegex(
                NativeReconstructionError, "invalid_native_material"
            ):
                reconstruct_ci_projection(invalid, expected_target=boundary.target)

    def test_valid_digests_do_not_admit_rebound_identity_or_constructor_repairs(self):
        _, _, boundary, _, _ = captured_case()
        identity = next(
            record
            for record in boundary.records
            if record.family == "investigation_inputs"
        )
        value = json.loads(identity.payload)
        value["pull_request"]["fields"]["head_sha"] = "f" * 40
        payload = json.dumps(value).encode()
        rebound = altered_record(
            boundary,
            identity.family,
            payload=payload,
            payload_digest=sha256(payload).hexdigest(),
        )
        with self.assertRaisesRegex(NativeReconstructionError, "wrong_target"):
            reconstruct_ci_projection(rebound, expected_target=boundary.target)

        authority = next(
            record
            for record in boundary.records
            if record.family == "upstream_authority"
        )
        value = json.loads(authority.payload)
        changelog = value["fields"]["tagged_changelog"]["fields"]
        changelog["repository"] = " " + changelog["repository"] + " "
        payload = json.dumps(value).encode()
        repair = altered_record(
            boundary,
            authority.family,
            payload=payload,
            payload_digest=sha256(payload).hexdigest(),
        )
        with self.assertRaisesRegex(
            NativeReconstructionError, "invalid_native_material"
        ):
            reconstruct_python_support_projection(
                repair, expected_target=boundary.target
            )

    def test_failed_staging_is_not_completed_recovery(self):
        capture = NativeInvestigationCapture()
        with self.assertRaisesRegex(ValueError, "completed normal investigation"):
            capture.snapshot()

        h, _, _, expected_ci, _ = captured_case()
        h.actions_client.get_exact_head_workflow_runs.side_effect = RuntimeError(
            "failed acquisition"
        )
        analysis = DependencyChangeAnalysis(
            expected_ci.inputs.dependency_result, expected_ci.inputs.source_contexts
        )
        with patch(
            "upgradepilot.investigation.analyze_dependency_change",
            return_value=analysis,
        ):
            with self.assertRaisesRegex(RuntimeError, "failed acquisition"):
                investigate_public_pull_request(
                    "example/project", 7, native_capture=capture, **h.kwargs()
                )
        with self.assertRaisesRegex(ValueError, "completed normal investigation"):
            capture.snapshot()

    def test_ambiguous_json_and_unsupported_boundary_format_refuse_explicitly(self):
        _, _, boundary, _, _ = captured_case()
        with self.assertRaisesRegex(
            NativeReconstructionError, "invalid_native_material"
        ):
            read_native_boundary(
                b'{"format_version":1,"format_version":1}',
                expected_target=boundary.target,
            )
        value = json.loads(encode_native_boundary(boundary))
        value["format_version"] = 999
        with self.assertRaisesRegex(
            NativeReconstructionError, "unsupported_capture_format"
        ):
            read_native_boundary(
                json.dumps(value).encode(), expected_target=boundary.target
            )


if __name__ == "__main__":
    unittest.main()
