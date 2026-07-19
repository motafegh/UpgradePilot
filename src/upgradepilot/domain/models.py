from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class EvidenceState(StrEnum):
    OBSERVED = "observed"
    INFERRED = "inferred"
    MISSING = "missing"
    INACCESSIBLE = "inaccessible"
    STALE = "stale"
    CONFLICTING = "conflicting"
    INVALID = "invalid"
    ACCEPTED = "accepted"
    REJECTED = "rejected"


class DecisionEffect(StrEnum):
    NEUTRAL = "neutral"
    TARGETED_CHECK = "targeted_check"
    BLOCK = "block"
    DEFER = "defer"


class ActionClass(StrEnum):
    MERGE_AFTER_NORMAL_REVIEW = "merge_after_normal_review"
    RUN_TARGETED_CHECKS = "run_targeted_checks"
    INVESTIGATE_OR_BLOCK = "investigate_or_block"
    DEFER = "defer"
    ABSTAIN = "abstain"


@dataclass(frozen=True, slots=True)
class SourceReference:
    locator: str
    retrieved_at: str
    revision: str | None = None

    def __post_init__(self) -> None:
        if not self.locator.strip():
            raise ValueError("source locator must not be empty")
        if not self.retrieved_at.strip():
            raise ValueError("source retrieval timestamp must not be empty")

        timestamp = self.retrieved_at.replace("Z", "+00:00")
        try:
            parsed = datetime.fromisoformat(timestamp)
        except ValueError as exc:
            raise ValueError("source retrieval timestamp must be ISO 8601") from exc
        if parsed.tzinfo is None:
            raise ValueError("source retrieval timestamp must include a timezone")


@dataclass(frozen=True, slots=True)
class CaseIdentity:
    repository_owner: str
    repository_name: str
    pull_request_number: int
    pull_request_url: str
    base_revision: str
    head_revision: str
    dependency_name: str
    old_version: str
    new_version: str
    changed_files: tuple[str, ...]

    def __post_init__(self) -> None:
        text_fields = {
            "repository_owner": self.repository_owner,
            "repository_name": self.repository_name,
            "pull_request_url": self.pull_request_url,
            "base_revision": self.base_revision,
            "head_revision": self.head_revision,
            "dependency_name": self.dependency_name,
            "old_version": self.old_version,
            "new_version": self.new_version,
        }
        for name, value in text_fields.items():
            if not value.strip():
                raise ValueError(f"{name} must not be empty")
        if self.pull_request_number < 1:
            raise ValueError("pull_request_number must be positive")
        if not self.changed_files or any(not item.strip() for item in self.changed_files):
            raise ValueError("changed_files must contain at least one non-empty path")
        if len(set(self.changed_files)) != len(self.changed_files):
            raise ValueError("changed_files must not contain duplicates")


@dataclass(frozen=True, slots=True)
class EvidenceItem:
    evidence_id: str
    claim: str
    state: EvidenceState
    decision_effect: DecisionEffect
    material: bool
    interpretation: str
    source: SourceReference | None = None
    suggested_check: str | None = None

    def __post_init__(self) -> None:
        if not self.evidence_id.strip():
            raise ValueError("evidence_id must not be empty")
        if not self.claim.strip():
            raise ValueError("evidence claim must not be empty")
        if not self.interpretation.strip():
            raise ValueError("evidence interpretation must not be empty")

        source_required = {
            EvidenceState.OBSERVED,
            EvidenceState.INFERRED,
            EvidenceState.ACCEPTED,
            EvidenceState.REJECTED,
        }
        if self.state in source_required and self.source is None:
            raise ValueError(f"evidence state {self.state.value!r} requires a source")
        if self.decision_effect is DecisionEffect.TARGETED_CHECK:
            if self.suggested_check is None or not self.suggested_check.strip():
                raise ValueError("targeted_check evidence requires suggested_check")


@dataclass(frozen=True, slots=True)
class AnalysisInput:
    schema_version: str
    case: CaseIdentity
    evidence: tuple[EvidenceItem, ...]
    limitations: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.schema_version != "1.0":
            raise ValueError(f"unsupported schema_version: {self.schema_version!r}")
        evidence_ids = [item.evidence_id for item in self.evidence]
        if len(set(evidence_ids)) != len(evidence_ids):
            raise ValueError("evidence IDs must be unique")
        if any(not limitation.strip() for limitation in self.limitations):
            raise ValueError("limitations must not contain empty values")


@dataclass(frozen=True, slots=True)
class PolicyDecision:
    action: ActionClass
    reason: str
    triggering_evidence_ids: tuple[str, ...]
    targeted_checks: tuple[str, ...]
    uncertainties: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class DecisionReport:
    schema_version: str
    policy_version: str
    generated_at: str
    case: CaseIdentity
    evidence: tuple[EvidenceItem, ...]
    action: ActionClass
    reason: str
    triggering_evidence_ids: tuple[str, ...]
    targeted_checks: tuple[str, ...]
    uncertainties: tuple[str, ...]
    limitations: tuple[str, ...]
    claim_boundary: str
