"""
Задача: найти компоненты сильной связности (КСС) ориентированного графа.

adj = {0: [1], 1: [2], 2: [0], ...} - список смежности (словарь),
каждая вершина присутствует как ключ. Рёбра направленные: ключ -> элемент списка.

КСС - максимальное множество вершин, попарно достижимых друг из друга
(есть путь u -> v и путь v -> u).

Используй алгоритм Косарайю (два обхода в глубину), без наивного
перебора пар вершин.
"""


def kosaraju(adj: dict) -> list:
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


def count_scc(adj: dict):
    comps = kosaraju(adj)
    return len(comps) if comps is not None else None


# ---- проверка: слева результат функции, справа ожидаемое ----

def _normalize(components):
    if components is None:
        return None
    return sorted(tuple(sorted(c)) for c in components)


g1 = {0: [1], 1: [2], 2: [0], 3: [1, 2, 4], 4: [5], 5: [3]}
print(_normalize(kosaraju(g1)), [(0, 1, 2), (3, 4, 5)])
print(count_scc(g1), 2)

# чистый DAG - каждая вершина сама себе КСС
print(count_scc({0: [1], 1: [2], 2: []}), 3)

# один цикл - одна КСС на весь граф
print(_normalize(kosaraju({0: [1], 1: [2], 2: [0]})), [(0, 1, 2)])

# две изолированные вершины без рёбер
print(count_scc({0: [], 1: []}), 2)

# два независимых двухвершинных цикла
print(count_scc({0: [1], 1: [0], 2: [3], 3: [2]}), 2)

# одна вершина с петлёй
print(count_scc({0: [0]}), 1)
