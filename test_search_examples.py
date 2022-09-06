import search_examples


def test_linear_search():
    assert search.linear(["Jett", "Brimstone", "Phoenix", "Fade", "Sage"], "Fade") == 3
    assert search.linear([10, 15, 100, 2, 34], 34) == 4


def test_binary_search():
    assert search.binary(["Brimstone", "Fade", "Jett", "Phoenix", "Sage"], "Fade") == 1
    assert search.binary([10, 15, 100, 304, 800], 15) == 1
    assert search.binary([10, 15, 100, 304, 800], 800) == 4


def test_binary_search_with_unsorted_lists():
    assert search.binary(["Fade", "Brimstone", "Phoenix", "Sage", "Phoenix"], "Sage") == 3
    assert search.binary([15, 304, 10, 800, 100], 800) == 3


def test_find_max():
    assert search.find_max([15, 304, 10, 800, 100])