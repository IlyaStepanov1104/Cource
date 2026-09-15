from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dist = {}
        q = deque()
        fresh = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                    dist[(i, j)] = 0
                elif grid[i][j] == 1:
                    fresh += 1
                    
        while q:
            i, j = q.popleft()
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                i_1, j_1 = i+di, j+dj
                if 0<=i_1<rows and 0<=j_1<cols and grid[i_1][j_1]==1 and (i_1, j_1) not in dist:
                    dist[(i_1, j_1)] = dist[(i, j)] + 1
                    fresh -= 1
                    q.append((i_1, j_1))
            
        if fresh > 0: 
            return -1
        
        return max(dist.values(), default=0)
