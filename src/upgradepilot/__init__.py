"""Define UpgradePilot's current public Python package interface.

Importing selected names here lets callers use ``upgradepilot.Name`` instead of
knowing which internal module owns each implementation. This file should remain
small: re-export only intentionally public contracts, not every internal helper.
"""

# Relative imports (the leading dot) resolve modules inside this package rather
# than searching for unrelated top-level modules with the same names.
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

# ``__all__`` documents the supported star-import surface and gives readers one
# explicit inventory of the package-level API. It does not make private names
# secure; the leading underscore convention and module boundaries still matter.
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
