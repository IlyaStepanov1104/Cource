# Поле из строк: '.' - свободная клетка, '#' - стена.
# Черепашка ходит только вправо и вниз из левого верхнего угла в правый нижний.
# Сколько существует маршрутов? Через стены ходить нельзя.
def grid_paths(grid: list[str]) -> int:
    n, m = len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                continue
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            up = dp[i - 1][j] if i > 0 else 0
            left = dp[i][j - 1] if j > 0 else 0
            dp[i][j] = up + left
    return dp[n - 1][m - 1]




print(grid_paths(['.....', '.....', '.....', '.....']), 35)
print(grid_paths(['.....', '..#..', '#....', '.....']), 12)
print(grid_paths(['...', '.#.', '...']), 2)
print(grid_paths(['.']), 1)
