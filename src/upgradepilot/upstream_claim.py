"""Compatibility import for deterministic upstream claim grounding.

New product code imports ``upgradepilot.upstream.claim``. This flat path remains only
while historical tests and tools migrate during source-structure reconciliation.
"""

from .upstream.claim import *  # noqa: F401,F403
