"Module for practicing type-hinting"


class Duck:
    """
    class representing duck
    """

    def __init__(self) -> None: ...

    def __getattr__(self, attr: str):
        if attr == "quack":
            return lambda: print("quack!")
        if attr == "swim":
            return lambda: print("splash!!")
        raise AttributeError


duck = Duck()
