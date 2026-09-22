from collections import deque


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = [[] for _ in range (n+1)] # 0 - не используем. Только от 1 до n включительно
        
        for v, to, w in times:
            prev = v
            for _ in range(w - 1):
                graph.append([])
                fake = len(graph) - 1
                graph[prev].append(fake)
                prev = fake
            graph[prev].append(to)
    
        dist = [-1] * len(graph)
        dist[k] = 0
        q = deque([k])
        while q:
            v = q.popleft()
            for to in graph[v]:
                if dist[to] == -1:
                    dist[to] = dist[v] + 1
                    q.append(to)
        
        answer = 0
        for city in range(1, n+1):
            if dist[city] == -1:
                return -1

            answer = max(answer, dist[city])
        
        return answer