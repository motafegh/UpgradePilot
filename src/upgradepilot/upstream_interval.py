"""Compatibility import for upstream interval authority contracts.

New product code imports ``upgradepilot.upstream.interval``. This flat path remains only
while historical tests and tools migrate during source-structure reconciliation.
"""

from .upstream.interval import *  # noqa: F401,F403
