from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        E = [[] for i in range(n + 1)]
        for v, u in dislikes:
            E[v].append(u)
            E[u].append(v)
            
        color = [-1] * (n + 1)

        def dfs(v, c):
            color[v] = c
            for neighbor in E[v]:
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - c):
                        return False
                elif color[neighbor] == c:
                    return False
            return True
    
        for v in range(1, n + 1):
            if color[v] == -1:
                if not dfs(v, 0):
                    return False
            
        return True


sol = Solution()

print(sol.possibleBipartition(3, [[1,2],[1,3],[2,3]]))