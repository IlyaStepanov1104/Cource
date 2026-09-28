# Реализация min-heap (бинарной кучи) на списке.
# push(value) - добавить значение с сохранением свойства кучи
# pop() - извлечь и вернуть минимальное значение


class Heap:
    def __init__(self) -> None:
        self.data: list[int] = []

    def push(self, value: int) -> None:
        self.data.append(value)
        i = len(self.data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.data[parent] <= self.data[i]:
                break
            self.data[parent], self.data[i] = self.data[i], self.data[parent]
            i = parent

    def pop(self) -> int:
        top = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            i = 0
            n = len(self.data)
            while True:
                left, right = 2*i + 1, 2*i + 2
                smallest = i
                if left < n and self.data[left] < self.data[smallest]:
                    smallest = left
                if right < n and self.data[right] < self.data[smallest]:
                    smallest = right
                if smallest == i:
                    break

                self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
                i = smallest
        return top

h = Heap()
for x in [5, 3, 8, 1, 9, 2]:
    h.push(x)

result = [h.pop() for _ in range(6)]
print(result, [1, 2, 3, 5, 8, 9])
