# LeetCode 136. Single Number.
# В списке каждое число встречается ровно два раза, и только одно - один раз. Найти его.
# Без словарей и множеств: один проход и одна переменная.
def single_number(nums: list[int]) -> int:
    # d = {}
    # for n in nums:
    #     if n not in d:
    #         d[n] = 1
    #     else:
    #         d[n] += 1 
    # for k, v in d:
    #     if v == 1:
    #         return k

    result = 0
    for x in nums:
        result ^= x
    return result


print(single_number([2, 2, 1]), 1)
print(single_number([4, 1, 2, 1, 2]), 4)
print(single_number([1]), 1)
print(single_number([7, 3, 5, 3, 7]), 5)
print(single_number([-1, 6, 6]), -1)
