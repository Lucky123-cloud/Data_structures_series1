def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot]  + quicksort(greater)
    

if __name__ == "__main__":
    sample_array = [10, 5, 2, 3]
    print("Unsorted array:", sample_array)
    sorted_array = quicksort(sample_array)
    print("Sorted array:", sorted_array)

# time complexity O(n log n) on average, O(n^2) in the worst case
# space complexity O(log n) due to recursive stack space

