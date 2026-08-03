"""Run the bounded live Step 5 upstream-acquisition proof for scenario S001.

This file is intentionally scenario-specific validation tooling, not production product
orchestration. It exercises the real Step 5A–5C acquisition components against the
public Soup Sieve identities selected by S001, then feeds the acquired records into the
existing Step 1 authority assembler.

Data flow
---------

```text
PyPI project JSON for soupsieve
→ PackageReleaseIndexEvidence
→ select_crossed_release_index(...)
→ CrossedReleaseIndexEvidence

facelessuser/soupsieve + tag 2.8.4
→ GitHubTagCommitClient.resolve_tag_to_commit(...)
→ immutable commit SHA

immutable commit SHA + explicit changelog path
→ GitHubRepositoryClient.get_exact_commit_text_file(...)
→ ExactRepositoryTextFile
→ build_tagged_changelog_evidence(...)
→ TaggedChangelogEvidence

crossed releases + tagged changelog
→ assemble_upstream_interval_authority(...)
→ AuthoritativeUpstreamIntervalEvidence
```

The runner does not interpret changelog prose, extract the Python 3.8 support-drop
claim, read the Pydantic target declaration, alter CLI order, or make a compatibility,
safety, or maintainer-action decision.

An optional ``GITHUB_TOKEN`` environment variable may be supplied for GitHub API rate
limits. The proof uses read-only public endpoints either way.
"""

from __future__ import annotations

import os

from upgradepilot.github_api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github_repository import GitHubRepositoryClient
from upgradepilot.github_tag import GitHubTagCommitClient, GitHubTagCommitProblem
from upgradepilot.pypi_client import PackageReleaseIndexProblem, PyPIReleaseIndexClient
from upgradepilot.upstream_interval import (
    AuthoritativeUpstreamIntervalEvidence,
    DependencyReleaseInterval,
    UpstreamIntervalAuthorityProblem,
    assemble_upstream_interval_authority,
)
from upgradepilot.upstream_interval_acquisition import (
    CrossedReleaseIndexSelectionProblem,
    SelectedCrossedReleaseIndex,
    build_tagged_changelog_evidence,
    select_crossed_release_index,
)
from upgradepilot.upstream_interval import (
    TaggedChangelogEvidence,
    UpstreamAuthoritySourceProblem,
)

_PACKAGE = "soupsieve"
_REPOSITORY = "facelessuser/soupsieve"
_OLD_VERSION = "2.6"
_PROPOSED_VERSION = "2.8.4"
_REQUESTED_TAG = "2.8.4"
_CHANGELOG_PATH = "docs/src/markdown/about/changelog.md"


def main() -> int:
    """Acquire and compose the real S001 upstream interval, returning shell status."""

    interval = DependencyReleaseInterval(
        package=_PACKAGE,
        normalized_package=_PACKAGE,
        old_version=_OLD_VERSION,
        proposed_version=_PROPOSED_VERSION,
    )

    print("S001 live Step 5 upstream-acquisition proof")
    print(f"dependency interval: {_PACKAGE} {_OLD_VERSION} -> {_PROPOSED_VERSION}")

    release_index = PyPIReleaseIndexClient().get_release_index(_PACKAGE)
    if isinstance(release_index, PackageReleaseIndexProblem):
        return _fail(
            "PyPI release-index acquisition",
            release_index.state,
            release_index.detail,
        )

    selected = select_crossed_release_index(interval, _REPOSITORY, release_index)
    if isinstance(selected, CrossedReleaseIndexSelectionProblem):
        return _fail(
            "crossed-release selection",
            selected.state,
            selected.detail,
        )
    if not isinstance(selected, SelectedCrossedReleaseIndex):
        return _fail(
            "crossed-release selection",
            "unexpected_result",
            f"unexpected result type: {type(selected).__name__}",
        )

    github_token = os.environ.get("GITHUB_TOKEN") or None
    tag_result = GitHubTagCommitClient(token=github_token).resolve_tag_to_commit(
        _REPOSITORY,
        _REQUESTED_TAG,
    )
    if isinstance(tag_result, GitHubTagCommitProblem):
        return _fail(
            "Git tag-to-commit resolution",
            tag_result.state,
            tag_result.detail,
        )

    try:
        file_result = GitHubRepositoryClient(token=github_token).get_exact_commit_text_file(
            _REPOSITORY,
            tag_result.resolved_commit_sha,
            _CHANGELOG_PATH,
        )
    except (GitHubAcquisitionError, GitHubResponseError) as exc:
        return _fail(
            "exact changelog-file acquisition",
            type(exc).__name__,
            str(exc),
        )

    changelog = build_tagged_changelog_evidence(
        interval,
        tag_result,
        file_result,
    )
    if isinstance(changelog, UpstreamAuthoritySourceProblem):
        return _fail(
            "tagged-changelog composition",
            changelog.state,
            changelog.detail,
        )
    if not isinstance(changelog, TaggedChangelogEvidence):
        return _fail(
            "tagged-changelog composition",
            "unexpected_result",
            f"unexpected result type: {type(changelog).__name__}",
        )

    authority = assemble_upstream_interval_authority(
        interval,
        _REPOSITORY,
        crossed_releases=selected.evidence,
        tagged_changelogs=(changelog,),
    )
    if isinstance(authority, UpstreamIntervalAuthorityProblem):
        return _fail(
            "Step 1 interval-authority composition",
            authority.state,
            authority.detail,
        )
    if not isinstance(authority, AuthoritativeUpstreamIntervalEvidence):
        return _fail(
            "Step 1 interval-authority composition",
            "unexpected_result",
            f"unexpected result type: {type(authority).__name__}",
        )

    print("\nLIVE STEP 5 PROOF: PASS")
    print("source identities acquired by UpgradePilot:")
    print(f"  PyPI source: {selected.source_index.source_url}")
    print(
        "  crossed releases: "
        + ", ".join(selected.evidence.ordered_versions)
    )
    if selected.ignored_non_pep440_versions:
        print(
            "  ignored non-PEP-440 release keys: "
            + ", ".join(selected.ignored_non_pep440_versions)
        )
    else:
        print("  ignored non-PEP-440 release keys: none")
    print(f"  tag ref: {tag_result.tag_ref}")
    print(
        "  direct tag object: "
        f"{tag_result.tag_object_type} {tag_result.tag_object_sha}"
    )
    print(f"  resolved commit: {tag_result.resolved_commit_sha}")
    print(f"  annotated-tag peel depth: {tag_result.peel_depth}")
    print(f"  changelog path: {changelog.path}")
    print(f"  changelog blob SHA: {changelog.blob_sha}")
    print(
        "  changelog bytes: "
        f"reported={changelog.reported_byte_count}, "
        f"decoded={changelog.decoded_byte_count}"
    )
    print(f"  authority basis: {authority.authority_basis}")
    print(f"  GitHub Release bodies admitted: {len(authority.release_bodies)}")
    print("\nNo changelog semantics or target-Python relevance were evaluated.")
    return 0


def _fail(stage: str, state: str, detail: str) -> int:
    """Print one explicit live-proof failure without converting it into success."""

    print("\nLIVE STEP 5 PROOF: FAIL")
    print(f"stage: {stage}")
    print(f"state: {state}")
    print(f"detail: {detail}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
