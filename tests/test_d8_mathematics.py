from src.pythontraining.d8_mathematics import multiply, divide, round_up, hypotenuse


def test_multiply():
    actual = multiply(4, 5)
    expected = 20
    assert actual == expected


def test_divide():
    assert divide(4, 5) == 0.8


def test_round_up():
    assert round_up(2.3) == 3


def test_hypotenuse():
    """Returns the longest side of a right-angled triangle.

    Pythagorean Theorem: a² + b² = c²

            |\
          L | \
          e |  \ Hypotenuse (C)
          g |   \
         (A)|    \
            ------
            Leg(B)

    3² + 4² = 5²
    9  + 16 = 25
    Hypotenuse (c) = 5.0
    """
    assert hypotenuse(3, 4) == 5