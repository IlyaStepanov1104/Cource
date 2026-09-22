from collections import deque
from typing import List, Tuple

def BFS(graph, start):
    dist = [-1] * len(graph)
    dist[start] = 0
    q = deque([start])
    while q:
        v = q.popleft()
        for to in graph[v]:
            if dist[to] == -1:
                dist[to] = dist[v] + 1
                q.append(to)
    return dist


# edges = [(v, to, w), ...]
def split_edges(n: int, edges: List[Tuple[int, int, int]]):
    graph = [[] for _ in range(n)]
    
    for v, to, w in edges:
        prev = v
        for _ in range(w - 1):
            graph.append([])
            fake = len(graph) - 1
            graph[prev].append(fake)
            prev = fake
        graph[prev].append(to)
        
    return graph