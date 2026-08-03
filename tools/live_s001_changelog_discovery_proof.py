"""Run the Step 7A exact-commit changelog-discovery proof for S001.

This is scenario-specific validation tooling, not product orchestration. Product code
receives only repository + exact commit identity and has no Soup Sieve path constant.
The expected path below is a test oracle used to verify that the generic discovery rule
reaches the exact file previously acquired during Step 5.

The proof intentionally uses anonymous public GitHub reads so a stale optional shell
``GITHUB_TOKEN`` cannot turn an otherwise public request into an authentication failure.
"""

from __future__ import annotations

from upgradepilot.github.changelog import (
    ChangelogPathDiscoveryProblem,
    DiscoveredChangelogPath,
    GitHubChangelogPathClient,
)

_REPOSITORY = "facelessuser/soupsieve"
_COMMIT_SHA = "28108ab805818c832d9568142a99844fd95a0d39"
_EXPECTED_PATH = "docs/src/markdown/about/changelog.md"


def main() -> int:
    print("S001 live Step 7A changelog-path discovery proof")
    print(f"repository: {_REPOSITORY}")
    print(f"exact commit: {_COMMIT_SHA}")

    result = GitHubChangelogPathClient(token=None).discover(_REPOSITORY, _COMMIT_SHA)
    if isinstance(result, ChangelogPathDiscoveryProblem):
        print("\nLIVE STEP 7A PROOF: FAIL")
        print(f"state: {result.state}")
        print(f"detail: {result.detail}")
        if result.candidate_paths:
            print("candidate paths: " + ", ".join(result.candidate_paths))
        return 1

    if not isinstance(result, DiscoveredChangelogPath):
        print("\nLIVE STEP 7A PROOF: FAIL")
        print(f"unexpected result type: {type(result).__name__}")
        return 1

    print("\nDiscovered exact-commit changelog evidence:")
    print(f"  tree SHA: {result.tree_sha}")
    print(f"  path: {result.path}")
    print(f"  admitted candidate count: {len(result.candidate_paths)}")

    if result.path != _EXPECTED_PATH:
        print("\nLIVE STEP 7A PROOF: FAIL")
        print(f"expected historical S001 path: {_EXPECTED_PATH}")
        print(f"discovered path: {result.path}")
        return 1

    print("\nLIVE STEP 7A PROOF: PASS")
    print(
        "The generic exact-commit discovery rule recovered the historical S001 "
        "changelog path without a product path constant."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
