# LC 977: Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/
# Вернуть квадраты элементов отсортированного списка по неубыванию за O(n). Новый список ответа разрешён. Пустой вход — дополнительный тест к LC.

def sorted_squares(nums: list[int]) -> list[int]:
    pass




print(sorted_squares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
print(sorted_squares([-5, -3, -1]), [1, 9, 25])
print(sorted_squares([-2, 0, 2]), [0, 4, 4])
print(sorted_squares([0]), [0])
print(sorted_squares([]), [])
