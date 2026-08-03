"""GitHub HTTP/JSON mechanics.

Active implementation is temporarily imported from the pre-reconciliation flat module
while callers migrate to this provider-owned path. No product code should introduce
new imports of ``upgradepilot.github_api``.
"""

from ..github_api import *  # noqa: F401,F403
