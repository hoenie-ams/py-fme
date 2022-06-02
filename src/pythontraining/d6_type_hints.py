"""
Demo of type hints
"""
from __future__ import annotations
from typing import Optional, List, Dict, Union

var: int | str = 1  # new syntax available in 3.10

a: int = 42
b: float = 3.14
c: bool = True
d: str = "hello world"


def add(x: int, y: int) -> int:
    return x + y


print(add(4, 5))
print(add(6, "7"))


def greet(name: Optional[str] = None):
    if name is None:
        name = "stranger"
    return "hello " + name


e: list[int] = [1, 2, 3]
f: dict[str, float] = {"location": 4.8, "service": 5.0, "quality": 4.7}
g: Union[int, str, float] = 1.0
h: List[Union[int, str]] = [1, 2, "c", "d"]


class MyClass:
    value: int = 42

    def add(self, x: int, y: int) -> int:
        return x + y
