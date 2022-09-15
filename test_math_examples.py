import examples_math


def test_add():
    assert examples_math.add(3, 5) == 8
    assert examples_math.add("Hello ", "World!") == "Hello World!"
    assert examples_math.add(5.6, 6.7) == 12.3
    assert examples_math.add(5.6, 6) == 11.6


def test_float_divide():
    assert examples_math.float_divide(2, 1) == 2
    assert examples_math.float_divide(3, 2) == 1.5
    assert examples_math.float_divide(1, 3) == 0.3333333333333333
    assert examples_math.float_divide(2, 3) == 0.6666666666666666
    assert examples_math.float_divide(-3, 2) == -1.5


def test_integer_divide():
    assert examples_math.integer_divide(2, 1) == 2
    assert examples_math.integer_divide(3, 2) == 1
    assert examples_math.integer_divide(1, 3) == 0
    assert examples_math.integer_divide(2, 3) == 0
    assert examples_math.integer_divide(-3, 2) == -2
