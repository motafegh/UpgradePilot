"""Define the intentionally supported package-level Python interface.

Purpose of this file
--------------------
Internal implementations live in focused modules such as ``github_client.py`` and
``dependency_change.py``. This file re-exports selected contracts so library callers
can write:

``from upgradepilot import GitHubReadClient, PinnedDependencyChange``

without depending on the internal file layout.

What is public here
-------------------
The current package-level surface exposes the first PR/dependency evidence stage:

* input, acquisition, and response error contracts;
* immutable PR and changed-file records;
* the read-only PR client;
* supported/unsupported dependency interpretation records and functions.

CI-specific clients and evaluators are still imported from their focused modules.
Not re-exporting every implementation keeps the package interface deliberate and
allows internal organization to evolve without promising every helper as public API.

Importing ``upgradepilot`` executes these imports but performs no GitHub requests.
Network activity begins only when a caller creates a client and invokes its methods.
"""

# Relative imports use the leading dot to resolve modules inside this package. Without
# it, Python would search for unrelated top-level modules named ``dependency_change``
# or ``github_client``.
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

# ``__all__`` is the explicit package-level export inventory used by
# ``from upgradepilot import *`` and by documentation/readers discovering the intended
# API. It does not enforce secrecy; names in internal modules remain technically
# importable, but they are not promised here as stable package-level contracts.
#
# A tuple is used because this inventory is fixed at import time and should not be
# mutated by ordinary callers.
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
