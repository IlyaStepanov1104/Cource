# Поляков, задача 33 к заданию 23 (PRO100-ЕГЭ). Файл 23-33.txt.
# В текстовом файле - ациклический ориентированный взвешенный граф в формате демо ЕГЭ-2027:
# L M W - ребро из вершины L в вершину M весом W.
# Найдите целую часть длины кратчайшего пути из вершины 1 в вершину 100.
# Граф из файла: graph[v] - список пар (куда, вес).
def read_graph(path: str) -> dict[int, list[tuple[int, float]]]:
    pass

# Длина кратчайшего пути из start в finish.
def shortest(graph: dict[int, list[tuple[int, float]]], start: int, finish: int) -> float:
    pass



def whole(x: float | None) -> int | None:
    return None if x is None else int(x)


example = {100: [(12, 1.0)], 6: [(7, 7.0), (1, 1.0)], 1: [(7, 5.5), (100, 12.0), (4, 2.5)],
           7: [(100, 2.0)], 4: [(100, 8.0)]}
print(shortest(example, 1, 100), 7.5)
print(whole(shortest(read_graph('23-33.txt'), 1, 100)), 51)
