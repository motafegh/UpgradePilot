"""Qualification of exact-attempt correspondence and scoped command evidence."""

from dataclasses import replace
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from upgradepilot.ci.dependency_exercise import evaluate_dependency_ci_coverage
from upgradepilot.ci.dependency_state import evaluate_runtime_dependency_state
from upgradepilot.ci.executable_selection import establish_executable_selection
from upgradepilot.ci.runtime_execution import assess_exact_command_execution
from upgradepilot.ci.runtime_strengthening import candidate_from_consumption
from upgradepilot.ci.workflow_runtime_correlation import correlate_workflow_runtime
from upgradepilot.dependency.analysis import DependencyChangeAnalysis
from upgradepilot.github.actions import GitHubActionsClient, WorkflowJob, WorkflowStep
from upgradepilot.github.pull_request import ChangedFile
from upgradepilot.github.workflow_command_analysis import analyze_run_step_commands
from upgradepilot.github.workflow_instance_commands import materialize_workflow_job_instance, run_script_identity
from upgradepilot.github.workflow_specialization import prepare_workflow_job_instances
from upgradepilot.investigation import investigate_public_pull_request
from upgradepilot.pypi.release import PackageReleaseProblem
from upgradepilot.report import render_investigation_report, render_report_facts
from upgradepilot.report_file import decode_report, encode_report
from upgradepilot.report_projection import project_ci_report, project_investigation_report
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
from upgradepilot.workspace.native_boundary import encode_native_boundary, read_native_boundary
from upgradepilot.workspace.native_codecs import encode_native_value
from upgradepilot.workspace.native_projection import reconstruct_ci_projection
from upgradepilot.workspace.native_representation import NativeReconstructionError

from test_ci_matrix_identity import _capture, _dependency_and_source, _mapproxy_input
from test_github_client import _observation
from test_investigation import _Harness
from test_cli import _supported_investigation


_FIXTURE = Path(__file__).parent / "fixtures/github/mapproxy-runtime-attempt.json"
_ORACLES = Path(__file__).resolve().parents[1] / (
    "working-memory/evidence/2026-11-18-matrix-baseline-and-oracles/ACCEPTANCE_ORACLES.json"
)


def frozen_workflow():
    workflow = _mapproxy_input()
    retained = json.loads(_FIXTURE.read_bytes())
    metadata = retained["provenance"]
    assert (metadata["run_id"], metadata["run_attempt"]) == (workflow.run.run_id, workflow.run.run_attempt)
    assert metadata["recorded_response_sha256"] == "cb2b1361da178a44936bf731476a4a4aacdc0f53eb515885fc64574da3b33c8b"
    identity = replace(
        _Harness().identity,
        repository=workflow.definition.repository, head_sha=workflow.definition.revision,
    )
    jobs = tuple(GitHubActionsClient._parse_workflow_job(identity, workflow.run, row) for row in retained["jobs"])
    assert len(jobs) == retained["total_count"] == 8 and sum(len(job.steps) for job in jobs) == 79
    return replace(workflow, jobs=jobs)


def _correlate(workflow, jobs=None):
    return correlate_workflow_runtime(
        workflow.definition, workflow.run, workflow.jobs if jobs is None else jobs,
        prepared=workflow.prepared,
    )


def _job(workflow, job_id):
    return next(job for job in workflow.jobs if job.job_id == job_id)


def _edit_job(workflow, job_id, **changes):
    return tuple(replace(job, **changes) if job.job_id == job_id else job for job in workflow.jobs)


def _match(result, runtime_id):
    return next(match for match in result.jobs if match.runtime_job.job_id == runtime_id)


def _with_source(workflow, content):
    source = replace(workflow.definition, content=content)
    return replace(workflow, definition=source, prepared=prepare_workflow_job_instances(source))


class MatrixAssociationTests(unittest.TestCase):
    def test_first_view_groups_successful_scoped_commands_and_keeps_detail(self):
        workflow = frozen_workflow()
        dependency, context = _dependency_and_source(
            workflow.definition, "requirements-tests.txt", "soupsieve"
        )
        coverage = evaluate_dependency_ci_coverage(dependency, (workflow,), source_contexts=(context,))
        runtime = evaluate_runtime_dependency_state(
            dependency, (workflow,), coverage, source_contexts=(context,)
        )
        base = _supported_investigation()
        result = replace(
            base,
            pull_request=replace(base.pull_request, repository=workflow.definition.repository,
                                 head_sha=workflow.definition.revision),
            dependency_result=dependency, workflow_evidence=((workflow.run, workflow.jobs),),
            ci_coverage_result=coverage, runtime_dependency_state_result=runtime,
            ci_workflow_inputs=(workflow,),
        )
        normal = project_investigation_report(result)
        saved = encode_report(normal)
        reopened = decode_report(saved)
        self.assertEqual(encode_report(reopened), saved)
        source, = (item for item in reopened.sources if item.kind == "workflow_execution")
        for view in (render_investigation_report(normal), render_investigation_report(reopened, saved=True)):
            opening, detail = view.split("Detailed evidence and action status", 1)
            self.assertIn("Run 43457921398 attempt 1: 7 successful scoped command observations", opening)
            self.assertIn("Command: pip install -r requirements-tests.txt", opening)
            self.assertNotIn("pip install Pillow", opening)
            steps = {line.partition(": ")[0]: line for line in opening.splitlines() if line.startswith("Step ")}
            self.assertIn("test (3.12, 13.0.0) (job 131996881880)", steps["Step 6"])
            self.assertIn("coverage (job 131996881258)", steps["Step 6"])
            self.assertIn("typechecking (job 131996881059)", steps["Step 4"])
            self.assertIn("Associated jobs with no admitted command observation: 1.", opening)
            self.assertEqual(opening.count("Installed version: unresolved"), 1)
            self.assertIn(f"--show-facts {source.source_id}", opening)
            self.assertIn("Maintainer action: abstain", detail)
            self.assertEqual(detail.count("Command-completion requirement state: unresolved"), 7)
        self.assertIn("Job 131996881880", render_report_facts(reopened, source.source_id))

        with patch("upgradepilot.report_projection._REPORTED_STEP_DETAIL_BYTES", 0):
            without_step_facts = project_investigation_report(result)
        self.assertNotIn("CI command execution\n", render_investigation_report(without_step_facts))

    def test_normal_investigation_delivers_mixed_matrix_rows_with_no_raw_step_budget(self):
        workflow = frozen_workflow()
        definition = workflow.definition
        dependency, context = _dependency_and_source(
            definition, "requirements-tests.txt", "soupsieve"
        )
        harness = _Harness()
        harness.package_client.get_release.side_effect = None
        harness.package_client.get_release.return_value = PackageReleaseProblem(
            "version_not_found", "soupsieve", "soupsieve", "4.0",
            "https://pypi.org/pypi/soupsieve/4.0/json", "Controlled unrelated package response.",
        )
        identity = replace(
            harness.identity, repository=definition.repository, head_sha=definition.revision
        )
        harness.pull_client.get_pull_request_observation.return_value = _observation(identity)
        harness.pull_client.get_changed_files.return_value = (
            ChangedFile("requirements-tests.txt", "modified", 1, 1, 2,
                        "-soupsieve==3.0.4\n+soupsieve==4.0"),
        )
        harness.repository_client.get_exact_head_workflow_file.return_value = definition
        harness.actions_client.get_exact_head_workflow_runs.return_value = (workflow.run,)
        cancelled_id = 131996881564
        skipped_id = 131996881411
        absent_id = 131996881633
        jobs = _edit_job(
            workflow, cancelled_id, conclusion="cancelled",
            steps=tuple(step for step in _job(workflow, cancelled_id).steps if step.number < 6),
        )
        workflow = replace(workflow, jobs=jobs)
        harness.actions_client.get_workflow_jobs.return_value = tuple(
            job for job in _edit_job(workflow, skipped_id, conclusion="skipped", steps=())
            if job.job_id != absent_id
        )
        with TemporaryDirectory() as directory:
            store = CheckpointStore.create(Path(directory) / "workspace", schema_version=2)
            with patch(
                "upgradepilot.investigation_inputs.analyze_dependency_change",
                return_value=DependencyChangeAnalysis(dependency, (context,)),
            ):
                result = investigate_public_pull_request(
                    identity.repository, identity.number,
                    workspace_host=InvestigationWorkspaceHost(store=store), **harness.kwargs(),
                )
            revision = store.read_selected_revision(result.workspace_revision.revision_id).revision
            recovered = reconstruct_ci_projection(revision.boundary, expected_target=revision.boundary.target)

        with patch("upgradepilot.report_projection._REPORTED_STEP_DETAIL_BYTES", 0):
            report = decode_report(encode_report(project_investigation_report(result)))
            partial = project_ci_report(
                pull_request=recovered.inputs.pull_request,
                dependency_result=recovered.inputs.dependency_result,
                workflow_evidence=tuple((item.run, item.jobs) for item in recovered.workflow_inputs),
                ci_coverage_result=recovered.ci_coverage_result,
                runtime_dependency_state_result=recovered.runtime_dependency_state_result,
                workflow_inputs=recovered.workflow_inputs,
            )

        def job_facts(assessments):
            return {
                item.assessment_id: (item.state, item.reason, {f.name: f.value for f in item.facts})
                for item in assessments if item.assessment_id.startswith("ci-job-instance-")
            }

        rows = job_facts(report.assessments)
        self.assertEqual(rows, job_facts(partial.assessments))
        self.assertEqual(len(rows), 9)  # Eight declared job contexts and one unassigned skip.
        self.assertEqual(rows["ci-job-instance-1-0-0"][2]["runtime_job_id"], "131996881880")
        self.assertEqual(rows["ci-job-instance-1-0-1"][2]["runtime_conclusion"], "cancelled")
        self.assertEqual(rows["ci-job-instance-1-0-2"][0], "unresolved")
        self.assertEqual(rows["ci-job-instance-1-0-3"][0], "unresolved")
        self.assertEqual(
            rows[f"ci-job-instance-1-reported-{skipped_id}"][2]["runtime_conclusion"], "skipped"
        )
        self.assertTrue(any(f.name == "reported_steps_omission"
                            for item in report.sources for f in item.identity))
        commands = [item for item in report.assessments if item.assessment_id.startswith("runtime-command-")]
        self.assertEqual(len(commands), 7)
        self.assertTrue(all(item.state == "unresolved" for item in commands))
        self.assertEqual(
            [next(f.value for f in item.facts if f.name == "execution_state") for item in commands],
            ["supported", "unresolved", "unresolved", "unresolved", "supported", "supported", "supported"],
        )
        self.assertNotIn("CI command execution\n", render_investigation_report(report, saved=True))

    def test_frozen_install_execution_keeps_later_command_package_and_test_proofs_distinct(self):
        workflow = frozen_workflow()
        dependency, context = _dependency_and_source(workflow.definition, "requirements-tests.txt", "soupsieve")
        coverage = evaluate_dependency_ci_coverage(dependency, (workflow,), source_contexts=(context,))
        runtime = evaluate_runtime_dependency_state(dependency, (workflow,), coverage, source_contexts=(context,))
        oracles = json.loads(_ORACLES.read_bytes())["observed_success_case"]
        result = coverage.workflows[0]
        self.assertEqual(result.direct_exercise_state, "not_established")
        self.assertEqual(len(runtime.assessments), 7)
        for assessment, oracle in zip(
            runtime.assessments, (item for item in oracles if item["original_yaml_job"] != "doc"),
            strict=True,
        ):
            consumption = assessment.consumption
            command = assessment.execution
            match = _match(result.runtime_correlation, oracle["runtime_job_id"])
            self.assertEqual(consumption.job_instance, match.job_instance)
            self.assertEqual(command.state, "supported")
            self.assertEqual(command.step_execution.correlation.job_instance, match.job_instance)
            later = consumption.job_key in {"test", "coverage"}
            self.assertEqual(command.step_execution.correlation.runtime_step.number, 6 if later else 4)
            self.assertEqual(command.command_location.source_order, 1 if later else 0)
            self.assertEqual(assessment.result.state, "unresolved")
            self.assertEqual(assessment.result.reason, "manager_environment_needs_lower_source_evidence")
        first, second, *rest = runtime.assessments
        forged = replace(runtime, assessments=(replace(first, execution=second.execution), second, *rest))
        boundary = _capture(workflow, dependency, context, coverage, forged)
        with self.assertRaisesRegex(NativeReconstructionError, "another exact command identity"):
            reconstruct_ci_projection(boundary, expected_target=boundary.target)

    def test_genuine_attempt_matches_all_eight_independent_oracles_without_runtime_job_labels(self):
        workflow = frozen_workflow()
        # The mixed workflow uses unnamed YAML jobs. Runtime job labels carry no
        # authority for these positive matches; reverse the list as another control.
        stripped_labels = tuple(
            replace(job, name="provider-default-label") for job in reversed(workflow.jobs)
        )
        result = _correlate(workflow, stripped_labels)
        self.assertEqual(result.state, "correlated")
        self.assertEqual(len(result.jobs), 8)
        self.assertEqual(len({match.job_instance for match in result.jobs}), 8)
        self.assertFalse(result.scoped.unmatched_instances)
        self.assertFalse(result.scoped.unassigned_jobs)
        expected = json.loads(_ORACLES.read_bytes())["observed_success_case"]
        for record in expected:
            match = _match(result, record["runtime_job_id"])
            identity = match.job_instance
            prepared = workflow.prepared.jobs[identity.job_source_index].instances[identity.expansion_slot]
            self.assertEqual(
                {coordinate.name: coordinate.literal.value for coordinate in prepared.coordinates},
                record["coordinates"],
            )
            self.assertEqual(identity.job_key, record["original_yaml_job"])
            self.assertEqual(match.runtime_job.conclusion, record["frozen_job_outcome"])
            install = record.get("selected_requirements_install_step")
            if install is not None:
                witness, = (step for step in match.steps if step.runtime_step.number == install)
                self.assertIn("pip install -r requirements-tests.txt", witness.static_step.command.text)
            self.assertTrue(match.association.witness_step_numbers)
            self.assertFalse(match.association.step_problems)

    def test_missing_or_repeated_install_keeps_independent_job_correspondence(self):
        workflow = frozen_workflow()
        job = _job(workflow, 131996881880)
        install = next(step for step in job.steps if step.number == 6)
        for runtime_steps, reason in (
            (tuple(step for step in job.steps if step.number != 6), "runtime_step_match_missing"),
            ((*job.steps, replace(install, number=99)), "runtime_step_match_ambiguous"),
        ):
            with self.subTest(reason=reason):
                result = _correlate(workflow, _edit_job(workflow, job.job_id, steps=runtime_steps))
                self.assertEqual(result.state, "partially_correlated")
                self.assertEqual(len(result.jobs), 8)
                match = _match(result, job.job_id)
                self.assertEqual([(p.source_index, p.reason) for p in match.association.step_problems], [(3, reason)])
                self.assertTrue(any(step.runtime_step.name == "Use python 3.12" for step in match.steps))
                self.assertTrue(all(step.static_step.source_index != 3 for step in match.steps))

    def test_ambiguous_or_conflicting_rows_do_not_become_unique_by_elimination(self):
        workflow = frozen_workflow()
        a, b = (_job(workflow, job_id) for job_id in (131996881880, 131996881633))
        discriminator = next(step for step in a.steps if step.name == "Use python 3.12")
        for steps, reason in (
            (tuple(s for s in a.steps if s != discriminator), "static_job_match_ambiguous"),
            ((*a.steps, replace(discriminator, number=99)), "static_job_match_ambiguous"),
            ((*a.steps, replace(discriminator, name="Use python 3.15", number=99)), "conflicting_job_or_step_witnesses"),
        ):
            with self.subTest(reason=reason, count=len(steps)):
                result = _correlate(workflow, _edit_job(workflow, a.job_id, steps=steps))
                affected = next(item for item in result.scoped.unassigned_jobs if item.job.job_id == a.job_id)
                self.assertEqual(affected.reason, reason)
                self.assertNotIn(a.job_id, {match.runtime_job.job_id for match in result.jobs})
                self.assertNotIn(b.job_id, {match.runtime_job.job_id for match in result.jobs})
                self.assertEqual(_match(result, 131996881440).job_instance.job_key, "doc")

    def test_same_source_witness_on_two_runtime_rows_preserves_both_candidates(self):
        workflow = frozen_workflow()
        original = _job(workflow, 131996881880)
        mirrored = replace(original, job_id=99)
        for extra, reason in ((mirrored, "runtime_job_match_ambiguous"),
                              (original, "duplicate_runtime_job_id")):
            result = _correlate(workflow, (*workflow.jobs, extra))
            self.assertEqual(len(result.jobs), 7)
            self.assertEqual(len(result.scoped.unassigned_jobs), 2)
            self.assertEqual({item.reason for item in result.scoped.unassigned_jobs}, {reason})
            self.assertEqual(result.scoped.unmatched_instances[0].instance.expansion_slot, 0)
        foreign = replace(original, job_id=99, run_id=987)
        result = _correlate(workflow, (*workflow.jobs, foreign))
        self.assertEqual(len(result.jobs), 8)
        self.assertEqual(result.scoped.unassigned_jobs[0].reason, "runtime_job_scope_mismatch")

    def test_unresolved_competing_origin_blocks_apparently_unique_association(self):
        workflow = frozen_workflow()
        source = workflow.definition.content + """
  delegated:
    uses: owner/project/.github/workflows/reusable.yml@main
"""
        result = _correlate(_with_source(workflow, source))
        self.assertFalse(result.jobs)
        self.assertEqual(result.scoped.unresolved_source_jobs, (5,))
        self.assertTrue(all(item.reason == "static_competing_origin_unresolved"
                            for item in result.scoped.unassigned_jobs))

    def test_frozen_default_fail_fast_mixed_lifecycle_remains_job_and_step_scoped(self):
        workflow = frozen_workflow()
        original = workflow.prepared.definition.jobs[0]
        self.assertIsNone(original.continue_on_error)
        self.assertEqual([field.key.text for field in original.strategy.entries], ["matrix"])
        fail, cancel, queued, absent = (131996881880, 131996881564, 131996881411, 131996881633)
        rows = []
        for job in workflow.jobs:
            if job.job_id == fail:
                job = replace(job, conclusion="failure", steps=tuple(
                    replace(step, conclusion={6: "failure", 7: "skipped"}[step.number])
                    if step.number in {6, 7} else step for step in job.steps
                ))
            elif job.job_id == cancel:
                job = replace(job, conclusion="cancelled", steps=tuple(
                    step for step in job.steps if step.number <= 5
                ))
            elif job.job_id == queued:
                job = replace(job, status="queued", conclusion=None, steps=())
            elif job.job_id == absent:
                continue
            rows.append(job)
        result = _correlate(workflow, rows)
        self.assertEqual(len(result.jobs), 6)
        failed = _match(result, fail)
        self.assertEqual(failed.runtime_job.conclusion, "failure")
        self.assertEqual({step.runtime_step.number: step.runtime_step.conclusion for step in failed.steps}[6], "failure")
        self.assertEqual({step.runtime_step.number: step.runtime_step.conclusion for step in failed.steps}[7], "skipped")
        cancelled = _match(result, cancel)
        self.assertEqual((cancelled.runtime_job.conclusion, cancelled.runtime_job.start_phase), ("cancelled", "started"))
        self.assertTrue(all(step.runtime_step.number < 6 for step in cancelled.steps))
        queued_observation, = result.scoped.unassigned_jobs
        self.assertEqual(queued_observation.job.job_id, queued)
        self.assertEqual(queued_observation.job.start_phase, "unstarted_at_observation")
        self.assertEqual({item.instance.expansion_slot for item in result.scoped.unmatched_instances}, {2, 3})
        self.assertNotIn(absent, {item.job.job_id for item in result.scoped.unassigned_jobs})
        self.assertEqual({match.job_instance.job_key for match in result.jobs if match.job_instance.kind == "ordinary"},
                         {"coverage", "doc", "lint", "typechecking"})
        partial = replace(workflow, jobs=tuple(rows),
                          run=replace(workflow.run, status="in_progress", conclusion=None))
        dependency, context = _dependency_and_source(partial.definition, "requirements-tests.txt", "soupsieve")
        coverage = evaluate_dependency_ci_coverage(dependency, (partial,), source_contexts=(context,))
        runtime = evaluate_runtime_dependency_state(dependency, (partial,), coverage, source_contexts=(context,))
        saved = _capture(partial, dependency, context, coverage, runtime)
        recovered = reconstruct_ci_projection(saved, expected_target=saved.target)
        self.assertEqual(recovered.ci_coverage_result.workflows[0].runtime_correlation, result)
        self.assertEqual(recovered.runtime_dependency_state_result, runtime)
        self.assertTrue(all(assessment.result.state == "unresolved" for assessment in runtime.assessments))
        self.assertEqual(
            [(row.execution.state, row.execution.runtime_conclusion) for row in runtime.assessments],
            [("not_established", "failure"), ("unresolved", None), ("unresolved", None),
             ("unresolved", None), *([("supported", "success")] * 3)],
        )

        cancelled_after_install = _job(workflow, cancel)
        snapshot = _correlate(workflow, _edit_job(
            workflow, cancel, conclusion="cancelled",
            steps=tuple(step for step in cancelled_after_install.steps if step.number <= 6),
        ))
        self.assertEqual({step.runtime_step.number: step.runtime_step.conclusion
                          for step in _match(snapshot, cancel).steps}[6], "success")
        self.assertEqual(assess_exact_command_execution(
            candidate_from_consumption(runtime.assessments[1].consumption), correlation=snapshot,
        ).state, "supported")

        successful_sibling = _match(snapshot, cancel)
        sibling_step = next(item for item in successful_sibling.steps if item.runtime_step.number == 6)
        forged_step = replace(sibling_step, job_instance=failed.job_instance)
        forged_correlation = replace(result, jobs=tuple(
            replace(job, steps=tuple(forged_step if step.runtime_step.number == 6 else step
                                     for step in job.steps))
            if job == failed else job for job in result.jobs
        ))
        self.assertEqual(assess_exact_command_execution(
            candidate_from_consumption(runtime.assessments[0].consumption), correlation=forged_correlation,
        ).basis, "step_correlation_unresolved")

    def test_explicit_skip_matches_without_steps_and_unidentified_skip_stays_unassigned(self):
        workflow = frozen_workflow()
        job_id = 131996881880
        rows = _edit_job(workflow, job_id, conclusion="skipped", steps=())
        result = _correlate(workflow, rows)
        skipped, = result.scoped.unassigned_jobs
        self.assertEqual((skipped.job.conclusion, skipped.job.start_phase), ("skipped", "unknown"))
        named = _with_source(workflow, workflow.definition.content.replace(
            "  test:\n", "  test:\n    name: Explicit Python ${{ matrix.python-version }}\n", 1,
        ))
        named_rows = tuple(
            replace(job, name=f"Explicit Python {job.name.split('(')[1].split(',')[0]}")
            if job.name.startswith("test (") else job for job in rows
        )
        matched = _correlate(named, named_rows)
        self.assertEqual(matched.state, "correlated_with_skipped_jobs")
        match = _match(matched, job_id)
        self.assertEqual(match.association.explicit_job_name, "Explicit Python 3.12")
        self.assertEqual(match.steps, ())
        self.assertEqual(match.association.witness_step_numbers, ())
        cancelled = tuple(replace(job, conclusion="cancelled") if job.job_id == job_id else job
                          for job in named_rows)
        self.assertEqual(_match(_correlate(named, cancelled), job_id).runtime_job.start_phase, "unknown")
        queued = tuple(replace(job, status="queued", conclusion=None) if job.job_id == job_id else job
                       for job in named_rows)
        self.assertEqual(_match(_correlate(named, queued), job_id).runtime_job.start_phase,
                         "unstarted_at_observation")

    def test_cold_storage_preserves_partial_association_and_refuses_missing_references(self):
        workflow = frozen_workflow()
        original = _job(workflow, 131996881880)
        workflow = replace(workflow, jobs=_edit_job(
            workflow, original.job_id, steps=tuple(step for step in original.steps if step.number != 6),
        ))
        dependency, context = _dependency_and_source(workflow.definition, "requirements-tests.txt", "soupsieve")
        coverage = evaluate_dependency_ci_coverage(dependency, (workflow,), source_contexts=(context,))
        runtime = evaluate_runtime_dependency_state(dependency, (workflow,), coverage, source_contexts=(context,))
        boundary = _capture(workflow, dependency, context, coverage, runtime)
        with patch("upgradepilot.ci.workflow_runtime_correlation._correlate_prepared_matrix",
                   side_effect=AssertionError("Cold recovery reran matrix association.")):
            restored = read_native_boundary(encode_native_boundary(boundary), expected_target=boundary.target)
            reopened = reconstruct_ci_projection(restored, expected_target=boundary.target)
        self.assertEqual(reopened.ci_coverage_result, coverage)
        self.assertEqual(reopened.runtime_dependency_state_result, runtime)
        with self.assertRaises(NativeReconstructionError):
            encode_native_value("ci_coverage", coverage, version=4)
        workflow_result, = coverage.workflows
        correlation = workflow_result.runtime_correlation
        for bad in (
            replace(correlation, scoped=replace(correlation.scoped, run_attempt=2)),
            replace(correlation, jobs=correlation.jobs[1:]),
            replace(correlation, jobs=(
                replace(correlation.jobs[0], association=replace(
                    correlation.jobs[0].association, witness_step_numbers=(6,),
                )),
                *correlation.jobs[1:],
            )),
        ):
            with self.subTest(bad=bad.reason):
                forged = replace(coverage, workflows=(replace(workflow_result, runtime_correlation=bad),))
                saved = _capture(workflow, dependency, context, forged, runtime)
                with self.assertRaisesRegex(NativeReconstructionError, "attempt|partition|witness numbers"):
                    reconstruct_ci_projection(saved, expected_target=saved.target)

    def test_setup_python_consumer_uses_its_own_variant_in_mixed_outcomes(self):
        workflow = _with_source(frozen_workflow(), """jobs:
  test:
    name: Python ${{ matrix.python }}
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python: ['3.12', '3.15']
    steps:
      - name: Use python ${{ matrix.python }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python }}
      - name: Invoke
        run: python -m pip --version
""")
        rows = tuple(
            WorkflowJob(
                index + 1, workflow.run.run_id, f"Python {version}", workflow.run.head_sha,
                "completed", outcome,
                (
                    WorkflowStep(1, f"Use python {version}", "completed", outcome),
                    WorkflowStep(2, "Invoke", "completed", "success" if outcome == "success" else "skipped"),
                ),
            )
            for index, (version, outcome) in enumerate((("3.12", "success"), ("3.15", "failure")))
        )
        correlation = _correlate(workflow, rows)
        self.assertEqual(len(correlation.jobs), 2)
        definition = workflow.prepared.definition
        outcomes = []
        for instance in workflow.prepared.jobs[0].instances:
            job = materialize_workflow_job_instance(definition, instance)
            step = job.steps[1]
            analysis = analyze_run_step_commands(
                definition, job, step, script_identity=run_script_identity(instance, 1),
            )
            result = establish_executable_selection(
                definition, job, step, analysis.command_occurrences[0], correlation=correlation,
            )
            outcomes.append(result)
        self.assertEqual(outcomes[0].state, "established")
        self.assertEqual(outcomes[1].reason, "setup_python_runtime_execution_not_supported")

    def test_specializing_unnamed_run_text_does_not_invent_runner_display_witness(self):
        workflow = _with_source(frozen_workflow(), """jobs:
  test:
    name: Slot ${{ matrix.slot }}
    runs-on: ubuntu-latest
    strategy:
      matrix:
        slot: [a, b]
    steps:
      - run: echo ${{ matrix.slot }}
""")
        rows = tuple(
            WorkflowJob(i, workflow.run.run_id, f"Slot {value}", workflow.run.head_sha,
                        "completed", "success",
                        (WorkflowStep(1, f"Run echo {value}", "completed", "success"),))
            for i, value in enumerate(("a", "b"), 1)
        )
        result = _correlate(workflow, rows)
        self.assertEqual(result.state, "partially_correlated")
        self.assertEqual(len(result.jobs), 2)
        for match in result.jobs:
            self.assertEqual(match.steps, ())
            self.assertEqual(match.association.step_problems[0].reason, "unnamed_run_step_display_name_dynamic")
