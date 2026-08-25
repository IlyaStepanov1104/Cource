# Задача: Электрические узлы
# N узлов, соединённых проводниками.
# Можно ли пометить каждый узел как + или - так, чтобы каждый провод соединял + с -?
# Если можно - вернуть список пометок, иначе None.
#
# Вход: n - кол-во узлов, wires - список пар (u, v)
# Выход: список ['+', '-', ...] или None

from Graph import Graph


def assign_poles(n, wires):
    POLES = ['+', '-']
    
    graph = Graph(n)
    for (i, j) in wires:
        graph.add_edge(i, j)
    
    result, colors = graph.is_bipartite()
    if not result:
        return None
    return [POLES[c] for c in colors]


print(assign_poles(2, [(0, 1)]))                          # ['+', '-']
print(assign_poles(4, [(0, 1), (1, 2), (2, 3), (3, 0)])) # ['+', '-', '+', '-']
print(assign_poles(3, [(0, 1), (1, 2), (0, 2)]))          # None
