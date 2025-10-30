def second_largest_number(nums):
    new_sorted_nums = sorted(nums, reverse=True)
    return new_sorted_nums[1]

# Example usage:
print(second_largest_number([10, 5, 8, 12, 20]))  # Output: 12