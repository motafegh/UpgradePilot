"""Exact declared-release/module acquisition and conditional adapter exploration.

Start at AdapterSourceExplorer with the invocation's explicit shared session.
source_run() caches exact release and module observations, including failures;
explore() spends that same run on labelled constraint samples rooted in positive
static origins. Target context is supplied by target.source_context. Both tag
spellings and exact commit inventory precede complete module reads.

ADR0011 declared-source association permits source examination only. It never
constructs stronger UpstreamRepositoryEvidence, proves shipped artifact identity,
resolves target environments or executes/imports acquired code. Native source
families reuse the typed premises below; application composition owns publication.
"""
from __future__ import annotations

from collections import deque
from hashlib import sha256
from dataclasses import dataclass, replace
from functools import partial
from typing import Literal
from urllib.parse import quote, urlsplit
from packaging.requirements import InvalidRequirement, Requirement
from packaging.specifiers import SpecifierSet
from packaging.version import InvalidVersion, Version

from ..github.api import GitHubAcquisitionError, GitHubResponseError
from ..github.identity import validate_repository
from ..github.repository import (GitHubRepositoryClient, RepositoryTextFile,
    GitHubRepositoryInventoryClient, RepositoryInventory, RepositoryInventoryProblem)
from ..github.tag import GitHubTagCommitClient, GitHubTagCommitEvidence, GitHubTagRepositoryRedirect
from ..package_identity import normalize_package_name
from ..pypi.api import PyPIJsonApiClient, PyPIRequestError, PyPIResponseError
from ..pypi.provenance import FileProvenanceProblem, PyPIProvenanceClient
from ..pypi.release import (PackageReleaseEvidence, PackageReleaseIndexEvidence,
    ProjectUrlCandidate, PyPIReleaseClient, PyPIReleaseIndexClient)
from ..upstream.repository import normalize_project_url_label
from ..target.source_context import TargetSourceContext, extract_python_facts
from .bindings import ImportFact, ReferenceFact
from .acquisition import AcquisitionSession
from .source_evidence import (
    AcquisitionProblem, SourceContextGap as ContextGap,
    SourceDependencyDeclaration as DependencyDeclaration,
    SourceImportCandidate as ImportDependencyCandidate,
    SourceDependencyMetadata as PackageDependencyMetadata,
    SourcePublisherInspection as PublisherProvenanceInspection,
    PackageSourceAssociation as DeclaredSourceAssociation,
    SourceAcquisitionWork as PythonSourceAcquisitionWork,
    ModuleSourceRequest, ModuleSourceReceipt, SourceProblem, SourceRepositoryMove, SourceTagCommit,
)

class PublisherProvenanceInspector:
    """Keep missing, adverse and unsupported publisher evidence distinguishable.

    The product resolver also gates on its own project-link grammar. Its combined
    result cannot represent this publisher-only proposition. Do not use homepage
    acceptance/failure to infer a publisher conflict, or create product authority.
    """

    def __init__(self, *, client=None):
        self.client = client or PyPIProvenanceClient()

    def resolve(self, release: PackageReleaseEvidence) -> PublisherProvenanceInspection:
        records = []
        repositories = set()
        kinds = set()
        for distribution in release.distribution_files:
            result = self.client.get_file_provenance(release, distribution)
            records.append(result)
            if isinstance(result, FileProvenanceProblem):
                if result.state == "provenance_unavailable":
                    continue
                state = (
                    "unsupported_source"
                    if result.state == "unsupported_provenance"
                    else result.state
                )
                return PublisherProvenanceInspection(
                    state, result.detail, records=tuple(records)
                )
            for publisher in result.publishers:
                kinds.add(publisher.kind.casefold())
                if publisher.kind.casefold() == "github":
                    try:
                        repository = validate_repository(publisher.repository)
                    except (TypeError, ValueError):
                        return PublisherProvenanceInspection(
                            "malformed_response",
                            "Malformed GitHub publisher identity.",
                            records=tuple(records),
                        )
                    repositories.add(repository.casefold())
        if not any(not isinstance(r, FileProvenanceProblem) for r in records):
            return PublisherProvenanceInspection(
                "source_unavailable",
                "No usable registry publisher records.",
                records=tuple(records),
            )
        if kinds != {"github"}:
            return PublisherProvenanceInspection(
                "ambiguous_source" if "github" in kinds else "unsupported_source",
                "Mixed or unsupported publisher kinds.",
                records=tuple(records),
            )
        if len(repositories) != 1:
            return PublisherProvenanceInspection(
                "ambiguous_source",
                "More than one publisher repository.",
                records=tuple(records),
            )
        return PublisherProvenanceInspection(
            "available",
            "Registry reports one GitHub publisher repository.",
            next(iter(repositories)),
            tuple(records),
        )

def associate_declared_source(
    release: PackageReleaseEvidence, provenance: PublisherProvenanceInspection
) -> DeclaredSourceAssociation | AcquisitionProblem:
    """Keep provenance outcomes visible; only absence allows weaker examination.

    A supported stronger association is retained as context, not downgraded or
    cast into stronger upstream authority. Homepage-only links are ignored.
    """
    if provenance.state not in {"available", "source_unavailable"}:
        return AcquisitionProblem(
            "association", provenance.state, provenance.detail, provenance
        )
    declarations = tuple(
        c
        for c in release.project_urls
        if normalize_project_url_label(c.label)
        in {"source", "sourcecode", "repository", "github"}
    )
    ignored = tuple(c for c in release.project_urls if c not in declarations)
    if not declarations:
        return AcquisitionProblem(
            "association",
            "no_source_declaration",
            "No explicit source/repository declaration.",
            provenance,
        )
    identities = []
    for candidate in declarations:
        try:
            url = urlsplit(candidate.url)
            if (
                url.scheme != "https"
                or url.hostname != "github.com"
                or url.port is not None
                or url.username is not None
                or url.password is not None
                or url.query
                or url.fragment
            ):
                raise ValueError("Noncanonical public GitHub source URL.")
            parts = url.path.strip("/").split("/")
            if len(parts) != 2:
                raise ValueError("Expected one repository root.")
            identities.append(validate_repository("/".join(parts).removesuffix(".git")))
        except ValueError as exc:
            return AcquisitionProblem(
                "association",
                "unsupported_declaration",
                str(exc),
                (declarations, provenance),
            )
    if len({i.casefold() for i in identities}) != 1:
        return AcquisitionProblem(
            "association",
            "conflicting_declarations",
            "Multiple declared repository identities.",
            (declarations, provenance),
        )
    repository = identities[0]
    if (
        provenance.state == "available"
        and provenance.repository.casefold() != repository.casefold()
    ):
        return AcquisitionProblem(
            "association",
            "identity_mismatch",
            "Declaration conflicts with publisher association.",
            provenance,
        )
    return DeclaredSourceAssociation(
        release, repository, declarations, ignored, provenance
    )

class PackageDependencyMetadataClient(PyPIJsonApiClient):
    """Read identity-checked Requires-Dist; no installation/marker evaluation."""

    def acquire(
        self, package: str, version: str
    ) -> PackageDependencyMetadata | AcquisitionProblem:
        url = f"https://pypi.org/pypi/{quote(package, safe='')}/{quote(version, safe='')}/json"
        try:
            response = self._get_response(url, resource="adapter-dependencies")
            if response.status_code != 200:
                status = response.status_code
                response.close()
                return AcquisitionProblem(
                    "adapter_metadata",
                    "acquisition_failed",
                    f"PyPI returned HTTP {status}.",
                )
            data = self._read_json_object(response, resource="adapter-dependencies")
            info = data["info"]
            if (
                normalize_package_name(info["name"]) != package
                or info["version"] != version
            ):
                return AcquisitionProblem(
                    "adapter_metadata",
                    "identity_mismatch",
                    "Requires-Dist response does not match exact release.",
                )
            raw = info.get("requires_dist")
            records = []
            gaps = []
            if raw is None:
                gaps.append(
                    ContextGap(
                        url,
                        "requires_dist_unavailable",
                        "Registry did not expose dependency requirements.",
                    )
                )
                raw = []
            if not isinstance(raw, list) or any(
                not isinstance(item, str) for item in raw
            ):
                raise ValueError("Requires-Dist is not a string array.")
            for i, text in enumerate(raw):
                try:
                    requirement = Requirement(text)
                except InvalidRequirement:
                    gaps.append(
                        ContextGap(
                            url,
                            "unsupported_requirement",
                            f"Requires-Dist[{i}] is unparsed.",
                        )
                    )
                    continue
                if requirement.url:
                    gaps.append(
                        ContextGap(
                            url,
                            "direct_url_not_followed",
                            f"Requires-Dist[{i}] uses a direct URL.",
                        )
                    )
                    continue
                records.append(
                    DependencyDeclaration(
                        url,
                        f"info.requires_dist[{i}]",
                        text,
                        normalize_package_name(requirement.name),
                        str(requirement.specifier),
                        tuple(sorted(requirement.extras)),
                        str(requirement.marker) if requirement.marker else None,
                        "registry-requires-dist",
                    )
                )
            return PackageDependencyMetadata(
                package, version, url, tuple(records), tuple(gaps)
            )
        except (
            PyPIRequestError,
            PyPIResponseError,
            KeyError,
            TypeError,
            ValueError,
        ) as exc:
            return AcquisitionProblem("adapter_metadata", "unusable_metadata", str(exc))

@dataclass(frozen=True)
class AdapterModuleSample:
    candidate: ImportDependencyCandidate
    depth: int
    version: str
    selection: str
    association: DeclaredSourceAssociation
    metadata: PackageDependencyMetadata
    tags: tuple[GitHubTagCommitEvidence, ...]
    inventory: RepositoryInventory
    file: RepositoryTextFile
    imports: tuple[ImportFact, ...]
    references: tuple[ReferenceFact, ...]
    gaps: tuple[ContextGap, ...]

@dataclass(frozen=True)
class AdapterExploration:
    samples: tuple[AdapterModuleSample, ...]
    problems: tuple[AcquisitionProblem, ...]
    omitted_candidates: tuple[ImportDependencyCandidate, ...]
    limitations: tuple[str, ...] = (
        "exploration_samples_not_resolved_target_versions",
        "declared_constraints_and_markers_not_evaluated_activation",
        "namespace_mapping_not_established",
        "samples_do_not_exhaust_version_ranges",
        "relative_module_forwarding_not_traversed",
    )
    deferred_candidates: tuple[ImportDependencyCandidate, ...] = ()
    failed_move_receipts: tuple[ModuleSourceReceipt, ...] = ()

@dataclass(frozen=True)
class AdapterDiscoverySeed:
    """Minimal producer facts for a labelled adapter-stage replay, not a report."""

    candidates: tuple[ImportDependencyCandidate, ...]
    references: tuple[ReferenceFact, ...]
    binding_analysis_version: int = 1

@dataclass(frozen=True)
class PythonModuleSourceRequest:
    """Caller-labelled version question plus original import/reference evidence.

    Correspondence owns why a source is relevant. The acquisition owner preserves
    version basis and original syntax evidence without changing imported binding states.
    A native version basis and a conditional origin can coexist; neither proves dispatch.
    Module names are provider questions; arbitrary repository paths are not inputs.
    """

    package: str
    version: str
    module: str
    version_basis: Literal[
        "native_old_version", "native_proposed_version", "constraint_sample", "explicit_version",
    ]
    origin: ReferenceFact | ImportFact | None = None

@dataclass(frozen=True)
class ExaminedPythonModule:
    request: PythonModuleSourceRequest
    association: DeclaredSourceAssociation
    metadata: PackageDependencyMetadata
    tags: tuple[GitHubTagCommitEvidence, ...]
    inventory: RepositoryInventory
    file: RepositoryTextFile
    imports: tuple[ImportFact, ...]
    references: tuple[ReferenceFact, ...]
    gaps: tuple[ContextGap, ...]

def select_exploration_version(
    index: PackageReleaseIndexEvidence, declaration: DependencyDeclaration
) -> str | AcquisitionProblem:
    """Deterministic sampling choice, explicitly separate from resolver truth."""
    candidates = []
    for raw in index.release_versions:
        try:
            version = Version(raw)
        except InvalidVersion:
            continue
        if (
            not version.is_prerelease
            and not version.is_devrelease
            and SpecifierSet(declaration.specifier).contains(version)
        ):
            candidates.append((version, raw))
    if not candidates:
        return AcquisitionProblem(
            "adapter_sample",
            "no_supported_sample",
            "No stable registry release satisfies the visible constraint.",
        )
    newest = max(version for version, _ in candidates)
    raw = [raw for version, raw in candidates if version == newest]
    if len(raw) != 1:
        return AcquisitionProblem(
            "adapter_sample",
            "ambiguous_version_identity",
            "Newest sample has equivalent raw version identities.",
        )
    return raw[0]

def _module_path(inventory: RepositoryInventory, module: str) -> str | AcquisitionProblem:
    """Use package path grammar; never a caller-supplied expected source path."""
    tail = module.replace(".", "/")
    allowed = {
        tail + ".py",
        tail + "/__init__.py",
        "src/" + tail + ".py",
        "src/" + tail + "/__init__.py",
    }
    paths = [
        e.path
        for e in inventory.entries
        if e.path in allowed and e.kind == "blob" and e.mode in {"100644", "100755"}
    ]
    if inventory.truncated:
        return AcquisitionProblem(
            "adapter_module",
            "inventory_truncated",
            "Cannot establish unique module path from truncated tree.",
        )
    if len(paths) != 1:
        return AcquisitionProblem(
            "adapter_module",
            "module_path_not_established",
            f"Expected one flat/src module path, found {len(paths)}.",
        )
    return paths[0]

@dataclass(frozen=True)
class ReleaseSourceProgress:
    """Returned provider premises observed before a later release-stage failure.

    Run-local progress is volatile until the application publishes a native source
    checkpoint. Each replacement is immutable, so earlier snapshots stay truthful.
    """
    package: str
    version: str
    release: PackageReleaseEvidence | None = None
    association: DeclaredSourceAssociation | None = None
    publisher: PublisherProvenanceInspection | None = None
    metadata: PackageDependencyMetadata | None = None
    tags: tuple[GitHubTagCommitEvidence, ...] = ()
    inventory: RepositoryInventory | None = None
    problem: AcquisitionProblem | None = None
    repository_move: SourceRepositoryMove | None = None


class PythonSourceAcquisitionRun:
    """Exact source examination with run-local identity, failure and work caches.

    Create through AdapterSourceExplorer.source_run. Share this run with explore
    when exact changed-version reads and adapter samples must use one budget and
    observation horizon. Fresh default explore calls still receive fresh runs.
    Success establishes captured source/facts only, never an installed namespace,
    positive imported binding, callable correspondence or compatibility.

    module_attempts counts new questions processed, including release refusals;
    source_bytes counts admitted complete text, not every downloaded response byte.
    Cached success/failure avoids implicit retries. Provider GET accounting remains
    separate at AcquisitionSession; this run is not a total-memory/time controller.
    """

    def __init__(self, source_owner, *, max_releases=4, max_module_files=12,
                 max_bytes=2 * 1024 * 1024):
        if (type(max_releases) is not int or not 1 <= max_releases <= 4
            or type(max_module_files) is not int or not 1 <= max_module_files <= 12
            or type(max_bytes) is not int or not 1 <= max_bytes <= 2 * 1024 * 1024):
            raise ValueError("Source budgets exceed admitted limits.")
        self._source_owner = source_owner
        self.max_releases = max_releases
        self.max_module_files = max_module_files
        self.max_bytes = max_bytes
        self._release_cache = {}
        self._release_progress = {}
        self._repository_moves: dict[str, SourceRepositoryMove] = {}
        self._module_cache = {}
        self._index_cache = {}
        self.module_attempts = 0
        self.source_bytes = 0

    @property
    def release_observations(self) -> tuple[ReleaseSourceProgress, ...]:
        """Actual returned release premises, including incomplete/refused stages."""
        return tuple(self._release_progress.values())

    @property
    def release_identities(self) -> tuple[tuple[str, str], ...]:
        """Attempted exact identities, including refused/unavailable releases."""
        return tuple(self._release_cache)

    @property
    def work(self) -> PythonSourceAcquisitionWork:
        return PythonSourceAcquisitionWork(self.release_identities, self.module_attempts, self.source_bytes)

    def examine(self, request: PythonModuleSourceRequest) -> ExaminedPythonModule | AcquisitionProblem:
        if (not isinstance(request, PythonModuleSourceRequest)
            or request.version_basis not in {"native_old_version", "native_proposed_version",
                                            "constraint_sample", "explicit_version"}
            or not isinstance(request.package, str) or not request.package
            or not isinstance(request.version, str) or not request.version.strip()
            or not isinstance(request.module, str)
            or not all(part.isidentifier() for part in request.module.split("."))):
            raise ValueError("Invalid Python module source question.")
        if request.origin is not None and not isinstance(request.origin, (ReferenceFact, ImportFact)):
            raise ValueError("Source origin must retain original import/reference evidence.")
        key = (request.package, request.version, request.module)
        if key in self._module_cache:
            cached = self._module_cache[key]
            # Source work is shared, but a later question keeps its own basis.
            return replace(cached, request=request) if isinstance(cached, ExaminedPythonModule) else cached
        if self.module_attempts >= self.max_module_files:
            return AcquisitionProblem("python_source_budget", "module_source_limit",
                                      "Module question remains unexamined at the shared run limit.")
        if self._source_owner.session.request_limit_reached:
            return AcquisitionProblem("python_source_budget", self._source_owner.session.request_limit_reason,
                                      "No new source read admitted after the provider request limit.")
        self.module_attempts += 1
        release_key = (request.package, request.version)
        if release_key not in self._release_cache:
            if len(self._release_cache) >= self.max_releases:
                return AcquisitionProblem("python_source_budget", "release_source_limit",
                                          "Exact release identity remains unexamined at the shared run limit.")
            try:
                inspected = self._inspect_release(*release_key)
            except (GitHubAcquisitionError, GitHubResponseError) as exc:
                inspected = self._provider_problem(exc)
            if isinstance(inspected, AcquisitionProblem):
                inspected = self._preserve_request_limit(inspected)
            if isinstance(inspected, AcquisitionProblem):
                progress = self._release_progress.get(release_key)
                if progress is not None:
                    self._release_progress[release_key] = replace(progress, problem=inspected)
            self._release_cache[release_key] = inspected
        inspected = self._release_cache[release_key]
        if isinstance(inspected, AcquisitionProblem):
            self._module_cache[key] = inspected
            return inspected
        association, metadata, tags, inventory = inspected
        path = _module_path(inventory, request.module)
        if isinstance(path, AcquisitionProblem):
            self._module_cache[key] = path
            return path
        try:
            file = self._source_owner.files.get_exact_commit_text_file(
                inventory.repository, inventory.revision, path,
            )
            if not isinstance(file, RepositoryTextFile):
                result = AcquisitionProblem("adapter_file", file.reason, file.detail, file)
            else:
                size = len(file.content.encode("utf-8"))
                if self.source_bytes + size > self.max_bytes:
                    result = AcquisitionProblem("python_source_budget", "source_text_limit",
                        "Full module text exceeds the shared run byte limit; no truncation.",
                        {"repository": file.repository, "revision": file.revision,
                         "path": file.path, "utf8_bytes": size})
                else:
                    self.source_bytes += size
                    imports, references, gaps = extract_python_facts(file)
                    result = ExaminedPythonModule(request, association, metadata, tuple(tags),
                                                  inventory, file, imports, references, gaps)
        except (GitHubAcquisitionError, GitHubResponseError) as exc:
            result = self._provider_problem(exc)
        if isinstance(result, AcquisitionProblem):
            result = self._preserve_request_limit(result)
        self._module_cache[key] = result
        return result

    def examine_with_receipt(self, request: PythonModuleSourceRequest):
        """Examine once and return its native receipt beside the qualified outcome.

        Native family roles normalize the question's qualified version labels at
        this boundary. Full successful premises remain mandatory. Failed reads
        retain earlier release/association/metadata/tag observations but cannot
        admit a comparison file. This method performs no Workspace publication.
        """
        outcome = self.examine(request)
        role = {"native_old_version": "old_dependency",
                "native_proposed_version": "proposed_dependency"}.get(request.version_basis, request.version_basis)
        native_request = ModuleSourceRequest(request.package, request.version, request.module, role, request.origin)
        progress = self._release_progress.get((request.package, request.version))
        move = progress.repository_move if progress else None
        if isinstance(outcome, ExaminedPythonModule):
            association, metadata, tags = outcome.association, outcome.metadata, outcome.tags
            repository, revision, path = outcome.file.repository, outcome.file.revision, outcome.file.path
            payload = outcome.file.content.encode("utf-8")
            digest, size = sha256(payload).hexdigest(), len(payload)
            state, problem, gaps = "module_examined", None, outcome.gaps
        else:
            association = progress.association if progress else None
            metadata = progress.metadata if progress else None
            tags = progress.tags if progress else ()
            repository = association.repository if association else None
            if move and move.verified:
                repository = move.canonical_repository
            revision = progress.inventory.revision if progress and progress.inventory else None
            if revision is None and tags and len({t.resolved_commit_sha for t in tags}) == 1:
                revision = tags[0].resolved_commit_sha
            path, digest, size = None, None, None
            if progress and progress.inventory:
                selected = _module_path(progress.inventory, request.module)
                path = selected if isinstance(selected, str) else None
            # The byte-limit refusal observed this exact file size, but did not
            # retain full text. Never fabricate its content hash or admit it.
            if outcome.reason == "source_text_limit" and isinstance(outcome.evidence, dict):
                size = outcome.evidence["utf8_bytes"]
            state = "refused" if outcome.stage in {"python_source_budget", "adapter_budget"} else "unavailable"
            problem = SourceProblem(outcome.stage, outcome.reason, outcome.detail)
            gaps = ()
        retention_gaps = ()
        if association is None and progress is not None:
            # The v1 module family has no standalone release/publisher slot.
            # Keep those live observations available to the composer and make
            # their absence from this partial retained summary explicit.
            retention_gaps = tuple(label for label, present in (
                ("release_observation_available_in_run_only", progress.release is not None),
                ("publisher_observation_available_in_run_only", progress.publisher is not None),
            ) if present)
        receipt = ModuleSourceReceipt(native_request, state, problem, repository, revision, path, digest, size,
            association.basis if association else None,
            association.provenance.state if association else None,
            tuple(SourceTagCommit(tag.requested_tag, tag.resolved_commit_sha) for tag in tags),
            metadata, gaps, association, tags, retention_gaps, move)
        return outcome, receipt

    def _preserve_request_limit(self, problem: AcquisitionProblem) -> AcquisitionProblem:
        # Providers may wrap the transport refusal in their own typed result.
        # Preserve both that evidence and the actual run-level stopping cause.
        if self._source_owner.session.request_limit_reached and problem.reason != self._source_owner.session.request_limit_reason:
            return AcquisitionProblem("python_source_budget", self._source_owner.session.request_limit_reason,
                                      "Provider request limit reached during source acquisition.", problem)
        return problem

    def _provider_problem(self, error: GitHubAcquisitionError | GitHubResponseError) -> AcquisitionProblem:
        if self._source_owner.session.request_limit_reached:
            return AcquisitionProblem("python_source_budget", self._source_owner.session.request_limit_reason, str(error), error)
        return AcquisitionProblem("adapter_acquisition", getattr(error, "reason", "malformed_response"),
                                  str(error), error)

    def _inspect_release(self, package: str, version: str):
        """Reuse one per-run exact release/tag/tree observation across module files.

        This cache controls requests and mutable registry observation drift; it is
        neither a persistent package database nor target resolution state.
        """
        key = (package, version)
        progress = ReleaseSourceProgress(package, version)
        self._release_progress[key] = progress
        release = self._source_owner.releases.get_release(package, version)
        if not isinstance(release, PackageReleaseEvidence):
            return AcquisitionProblem(
                "adapter_release", release.state, release.detail, release
            )
        progress = replace(progress, release=release)
        self._release_progress[key] = progress
        publisher = self._source_owner.provenance.resolve(release)
        progress = replace(progress, publisher=publisher)
        self._release_progress[key] = progress
        association = associate_declared_source(release, publisher)
        if isinstance(association, AcquisitionProblem):
            return association
        progress = replace(progress, association=association)
        self._release_progress[key] = progress
        metadata = self._source_owner.metadata.acquire(package, version)
        if isinstance(metadata, AcquisitionProblem):
            return metadata
        progress = replace(progress, metadata=metadata)
        self._release_progress[key] = progress
        tags = self._inspect_tags(progress, association.repository)
        if isinstance(tags, AcquisitionProblem):
            return tags
        if not tags or len({t.resolved_commit_sha for t in tags}) != 1:
            return AcquisitionProblem(
                "adapter_tag",
                "tag_not_established",
                "Missing/conflicting exact tag spellings.",
                tuple(tags),
            )
        repository = tags[0].repository
        inventory = self._source_owner.inventory.acquire(repository, tags[0].resolved_commit_sha)
        if isinstance(inventory, RepositoryInventoryProblem):
            return AcquisitionProblem("inventory", inventory.reason, inventory.detail, inventory.status_code)
        if isinstance(inventory, AcquisitionProblem):
            return inventory
        self._release_progress[key] = replace(self._release_progress[key], inventory=inventory)
        return association, metadata, tags, inventory

    def _inspect_tags(self, progress: ReleaseSourceProgress, declared_repository: str):
        key = (progress.package, progress.version)
        move = self._repository_moves.get(declared_repository.casefold())
        repository = move.canonical_repository if move else declared_repository
        lookup = self._source_owner.tags.resolve_tag_to_commit if move else self._source_owner.initial_tag_lookup
        if move:
            self._release_progress[key] = replace(progress, repository_move=move)
        tags = []
        for spelling in (progress.version, "v" + progress.version):
            tag = lookup(repository, spelling)
            if isinstance(tag, GitHubTagRepositoryRedirect):
                return self._verify_move_and_read_tags(key, tag, tags[0] if tags else None)
            if isinstance(tag, GitHubTagCommitEvidence):
                tags.append(tag)
                self._release_progress[key] = replace(self._release_progress[key], tags=tuple(tags))
            elif tag.state != "source_unavailable":
                return AcquisitionProblem("adapter_tag", tag.state, tag.detail, tag)
        return tuple(tags)

    def _verify_move_and_read_tags(self, key, redirect, prior_tag):
        progress = self._release_progress[key]
        move = SourceRepositoryMove(redirect, prior_tag=prior_tag)
        self._release_progress[key] = replace(progress, repository_move=move, tags=())
        repositories = self._source_owner.files
        canonical = repositories.get_public_repository_name(redirect.repository_id)
        if canonical.casefold() == redirect.repository.casefold():
            return AcquisitionProblem("adapter_tag", "repository_move_unresolved",
                                      "GitHub returned the declared name as the move destination.")
        move = replace(move, canonical_repository=canonical)
        self._release_progress[key] = replace(self._release_progress[key], repository_move=move)
        repositories.get_public_repository_name(redirect.repository_id, name=canonical)
        move = replace(move, verified=True)
        self._repository_moves[redirect.repository.casefold()] = replace(move, prior_tag=None)
        tags = self._inspect_tags(replace(progress, tags=()), redirect.repository)
        self._release_progress[key] = replace(self._release_progress[key], repository_move=move)
        if not isinstance(tags, AcquisitionProblem) and prior_tag and not any(
            (tag.requested_tag, tag.resolved_commit_sha) == (prior_tag.requested_tag, prior_tag.resolved_commit_sha)
            for tag in tags
        ):
            return AcquisitionProblem("adapter_tag", "tag_not_established",
                                      "The prior tag observation disagrees with the canonical repository.")
        return tags

class AdapterSourceExplorer:
    def __init__(
        self,
        *,
        session,
        index=None,
        releases=None,
        provenance=None,
        metadata=None,
        tags=None,
        inventory=None,
        files=None,
    ):
        self.session = session
        self.index = index or PyPIReleaseIndexClient(session=self.session)
        self.releases = releases or PyPIReleaseClient(session=self.session)
        self.provenance = provenance or PublisherProvenanceInspector(
            client=PyPIProvenanceClient(session=self.session)
        )
        self.metadata = metadata or PackageDependencyMetadataClient(session=self.session)
        self.tags = tags or GitHubTagCommitClient(session=self.session)
        self.initial_tag_lookup = self.tags.resolve_tag_to_commit
        if tags is None and isinstance(session, AcquisitionSession):
            self.initial_tag_lookup = partial(self.initial_tag_lookup, observe_repository_move=True)
        self.inventory = inventory or GitHubRepositoryInventoryClient(
            session=self.session
        )
        self.files = files or GitHubRepositoryClient(session=self.session)

    def source_run(self, *, max_releases=4, max_module_files=12,
                   max_bytes=2 * 1024 * 1024) -> PythonSourceAcquisitionRun:
        return PythonSourceAcquisitionRun(
            self, max_releases=max_releases, max_module_files=max_module_files, max_bytes=max_bytes,
        )

    def explore(
        self,
        context: TargetSourceContext | AdapterDiscoverySeed,
        *,
        max_samples=4,
        max_hops=2,
        max_module_files=12,
        source_run: PythonSourceAcquisitionRun | None = None,
        stop_at_package: str | None = None,
        max_candidate_attempts: int = 12,
        prioritize_indirect_exact_pair: bool = False,
    ) -> AdapterExploration:
        if (
            type(max_samples) is not int
            or not 1 <= max_samples <= 4
            or type(max_hops) is not int
            or not 0 <= max_hops <= 2
            or type(max_module_files) is not int
            or not 1 <= max_module_files <= 12
            or type(max_candidate_attempts) is not int
            or not 1 <= max_candidate_attempts <= 12
        ):
            raise ValueError("Exploration budgets exceed admitted limits.")
        if source_run is not None and (
            source_run._source_owner is not self or source_run.max_releases > max_samples
            or source_run.max_module_files > max_module_files
        ):
            raise ValueError("Shared source run must use this owner and fit exploration limits.")
        self._source_run = source_run if source_run is not None else self.source_run(
            max_releases=max_samples, max_module_files=max_module_files,
        )
        self._index_cache = self._source_run._index_cache
        # More specific acquired modules first; lexical target calls/bases justify
        # exploration. Ordering contains no package/adapter-name special cases.
        used = [
            c
            for c in context.candidates
            if any(
                r.lexical_import
                and (
                    r.lexical_import == c.imported_module
                    or r.lexical_import.startswith(c.imported_module + ".")
                )
                and r.source_id == c.import_source_id
                for r in context.references
            )
        ]
        pending = deque(
            (c, 0, frozenset(
                r.lexical_import[len(c.imported_module) + 1:].split(".")[0]
                for r in context.references if r.lexical_import
                and r.source_id == c.import_source_id
                and r.lexical_import.startswith(c.imported_module + ".")))
            for c in sorted(
                used, key=lambda c: (-c.imported_module.count("."), c.imported_module)
            )
        )
        seen = set()
        samples = []
        problems = []
        omitted = []
        deferred = []
        failed_move_receipts = []
        attempts = 0
        while pending:
            candidate, depth, members = pending.popleft()
            key = (candidate.imported_module, candidate.declaration)
            if key in seen:
                continue
            seen.add(key)
            if depth > max_hops:
                omitted.append(candidate)
                continue
            # The ordinary PR caller already knows this dependency's exact old/
            # proposed identities. Let that stage inspect them instead of sampling
            # a potentially unrelated third version and consuming its source slots.
            if candidate.declaration.package == stop_at_package:
                deferred.append(candidate)
                if depth and prioritize_indirect_exact_pair:
                    # Hand the observed path to the exact-version composer while
                    # unrelated queued samples can still be left unexamined.
                    omitted.extend(c for c, _, _ in pending if (c.imported_module, c.declaration) not in seen)
                    break
                continue
            if attempts >= min(max_module_files, max_candidate_attempts):
                omitted.append(candidate)
                continue
            attempts += 1
            try:
                sample = self._acquire(candidate, depth, failed_move_receipts)
            except GitHubAcquisitionError as exc:
                sample = AcquisitionProblem("adapter_acquisition", exc.reason, str(exc))
            except GitHubResponseError as exc:
                sample = AcquisitionProblem(
                    "adapter_acquisition", "malformed_response", str(exc)
                )
            if isinstance(sample, AcquisitionProblem):
                if self.session.request_limit_reached:
                    sample = AcquisitionProblem(
                        "adapter_budget",
                        self.session.request_limit_reason,
                        "Invocation GitHub request budget exhausted; remaining adapter candidates are unexamined.",
                        sample,
                    )
                problems.append(sample)
                if sample.reason == self.session.request_limit_reason:
                    omitted.append(candidate)
                    omitted.extend(c for c, _, _ in pending)
                    break
                if sample.stage == "adapter_budget":
                    omitted.append(candidate)
                continue
            samples.append(sample)
            # Follow only external imports also declared by this exact sample's
            # metadata. Imported-but-undeclared names remain unresolved, not guessed.
            continuations = []
            for fact in sample.imports:
                if fact.relative_level or not fact.module:
                    continue
                root = normalize_package_name(fact.module.split(".")[0])
                for declaration in sample.metadata.requirements:
                    if declaration.package == root:
                        follows_member = bool(fact.member and (fact.alias or fact.member) in members)
                        child = (ImportDependencyCandidate(fact.module, declaration, fact.source_id, fact.line),
                                 depth + 1, frozenset((fact.member,)) if follows_member else frozenset())
                        # Follow an acquired re-export of the target's observed
                        # member before unrelated roots. This chooses work only;
                        # source correspondence still owns the conditional edge.
                        if stop_at_package and (follows_member or declaration.package == stop_at_package):
                            continuations.append(child)
                        else:
                            pending.append(child)
            pending.extendleft(reversed(continuations))
        return AdapterExploration(
            tuple(samples), tuple(problems), tuple(omitted), deferred_candidates=tuple(deferred),
            failed_move_receipts=tuple(failed_move_receipts),
        )

    def _acquire(
        self, candidate: ImportDependencyCandidate, depth: int,
        failed_move_receipts: list[ModuleSourceReceipt],
    ) -> AdapterModuleSample | AcquisitionProblem:
        declaration = candidate.declaration
        if declaration.package not in self._index_cache:
            self._index_cache[declaration.package] = self.index.get_release_index(
                declaration.package
            )
        index = self._index_cache[declaration.package]
        if not isinstance(index, PackageReleaseIndexEvidence):
            return AcquisitionProblem("adapter_index", index.state, index.detail, index)
        if index.normalized_package != declaration.package:
            return AcquisitionProblem(
                "adapter_index",
                "identity_mismatch",
                "Sample index describes another package.",
            )
        version = select_exploration_version(index, declaration)
        if isinstance(version, AcquisitionProblem):
            return version
        examined, receipt = self._source_run.examine_with_receipt(PythonModuleSourceRequest(
            declaration.package, version, candidate.imported_module, "constraint_sample",
        ))
        if isinstance(examined, AcquisitionProblem):
            if receipt.repository_move is not None:
                failed_move_receipts.append(receipt)
            if examined.stage == "python_source_budget":
                reasons = {"release_source_limit": "release_sample_limit", "source_text_limit": "adapter_text_limit"}
                return replace(examined, stage="adapter_budget", reason=reasons.get(examined.reason, examined.reason))
            return examined
        return AdapterModuleSample(
            candidate, depth, version,
            "latest_stable_satisfying_visible_constraint_exploration_only",
            examined.association, examined.metadata, examined.tags, examined.inventory,
            examined.file, examined.imports, examined.references, examined.gaps,
        )
