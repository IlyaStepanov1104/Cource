from collections import deque

def BFS(adj, start):
    dist = {start: 0}
    parent = {start: None}
    q = deque([start])
    while q:
        v = q.popleft()
        for to in adj[v]:
            if to not in dist:
                dist[to] = dist[v] + 1
                parent[to] = v
                q.append(to)
    return dist, parent


def min_path(adj, start, end):
    _, parent = BFS(adj, start)
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    path.reverse()
    return path


G = {
    'A': ['B', 'C'], 
    'B': ['A', 'D'], 
    'C': ['A', 'D', 'E'], 
    'D': ['B', 'C', 'F'], 
    'E': ['C', 'F'], 
    'F': ['D', 'E']
    }

print(min_path(G, 'A', 'F'))