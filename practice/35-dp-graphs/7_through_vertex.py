# Граф без циклов, рёбра (откуда, куда).
# Сколько путей из start в finish проходят через вершину must?
def count_through(n: int, edges: list[tuple[int, int]], start: int, finish: int, must: int) -> int:
    pass




# граф со слайда "Обязательно через C": S=0, A=1, C=2, T=3
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
print(count_through(4, edges, 0, 3, 2), 2)
print(count_through(4, edges, 0, 3, 1), 2)
