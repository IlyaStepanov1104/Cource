# Задача: Реактивы на складе
# N химических веществ. Некоторые пары взрываются при контакте.
# Можно ли разложить их по 2 комнатам так, чтобы опасные пары были в разных?
#
# Вход: n - кол-во веществ, dangerous - список пар (i, j)
# Выход: True / False

from Graph import Graph


def can_store(n, dangerous):
    graph = Graph(n)
    for (i, j) in dangerous:
        graph.add_edge(i, j)
    
    return graph.is_bipartite()


print(can_store(4, [(0, 1), (1, 2), (2, 3), (3, 0)]))  # True  (квадрат - чётный цикл)
print(can_store(3, [(0, 1), (1, 2), (0, 2)]))           # False (треугольник)
print(can_store(5, [(0, 2), (1, 2), (3, 4)]))           # True
print(can_store(5, [(0,1),(1,2),(2,3),(3,4),(4,0)]))    # False (5-цикл - нечётный)
