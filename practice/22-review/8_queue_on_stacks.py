# Задача: Очередь на двух стеках
# Реализуй очередь (FIFO), используя только два стека (LIFO):
# in_stack - для добавления, out_stack - для извлечения.
#
# Подсказка: перекладывай элементы из in_stack в out_stack
# только тогда, когда out_stack пуст.


class QueueOnStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, value):
        # TODO: добавь элемент в in_stack
        pass

    def dequeue(self):
        # TODO: если out_stack пуст - перелей все элементы из in_stack,
        # затем удали и верни верхний элемент out_stack
        pass


q = QueueOnStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
q.enqueue(4)
print(q.dequeue())  # 2
print(q.dequeue())  # 3
print(q.dequeue())  # 4
