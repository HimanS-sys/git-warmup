"Module for practicing type-hinting"


class Duck:
    """
    class representing duck
    """
    def __init__(self) -> None:
        ...

    def __getattr__(self, attr: str):
        if attr == "quack":
            return lambda: print("quack!")
        elif attr == "swim":
            return lambda: print("splash!!")
        else:
            raise AttributeError


duck = Duck()
