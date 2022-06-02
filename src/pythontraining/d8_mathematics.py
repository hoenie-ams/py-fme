"""
Demo of the pytest package
"""


def multiply(x, y):
    return x * y


def divide(x, y):
    return round(x / y, 1)


def round_up(x):
    rounded_up = int(x) + int((x > 0) and (x - int(x)) > 0)
    return rounded_up


def hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5
