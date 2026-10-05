import csv
from pathlib import Path

# ЕГЭ №18. Робот стоит в левой верхней клетке поля и за один ход идёт вправо или вниз.
# В каждой клетке лежит монета. Робот собирает монеты во всех клетках, через которые прошёл,
# включая первую и последнюю. Найти максимальную и минимальную сумму, которую он может
# собрать по пути в правую нижнюю клетку.
# Поле лежит в файле ege18_coins.csv, числа в строке разделены ';'.
def read_grid(path: str) -> list[list[int]]:
    pass


def max_min_sum(grid: list[list[int]]) -> tuple[int, int]:
    pass




print(max_min_sum([[1, 8, 8], [1, 1, 8], [9, 1, 1]]), (26, 5))
print(max_min_sum([[5, 1], [2, 7]]), (14, 13))
print(max_min_sum([[42]]), (42, 42))

print(max_min_sum(read_grid(str(Path(__file__).parent / 'ege18_coins.csv'))))
