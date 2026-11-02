"""Captured acquisition premises for caller/signature source material.

These immutable records preserve what a source owner observed/selected, not
installed dependencies or permission to execute. ``CallerSignatureSources`` is
the source-family payload; ``source_codec`` owns its fixed representation and
joins to exact text. Acquisition will produce these through the existing
provider boundaries. Retained experimental receipts have a separate origin and
explicit missing-observation gaps, never invented full provenance.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Literal

from .bindings import ImportFact, ReferenceFact
from .correspondence import PythonSourceModule
from .evidence import AnalysisLimits, MeasuredDuration, SourceAnalysisInput
from ..github.tag import GitHubTagCommitEvidence
from ..pypi.provenance import FileProvenanceEvidence, FileProvenanceProblem
from ..pypi.release import PackageReleaseEvidence, ProjectUrlCandidate
from ..workspace.source_access import RetainedSourceCatalog


@dataclass(frozen=True)
class SourceProblem:
    stage: str
    reason: str
    detail: str


@dataclass(frozen=True)
class SourceContextGap:
    path: str | None
    reason: str
    detail: str


@dataclass(frozen=True)
class SourceDependencyDeclaration:
    source_id: str
    location: str
    raw: str
    package: str
    specifier: str
    extras: tuple[str, ...]
    marker: str | None
    group: str


@dataclass(frozen=True)
class SourceImportCandidate:
    imported_module: str
    declaration: SourceDependencyDeclaration
    import_source_id: str
    import_line: int
    basis: str


@dataclass(frozen=True)
class SourceFileReceipt:
    source_id: str
    sha256: str
    utf8_bytes: int


@dataclass(frozen=True)
class TargetSourceReceipt:
    repository: str
    revision: str
    tree_sha: str
    inventory_entries: int
    inventory_truncated: bool
    files: tuple[SourceFileReceipt, ...]
    declarations: tuple[SourceDependencyDeclaration, ...]
    candidates: tuple[SourceImportCandidate, ...]
    excluded_paths: tuple[str, ...]
    omitted_paths: tuple[str, ...]
    gaps: tuple[SourceContextGap, ...]
    examined_bytes: int
    limitations: tuple[str, ...]


@dataclass(frozen=True)
class SourceDependencyMetadata:
    package: str
    version: str
    source_url: str
    requirements: tuple[SourceDependencyDeclaration, ...]
    gaps: tuple[SourceContextGap, ...]


@dataclass(frozen=True)
class SourcePublisherInspection:
    state: str
    detail: str
    repository: str | None
    records: tuple[FileProvenanceEvidence | FileProvenanceProblem, ...]


@dataclass(frozen=True)
class PackageSourceAssociation:
    """ADR0011 declared-source basis, never the stronger upstream authority type."""
    release: PackageReleaseEvidence
    repository: str
    declarations: tuple[ProjectUrlCandidate, ...]
    ignored_links: tuple[ProjectUrlCandidate, ...]
    provenance: SourcePublisherInspection
    basis: str


@dataclass(frozen=True)
class ModuleSourceRequest:
    package: str
    version: str
    module: str
    version_basis: Literal["old_dependency", "proposed_dependency", "constraint_sample", "explicit_version"]
    origin: ImportFact | ReferenceFact | None


@dataclass(frozen=True)
class SourceTagCommit:
    tag: str
    revision: str


@dataclass(frozen=True)
class ModuleSourceReceipt:
    """A question and its observation/refusal; text admission is separately joined.

    Full association/tag observations may be absent in historical summaries.
    Keep the summarized basis/state/tag commits and explicit retention gaps.
    Failed reads may retain earlier association/metadata/tag progress; only a
    module_examined receipt can admit a file to comparison source material.
    """
    request: ModuleSourceRequest
    state: Literal["module_examined", "refused", "unavailable"]
    problem: SourceProblem | None
    repository: str | None
    revision: str | None
    path: str | None
    sha256: str | None
    utf8_bytes: int | None
    association_basis: str | None
    provenance_state: str | None
    tag_commits: tuple[SourceTagCommit, ...]
    metadata: SourceDependencyMetadata | None
    gaps: tuple[SourceContextGap, ...]
    association: PackageSourceAssociation | None
    tags: tuple[GitHubTagCommitEvidence, ...]
    retention_gaps: tuple[str, ...]


@dataclass(frozen=True)
class SourceSampleSelection:
    candidate: SourceImportCandidate
    depth: int
    version: str
    selection: str
    repository: str
    revision: str
    path: str
    sha256: str


@dataclass(frozen=True)
class SourceMaterialOmission:
    repository: str
    revision: str
    path: str
    role: str
    reason: str


@dataclass(frozen=True)
class SourceAcquisitionWork:
    release_identities: tuple[tuple[str, str], ...]
    module_attempts: int
    source_bytes: int


@dataclass(frozen=True)
class SourceAcquisitionLimits:
    github_requests: int
    provider_requests: int
    response_bytes: int
    aggregate_bytes: int
    elapsed_seconds: MeasuredDuration
    source_request_reserve: int
    target_file_attempts: int
    adapter_candidate_attempts: int


@dataclass(frozen=True)
class SourceRequestEvent:
    stage: str
    host: str
    path: str
    github_requests: int
    provider_requests: int
    decoded_body_bytes: int
    status: int | None
    state: str
    reason: str | None


@dataclass(frozen=True)
class SourceAcquisitionStop:
    stage: str
    reason: str


@dataclass(frozen=True)
class SourceRetryDecision:
    after_provider_request: int
    retry_provider_request: int | None
    reason: str
    state: str


@dataclass(frozen=True)
class SourceTransportReceipt:
    limits: SourceAcquisitionLimits
    auth: Literal["anonymous", "token-env"]
    github_requests: int
    provider_requests: int
    decoded_body_bytes: int
    elapsed: MeasuredDuration
    deadline_kind: str
    stops: tuple[SourceAcquisitionStop, ...]
    requests: tuple[SourceRequestEvent, ...]
    retry_policy: Literal["none", "pypi-get-timeout-once/1"]
    retry_decisions: tuple[SourceRetryDecision, ...]


@dataclass(frozen=True)
class SourceMethodFile:
    path: str
    sha256: str


@dataclass(frozen=True)
class SourceAcquisitionReceipt:
    origin: Literal["native_observation", "retained_experiment", "controlled_observation"]
    state: Literal["complete", "partial", "failed"]
    observed_at: datetime | None
    target: TargetSourceReceipt | None
    module_requests: tuple[ModuleSourceReceipt, ...]
    samples: tuple[SourceSampleSelection, ...]
    problems: tuple[SourceProblem, ...]
    omitted_candidates: tuple[SourceImportCandidate, ...]
    deferred_candidates: tuple[SourceImportCandidate, ...]
    unexamined_modules: tuple[str, ...]
    material_omissions: tuple[SourceMaterialOmission, ...]
    adapter_limitations: tuple[str, ...]
    source_work: SourceAcquisitionWork | None
    transport: SourceTransportReceipt | None
    method_files: tuple[SourceMethodFile, ...]
    retention_gaps: tuple[str, ...]


@dataclass(frozen=True)
class CallerSignatureSources:
    catalog: RetainedSourceCatalog | None
    modules: tuple[PythonSourceModule, ...]
    analysis_limits: AnalysisLimits
    acquisition: SourceAcquisitionReceipt

    def analysis_input(self) -> SourceAnalysisInput | None:
        """No analysis is ready before any classified Python text is retained."""
        if self.catalog is None or not self.modules:
            return None
        return SourceAnalysisInput(self.catalog, self.modules, self.analysis_limits)
