# Задача про проект: граф без циклов, рёбра (откуда, куда, дней).
# Найти самый длинный путь из start в finish и сам путь (список вершин от start до finish).
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

def longest_path(n: int, edges: list[tuple[int, int, int]], start: int, finish: int) -> tuple[float, list[int]]:
    adj = [[] for _ in range(n)]
    for v, to, w in edges:
        adj[v].append((to, w))

    best = [float('-inf')] * n
    parent = [-1] * n
    best[start] = 0
    order = top_sort(n, [[to for to, w in adj[v]] for v in range(n)])
    for v in order:
        if best[v] == float('-inf'):
            continue
        for to, w in adj[v]:
            if best[v] + w > best[to]:
                best[to] = best[v] + w
                parent[to] = v

    path = [finish]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return best[finish], path[::-1]


# граф со слайдов: S=0, A=1, B=2, C=3, D=4, T=5
edges = [(3, 5, 3), (0, 1, 3), (2, 4, 5), (0, 2, 2), (1, 3, 4), (2, 3, 1), (1, 4, 2), (4, 5, 2)]
print(longest_path(6, edges, 0, 5), (10, [0, 1, 3, 5]))

print(longest_path(4, [(0, 1, 1), (1, 3, 1), (0, 2, 5), (2, 3, 1), (0, 3, 4)], 0, 3), (6, [0, 2, 3]))
