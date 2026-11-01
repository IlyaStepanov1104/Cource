from itertools import combinations

# Найди все пары разных товаров, суммарная цена которых не больше budget.
# items: список (уникальное название, положительная целая цена), до 20 товаров.
# budget: неотрицательное целое число. Один товар нельзя взять дважды.
# Верни список пар названий в порядке combinations(items, 2).
def shopping_pairs(items: list[tuple[str, int]], budget: int) -> list[tuple[str, str]]:
    pass




print(shopping_pairs([("рюкзак", 1000), ("термос", 700), ("фонарик", 500)], 1500),
      [("рюкзак", "фонарик"), ("термос", "фонарик")])
print(shopping_pairs([("чай", 200), ("кофе", 300)], 500), [("чай", "кофе")])
print(shopping_pairs([("чай", 200), ("кофе", 300)], 499), [])
print(shopping_pairs([("чай", 200)], 1000), [])
print(shopping_pairs([], 1000), [])
print(shopping_pairs([("чай", 200), ("кофе", 200)], 400), [("чай", "кофе")])
