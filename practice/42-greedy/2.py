from itertools import combinations


def greedy_backpack(items, capacity):
    result = []
    remainder = capacity

    for item in sorted(items, key=lambda item: item[2], reverse=True):
        name, weight, cost = item
        if weight <= remainder:
            result.append(item)
            remainder -= weight

    return result

def exect_backpack(items, capacity):
    best = []
    best_cost = 0

    for count in range(len(items) + 1):
        for variant in combinations(items, count):
            weight = sum(item[1] for item in variant)
            cost = sum(item[2] for item in variant)

            if weight <= capacity and cost > best_cost:
                best = list(variant)
                best_cost = cost
    return best


def describe(items):
    return (
        [item[0] for item in items],
        sum(item[1] for item in items),
        sum(item[2] for item in items),
    )

items = [('Телефон', 20, 3500), ('Наушники', 25, 2000), ('Ручка', 45, 4000),]
CAPACITY = 45


print('Жадный:', describe(greedy_backpack(items, CAPACITY)))
print('Точный:', describe(exect_backpack(items, CAPACITY)))