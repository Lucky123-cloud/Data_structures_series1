def freq_elem(nums):
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get)

# Example usage:
print(freq_elem([1, 3, 2, 1, 4, 1, 3, 1, 2, 1]))  # Output: 1