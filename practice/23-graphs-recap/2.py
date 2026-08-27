from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        E = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    E[i].append(j)
        
        visited = set()
        
        def dfs(v):
            visited.add(v)
            for neighbor in E[v]:
                if neighbor not in visited:
                    dfs(neighbor)
                    
        count = 0
        for v in range(n):
            if v not in visited:
                dfs(v)
                count += 1
                
        return count
        
        
        
solution = Solution()

# пример со слайда: города 0,1 связаны, город 2 - отдельно
print(solution.findCircleNum([[1, 1, 0],
                               [1, 1, 0],
                               [0, 0, 1]]))  # 2

# все изолированы - каждый сам себе провинция
print(solution.findCircleNum([[1, 0, 0],
                               [0, 1, 0],
                               [0, 0, 1]]))  # 3

# все связаны напрямую - одна провинция
print(solution.findCircleNum([[1, 1, 1],
                               [1, 1, 1],
                               [1, 1, 1]]))  # 1

# связь не прямая, а через посредника (0-1, 1-2, но не 0-2) - всё равно одна провинция
print(solution.findCircleNum([[1, 1, 0],
                               [1, 1, 1],
                               [0, 1, 1]]))  # 1

# один город
print(solution.findCircleNum([[1]]))  # 1