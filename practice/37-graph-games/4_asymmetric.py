from collections import deque


# Асимметричная игра: одна фишка на графе, вершины 0..n-1. Оранжевый ходит только
# по стрелкам orange, Синий - только по стрелкам blue. Ходят по очереди, кто не может
# сходить - проиграл, бесконечная игра - ничья.
# Вернуть две строки из W / L / D: результат для ходящего в каждой вершине,
# если сейчас ходит Оранжевый, и если сейчас ходит Синий.
def classify(n: int, edges: list[tuple[int, int]]) -> str:
    pass


def asymmetric(n: int, orange: list[tuple[int, int]], blue: list[tuple[int, int]]) -> tuple[str, str]:
    # позиция v - ходит Оранжевый, позиция n + v - ходит Синий
    pass




# пример с занятия: A=0 B=1 C=2 D=3
print(asymmetric(4, [(0, 1), (1, 2), (2, 3)], [(3, 2), (0, 3)]), ('WWDL', 'WLLD'))
print(asymmetric(2, [(0, 1)], []), ('WL', 'LL'))
print(asymmetric(2, [(0, 1)], [(1, 0)]), ('DL', 'LD'))
print(asymmetric(2, [(0, 1), (1, 0)], [(0, 1), (1, 0)]), ('DD', 'DD'))
print(asymmetric(3, [(0, 1), (1, 2)], [(1, 0), (2, 1)]), ('DDL', 'LDD'))
