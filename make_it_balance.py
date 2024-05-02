# Write a function isBalanacedParentheses that gets a string of parentheses, brackets, and braces and returns True if the string is balanced, otherwise False.

# That is, every opening symbol must have a corresponding closing symbol

# Use stack to solve this problem! To solve this you will need to make an adjustment to your stack to store characters instead of integers.

 

# Examples:

# Input: "({[]})"

# Output: True

 

# Input: "({[)})]"

# Output: False

class Stack:
    def __init__(self):
        self.stack_elements = []

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

def isBalanacedParentheses(s):
    # Write code here
    stack = Stack()

    # Dictionary to store matching pairs of parentheses
    matching = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in ['(', '{', '[']:
            stack.push(char)
        elif char in [')', '}', ']']:
            if stack.empty() or stack.top() != matching[char]:
                return False
            stack.pop()

    return stack.empty()
