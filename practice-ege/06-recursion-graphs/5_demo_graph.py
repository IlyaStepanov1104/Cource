import sys
sys.setrecursionlimit(10000)

# Демо ЕГЭ-2027, №23. Файл demo_23.txt.
# В текстовом файле - ациклический ориентированный взвешенный граф. В каждой строке:
# L M W - ребро из вершины L в вершину M весом W (вещественное число).
# Вершины пронумерованы не подряд (L, M <= 1000), числа разделены любыми пробелами и табуляциями.
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


# Сколько разных путей из start в finish.
def count_paths(graph: dict[int, list[tuple[int, float]]], start: int, finish: int) -> int:
    memo = {}

    def count(v):
        if v == finish:
            return 1
        if v in memo:
            return memo[v]

        res = 0
        for to, w in graph[v]:
            res += count(to)
        memo[v] = res
        return res

    return count(start)

# Длина кратчайшего пути из start в finish.
def shortest(graph: dict[int, list[tuple[int, float]]], start: int, finish: int) -> float:
    memo = {}

    def best(v):
        if v == finish:
            return 0
        if v in memo:
            return memo[v]
        res = float('inf')
        for to, w in graph[v]:
            res = min(res, w + best(to))
        memo[v] = res
        return res

    return best(start)



def whole(x: float | None) -> int | None:
    return None if x is None else int(x)

# пример из условия: 8 строк файла
example = {100: [(12, 1.0)], 6: [(7, 7.0), (1, 1.0)], 1: [(7, 5.5), (100, 12.0), (4, 2.5)],
           7: [(100, 2.0)], 4: [(100, 8.0)]}
print(count_paths(example, 1, 100), 3)
print(shortest(example, 1, 100), 7.5)

graph = read_graph('demo_23.txt')
print(count_paths(graph, 1, 100), 2033652335)
print(whole(shortest(graph, 1, 100)), 10971)
