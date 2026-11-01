from itertools import product, permutations, combinations

# Верни пары различных чисел с суммой target. Числа во входе не повторяются. Порядок результата как у combinations.
def pair_sum(numbers: list[int], target: int) -> list[tuple[int, int]]:
    # return [(a, b) for a, b in combinations(numbers, 2) if a + b == target]
    res = []
    for a, b in combinations(numbers, 2):
        if a + b == target:
            res.append((a, b))
    return res




print(pair_sum([1, 2, 3, 4, 5], 6), [(1, 5), (2, 4)])
print(pair_sum([3], 6), [])
print(pair_sum([-2, 0, 2], 0), [(-2, 2)])
