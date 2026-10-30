"""Acquire declared upstream text for the API feasibility trial.

Start at DeclaredReleaseWindowAcquirer.acquire: exact PyPI releases/index → separate
association → exact Git tags/tree/file → complete Markdown release sections.
These records permit examination only. They never create product authority,
interpret API meaning or discover target exposure. Existing provider mechanics
are reused without constructing trusted interval/changelog evidence objects.
"""

from __future__ import annotations

import hashlib
import re
import time
from contextlib import contextmanager
from dataclasses import asdict, dataclass, replace
from datetime import UTC, datetime
from itertools import pairwise
from urllib.parse import urlsplit

from packaging.version import InvalidVersion, Version
from requests.exceptions import RequestException

from upgradepilot.dependency.versioning import (
    PackagingVersionProblem,
    order_crossed_release_versions,
    parse_dependency_release_interval,
)
from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github.auth_session import GitHubPublicSession
from upgradepilot.github.changelog import (
    DiscoveredChangelogPath,
    GitHubChangelogPathClient,
)
from upgradepilot.github.identity import validate_repository
from upgradepilot.github.repository import GitHubRepositoryClient, RepositoryTextFile
from upgradepilot.github.tag import GitHubTagCommitClient, GitHubTagCommitEvidence
from upgradepilot.pypi.provenance import FileProvenanceProblem, PyPIProvenanceClient
from upgradepilot.pypi.release import (
    PackageReleaseEvidence,
    PackageReleaseIndexEvidence,
    ProjectUrlCandidate,
    PyPIReleaseClient,
    PyPIReleaseIndexClient,
)
from upgradepilot.upstream.interval import DependencyReleaseInterval
from upgradepilot.upstream.repository import (
    normalize_project_url_label,
)


@dataclass(frozen=True)
class AcquisitionProblem:
    stage: str
    reason: str
    detail: str
    # Keep the original typed provider problem, including status/identity scope.
    evidence: object | None = None


@dataclass(frozen=True)
class PublisherProvenanceInspection:
    """Registry publisher records only, independent of project-link selection."""

    state: str
    detail: str
    repository: str | None = None
    records: tuple[object, ...] = ()


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


@dataclass(frozen=True)
class DeclaredSourceAssociation:
    release: PackageReleaseEvidence
    repository: str
    declarations: tuple[ProjectUrlCandidate, ...]
    ignored_links: tuple[ProjectUrlCandidate, ...]
    provenance_result: object
    basis: str = "exact_release_publisher_declared_repository"


@dataclass(frozen=True)
class ReleaseSection:
    version: str
    start_line: int
    start_offset: int
    end_offset: int
    text: str


@dataclass(frozen=True)
class ReleaseSectionCandidate:
    """Observed exact-heading match, including competing matches; no winner."""

    version: str
    match_count: int
    start_line: int
    start_offset: int
    end_offset: int
    sha256: str
    text: str | None


@dataclass(frozen=True)
class ReleaseWindowExamination:
    """Acquired-file observations retained when complete admission fails.

    Ranges use character offsets; hashes cover UTF-8 bytes. No-match means missing
    or outside the admitted heading grammar, never proven undocumented release.
    All candidate text is omitted if its aggregate exceeds the budget; metadata
    still identifies exact recovery, without silently choosing a smaller window.
    """

    repository: str
    revision: str
    path: str
    full_source_sha256: str
    required_versions: tuple[str, ...]
    candidates: tuple[ReleaseSectionCandidate, ...]
    missing_or_unsupported_versions: tuple[str, ...]
    ambiguous_versions: tuple[str, ...]
    issues: tuple[str, ...]
    max_characters: int
    text_omission_reason: str | None


@dataclass(frozen=True)
class IncompleteDeclaredReleaseWindow:
    """Section examination with the acquired declaration/provenance chain.

    Retaining this context does not construct an admitted DeclaredReleaseWindow.
    No file-acquisition failure can produce a section examination.
    """

    interval: DependencyReleaseInterval
    release_associations: tuple[DeclaredSourceAssociation, ...]
    release_index: PackageReleaseIndexEvidence
    ignored_index_versions: tuple[str, ...]
    tags: tuple[GitHubTagCommitEvidence, ...]
    tag_problems: tuple[object, ...]
    examination: ReleaseWindowExamination


@dataclass(frozen=True)
class DeclaredReleaseWindow:
    interval: DependencyReleaseInterval
    association: DeclaredSourceAssociation
    release_associations: tuple[DeclaredSourceAssociation, ...]
    release_index: PackageReleaseIndexEvidence
    ignored_index_versions: tuple[str, ...]
    ordered_versions: tuple[str, ...]
    tags: tuple[GitHubTagCommitEvidence, ...]
    tag_problems: tuple[object, ...]
    file: RepositoryTextFile
    sections: tuple[ReleaseSection, ...]
    full_text_sha256: str
    window_sha256: str
    # Coverage is the admitted exact-heading grammar, never all release channels.
    coverage: str = "complete_exact_version_atx_sections_at_proposed_tag"


def associate_declared_source(
    release: PackageReleaseEvidence, provenance: PublisherProvenanceInspection
) -> DeclaredSourceAssociation | AcquisitionProblem:
    """Keep provenance outcomes visible; only absence allows weaker examination.

    A supported stronger association is retained as context, not downgraded or
    cast into this trial's proposal authority. Homepage-only links are ignored.
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


def _version_heading(title: str) -> str:
    """Strip only a validated calendar-date suffix, not arbitrary release prose."""
    match = re.fullmatch(r"([^ ()]+) \(([^()]+)\)", title)
    if match is None:
        return title
    date = re.sub(r"(?<=\d)(?:st|nd|rd|th)(?= )", "", match[2])
    for grammar in ("%Y-%m-%d", "%d %B, %Y"):
        try:
            datetime.strptime(date, grammar).replace(tzinfo=UTC)
        except ValueError:
            continue
        return match[1]
    return title


def select_release_sections(
    file: RepositoryTextFile, versions: tuple[str, ...], *, max_characters: int = 20000
) -> tuple[ReleaseSection, ...] | AcquisitionProblem:
    """Select complete exact-version ATX sections, ignoring fenced headings.

    Collect all matches before admission, so missing/duplicate/order/overlap/size
    problems retain independently scoped observations. Equal/lower headings
    delimit sections; validated calendar suffixes are admitted. Other titles are
    unsupported. Partial evidence cannot stand in for a complete window.
    """
    headings = []
    offset = 0
    fence = None
    for number, line in enumerate(file.content.splitlines(keepends=True), 1):
        text = line.rstrip("\r\n")
        mark = re.fullmatch(r" {0,3}(`{3,}|~{3,})(.*)", text)
        if fence:
            char, count = fence
            if re.fullmatch(
                r" {0,3}" + re.escape(char) + "{" + str(count) + r",}[ \t]*", text
            ):
                fence = None
        elif mark:
            fence = (mark[1][0], len(mark[1]))
        else:
            match = re.fullmatch(r" {0,3}(#{1,6})(?:[ \t]+(.*))?", text)
            if match:
                title = re.sub(r"[ \t]+#+[ \t]*$", "", match[2] or "").strip()
                headings.append((len(match[1]), title, number, offset))
        offset += len(line)
    # Examine duplicate-heavy acquired files without a quadratic scan for every
    # candidate. The nearest equal/lower heading ends the exact section.
    ends = {}
    next_offsets = {}
    for level, _, _, start in reversed(headings):
        ends[start] = min(
            (end for other_level, end in next_offsets.items() if other_level <= level),
            default=len(file.content),
        )
        next_offsets[level] = start
    candidates = []
    missing = []
    ambiguous = []
    for version in versions:
        found = [
            h for h in headings if _version_heading(h[1]) in {version, "v" + version}
        ]
        if not found:
            missing.append(version)
        elif len(found) > 1:
            ambiguous.append(version)
        for heading in found:
            end = ends[heading[3]]
            text = file.content[heading[3] : end]
            candidates.append(
                ReleaseSectionCandidate(
                    version,
                    len(found),
                    heading[2],
                    heading[3],
                    end,
                    hashlib.sha256(text.encode("utf-8")).hexdigest(),
                    text,
                )
            )
    candidates.sort(key=lambda s: s.start_offset)
    issues = []
    if missing or ambiguous:
        issues.append("missing_or_duplicate_section")
    # Missing/ambiguous versions cannot establish order, but independent unique
    # matches can still expose inconsistent order. All ranges expose overlap.
    unique_order = tuple(s.version for s in candidates if s.match_count == 1)
    expected_order = tuple(v for v in versions if v in unique_order)
    if unique_order not in (expected_order, tuple(reversed(expected_order))) or any(
        a.end_offset > b.start_offset for a, b in pairwise(candidates)
    ):
        issues.append("section_order_or_overlap")
    omitted = None
    if sum(s.end_offset - s.start_offset for s in candidates) > max_characters:
        issues.append("window_too_large")
        omitted = "candidate_text_exceeds_character_budget"
        candidates = [replace(s, text=None) for s in candidates]
    if issues:
        return AcquisitionProblem(
            "window",
            issues[0],
            "Complete window not admitted: " + ", ".join(issues) + ".",
            ReleaseWindowExamination(
                file.repository,
                file.revision,
                file.path,
                hashlib.sha256(file.content.encode("utf-8")).hexdigest(),
                versions,
                tuple(candidates),
                tuple(missing),
                tuple(ambiguous),
                tuple(issues),
                max_characters,
                omitted,
            ),
        )
    return tuple(
        ReleaseSection(s.version, s.start_line, s.start_offset, s.end_offset, s.text)
        for s in candidates
    )


@dataclass(frozen=True)
class TrialAcquisitionPolicy:
    """Explicit experimental work policy, independent of provider/account quota.

    Larger finite selections are available for controlled qualification; selecting
    one here does not authorize a live run. Source/checker capability stays separate.
    """

    github_requests: int = 50
    provider_requests: int = 100
    response_bytes: int = 8 * 1024 * 1024
    aggregate_bytes: int = 32 * 1024 * 1024
    elapsed_seconds: float = 180.0
    source_request_reserve: int = 24
    target_file_attempts: int = 16
    adapter_candidate_attempts: int = 2

    def __post_init__(self):
        ceilings = (200, 400, 8 * 1024 * 1024, 64 * 1024 * 1024, 300.0, 199, 200, 12)
        for name, ceiling in zip(self.__dataclass_fields__, ceilings):
            value = getattr(self, name)
            types = (int, float) if name == "elapsed_seconds" else (int,)
            if type(value) not in types or not 0 < value <= ceiling:
                raise ValueError("Invalid acquisition policy: " + name)
        if self.source_request_reserve >= self.github_requests:
            raise ValueError("Source reservation must leave earlier GitHub work available.")
        if self.provider_requests < self.github_requests:
            raise ValueError("All-provider budget cannot be below the GitHub budget.")


class TrialPublicSession(GitHubPublicSession):
    """Host-scoped transport; anonymous unless a token is explicitly supplied.

    No declared URL is passed here: provider clients construct their own URLs.
    Rejected redirects are provider failures, never source absence or success.
    """

    def __init__(self, *, token: str | None = None, policy: TrialAcquisitionPolicy | None = None,
                 clock=time.monotonic):
        super().__init__()
        self.github_requests = 0
        self.request_limit_reached = False
        self._github_token = token
        self.auth_mode = "token-env" if token else "anonymous"
        self.policy = policy
        self._clock = clock
        self._started = clock()
        self._stage = "unscoped"
        self._reserve = 0
        self.provider_requests = 0
        self.body_bytes = 0
        self.receipts = []
        self.stop_reasons = []

    @contextmanager
    def stage(self, name, *, reserve_github=0):
        """Reserve later work without resetting shared counters or changing auth."""
        previous = self._stage, self._reserve
        if type(reserve_github) is not int or reserve_github < 0:
            raise ValueError("Invalid stage reservation.")
        self._stage, self._reserve = name, max(self._reserve, reserve_github)
        try:
            yield
        finally:
            self._stage, self._reserve = previous

    def _refuse(self, reason):
        marker = {"stage": self._stage, "reason": reason}
        if marker not in self.stop_reasons:
            self.stop_reasons.append(marker)
        if reason == "trial_request_limit":
            self.request_limit_reached = True
        raise GitHubAcquisitionError("Experimental acquisition stopped: " + reason, reason=reason)

    def _remaining_time(self):
        remaining = self.policy.elapsed_seconds - (self._clock() - self._started)
        if remaining <= 0:
            self._refuse("trial_acquisition_deadline")
        return remaining

    def finish_acquisition(self):
        """Reject an over-deadline acquisition even if its last read completed."""
        if self.policy:
            self._remaining_time()

    def acquisition_receipt(self):
        """Public-safe policy/cost data; never retain headers or credential values."""
        if self.policy is None:
            return None
        return dict(format="trial-acquisition-policy/1", limits=asdict(self.policy), auth=self.auth_mode,
                    github_requests=self.github_requests, provider_requests=self.provider_requests,
                    decoded_body_bytes=self.body_bytes, elapsed_seconds=max(0, self._clock() - self._started),
                    deadline_kind="cooperative_monotonic_checks_and_bounded_socket_timeouts",
                    stops=list(self.stop_reasons), requests=[dict(r) for r in self.receipts])

    def request(self, method, url, **kwargs):
        parsed = urlsplit(url)
        if (
            method.upper() != "GET"
            or parsed.scheme != "https"
            or parsed.hostname not in {"pypi.org", "api.github.com"}
            or parsed.username
            or parsed.password
            or parsed.port
        ):
            raise RequestException("Trial request outside admitted provider scope.")
        github = parsed.hostname == "api.github.com"
        maximum = self.policy.github_requests if self.policy else 50
        if github:
            if self.github_requests >= maximum:
                self.request_limit_reached = True
                self._refuse("trial_request_limit")
            if self.policy and self.github_requests >= maximum - self._reserve:
                self._refuse("trial_stage_request_limit")
        if self.policy:
            remaining = self._remaining_time()
            if self.provider_requests >= self.policy.provider_requests:
                self._refuse("trial_provider_request_limit")
            if self.body_bytes >= self.policy.aggregate_bytes:
                self._refuse("trial_aggregate_body_limit")
            timeout = kwargs.get("timeout", (3.05, 15.0))
            timeout = timeout if isinstance(timeout, tuple) else (timeout, timeout)
            kwargs["timeout"] = tuple(min(t or remaining, remaining) for t in timeout)
            kwargs["stream"] = True
        if github:
            self.github_requests += 1
        headers = dict(kwargs.get("headers", {}))
        if parsed.hostname == "api.github.com" and self._github_token:
            headers["Authorization"] = "Bearer " + self._github_token
        elif self.policy or parsed.hostname != "api.github.com":
            headers.pop("Authorization", None)
        kwargs["headers"] = headers
        kwargs["allow_redirects"] = False
        if self.policy is None:
            return super().request(method, url, **kwargs)
        self.provider_requests += 1
        receipt = dict(stage=self._stage, host=parsed.hostname, path=parsed.path[:512],
                       github_requests=self.github_requests, provider_requests=self.provider_requests,
                       decoded_body_bytes=0, status=None, state="started", reason=None)
        self.receipts.append(receipt)
        response = None
        try:
            response = super().request(method, url, **kwargs)
            receipt["status"] = response.status_code
            body = bytearray()
            for chunk in response.iter_content(chunk_size=8192):
                self.body_bytes += len(chunk)
                receipt["decoded_body_bytes"] += len(chunk)
                self._remaining_time()
                if receipt["decoded_body_bytes"] > self.policy.response_bytes:
                    self._refuse("trial_response_body_limit")
                if self.body_bytes > self.policy.aggregate_bytes:
                    self._refuse("trial_aggregate_body_limit")
                body.extend(chunk)
            self._remaining_time()
            # Requests' Response API then serves both json() and iter_content()
            # from these bounded decoded bytes. Providers keep their stricter caps.
            response._content = bytes(body)
            response._content_consumed = True
            receipt["state"] = "received"
            return response
        except Exception as exc:
            receipt["state"] = "failed"
            receipt["reason"] = getattr(exc, "reason", "transport_error")
            raise
        finally:
            if response is not None:
                response.close()


class DeclaredReleaseWindowAcquirer:
    """Trial orchestration; caller may inject providers for deterministic proof.

    Default providers remain public/anonymous. Optional distribution sampling is
    not performed: this first route has no shipped-metadata conflict question.
    Version/tag grammar is raw version or v-prefixed version; both are examined
    and disagreement is rejected, rather than first-match selection.
    """

    def __init__(
        self,
        *,
        session=None,
        releases=None,
        index=None,
        provenance=None,
        tags=None,
        paths=None,
        files=None,
    ):
        self.session = session or TrialPublicSession()
        self.releases = releases or PyPIReleaseClient(session=self.session)
        self.index = index or PyPIReleaseIndexClient(session=self.session)
        self.provenance = provenance or PublisherProvenanceInspector(
            client=PyPIProvenanceClient(session=self.session)
        )
        self.tags = tags or GitHubTagCommitClient(session=self.session)
        self.paths = paths or GitHubChangelogPathClient(session=self.session)
        self.files = files or GitHubRepositoryClient(session=self.session)

    def acquire(
        self,
        interval: DependencyReleaseInterval,
        *,
        max_releases=10,
        max_characters=20000,
    ):
        if (
            type(max_releases) is not int
            or not 1 <= max_releases <= 10
            or type(max_characters) is not int
            or max_characters <= 0
        ):
            raise ValueError(
                "Positive window bound and release budget within 1..10 required."
            )
        parsed = parse_dependency_release_interval(interval)
        if isinstance(parsed, PackagingVersionProblem):
            return AcquisitionProblem("interval", parsed.state, parsed.detail, parsed)
        index = self.index.get_release_index(interval.package)
        if not isinstance(index, PackageReleaseIndexEvidence):
            return AcquisitionProblem("index", index.state, index.detail, index)
        if index.normalized_package != interval.normalized_package:
            return AcquisitionProblem(
                "index",
                "identity_mismatch",
                "Index package differs from interval.",
                index,
            )
        selected = []
        ignored = []
        for raw in index.release_versions:
            try:
                version = Version(raw)
            except InvalidVersion:
                ignored.append(raw)
                continue
            if parsed.old_version < version <= parsed.proposed_version:
                selected.append(raw)
        ordered = order_crossed_release_versions(parsed, selected)
        if isinstance(ordered, PackagingVersionProblem):
            return AcquisitionProblem("index", ordered.state, ordered.detail, ordered)
        versions = ordered.ordered_raw_versions
        if len(versions) > max_releases:
            return AcquisitionProblem(
                "index", "release_limit", "Crossed-release budget exhausted.", index
            )
        associations = []
        for version in versions:
            release = self.releases.get_release(interval.package, version)
            if not isinstance(release, PackageReleaseEvidence):
                return AcquisitionProblem(
                    "release", release.state, release.detail, release
                )
            association = associate_declared_source(
                release, self.provenance.resolve(release)
            )
            if isinstance(association, AcquisitionProblem):
                return association
            associations.append(association)
        association = associations[-1]
        if len({a.repository.casefold() for a in associations}) != 1:
            return AcquisitionProblem(
                "association",
                "cross_release_conflict",
                "Crossed releases declare different repositories.",
                tuple(associations),
            )
        candidates = []
        tag_problems = []
        for tag in (interval.proposed_version, "v" + interval.proposed_version):
            result = self.tags.resolve_tag_to_commit(association.repository, tag)
            if isinstance(result, GitHubTagCommitEvidence):
                candidates.append(result)
            elif result.state != "source_unavailable":
                return AcquisitionProblem("tag", result.state, result.detail, result)
            else:
                tag_problems.append(result)
        if not candidates:
            return AcquisitionProblem(
                "tag", "source_unavailable", "Neither admitted exact tag was available."
            )
        if len({t.resolved_commit_sha for t in candidates}) != 1:
            return AcquisitionProblem(
                "tag",
                "ambiguous_tag",
                "Admitted tag spellings identify different commits.",
                tuple(candidates),
            )
        tag = candidates[0]
        path = self.paths.discover(association.repository, tag.resolved_commit_sha)
        if not isinstance(path, DiscoveredChangelogPath):
            return AcquisitionProblem("path", path.state, path.detail, path)
        try:
            file = self.files.get_exact_commit_text_file(
                association.repository, tag.resolved_commit_sha, path.path
            )
        except GitHubAcquisitionError as exc:
            return AcquisitionProblem("file", exc.reason, str(exc))
        except GitHubResponseError as exc:
            return AcquisitionProblem("file", "malformed_response", str(exc))
        if not isinstance(file, RepositoryTextFile):
            return AcquisitionProblem("file", file.reason, file.detail, file)
        sections = select_release_sections(
            file, versions, max_characters=max_characters
        )
        if isinstance(sections, AcquisitionProblem):
            return replace(
                sections,
                evidence=IncompleteDeclaredReleaseWindow(
                    interval,
                    tuple(associations),
                    index,
                    tuple(ignored),
                    tuple(candidates),
                    tuple(tag_problems),
                    sections.evidence,
                ),
            )
        sha = lambda text: hashlib.sha256(text.encode("utf-8")).hexdigest()
        return DeclaredReleaseWindow(
            interval,
            association,
            tuple(associations),
            index,
            tuple(ignored),
            versions,
            tuple(candidates),
            tuple(tag_problems),
            file,
            sections,
            sha(file.content),
            sha("".join(s.text for s in sections)),
        )
