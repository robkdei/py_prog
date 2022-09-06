import various_examples


def test_swap():
    assert project_one.swap(2, 4) == [4, 2]
    assert project_one.swap("Rob", "Hello") == ["Hello", "Rob"]


def test_swap_if_out_of_order():
    assert project_one.swap_if_out_of_order(4, 2) == [2, 4]
    assert project_one.swap_if_out_of_order(3, 4) == [3, 4]


def test_return_greeting():
    assert project_one.return_greeting("Rob") == "Hello, Rob"
