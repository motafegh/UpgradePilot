"""Explore version-specific adapter sources from acquired import/dependency candidates.

Start at AdapterSourceExplorer.explore. Samples are the latest stable releases
satisfying a visible declaration, explicitly NOT resolved target versions. Exact
PyPI metadata, declared association, tag/tree/module acquisition and static facts
remain attributable. A package/module naming match is a candidate, never installed
namespace proof. Two dependency hops/four release identities bound exploration, not coverage.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
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


@dataclass(frozen=True)
class AdapterDiscoverySeed:
    """Minimal producer facts for a labelled adapter-stage replay, not a report."""

    candidates: tuple[ImportDependencyCandidate, ...]
    references: tuple[ReferenceFact, ...]
    binding_analysis_version: int = 1


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

    def explore(
        self,
        context: TargetContext | AdapterDiscoverySeed,
        *,
        max_samples=4,
        max_hops=2,
        max_module_files=12,
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
        self._index_cache = {}
        self._release_cache = {}
        self._max_samples = max_samples
        self._adapter_bytes = 0
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
        attempts = 0
        while pending:
            candidate, depth = pending.popleft()
            key = (candidate.imported_module, candidate.declaration)
            if key in seen:
                continue
            seen.add(key)
            if attempts >= max_module_files or depth > max_hops:
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
        return AdapterExploration(tuple(samples), tuple(problems), tuple(omitted))

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
        key = (declaration.package, version)
        if key not in self._release_cache:
            if len(self._release_cache) >= self._max_samples:
                return AcquisitionProblem(
                    "adapter_budget",
                    "release_sample_limit",
                    "Unexamined release identity; four samples do not exhaust a range.",
                )
            self._release_cache[key] = self._inspect_release(
                declaration.package, version
            )
        inspected = self._release_cache[key]
        if isinstance(inspected, AcquisitionProblem):
            return inspected
        association, metadata, tags, inventory = inspected
        repository = association.repository
        path = _module_path(inventory, candidate.imported_module)
        if isinstance(path, AcquisitionProblem):
            return path
        file = self.files.get_exact_commit_text_file(
            repository, inventory.revision, path
        )
        if not isinstance(file, RepositoryTextFile):
            return AcquisitionProblem("adapter_file", file.reason, file.detail, file)
        size = len(file.content.encode("utf-8"))
        if self._adapter_bytes + size > 2 * 1024 * 1024:
            return AcquisitionProblem(
                "adapter_budget",
                "adapter_text_limit",
                "Adapter text exceeds 2 MiB; source is not truncated.",
            )
        self._adapter_bytes += size
        imports, references, gaps = extract_python_facts(file)
        return AdapterModuleSample(
            candidate,
            depth,
            version,
            "latest_stable_satisfying_visible_constraint_exploration_only",
            association,
            metadata,
            tuple(tags),
            inventory,
            file,
            imports,
            references,
            gaps,
        )

    def _inspect_release(self, package: str, version: str):
        """Reuse one per-run exact release/tag/tree observation across module files.

        This cache controls requests and mutable registry observation drift; it is
        neither a persistent package database nor target resolution state.
        """
        release = self.releases.get_release(package, version)
        if not isinstance(release, PackageReleaseEvidence):
            return AcquisitionProblem(
                "adapter_release", release.state, release.detail, release
            )
        association = associate_declared_source(
            release, self.provenance.resolve(release)
        )
        if isinstance(association, AcquisitionProblem):
            return association
        metadata = self.metadata.acquire(package, version)
        if isinstance(metadata, AcquisitionProblem):
            return metadata
        tags = []
        for spelling in (version, "v" + version):
            tag = self.tags.resolve_tag_to_commit(association.repository, spelling)
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
        inventory = self.inventory.acquire(repository, tags[0].resolved_commit_sha)
        if isinstance(inventory, AcquisitionProblem):
            return inventory
        return association, metadata, tuple(tags), inventory
