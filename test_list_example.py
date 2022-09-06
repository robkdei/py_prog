import list_examples


def test_list_length():
    assert list_examples.list_length(["oranges", "apples", "pears", "grapes"]) == 4


def test_slice():
    assert list_examples.slice(["oranges", "apples", "pears", "grapes"], 2, 4) == ["pears", "grapes"]
    assert list_examples.slice(["oranges", "apples", "pears", "grapes"], -4, -1) == ["oranges", "apples", "pears"]


def test_is_present():
    assert not list_examples.is_present(["oranges", "apples", "pears", "grapes"], "strawberries")
    assert list_examples.is_present(["oranges", "apples", "pears", "grapes"], "oranges")


def test_is_no_present():
    assert list_examples.is_present(["oranges", "apples", "pears", "grapes"], "strawberries")
    assert not list_examples.is_present(["oranges", "apples", "pears", "grapes"], "oranges")