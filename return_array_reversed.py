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
    

    # here is the solution
def reversed(arr):
    stack = Stack()

    # create an empty array for storing the items from arr
    reversed_arr = [] 

    # put the items from arr in the stack using push method defined earlier
    for item in arr:
        stack.push(item)

    # remove them putting them in the empty array created ealier
    while not stack.empty():
        reversed_arr.append(stack.pop())
    
    # return the filled array
    return reversed_arr

# Write a function nse that gets an integer array and returns an array that contains the nearest smaller element of each element (to the left). If there is no smaller element to the left of an element, return -1.

# Use stack to solve this problem!

def nse(n):
    stack2 = Stack()
    result = []

    for num in n:
        while not stack2.empty and stack2.top >= num:
            stack2.pop()

        if stack2.empty():
            result.append(-1)
        else:
            result.append(stack2.top())
        stack2.push(num)
    return result
