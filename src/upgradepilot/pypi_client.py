"""Compatibility import for PyPI release and release-index acquisition.

New product code imports ``upgradepilot.pypi.release``. This flat path remains only
while historical tests and tools migrate during source-structure reconciliation.
"""

from .pypi.release import *  # noqa: F401,F403
