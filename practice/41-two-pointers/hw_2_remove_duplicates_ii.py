# LC 80: Remove Duplicates II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Обязательное ДЗ. Оставить максимум две копии каждого значения в отсортированном списке. Менять на месте, вернуть k. Проверяются первые k ячеек. O(n) времени, O(1) памяти.

def remove_duplicates_ii(nums: list[int]) -> int:
    pass




def check(values):
    nums = values.copy()
    k = remove_duplicates_ii(nums)
    if k is None:
        return None
    return k, nums[:k]

print(check([1, 1, 1, 2, 2, 3]), (5, [1, 1, 2, 2, 3]))
print(check([0, 0, 1, 1, 1, 1, 2, 3, 3]), (7, [0, 0, 1, 1, 2, 3, 3]))
print(check([4, 4, 4, 4]), (2, [4, 4]))
print(check([]), (0, []))
