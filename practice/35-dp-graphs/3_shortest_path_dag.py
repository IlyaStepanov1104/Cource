# Граф без циклов, рёбра (откуда, куда, вес), веса бывают отрицательными.
# Найти кратчайший путь из start в finish и сам путь.
# Если finish недостижима - вернуть None.
def top_sort(n: int, adj: list[list[int]]) -> list[int]:
    visited = [False] * n
    order = []

    def dfs(v):
        visited[v] = True
        for to in adj[v]:
            if not visited[to]:
                dfs(to)
        order.append(v)

    for v in range(n):
        if not visited[v]:
            dfs(v)

    return order[::-1]

def shortest_path(n: int, edges: list[tuple[int, int, int]], start: int, finish: int) -> tuple[float, list[int]]:
    adj = [[] for _ in range(n)]
    for v, to, w in edges:
        adj[v].append((to, w))

    best = [float('inf')] * n
    parent = [-1] * n
    best[start] = 0
    order = top_sort(n, [[to for to, w in adj[v]] for v in range(n)])
    for v in order:
        if best[v] == float('-inf'):
            continue
        for to, w in adj[v]:
            if best[v] + w < best[to]:
                best[to] = best[v] + w
                parent[to] = v

    path = [finish]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return best[finish], path[::-1]


# граф со слайда "Кратчайший путь тоже можно": ребро B -> C теперь -3
edges = [(3, 5, 3), (0, 1, 3), (2, 4, 5), (0, 2, 2), (1, 3, 4), (2, 3, -3), (1, 4, 2), (4, 5, 2)]
print(shortest_path(6, edges, 0, 5), (2, [0, 2, 3, 5]))

print(shortest_path(3, [(1, 2, 1)], 0, 2), None)
