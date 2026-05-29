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
        
    def has_cycle(self):
        visited = set()
        
        def _dfs(v, parent):
            visited.add(v)
            for neighbor in self.edges[v]:
                if neighbor not in visited:
                    if _dfs(neighbor, v):
                        return True
                elif neighbor != parent:
                    return True
            return False

        for v in range(len(self.edges)):
            if v not in visited:
                if _dfs(v, -1):
                    return True
        
        return False
    
    def topsort(self):
        visited = set()
        order = []
        
        def _dfs(v):
            visited.add(v)
            for neighbor in self.edges[v]:
                if neighbor not in visited:
                    _dfs(neighbor)
            order.append(v)

        for v in range(len(self.edges)):
            if v not in visited:
                _dfs(v)
            
        return order[::-1]
        
        
        
graph = Graph(6, is_directed=True)
graph.add_edge(1, 0)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(4, 2)
graph.add_edge(3, 5)
graph.add_edge(4, 5)
print(graph.topsort())