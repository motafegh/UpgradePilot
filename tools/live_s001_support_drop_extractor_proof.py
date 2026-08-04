"""Run a live S001 proof through the current Step 7B + Step 7C product path.

This is developer validation tooling, not product orchestration. It reacquires the real
public Soup Sieve evidence for S001, builds the deterministic crossed-release Markdown
window with product code, invokes the adopted local LM Studio extractor with product
code, and then passes the untrusted candidate result through the existing deterministic
claim validator.

Data flow
---------

```text
PyPI release index
→ trusted crossed-release interval
→ exact Soup Sieve 2.8.4 tag commit
→ exact-commit changelog-path discovery
→ exact tagged changelog
→ Step 7B CrossedReleaseSourceWindow
→ Step 7C LocalSupportDropExtractor (LM Studio / gemma-4-e4b-it-ud)
→ CandidateUpstreamClaimResult (untrusted)
→ validate_support_drop_candidates(...)
→ grounded claim or explicit problem
```

The tool intentionally uses anonymous public GitHub reads. It does not inspect the
Pydantic target declaration, decide target relevance, claim compatibility/safety, or
make a maintainer recommendation.
"""

from __future__ import annotations

from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github.changelog import (
    ChangelogPathDiscoveryProblem,
    GitHubChangelogPathClient,
)
from upgradepilot.github.repository import GitHubRepositoryClient
from upgradepilot.github.tag import GitHubTagCommitClient, GitHubTagCommitProblem
from upgradepilot.pypi.release import PackageReleaseIndexProblem, PyPIReleaseIndexClient
from upgradepilot.upstream.changelog import (
    CrossedReleaseSourceWindow,
    CrossedReleaseSourceWindowProblem,
    build_crossed_release_source_window,
)
from upgradepilot.upstream.claim import (
    GroundedPythonSupportDropClaim,
    UpstreamSupportDropClaimProblem,
    validate_support_drop_candidates,
)
from upgradepilot.upstream.interval import (
    AuthoritativeUpstreamIntervalEvidence,
    DependencyReleaseInterval,
    TaggedChangelogEvidence,
    UpstreamAuthoritySourceProblem,
    UpstreamIntervalAuthorityProblem,
    assemble_upstream_interval_authority,
)
from upgradepilot.upstream.interval_evidence import (
    CrossedReleaseIndexSelectionProblem,
    SelectedCrossedReleaseIndex,
    build_tagged_changelog_evidence,
    select_crossed_release_index,
)
from upgradepilot.upstream.support_drop_extractor import (
    ADOPTED_MODEL_ID,
    LM_STUDIO_BASE_URL,
    MAX_SOURCE_WINDOW_CHARACTERS,
    LocalSupportDropExtractor,
)

_PACKAGE = "soupsieve"
_REPOSITORY = "facelessuser/soupsieve"
_OLD_VERSION = "2.6"
_PROPOSED_VERSION = "2.8.4"
_REQUESTED_TAG = "2.8.4"
_EXPECTED_PYTHON_LINE = "3.8"
_EXPECTED_INTRODUCED_VERSION = "2.8"


def main() -> int:
    """Reacquire S001 and run one real local semantic extraction."""

    interval = DependencyReleaseInterval(
        package=_PACKAGE,
        normalized_package=_PACKAGE,
        old_version=_OLD_VERSION,
        proposed_version=_PROPOSED_VERSION,
    )

    print("S001 live Step 7C semantic-extractor proof")
    print(f"dependency interval: {_PACKAGE} {_OLD_VERSION} -> {_PROPOSED_VERSION}")
    print(f"local provider: {LM_STUDIO_BASE_URL}")
    print(f"model: {ADOPTED_MODEL_ID}")
    print("automatic retries: disabled")

    release_index = PyPIReleaseIndexClient().get_release_index(_PACKAGE)
    if isinstance(release_index, PackageReleaseIndexProblem):
        return _fail("PyPI release-index acquisition", release_index.state, release_index.detail)

    selected = select_crossed_release_index(interval, _REPOSITORY, release_index)
    if isinstance(selected, CrossedReleaseIndexSelectionProblem):
        return _fail("crossed-release selection", selected.state, selected.detail)
    if not isinstance(selected, SelectedCrossedReleaseIndex):
        return _fail(
            "crossed-release selection",
            "unexpected_result",
            f"unexpected result type: {type(selected).__name__}",
        )

    tag_result = GitHubTagCommitClient(token=None).resolve_tag_to_commit(
        _REPOSITORY,
        _REQUESTED_TAG,
    )
    if isinstance(tag_result, GitHubTagCommitProblem):
        return _fail("Git tag-to-commit resolution", tag_result.state, tag_result.detail)

    discovered = GitHubChangelogPathClient(token=None).discover(
        _REPOSITORY,
        tag_result.resolved_commit_sha,
    )
    if isinstance(discovered, ChangelogPathDiscoveryProblem):
        return _fail("exact-commit changelog discovery", discovered.state, discovered.detail)

    try:
        file_result = GitHubRepositoryClient(token=None).get_exact_commit_text_file(
            _REPOSITORY,
            tag_result.resolved_commit_sha,
            discovered.path,
        )
    except (GitHubAcquisitionError, GitHubResponseError) as exc:
        return _fail("exact changelog-file acquisition", type(exc).__name__, str(exc))

    changelog = build_tagged_changelog_evidence(interval, tag_result, file_result)
    if isinstance(changelog, UpstreamAuthoritySourceProblem):
        return _fail("tagged-changelog composition", changelog.state, changelog.detail)
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
        return _fail("interval-authority composition", authority.state, authority.detail)
    if not isinstance(authority, AuthoritativeUpstreamIntervalEvidence):
        return _fail(
            "interval-authority composition",
            "unexpected_result",
            f"unexpected result type: {type(authority).__name__}",
        )

    window = build_crossed_release_source_window(
        selected.evidence,
        changelog,
        max_characters=MAX_SOURCE_WINDOW_CHARACTERS,
    )
    if isinstance(window, CrossedReleaseSourceWindowProblem):
        return _fail("Step 7B source-window construction", window.state, window.detail)
    if not isinstance(window, CrossedReleaseSourceWindow):
        return _fail(
            "Step 7B source-window construction",
            "unexpected_result",
            f"unexpected result type: {type(window).__name__}",
        )

    print("\nReacquired trusted source context:")
    print("  crossed releases: " + ", ".join(window.trusted_ordered_versions))
    print(f"  exact commit: {window.resolved_commit_sha}")
    print(f"  changelog path: {window.path}")
    print(f"  changelog blob: {window.blob_sha}")
    print("  source-order sections: " + ", ".join(window.source_ordered_versions))
    print(
        "  bounded window: "
        f"{window.character_count}/{window.max_characters} characters"
    )

    candidate_result = LocalSupportDropExtractor().extract(window)

    print("\nActual Step 7C model result after deterministic reconstruction:")
    print(f"  state: {candidate_result.state}")
    print(f"  detail: {candidate_result.detail or 'none'}")
    print(f"  candidates: {len(candidate_result.candidates)}")
    for index, candidate in enumerate(candidate_result.candidates, start=1):
        print(f"  candidate {index}:")
        print(f"    python_line: {candidate.python_line}")
        print(f"    introduced_in_version: {candidate.introduced_in_version}")
        print(f"    source_kind: {candidate.source_kind}")
        print(f"    source_quote: {candidate.source_quote}")
        print(f"    exact offsets: {candidate.quote_start}:{candidate.quote_end}")

    trust_result = validate_support_drop_candidates(authority, candidate_result)
    print("\nDeterministic trust admission:")
    if isinstance(trust_result, UpstreamSupportDropClaimProblem):
        print(f"  state: {trust_result.state}")
        print(f"  detail: {trust_result.detail}")
        return _fail(
            "deterministic claim admission",
            trust_result.state,
            trust_result.detail,
            print_header=False,
        )

    if not isinstance(trust_result, GroundedPythonSupportDropClaim):
        return _fail(
            "deterministic claim admission",
            "unexpected_result",
            f"unexpected result type: {type(trust_result).__name__}",
            print_header=False,
        )

    print("  state: grounded")
    print(f"  python_line: {trust_result.python_line}")
    print(f"  introduced_in_version: {trust_result.introduced_in_version}")
    print(f"  grounded sources: {len(trust_result.source_evidence)}")

    if (
        trust_result.python_line != _EXPECTED_PYTHON_LINE
        or trust_result.introduced_in_version != _EXPECTED_INTRODUCED_VERSION
    ):
        return _fail(
            "S001 expected bounded outcome",
            "unexpected_grounded_claim",
            (
                "Expected Python 3.8 support drop introduced in 2.8, got "
                f"Python {trust_result.python_line} in "
                f"{trust_result.introduced_in_version}."
            ),
            print_header=False,
        )

    print("\nLIVE STEP 7C PROOF: PASS")
    print("bounded result: Python 3.8 support drop introduced in Soup Sieve 2.8")
    print("No target-Python relevance, compatibility, safety, or merge claim was made.")
    return 0


def _fail(
    stage: str,
    state: str,
    detail: str,
    *,
    print_header: bool = True,
) -> int:
    if print_header:
        print("\nLIVE STEP 7C PROOF: FAIL")
    else:
        print("\nLIVE STEP 7C PROOF: FAIL")
    print(f"stage: {stage}")
    print(f"state: {state}")
    print(f"detail: {detail}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
