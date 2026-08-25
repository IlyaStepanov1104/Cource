# Задача: Возврат в начало
# Фишка стоит в вершине start. За один ход переходит по ребру.
# Может ли она вернуться в start за НЕЧЁТНОЕ число ходов?
#
# Вход: n, edges - список пар (u, v), start - стартовая вершина
# Выход: True / False

from Graph import Graph


def can_return_odd(n, edge_list, start):
    pass


print(can_return_odd(3, [(0, 1), (1, 2), (0, 2)], 0))        # True  (треугольник)
print(can_return_odd(4, [(0, 1), (1, 2), (2, 3), (3, 0)], 0)) # False (квадрат)
print(can_return_odd(3, [(0, 1), (1, 2)], 0))                 # False (цепочка)
print(can_return_odd(4, [(0, 1), (1, 2), (2, 3), (3, 1)], 0)) # True  (треугольник 1-2-3)
