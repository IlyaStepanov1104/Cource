from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        E = [[] for i in range(n)]
        for v, u in connections:
            E[v].append(u)
            E[u].append(v)
            
        visited = set()

        def dfs(v):
            visited.add(v)
            for neighbor in connections[v]:
                if neighbor not in visited:
                    dfs(neighbor)
                    
        count = 0
        
        for v in range(n):
            if v not in visited:
                dfs(v)
                count+=1
                
        if len(connections) < n - 1:
            return -1
        
        return count - 1