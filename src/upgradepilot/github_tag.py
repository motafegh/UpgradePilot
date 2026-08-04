"""Compatibility import for exact Git tag resolution.

New product code imports ``upgradepilot.github.tag``. This flat path remains only while
historical tests and tools migrate during source-structure reconciliation.
"""

from .github.tag import *  # noqa: F401,F403
