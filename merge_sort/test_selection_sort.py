import pytest
from selection_sort import selectionSort, smallestElem

class TestSelectionSort:
    def test_selection_sort(self):
        assert selectionSort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
        assert selectionSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        assert selectionSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert selectionSort([]) == []
        assert selectionSort([42]) == [42]
        assert selectionSort([-1, -3, -2, -5, -4]) == [-5, -4, -3, -2, -1]

    def test_smallest_elem(self):
        assert smallestElem([5, 3, 6, 2, 10]) == 3
        assert smallestElem([1, 2, 3, 4, 5]) == 0
        assert smallestElem([5, 4, 3, 2, 1]) == 4
        assert smallestElem([-1, -3, -2, -5, -4]) == 3
        assert smallestElem([42]) == 0