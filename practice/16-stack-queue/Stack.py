class Stack:
    def __init__(self):
        self.val = []
        
    def push(self, item):
        self.val.append(item)
        
    def pop(self):
        return self.val.pop()   
        
    def peek(self):
        if self.is_empty():
            return None
        return self.val[-1]    
        
    def is_empty(self):
        return len(self.val) == 0
    
    def size(self):
        return len(self.val)

    def __str__(self):
        return f"Stack: {self.val}"
        
stack = Stack()

stack.push('A')
print(stack)
stack.push('B')
print(stack)
stack.push('C')
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
