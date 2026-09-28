# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# n городов с номерами от 0 до n - 1 и n - 1 дорога, все дороги
# односторонние. Разрешили развернуть любые дороги. Найти минимальное
# число разворотов, после которых из каждого города можно доехать до 0.


def min_reorder(n: int, connections: list[list[int]]) -> int:
    pass


print(min_reorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]), 3)
print(min_reorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]), 2)
print(min_reorder(3, [[1, 0], [2, 0]]), 0)
