# Решу ЕГЭ 92565 (тот же файл, что в демо ЕГЭ-2027), №23. Файл 23.txt.
# В текстовом файле - ациклический ориентированный взвешенный граф. В каждой строке:
# L M W - ребро из вершины L в вершину M весом W (вещественное число).
# Вершины пронумерованы не подряд, числа разделены любыми пробелами и табуляциями.
# Найдите целую часть длины кратчайшего пути из вершины 1 в вершину 100.
# Граф из файла: graph[v] - список пар (куда, вес).
def read_graph(path: str) -> dict[int, list[tuple[int, float]]]:
    graph = {}
    for line in open(path):
        a, b, w = line.split()
        a, b, w = int(a), int(b), float(w)
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append((b, w))
    return graph


# Длина кратчайшего пути из start в finish.
def shortest(graph: dict[int, list[tuple[int, float]]], start: int, finish: int) -> float:
    pass



def whole(x: float | None) -> int | None:
    return None if x is None else int(x)

# пример из условия: 8 строк файла
example = {100: [(12, 1.0)], 6: [(7, 7.0), (1, 1.0)], 1: [(7, 5.5), (100, 12.0), (4, 2.5)],
           7: [(100, 2.0)], 4: [(100, 8.0)], 12: []}




print(shortest(example, 1, 100), 7.5)
print(whole(shortest(read_graph('23.txt'), 1, 100)), 10971)
