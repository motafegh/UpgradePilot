"""Shared, framework-independent investigation report and deterministic human rendering.

``report_projection.project_investigation_report`` supplies this record from typed domain
results. ``report_file`` encodes/validates it; reopening reconstructs only these records.
No rendering or decoding operation acquires evidence or grants action permission.
Source content can be richer than the displayed summary, enabling non-rendering consumers.
"""

from __future__ import annotations

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
            f"Recorded generator version: {report.generator_version}; renderer version: 4",
            f"Product version: {report.product_version or 'not recorded'}",
        )
    )
    lines.extend(f"{fact.label}: {fact.value}" for fact in report.identity)
    lines.extend(_first_view_lines(report))
    lines.extend(_assessment_lines(report.assessments, report.unknowns))
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
    lines.append("Applies under the recorded source and dispatch assumptions. See witness conditions below.")
    open_questions = [unknown for unknown in report.unknowns
                      if unknown.assessment_id == "caller-signature-analysis"]
    lines.extend(f"Open: {unknown.question}" for unknown in open_questions)
    for item in report.assessments:
        if item.assessment_id in {"ci", "runtime"} and item.status == "not_evaluated":
            lines.append(f"{item.topic}: {item.state}")
    lines.append(_evidence_refs(*(witness for rows in witnesses.values() for witness in rows), *open_questions))
    return lines


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
    lines.extend(_source_lines(report.sources))
    lines.extend(("", "CI view limits", *report.limits))
    return _display_lines(lines)


def _assessment_lines(
    assessments: tuple[ReportAssessment, ...], unknowns: tuple[ReportUnknown, ...]
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


def _source_lines(sources: tuple[ReportSource, ...]) -> list[str]:
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
                if not fact.name.startswith(("file_", "job_"))
            )
        lines.append(
            "  Method: recorded domain assessment"
            if source.kind == "producer_assessment"
            else f"  Method: {source.method}"
        )
        lines.append(f"  Acquisition time: {source.retrieved_at or 'not recorded'}")
        lines.append(f"  Preservation limit: {source.limitation}")
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
    # Other selected-fact sources can contain bulk records such as an entire CI job inventory.
    if source.kind not in {"artifact_capabilities", "package_metadata"}:
        raise ReportSourceUnavailable(f"Selected-fact inspection is unavailable for {source.kind}.")
    if not source.identity:
        raise ReportSourceUnavailable("This source has no saved fact values.")

    return _display_lines([
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
        "Selected facts",
        *(f"{fact.label} [{fact.name}]: {fact.value}" for fact in source.identity),
    ])


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
