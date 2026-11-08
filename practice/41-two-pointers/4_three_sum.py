# LC 15: 3Sum
# https://leetcode.com/problems/3sum/
# Вернуть все различные по значениям тройки с суммой 0. Индексы внутри тройки различны. Повторы значений допустимы, повторы троек нет. Порядок ответа не важен. Цель O(n²).

def three_sum(nums: list[int]) -> list[list[int]]:
    pass




def normalize(result):
    if result is None:
        return None
    return sorted(sorted(triple) for triple in result)

print(normalize(three_sum([-2, 0, 1, 1, 2])), [[-2, 0, 2], [-2, 1, 1]])
print(normalize(three_sum([-2, 0, 0, 2, 2])), [[-2, 0, 2]])
print(normalize(three_sum([0, 0, 0, 0])), [[0, 0, 0]])
print(normalize(three_sum([0, 1, 1])), [])
