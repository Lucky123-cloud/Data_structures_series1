# 1. Explain the difference between list.append() and list.extend().

# What does each method do internally?

# Give examples showing how they handle iterables differently.

# Bonus: What happens if you pass a string to each?



# The list.append() method adds a single element to the end of the list.
# It takes one argument, which can be of any data type, and adds it as a single item.
my_list = [1, 2, 3]
my_list.append(4)
print("After append:", my_list)  # Output: [1, 2, 3, 4]
my_list.append([5, 6])
print("After appending a list:", my_list)  # Output: [1, 2, 3, 4, [5, 6]]

# The list.extend() method takes an iterable (like a list, tuple, or string) and adds each of its elements to the end of the list.
my_list = [1, 2, 3]
my_list.extend([4, 5])
print("After extend:", my_list)  # Output: [1, 2, 3, 4, 5]
my_list.extend((6, 7))
print("After extending with a tuple:", my_list)  # Output: [1, 2, 3, 4, 5, 6, 7]


# When passing a string to each method:
my_list = ['a', 'b', 'c']
my_list.append('de')
print("After appending a string:", my_list)  # Output: ['a', 'b', 'c', 'de']
my_list = ['a', 'b', 'c']
my_list.extend('de')
print("After extending with a string:", my_list)  # Output: ['a', 'b', 'c', 'd', 'e']
# In summary:
# - list.append() adds its argument as a single element to the end of the list.
# - list.extend() iterates over its argument and adds each element to the list.


