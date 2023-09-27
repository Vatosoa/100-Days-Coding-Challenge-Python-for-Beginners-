class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def is_empty(self):
        return len(self.items) == 0
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
