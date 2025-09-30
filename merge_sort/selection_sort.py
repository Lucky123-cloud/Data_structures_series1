def smallestElem(arr):
    smallest = arr[0]
    smallest_index = 0


    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = smallestElem(arr)
        newArr.append(arr.pop(smallest))
    return newArr



# time complexity O(n^2)
# space complexity O(n)
# selection sort is not a stable sort



