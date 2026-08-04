"""Compatibility imports for GitHub pull-request acquisition.

New product code imports ``upgradepilot.github.pull_request`` and
``upgradepilot.github.identity``. This flat module remains only while historical tests
and tools are migrated during source-structure reconciliation.
"""

from .github.api import GitHubAcquisitionError, GitHubResponseError
from .github.identity import UpgradePilotInputError, validate_pull_number, validate_repository
from .github.pull_request import (
    ChangedFile,
    GitHubPullRequestClient,
    GitHubReadClient,
    PullRequestIdentity,
)

__all__ = (
    "ChangedFile",
    "GitHubAcquisitionError",
    "GitHubPullRequestClient",
    "GitHubReadClient",
    "GitHubResponseError",
    "PullRequestIdentity",
    "UpgradePilotInputError",
    "validate_pull_number",
    "validate_repository",
)
