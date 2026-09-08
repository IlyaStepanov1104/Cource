"""
Задача: построить эйлеров цикл в неориентированном графе (алгоритм Хиерхольцера).

adj = {0: [1, 2], 1: [0, 2], ...} - список смежности (словарь), рёбра
неориентированные и хранятся в обе стороны. Гарантируется, что эйлеров цикл
существует (граф связен, все степени чётные - см. задачу 1).

Вернуть сам маршрут списком вершин, где первая и последняя вершина совпадают,
а каждое ребро графа пройдено ровно один раз.

Идея: стек вершин + множество использованных рёбер used.add((u, v)).
Пока у вершины на вершине стека есть непройденное ребро - идём по нему и
кладём соседа в стек. Как только рёбер не осталось - снимаем вершину со
стека и дописываем в ответ. В конце разворачиваем список.
"""


def euler_circuit(adj: dict) -> list:
    used = set()

    start = next(v for v in adj if adj[v])

    stack = [start]
    circuit = []

    while stack:
        v = stack[-1]
        
        next_v = None
        for to in adj[v]:
            if (v, to) not in used:
                next_v = to
                break

        if next_v is None:
            circuit.append(stack.pop())
        else:
            used.add((v, next_v))
            used.add((next_v, v))
            stack.append(next_v)

    circuit.reverse()
    return circuit



# ---- проверка: маршрут не единственный, поэтому сверяем не список, а корректность ----

def _edge_set(adj: dict) -> set:
    return {frozenset((v, to)) for v in adj for to in adj[v]}


def _is_valid_euler_circuit(adj: dict, route: list) -> bool:
    edges = _edge_set(adj)
    if not route or route[0] != route[-1]:
        return False
    if len(route) - 1 != len(edges):
        return False

    seen = set()
    for u, v in zip(route, route[1:]):
        e = frozenset((u, v))
        if e not in edges or e in seen:
            return False
        seen.add(e)

    return seen == edges


# граф-бабочка (пример со слайда трассировки)
bowtie = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B", "D", "E"],
    "D": ["C", "E"],
    "E": ["C", "D"],
}
print(_is_valid_euler_circuit(bowtie, euler_circuit(bowtie)), True)

# простой квадрат
square = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 0]}
print(_is_valid_euler_circuit(square, euler_circuit(square)), True)

# треугольник
triangle = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
print(_is_valid_euler_circuit(triangle, euler_circuit(triangle)), True)

# два квадрата с общей вершиной - все степени чётные (3 - степени 4, остальные 2)
double_square = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2, 4, 6],
    4: [3, 5],
    5: [4, 6],
    6: [5, 3],
}
print(_is_valid_euler_circuit(double_square, euler_circuit(double_square)), True)
