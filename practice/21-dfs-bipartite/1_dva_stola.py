# Задача: Два стола
# На вечеринке N человек. Некоторые пары конфликтуют.
# Можно ли рассадить всех за 2 стола так, чтобы за каждым не было ни одной ссоры?
#
# Вход: n - кол-во людей, conflicts - список пар (i, j)
# Выход: True / False

from Graph import Graph


def can_seat(n, conflicts):
    graph = Graph(n)
    for (i, j) in conflicts:
        graph.add_edge(i, j)
    
    return graph.is_bipartite()
    


print(can_seat(4, [(0, 1), (1, 2), (2, 3)]))        # True  (цепочка)
print(can_seat(3, [(0, 1), (1, 2), (0, 2)]))        # False (треугольник)
print(can_seat(4, [(0, 1), (2, 3)]))                # True  (два несвязных ребра)
print(can_seat(4, [(0,1),(1,2),(2,3),(3,0),(0,2)]))  # False (есть треугольник)
