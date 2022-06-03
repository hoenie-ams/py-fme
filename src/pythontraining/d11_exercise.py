"""
Decorator exercise
"""


# Exercise
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Docstring from wrapper"""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Run time was {end - start} seconds.")
        return result
    return wrapper


@timer
def do_something():
    """Toy function to keep Python busy"""
    return "-".join(str(n) for n in range(1000))


print(do_something())
print(do_something)
print(do_something.__doc__)


def func(*args, **kwargs):
    print("args", args)
    print("kwargs", kwargs)


func(1, 2, debug=True, flag=False)
