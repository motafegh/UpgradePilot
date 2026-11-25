"""Shared, framework-independent investigation report and deterministic human rendering.

``report_projection.project_investigation_report`` supplies this record from typed domain
results. ``report_file`` encodes/validates it; reopening reconstructs only these records.
No rendering or decoding operation acquires evidence or grants action permission.
Source content can be richer than the displayed summary, enabling non-rendering consumers.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ReportFact:
    name: str
    label: str
    value: str


@dataclass(frozen=True, slots=True)
class ReportSource:
    source_id: str
    kind: str
    locator: str | None
    identity: tuple[ReportFact, ...]
    method: str
    retrieved_at: str | None
    retention: str
    content: str | None
    limitation: str


@dataclass(frozen=True, slots=True)
class ReportAssessment:
    assessment_id: str
    topic: str
    owner: str
    state: str
    status: str
    reason: str
    detail: str
    proposition: str
    strength: str
    source_ids: tuple[str, ...]
    facts: tuple[ReportFact, ...]
    limitations: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ReportFinding:
    assessment_id: str
    statement: str
    strength: str
    source_ids: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ReportUnknown:
    assessment_id: str
    question: str
    reason: str
    source_ids: tuple[str, ...]
    consequence: str


@dataclass(frozen=True, slots=True)
class ReportAction:
    state: str
    reasons: tuple[str, ...]
    uncertainty: tuple[str, ...]
    limitations: tuple[str, ...]
    claim_limits: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class InvestigationReport:
    report_id: str
    generated_at: str
    generator_version: str
    product_version: str | None
    auth_mode: str
    production_limits: tuple[str, ...]
    identity: tuple[ReportFact, ...]
    assessments: tuple[ReportAssessment, ...]
    findings: tuple[ReportFinding, ...]
    unknowns: tuple[ReportUnknown, ...]
    action: ReportAction
    sources: tuple[ReportSource, ...]
    preservation_limits: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class CIReport:
    """CI-only presentation of owned results; no synthetic whole-result or action.

    Uses the same assessment/source records as InvestigationReport. Native material
    identities and historical retention gaps belong to the caller's capture boundary.
    This is an internal view, not a new saved-report file format.
    """

    identity: tuple[ReportFact, ...]
    assessments: tuple[ReportAssessment, ...]
    findings: tuple[ReportFinding, ...]
    unknowns: tuple[ReportUnknown, ...]
    sources: tuple[ReportSource, ...]
    limits: tuple[str, ...]


def render_investigation_report(
    report: InvestigationReport, *, saved: bool = False
) -> str:
    """Describe exactly the record supplied; saved mode never refreshes its contents."""
    lines = ["UpgradePilot public pull-request evidence"]
    lines.append(
        "Mode: saved report; no live refresh"
        if saved
        else "Mode: new investigation report"
    )
    lines.extend(
        (
            f"Report: {report.report_id}",
            f"Generated at: {report.generated_at}",
            f"Recorded generator version: {report.generator_version}; renderer version: 9",
            f"Product version: {report.product_version or 'not recorded'}",
        )
    )
    lines.extend(f"{fact.label}: {fact.value}" for fact in report.identity)
    lines.extend(_first_view_lines(report))
    lines.extend(_assessment_lines(
        report.assessments, report.unknowns,
        pr_description_cue=_pr_description_cue(report, saved=saved),
    ))
    lines.extend(("", f"Maintainer action: {report.action.state}"))
    lines.extend(f"Action reason: {reason}" for reason in report.action.reasons)
    lines.extend(
        f"Remaining uncertainty: {value}" for value in report.action.uncertainty
    )
    lines.extend(f"Action limitation: {value}" for value in report.action.limitations)
    lines.extend(f"Claim limit: {value}" for value in report.action.claim_limits)
    lines.extend(_source_lines(report.sources))
    if any(source.retention == "retained_text" for source in report.sources):
        lines.append(
            "Inspect retained source text with --open-report PATH --show-source SOURCE_ID. "
            "For a new investigation, first save explicitly with --save-report PATH."
        )
    lines.extend(("", "Report limits"))
    lines.extend(report.production_limits + report.preservation_limits)
    return _display_lines(lines)


def _pr_description_cue(report: InvestigationReport, *, saved: bool) -> tuple[str, ...]:
    """Direct the reader to recorded PR text without interpreting its contents."""

    sources = [source for source in report.sources if source.kind == "pull_request"]
    if len(sources) != 1:
        return ()
    source = sources[0]
    states = [fact.value for fact in source.identity if fact.name == "description_state"]
    if source.retention != "retained_text" or states != ["retained"] or not (source.content or "").strip():
        return ()
    inspection = "Inspect with" if saved else "Save with --save-report PATH, then inspect with"
    return (
        "",
        "Retained PR description is available. PR-authored or copied text remains unverified as upstream evidence.",
        f"{inspection} --open-report PATH --show-source {source.source_id}.",
    )


def _first_view_lines(report: InvestigationReport) -> list[str]:
    """Group recorded assessments for a quick read while leaving full detail below."""
    assessments = {item.assessment_id: item for item in report.assessments}
    dependency = assessments.get("dependency")
    if dependency is None or (dependency.status, dependency.state) != ("available", "supported"):
        return []
    transition = {fact.name: fact.value for fact in dependency.facts}
    if (len(transition) != len(dependency.facts)
            or not all(transition.get(name) for name in ("package", "old_version", "proposed_version"))):
        return []

    sections = _signature_overview(report, transition)
    sections.extend(_ci_log_overview(report))
    sections.extend(_ci_command_overview(report, assessments.get("ci")))
    artifact = assessments.get("artifact-candidate")
    if artifact is not None and (artifact.status, artifact.state) == ("available", "established"):
        sections.extend(_artifact_overview(artifact, assessments, report.unknowns))

    support = assessments.get("support-drop")
    tag = assessments.get("tag")
    # A failed tag belongs in this section only when the support assessment cites it.
    if (support is not None and support.status == "not_evaluated"
            and tag is not None and tag.status == "problem"
            and tag.source_ids and tag.source_ids[0] in support.source_ids):
        sections.extend((
            "", "Upstream support evaluation: not evaluated",
            f"{tag.topic}: {tag.detail}",
            _evidence_refs(tag, support),
        ))

    if not sections:
        return []
    return [
        "", "Review at a glance",
        f"Update: {transition['package']} {transition['old_version']} -> {transition['proposed_version']}",
        *sections,
        "", "Detailed evidence and action status",
    ]


def _ci_command_overview(
    report: InvestigationReport, ci: ReportAssessment | None
) -> list[str]:
    """Summarize one attempt whose commands share an exact outcome and package-state limit."""

    if ci is None or (ci.status, ci.state) != ("available", "supported_runtime_correlated"):
        return []
    sources = [
        item for item in report.sources
        if item.source_id in ci.source_ids and item.kind == "workflow_execution"
    ]
    if len(sources) != 1 or sources[0].retention != "selected_facts":
        return []
    source = sources[0]
    attempt = {fact.name: fact.value for fact in source.identity}
    head = next((fact.value for fact in report.identity if fact.name == "head_sha"), None)
    if (len(attempt) != len(source.identity) or not head or attempt.get("head_sha") != head
            or (attempt.get("status"), attempt.get("conclusion")) != ("completed", "success")):
        return []

    jobs = {}
    job_ids = set()
    for item in report.assessments:
        if not item.assessment_id.startswith("ci-job-instance-"):
            continue
        facts = {fact.name: fact.value for fact in item.facts}
        scope = _ci_job_scope(facts, attempt)
        job_id = facts.get("runtime_job_id", "")
        job_name = facts.get("runtime_job_name", "").strip()
        if (len(facts) != len(item.facts) or scope is None or scope in jobs
                or source.source_id not in item.source_ids
                or (item.status, item.state) != ("available", "associated")
                or not re.fullmatch(r"[1-9][0-9]*", job_id) or job_id in job_ids
                or not job_name or attempt.get(f"job_{job_id}_name") != job_name
                or attempt.get(f"job_{job_id}_head_sha") != head
                or (facts.get("runtime_status"), facts.get("runtime_conclusion")) != ("completed", "success")
                or (attempt.get(f"job_{job_id}_status"), attempt.get(f"job_{job_id}_conclusion"))
                != ("completed", "success")):
            return []
        job_ids.add(job_id)
        jobs[scope] = facts
    if attempt.get("captured_job_count") != str(len(jobs)):
        return []

    counts = Counter()
    steps: dict[str, list[str]] = {}
    commands = set()
    limits = set()
    for item in report.assessments:
        if not item.assessment_id.startswith("runtime-command-"):
            continue
        facts = {fact.name: fact.value for fact in item.facts}
        scope = _ci_job_scope(facts, attempt)
        job = jobs.get(scope)
        command = _ci_command_excerpt(facts)
        step = facts.get("runtime_step_number", "")
        detail = facts.get("blocking_evidence_detail")
        # A successful workflow can contain an unresolved command. Group only
        # explicitly supported observations with the same package-state limit.
        if (len(facts) != len(item.facts) or job is None or command is None
                or source.source_id not in item.source_ids or facts.get("revision") != head
                or (item.status, item.state, item.reason)
                != ("problem", "unresolved", "manager_environment_needs_lower_source_evidence")
                or (facts.get("execution_state"), facts.get("execution_reason"))
                != ("supported", "exact_command_execution_supported")
                or facts.get("blocking_dimension") != "manager_environment" or not detail
                or not re.fullmatch(r"[1-9][0-9]*", step)
                or not job.get(f"step_{step}", "").endswith(" | completed | success")):
            return []
        job_id = job["runtime_job_id"]
        rows = attempt.get(f"job_{job_id}_reported_steps", "").splitlines()
        step_rows = [row for row in rows if row.startswith(f"{step}. ")]
        if len(step_rows) != 1 or not step_rows[0].endswith(" | 'completed' | 'success'"):
            return []
        counts[scope] += 1
        commands.add(command)
        limits.add(detail)
        steps.setdefault(step, []).append(f"{job['runtime_job_name']} (job {job_id})")
    if (len(commands) != 1 or len(limits) != 1
            or any(job.get("requirements_candidates") !=
                   (str(counts[scope]) if counts[scope] else "no admitted candidate")
                   for scope, job in jobs.items())
            or any(count != 1 for count in counts.values())):
        return []

    lines = [
        "",
        "CI command execution",
        f"Run {attempt['run_id']} attempt {attempt['run_attempt']}: "
        f"{len(counts)} successful scoped command observations",
        f"Command: {next(iter(commands))}",
    ]
    preview_limit = 8  # Bound the opening; full per-job evidence follows.
    remaining = preview_limit
    for step, labels in steps.items():
        if not remaining:
            break
        lines.append(f"Step {step}: " + "; ".join(labels[:remaining]))
        remaining -= min(remaining, len(labels))
    if len(counts) > preview_limit:
        lines.append(f"{len(counts) - preview_limit} more command observations in the detailed evidence.")
    if len(jobs) > len(counts):
        lines.append(f"Associated jobs with no admitted command observation: {len(jobs) - len(counts)}.")
    lines.extend((
        "Installed version: unresolved for these observations; the effective pip environment is unknown.",
        f"Inspect the recorded jobs and steps with --open-report PATH --show-facts {source.source_id}.",
        f"Recorded maintainer action: {report.action.state}",
    ))
    return lines


def _ci_job_scope(facts: dict[str, str], attempt: dict[str, str]) -> tuple[str, ...] | None:
    scope = tuple(facts.get(name, "") for name in (
        "run_id", "run_attempt", "job_source_index", "job_kind", "expansion_slot"
    ))
    if (not all(scope) or scope[:2] != (attempt.get("run_id"), attempt.get("run_attempt"))
            or not all(re.fullmatch(r"[1-9][0-9]*", value) for value in scope[:2])):
        return None
    return scope


def _ci_command_excerpt(facts: dict[str, str]) -> str | None:
    """Recover the admitted byte span inside a possibly multi-command script."""

    try:
        start, end = int(facts["command_start_byte"]), int(facts["command_end_byte"])
        script = facts["command"].encode()
        if not 0 <= start < end <= len(script):
            return None
        command = script[start:end].decode().strip()
    except (KeyError, ValueError):
        return None
    return command if len(command.splitlines()) == 1 else None


def _ci_log_overview(report: InvestigationReport) -> list[str]:
    witness = next(
        (item for item in report.assessments if item.assessment_id == "ci-job-log"),
        None,
    )
    if witness is None:
        return []
    facts = {fact.name: fact.value for fact in witness.facts}
    header = ["", "Selected historical CI job log (independent recorded observation)"]
    if witness.status != "available":
        return [*header, f"CI log: {witness.state}; {witness.reason}",
                "This does not establish a matching runtime cause."]
    return [
        *header,
        f"Run {facts.get('run_id', 'unknown')} attempt {facts.get('run_attempt', 'unknown')}, "
        f"job {facts.get('job_id', 'unknown')}",
        f"Observed error text: {facts.get('error_excerpt', 'not recorded')}",
        f"Installation-summary token: {facts.get('install_token', 'not recorded')} "
        "(log text only, not direct imported-module proof)",
        "Link to analyzed source: not established as loaded code; "
        "upgrade-caused regression: not established.",
        _evidence_refs(witness),
    ]


def _signature_overview(
    report: InvestigationReport, transition: dict[str, str],
) -> list[str]:
    roles = {"old_dependency": "old_version", "proposed_dependency": "proposed_version"}
    witnesses = {role: [] for role in roles}
    locations: set[tuple[str, str, str]] = set()
    heading = ["", "Caller and signature fit (conditional source evidence)"]
    details = "See detailed witnesses for the recorded calls, outcomes and conditions."
    for item in report.assessments:
        if (item.owner != "caller_signature.analysis"
                or not item.assessment_id.startswith("caller-signature-comparison-")):
            continue
        facts = {fact.name: fact.value for fact in item.facts}
        role = facts.get("role", "")
        if role in {"constraint_sample", "target_repository"}:
            continue
        if (len(facts) != len(item.facts) or role not in roles
                or item.status != "available" or not item.source_ids
                or facts.get("version") != transition[roles[role]]
                or not all(facts.get(name) for name in ("root_call_id", "root_location", "caller"))):
            return [*heading, "Witnesses lack a consistent call or version identity.", details]
        locations.add((facts["root_call_id"], facts["root_location"], facts["caller"]))
        witnesses[role].append(item)

    if not locations:
        return []
    # Comparing two roles requires the same root and compared call. The renderer
    # preserves each role's outcome and leaves all path-specific premises below.
    if len(locations) != 1:
        return [*heading, "More than one target or compared call is recorded.", details]
    if not all(witnesses.values()):
        return [*heading, "The recorded comparison is missing an old or proposed witness.", details]
    _, root_location, caller = next(iter(locations))
    lines = [*heading, f"Target call: {root_location}", f"Compared call: {caller}"]
    outcome_labels = {
        "bound": "arguments fit", "rejected": "arguments rejected",
        "undetermined": "argument fit undetermined",
    }
    for role, version_key in roles.items():
        rows = witnesses[role]
        states = {item.state for item in rows}
        if len(states) != 1 or not states <= outcome_labels.keys():
            return [*heading, "Witnesses have differing or unrecognized outcomes for one version.", details]
        label = "Old" if role == "old_dependency" else "Proposed"
        lines.append(f"{label} {transition[version_key]}: {outcome_labels[rows[0].state]}")
        if role == "proposed_dependency" and states == {"rejected"}:
            # Witness identity/outcome agreement is not sufficient to select a
            # particular failure reason. Preserve disagreement and missing facts.
            recorded = [
                tuple(sorted(fact.value for fact in item.facts if fact.name.startswith("violation_")))
                for item in rows
            ]
            if len(set(recorded)) != 1:
                return [*heading, "Witnesses disagree on the recorded rejection details.", details]
            if not recorded[0]:
                lines.append("Rejection detail: not recorded in the saved witnesses.")
            else:
                for violation in recorded[0]:
                    reason, separator, parameter = violation.partition(": ")
                    if reason == "unexpected_keyword" and separator and parameter:
                        lines.append(f"Rejected keyword: {parameter}")
                    else:
                        lines.append(f"Recorded violation: {violation}")
    paired_witnesses = tuple(witness for rows in witnesses.values() for witness in rows)
    sampled_adapters = _shared_sampled_adapter_versions(paired_witnesses, report.sources)
    if sampled_adapters:
        versions = ", ".join(f"{package} {version}" for package, version in sampled_adapters)
        lines.append(f"Sampled adapter versions: {versions}.")
    lines.append("Applies under the recorded source and dispatch assumptions. See witness conditions below.")
    open_questions = [unknown for unknown in report.unknowns
                      if unknown.assessment_id == "caller-signature-analysis"]
    lines.extend(f"Open: {unknown.question}" for unknown in open_questions)
    for item in report.assessments:
        if item.assessment_id in {"ci", "runtime"} and item.status == "not_evaluated":
            lines.append(f"{item.topic}: {item.state}")
    lines.append(_evidence_refs(*paired_witnesses, *open_questions))
    return lines


def _shared_sampled_adapter_versions(
    witnesses: tuple[ReportAssessment, ...], sources: tuple[ReportSource, ...],
) -> tuple[tuple[str, str], ...]:
    """Summarize the common exact source samples behind the displayed witnesses."""
    sources_by_id = {source.source_id: source for source in sources}
    shared_samples: set[tuple[str, str, str, str]] | None = None
    for witness in witnesses:
        samples: set[tuple[str, str, str, str]] = set()
        for source_id in witness.source_ids:
            source = sources_by_id.get(source_id)
            if source is None:
                return ()
            if source.kind != "dependency_source":
                continue
            facts = {fact.name: fact.value for fact in source.identity}
            role = facts.get("role")
            if len(facts) != len(source.identity) or role in (None, "", "not recorded"):
                return ()
            if role != "constraint_sample":
                continue
            package = facts.get("package", "")
            version = facts.get("version", "")
            repository = facts.get("repository", "")
            revision = facts.get("revision", "")
            sample_identity = (package, version, repository, revision)
            if source.retention != "retained_text" or any(
                not value or not value.isprintable() or value != value.strip() or value == "not recorded"
                for value in sample_identity
            ):
                return ()
            samples.add(sample_identity)
        # A shared label requires agreement on the recorded source identity, even when
        # separate modules or paths use the same release.
        if shared_samples is None:
            shared_samples = samples
        elif samples != shared_samples:
            return ()
    if not shared_samples or len({package for package, _, _, _ in shared_samples}) != len(shared_samples):
        return ()
    return tuple((package, version) for package, version, _, _ in sorted(shared_samples))


def _artifact_overview(
    artifact: ReportAssessment, assessments: dict[str, ReportAssessment],
    unknowns: tuple[ReportUnknown, ...],
) -> list[str]:
    publication_facts = {"removed_count", "added_count", "source_distribution"}
    facts = [fact for fact in artifact.facts if fact.name in publication_facts]
    if len(facts) != len(publication_facts) or {fact.name for fact in facts} != publication_facts:
        return []

    lines = ["", "Published artifacts"]
    lines.extend(f"{fact.label}: {fact.value}" for fact in facts)
    lines.append(f"Scope: {artifact.proposition}")
    related: list[ReportAssessment | ReportUnknown] = [artifact]
    for assessment_id in ("artifact-environments", "artifact-impact"):
        item = assessments.get(assessment_id)
        if item is not None:
            lines.append(f"{item.topic}: {item.state}")
            related.append(item)
    impact = assessments.get("artifact-impact")
    if impact is not None:
        lines.extend(f"{fact.label}: {fact.value}" for fact in impact.facts
                     if fact.name == "target_compatibility")
        # Each recorded unknown retains its own proposition. A source archive's
        # presence alone cannot supply an unobserved target build outcome.
        for unknown in unknowns:
            if unknown.assessment_id == "artifact-impact":
                lines.append(f"Open: {unknown.question} {unknown.reason}")
                related.append(unknown)
    lines.append(_evidence_refs(*related))
    return lines


def _evidence_refs(*records: ReportAssessment | ReportUnknown) -> str:
    return "Evidence references: " + ", ".join(dict.fromkeys(
        source_id for item in records for source_id in item.source_ids
    ))


def render_ci_report(report: CIReport) -> str:
    """Display CI owner results without importing interpretation or granting actions."""
    lines = ["UpgradePilot CI evidence", "Mode: recorded CI view; no live refresh"]
    lines.extend(f"{fact.label}: {fact.value}" for fact in report.identity)
    lines.extend(_assessment_lines(report.assessments, report.unknowns))
    lines.extend(_source_lines(report.sources, show_saved_fact_commands=False))
    lines.extend(("", "CI view limits", *report.limits))
    return _display_lines(lines)


def _assessment_lines(
    assessments: tuple[ReportAssessment, ...], unknowns: tuple[ReportUnknown, ...],
    *, pr_description_cue: tuple[str, ...] = (),
) -> list[str]:
    lines: list[str] = []
    for assessment in assessments:
        lines.extend(("", f"{assessment.topic}: {assessment.state}"))
        for fact in assessment.facts:
            # Keep LF boundaries visible without promoting fact text to report labels.
            first, *continuations = fact.value.split("\n")
            lines.append(f"{fact.label}: {first}")
            lines.extend(f"    | {line}" for line in continuations)
        lines.extend((f"Reason: {assessment.reason}", f"Detail: {assessment.detail}"))
        lines.append(f"Evidence meaning: {assessment.proposition}")
        lines.append(f"Evidence strength: {assessment.strength}")
        lines.append("Sources: " + ", ".join(assessment.source_ids))
        lines.extend(f"Limitation: {limit}" for limit in assessment.limitations)
        if (assessment.assessment_id, assessment.status, assessment.state) == (
            "upstream-repository", "problem", "source_unavailable"
        ):
            lines.extend(pr_description_cue)
    lines.extend(("", "Unresolved questions"))
    for unknown in unknowns:
        lines.extend(
            (
                f"Question: {unknown.question}",
                f"Why unresolved: {unknown.reason}",
                f"Consequence: {unknown.consequence}",
                "Sources: " + ", ".join(unknown.source_ids),
            )
        )
    return lines


def _source_lines(
    sources: tuple[ReportSource, ...], *, show_saved_fact_commands: bool = True,
) -> list[str]:
    lines = ["", "Evidence sources"]
    for source in sources:
        lines.append(
            f"{source.source_id}: {source.kind.replace('_', ' ')} | "
            f"{source.retention.replace('_', ' ')}"
        )
        if source.locator is not None:
            lines.append(f"  Location: {source.locator}")
        if source.kind not in {"producer_assessment", "artifact_capabilities"}:
            lines.extend(
                f"  {fact.label}: {fact.value}"
                for fact in source.identity
                if not fact.name.startswith(("file_", "job_", "release_advisory_entry_"))
            )
        lines.append(
            "  Method: recorded domain assessment"
            if source.kind == "producer_assessment"
            else f"  Method: {source.method}"
        )
        lines.append(f"  Acquisition time: {source.retrieved_at or 'not recorded'}")
        lines.append(f"  Preservation limit: {source.limitation}")
        if show_saved_fact_commands and source.kind == "workflow_execution":
            lines.append(
                "  Inspect captured jobs with "
                f"--open-report PATH --show-facts {source.source_id}."
            )
    return lines


class ReportSourceUnavailable(ValueError):
    """A report source is missing or cannot be shown in the requested view."""


def _report_source(report: InvestigationReport, source_id: str) -> ReportSource:
    source = next((s for s in report.sources if s.source_id == source_id), None)
    if source is None:
        raise ReportSourceUnavailable("Unknown report source ID.")
    return source


def render_report_facts(report: InvestigationReport, source_id: str) -> str:
    """Display the facts retained for one supported report source."""
    source = _report_source(report, source_id)
    if source.retention != "selected_facts":
        raise ReportSourceUnavailable("This source does not retain selected facts.")
    if source.kind not in {"artifact_capabilities", "package_metadata", "workflow_execution"}:
        raise ReportSourceUnavailable(f"Selected-fact inspection is unavailable for {source.kind}.")
    if not source.identity:
        raise ReportSourceUnavailable("This source has no saved fact values.")

    lines = [
        "UpgradePilot saved facts; offline, no live refresh",
        f"Report: {report.report_id}",
        f"Report generated at: {report.generated_at}",
        *(f"{fact.label}: {fact.value}" for fact in report.identity),
        f"Source: {source.source_id} | {source.kind} | {source.retention}",
        f"Location: {source.locator or 'not recorded'}",
        f"Observation time: {source.retrieved_at or 'not recorded'}",
        f"Method: {source.method}",
        f"Preservation limit: {source.limitation}",
        "",
    ]
    if source.kind == "workflow_execution":
        lines.extend(_workflow_execution_fact_lines(source))
    else:
        lines.extend((
            "Selected facts",
            *(f"{fact.label} [{fact.name}]: {fact.value}" for fact in source.identity),
        ))
    return _display_lines(lines)


def _workflow_execution_fact_lines(source: ReportSource) -> list[str]:
    """Group facts for one recorded attempt using the saved numeric job identities."""
    facts = {fact.name: fact.value for fact in source.identity}
    lines = ["GitHub-reported jobs and steps"]
    lines.extend(
        f"{fact.label}: {fact.value}"
        for fact in source.identity
        if not fact.name.startswith("job_")
    )
    lines.append(
        "These are GitHub's displayed labels and outcomes. "
        "Step outcomes absent from the retained rows are unknown. "
        "Dependency command execution and package state require separate evidence."
    )
    job_names = [
        (match[1], fact.value)
        for fact in source.identity
        if (match := re.fullmatch(r"job_([0-9]+)_name", fact.name))
    ]
    if not job_names:
        lines.append(
            "No job rows in this captured attempt."
            if facts.get("captured_job_count") == "0"
            else "No job rows were saved in this report."
        )
    elif "reported_steps_omission" not in facts and not any(
        f"job_{job_id}_reported_steps" in facts for job_id, _ in job_names
    ):
        lines.append("Individual step outcomes were not saved in this report.")
    for job_id, name in job_names:
        key = f"job_{job_id}_"
        status = facts.get(key + "status", "not recorded")
        conclusion = facts.get(key + "conclusion", "not recorded")
        lines.extend(("", f"Job {job_id} {name!r}",
                      f"  Status {status!r} | conclusion {conclusion!r}"))
        if key + "head_sha" in facts:
            lines.append(f"  Job execution revision: {facts[key + 'head_sha']}")
        if key + "steps" in facts:
            lines.append(f"  Captured step count: {facts[key + 'steps']}")
        if key + "reported_steps" in facts:
            lines.extend(f"  {row}" for row in facts[key + "reported_steps"].split("\n"))
    return lines


def render_report_source(report: InvestigationReport, source_id: str) -> str:
    """Display one retained original source as inert text, without I/O or interpretation."""
    source = _report_source(report, source_id)
    return render_original_source(source, context=(
        f"Report: {report.report_id}", f"Report generated at: {report.generated_at}",
    ))


def render_original_source(source: ReportSource, *, context: tuple[str, ...] = ()) -> str:
    """Display retained original text with the same inert handling in every offline view."""
    if source.retention != "retained_text" or source.content is None:
        raise ReportSourceUnavailable("This source has no retained original text.")
    lines = [
        "UpgradePilot saved source; offline, no live refresh",
        *context,
        f"Source: {source.source_id} | {source.kind} | {source.retention}",
        f"Location: {source.locator or 'not recorded'}",
        f"Observation time: {source.retrieved_at or 'not recorded'}",
        *[f"{fact.label}: {fact.value}" for fact in source.identity],
        f"Method: {source.method}",
        f"Limit: {source.limitation}",
        "Display removes nonprinting controls; saved text and digest remain unchanged.",
        "HTML/Markdown and embedded instructions are literal untrusted source text.",
        "BEGIN LITERAL SOURCE TEXT" + (" (empty)" if source.content == "" else ""),
        # Split only on LF: splitlines would turn other controls into invented lines.
        *source.content.split("\n"),
        "END LITERAL SOURCE TEXT",
    ]
    return _display_lines(lines)


def _display_lines(lines: list[str]) -> str:
    # External source text remains untrusted display data. Strip terminal controls without
    # changing the retained record, so reopening cannot execute terminal escape sequences.
    return "\n".join(
        "".join(c for c in line if c == "\t" or (c.isprintable())) for line in lines
    )
