# LC 15: 3Sum
# https://leetcode.com/problems/3sum/
# Вернуть все различные по значениям тройки с суммой 0. Индексы внутри тройки различны. Повторы значений допустимы, повторы троек нет. Порядок ответа не важен. Цель O(n²).

def three_sum(nums: list[int]) -> list[list[int]]:
    values = sorted(nums)
    result = []
    for i in range(len(values) - 2):
        if i > 0 and values[i] == values[i - 1]:
            continue
        left, right = i + 1, len(values) - 1
        while left < right:
            total = values[i] + values[left] + values[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([values[i], values[left], values[right]])
                left += 1
                right -= 1
                while left < right and values[left] == values[left - 1]:
                    left += 1
                while left < right and values[right] == values[right + 1]:
                    right -= 1

    return result

def normalize(result):
    if result is None:
        return None
    return sorted(sorted(triple) for triple in result)

print(normalize(three_sum([-2, 0, 1, 1, 2])), [[-2, 0, 2], [-2, 1, 1]])
print(normalize(three_sum([-2, 0, 0, 2, 2])), [[-2, 0, 2]])
print(normalize(three_sum([0, 0, 0, 0])), [[0, 0, 0]])
print(normalize(three_sum([0, 1, 1])), [])
