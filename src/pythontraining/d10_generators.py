"""
Demo of generators
"""

for x in [1, 2, 3]:
    print(x)


class MyCounter:
    def __init__(self, start=0):
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        value = self.value
        self.value += 1
        return value


counter = MyCounter()


def my_generator():
    a = "going first"
    yield a
    b = "going second"
    yield b


gen = my_generator()


def my_counter(n=0):
    while True:
        yield n
        n += 1


counter_gen = my_counter()

import sys
list_comp = [x for x in range(1000000)]
generator = (x for x in range(1000000))
print(sys.getsizeof(list_comp))
print(sys.getsizeof(generator))

