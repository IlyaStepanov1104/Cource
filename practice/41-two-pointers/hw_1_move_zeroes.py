# LC 283: Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# Обязательное ДЗ. Перенести нули в конец входного списка на месте, сохранив порядок остальных. Возвращать None. O(n) времени и O(1) памяти.

def move_zeroes(nums: list[int]) -> None:
    pass




def check(values):
    nums = values.copy()
    returned = move_zeroes(nums)
    if returned is not None:
        return "Expected return None"
    if nums == values and 0 in values and any(value != 0 for value in values[values.index(0) + 1:]):
        return None
    return nums

print(check([0, 4, 0, -2, 3]), [4, -2, 3, 0, 0])
print(check([0, 0]), [0, 0])
print(check([1, 2]), [1, 2])
print(check([]), [])
