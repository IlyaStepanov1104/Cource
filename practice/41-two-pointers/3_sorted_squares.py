# LC 977: Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/
# Вернуть квадраты элементов отсортированного списка по неубыванию за O(n). Новый список ответа разрешён. Пустой вход — дополнительный тест к LC.

def sorted_squares(nums: list[int]) -> list[int]:
    res = [0] * len(nums)
    left, right = 0, len(nums) - 1
    write = len(nums) - 1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            res[write] = nums[left] ** 2
            left += 1
        else:
            res[write] = nums[right] ** 2
            right -= 1
        write -= 1
    return res




print(sorted_squares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
print(sorted_squares([-5, -3, -1]), [1, 9, 25])
print(sorted_squares([-2, 0, 2]), [0, 4, 4])
print(sorted_squares([0]), [0])
print(sorted_squares([]), [])
