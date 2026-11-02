# Есть ли непустой подотрезок с суммой target? Верни bool.
# До 100000 целых элементов; a[i] и target от -10**9 до 10**9.
# Ожидаемое время O(n), память O(n).
def has_target_sum(a: list[int], target: int) -> bool:
    seen = {0}
    current = 0
    for value in a:
        current += value
        if current - target in seen:
            return True
        seen.add(current)
    return False


print(has_target_sum([3, -1, 4, -2], 3), True)
print(has_target_sum([2, -1, 3], 3), True)
print(has_target_sum([2, -1, 3], 8), False)
print(has_target_sum([5], 0), False)
print(has_target_sum([0], 0), True)
print(has_target_sum([], 0), False)
print(has_target_sum([-3, 1], -2), True)
