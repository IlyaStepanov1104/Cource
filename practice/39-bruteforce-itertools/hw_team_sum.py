from itertools import product, permutations, combinations

# ДЗ по желанию: верни команды из k чисел с суммой target. Числа различны, их не больше 12; 1 <= k <= len(numbers). Порядок как у combinations.
def team_sum(numbers: list[int], k: int, target: int) -> list[tuple[int, ...]]:
    pass




print(team_sum([1, 2, 3, 4, 5], 3, 9), [(1, 3, 5), (2, 3, 4)])
print(team_sum([1, 2], 2, 10), [])
