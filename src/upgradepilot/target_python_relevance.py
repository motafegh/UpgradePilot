"""Compatibility import for target Python relevance evaluation.

New product code imports ``upgradepilot.target.relevance``. This flat path remains only
while historical tests and tools are migrated during source-structure reconciliation.
"""

from .target.relevance import *  # noqa: F401,F403
