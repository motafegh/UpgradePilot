"""Version-1 report JSON encoding, strict offline decoding and non-replacing publication.

The public payload is explicitly named here, independent of Python class layout/imports.
SHA-256 checks accidental corruption only. Parsing does not execute code or fetch locators.
A fsynced invocation-owned sibling is linked into place: the final path becomes visible
only with complete contents, and a concurrent existing destination is never overwritten.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any, get_args

# State vocabularies remain owned by domain modules. Decoding admits these values without
# constructing any domain evidence objects or recomputing their meaning.
from .ci.dependency_exercise import DependencyCICoverageState
from .ci.dependency_state import RequirementStateProblemState
from .github.changelog import ChangelogPathDiscoveryProblemState
from .github.tag import GitHubTagCommitProblemState
from .impact.applicability import CandidateApplicabilityState
from .pypi.release import PackageReleaseIndexProblemState, PackageReleaseProblemState
from .report import (
    InvestigationReport,
    ReportAction,
    ReportAssessment,
    ReportFact,
    ReportFinding,
    ReportSource,
    ReportUnknown,
)
from .target.artifact_environment import TargetArtifactEnvironmentProblemState
from .target.python import TargetPythonProblemState
from .target.relevance import TargetPythonRelevanceState
from .upstream.claim import UpstreamSupportDropClaimProblemState
from .upstream.interval import (
    UpstreamAuthoritySourceProblemState,
    UpstreamIntervalAuthorityProblemState,
)
from .upstream.interval_evidence import CrossedReleaseIndexSelectionProblemState
from .upstream.repository import UpstreamRepositoryProblemState

SCHEMA = "upgradepilot.investigation-report"
SCHEMA_VERSION = 1
# One bounded report/export, not an unrestricted raw-capture archive. Larger retained
# authoritative content must fail visibly rather than silently truncate supporting text.
MAX_REPORT_BYTES = 16 * 1024 * 1024
MAX_JSON_DEPTH = 24


class ReportValidationError(ValueError):
    """The saved file cannot establish a supported, internally consistent report."""


class ReportSaveError(OSError):
    """The requested complete report could not be published without replacement."""


def encode_report(report: InvestigationReport) -> bytes:
    payload = {
        "schema": SCHEMA,
        "schema_version": SCHEMA_VERSION,
        "report": _encode_report_record(report),
    }
    try:
        envelope = {
            **payload,
            "integrity": {"method": "sha256", "digest": _digest(payload)},
        }
        data = (
            json.dumps(envelope, ensure_ascii=False, allow_nan=False, indent=2).encode(
                "utf-8"
            )
            + b"\n"
        )
    except (ValueError, UnicodeError, TypeError) as exc:
        raise ReportValidationError(f"Report cannot be encoded: {exc}") from exc
    # Apply the public boundary once to the complete representation, including references.
    decode_report(data)
    return data


def decode_report(data: bytes) -> InvestigationReport:
    if len(data) > MAX_REPORT_BYTES:
        raise ReportValidationError(f"Report exceeds {MAX_REPORT_BYTES} bytes.")
    try:
        text = data.decode("utf-8")
        _check_depth(text)
        envelope = json.loads(
            text, object_pairs_hook=_unique_object, parse_constant=_reject_constant
        )
        _object(envelope, {"schema", "schema_version", "report", "integrity"})
        if (
            envelope["schema"] != SCHEMA
            or type(envelope["schema_version"]) is not int
            or envelope["schema_version"] != SCHEMA_VERSION
        ):
            raise ReportValidationError("Unsupported report schema/version.")
        integrity = _object(envelope["integrity"], {"method", "digest"})
        if (
            integrity["method"] != "sha256"
            or not isinstance(integrity["digest"], str)
            or not re.fullmatch(r"[0-9a-f]{64}", integrity["digest"])
        ):
            raise ReportValidationError("Invalid report integrity declaration.")
        payload = {key: envelope[key] for key in ("schema", "schema_version", "report")}
        if integrity["digest"] != _digest(payload):
            raise ReportValidationError(
                "Report digest mismatch; recorded contents may be damaged."
            )
        report = _decode_report_record(envelope["report"])
        _validate_references(report)
        return report
    except ReportValidationError:
        raise
    except (
        UnicodeError,
        ValueError,
        TypeError,
        KeyError,
        RecursionError,
        OverflowError,
    ) as exc:
        raise ReportValidationError(f"Invalid saved report: {exc}") from exc


def read_report(path: str | Path) -> InvestigationReport:
    try:
        descriptor = os.open(path, os.O_RDONLY | os.O_NONBLOCK)
        with os.fdopen(descriptor, "rb") as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise ReportValidationError("Saved report must be a regular file.")
            data = stream.read(MAX_REPORT_BYTES + 1)
        return decode_report(data)
    except OSError as exc:
        raise ReportValidationError(f"Could not read saved report: {exc}") from exc


def save_report(report: InvestigationReport, path: str | Path) -> None:
    """Publish a complete validated file; never replace a file, directory or symlink."""
    destination = Path(path)
    temporary: str | None = None
    try:
        data = encode_report(report)
        with tempfile.NamedTemporaryFile(
            dir=destination.parent, prefix=".upgradepilot-report-", delete=False
        ) as stream:
            temporary = stream.name
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        # link() is an atomic create-if-absent on this same-filesystem sibling. Unlike
        # replace()/rename(), it protects a destination created after our preparation.
        os.link(temporary, destination)
    except (OSError, ReportValidationError) as exc:
        raise ReportSaveError(
            f"Could not save report without replacement: {exc}"
        ) from exc
    finally:
        if temporary is not None:
            try:
                os.unlink(temporary)
            except OSError as exc:
                raise ReportSaveError(
                    f"Report temporary-file cleanup failed: {exc}"
                ) from exc


def _digest(payload: dict[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ReportValidationError(f"Duplicate object key: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ReportValidationError(f"Non-finite JSON value: {value}")


def _check_depth(text: str) -> None:
    depth = 0
    quoted = escaped = False
    for char in text:
        if quoted:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quoted = False
        elif char == '"':
            quoted = True
        elif char in "[{":
            depth += 1
            if depth > MAX_JSON_DEPTH:
                raise ReportValidationError(
                    f"Report JSON exceeds depth {MAX_JSON_DEPTH}."
                )
        elif char in "]}":
            depth -= 1


def _object(value: Any, keys: set[str]) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != keys:
        raise ReportValidationError(
            f"Expected object with exactly these fields: {', '.join(sorted(keys))}"
        )
    return value


def _text(value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ReportValidationError("Expected non-empty text.")
    return value


def _optional_text(value: Any) -> str | None:
    return None if value is None else _text(value)


def _enum(value: Any, allowed: set[str]) -> str:
    value = _text(value)
    if value not in allowed:
        raise ReportValidationError(f"Unsupported state: {value}")
    return value


def _list(value: Any) -> list[Any]:
    if not isinstance(value, list):
        raise ReportValidationError("Expected a JSON list.")
    return value


def _texts(value: Any) -> tuple[str, ...]:
    return tuple(_text(item) for item in _list(value))


def _time(value: Any) -> str:
    value = _text(value)
    parsed = datetime.fromisoformat(value)
    if parsed.utcoffset() is None:
        raise ReportValidationError("Timestamp must have a timezone.")
    return value


def _encode_facts(facts: tuple[ReportFact, ...]) -> list[dict[str, str]]:
    return [{"name": f.name, "label": f.label, "value": f.value} for f in facts]


def _decode_facts(value: Any) -> tuple[ReportFact, ...]:
    facts = []
    for f in _list(value):
        _object(f, {"name", "label", "value"})
        # Empty recorded text (e.g. an absent static witness path) is not an evidence-backed
        # negative: its owning assessment supplies the exact state/meaning.
        if not isinstance(f["value"], str):
            raise ReportValidationError("Fact value must be text.")
        facts.append(ReportFact(_text(f["name"]), _text(f["label"]), f["value"]))
    if len({f.name for f in facts}) != len(facts):
        raise ReportValidationError("Duplicate named fact.")
    return tuple(facts)


def _encode_report_record(r: InvestigationReport) -> dict[str, Any]:
    return {
        "report_id": r.report_id,
        "generated_at": r.generated_at,
        "generator_version": r.generator_version,
        "product_version": r.product_version,
        "auth_mode": r.auth_mode,
        "production_limits": list(r.production_limits),
        "identity": _encode_facts(r.identity),
        "assessments": [
            {
                "assessment_id": a.assessment_id,
                "topic": a.topic,
                "owner": a.owner,
                "state": a.state,
                "status": a.status,
                "reason": a.reason,
                "detail": a.detail,
                "proposition": a.proposition,
                "strength": a.strength,
                "source_ids": list(a.source_ids),
                "facts": _encode_facts(a.facts),
                "limitations": list(a.limitations),
            }
            for a in r.assessments
        ],
        "findings": [
            {
                "assessment_id": f.assessment_id,
                "statement": f.statement,
                "strength": f.strength,
                "source_ids": list(f.source_ids),
            }
            for f in r.findings
        ],
        "unknowns": [
            {
                "assessment_id": u.assessment_id,
                "question": u.question,
                "reason": u.reason,
                "source_ids": list(u.source_ids),
                "consequence": u.consequence,
            }
            for u in r.unknowns
        ],
        "action": {
            "state": r.action.state,
            "reasons": list(r.action.reasons),
            "uncertainty": list(r.action.uncertainty),
            "limitations": list(r.action.limitations),
            "claim_limits": list(r.action.claim_limits),
        },
        "sources": [
            {
                "source_id": s.source_id,
                "kind": s.kind,
                "locator": s.locator,
                "identity": _encode_facts(s.identity),
                "method": s.method,
                "retrieved_at": s.retrieved_at,
                "retention": s.retention,
                "content": s.content,
                "limitation": s.limitation,
            }
            for s in r.sources
        ],
        "preservation_limits": list(r.preservation_limits),
    }


def _decode_report_record(value: Any) -> InvestigationReport:
    r = _object(
        value,
        {
            "report_id",
            "generated_at",
            "generator_version",
            "product_version",
            "auth_mode",
            "production_limits",
            "identity",
            "assessments",
            "findings",
            "unknowns",
            "action",
            "sources",
            "preservation_limits",
        },
    )
    assessments = []
    for a in _list(r["assessments"]):
        _object(
            a,
            {
                "assessment_id",
                "topic",
                "owner",
                "state",
                "status",
                "reason",
                "detail",
                "proposition",
                "strength",
                "source_ids",
                "facts",
                "limitations",
            },
        )
        strength = _enum(
            a["strength"],
            {"recorded_fact", "grounded_interpretation", "candidate", "unresolved"},
        )
        status = _enum(a["status"], {"available", "problem", "not_evaluated"})
        if (status != "available") != (strength == "unresolved"):
            raise ReportValidationError(
                "Assessment status/strength combination is invalid."
            )
        _validate_assessment_state(a["assessment_id"], a["state"], status)
        assessments.append(
            ReportAssessment(
                _text(a["assessment_id"]),
                _text(a["topic"]),
                _text(a["owner"]),
                _text(a["state"]),
                status,
                _text(a["reason"]),
                _text(a["detail"]),
                _text(a["proposition"]),
                strength,
                _texts(a["source_ids"]),
                _decode_facts(a["facts"]),
                _texts(a["limitations"]),
            )
        )
    findings = []
    for f in _list(r["findings"]):
        _object(f, {"assessment_id", "statement", "strength", "source_ids"})
        findings.append(
            ReportFinding(
                _text(f["assessment_id"]),
                _text(f["statement"]),
                _enum(
                    f["strength"],
                    {"recorded_fact", "grounded_interpretation", "candidate"},
                ),
                _texts(f["source_ids"]),
            )
        )
    unknowns = []
    for u in _list(r["unknowns"]):
        _object(u, {"assessment_id", "question", "reason", "source_ids", "consequence"})
        unknowns.append(
            ReportUnknown(
                _text(u["assessment_id"]),
                _text(u["question"]),
                _text(u["reason"]),
                _texts(u["source_ids"]),
                _text(u["consequence"]),
            )
        )
    sources = []
    for s in _list(r["sources"]):
        _object(
            s,
            {
                "source_id",
                "kind",
                "locator",
                "identity",
                "method",
                "retrieved_at",
                "retention",
                "content",
                "limitation",
            },
        )
        retention = _enum(
            s["retention"],
            {"retained_text", "reference_only", "producer_result", "selected_facts"},
        )
        content = s["content"]
        if content is not None and not isinstance(content, str):
            raise ReportValidationError("Retained content must be text or null.")
        if (retention in {"retained_text", "producer_result"}) != (content is not None):
            raise ReportValidationError(
                "Source retention/content combination is invalid."
            )
        sources.append(
            ReportSource(
                _text(s["source_id"]),
                _enum(
                    s["kind"],
                    {
                        "producer_assessment",
                        "pull_request",
                        "dependency_source",
                        "workflow_execution",
                        "workflow_source",
                        "package_metadata",
                        "tagged_changelog",
                        "github_release_body",
                        "grounded_quote",
                        "target_source",
                        "artifact_capabilities",
                        "publisher_provenance",
                    },
                ),
                _optional_text(s["locator"]),
                _decode_facts(s["identity"]),
                _text(s["method"]),
                _time(s["retrieved_at"]) if s["retrieved_at"] is not None else None,
                retention,
                content,
                _text(s["limitation"]),
            )
        )
    a = _object(
        r["action"], {"state", "reasons", "uncertainty", "limitations", "claim_limits"}
    )
    action = ReportAction(
        _enum(a["state"], {"abstain", "not_evaluated"}),
        _texts(a["reasons"]),
        _texts(a["uncertainty"]),
        _texts(a["limitations"]),
        _texts(a["claim_limits"]),
    )
    if not action.reasons or not action.limitations or not action.claim_limits:
        raise ReportValidationError(
            "Action must preserve reasons, limitations and claim limits."
        )
    report = InvestigationReport(
        _text(r["report_id"]),
        _time(r["generated_at"]),
        _text(r["generator_version"]),
        _optional_text(r["product_version"]),
        _enum(r["auth_mode"], {"anonymous", "token-env"}),
        _texts(r["production_limits"]),
        _decode_facts(r["identity"]),
        tuple(assessments),
        tuple(findings),
        tuple(unknowns),
        action,
        tuple(sources),
        _texts(r["preservation_limits"]),
    )
    if not report.production_limits or not report.preservation_limits:
        raise ReportValidationError(
            "Report must declare production/preservation limits."
        )
    identity = {f.name: f.value for f in report.identity}
    if not {"repository", "pull_number", "base_sha", "head_sha"} <= identity.keys():
        raise ReportValidationError("Report identity is incomplete.")
    from .github.identity import (
        validate_commit_sha,
        validate_pull_number,
        validate_repository,
    )

    validate_repository(identity["repository"])
    validate_pull_number(int(identity["pull_number"]))
    validate_commit_sha(identity["base_sha"])
    validate_commit_sha(identity["head_sha"])
    return report


def _validate_references(report: InvestigationReport) -> None:
    source_ids = {s.source_id for s in report.sources}
    assessments = {a.assessment_id: a for a in report.assessments}
    if len(source_ids) != len(report.sources) or len(assessments) != len(
        report.assessments
    ):
        raise ReportValidationError("Duplicate source/assessment identifiers.")
    if (
        not {
            "dependency",
            "ci",
            "runtime",
            "package",
            "old-package",
            "upstream-repository",
            "upstream-interval",
            "support-drop",
            "artifact-candidate",
            "artifact-impact",
            "target-python",
            "python-relevance",
        }
        <= assessments.keys()
    ):
        raise ReportValidationError("Required assessment topics are missing.")
    for record in (*report.assessments, *report.findings, *report.unknowns):
        if not record.source_ids or not set(record.source_ids) <= source_ids:
            raise ReportValidationError("Empty or dangling source reference.")
    for finding in report.findings:
        assessment = assessments.get(finding.assessment_id)
        if (
            assessment is None
            or assessment.status != "available"
            or finding.strength != assessment.strength
            or finding.source_ids != assessment.source_ids
            or finding.statement != assessment.detail
        ):
            raise ReportValidationError(
                "Finding does not preserve its assessment strength/sources."
            )
    if len({f.assessment_id for f in report.findings}) != len(report.findings) or {
        f.assessment_id for f in report.findings
    } != {a.assessment_id for a in report.assessments if a.status == "available"}:
        raise ReportValidationError("Required findings are missing or duplicated.")
    dependency = assessments["dependency"]
    if dependency.state == "supported" and not {
        "package",
        "normalized_package",
        "old_version",
        "proposed_version",
    } <= {f.name for f in dependency.facts}:
        raise ReportValidationError(
            "Supported dependency transition is missing exact identity/version fields."
        )
    for unknown in report.unknowns:
        if unknown.assessment_id not in assessments or not set(
            unknown.source_ids
        ) <= set(assessments[unknown.assessment_id].source_ids):
            raise ReportValidationError(
                "Unknown does not preserve its assessment sources."
            )


def _validate_assessment_state(assessment_id: Any, state: Any, status: str) -> None:
    """Reject unsupported owner states and false not-evaluated combinations in version 1."""
    assessment_id, state = _text(assessment_id), _text(state)
    empty_states = {"not evaluated", "not activated", "not established"}
    if (status == "not_evaluated") != (state in empty_states):
        raise ReportValidationError("Assessment state/status combination is invalid.")
    vocabularies = {
        "dependency": {"supported", "unsupported"},
        "ci": set(get_args(DependencyCICoverageState.__value__)),
        "runtime": {"evaluated", "no_admitted_candidate"},
        "package": {"available", *get_args(PackageReleaseProblemState.__value__)},
        "old-package": {"available", *get_args(PackageReleaseProblemState.__value__)},
        "upstream-repository": {
            "available",
            *get_args(UpstreamRepositoryProblemState.__value__),
        },
        "upstream-interval": {
            "available",
            *get_args(UpstreamIntervalAuthorityProblemState.__value__),
        },
        "support-drop": {
            "grounded",
            *get_args(UpstreamSupportDropClaimProblemState.__value__),
        },
        "artifact-candidate": {"established", "not observed", "evidence problem"},
        "artifact-impact": set(get_args(CandidateApplicabilityState.__value__)),
        "target-python": {"available", *get_args(TargetPythonProblemState.__value__)},
        "python-relevance": set(get_args(TargetPythonRelevanceState.__value__)),
        "python-impact": set(get_args(CandidateApplicabilityState.__value__)),
        "release-index": set(get_args(PackageReleaseIndexProblemState.__value__)),
        "crossed-release": set(
            get_args(CrossedReleaseIndexSelectionProblemState.__value__)
        ),
        "tag": set(get_args(GitHubTagCommitProblemState.__value__)),
        "changelog-path": set(get_args(ChangelogPathDiscoveryProblemState.__value__)),
        "tagged-changelog": set(
            get_args(UpstreamAuthoritySourceProblemState.__value__)
        ),
    }
    if assessment_id.startswith("ci-workflow-"):
        allowed = vocabularies["ci"]
    elif assessment_id.startswith("runtime-command-"):
        allowed = {
            "satisfied_at_command_completion",
            *get_args(RequirementStateProblemState.__value__),
        }
    elif assessment_id.startswith("artifact-environment-"):
        allowed = {
            "available",
            *get_args(TargetArtifactEnvironmentProblemState.__value__),
        }
    elif assessment_id == "artifact-environments":
        allowed = {state} if state.isdecimal() and int(state) > 0 else set()
    else:
        allowed = vocabularies.get(assessment_id)
        if allowed is None:
            raise ReportValidationError("Unsupported assessment topic.")
    if state not in allowed | empty_states:
        raise ReportValidationError(f"Unsupported state for {assessment_id}: {state}")
