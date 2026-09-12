from collections import deque


def grid_shortest(grid: list, start: tuple, target: tuple):
    rows, cols = len(grid), len(grid[0])
    dist = {start: 0}
    parent = {start: None}
    q = deque([start])
    
    while q:
        x_0, y_0 = q.popleft()
        
        if (x_0, y_0) == target:
            path = []
            cur =  target
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            
            path.reverse()
            return dist[(x_0, y_0)], path
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x_1, y_1 = x_0 + dx, y_0 + dy
            if 0 <= x_1 < rows and 0 <= y_1 < cols and grid[x_1][y_1] != '#' and (x_1, y_1) not in dist:
                dist[(x_1, y_1)] = dist[(x_0, y_0)] + 1
                parent[(x_1, y_1)] = (x_0, y_0)
                q.append((x_1, y_1))
                
    return -1, []

def print_path(grid, path):
    grid_chars = [list(row) for row in grid]
    
    for x, y in path:
        if grid_chars[x][y] == '.':
            grid_chars[x][y] = '+'
        
    for row in grid_chars:
        print(''.join(row))
    

# ---- проверка: слева результат функции, справа ожидаемое ----

maze = [
    "S..#.",
    "##.#.",
    ".....",
    ".###.",
    "....T",
]

# лабиринт со слайда: путь есть за 8 шагов
dist, path = grid_shortest(maze, (0, 0), (4, 4))
print(*maze, sep='\n')
print(dist, 8)
print_path(maze, path)

# соседняя клетка - один шаг
dist, path = grid_shortest(maze, (0, 0), (0, 1))
print(*maze, sep='\n')
print(dist, 1)
print_path(maze, path)

# старт и цель совпадают - ноль шагов
dist, path = grid_shortest(maze, (2, 2), (2, 2))
print(*maze, sep='\n')
print(dist, 0)
print_path(maze, path)

# цель за сплошной стеной - пути нет
walled = [
    "...",
    "###",
    "..T",
]
dist, path = grid_shortest(walled, (0, 0), (2, 2))
print(*walled, sep='\n')
print(dist, -1)
print_path(walled, path)

# длинный обход вокруг перегородок
snake = [
    "S.....",
    "#####.",
    "......",
    ".#####",
    ".....T",
]
dist, path = grid_shortest(snake, (0, 0), (4, 5))
print(*snake, sep='\n')
print(dist, 19)
print_path(snake, path)
