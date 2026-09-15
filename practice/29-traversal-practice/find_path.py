class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        visited = {source}
        stack = [source]
        
        while stack:
            v = stack.pop()
            if v == destination:
                return True

            for to in adj[v]:
                if to not in visited:
                    visited.add(to)
                    stack.append(to)
                    
        return False