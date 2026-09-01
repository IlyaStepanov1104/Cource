from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.n = n
        self.connections = connections
        E = [[] for i in range(n)]
        for start, end in connections:
            E[start].append(end)
            E[end].append(start)

        visited = set()
        tin = [0 for i in range(n)]
        low = [0 for i in range(n)]
        t = 0
        res = []
        
        def dfs(v, parent):
            nonlocal t
            
            visited.add(v)
            t += 1
            tin[v] = t
            low[v] = tin[v]
            for neighbor in E[v]:
                if neighbor == parent:
                    continue
                elif neighbor not in visited:
                    dfs(neighbor, v)
                    low[v] = min(low[v], low[neighbor])
                else:
                    low[v] = min(low[v], tin[neighbor])
                
                if low[neighbor] > tin[v]:
                    res.append([v, neighbor])
        
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
        
        return res