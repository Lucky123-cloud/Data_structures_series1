# 3. What happens if you multiply a list, e.g., a = [[0]*3]*3?

# What is the output?

# Why might modifying one element affect all rows?

# How would you fix it so each sublist is independent?     


a = [[0] * 3] * 3

print(a)

a[0][0] = 1
print(a)  # all the rows are changed because they reference the same inner list

b = [[0] * 3 for _ in range(3)]
print(b)

b[0][0] = 1
print(b)  # only the first row is changed because each inner list is a different object