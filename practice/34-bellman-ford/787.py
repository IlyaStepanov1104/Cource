def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    INF = float('inf')
    dist = [INF] * n
    dist[src] = 0

    for _ in range(k+1):
        prev = dist.copy()
        changed = False
        for v, to, w in flights:
            if prev[v] != INF and prev[v] + w < dist[to]:
                dist[to] = prev[v] + w
                changed = True

        if not changed:
            break

    if dist[dst] == INF:
        return -1
    
    return int(dist[dst])