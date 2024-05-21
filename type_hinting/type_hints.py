"""Module for practicing type-hinting."""


class Duck:
    """Class representing duck."""

    def __init__(self) -> None:
        """Initialize the class."""

    def __getattr__(self, attr: str):
        """Return result based on the attribute called."""
        if attr == "quack":
            return lambda: print("quack!quack!")
        if attr == "swim":
            return lambda: print("splash!!")
        raise AttributeError


duck = Duck()
