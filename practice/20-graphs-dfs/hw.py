from typing import List


class Graph:
    def __init__(self, n, is_directed=False):
        self.edges = [[] for i in range(n)]
        self.is_directed = is_directed
        
    def add_edge(self, start, end):
        self.edges[start].append(end)
        if not self.is_directed:
            self.edges[end].append(start)
            
    def DFS(self, start=0):
        visited = set()
        
        def _dfs(v):
            visited.add(v)
            print(v)
            for neighbor in self.edges[v]:
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        
        
    def count_components(self):
        visited = set()
        count = 0
        
        def _dfs(v):
            visited.add(v)
            for neighbor in self.edges[v]:
                if neighbor not in visited:
                    _dfs(neighbor)

        for v in range(len(self.edges)):
            if v not in visited:
                _dfs(v)
                count += 1
                
        return count
        
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = Graph(n)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    graph.add_edge(i, j)
                    
        return graph.count_components()
        
solution = Solution()
print(solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))