# https://leetcode.com/problems/unique-paths-ii/
# Поле из 0 и 1, 1 - препятствие. Робот ходит вправо и вниз из левого верхнего угла
# в правый нижний. Сколько существует маршрутов?
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        pass




print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)
print(Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]), 1)
