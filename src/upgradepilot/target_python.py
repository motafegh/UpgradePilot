"""Compatibility import for target Python declaration interpretation.

New product code imports ``upgradepilot.target.python``. This flat path remains only
while historical tests and tools are migrated during source-structure reconciliation.
"""

from .target.python import *  # noqa: F401,F403
