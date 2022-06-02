"""
Demo of type hints
"""
from typing import Optional, List, Dict, Union

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


e: List[int] = [1, 2, 3]
f: Dict[str, float] = {"location": 4.8, "service": 5.0, "quality": 4.7}
g: Union[int, str, float] = 1.0
h: List[Union[int, str]] = [1, 2, "c", "d"]


class MyClass:
    value: int = 42

    def add(self, x: int, y: int) -> int:
        return x + y
