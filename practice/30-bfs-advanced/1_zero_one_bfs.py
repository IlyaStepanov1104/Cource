from collections import deque


# Реализация 0-1 BFS.
# graph - словарь вида {вершина: [(сосед, вес), ...]}, вес только 0 или 1.
# start - вершина, от которой считаем.
# Вернуть словарь {вершина: минимальная сумма весов пути от start}.
# Недостижимых вершин в словаре быть не должно.


def zero_one_bfs(graph: dict[str, list[tuple[str, int]]], start: str) -> dict[str, int]:
    dist = {start: 0}
    dq = deque([start])
    
    while dq:
        v = dq.popleft()
        d = dist[v]
        
        for to, w in graph[v]:
            if to not in dist or dist[to] > d + w:
                dist[to] = d + w
                if w == 0:
                    dq.appendleft(to)
                else:
                    dq.append(to)
                    
    return dist




# граф с трассировки на слайде: через C до B бесплатно, хотя напрямую стоит 1
TRACE = {
    'A': [('B', 1), ('C', 0)],
    'B': [('D', 1)],
    'C': [('B', 0), ('E', 1)],
    'D': [],
    'E': [],
}
print(zero_one_bfs(TRACE, 'A'), {'A': 0, 'B': 0, 'C': 0, 'D': 1, 'E': 1})

# длинный бесплатный путь дешевле короткого платного
FREE = {
    'S': [('A', 0), ('T', 1)],
    'A': [('B', 0)],
    'B': [('T', 0)],
    'T': [],
}
print(zero_one_bfs(FREE, 'S'), {'S': 0, 'A': 0, 'B': 0, 'T': 0})

# одно ребро веса 1
ONE_EDGE = {'X': [('Y', 1)], 'Y': []}
print(zero_one_bfs(ONE_EDGE, 'X'), {'X': 0, 'Y': 1})

# в C попасть нельзя, её в ответе быть не должно
ALONE = {'A': [('B', 1)], 'B': [], 'C': [('A', 0)]}
print(zero_one_bfs(ALONE, 'A'), {'A': 0, 'B': 1})
