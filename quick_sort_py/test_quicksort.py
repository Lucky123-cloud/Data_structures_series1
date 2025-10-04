import pytest
from quicksort import quicksort

class TestQuickSort:
    def test_empty_array(self):
        assert quicksort([]) == []

    def test_single_element(self):
        assert quicksort([1]) == [1]

    def test_sorted_array(self):
        assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_array(self):
        assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_unsorted_array(self):
        assert quicksort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]

    def test_array_with_duplicates(self):
        assert quicksort([3, 6, 8, 3, 2, 1, 6]) == [1, 2, 3, 3, 6, 6, 8]

    def test_negative_numbers(self):
        assert quicksort([-3, -1, -7, -4]) == [-7, -4, -3, -1]

    def test_mixed_numbers(self):
        assert quicksort([3, -2, -5, 0, 4]) == [-5, -2, 0, 3, 4]