# we can copy a list, but we have to be careful

# for instance

numbers = [1, 2, 3, 4, 5]

numbers2 = numbers

numbers2.append(6)
print(numbers)
print(numbers2)  #both the lists have the same refences - that means, we the list is the same, we can avoid this, here is how


numbers3 = numbers.copy() #we use the copy() method to create a new list - this is called shallow copy

numbers3.append(7)
print(numbers)
print(numbers3)  # now the lists are different

# another way to copy a list is to use the list() function
numbers4 = list(numbers)
numbers4.append(8)
print(numbers)
print(numbers4)  # now the lists are different


# another way to copy a list is to use slicing
numbers5 = numbers[:]
numbers5.append(9)
print(numbers)
print(numbers5)  # now the lists are different

# all the three methods create a shallow copy of the list
# if the list contains mutable objects, then the references to those objects are copied, not the objects themselves
# for example
list_of_lists = [[1, 2], [3, 4]]
list_of_lists_copy = list_of_lists.copy()
list_of_lists_copy[0].append(5)
print(list_of_lists)  # both lists reflect the change
print(list_of_lists_copy)  # both lists reflect the change
