nums = [2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9, 10]


result = []

for n in nums:
    if n not in result:
        result.append(n)
print(result)