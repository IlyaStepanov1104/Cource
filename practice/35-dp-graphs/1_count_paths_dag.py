# Граф без циклов: n вершин (0 .. n-1), рёбра (откуда, куда).
# Посчитать, сколько существует разных путей из start в finish.
# Вершины идут в списке рёбер в произвольном порядке - сначала нужен топологический порядок.
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

def count_paths(n: int, edges: list[tuple[int, int]], start: int, finish: int) -> int:
    adj = [[] for _ in range(n)]
    for v, to in edges:
        adj[v].append(to)

    ways = [0] * n
    ways[start] = 1
    for v in top_sort(n, adj):
        for to in adj[v]:
            ways[to] += ways[v]

    return ways[finish]



# граф со слайда "Вспоминаем занятие 26": S=0, A=1, B=2, C=3, D=4, T=5
edges = [(3, 5), (0, 1), (4, 5), (1, 4), (0, 2), (2, 4), (1, 3)]
print(count_paths(6, edges, 0, 5), 3)

print(count_paths(4, [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)], 0, 3), 3)
print(count_paths(3, [(1, 2)], 0, 2), 0)
