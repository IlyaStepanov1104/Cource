def find_itinerary(tickets: list) -> list:
    adj = {}
    for src, dst in tickets:
        if src not in adj:
            adj[src] = []
        adj[src].append(dst)
    for city in adj:
        adj[city].sort()

    it = {city: 0 for city in adj}
    stack = ["JFK"]
    route = []

    while stack:
        city = stack[-1]
        neighbors = adj.get(city)
        if neighbors and it[city] < len(neighbors):
            nxt = neighbors[it[city]]
            it[city] += 1
            stack.append(nxt)
        else:
            route.append(stack.pop())

    route.reverse()
    return route



print(find_itinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]),
      ["JFK", "MUC", "LHR", "SFO", "SJC"])

print(find_itinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]),
      ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])
