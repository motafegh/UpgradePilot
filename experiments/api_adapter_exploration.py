"""Explore version-specific adapter sources from acquired import/dependency candidates.

Start at AdapterSourceExplorer.explore for constraint-selected samples, or create
its source_run() to examine explicit package/version/module questions. Both use
one bounded exact-release/tag/tree/module owner. Samples are the latest stable releases
satisfying a visible declaration, explicitly NOT resolved target versions. Exact
PyPI metadata, declared association, tag/tree/module acquisition and static facts
remain attributable. A package/module naming match is a candidate, never installed
namespace proof. Two dependency hops/four release identities bound exploration, not coverage.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, replace
from typing import Literal
from urllib.parse import quote

from packaging.requirements import InvalidRequirement, Requirement
from packaging.specifiers import SpecifierSet
from packaging.version import InvalidVersion, Version

from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github.identity import validate_repository
from upgradepilot.github.repository import GitHubRepositoryClient, RepositoryTextFile
from upgradepilot.github.tag import GitHubTagCommitClient, GitHubTagCommitEvidence
from upgradepilot.package_identity import normalize_package_name
from upgradepilot.pypi.api import PyPIJsonApiClient, PyPIRequestError, PyPIResponseError
from upgradepilot.pypi.provenance import PyPIProvenanceClient
from upgradepilot.pypi.release import (
    PackageReleaseEvidence,
    PackageReleaseIndexEvidence,
    PyPIReleaseClient,
    PyPIReleaseIndexClient,
)

from .api_change_source_acquisition import (
    AcquisitionProblem,
    DeclaredSourceAssociation,
    PublisherProvenanceInspector,
    TrialPublicSession,
    associate_declared_source,
)
from .api_target_context import (
    ContextGap,
    DependencyDeclaration,
    ImportDependencyCandidate,
    ImportFact,
    ReferenceFact,
    TargetContext,
    TargetInventory,
    TrialRepositoryInventoryClient,
    extract_python_facts,
)


@dataclass(frozen=True)
class PackageDependencyMetadata:
    package: str
    version: str
    source_url: str
    requirements: tuple[DependencyDeclaration, ...]
    gaps: tuple[ContextGap, ...]


class TrialDependencyMetadataClient(PyPIJsonApiClient):
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
    inventory: TargetInventory
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
    inventory: TargetInventory
    file: RepositoryTextFile
    imports: tuple[ImportFact, ...]
    references: tuple[ReferenceFact, ...]
    gaps: tuple[ContextGap, ...]


@dataclass(frozen=True)
class PythonSourceAcquisitionWork:
    release_identities: tuple[tuple[str, str], ...]
    module_attempts: int
    source_bytes: int


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


def _module_path(inventory: TargetInventory, module: str) -> str | AcquisitionProblem:
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
    separate at TrialPublicSession; this run is not a total-memory/time controller.
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
        self._module_cache = {}
        self._index_cache = {}
        self.module_attempts = 0
        self.source_bytes = 0

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
            return AcquisitionProblem("python_source_budget", "trial_request_limit",
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
                association.repository, inventory.revision, path,
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

    def _preserve_request_limit(self, problem: AcquisitionProblem) -> AcquisitionProblem:
        # Providers may wrap the transport refusal in their own typed result.
        # Preserve both that evidence and the actual run-level stopping cause.
        if self._source_owner.session.request_limit_reached and problem.reason != "trial_request_limit":
            return AcquisitionProblem("python_source_budget", "trial_request_limit",
                                      "Provider request limit reached during source acquisition.", problem)
        return problem

    def _provider_problem(self, error: GitHubAcquisitionError | GitHubResponseError) -> AcquisitionProblem:
        if self._source_owner.session.request_limit_reached:
            return AcquisitionProblem("python_source_budget", "trial_request_limit", str(error), error)
        return AcquisitionProblem("adapter_acquisition", getattr(error, "reason", "malformed_response"),
                                  str(error), error)

    def _inspect_release(self, package: str, version: str):
        """Reuse one per-run exact release/tag/tree observation across module files.

        This cache controls requests and mutable registry observation drift; it is
        neither a persistent package database nor target resolution state.
        """
        release = self._source_owner.releases.get_release(package, version)
        if not isinstance(release, PackageReleaseEvidence):
            return AcquisitionProblem(
                "adapter_release", release.state, release.detail, release
            )
        association = associate_declared_source(
            release, self._source_owner.provenance.resolve(release)
        )
        if isinstance(association, AcquisitionProblem):
            return association
        metadata = self._source_owner.metadata.acquire(package, version)
        if isinstance(metadata, AcquisitionProblem):
            return metadata
        tags = []
        for spelling in (version, "v" + version):
            tag = self._source_owner.tags.resolve_tag_to_commit(association.repository, spelling)
            if isinstance(tag, GitHubTagCommitEvidence):
                tags.append(tag)
            elif tag.state != "source_unavailable":
                return AcquisitionProblem("adapter_tag", tag.state, tag.detail, tag)
        if not tags or len({t.resolved_commit_sha for t in tags}) != 1:
            return AcquisitionProblem(
                "adapter_tag",
                "tag_not_established",
                "Missing/conflicting exact tag spellings.",
                tuple(tags),
            )
        repository = validate_repository(association.repository)
        inventory = self._source_owner.inventory.acquire(repository, tags[0].resolved_commit_sha)
        if isinstance(inventory, AcquisitionProblem):
            return inventory
        return association, metadata, tuple(tags), inventory


class AdapterSourceExplorer:
    def __init__(
        self,
        *,
        session=None,
        index=None,
        releases=None,
        provenance=None,
        metadata=None,
        tags=None,
        inventory=None,
        files=None,
    ):
        self.session = session or TrialPublicSession()
        self.index = index or PyPIReleaseIndexClient(session=self.session)
        self.releases = releases or PyPIReleaseClient(session=self.session)
        self.provenance = provenance or PublisherProvenanceInspector(
            client=PyPIProvenanceClient(session=self.session)
        )
        self.metadata = metadata or TrialDependencyMetadataClient(session=self.session)
        self.tags = tags or GitHubTagCommitClient(session=self.session)
        self.inventory = inventory or TrialRepositoryInventoryClient(
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
        context: TargetContext | AdapterDiscoverySeed,
        *,
        max_samples=4,
        max_hops=2,
        max_module_files=12,
        source_run: PythonSourceAcquisitionRun | None = None,
        stop_at_package: str | None = None,
    ) -> AdapterExploration:
        if (
            type(max_samples) is not int
            or not 1 <= max_samples <= 4
            or type(max_hops) is not int
            or not 0 <= max_hops <= 2
            or type(max_module_files) is not int
            or not 1 <= max_module_files <= 12
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
            (c, 0)
            for c in sorted(
                used, key=lambda c: (-c.imported_module.count("."), c.imported_module)
            )
        )
        seen = set()
        samples = []
        problems = []
        omitted = []
        deferred = []
        attempts = 0
        while pending:
            candidate, depth = pending.popleft()
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
                continue
            if attempts >= max_module_files:
                omitted.append(candidate)
                continue
            attempts += 1
            try:
                sample = self._acquire(candidate, depth)
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
                        "trial_request_limit",
                        "Trial GitHub request budget exhausted; remaining adapter candidates are unexamined.",
                        sample,
                    )
                problems.append(sample)
                if sample.reason == "trial_request_limit":
                    omitted.append(candidate)
                    omitted.extend(c for c, _ in pending)
                    break
                if sample.stage == "adapter_budget":
                    omitted.append(candidate)
                continue
            samples.append(sample)
            # Follow only external imports also declared by this exact sample's
            # metadata. Imported-but-undeclared names remain unresolved, not guessed.
            for fact in sample.imports:
                if fact.relative_level or not fact.module:
                    continue
                root = normalize_package_name(fact.module.split(".")[0])
                for declaration in sample.metadata.requirements:
                    if declaration.package == root:
                        pending.append(
                            (
                                ImportDependencyCandidate(
                                    fact.module, declaration, fact.source_id, fact.line
                                ),
                                depth + 1,
                            )
                        )
        return AdapterExploration(
            tuple(samples), tuple(problems), tuple(omitted), deferred_candidates=tuple(deferred),
        )

    def _acquire(
        self, candidate: ImportDependencyCandidate, depth: int
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
        examined = self._source_run.examine(PythonModuleSourceRequest(
            declaration.package, version, candidate.imported_module, "constraint_sample",
        ))
        if isinstance(examined, AcquisitionProblem):
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
