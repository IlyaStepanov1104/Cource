from itertools import product, permutations, combinations

# Верни все команды из двух участников A, B, C. Состав важен, порядок нет. Формат: строки AB, AC, BC.
def teams() -> list[str]:
    res = []
    for chars in combinations('ABC', 2):
        res.append(''.join(chars))
    return res




print(teams(), ['AB', 'AC', 'BC'])
