from collections import deque


# Фишка на ориентированном графе (могут быть циклы), вершины 0..n-1.
# Ходят по очереди, ход - по одной стрелке, кто не может сходить - проиграл.
# Бесконечная игра - ничья. Для каждой вершины вернуть строку из букв:
# W - тот, кто ходит отсюда, выигрывает, L - проигрывает, D - ничья.
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


# граф с занятия: A=0 B=1 C=2 D=3 G=4 H=5 T=6
lesson = [(0, 1), (1, 0), (0, 2), (1, 3), (3, 2), (2, 6), (4, 5), (5, 4), (4, 2), (5, 2)]
print(classify(7, lesson), 'LWWLDDL')
print(classify(1, []), 'L')
print(classify(2, [(0, 1)]), 'WL')
print(classify(2, [(0, 1), (1, 0)]), 'DD')
print(classify(3, [(0, 1), (1, 2), (2, 0)]), 'DDD')
print(classify(4, [(0, 1), (1, 2), (2, 3)]), 'WLWL')
print(classify(3, [(0, 0), (0, 1), (1, 2)]), 'DWL')
