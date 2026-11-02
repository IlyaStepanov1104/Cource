# Дано мультимножество из n=len(a) целых чисел, n>=1.
# Верни индексы любого непустого подмножества, сумма которого делится на n.
# Индексы различны; равные значения в разных позициях можно выбирать отдельно.
# 1 <= n <= 100000, -10**9 <= a[i] <= 10**9. Найди решение за O(n) и объясни, почему оно существует.
def divisible_subset(a: list[int]):
    n = len(a)
    first = [-1] * n
    first[0] = 0
    current = 0

    for i in range(n):
        current = (current + a[i]) % n

        if first[current] != -1:
            return first[current], i + 1

        first[current] = i + 1

    return None


def check_subset(a: list[int], indices: list[int] | None) -> bool | None:
    if indices is None:
        return None
    if not indices or len(indices) != len(set(indices)):
        return False
    if not all(0 <= i < len(a) for i in indices):
        return False
    return sum(a[i] for i in indices) % len(a) == 0


for a in ([2, 2, 3], [1, 1, 1], [-2, 5, 4], [7], [0, 0], [1, 2, 4, 8]):
    print(check_subset(a, divisible_subset(a)), True)