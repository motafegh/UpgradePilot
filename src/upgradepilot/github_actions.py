"""Compatibility import for GitHub Actions acquisition.

New product code imports ``upgradepilot.github.actions``. This flat path remains only
while historical tests and tools migrate during source-structure reconciliation.
"""

from .github.actions import *  # noqa: F401,F403
