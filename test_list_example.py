import examples_list


def test_list_length():
    assert examples_list.list_length(["oranges", "apples", "pears", "grapes"]) == 4


def test_slice():
    assert examples_list.slice(["oranges", "apples", "pears", "grapes"], 2, 4) == ["pears", "grapes"]
    assert examples_list.slice(["oranges", "apples", "pears", "grapes"], -4, -1) == ["oranges", "apples", "pears"]


def test_is_present():
    assert not examples_list.is_present(["oranges", "apples", "pears", "grapes"], "strawberries")
    assert examples_list.is_present(["oranges", "apples", "pears", "grapes"], "oranges")


def test_is_no_present():
    assert examples_list.is_present(["oranges", "apples", "pears", "grapes"], "strawberries")
    assert not examples_list.is_present(["oranges", "apples", "pears", "grapes"], "oranges")