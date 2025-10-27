from copy import deepcopy

nums = [[1, 2], [3, 4]]

shallow_copied_nums = nums.copy()
deep_copied_nums = deepcopy(nums)


print("Before modification:")
print("Original:", nums)
print("Shallow Copy:", shallow_copied_nums)
print("Deep Copy:", deep_copied_nums)

shallow_copied_nums[0].append(5)
deep_copied_nums[1].append(6)
print("\nAfter modification:")
print("Original:", nums)
print("Shallow Copy:", shallow_copied_nums)
print("Deep Copy:", deep_copied_nums)
# In this example, modifying the shallow copy affects the original list,
# while modifying the deep copy does not.
# This demonstrates the difference between shallow and deep copies.

