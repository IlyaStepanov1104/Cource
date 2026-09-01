"""
Задача: построить конденсацию орграфа и посчитать истоки и стоки.

adj = {0: [1], ...} - список смежности, каждая вершина есть как ключ.

Конденсация: каждую КСС стягиваем в одну вершину. Ребро между КСС-узлами -
если в исходном графе было хотя бы одно ребро между их вершинами (петли КСС
не считаем). Конденсация всегда DAG.

Исток конденсации - КСС без входящих рёбер.
Сток конденсации  - КСС без исходящих рёбер.

Вернуть кортеж (число истоков, число стоков).
Если КСС одна - это одновременно исток и сток, ответ (1, 1).

Подсказка: kosaraju из задачи 1 скопируй сюда и переиспользуй.
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


def condensation_sources_sinks(adj: dict) -> tuple:
    components = kosaraju(adj)
    
    # comp_id[v] - Номер КСС, в которой лежит вершина v
    comp_id = {}
    
    for i in range(len(components)):
        comp = components[i]
        for v in comp:
            comp_id[v] = i
            
    has_in = [False] * len(components)
    has_out = [False] * len(components)
    
    for u in adj:
        for v in adj[u]:
            if comp_id[u] != comp_id[v]:
                has_in[comp_id[v]] = True
                has_out[comp_id[u]] = True

    sources = sum(1 for x in has_in if not x)
    sinks = sum(1 for x in has_out if not x)
    
    return sources, sinks
    
def min_edges_to_strongly_connect(adj: dict):
    # бонус: минимум рёбер, чтобы весь граф стал одной КСС
    # 0, если КСС уже одна; иначе max(истоки, стоки)
    comps = kosaraju(adj)
    if comps is None:
        return None
    if len(comps) == 1:
        return 0
    sources, sinks = condensation_sources_sinks(adj)
    return max(sources, sinks)


# ---- проверка: слева результат функции, справа ожидаемое ----

# B = {3,4,5} -> A = {0,1,2}; цепочка из двух КСС
g1 = {0: [1], 1: [2], 2: [0], 3: [1, 2, 4], 4: [5], 5: [3]}
print(condensation_sources_sinks(g1), (1, 1))
print(min_edges_to_strongly_connect(g1), 1)

# один исток, два стока
g2 = {0: [1, 2], 1: [], 2: []}
print(condensation_sources_sinks(g2), (1, 2))
print(min_edges_to_strongly_connect(g2), 2)

# два истока, один сток
g3 = {0: [2], 1: [2], 2: []}
print(condensation_sources_sinks(g3), (2, 1))
print(min_edges_to_strongly_connect(g3), 2)

# весь граф - одна КСС
print(condensation_sources_sinks({0: [1], 1: [2], 2: [0]}), (1, 1))
print(min_edges_to_strongly_connect({0: [1], 1: [2], 2: [0]}), 0)

# две несвязные КСС-цепочки: истоки {0,2}, стоки {1,3}
g4 = {0: [1], 1: [], 2: [3], 3: []}
print(condensation_sources_sinks(g4), (2, 2))
print(min_edges_to_strongly_connect(g4), 2)
