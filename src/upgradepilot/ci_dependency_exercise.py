"""Compatibility import for dependency CI-exercise interpretation.

New product code imports ``upgradepilot.ci.dependency_exercise``. This flat path remains
only while historical tests and tools migrate during source-structure reconciliation.
"""

from .ci.dependency_exercise import *  # noqa: F401,F403
