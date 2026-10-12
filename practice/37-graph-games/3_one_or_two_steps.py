from collections import deque


# Фишка на ориентированном графе, вершины 0..n-1. За ход фишку двигают
# на одно или на два ребра вперёд (на выбор ходящего). Кто не может сходить - проиграл.
# Бесконечная игра - ничья. Вернуть строку из W / L / D для каждой вершины.
# Построить новый граф ходов и раскрасить обычной раскраской (из задачи 1).
def classify(n: int, edges: list[tuple[int, int]]) -> str:
    pass


def one_or_two(n: int, edges: list[tuple[int, int]]) -> str:
    pass




print(one_or_two(5, [(0, 1), (1, 2), (1, 3), (2, 4), (3, 4)]), 'LWWWL')
print(one_or_two(3, [(0, 1), (1, 2)]), 'WWL')
print(one_or_two(4, [(0, 1), (1, 2), (2, 3)]), 'LWWL')
print(one_or_two(5, [(0, 1), (1, 2), (2, 3), (3, 4)]), 'WLWWL')
print(one_or_two(2, [(0, 1), (1, 0)]), 'DD')
print(one_or_two(1, []), 'L')
