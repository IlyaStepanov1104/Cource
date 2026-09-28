import heapq
from collections import defaultdict

def read_graph(file):
    graph = defaultdict(list)
    with open(file) as f:
        for line in f:
            parts = line.split()
            if not parts:
                continue
            l, m, w = int(parts[0]), int(parts[1]), float(parts[2])
            graph[l].append((m, w))
    return graph

def get_inf(): return float('inf')

def dijkstra(graph, source):
    dist = defaultdict(get_inf)
    dist[source] = 0.0
    visited = set()
    heap = [(0.0, source)]

    while heap:
        d, v = heapq.heappop(heap)
        if v in visited:
            continue
        visited.add(v)
        for to, w in graph[v]:
            if d + w < dist[to]:
                dist[to] = d + w
                heapq.heappush(heap, (dist[to], to))

    return dist

graph = read_graph('D:/Work/Cource/practice/33-dijkstra-continued/demo_23.txt')
dist = dijkstra(graph, 1)
print(int(dist[100]))
