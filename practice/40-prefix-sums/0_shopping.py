from itertools import combinations

# Найди пары разных товаров с суммой цен не больше budget.
# До 20 товаров: (уникальное название, положительная целая цена). budget >= 0.
# Верни пары названий в порядке combinations(items, 2), без обратных дублей.
def shopping_pairs(items: list[tuple[str, int]], budget: int) -> list[tuple[str, str]]:
    pass




print(shopping_pairs([("рюкзак", 1000), ("термос", 700), ("фонарик", 500)], 1500),
      [("рюкзак", "фонарик"), ("термос", "фонарик")])
print(shopping_pairs([("чай", 200), ("кофе", 300)], 500), [("чай", "кофе")])
print(shopping_pairs([("чай", 200), ("кофе", 300)], 499), [])
print(shopping_pairs([("чай", 200)], 1000), [])
print(shopping_pairs([], 1000), [])
print(shopping_pairs([("чай", 200), ("кофе", 200)], 400), [("чай", "кофе")])

