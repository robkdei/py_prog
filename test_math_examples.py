import math_examples


def test_add():
    assert math_examples.add(3, 5) == 8
    assert math_examples.add("Hello ", "World!") == "Hello World!"


def test_float_divide():
    assert math_examples.float_divide(2, 1) == 2
    assert math_examples.float_divide(3, 2) == 1.5
    assert math_examples.float_divide(1, 3) == 0.3333333333333333
    assert math_examples.float_divide(2, 3) == 0.6666666666666666
    assert math_examples.float_divide(-3, 2) == -1.5


def test_integer_divide():
    assert math_examples.integer_divide(2, 1) == 2
    assert math_examples.integer_divide(3, 2) == 1
    assert math_examples.integer_divide(1, 3) == 0
    assert math_examples.integer_divide(2, 3) == 0
    assert math_examples.integer_divide(-3, 2) == -2
