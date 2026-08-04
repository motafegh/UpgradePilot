"""Compatibility import for PyPI HTTP/JSON mechanics.

New product code imports ``upgradepilot.pypi.api``. This flat path remains only while
historical tests and tools migrate during source-structure reconciliation.
"""

from .pypi.api import *  # noqa: F401,F403
