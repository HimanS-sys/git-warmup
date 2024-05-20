"""A test module to check mypy functionality"""

from __future__ import annotations

from dataclasses import dataclass
from typing import (  # TypedDict
    Dict,
    Generic,
    List,
    NamedTuple,
    TypeVar,
    Union,
)


class Duck:
    """
    A Class representing a duck.
    ...

    Attributes
    ----------
    name: str
        Name of the duck

    Methods
    -------
    quack : prints quack
    """

    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        """
        Returns a quack from the given duck.
        """
        print(f"{self.name}: quack!")


def consume_many_type(
    num: int,
    decimal: float,
    boolean: bool,
    binary: bytes,
    obj: object,
) -> None:
    """
    A demo function to check type hinting
    """
    print(
        f"values are\nnum:{num}\ndecimal: {decimal}\nbinary: {binary!r}\n \
        boolean: {boolean}\nobj: {obj}"
    )


duck = Duck("dodo")
duck.speak()

VAR: int = 7
# VAR = "Hi"


student_dict: Dict[str, Union[str, int]]


class Point(NamedTuple):
    """
    A class representing NamedTuple
    """

    x: int
    y: int


class LivingOrganism:
    """
    Class representing a living organism
    """


class Animal(LivingOrganism):
    """
    class representing an animal
    """


Tfriend = TypeVar("Tfriend")


@dataclass
class Student(Generic[Tfriend]):
    """
    A class demonstrating TypedDict
    """

    name: str
    age: int
    position: Point
    friends: List[Tfriend]


student_that_only_likes_animal: Student[Animal] = Student(
    name="Naveen",
    age=34,
    position=Point(9, 12),
    friends=[Animal()],
)


student = Student(
    **{  # type: ignore
        "name": "Himanshu",
        "age": 24,
        "position": Point(1, 3),
        "friends": [
            Student(
                **{  # type: ignore
                    "name": "Suresh",
                    "age": 26,
                    "position": Point(6, 8),
                    "friends": [],
                }
            )
        ],
    }
)


TstudentArgsDictKey = Union[str, int, Point, List[Student]]
print(f"student: {student}")
# print(f"x-axis: {point2d.x}")
# print(f"y-axis: {point2d.y}")

# TaddableEntity = Union[int, float, str, list, tuple]
TaddableEntity = TypeVar("TaddableEntity", int, float, str, list, tuple)

Texception = TypeVar("Texception", bound=Exception)


def raise_exception(err: Texception):
    """
    raise custom exception
    """
    raise err


def make_list_of_addable_entity(
    a: TaddableEntity, b: TaddableEntity
) -> List[TaddableEntity]:
    """
    A function demonstrating grouping of types for common operation
    """
    return [a, b]


def basic_add(a: TaddableEntity, b: TaddableEntity) -> TaddableEntity:
    """
    A function demonstrating grouping of types for common operation
    """
    return a + b


make_list_of_addable_entity(a=9, b=5)
basic_add(a="Hi", b="There!")
