from collections import deque

class Queue:
    def __init__(self):
        self.val = deque()
        
    def enqueue(self, item):
        self.val.append(item)
        
    def dequeue(self):
        return self.val.popleft()   
        
    def peek(self):
        if self.is_empty():
            return None
        return self.val[0]    
        
    def is_empty(self):
        return len(self.val) == 0
    
    def size(self):
        return len(self.val)

    def __str__(self):
        return f"Queue: {self.val}"
        
queue = Queue()

queue.enqueue('A')
print(queue)
queue.enqueue('B')
print(queue)
queue.enqueue('C')
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
