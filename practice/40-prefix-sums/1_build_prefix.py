# Верни префиксные суммы: prefix[k] — сумма первых k элементов a.
# В начале обязательно 0. Исходный список не изменять.
# До 100000 целых чисел, каждое от -10**9 до 10**9.
def build_prefix(a: list[int]) -> list[int]:
    prefix = [0]
    for value in a:
        prefix.append(prefix[-1] + value)
    return prefix

print(build_prefix([3, 1, 4, 2, 5]), [0, 3, 4, 8, 10, 15])
print(build_prefix([]), [0])
print(build_prefix([2, -3, 4]), [0, 2, -1, 3])
print(build_prefix([0]), [0, 0])
