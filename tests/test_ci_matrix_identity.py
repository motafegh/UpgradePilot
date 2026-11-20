"""Exercise scoped CI evidence before admitting matrix runtime associations."""

from dataclasses import replace
from hashlib import sha256
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from upgradepilot.ci.dependency_exercise import (
    WorkflowDependencyCoverageInput,
    _supported_consumption_candidates,
    evaluate_dependency_ci_coverage,
)
from upgradepilot.ci.dependency_state import (
    RequirementSatisfiedAtCommandCompletion,
    compose_requirement_satisfied_at_command_completion,
    evaluate_runtime_dependency_state,
    scope_package_manager_semantics,
)
from upgradepilot.ci.runtime_execution import assess_exact_command_execution
from upgradepilot.ci.runtime_strengthening import candidate_from_consumption
from upgradepilot.ci.static_command_order import relate_invocation_after_consumption
from upgradepilot.ci.workflow_commands import inspect_workflow_dependency_evidence
from upgradepilot.ci.workflow_runtime_correlation import (
    WorkflowRuntimeCorrelationResult,
    WorkflowRuntimeJobCorrelation,
    WorkflowRuntimeStepCorrelation,
)
from upgradepilot.dependency.change import DependencyChangeSourceEvidence, DependencyVersionChange
from upgradepilot.dependency.environment import RequirementsFileDependencyContext
from upgradepilot.github.actions import WorkflowJob, WorkflowRun, WorkflowStep
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.workflow_instance_commands import materialize_workflow_job_instance
from upgradepilot.github.workflow_specialization import prepare_workflow_job_instances
from upgradepilot.workspace.native_boundary import encode_native_boundary, read_native_boundary
from upgradepilot.workspace.native_capture import NativeInvestigationCapture
from upgradepilot.workspace.native_codecs import decode_native_value, encode_native_value
from upgradepilot.workspace.native_projection import reconstruct_ci_projection
from upgradepilot.workspace.native_representation import NativeReconstructionError

from test_ci_dependency_state import _execution, _semantics
from test_workspace_native_reconstruction import captured_case


def _dependency_and_source(source, path, package):
    evidence = DependencyChangeSourceEvidence(path, "exact_requirement", "exact_base_head_files")
    return (
        DependencyVersionChange(package, package, "3.0.4", "4.0", (evidence,)),
        RequirementsFileDependencyContext(source.repository, source.revision, package, evidence),
    )


def _mapproxy_input():
    fixture_dir = Path(__file__).parent / "fixtures" / "github"
    content = (fixture_dir / "mapproxy-matrix-test.yml").read_bytes()
    receipt = json.loads((fixture_dir / "mapproxy-matrix-test.receipt.json").read_text())
    assert sha256(content).hexdigest() == receipt["fixture_sha256"]
    source = RepositoryTextFile(receipt["repository"], receipt["path"], receipt["revision"], content.decode())
    run = WorkflowRun(43457921398, 1, "Running mapproxy tests", "pull_request", source.revision,
                      "completed", "success", 1)
    # Runtime rows here are controlled. Real provider replay is independent evidence.
    jobs = (WorkflowJob(1, run.run_id, "coverage", source.revision, "completed", "success", ()),)
    return WorkflowDependencyCoverageInput(run, jobs, source, prepared=prepare_workflow_job_instances(source))


def _static(workflow, context):
    return inspect_workflow_dependency_evidence(
        workflow.definition, source_contexts=(context,),
        package=context.normalized_package, normalized_package=context.normalized_package,
        prepared=workflow.prepared,
    )


def _capture(workflow, dependency, context, coverage, runtime):
    capture = NativeInvestigationCapture()
    pr = PullRequestIdentity(
        workflow.definition.repository, 1559, "Bump soupsieve", "open", False, "dependabot",
        "master", "a6507dd0dba671e48d303a74f7a5575dadf7fd76",
        "dependabot/pip/soupsieve-4.0", workflow.definition.revision, 1,
    )
    capture.start(pr, (ChangedFile(context.source_path, "modified", 1, 1, 2, None),),
                  dependency, (context,))
    capture.capture_ci((workflow,), coverage, runtime)
    return capture.partial_snapshot()


class ScopedCommandIdentityTests(unittest.TestCase):
    def test_real_mapproxy_source_keeps_every_context_and_seven_requirements_commands(self):
        workflow = _mapproxy_input()
        dependency, context = _dependency_and_source(workflow.definition, "requirements-tests.txt", "soupsieve")
        static = _static(workflow, context)
        self.assertEqual(static.job_count, 8)
        candidates = _supported_consumption_candidates(static)
        self.assertEqual([c.job_key for c in candidates],
                         ["test"] * 4 + ["coverage", "lint", "typechecking"])
        matrix = candidates[:4]
        self.assertEqual({c.command_location.source_order for c in matrix}, {1})
        self.assertEqual(len({c.command_location.source_span for c in matrix}), 1)
        self.assertEqual(len({c.command_location.script_identity.script_digest for c in matrix}), 1)
        self.assertEqual(len({c.command_location for c in matrix}), 4)
        self.assertEqual(len(_supported_consumption_candidates(
            replace(static, consumptions=static.consumptions * 2),
        )), 7)
        self.assertTrue(all(c.whole_step_relation is None for c in matrix))
        coverage = evaluate_dependency_ci_coverage(dependency, (workflow,), source_contexts=(context,))
        runtime = evaluate_runtime_dependency_state(dependency, (workflow,), coverage, source_contexts=(context,))
        self.assertEqual(coverage.state, "supported_not_correlated")
        self.assertEqual(coverage.workflows[0].runtime_correlation.reason, "scoped_job_correspondence_unresolved")
        self.assertEqual(len(runtime.assessments), 7)
        self.assertTrue(all(not isinstance(a.result, RequirementSatisfiedAtCommandCompletion)
                            for a in runtime.assessments))

    def test_cross_variant_step_and_package_fact_substitution_cannot_supply_success(self):
        source = RepositoryTextFile("example/project", ".github/workflows/ci.yml", "a" * 40, """jobs:
  test:
    name: Test
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python: ['3.12', '3.15']
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements.txt
      - run: soupsieve
""")
        prepared = prepare_workflow_job_instances(source)
        dependency, context = _dependency_and_source(source, "requirements.txt", "soupsieve")
        static = inspect_workflow_dependency_evidence(
            source, source_contexts=(context,), package="soupsieve",
            normalized_package="soupsieve", prepared=prepared,
        )
        first, second = static.consumptions
        self.assertEqual(relate_invocation_after_consumption(first, static.invocations[0]), "ordered_after")
        self.assertEqual(relate_invocation_after_consumption(first, static.invocations[1]), "not_after")
        self.assertEqual(first.command_location.source_span, second.command_location.source_span)
        sibling_semantics = _semantics(second)
        result = compose_requirement_satisfied_at_command_completion(
            dependency, context, first, sibling_semantics, _execution(first),
        )
        self.assertEqual(result.reason, "scoped_semantic_command_identity_mismatch")
        first_semantics = _semantics(first)
        result = scope_package_manager_semantics(
            first_semantics.command_identity,
            manager_environment=sibling_semantics.manager_environment,
            installation_destination=first_semantics.installation_destination,
            package_mutation_mode=first_semantics.package_mutation_mode,
            direct_requirement_handling=first_semantics.direct_requirement_handling,
        )
        self.assertEqual(result.reason, "semantic_command_identity_mismatch")
        result = compose_requirement_satisfied_at_command_completion(
            dependency, context, first, first_semantics, _execution(second),
        )
        self.assertEqual(result.reason, "runtime_command_identity_mismatch")

        # Controlled associated rows isolate the lookup contract. Milestone 4 owns
        # establishing such relationships from provider observations.
        matches = []
        for index, instance in enumerate(prepared.jobs[0].instances):
            job = materialize_workflow_job_instance(prepared.definition, instance)
            outcome = "success" if index == 0 else "failure"
            step = WorkflowStep(2, "Install", "completed", outcome)
            runtime = WorkflowJob(index + 1, 1, f"Test {index}", source.revision,
                                  "completed", outcome, (step,))
            matches.append(WorkflowRuntimeJobCorrelation(
                job, runtime, (WorkflowRuntimeStepCorrelation(job.steps[1], step, instance.identity),),
                instance.identity,
            ))
        correlation = WorkflowRuntimeCorrelationResult("correlated", "controlled", "", tuple(matches))
        self.assertEqual(assess_exact_command_execution(candidate_from_consumption(first),
                                                        correlation=correlation).state, "supported")
        self.assertEqual(assess_exact_command_execution(candidate_from_consumption(second),
                                                        correlation=correlation).runtime_conclusion, "failure")
        contaminated = replace(correlation, jobs=(replace(matches[0], steps=matches[1].steps),))
        self.assertEqual(assess_exact_command_execution(candidate_from_consumption(first),
                                                        correlation=contaminated).state, "unresolved")

    def test_scoped_native_capture_reopens_and_rejects_foreign_script_even_with_equal_bytes(self):
        workflow = _mapproxy_input()
        dependency, context = _dependency_and_source(workflow.definition, "requirements-tests.txt", "soupsieve")
        coverage = evaluate_dependency_ci_coverage(dependency, (workflow,), source_contexts=(context,))
        runtime = evaluate_runtime_dependency_state(dependency, (workflow,), coverage, source_contexts=(context,))
        boundary = _capture(workflow, dependency, context, coverage, runtime)
        restored = read_native_boundary(encode_native_boundary(boundary), expected_target=boundary.target)
        with (
            patch("upgradepilot.github.workflow_definition._compose_workflow_yaml",
                  side_effect=AssertionError("cold recovery parsed YAML")),
            patch("upgradepilot.github.workflow_matrix._expand_literal_matrix",
                  side_effect=AssertionError("cold recovery expanded a matrix")),
            patch("upgradepilot.github.workflow_command_analysis.Parser",
                  side_effect=AssertionError("cold recovery parsed a shell script")),
        ):
            replay = reconstruct_ci_projection(restored, expected_target=boundary.target)
        self.assertEqual(replay.workflow_inputs, (workflow,))
        self.assertEqual(replay.ci_coverage_result, coverage)
        self.assertEqual(replay.runtime_dependency_state_result, runtime)
        records = {record.family: record for record in boundary.records}
        self.assertEqual([records[f].codec_version for f in (
            "ci_inputs", "ci_coverage", "runtime_dependency_state",
        )], [2, 5, 2])
        workflow_result = coverage.workflows[0]
        first, second, *rest = workflow_result.consumptions
        swapped = replace(first, command_location=second.command_location)
        broken = replace(coverage, workflows=(
            replace(workflow_result, consumptions=(swapped, second, *rest)),
        ))
        broken_boundary = _capture(workflow, dependency, context, broken, runtime)
        with self.assertRaisesRegex(NativeReconstructionError, "retained instance, step or script"):
            reconstruct_ci_projection(broken_boundary, expected_target=boundary.target)
        for family, value, historical in (
            ("ci_inputs", (workflow,), 1), ("ci_coverage", coverage, 3),
            ("runtime_dependency_state", runtime, 1),
        ):
            with self.subTest(family=family), self.assertRaises(NativeReconstructionError):
                encode_native_value(family, value, version=historical)
        with self.assertRaises(NativeReconstructionError):
            decode_native_value("ci_coverage", 3, records["ci_coverage"].payload)

    def test_ordinary_scoped_producer_preserves_positive_execution_and_native_meaning(self):
        _, original, boundary, expected, _ = captured_case(direct_invocation=True, skipped_sibling=True)
        old = reconstruct_ci_projection(boundary, expected_target=boundary.target)
        workflow, = old.workflow_inputs
        scoped = replace(workflow, prepared=prepare_workflow_job_instances(workflow.definition))
        dependency = old.inputs.dependency_result
        contexts = old.inputs.source_contexts
        coverage = evaluate_dependency_ci_coverage(dependency, (scoped,), source_contexts=contexts)
        runtime = evaluate_runtime_dependency_state(dependency, (scoped,), coverage, source_contexts=contexts)
        self.assertEqual(coverage.state, original.ci_coverage_result.state)
        self.assertEqual(coverage.reason, original.ci_coverage_result.reason)
        self.assertEqual(coverage.workflows[0].runtime_direct_exercise_state, "supported")
        assessment, = runtime.assessments
        self.assertIsInstance(assessment.result, RequirementSatisfiedAtCommandCompletion)
        self.assertEqual(assessment.result.execution.runtime_conclusion, "success")
        self.assertEqual(assessment.consumption.job_instance.kind, "ordinary")
        capture = NativeInvestigationCapture()
        capture.start(old.inputs.pull_request, old.inputs.changed_files, dependency, contexts)
        capture.capture_ci((scoped,), coverage, runtime)
        saved = capture.partial_snapshot()
        reopened = reconstruct_ci_projection(saved, expected_target=saved.target)
        self.assertEqual(reopened.runtime_dependency_state_result, runtime)
        self.assertEqual(old, expected)

    def test_scoped_version_requests_keep_each_variant_through_cold_reopen(self):
        workflow = _mapproxy_input()
        source = replace(workflow.definition, content="""
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python: ['3.12', '3.15']
    steps:
      - run: pip install soupsieve==4.0
""")
        workflow = replace(workflow, definition=source, prepared=prepare_workflow_job_instances(source))
        dependency, context = _dependency_and_source(source, "requirements-tests.txt", "soupsieve")
        coverage = evaluate_dependency_ci_coverage(dependency, (workflow,), source_contexts=(context,))
        runtime = evaluate_runtime_dependency_state(dependency, (workflow,), coverage, source_contexts=(context,))
        boundary = _capture(workflow, dependency, context, coverage, runtime)
        restored = reconstruct_ci_projection(boundary, expected_target=boundary.target)
        requests = restored.ci_coverage_result.workflows[0].version_requests
        self.assertEqual([item.request.version for item in requests], ["4.0", "4.0"])
        self.assertEqual(
            [item.command_location.script_identity.instance.expansion_slot for item in requests],
            [0, 1],
        )
