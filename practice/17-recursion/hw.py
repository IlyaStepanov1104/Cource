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


class Queue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()
                
    def enqueue(self, item):
        self.stack_in.push(item)
        
    def dequeue(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
                
        return self.stack_out.pop()   
        
    def peek(self):
        if self.is_empty():
            return None
        return self.stack_out.peek()
        
    def is_empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()
    
    def size(self):
        return self.stack_in.size() + self.stack_out.size()
    
# --- Тесты ---

def check(label, expected, result):
    print(f"{label}: ожидалось={expected}, результат={result}")


q = Queue()

# enqueue трёх элементов
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# dequeue должен отдавать в порядке FIFO
check("dequeue 1", 1, q.dequeue())
check("dequeue 2", 2, q.dequeue())
check("dequeue 3", 3, q.dequeue())

# после полного опустошения - is_empty
check("is_empty после очистки", True, q.is_empty())

# перемешанные enqueue/dequeue
q.enqueue("a")
q.enqueue("b")
check("dequeue a", "a", q.dequeue())
q.enqueue("c")
check("dequeue b", "b", q.dequeue())
check("dequeue c", "c", q.dequeue())
check("is_empty после перемешки", True, q.is_empty())

# одиночный элемент
q.enqueue(42)
check("is_empty=False с элементом", False, q.is_empty())
check("dequeue 42", 42, q.dequeue())
check("is_empty после последнего", True, q.is_empty())
