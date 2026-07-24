"""UpgradePilot active package."""

from .dependency_change import (
    DependencyChangeResult,
    PinnedDependencyChange,
    UnsupportedDependencyChange,
    extract_pinned_dependency_change,
    normalize_package_name,
)
from .github_client import (
    ChangedFile,
    GitHubAcquisitionError,
    GitHubReadClient,
    GitHubResponseError,
    PullRequestIdentity,
    UpgradePilotInputError,
)

__all__ = (
    "ChangedFile",
    "DependencyChangeResult",
    "GitHubAcquisitionError",
    "GitHubReadClient",
    "GitHubResponseError",
    "PinnedDependencyChange",
    "PullRequestIdentity",
    "UnsupportedDependencyChange",
    "UpgradePilotInputError",
    "extract_pinned_dependency_change",
    "normalize_package_name",
)
