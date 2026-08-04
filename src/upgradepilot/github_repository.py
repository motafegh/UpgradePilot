"""Compatibility import for exact GitHub repository-file acquisition.

New product code imports ``upgradepilot.github.repository``. This flat path remains
only while historical tests and tools migrate during source-structure reconciliation.
"""

from .github.repository import *  # noqa: F401,F403
