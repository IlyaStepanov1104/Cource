# Граф может содержать циклы, рёбра (откуда, куда).
# Сколько маршрутов из start в finish ровно из k рёбер? Вершины и рёбра можно повторять.
def count_walks(n: int, edges: list[tuple[int, int]], start: int, finish: int, k: int) -> int:
    pass




# граф со слайдов: A=0, B=1, C=2, D=3
edges = [(0, 1), (0, 2), (1, 2), (2, 1), (1, 3), (2, 3)]
print(count_walks(4, edges, 0, 3, 3), 2)
print(count_walks(4, edges, 0, 3, 2), 2)
print(count_walks(4, edges, 0, 3, 1), 0)
print(count_walks(4, edges, 0, 3, 5), 2)
