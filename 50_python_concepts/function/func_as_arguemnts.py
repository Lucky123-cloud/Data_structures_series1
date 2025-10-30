def add(a, b): return a + b
def multiply(a, b): return a * b



def operate(func, x, y):
    return func(x, y)



result1 = operate(add, 5, 3)        # Should return 8
result2 = operate(multiply, 5, 3)   # Should return 15

print(result1)  # Output: 8
print(result2)  # Output: 15