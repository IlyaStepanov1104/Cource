from collections import deque


# Поддавки на ориентированном графе, вершины 0..n-1: кто НЕ может сходить - выиграл.
# Бесконечная игра - ничья. Вернуть строку из W / L / D для каждой вершины (для того, кто ходит).
# Не писать новую раскраску: перестроить граф и раскрасить обычной (из задачи 1).
def classify(n: int, edges: list[tuple[int, int]]) -> str:
    pass


def misere(n: int, edges: list[tuple[int, int]]) -> str:
    pass




print(misere(3, [(0, 1), (1, 2)]), 'WLW')
print(misere(1, []), 'W')
print(misere(2, [(0, 1), (1, 0)]), 'DD')
print(misere(3, [(0, 1), (0, 2), (1, 2)]), 'WLW')
print(misere(4, [(0, 1), (1, 0), (0, 2), (2, 3)]), 'WLLW')
