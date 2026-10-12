from collections import deque


# Поддавки на ориентированном графе, вершины 0..n-1: кто НЕ может сходить - выиграл.
# Бесконечная игра - ничья. Вернуть строку из W / L / D для каждой вершины (для того, кто ходит).
# Не писать новую раскраску: перестроить граф и раскрасить обычной (из задачи 1).
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


def misere(n: int, edges: list[tuple[int, int]]) -> str:
    out_deg = [0] * n
    for v, to in edges:
        out_deg[v] += 1
    new_edges = list(edges)
    for v in range(n):
        if out_deg[v] == 0:
            new_edges.append((v, n))
    return classify(n + 1, new_edges)[:n]


print(misere(3, [(0, 1), (1, 2)]), 'WLW')
print(misere(1, []), 'W')
print(misere(2, [(0, 1), (1, 0)]), 'DD')
print(misere(3, [(0, 1), (0, 2), (1, 2)]), 'WLW')
print(misere(4, [(0, 1), (1, 0), (0, 2), (2, 3)]), 'WLLW')
