from collections import deque


# Фишка на ориентированном графе, вершины 0..n-1, ходы у обоих одинаковые.
# Первый хочет, чтобы фишка попала в тупик (игра кончилась), Второй - чтобы игра не кончалась никогда.
# Фишка в start, первым ходит Первый. Вернуть True, если Первый может добиться своего
# при любой игре Второго. За O(n + m).
def first_can_end(n: int, edges: list[tuple[int, int]], start: int) -> bool:
    # позиция v - ходит Первый, n + v - ходит Второй
    pass




# пример с занятия: T=0 A=1 B=2 C=3
lesson = [(1, 0), (1, 2), (2, 1), (2, 3), (3, 2)]
print(first_can_end(4, lesson, 1), True)
print(first_can_end(4, lesson, 2), False)
print(first_can_end(4, lesson, 3), False)
print(first_can_end(4, lesson, 0), True)
print(first_can_end(2, [(0, 1), (1, 0)], 0), False)
print(first_can_end(3, [(0, 1), (1, 2), (1, 0)], 0), False)
print(first_can_end(3, [(0, 1), (1, 2), (0, 2)], 0), True)
