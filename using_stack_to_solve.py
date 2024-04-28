# Practice #1

# The next challenges are designed to use stack in them.

# Copy the Stack code you made in the previous lessons and use it here! 


# Challenge

# Easy
# Write a function reverse that gets an integer array as input (a) and returns the reversed array.

# Use stack to solve this problem!


# Hints

# Hint 1
# Revealed

# First, fill the stack with all the elements from the array, after pop them all into a new array!

# Remember! In a stack - last in, first out (LIFO), so you get the reversed order.


class Stack:
    def __init__(self):
        # Writing our code here
        self.stack_elements = [];
        
    def push(self, item):
        self.stack_elements.append(item)
        
    def top(self):
        if self.stack_elements:
            return self.stack_elements[-1]
        else:
            return None
            
    def pop(self):
        if self.stack_elements:
            return self.stack_elements.pop()
        else:
            return None
            
    def size(self):
        return len(self.stack_elements)
        
    def empty(self):
        return len(self.stack_elements) == 0
    
def reversed(arr):
    stack = Stack()
    reversed_arr = []

    for item in arr:
        stack.push(item)

    while not stack.empty():
        reversed_arr.append(stack.pop())
    
    return reversed_arr