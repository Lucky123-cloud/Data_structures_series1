# Stack Class

# The Stack data structure we will create, will store only integers.

# Every time you create a data structure, you should decide how to handle the elements of the data structure internally.

# The most popular way is with an array, but there are many ways that differ from one programming language to another.

# During this project, we will take you hand in hand while creating the Stack class, but you will need to decide how to implement everything internally.

# If you are stuck don't hesitate to use our support for help!


# Challenge

# Easy
# Write a class Stack with a constructor that gets no input.

# In the constructor initialize class variable that will hold the stack elements, start from an empty array.


class Stack:

    def __init__(self):
        #write code here
        self.stack_elements = [];

# Add to Stack a method called push that gets an integer and pushes the integer to the top of the stack

    def push(self, item):
        self.stack_elements.append(item)

# Add to Stack a method called top that gets no arguments and returns the integer on the top of the stack.
    def top(self):
        if self.stack_elements:
            return self.stack_elements[-1]
        else:
            return None
        
# Add to Stack a method called pop that gets no arguments, the function will remove the integer on the top of the stack and returns it.
    def pop(self):
        if self.stack_elements:
            return self.stack_elements.pop()
        else:
            return None
        
# Add to Stack a method called size that gets no arguments and returns the number of elements currently in the stack.

    def size(self):
        return len(self.stack_elements)
    
# Add to Stack a method called empty that gets no arguments and returns true if the stack is empty, otherwise false.

    def empty(self):
        return len(self.stack_elements) == 0


# testing in order of instruction
my_stack = Stack()
my_stack.push(3)
my_stack.push(5)
print(my_stack.top())
my_stack.pop()
print(my_stack.size())
print(my_stack.empty())