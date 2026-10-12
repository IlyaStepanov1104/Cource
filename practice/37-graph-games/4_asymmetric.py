from collections import deque


# Асимметричная игра: одна фишка на графе, вершины 0..n-1. Оранжевый ходит только
# по стрелкам orange, Синий - только по стрелкам blue. Ходят по очереди, кто не может
# сходить - проиграл, бесконечная игра - ничья.
# Вернуть две строки из W / L / D: результат для ходящего в каждой вершине,
# если сейчас ходит Оранжевый, и если сейчас ходит Синий.
def classify(n: int, edges: list[tuple[int, int]]) -> str:
    rev = [[] for _ in range(n)]
    counter = [0] * n
    for v, to in edges:
        rev[to].append(v)
        counter[v] += 1
    res = ['D'] * n
    q = deque()

    # Помечаем тупики
    for v in range(n):
        if counter[v] == 0:
            res[v] = 'L'
            q.append(v)

    while q:
        v = q.popleft()
        for parent in rev[v]:
            if res[parent] != 'D':
                continue
            elif res[v] == 'L':
                res[parent] = 'W'
                q.append(parent)
            else:
                counter[parent] -= 1
                if counter[parent] == 0:
                    res[parent] = 'L'
                    q.append(parent)

    return ''.join(res)


def asymmetric(n: int, orange: list[tuple[int, int]], blue: list[tuple[int, int]]) -> tuple[str, str]:
    # позиция v - ходит Оранжевый, позиция n + v - ходит Синий
    # edges = [(v, n + to) for v, to in orange] + [(n + v, to) for v, to in blue]
    edges = []
    for v, to in orange:
        # от 0 до n - оранжевый этаж
        # от n до 2n - голубой этаж
        edges.append((v, to + n))

    for v, to in blue:
        edges.append((n + v, to))

    res = classify(2*n, edges)
    return res[:n], res[n:]

# пример с занятия: A=0 B=1 C=2 D=3
print(asymmetric(4, [(0, 1), (1, 2), (2, 3)], [(3, 2), (0, 3)]), ('WWDL', 'WLLD'))
print(asymmetric(2, [(0, 1)], []), ('WL', 'LL'))
print(asymmetric(2, [(0, 1)], [(1, 0)]), ('DL', 'LD'))
print(asymmetric(2, [(0, 1), (1, 0)], [(0, 1), (1, 0)]), ('DD', 'DD'))
print(asymmetric(3, [(0, 1), (1, 2)], [(1, 0), (2, 1)]), ('DDL', 'LDD'))
