nums = [1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 9, 5, 6, 90, 98]

seen = set()

result = []

for n in nums:
    if n not in seen:
        result.append(n)
        seen.add(n)

print(result)
