from typing import List


def kosaraju(adj: dict) -> List[int]:
    visited_1 = set()
    order = []
    
    def dfs_1(v):
        visited_1.add(v)
        for to in adj[v]:
            if to not in visited_1:
                dfs_1(to)
                
        order.append(v)
        
    for v in adj:
        if v not in visited_1:
            dfs_1(v)
    
    radj = {v: [] for v in adj}
    for v in adj:
        for to in adj[v]:
            radj[to].append(v)
    
    visited_2 = set()
    components = []
    
    def dfs_2(v, comp):
        visited_2.add(v)
        comp.append(v)
        for to in radj[v]:
            if to not in visited_2:
                dfs_2(to, comp)
                
    for v in reversed(order):
        if v not in visited_2:
            comp = []
            dfs_2(v, comp)
            components.append(comp)
            
    return components

def eventual_safe_nodes(E: List[List[int]]) -> List[int]:
    components = kosaraju({i: E[i] for i in range(len(E))})

    comp_id = {} # comp_id[v] - Номер КСС вершины v

    for i in range(len(components)):
        for v in components[i]:
            comp_id[v] = i

    unsafe = [len(comp) > 1 for comp in components]
    out_edges = [[] for _ in components] # Список смежности после конденсации графа

    for u in range(len(E)):
        for v in E[u]:
            if comp_id[u] == comp_id[v]:
                unsafe[comp_id[u]] = True
            else:
                out_edges[comp_id[u]].append(comp_id[v])

    for i in range(len(components) - 1, -1, -1):
        for j in out_edges[i]:
            if unsafe[j]:
                unsafe[i] = True
                break

    return sorted(v for v in range(len(E)) if not unsafe[comp_id[v]])
