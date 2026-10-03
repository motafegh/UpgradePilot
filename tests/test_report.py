"""Report meaning and offline consumer proof over existing investigation evidence families."""

from __future__ import annotations

import unittest
from dataclasses import replace
from datetime import UTC, datetime

from test_cli import _artifact_candidate_investigation, _supported_investigation
from test_investigation import _dependency, _Harness, _run

from upgradepilot.report import render_investigation_report
from upgradepilot.report_file import decode_report, encode_report
from upgradepilot.report_projection import project_investigation_report
from upgradepilot.upstream.claim import (
    GroundedPythonSupportDropClaim,
    GroundedUpstreamClaimSource,
)
from upgradepilot.upstream.interval import (
    AuthoritativeUpstreamIntervalEvidence,
    TaggedChangelogEvidence,
    release_interval_from_dependency_change,
)


class ReportProjectionTests(unittest.TestCase):
    def test_normal_application_composition_retains_source_and_bounded_no_claim(self):
        harness = _Harness()
        investigation = _run(harness, _dependency())
        report = project_investigation_report(investigation)
        opened = decode_report(encode_report(report))
        self.assertEqual(opened, report)
        source = next(s for s in opened.sources if s.kind == "tagged_changelog")
        self.assertEqual(
            source.content,
            investigation.upstream_interval_result.tagged_changelog.content,
        )
        self.assertIn("c" * 40, source.locator)
        claim = next(a for a in opened.assessments if a.assessment_id == "support-drop")
        self.assertEqual(claim.state, "no_support_drop_claim")
        self.assertIn("no global absence", claim.proposition)
        self.assertEqual(opened.action.state, "abstain")
        self.assertNotIn("safe", " ".join(f.statement for f in opened.findings))

    def test_grounded_model_interpretation_keeps_exact_text_offsets_and_strength(self):
        investigation = _supported_investigation()
        interval = release_interval_from_dependency_change(
            investigation.dependency_result
        )
        text = "Intro context.\nDrop Python 3.9 support.\nAdditional context.\n"
        quote = "Drop Python 3.9 support."
        source = TaggedChangelogEvidence(
            "example/upstream", interval, "c" * 40, "CHANGELOG.md", text
        )
        authority = AuthoritativeUpstreamIntervalEvidence(
            interval, "example/upstream", None, (), source, (), (), "tagged_changelog"
        )
        claim = GroundedPythonSupportDropClaim(
            "3.9",
            "1.1",
            interval,
            (
                GroundedUpstreamClaimSource(
                    "tagged_changelog",
                    "1.1",
                    source,
                    quote,
                    text.index(quote),
                    text.index(quote) + len(quote),
                ),
            ),
        )
        report = decode_report(
            encode_report(
                project_investigation_report(
                    replace(
                        investigation,
                        upstream_interval_result=authority,
                        upstream_support_drop_result=claim,
                    )
                )
            )
        )
        assessment = next(
            a for a in report.assessments if a.assessment_id == "support-drop"
        )
        self.assertEqual(assessment.strength, "grounded_interpretation")
        retained = next(s for s in report.sources if s.kind == "tagged_changelog")
        excerpt = next(s for s in report.sources if s.kind == "grounded_quote")
        positions = {f.name: f.value for f in excerpt.identity}
        self.assertEqual(
            retained.content[
                int(positions["quote_start"]) : int(positions["quote_end"])
            ],
            excerpt.content,
        )
        self.assertIn("not independent", assessment.proposition)
        self.assertTrue(
            any(
                f.assessment_id == "support-drop"
                and f.strength == "grounded_interpretation"
                for f in report.findings
            )
        )

    def test_runtime_omission_is_visible_and_cannot_look_like_closed_evidence(self):
        report = project_investigation_report(_supported_investigation())
        runtime = next(a for a in report.assessments if a.assessment_id == "runtime")
        self.assertEqual(runtime.state, "no_admitted_candidate")
        self.assertTrue(any(u.assessment_id == "runtime" for u in report.unknowns))
        self.assertTrue(
            any("Runtime requirement state" in u for u in report.action.uncertainty)
        )
        self.assertIn(
            "Runtime dependency state: no_admitted_candidate",
            render_investigation_report(report),
        )

    def test_artifact_candidate_is_not_installation_failure(self):
        investigation = replace(
            _artifact_candidate_investigation(), target_artifact_environment_results=()
        )
        report = decode_report(
            encode_report(project_investigation_report(investigation))
        )
        candidate = next(
            a for a in report.assessments if a.assessment_id == "artifact-candidate"
        )
        self.assertEqual(candidate.strength, "candidate")
        self.assertIn("not target installation failure", candidate.proposition)
        impact = next(
            a for a in report.assessments if a.assessment_id == "artifact-impact"
        )
        self.assertEqual(impact.state, "unresolved")
        self.assertTrue(
            any(u.assessment_id == "artifact-impact" for u in report.unknowns)
        )
        environments = next(
            a for a in report.assessments if a.assessment_id == "artifact-environments"
        )
        self.assertEqual(environments.state, "not established")
        self.assertIn("no supported target environment associations", environments.detail)
        self.assertIn(
            "Target artifact environments: not established",
            render_investigation_report(report),
        )
        self.assertEqual(report.action.state, "abstain")

    def test_real_command_producers_preserve_separate_positive_and_unresolved_scopes(
        self,
    ):
        from test_ci_dependency_state import (
            _dependency as runtime_dependency,
        )
        from test_ci_dependency_state import (
            _evaluate_runtime_state_for_commands,
        )

        from upgradepilot.ci.dependency_state import (
            RequirementSatisfiedAtCommandCompletion,
        )

        positive = "PIP_DRY_RUN=0 PIP_CONFIG_FILE=/dev/null PIP_TARGET= PIP_PREFIX= PIP_ROOT= PIP_ONLY_DEPS=0 PIP_ONLY_DEPENDENCIES=0 /opt/bootstrap/bin/python -m pip --python /opt/target/bin/python install --no-user --no-deps -r requirements.txt"
        runtime, coverage = _evaluate_runtime_state_for_commands(
            (positive, positive), install_conclusions=("success", "failure")
        )
        investigation = replace(
            _supported_investigation(),
            dependency_result=runtime_dependency(),
            runtime_dependency_state_result=runtime,
            ci_coverage_result=coverage,
        )
        self.assertIsInstance(
            runtime.assessments[0].result, RequirementSatisfiedAtCommandCompletion
        )
        report = decode_report(
            encode_report(project_investigation_report(investigation))
        )
        commands = [
            a
            for a in report.assessments
            if a.assessment_id.startswith("runtime-command-")
        ]
        self.assertEqual(commands[0].state, "satisfied_at_command_completion")
        self.assertNotEqual(commands[1].state, commands[0].state)
        facts = {f.name: f.value for f in commands[0].facts}
        self.assertIn("/opt/target/bin/python", facts["manager_environment"])
        self.assertIn("command_start_byte", facts)
        self.assertIn("command-completion", commands[0].proposition.lower())
        self.assertTrue(
            any(u.assessment_id == commands[1].assessment_id for u in report.unknowns)
        )
        self.assertTrue(
            any("Runtime requirement state for" in u for u in report.action.uncertainty)
        )
        self.assertTrue(
            any("later package use" in u for u in report.action.uncertainty)
        )
        self.assertEqual(report.action.state, "abstain")

    def test_halted_upstream_question_links_the_actual_prerequisite_problem(self):
        harness = _Harness()
        harness.stop_upstream_at_changelog()
        report = decode_report(
            encode_report(project_investigation_report(_run(harness, _dependency())))
        )
        problem = next(
            a for a in report.assessments if a.assessment_id == "changelog-path"
        )
        for key in ("upstream-interval", "support-drop"):
            question = next(u for u in report.unknowns if u.assessment_id == key)
            self.assertIn("No admitted changelog path.", question.reason)
            self.assertTrue(set(problem.source_ids) <= set(question.source_ids))

    def test_static_ci_with_unmatched_runtime_keeps_its_uncertainty_in_action(self):
        harness = _Harness()
        harness.set_workflow(
            "jobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - run: python -m pip install -r requirements.txt\n"
        )
        investigation = _run(harness, _dependency())
        self.assertEqual(
            investigation.ci_coverage_result.state, "supported_not_correlated"
        )
        report = decode_report(
            encode_report(project_investigation_report(investigation))
        )
        self.assertTrue(
            any(
                "supported_not_correlated" in item for item in report.action.uncertainty
            )
        )
        self.assertEqual(report.action.state, "abstain")

    def test_source_location_encodes_real_filename_characters_without_losing_identity(
        self,
    ):
        harness = _Harness()
        investigation = _run(harness, _dependency())
        source = replace(
            investigation.upstream_interval_result.tagged_changelog,
            path="notes/change log #1.md",
        )
        investigation = replace(
            investigation,
            upstream_interval_result=replace(
                investigation.upstream_interval_result, tagged_changelog=source
            ),
        )
        report = decode_report(
            encode_report(project_investigation_report(investigation))
        )
        saved = next(s for s in report.sources if s.kind == "tagged_changelog")
        self.assertTrue(saved.locator.endswith("notes/change%20log%20%231.md"))
        self.assertEqual(
            next(f.value for f in saved.identity if f.name == "path"),
            "notes/change log #1.md",
        )

    def test_generation_time_does_not_invent_source_acquisition_time(self):
        report = project_investigation_report(
            _supported_investigation(), now=datetime(2026, 10, 3, tzinfo=UTC)
        )
        pr = next(s for s in report.sources if s.kind == "pull_request")
        package = next(s for s in report.sources if s.kind == "package_metadata")
        self.assertIsNone(pr.retrieved_at)
        self.assertNotEqual(package.retrieved_at, report.generated_at)
        self.assertEqual(pr.retention, "reference_only")
        self.assertIsNone(pr.content)

    def test_terminal_controls_are_removed_without_altering_retained_evidence(self):
        investigation = _supported_investigation()
        investigation = replace(
            investigation,
            pull_request=replace(
                investigation.pull_request, title="Untrusted\x1b[31m text\x07"
            ),
        )
        report = project_investigation_report(investigation)
        self.assertNotIn("\x1b", render_investigation_report(report))
        self.assertIn(
            "\x1b", next(f.value for f in report.identity if f.name == "title")
        )
