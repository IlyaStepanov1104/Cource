from collections import deque


# Фишка на ориентированном графе, вершины 0..n-1. За ход фишку двигают
# на одно или на два ребра вперёд (на выбор ходящего). Кто не может сходить - проиграл.
# Бесконечная игра - ничья. Вернуть строку из W / L / D для каждой вершины.
# Построить новый граф ходов и раскрасить обычной раскраской (из задачи 1).
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


def one_or_two(n: int, edges: list[tuple[int, int]]) -> str:
    adj = [set() for _ in range(n)]
    for v, to in edges:
        adj[v].add(to)

    moves = set()
    for v in range(n):
        for to in adj[v]:
            moves.add((v, to))
            for w in adj[to]:
                moves.add((v, w))

    return classify(n, list(moves))


print(one_or_two(5, [(0, 1), (1, 2), (1, 3), (2, 4), (3, 4)]), 'LWWWL')
print(one_or_two(3, [(0, 1), (1, 2)]), 'WWL')
print(one_or_two(4, [(0, 1), (1, 2), (2, 3)]), 'LWWL')
print(one_or_two(5, [(0, 1), (1, 2), (2, 3), (3, 4)]), 'WLWWL')
print(one_or_two(2, [(0, 1), (1, 0)]), 'DD')
print(one_or_two(1, []), 'L')
