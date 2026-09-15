from collections import deque


def shortest_path(grid: list) -> int:
    """Кратчайший путь из левого верхнего угла в правый нижний по клеткам с 0.

    Ходить можно в 8 направлений. Длина пути - число посещённых клеток.
    Если пути нет - вернуть -1.
    """
    n = len(grid)
    start = (0, 0)
    target = (n - 1, n - 1)
    
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1

    MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    dist = {start: 1}
    q = deque([start])
    
    while q:
        x0, y0 = q.popleft()
        
        if (x0, y0) == target:
            return dist[target]
        
        for dx, dy in MOVES:
            x1, y1 = x0 + dx, y0 + dy
            if 0 <= x1 < n and 0 <= y1 < n and grid[x1][y1] == 0 and (x1, y1) not in dist:
                q.append((x1, y1))
                dist[(x1, y1)] = dist[(x0, y0)] + 1
                
    return -1
                

# ---- проверка: слева результат функции, справа ожидаемое ----

# по диагонали за два шага
print(shortest_path([[0, 1], [1, 0]]), 2)

# обход препятствий, четыре клетки
print(shortest_path([[0, 0, 0], [1, 1, 0], [1, 1, 0]]), 4)

# старт закрыт
print(shortest_path([[1, 0, 0], [1, 1, 0], [1, 1, 0]]), -1)

# сетка из одной свободной клетки
print(shortest_path([[0]]), 1)

# сплошная стена поперёк - пути нет
print(shortest_path([[0, 0, 0], [1, 1, 1], [0, 0, 0]]), -1)
