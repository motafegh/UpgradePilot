"""Define the intentionally supported package-level Python interface.

Focused implementations live in modules such as ``github_client.py``,
``dependency_change.py``, and ``pypi_client.py``. Re-exporting selected contracts
lets callers use stable package-level imports without depending on file layout.

Importing ``upgradepilot`` performs no network request. Acquisition starts only when
a caller invokes a client method.
"""

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
from .pypi_client import (
    PackageReleaseEvidence,
    PackageReleaseProblem,
    PackageReleaseResult,
    ProjectUrlCandidate,
    PyPIReleaseClient,
)

# ``__all__`` records the package-level contracts UpgradePilot deliberately promises.
__all__ = (
    "ChangedFile",
    "DependencyChangeResult",
    "GitHubAcquisitionError",
    "GitHubReadClient",
    "GitHubResponseError",
    "PackageReleaseEvidence",
    "PackageReleaseProblem",
    "PackageReleaseResult",
    "PinnedDependencyChange",
    "ProjectUrlCandidate",
    "PullRequestIdentity",
    "PyPIReleaseClient",
    "UnsupportedDependencyChange",
    "UpgradePilotInputError",
    "extract_pinned_dependency_change",
    "normalize_package_name",
)
