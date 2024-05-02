# Add to your Stack class from before two functions:

# min - returns the minimum number in the stack currently.
# max - returns the maximum number in the stack currently.
# Bonus: Try not to iterate over all the elements in the stack each push or pop

class Stack:
    def __init__(self):
        self.stack_elements = []
        self.min_stack = []
        self.max_stack = []

    def push(self, item):
        self.stack_elements.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)
        if not self.max_stack or item >= self.max_stack[-1]:
            self.max_stack.append(item)

    def top(self):
        if self.stack_elements:
            return self.stack_elements[-1]
        else:
            return None

    def pop(self):
        if self.stack_elements:
            popped_item = self.stack_elements.pop()
            if popped_item == self.min_stack[-1]:
                self.min_stack.pop()
            if popped_item == self.max_stack[-1]:
                self.max_stack.pop()
            return popped_item
        else:
            return None

    def size(self):
        return len(self.stack_elements)

    def empty(self):
        return len(self.stack_elements) == 0

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None

    def max(self):
        if self.max_stack:
            return self.max_stack[-1]
        else:
            return None