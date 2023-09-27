class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
