"""Connect ``python -m upgradepilot`` to the command-line orchestrator.

When Python executes a package with ``-m``, it looks for that package's
``__main__.py`` and executes it as the program entry point. This adapter stays tiny:
all argument parsing, acquisition, interpretation, output, and exit-code policy live
in ``cli.main`` rather than being duplicated here.
"""

from .cli import main

# ``main`` returns an integer process status. Raising ``SystemExit`` gives that value
# to the operating system or calling shell. It also prevents this adapter from silently
# discarding non-zero failure statuses returned by ``cli.py``.
raise SystemExit(main())
