import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        E = [[] for _ in range(n)]
        for v, to, w in flights:
            E[v].append((to,w))
        dist = [[float('inf')] * (k+2) for _ in range(n)]
        dist[src][0] = 0
        limit = k+1
        visited = set()
        heap = [(0, src, 0)]
        while heap:
            d, v, used = heapq.heappop(heap)
            if v == dst:
                return d
            if (v, used) in visited:
                continue
            visited.add((v,used))
            if used < limit:
                for to, w in E[v]:
                    if d+w < dist[to][used + 1]:
                        dist[to][used + 1] = d+w
                        heapq.heappush(heap, (d+w, to, used+1))
        return -1
