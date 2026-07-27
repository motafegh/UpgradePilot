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
from .github_release import (
    GitHubReleaseClient,
    GitHubReleaseEvidence,
    GitHubReleaseProblem,
    GitHubReleaseResult,
)
from .pypi_client import (
    DistributionFile,
    PackageReleaseEvidence,
    PackageReleaseProblem,
    PackageReleaseResult,
    ProjectUrlCandidate,
    PyPIReleaseClient,
)
from .pypi_provenance import (
    FileProvenanceEvidence,
    FileProvenanceProblem,
    FileProvenanceResult,
    PublisherIdentity,
    PyPIProvenanceClient,
)
from .upstream_source import (
    UpstreamReleaseEvidence,
    UpstreamSourceProblem,
    UpstreamSourceResolver,
    UpstreamSourceResult,
    normalize_project_url_label,
)

__all__ = (
    "ChangedFile",
    "DependencyChangeResult",
    "DistributionFile",
    "FileProvenanceEvidence",
    "FileProvenanceProblem",
    "FileProvenanceResult",
    "GitHubAcquisitionError",
    "GitHubReadClient",
    "GitHubReleaseClient",
    "GitHubReleaseEvidence",
    "GitHubReleaseProblem",
    "GitHubReleaseResult",
    "GitHubResponseError",
    "PackageReleaseEvidence",
    "PackageReleaseProblem",
    "PackageReleaseResult",
    "PinnedDependencyChange",
    "ProjectUrlCandidate",
    "PublisherIdentity",
    "PullRequestIdentity",
    "PyPIProvenanceClient",
    "PyPIReleaseClient",
    "UnsupportedDependencyChange",
    "UpgradePilotInputError",
    "UpstreamReleaseEvidence",
    "UpstreamSourceProblem",
    "UpstreamSourceResolver",
    "UpstreamSourceResult",
    "extract_pinned_dependency_change",
    "normalize_package_name",
    "normalize_project_url_label",
)
