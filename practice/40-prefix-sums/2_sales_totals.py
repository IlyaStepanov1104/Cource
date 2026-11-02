# Найди суммы значений на запрошенных отрезках.
# Для каждого (l, r) используются индексы l <= i < r. Верни ответы в порядке запросов.
# До 100000 элементов и запросов; -10**9 <= a[i] <= 10**9, 0 <= l <= r <= len(a).
# Массив между запросами не меняется. Время O(n + q).
def sales_totals(a: list[int], queries: list[tuple[int, int]]) -> list[int]:
    prefix = [0]
    for value in a:
        prefix.append(prefix[-1] + value)

    return [prefix[r] - prefix[l] for l, r in queries]


print(sales_totals([3, 1, 4, 2, 5], [(1, 4), (0, 5), (2, 2)]), [7, 15, 0])
print(sales_totals([3, 1, 4, 2, 5], [(2, 3), (4, 5)]), [4, 5])
print(sales_totals([2, -3, 4], [(0, 3), (1, 2)]), [3, -3])
print(sales_totals([], [(0, 0)]), [0])
print(sales_totals([1, 2], []), [])
