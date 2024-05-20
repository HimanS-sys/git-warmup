"""
a module demonstrating how to use type hinting for code
without obvious attributes (eg: defined in __getattr__)
"""

from .type_hints import (
    Duck,  # type: ignore  # pylint: disable=relative-beyond-top-level
)

duck = Duck()
