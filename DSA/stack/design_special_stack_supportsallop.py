""" Special Stack in Python that supports all standard stack operations—push, pop, peek, isEmpty—and also includes an efficient getMin() operation that returns the minimum element in constant time O(1).

🧠 Design Strategy
We'll use two stacks:
- main_stack: stores all elements.
- min_stack: keeps track of the minimums.
Whenever we push a new element:
- Push it to main_stack.
- Push it to min_stack only if it's smaller than or equal to the current minimum.
When popping:
- Pop from main_stack.
- If the popped element is equal to the top of min_stack, pop from min_stack too.
 """

class SpecialStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, value):
        self.main_stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.main_stack:
            return None
        value = self.main_stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def peek(self):
        if not self.main_stack:
            return None
        return self.main_stack[-1]

    def is_empty(self):
        return len(self.main_stack) == 0

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]
    
#shortened the code
class SpecialStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, value):
        self.main_stack.append(value)
        # Push to min_stack if it's the new minimum
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.main_stack:
            return None
        value = self.main_stack.pop()
        # Pop from min_stack if it was the minimum
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def peek(self):
        return self.main_stack[-1] if self.main_stack else None

    def is_empty(self):
        return len(self.main_stack) == 0

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

stack = SpecialStack()
stack.push(5)
stack.push(2)
stack.push(8)
stack.push(1)

print("Current Min:", stack.get_min())  # Output: 1
stack.pop()
print("After popping, Min:", stack.get_min())  # Output: 2