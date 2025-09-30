import pytest

from binary_search import binary_search


class TestBinarySearch:
    def test_found(self):
        arr = [1, 2, 3, 4, 5]
        target = 3
        assert binary_search(arr, target) == 2

    def test_not_found(self):
        arr = [1, 2, 3, 4, 5]
        target = 6
        assert binary_search(arr, target) == -1

    def test_empty_array(self):
        arr = []
        target = 1
        assert binary_search(arr, target) == -1

    def test_single_element_found(self):
        arr = [1]
        target = 1
        assert binary_search(arr, target) == 0

    def test_single_element_not_found(self):
        arr = [1]
        target = 2
        assert binary_search(arr, target) == -1

    def test_large_array(self):
        arr = list(range(1000000))
        target = 999999
        assert binary_search(arr, target) == 999999

    def test_negative_numbers(self):
        arr = [-10, -5, 0, 5, 10]
        target = -5
        assert binary_search(arr, target) == 1

    def test_duplicates(self):
        arr = [1, 2, 2, 2, 3]
        target = 2
        result = binary_search(arr, target)
        assert result in [1, 2, 3]