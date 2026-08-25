class Graph:
    def __init__(self, n):
        self.edges = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def is_bipartite(self):
        '''
        Раскраска:
            -1 - нет цвета
            0 - красный
            1 - синий
        '''
        color = [-1] * len(self.edges)
        
        def _dfs(v, c):
            color[v] = c
            for neighbor in self.edges[v]:
                if color[neighbor] == -1:
                    if not _dfs(neighbor, 1 - c):
                        return False
                elif color[neighbor] == c:
                    return False
            return True
        
        for v in range(len(self.edges)):
            if color[v] == -1:
                if not _dfs(v, 1):
                    return False, color
        return True, color
