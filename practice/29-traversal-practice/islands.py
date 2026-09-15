from collections import deque


def count_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0
    
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == '1' and (x, y) not in visited:
                count += 1
                mark_island(grid, x, y, visited)
                
    return count

def mark_island(grid: list[list[str]], x, y, visited):
    rows, cols = len(grid), len(grid[0])
    q = deque([(x, y)])
    visited.add((x, y))
    
    while q:
        x_0, y_0 = q.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x_1, y_1 = x_0 + dx, y_0 + dy
            if 0 <= x_1 < rows and 0 <= y_1 < cols and grid[x_1][y_1] == '1' and (x_1, y_1) not in visited:
                visited.add((x_1, y_1))
                q.append((x_1, y_1))


# ---- проверка: слева результат функции, справа ожидаемое ----

# три острова с картинки на слайде
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(count_islands(grid))
