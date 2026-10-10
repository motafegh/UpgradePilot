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
from upgradepilot.dependency.environment import (
    ConstraintsFileDependencyContext,
    PyprojectDependencyGroupContext,
    PyprojectOptionalExtraDependencyContext,
    RequirementsFileDependencyContext,
    UvLockDependencyContext,
)
from upgradepilot.github.actions import WorkflowStep
from upgradepilot.github.repository import RepositoryTextFile, UnavailableRepositoryFile
from upgradepilot.github.release import GitHubReleaseEvidence
from upgradepilot.impact.python_support_codec import LAYOUTS as IMPACT_LAYOUTS
from upgradepilot.investigation import investigate_public_pull_request
from upgradepilot.target.python import TargetPythonDeclaration
from upgradepilot.upstream.claim import (
    GroundedPythonSupportDropClaim,
    GroundedUpstreamClaimSource,
)
from upgradepilot.upstream.interval import (
    IntervalGitHubReleaseSource,
    PackageMetadataCorroboration,
    UpstreamIntervalAuthorityProblem,
    assemble_upstream_interval_authority,
    release_interval_from_dependency_change,
)
from upgradepilot.workspace.native_boundary import (
    encode_native_boundary,
    read_native_boundary,
)
from upgradepilot.workspace.native_capture import NativeInvestigationCapture
from upgradepilot.workspace.native_codecs import (
    FAMILY_CONTRACTS,
    decode_native_value,
    encode_native_value,
)
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
    *,
    command_variant="positive",
    python_variant="outside",
    dependency_problem=False,
    direct_invocation=False,
    second_source=False,
):
    h = _Harness()
    dependency = _dependency()
    if second_source:
        dependency = replace(
            dependency,
            source_evidence=dependency.source_evidence
            + (replace(dependency.source_evidence[0], path="other-requirements.txt"),),
        )
        h.identity = replace(h.identity, changed_files=2)
        h.pull_client.get_pull_request.return_value = h.identity
        h.pull_client.get_changed_files.return_value += (
            replace(
                h.pull_client.get_changed_files.return_value[0],
                filename="other-requirements.txt",
            ),
        )
    context = RequirementsFileDependencyContext(
        repository=h.identity.repository,
        revision=h.identity.head_sha,
        normalized_package=dependency.normalized_package,
        source_evidence=dependency.source_evidence[0],
    )
    contexts = (context,) + (
        (replace(context, source_evidence=dependency.source_evidence[1]),)
        if second_source
        else ()
    )
    workflow = _WORKFLOW
    if command_variant == "dry_run":
        workflow = workflow.replace("PIP_DRY_RUN=0", "PIP_DRY_RUN=1")
    elif command_variant == "ambient":
        workflow = workflow.replace("PIP_CONFIG_FILE=/dev/null ", "")
    if direct_invocation:
        workflow += "      - name: Invoke\n        run: demo\n"
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
            )
            + (
                (WorkflowStep(3, "Invoke", "completed", "success"),)
                if direct_invocation
                else ()
            ),
        )
        for job in jobs
    )
    if python_variant != "no_claim":

        def controlled_claim(authority):
            # Controlled semantic answer, with actual retained authority provenance.
            source = authority.tagged_changelog
            quote = "Removed Python 3.9 support."
            start = source.content.index(quote)
            return GroundedPythonSupportDropClaim(
                python_line="3.9",
                introduced_in_version=dependency.proposed_version,
                interval=release_interval_from_dependency_change(dependency),
                source_evidence=(
                    GroundedUpstreamClaimSource(
                        "tagged_changelog",
                        dependency.proposed_version,
                        source,
                        quote,
                        start,
                        start + len(quote),
                    ),
                ),
            )

        h.support_drop_evaluator.side_effect = controlled_claim
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
    analysis = DependencyChangeAnalysis(dependency, contexts)
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
        () if dependency_problem else contexts,
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


def retained_values(boundary):
    return {
        record.family: decode_native_value(record.family, 1, record.payload)
        for record in boundary.records
    }


def replaced_values(boundary, **values):
    """Substitute typed material while preserving IDs/references and valid new digests."""
    for family, value in values.items():
        payload = encode_native_value(family, value)
        boundary = altered_record(
            boundary,
            family,
            payload=payload,
            payload_digest=sha256(payload).hexdigest(),
        )
    return boundary


def unevaluated_families(boundary, families):
    for family in families:
        empty = () if family == "ci_inputs" else None
        if family == "target_python":
            empty = {"source": None, "result": None}
        boundary = replaced_values(boundary, **{family: empty})
        boundary = altered_record(
            boundary,
            family,
            outcome="not_evaluated",
            producer_method=None,
            producer_version=None,
            retention_gaps=(),
        )
    return boundary


def captured_project_case(kind, *, unavailable=False, second_context=False):
    """Normal acquisition/CI/capture with controlled dependency-owned context variants.

    Group is an admitted native context, not a claim that current dependency analysis
    discovers group changes. Project/lock reads and subsequent CI processing are real.
    """
    h = _Harness()
    path = "app/uv.lock" if kind == "uv" else "app/pyproject.toml"
    evidence = replace(
        _dependency().source_evidence[0],
        path=path,
        file_format="uv_lock" if kind == "uv" else "pyproject_optional_extra",
        extraction_method="exact_base_head_files",
    )
    dependency = replace(_dependency(), source_evidence=(evidence,))
    common = (h.identity.repository, h.identity.head_sha, "demo", evidence)
    context = (
        UvLockDependencyContext(*common)
        if kind == "uv"
        else PyprojectOptionalExtraDependencyContext(*common, extra="test")
        if kind == "extra"
        else PyprojectDependencyGroupContext(*common, group="test")
    )
    contexts = (context,)
    h.pull_client.get_changed_files.return_value = (
        replace(h.pull_client.get_changed_files.return_value[0], filename=path),
    )
    if second_context:
        other_evidence = replace(
            evidence,
            path="other/pyproject.toml",
            file_format="pyproject_optional_extra",
        )
        dependency = replace(dependency, source_evidence=(evidence, other_evidence))
        contexts += (
            PyprojectOptionalExtraDependencyContext(
                h.identity.repository,
                h.identity.head_sha,
                "demo",
                other_evidence,
                "test",
            ),
        )
        h.identity = replace(h.identity, changed_files=2)
        h.pull_client.get_pull_request.return_value = h.identity
        h.pull_client.get_changed_files.return_value += (
            replace(
                h.pull_client.get_changed_files.return_value[0],
                filename=other_evidence.path,
            ),
        )
    h.set_workflow(_WORKFLOW, job_names=("Test",))

    def exact_file(identity, requested):
        if unavailable:
            return UnavailableRepositoryFile(
                identity.repository,
                requested,
                identity.head_sha,
                "file_unavailable",
                "Controlled unavailable project source.",
            )
        return RepositoryTextFile(
            identity.repository,
            requested,
            identity.head_sha,
            "version = 1\n"
            if requested.endswith("uv.lock")
            else '[project]\nname = "demo"\n',
        )

    h.repository_client.get_exact_head_text_file.side_effect = exact_file
    capture = NativeInvestigationCapture()
    with patch(
        "upgradepilot.investigation.analyze_dependency_change",
        return_value=DependencyChangeAnalysis(dependency, contexts),
    ):
        original = investigate_public_pull_request(
            "example/project", 7, native_capture=capture, **h.kwargs()
        )
    return capture.snapshot(), original


def rebound_claim(boundary, claim):
    """Keep every downstream copy consistent so only claim→authority binding is tested."""
    values = retained_values(boundary)
    pre = values["python_support_pre_assessment"]
    relevance = values["target_relevance"]
    post = values["python_support_post_assessment"]
    candidate = replace(pre.candidate, upstream_claim=claim)
    relevance = replace(relevance, upstream_result=claim)
    return replaced_values(
        boundary,
        upstream_support_drop=claim,
        python_support_pre_assessment=replace(pre, candidate=candidate),
        target_relevance=relevance,
        python_support_post_assessment=replace(
            post, candidate=candidate, target_relevance=relevance
        ),
    )


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
    'upgradepilot.ci.workflow_commands', 'upgradepilot.ci.workflow_runtime_correlation',
    'upgradepilot.ci.runtime_execution', 'upgradepilot.ci.runtime_strengthening',
    'upgradepilot.github.workflow_definition', 'upgradepilot.github.workflow_command_analysis',
    'upgradepilot.dependency.environment_membership', 'upgradepilot.dependency.environment_selection',
    'upgradepilot.dependency.uv_reachability', 'upgradepilot.dependency.package_manager_semantics',
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
    refusals = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
    result = {}
    for name, reconstruct in (('ci', reconstruct_ci_projection), ('python', reconstruct_python_support_projection)):
        try:
            projection = reconstruct(boundary, expected_target=target)
        except NativeReconstructionError as error:
            assert name in refusals and error.reason == refusals[name], error
            result[name + '_refusal'] = error.reason
        else:
            assert name not in refusals, 'substituted ' + name + ' material was accepted'
            result[name] = independent_native_values(projection)
    # Preserve the original Python-only control's result spelling.
    if set(refusals) == {'python'}:
        result['refusal'] = result.pop('python_refusal')
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

    def _cold_reconstruction(
        self, boundary, expected_refusal=None, *, refused="python"
    ):
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
                names = ("ci", "python") if refused == "both" else (refused,)
                arguments.append(json.dumps(dict.fromkeys(names, expected_refusal)))
            result = subprocess.run(
                arguments,
                env=env,
                capture_output=True,
                text=True,
                timeout=20,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def _assert_binding_refusal(
        self, boundary, *, refused="python", reason="invalid_native_material"
    ):
        # Envelope validity is a precondition: this control targets decoded relationships.
        restored = read_native_boundary(
            encode_native_boundary(boundary), expected_target=boundary.target
        )
        self.assertEqual(restored, boundary)
        result = self._cold_reconstruction(boundary, reason, refused=refused)
        self.assertEqual(result["blocked_controls"], 4)
        if refused != "both":
            other = "ci" if refused == "python" else "python"
            reconstruct = (
                reconstruct_ci_projection
                if other == "ci"
                else reconstruct_python_support_projection
            )
            self.assertEqual(
                result[other],
                independent_native_values(
                    reconstruct(boundary, expected_target=boundary.target)
                ),
            )

    def test_every_declared_edge_refuses_substituted_record_reference(self):
        _, _, boundary, _, _ = captured_case()
        records = {record.family: record for record in boundary.records}
        edges = [
            (family, name)
            for family, contract in FAMILY_CONTRACTS.items()
            for name in contract.inputs
        ]
        self.assertEqual((len(FAMILY_CONTRACTS), len(edges)), (11, 18))
        for family, name in edges:
            with self.subTest(family=family, input=name):
                record = records[family]
                # Use the other independent branch to preserve acyclic reference closure.
                alternate = (
                    "upstream_authority"
                    if family.startswith("ci_") or family == "runtime_dependency_state"
                    else "ci_inputs"
                )
                substitute = records[alternate].record_id
                changed = altered_record(
                    boundary,
                    family,
                    input_record_ids=tuple(
                        substitute if ref == records[name].record_id else ref
                        for ref in record.input_record_ids
                    ),
                )
                reconstruct = (
                    reconstruct_ci_projection
                    if family.startswith("ci_") or family == "runtime_dependency_state"
                    else reconstruct_python_support_projection
                )
                refused = "ci" if reconstruct is reconstruct_ci_projection else "python"
                self._assert_binding_refusal(
                    changed, refused=refused, reason="missing_native_material"
                )

    def test_context_provenance_substitution_refuses_for_all_five_admitted_variants(
        self,
    ):
        _, _, boundary, _, _ = captured_case()
        values = retained_values(boundary)
        inputs = values["investigation_inputs"]
        evidence = replace(
            inputs["dependency_result"].source_evidence[0],
            extraction_method="exact_base_head_files",
        )
        args = (
            boundary.target.repository,
            boundary.target.head_sha,
            boundary.target.normalized_package,
            evidence,
        )
        contexts = (
            RequirementsFileDependencyContext(*args),
            ConstraintsFileDependencyContext(*args),
            UvLockDependencyContext(*args),
            PyprojectOptionalExtraDependencyContext(*args, extra="test"),
            PyprojectDependencyGroupContext(*args, group="test"),
        )
        # Avoid downstream duplicate-context checks hiding the common input omission.
        pending = unevaluated_families(boundary, tuple(FAMILY_CONTRACTS)[1:])
        for context in contexts:
            with self.subTest(context=type(context).__name__):
                changed = replaced_values(
                    pending,
                    investigation_inputs={**inputs, "source_contexts": (context,)},
                )
                self._assert_binding_refusal(changed, refused="both")

    def test_changed_file_and_dependency_source_locators_are_bound(self):
        _, _, boundary, _, _ = captured_case()
        inputs = retained_values(boundary)["investigation_inputs"]
        cases = (
            {**inputs, "changed_files": ()},
            {
                **inputs,
                "changed_files": (
                    replace(inputs["changed_files"][0], filename="other.txt"),
                ),
            },
        )
        for index, values in enumerate(cases):
            with self.subTest(index=index):
                self._assert_binding_refusal(
                    replaced_values(boundary, investigation_inputs=values),
                    refused="both",
                )

    def test_existing_decoded_scope_and_candidate_basis_checks_have_cold_controls(self):
        _, _, boundary, _, _ = captured_case()
        values = retained_values(boundary)
        workflow = values["ci_inputs"][0]
        job = workflow.jobs[0]
        cases = (
            replace(workflow, run=replace(workflow.run, head_sha="e" * 40)),
            replace(workflow, jobs=(replace(job, head_sha="e" * 40),)),
            replace(workflow, jobs=(replace(job, run_id=999),)),
            replace(
                workflow,
                definition=replace(workflow.definition, repository="other/project"),
            ),
            replace(
                workflow, definition=replace(workflow.definition, revision="e" * 40)
            ),
        )
        for index, replacement in enumerate(cases):
            with self.subTest(ci_scope=index):
                self._assert_binding_refusal(
                    replaced_values(boundary, ci_inputs=(replacement,)),
                    refused="ci",
                    reason="wrong_target",
                )
        for field, replacement in (
            ("repository", "other/project"),
            ("revision", "e" * 40),
            ("normalized_package", "other"),
        ):
            with self.subTest(context_scope=field):
                context = replace(
                    values["investigation_inputs"]["source_contexts"][0],
                    **{field: replacement},
                )
                self._assert_binding_refusal(
                    replaced_values(
                        boundary,
                        investigation_inputs={
                            **values["investigation_inputs"],
                            "source_contexts": (context,),
                        },
                    ),
                    refused="both",
                    reason="wrong_target",
                )
        pre = values["python_support_pre_assessment"]
        for field, replacement in (
            ("pull_request", replace(pre.candidate.pull_request, number=99)),
            ("dependency", replace(pre.candidate.dependency, old_version="0.1")),
            (
                "upstream_claim",
                replace(pre.candidate.upstream_claim, python_line="3.8"),
            ),
            ("target_repository", "other/project"),
            ("target_revision", "e" * 40),
        ):
            with self.subTest(candidate_basis=field):
                self._assert_binding_refusal(
                    replaced_values(
                        boundary,
                        python_support_pre_assessment=replace(
                            pre,
                            candidate=replace(pre.candidate, **{field: replacement}),
                        ),
                    )
                )
        for field, replacement in (
            (
                "upstream_result",
                replace(values["upstream_support_drop"], python_line="3.8"),
            ),
            (
                "target_evidence",
                replace(values["target_python"]["result"], requires_python=">=3.8"),
            ),
        ):
            with self.subTest(relevance_basis=field):
                self._assert_binding_refusal(
                    replaced_values(
                        boundary,
                        target_relevance=replace(
                            values["target_relevance"], **{field: replacement}
                        ),
                    )
                )
        post = values["python_support_post_assessment"]
        self._assert_binding_refusal(
            replaced_values(
                boundary,
                python_support_post_assessment=replace(post, target_relevance=None),
            )
        )

    def test_project_bundle_paths_presence_and_context_order_are_bound_in_cold_recovery(
        self,
    ):
        for kind in ("uv", "extra", "group"):
            for unavailable in (False, True):
                boundary, original = captured_project_case(
                    kind, unavailable=unavailable
                )
                with self.subTest(positive=(kind, unavailable)):
                    result = self._cold_reconstruction(boundary)
                    self.assertEqual(
                        result["ci"],
                        independent_native_values(
                            reconstruct_ci_projection(
                                boundary, expected_target=boundary.target
                            )
                        ),
                    )
                    self.assertEqual(
                        original.ci_coverage_result,
                        reconstruct_ci_projection(
                            boundary, expected_target=boundary.target
                        ).ci_coverage_result,
                    )
                values = retained_values(boundary)
                workflow = values["ci_inputs"][0]
                bundle = workflow.project_environment_sources[0]
                cases = {
                    "project_path": replace(
                        bundle,
                        project_file=replace(
                            bundle.project_file, path="other/pyproject.toml"
                        ),
                    ),
                }
                if kind == "uv":
                    cases["lock_path"] = replace(
                        bundle,
                        lock_file=replace(bundle.lock_file, path="other/uv.lock"),
                    )
                    cases["missing_lock"] = replace(bundle, lock_file=None)
                else:
                    cases["extra_lock"] = replace(bundle, lock_file=bundle.project_file)
                for name, replacement in cases.items():
                    with self.subTest(
                        kind=kind, unavailable=unavailable, mutation=name
                    ):
                        changed = replaced_values(
                            boundary,
                            ci_inputs=(
                                replace(
                                    workflow, project_environment_sources=(replacement,)
                                ),
                            ),
                        )
                        self._assert_binding_refusal(changed, refused="ci")
                for field, value in (
                    ("repository", "other/project"),
                    ("revision", "e" * 40),
                ):
                    with self.subTest(
                        kind=kind, unavailable=unavailable, source_scope=field
                    ):
                        replacement = replace(
                            bundle,
                            project_file=replace(bundle.project_file, **{field: value}),
                        )
                        changed = replaced_values(
                            boundary,
                            ci_inputs=(
                                replace(
                                    workflow, project_environment_sources=(replacement,)
                                ),
                            ),
                        )
                        self._assert_binding_refusal(
                            changed, refused="ci", reason="wrong_target"
                        )
                with self.subTest(
                    kind=kind, unavailable=unavailable, mutation="missing_bundle"
                ):
                    self._assert_binding_refusal(
                        replaced_values(
                            boundary,
                            ci_inputs=(
                                replace(workflow, project_environment_sources=()),
                            ),
                        ),
                        refused="ci",
                    )
        boundary, _ = captured_project_case("uv", second_context=True)
        self._cold_reconstruction(boundary)
        workflow = retained_values(boundary)["ci_inputs"][0]
        for bundles in (
            workflow.project_environment_sources[::-1],
            workflow.project_environment_sources * 2,
        ):
            with self.subTest(bundle_count=len(bundles)):
                self._assert_binding_refusal(
                    replaced_values(
                        boundary,
                        ci_inputs=(
                            replace(workflow, project_environment_sources=bundles),
                        ),
                    ),
                    refused="ci",
                )

    def test_coverage_correlation_members_and_workflow_name_are_bound(self):
        _, _, boundary, _, _ = captured_case()
        coverage = retained_values(boundary)["ci_coverage"]
        workflow = coverage.workflows[0]
        correlation = workflow.runtime_correlation
        job = correlation.jobs[0]
        step = job.steps[0]
        cases = {
            "workflow_name": replace(workflow, workflow_name="Other"),
            "static_job_name": replace(
                workflow,
                runtime_correlation=replace(
                    correlation,
                    jobs=(
                        replace(
                            job,
                            static_job=replace(
                                job.static_job,
                                name=replace(job.static_job.name, text="Other"),
                            ),
                        ),
                    ),
                ),
            ),
            "swapped_members": replace(
                workflow,
                runtime_correlation=replace(
                    correlation,
                    jobs=(
                        replace(
                            job,
                            steps=(replace(step, static_step=job.steps[1].static_step),)
                            + job.steps[1:],
                        ),
                    ),
                ),
            ),
            "duplicate_job": replace(
                workflow,
                runtime_correlation=replace(correlation, jobs=correlation.jobs * 2),
            ),
            "missing_step": replace(
                workflow,
                runtime_correlation=replace(
                    correlation, jobs=(replace(job, steps=job.steps[1:]),)
                ),
            ),
            "runtime_job": replace(
                workflow,
                runtime_correlation=replace(
                    correlation,
                    jobs=(
                        replace(job, runtime_job=replace(job.runtime_job, job_id=999)),
                    ),
                ),
            ),
            "runtime_step": replace(
                workflow,
                runtime_correlation=replace(
                    correlation,
                    jobs=(
                        replace(
                            job,
                            steps=(
                                replace(
                                    step,
                                    runtime_step=replace(step.runtime_step, number=999),
                                ),
                            )
                            + job.steps[1:],
                        ),
                    ),
                ),
            ),
            "static_step": replace(
                workflow,
                runtime_correlation=replace(
                    correlation,
                    jobs=(
                        replace(
                            job,
                            steps=(
                                replace(
                                    step,
                                    static_step=replace(
                                        step.static_step, source_index=999
                                    ),
                                ),
                            )
                            + job.steps[1:],
                        ),
                    ),
                ),
            ),
        }
        for name, replacement in cases.items():
            with self.subTest(mutation=name):
                self._assert_binding_refusal(
                    replaced_values(
                        boundary,
                        ci_coverage=replace(coverage, workflows=(replacement,)),
                    ),
                    refused="ci",
                )

    def test_coverage_consumption_source_and_invocation_scope_are_bound(self):
        _, _, boundary, _, _ = captured_case(direct_invocation=True)
        values = retained_values(boundary)
        coverage = values["ci_coverage"]
        workflow = coverage.workflows[0]
        self.assertEqual(len(workflow.invocations), 1)
        for field, replacement in (
            ("workflow_path", "other.yml"),
            ("workflow_revision", "c" * 40),
            ("command", "other-command"),
        ):
            with self.subTest(invocation_field=field):
                changed = replace(
                    workflow,
                    invocations=(
                        replace(workflow.invocations[0], **{field: replacement}),
                    ),
                )
                self._assert_binding_refusal(
                    replaced_values(
                        boundary, ci_coverage=replace(coverage, workflows=(changed,))
                    ),
                    refused="ci",
                )
        consumption = replace(workflow.consumptions[0], source_path="other.txt")
        runtime = values["runtime_dependency_state"]
        assessment = runtime.assessments[0]
        witness = replace(assessment.result, consumption=consumption)
        changed = replaced_values(
            boundary,
            ci_coverage=replace(
                coverage, workflows=(replace(workflow, consumptions=(consumption,)),)
            ),
            runtime_dependency_state=replace(
                runtime,
                assessments=(
                    replace(assessment, consumption=consumption, result=witness),
                ),
            ),
        )
        self._assert_binding_refusal(changed, refused="ci")

        consumption = replace(workflow.consumptions[0], command="other-command")
        witness = replace(assessment.result, consumption=consumption)
        changed = replaced_values(
            boundary,
            ci_coverage=replace(
                coverage, workflows=(replace(workflow, consumptions=(consumption,)),)
            ),
            runtime_dependency_state=replace(
                runtime,
                assessments=(
                    replace(assessment, consumption=consumption, result=witness),
                ),
            ),
        )
        self._assert_binding_refusal(changed, refused="ci")

    def test_runtime_nested_semantic_and_execution_bases_are_bound(self):
        _, _, boundary, _, _ = captured_case()
        runtime = retained_values(boundary)["runtime_dependency_state"]
        assessment = runtime.assessments[0]
        witness = assessment.result
        cases = {}
        for dimension in (
            "manager_environment",
            "installation_destination",
            "package_mutation_mode",
            "direct_requirement_handling",
        ):
            fact = getattr(witness.semantics, dimension)
            cases[dimension + "_command"] = replace(
                witness,
                semantics=replace(
                    witness.semantics,
                    **{
                        dimension: replace(
                            fact,
                            command_location=replace(
                                fact.command_location, source_order=99
                            ),
                        )
                    },
                ),
            )
            other = (
                "manager_environment"
                if dimension != "manager_environment"
                else "installation_destination"
            )
            cases[dimension + "_dimension"] = replace(
                witness,
                semantics=replace(
                    witness.semantics,
                    **{
                        dimension: replace(
                            fact, provenance=replace(fact.provenance, dimension=other)
                        )
                    },
                ),
            )
            cases[dimension + "_winner"] = replace(
                witness,
                semantics=replace(
                    witness.semantics,
                    **{
                        dimension: replace(
                            fact,
                            provenance=replace(fact.provenance, inspected_sources=()),
                        )
                    },
                ),
            )
        step_execution = witness.execution.step_execution
        cases["execution_step"] = replace(
            witness,
            execution=replace(
                witness.execution,
                step_execution=replace(
                    step_execution,
                    correlation=replace(
                        step_execution.correlation,
                        runtime_step=replace(
                            step_execution.correlation.runtime_step, number=99
                        ),
                    ),
                ),
            ),
        )
        cases["missing_execution_step"] = replace(
            witness, execution=replace(witness.execution, step_execution=None)
        )
        for name, replacement in cases.items():
            with self.subTest(mutation=name):
                changed = replaced_values(
                    boundary,
                    runtime_dependency_state=replace(
                        runtime, assessments=(replace(assessment, result=replacement),)
                    ),
                )
                self._assert_binding_refusal(changed, refused="ci")
        for assessments in ((), runtime.assessments * 2):
            with self.subTest(assessment_count=len(assessments)):
                self._assert_binding_refusal(
                    replaced_values(
                        boundary,
                        runtime_dependency_state=replace(
                            runtime, assessments=assessments
                        ),
                    ),
                    refused="ci",
                )

    def test_runtime_problem_evidence_location_and_dimension_are_bound(self):
        _, _, boundary, _, _ = captured_case(command_variant="dry_run")
        runtime = retained_values(boundary)["runtime_dependency_state"]
        assessment = runtime.assessments[0]
        problem = assessment.result
        evidence = problem.blocking_semantic_evidence
        self.assertIsNotNone(evidence)
        cases = (
            replace(
                problem,
                blocking_semantic_evidence=replace(
                    evidence,
                    command_location=replace(
                        evidence.command_location, source_order=99
                    ),
                ),
            ),
            replace(problem, blocking_dimension="manager_environment"),
        )
        for index, replacement in enumerate(cases):
            with self.subTest(index=index):
                self._assert_binding_refusal(
                    replaced_values(
                        boundary,
                        runtime_dependency_state=replace(
                            runtime,
                            assessments=(replace(assessment, result=replacement),),
                        ),
                    ),
                    refused="ci",
                )

    def test_witness_cannot_substitute_another_retained_dependency_source(self):
        _, _, boundary, _, _ = captured_case(second_source=True)
        self._cold_reconstruction(boundary)
        values = retained_values(boundary)
        runtime = values["runtime_dependency_state"]
        assessment = runtime.assessments[0]
        context = values["investigation_inputs"]["source_contexts"][1]
        replacement = replace(assessment.result, source_context=context)
        self._assert_binding_refusal(
            replaced_values(
                boundary,
                runtime_dependency_state=replace(
                    runtime, assessments=(replace(assessment, result=replacement),)
                ),
            ),
            refused="ci",
        )

    def test_grounded_claim_sources_quotes_and_introduced_release_are_bound(self):
        _, _, boundary, _, _ = captured_case()
        claim = retained_values(boundary)["upstream_support_drop"]
        evidence = claim.source_evidence[0]
        cases = {
            "source_content": replace(
                evidence,
                source=replace(
                    evidence.source, content=evidence.source.content + "substitution"
                ),
            ),
            "source_path": replace(
                evidence, source=replace(evidence.source, path="OTHER.md")
            ),
            "source_commit": replace(
                evidence, source=replace(evidence.source, resolved_commit_sha="e" * 40)
            ),
            "source_kind": replace(evidence, source_kind="github_release_body"),
            "quote": replace(evidence, source_quote="A different quote"),
            "offset": replace(evidence, quote_start=0),
            "introduced": replace(evidence, introduced_in_version="9.9"),
        }
        for name, replacement in cases.items():
            with self.subTest(mutation=name):
                self._assert_binding_refusal(
                    rebound_claim(
                        boundary, replace(claim, source_evidence=(replacement,))
                    )
                )
        self._assert_binding_refusal(
            rebound_claim(boundary, replace(claim, source_evidence=()))
        )
        self._assert_binding_refusal(
            rebound_claim(
                boundary,
                replace(
                    claim,
                    introduced_in_version="9.9",
                    source_evidence=(replace(evidence, introduced_in_version="9.9"),),
                ),
            )
        )

    def test_successful_authority_nested_interval_repository_and_metadata_are_bound(
        self,
    ):
        _, _, boundary, _, _ = captured_case(python_variant="no_claim")
        authority = retained_values(boundary)["upstream_authority"]
        index = authority.crossed_releases
        changelog = authority.tagged_changelog
        cases = {
            "index_repository": replace(
                authority, crossed_releases=replace(index, repository="other/upstream")
            ),
            "index_interval": replace(
                authority,
                crossed_releases=replace(
                    index, interval=replace(index.interval, old_version="0.1")
                ),
            ),
            "changelog_repository": replace(
                authority,
                tagged_changelog=replace(changelog, repository="other/upstream"),
            ),
            "changelog_interval": replace(
                authority,
                tagged_changelog=replace(
                    changelog, interval=replace(changelog.interval, old_version="0.1")
                ),
            ),
        }
        for name, replacement in cases.items():
            with self.subTest(mutation=name):
                self._assert_binding_refusal(
                    replaced_values(boundary, upstream_authority=replacement)
                )
        # Keep every interval copy internally equal while substituting the source package
        # spelling: the remaining mismatch is authority→retained dependency identity.
        interval = replace(authority.interval, package="DEMO")
        altered_authority = replace(
            authority,
            interval=interval,
            crossed_releases=replace(index, interval=interval),
            tagged_changelog=replace(changelog, interval=interval),
        )
        values = retained_values(boundary)
        claim_problem = replace(values["upstream_support_drop"], interval=interval)
        self._assert_binding_refusal(
            replaced_values(
                boundary,
                upstream_authority=altered_authority,
                upstream_support_drop=claim_problem,
                target_relevance=replace(
                    values["target_relevance"], upstream_result=claim_problem
                ),
            )
        )

    def test_release_body_grounding_and_authority_source_bases_remain_bound(self):
        # Exercise the admitted release-body variant through actual authority composition,
        # without claiming that the current normal pipeline acquires release-body bundles.
        _, _, boundary, _, _ = captured_case()
        values = retained_values(boundary)
        original_authority = values["upstream_authority"]
        claim = values["upstream_support_drop"]
        quote = claim.source_evidence[0].source_quote
        release = IntervalGitHubReleaseSource(
            claim.introduced_in_version,
            GitHubReleaseEvidence(
                repository=original_authority.repository,
                requested_tag=claim.introduced_in_version,
                release_id=1,
                release_url="https://example.invalid/release",
                release_name="Release",
                body=quote,
                prerelease=False,
                published_at="2026-10-10T00:00:00Z",
                tag_ref=f"refs/tags/{claim.introduced_in_version}",
                tag_object_type="commit",
                tag_object_sha="c" * 40,
                retrieved_at=original_authority.crossed_releases.retrieved_at,
            ),
        )
        metadata = PackageMetadataCorroboration(
            "demo",
            "demo",
            claim.introduced_in_version,
            "https://example.invalid/package",
            ">=3.10",
            release.release.retrieved_at,
        )
        authority = assemble_upstream_interval_authority(
            claim.interval,
            original_authority.repository,
            crossed_releases=original_authority.crossed_releases,
            release_bodies=(release,),
            package_metadata=(metadata,),
        )
        grounded = replace(
            claim,
            source_evidence=(
                GroundedUpstreamClaimSource(
                    "github_release_body",
                    claim.introduced_in_version,
                    release,
                    quote,
                    0,
                    len(quote),
                ),
            ),
        )
        release_boundary = rebound_claim(
            replaced_values(boundary, upstream_authority=authority), grounded
        )
        self._cold_reconstruction(release_boundary)
        evidence = grounded.source_evidence[0]
        for name, changed in {
            "release_source": replace(
                evidence,
                source=replace(
                    release, release=replace(release.release, release_id=99)
                ),
            ),
            "release_version": replace(
                evidence, source=replace(release, release_version="9.9")
            ),
            "release_kind": replace(evidence, source_kind="tagged_changelog"),
            "release_quote": replace(evidence, source_quote="substitution"),
        }.items():
            with self.subTest(claim_mutation=name):
                self._assert_binding_refusal(
                    rebound_claim(
                        release_boundary, replace(grounded, source_evidence=(changed,))
                    )
                )
        for name, changed in {
            "release_repository": replace(
                authority,
                release_bodies=(
                    replace(
                        release,
                        release=replace(release.release, repository="other/upstream"),
                    ),
                ),
            ),
            "release_tag": replace(
                authority,
                release_bodies=(
                    replace(
                        release, release=replace(release.release, requested_tag="9.9")
                    ),
                ),
            ),
            "release_ref": replace(
                authority,
                release_bodies=(
                    replace(
                        release,
                        release=replace(release.release, tag_ref="refs/tags/9.9"),
                    ),
                ),
            ),
            "release_member": replace(
                authority, release_bodies=(replace(release, release_version="9.9"),)
            ),
            "duplicate_release": replace(authority, release_bodies=(release, release)),
            "missing_series": replace(authority, release_bodies=()),
            "missing_index": replace(authority, crossed_releases=None),
            "missing_tagged_basis": replace(original_authority, tagged_changelog=None),
            "metadata_package": replace(
                authority,
                package_metadata=(replace(metadata, normalized_package="other"),),
            ),
            "metadata_version": replace(
                authority, package_metadata=(replace(metadata, release_version="9.9"),)
            ),
        }.items():
            with self.subTest(authority_mutation=name):
                self._assert_binding_refusal(
                    replaced_values(release_boundary, upstream_authority=changed)
                )
        problem = UpstreamIntervalAuthorityProblem(
            "identity_mismatch",
            authority.interval,
            authority.repository,
            "Historical failed authority.",
        )
        self._assert_binding_refusal(
            replaced_values(release_boundary, upstream_authority=problem)
        )
        only_problem = unevaluated_families(
            replaced_values(boundary, upstream_authority=problem),
            tuple(FAMILY_CONTRACTS)[5:],
        )
        self._cold_reconstruction(only_problem)

    def test_unrelated_unsupported_versions_preserve_every_unaffected_projection(self):
        _, _, boundary, _, _ = captured_case()
        for family in FAMILY_CONTRACTS:
            for field, value, reason in (
                ("codec_version", 999, "unsupported_native_codec"),
                (
                    "producer_version",
                    "unadmitted",
                    "unsupported_native_semantic_version",
                ),
            ):
                with self.subTest(family=family, version=field):
                    refused = (
                        "both"
                        if family == "investigation_inputs"
                        else "ci"
                        if family.startswith("ci_")
                        or family == "runtime_dependency_state"
                        else "python"
                    )
                    self._assert_binding_refusal(
                        altered_record(boundary, family, **{field: value}),
                        refused=refused,
                        reason=reason,
                    )

    def test_missing_recorded_method_requires_explicit_retention_gap_for_every_root(
        self,
    ):
        _, _, boundary, _, _ = captured_case()
        for record in boundary.records:
            with self.subTest(family=record.family):
                missing = altered_record(
                    boundary,
                    record.family,
                    producer_method=None,
                    retention_gaps=tuple(
                        gap
                        for gap in record.retention_gaps
                        if gap != "producer_method_unavailable"
                    ),
                )
                refused = (
                    "both"
                    if record.family == "investigation_inputs"
                    else "ci"
                    if record.family.startswith("ci_")
                    or record.family == "runtime_dependency_state"
                    else "python"
                )
                self._assert_binding_refusal(missing, refused=refused)
                declared = altered_record(
                    missing,
                    record.family,
                    retention_gaps=record.retention_gaps
                    + ("producer_method_unavailable",),
                )
                self._cold_reconstruction(declared)

    def test_compatibility_input_consumptions_are_exclusive_and_source_scoped(self):
        _, _, boundary, _, _ = captured_case()
        values = retained_values(boundary)
        workflow = values["ci_inputs"][0]
        consumption = values["ci_coverage"].workflows[0].consumptions[0]
        # The codec retains this existing seam; it does not create a new acquisition path.
        supplied = replace(workflow, project_environment_consumptions=(consumption,))
        self._cold_reconstruction(replaced_values(boundary, ci_inputs=(supplied,)))
        for field, replacement in (
            ("workflow_path", "other.yml"),
            ("workflow_revision", "e" * 40),
            ("normalized_package", "other"),
            ("source_path", "other.txt"),
        ):
            with self.subTest(field=field):
                self._assert_binding_refusal(
                    replaced_values(
                        boundary,
                        ci_inputs=(
                            replace(
                                supplied,
                                project_environment_consumptions=(
                                    replace(consumption, **{field: replacement}),
                                ),
                            ),
                        ),
                    ),
                    refused="ci",
                )
        project, _ = captured_project_case("uv")
        workflow = retained_values(project)["ci_inputs"][0]
        self._assert_binding_refusal(
            replaced_values(
                project,
                ci_inputs=(
                    replace(workflow, project_environment_consumptions=(consumption,)),
                ),
            ),
            refused="ci",
        )

    def test_selection_is_bound_to_pre_assessment_without_rerunning_selector(self):
        _, _, boundary, _, _ = captured_case()
        pending, _, expected = self._pending_selected_acquisition()
        values = retained_values(pending)
        selection = values["python_support_selection"]
        pre = values["python_support_pre_assessment"]
        path = pre.applicability.paths[0]
        proposition = next(
            p for p in path.propositions if p.key == selection.proposition_key
        )
        for name, replacement in (
            (
                "proposition_key",
                replace(
                    selection, proposition_key="upstream_python_support_drop_crossed"
                ),
            ),
            ("path", replace(selection, path="other/pyproject.toml")),
        ):
            with self.subTest(mutation=name):
                self._assert_binding_refusal(
                    replaced_values(pending, python_support_selection=replacement)
                )
        for field, replacement in (
            ("state", "established"),
            ("evidence_coverage", "sufficient"),
        ):
            with self.subTest(proposition_field=field):
                altered = replace(
                    path,
                    propositions=tuple(
                        replace(p, **{field: replacement}) if p == proposition else p
                        for p in path.propositions
                    ),
                )
                self._assert_binding_refusal(
                    replaced_values(
                        pending,
                        python_support_pre_assessment=replace(
                            pre,
                            applicability=replace(pre.applicability, paths=(altered,)),
                        ),
                    )
                )
        # Absence of a chosen read is a retained selector result, not a reason to select now.
        abstained = replaced_values(pending, python_support_selection=None)
        restored = self._cold_reconstruction(abstained)
        self.assertEqual(
            restored["python"],
            independent_native_values(replace(expected, investigation_selection=None)),
        )

    def test_pre_assessment_and_nested_specifier_inputs_are_bound(self):
        _, _, boundary, _, _ = captured_case()
        values = retained_values(boundary)
        pre = values["python_support_pre_assessment"]
        relevance = values["target_relevance"]
        self._assert_binding_refusal(
            replaced_values(
                boundary,
                python_support_pre_assessment=replace(pre, target_relevance=relevance),
            )
        )
        for field, replacement in (
            ("python_line", "3.8"),
            ("requires_python", ">=3.8"),
        ):
            with self.subTest(specifier_field=field):
                changed_relevance = replace(
                    relevance,
                    specifier_result=replace(
                        relevance.specifier_result, **{field: replacement}
                    ),
                )
                changed = replaced_values(
                    boundary,
                    target_relevance=changed_relevance,
                    python_support_post_assessment=replace(
                        values["python_support_post_assessment"],
                        target_relevance=changed_relevance,
                    ),
                )
                self._assert_binding_refusal(changed)

    def test_domain_conclusions_are_preserved_without_current_semantic_rederivation(
        self,
    ):
        _, _, boundary, expected_ci, expected_python = captured_case()
        # An admitted historical result remains an owner conclusion. This constructed
        # control changes that conclusion while keeping every material basis identical;
        # it is not admission/authentication of a fabricated checkpoint or semantic proof.
        post = expected_python.impact_result
        changed_post = replace(
            post,
            applicability=replace(
                post.applicability,
                state="conflicted",
                detail="Retained historical owner conclusion.",
            ),
        )
        changed = replaced_values(boundary, python_support_post_assessment=changed_post)
        self.assertEqual(
            self._cold_reconstruction(changed),
            {
                "ci": independent_native_values(expected_ci),
                "python": independent_native_values(
                    replace(expected_python, impact_result=changed_post)
                ),
                "blocked_controls": 4,
            },
        )

    def test_unavailable_target_cannot_supply_an_available_or_unrelated_problem(self):
        _, _, boundary, _, _ = captured_case(python_variant="unavailable")
        values = retained_values(boundary)
        target = values["target_python"]
        for field, replacement in (
            ("state", "malformed_toml"),
            ("detail", "Other acquisition"),
        ):
            with self.subTest(field=field):
                result = replace(target["result"], **{field: replacement})
                relevance = replace(values["target_relevance"], target_evidence=result)
                self._assert_binding_refusal(
                    replaced_values(
                        boundary,
                        target_python={**target, "result": result},
                        target_relevance=relevance,
                        python_support_post_assessment=replace(
                            values["python_support_post_assessment"],
                            target_relevance=relevance,
                        ),
                    )
                )
        available = TargetPythonDeclaration(
            target["source"].path, target["source"].revision, ">=3.10"
        )
        relevance = replace(values["target_relevance"], target_evidence=available)
        self._assert_binding_refusal(
            replaced_values(
                boundary,
                target_python={**target, "result": available},
                target_relevance=relevance,
                python_support_post_assessment=replace(
                    values["python_support_post_assessment"], target_relevance=relevance
                ),
            )
        )

    def test_recorded_empty_results_and_unexecuted_input_operations_refuse(self):
        _, _, boundary, _, _ = captured_case()
        ci_families = {"ci_inputs", "ci_coverage", "runtime_dependency_state"}
        for family in FAMILY_CONTRACTS:
            if family in (
                "investigation_inputs",
                "ci_inputs",
                "python_support_selection",
            ):
                continue
            with self.subTest(recorded_empty=family):
                changed = replaced_values(
                    boundary,
                    **{
                        family: {"source": None, "result": None}
                        if family == "target_python"
                        else None
                    },
                )
                self._assert_binding_refusal(
                    changed,
                    refused="ci" if family in ci_families else "python",
                    reason="missing_native_material",
                )
        # A real empty CI acquisition is legal, but cannot be substituted as unexecuted
        # while evaluated empty coverage/runtime still claims to have consumed it.
        h = _Harness()
        capture = NativeInvestigationCapture()
        with patch(
            "upgradepilot.investigation.analyze_dependency_change",
            return_value=DependencyChangeAnalysis(_dependency(), ()),
        ):
            investigate_public_pull_request(
                "example/project", 7, native_capture=capture, **h.kwargs()
            )
        empty_ci = capture.snapshot()
        self._cold_reconstruction(empty_ci)
        changed = unevaluated_families(empty_ci, ("ci_inputs",))
        self._assert_binding_refusal(
            changed, refused="ci", reason="missing_native_material"
        )

    def test_all_coherent_unexecuted_prefixes_and_carried_pre_result_remain_supported(
        self,
    ):
        _, _, boundary, _, _ = captured_case()
        families = tuple(FAMILY_CONTRACTS)
        for count in range(1, len(families) + 1):
            with self.subTest(recorded_prefix=count):
                self._cold_reconstruction(
                    unevaluated_families(boundary, families[count:])
                )
        pending, _, _ = self._pending_selected_acquisition()
        pre = retained_values(pending)["python_support_pre_assessment"]
        carried = replaced_values(
            pending, python_support_selection=None, python_support_post_assessment=pre
        )
        carried = altered_record(
            carried,
            "python_support_post_assessment",
            outcome="recorded",
            producer_method="investigation.investigate_public_pull_request",
            retention_gaps=("producer_version_unavailable",),
        )
        self._cold_reconstruction(carried)
        changed = replaced_values(
            carried,
            python_support_post_assessment=replace(
                pre,
                applicability=replace(
                    pre.applicability, state="established_applicable"
                ),
            ),
        )
        self._assert_binding_refusal(changed)

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
