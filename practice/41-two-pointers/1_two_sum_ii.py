# LC 167: Two Sum II
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Отсортированный по неубыванию список, ровно одна пара разных индексов с суммой target. Вернуть индексы с единицы. O(n) времени, O(1) дополнительной памяти.

from itertools import combinations


def two_sum_ii(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1

    return []

def two_sum(numbers: list[int], target: int) -> list[int]:
        for i, j in combinations(range(len(numbers)), 2):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
        return []




print(two_sum_ii([2, 7, 11, 15], 9), [1, 2])
print(two_sum_ii([-3, 0, 2, 4], 1), [1, 4])
print(two_sum_ii([1, 1], 2), [1, 2])
print(two_sum_ii([2, 3, 4], 6), [1, 3])
