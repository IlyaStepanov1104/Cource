# Два массива одинаковой длины. Найди непустой [l, r), на котором их суммы равны.
# Верни любые границы (l, r) или None, если решения нет. Правая граница исключена.
# До 100000 элементов, значения от -10**9 до 10**9. Ожидаемое время O(n).
def equal_sum_segment(a: list[int], b: list[int]) -> tuple[int, int] | None:
    first = {0: 0}
    current = 0

    for i in range(len(a)):
        current += a[i] - b[i]

        if current in first:
            return first[current], i + 1

        first[current] = i + 1

    return None
        




def check_segment(a: list[int], b: list[int], result: tuple[int, int] | None) -> bool | None:
    if result is None:
        return None
    l, r = result
    return 0 <= l < r <= len(a) and sum(a[l:r]) == sum(b[l:r])


a, b = [2, 5, 1, 4], [1, 3, 4, 8]
print(check_segment(a, b, equal_sum_segment(a, b)), True)
a, b = [5, 2], [8, 2]
print(check_segment(a, b, equal_sum_segment(a, b)), True)
a, b = [-2, 3], [1, 0]
print(check_segment(a, b, equal_sum_segment(a, b)), True)
print(equal_sum_segment([1, 2], [3, 4]), None)
print(equal_sum_segment([], []), None)
