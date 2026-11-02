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
from dataclasses import asdict, dataclass, replace
from datetime import UTC, datetime
from itertools import pairwise
from urllib.parse import urlsplit

from packaging.version import InvalidVersion, Version

from upgradepilot.dependency.versioning import (
    PackagingVersionProblem,
    order_crossed_release_versions,
    parse_dependency_release_interval,
)
from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.caller_signature.source_acquisition import (
    AcquisitionProblem, PublisherProvenanceInspection, PublisherProvenanceInspector,
    DeclaredSourceAssociation, associate_declared_source,
)
from upgradepilot.caller_signature.acquisition import (
    AcquisitionPolicy, AcquisitionSession, PYPI_TIMEOUT_RETRY_POLICY,
)
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


# Historical names and trial receipt formats stay experimental. The charged
# implementation lives in the product; this adapter does not own a second ledger.
TrialAcquisitionPolicy = AcquisitionPolicy


class TrialPublicSession(AcquisitionSession):
    """Compatibility for historical trial callers, not a product invocation API.

    Old no-policy trials retained only the 50-GitHub-request guard. Keep that
    separate legacy route here; new product acquisition requires explicit policy.
    Frozen result files retain their original formats/reasons/source hashes.
    """

    request_limit_reason = "trial_request_limit"

    def __init__(self, *, token=None, policy=None, clock=time.monotonic,
                 retry_pypi_timeouts=False):
        if retry_pypi_timeouts and policy is None:
            raise ValueError("Timeout recovery requires an explicit charged policy.")
        super().__init__(token=token, policy=policy or AcquisitionPolicy(), clock=clock,
                         retry_pypi_timeouts=retry_pypi_timeouts)
        self.policy = policy

    def _refuse(self, reason):
        historical = {
            "acquisition_request_limit": "trial_request_limit",
            "acquisition_stage_request_limit": "trial_stage_request_limit",
            "acquisition_deadline": "trial_acquisition_deadline",
            "acquisition_provider_request_limit": "trial_provider_request_limit",
            "acquisition_aggregate_body_limit": "trial_aggregate_body_limit",
            "acquisition_response_body_limit": "trial_response_body_limit",
        }.get(reason, reason)
        if reason == "acquisition_request_limit":
            self.request_limit_reached = True
        super()._refuse(historical)

    def finish_acquisition(self):
        if self.policy is not None:
            super().finish_acquisition()

    def acquisition_receipt(self):
        if self.policy is None:
            return None
        native = super().acquisition_receipt()
        receipt = dict(format="trial-acquisition-policy/1", limits=asdict(self.policy), auth=native.auth,
                       github_requests=native.github_requests, provider_requests=native.provider_requests,
                       decoded_body_bytes=native.decoded_body_bytes, elapsed_seconds=native.elapsed.seconds,
                       deadline_kind=native.deadline_kind, stops=[asdict(x) for x in native.stops],
                       requests=[asdict(x) for x in native.requests])
        if self.retry_pypi_timeouts:
            receipt.update(format="trial-acquisition-policy/2", retry_policy=dict(PYPI_TIMEOUT_RETRY_POLICY),
                           retry_decisions=[asdict(x) for x in native.retry_decisions])
        return receipt

    def _request_once(self, method, url, **kwargs):
        if self.policy is not None:
            return super()._request_once(method, url, **kwargs)
        host = self._request_host(method, url)
        if host == "api.github.com":
            if self.github_requests >= 50:
                self._refuse("acquisition_request_limit")
            self.github_requests += 1
        # Preserve the pre-policy trial route; all native invocations use the
        # product's charged path, shared scope check and credential confinement.
        headers = kwargs.get("headers", {})
        if host != "api.github.com" or self._github_token:
            headers = self._request_headers(host, headers)
        kwargs.update(headers=headers, allow_redirects=False)
        return super(AcquisitionSession, self).request(method, url, **kwargs)


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
