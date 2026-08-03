"""GitHub pull-request identity and complete changed-file acquisition."""

from ..github_client import (
    ChangedFile,
    GitHubAcquisitionError,
    GitHubReadClient,
    GitHubResponseError,
    PullRequestIdentity,
    UpgradePilotInputError,
    validate_pull_number,
    validate_repository,
)

# The clearer name becomes the preferred product name during the migration. The old
# class remains the same implementation so behavior does not change merely for naming.
GitHubPullRequestClient = GitHubReadClient

__all__ = (
    "ChangedFile",
    "GitHubAcquisitionError",
    "GitHubPullRequestClient",
    "GitHubResponseError",
    "PullRequestIdentity",
    "UpgradePilotInputError",
    "validate_pull_number",
    "validate_repository",
)
