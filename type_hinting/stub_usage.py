" type hinting for code without obvious attributes "

from .type_hints import Duck  # type: ignore # pylint: disable=relative-beyond-top-level

duck = Duck()
