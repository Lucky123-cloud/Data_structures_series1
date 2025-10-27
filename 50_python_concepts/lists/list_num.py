numbers = []

for i in range(1, 11):
    numbers.append(i)

print(numbers)

numbers.append(11)
print(numbers)
numbers.insert(1, 2.5)
print(numbers)
numbers.pop()
print(numbers)
numbers.remove(2.5)
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.sort(reverse=False)
print(numbers)
numbers.reverse()
print(numbers)
print(numbers[1:3])