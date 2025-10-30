def sum_two(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
            return None
        


# Example usage:
arr = [2, 7, 11, 15]
target = 9
result = sum_two(arr, target)
print(result)  # Output: (0, 1)
            