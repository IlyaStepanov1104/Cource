# Задача: 2-раскраска графа
# Граф: цикл 1-2, 2-3, 3-4, 4-5, 5-1 (5 вершин).
# Проверь двудольность через 2-раскраску DFS (см. Graph.is_bipartite).
# Если раскрасить не получится - метод вернёт False.


from Graph import Graph


def check(n, edges):
    g = Graph(n)
    for u, v in edges:
        g.add_edge(u, v)
    return g.is_bipartite()


# квадрат - двудольный
print(check(4, [(0, 1), (1, 2), (2, 3), (3, 0)]))  # (True, [...])

# цикл длины 5 - НЕ двудольный
print(check(5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]))  # (False, [...])
