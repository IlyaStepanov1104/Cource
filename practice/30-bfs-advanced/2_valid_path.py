from collections import deque


# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
# В каждой клетке нарисована стрелка: 1 вправо, 2 влево, 3 вниз, 4 вверх.
# Идти можно в любую из 4 сторон: по стрелке бесплатно,
# в любую другую сторону - развернуть стрелку за 1 монету.
# Вернуть минимальное число монет, чтобы дойти из (0, 0) в правый нижний угол.


def min_cost(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    MOVES = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
    
    dist = {(0, 0): 0}
    dq = deque([(0, 0)])
    
    while dq:
        x_0, y_0 = dq.popleft()
        d = dist[(x_0, y_0)]
        
        for arrow, (dx, dy) in MOVES.items():
            x_1, y_1 = x_0 + dx, y_0 + dy
            if 0 <= x_1 < rows and 0 <= y_1 < cols:
                w = 0 if grid[x_0][y_0] == arrow else 1
                if (x_1, y_1) not in dist or d + w < dist[(x_1, y_1)]:
                    dist[(x_1, y_1)] = d + w
                    if w == 0:
                        dq.appendleft((x_1, y_1))
                    else:
                        dq.append((x_1, y_1))

    return dist[(rows - 1, cols - 1)]


print(min_cost([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]), 3)
print(min_cost([[1, 1, 3], [3, 2, 2], [1, 1, 4]]), 0)
print(min_cost([[1, 2], [4, 3]]), 1)
print(min_cost([[2, 2, 2], [2, 2, 2]]), 3)
print(min_cost([[4]]), 0)
