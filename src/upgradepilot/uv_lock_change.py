"""Compatibility import for ``uv.lock`` dependency extraction.

New product code imports ``upgradepilot.dependency.uv_lock``. This flat path remains
only while historical tests and tools migrate during source-structure reconciliation.
"""

from .dependency.uv_lock import *  # noqa: F401,F403
