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