import examples_various


def test_swap():
    assert examples_various.swap(2, 4) == [4, 2]
    assert examples_various.swap("Rob", "Hello") == ["Hello", "Rob"]


def test_swap_if_out_of_order():
    assert examples_various.swap_if_out_of_order(4, 2) == [2, 4]
    assert examples_various.swap_if_out_of_order(3, 4) == [3, 4]


def test_return_greeting():
    assert examples_various.return_greeting("Rob") == "Hello, Rob"
