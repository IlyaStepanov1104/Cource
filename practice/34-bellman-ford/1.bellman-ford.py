def bellman_ford(n: int, edges: list[tuple[int, int, int]], start):
    '''
    args:
        n - количество вершин
        edges - список ребер (откуда, куда, вес)
        start - стартовая вершина
        Возвращает список кратчайших расстояний от start
    '''
    INF = float('inf')
    dist = [INF] * n
    dist[start] = 0

    for _ in range(n - 1):
        changed = False
        for v, to, w in edges:
            if dist[v] != INF and dist[v] + w < dist[to]:
                dist[to] = dist[v] + w
                changed = True

        if not changed:
            break

    for v, to, w in edges:
        if dist[v] != INF and dist[v] + w < dist[to]:
            return None

    return dist


# пример со слайдов: S=0, A=1, B=2, C=3, D=4
S, A, B, C, D = range(5)
edges = [
    (A, C, -3),
    (C, D, 2),
    (S, A, 4),
    (S, B, 2),
    (B, D, 7),
    (B, A, 1),
]
print(bellman_ford(5, edges, S), [0, 3, 2, 0, 2])

edges = [
    (S, A, 2),
    (A, B, 1),
    (B, C, -3),
    (C, A, 1)
]
print(bellman_ford(4, edges, S), None)