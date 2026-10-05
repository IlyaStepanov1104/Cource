# https://leetcode.com/problems/parallel-courses-iii/
# n курсов (нумерация с 1), relations[i] = [a, b]: курс a нужно пройти до курса b.
# time[i] - сколько месяцев идёт курс i + 1. Курсы без зависимостей можно проходить одновременно.
# За сколько месяцев можно пройти все курсы?
class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        pass




print(Solution().minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5]), 8)
print(Solution().minimumTime(5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]), 12)
