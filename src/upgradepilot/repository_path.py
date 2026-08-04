"""Own source-neutral repository-relative POSIX path validation.

Several UpgradePilot responsibilities inspect paths already reported as repository
paths. They need the same small structural rule: a path must be relative, use POSIX
``/`` separators, contain no empty components, and contain no ``.`` or ``..`` traversal
components.

Provider- or role-specific meaning stays with the caller. For example, this module does
not decide whether a path is a requirements file, ``uv.lock``, a workflow, or a
changelog.
"""

from __future__ import annotations


def repository_relative_parts(path: str) -> tuple[str, ...] | None:
    """Return validated repository-relative POSIX components or ``None``.

    The function preserves exact component spelling. It validates only structural path
    form and does not normalize case, collapse components, or assign source meaning.
    """

    if not isinstance(path, str) or not path or path.startswith("/") or "\\" in path:
        return None

    parts = tuple(path.split("/"))
    if any(not part or part in {".", ".."} for part in parts):
        return None
    return parts
