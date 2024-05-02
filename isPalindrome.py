# Write a function isPalindrome that gets a string and returns True if the string is a palindrome, otherwise False.

# Palindrome is a word or phrase that reads same backward as forward.

# Use stack to solve this problem!

class Stack:
    def __init__(self):
        self.stack_elements = []

    def push(self, item):
        self.stack_elements.append(item)

    def pop(self):
        if self.stack_elements:
            return self.stack_elements.pop()
        else:
            return None

    def empty(self):
        return len(self.stack_elements) == 0

def isPalindrome(s):
    stack = Stack()
    n = len(s)

    # Push the first half of characters onto the stack
    for i in range(n // 2):
        stack.push(s[i])

    # Skip the middle character if the string length is odd
    if n % 2 != 0:
        n = n // 2 + 1

    # Compare the second half of characters with the elements popped from the stack
    for i in range(n, len(s)):
        if stack.pop() != s[i]:
            return False

    return True