# LC 26: Remove Duplicates
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Изменить отсортированный список на месте: первые k элементов — разные значения в исходном порядке. Вернуть k. Хвост игнорируется. O(n) времени, O(1) памяти. Пустой вход поддерживаем дополнительно к LC.

def remove_duplicates(nums: list[int]) -> int:
    write = 0
    for read in range(len(nums)):
        if write == 0 or nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write




def check(values):
    nums = values.copy()
    k = remove_duplicates(nums)
    if k is None:
        return None
    return k, nums[:k]

print(check([1, 1, 2, 2, 3]), (3, [1, 2, 3]))
print(check([5, 5, 5]), (1, [5]))
print(check([-2, -2, 0, 3, 3]), (3, [-2, 0, 3]))
print(check([]), (0, []))
