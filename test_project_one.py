import project_one


def test_add():
    assert project_one.add(3, 5) == 8


def test_swap():
    assert project_one.swap(2, 4) == [4, 2]


def test_swap_if_out_of_order():
    assert project_one.swap_if_out_of_order(4, 2) == [2, 4]
    assert project_one.swap_if_out_of_order(3, 4) == [3, 4]


def test_sublist():
    assert project_one.sublist(["oranges", "apples", "pears", "grapes"], 2, 4) == ["pears", "grapes"]


def test_is_present():
    assert not project_one.is_present(["oranges", "apples", "pears", "grapes"], "strawberries")
    assert project_one.is_present(["oranges", "apples", "pears", "grapes"], "oranges")
