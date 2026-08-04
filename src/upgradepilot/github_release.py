"""Compatibility import for GitHub Release acquisition.

New product code imports ``upgradepilot.github.release``. This flat path remains only
while historical tests and tools migrate during source-structure reconciliation.
"""

from .github.release import *  # noqa: F401,F403
