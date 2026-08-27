from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        E = [[] for i in range(n)]
        for v, u in edges:
            E[v].append(u)
            E[u].append(v)
            
        visited = set()
        
        def dfs(v):
            visited.add(v)
            
            for neighbor in E[v]:
                if neighbor not in visited:
                    dfs(neighbor)
            
        dfs(source)
        
        return destination in visited
    
solution = Solution()

# пример 1: путь есть (треугольник 0-1-2-0)
print(solution.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))  # True

# пример 2: два отдельных компонента, пути нет
print(solution.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))  # False

# source == destination - путь длины 0 тоже считается
print(solution.validPath(1, [], 0, 0))  # True

# рёбер нет вообще, вершины разные
print(solution.validPath(2, [], 0, 1))  # False

# путь есть, но не по прямому ребру - через промежуточную вершину
print(solution.validPath(4, [[0, 1], [1, 2], [2, 3]], 0, 3))  # True
