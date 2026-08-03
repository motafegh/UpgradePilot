"""Compatibility import path for exact-commit changelog discovery.

Active ownership moved to :mod:`upgradepilot.github.changelog` because the behavior is
GitHub Git-object acquisition, not provider-neutral upstream-domain interpretation.
"""

from .github.changelog import (
    ADMITTED_CHANGELOG_BASENAMES,
    ChangelogPathDiscoveryProblem,
    ChangelogPathDiscoveryProblemState,
    ChangelogPathDiscoveryResult,
    DiscoveredChangelogPath,
    GitHubChangelogPathClient,
)

__all__ = (
    "ADMITTED_CHANGELOG_BASENAMES",
    "ChangelogPathDiscoveryProblem",
    "ChangelogPathDiscoveryProblemState",
    "ChangelogPathDiscoveryResult",
    "DiscoveredChangelogPath",
    "GitHubChangelogPathClient",
)
