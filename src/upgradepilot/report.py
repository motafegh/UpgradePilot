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
            f"Recorded generator version: {report.generator_version}; renderer version: 1",
            f"Product version: {report.product_version or 'not recorded'}",
        )
    )
    lines.extend(f"{fact.label}: {fact.value}" for fact in report.identity)
    for assessment in report.assessments:
        lines.extend(("", f"{assessment.topic}: {assessment.state}"))
        lines.extend(f"{fact.label}: {fact.value}" for fact in assessment.facts)
        lines.extend((f"Reason: {assessment.reason}", f"Detail: {assessment.detail}"))
        lines.append(f"Evidence meaning: {assessment.proposition}")
        lines.append(f"Evidence strength: {assessment.strength}")
        lines.append("Sources: " + ", ".join(assessment.source_ids))
        lines.extend(f"Limitation: {limit}" for limit in assessment.limitations)
    lines.extend(("", "Unresolved questions"))
    for unknown in report.unknowns:
        lines.extend(
            (
                f"Question: {unknown.question}",
                f"Why unresolved: {unknown.reason}",
                f"Consequence: {unknown.consequence}",
                "Sources: " + ", ".join(unknown.source_ids),
            )
        )
    lines.extend(("", f"Maintainer action: {report.action.state}"))
    lines.extend(f"Action reason: {reason}" for reason in report.action.reasons)
    lines.extend(
        f"Remaining uncertainty: {value}" for value in report.action.uncertainty
    )
    lines.extend(f"Action limitation: {value}" for value in report.action.limitations)
    lines.extend(f"Claim limit: {value}" for value in report.action.claim_limits)
    lines.extend(("", "Evidence sources"))
    for source in report.sources:
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
    lines.extend(("", "Report limits"))
    lines.extend(report.production_limits + report.preservation_limits)
    # External source text remains untrusted display data. Strip terminal controls without
    # changing the retained record, so reopening cannot execute terminal escape sequences.
    return "\n".join(
        "".join(c for c in line if c == "\t" or (c.isprintable())) for line in lines
    )
