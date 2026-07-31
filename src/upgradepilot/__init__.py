"""Define the intentionally supported package-level Python interface.

Focused implementations live in modules such as ``github_client.py``,
``dependency_change.py``, ``exact_requirement_change.py``, ``uv_lock_change.py``, and
``pypi_client.py``. Re-exporting selected contracts lets callers use stable
package-level imports without depending on file layout.

Importing ``upgradepilot`` performs no network request. Acquisition starts only when a
caller invokes a client method.
"""

from .dependency_change import (
    DEPENDENCY_CHANGE_PROBLEM_CODES,
    DependencyChangeComparisonResult,
    DependencyChangeEvidenceProblem,
    DependencyChangeExtractionResult,
    DependencyChangeProblemCode,
    DependencyChangeResult,
    DependencyEvidenceMethod,
    DependencyFileEvidence,
    DependencyFileFormat,
    DependencyVersionChange,
    ExtractedDependencyVersionChange,
    PinnedDependencyChange,
    UnsupportedDependencyChange,
    compare_extracted_dependency_changes,
    extract_pinned_dependency_change,
    normalize_package_name,
)
from .exact_requirement_change import (
    extract_exact_requirement_changes,
    is_exact_requirement_file,
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
from .uv_lock_change import (
    extract_uv_lock_changes,
    is_modified_uv_lock_file,
)

__all__ = (
    "ChangedFile",
    "DEPENDENCY_CHANGE_PROBLEM_CODES",
    "DependencyChangeComparisonResult",
    "DependencyChangeEvidenceProblem",
    "DependencyChangeExtractionResult",
    "DependencyChangeProblemCode",
    "DependencyChangeResult",
    "DependencyEvidenceMethod",
    "DependencyFileEvidence",
    "DependencyFileFormat",
    "DependencyVersionChange",
    "DistributionFile",
    "ExtractedDependencyVersionChange",
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
    "compare_extracted_dependency_changes",
    "extract_exact_requirement_changes",
    "extract_pinned_dependency_change",
    "extract_uv_lock_changes",
    "is_exact_requirement_file",
    "is_modified_uv_lock_file",
    "normalize_package_name",
    "normalize_project_url_label",
)
