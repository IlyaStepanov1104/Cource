from itertools import product, permutations, combinations

# Верни все расстановки двух разных букв из ABC. Порядок букв важен; порядок списка как у permutations.
def arrangements() -> list[str]:
    res = []
    for chars in permutations('ABC', 2):
        res.append(''.join(chars))
    return res




print(arrangements(), ['AB', 'AC', 'BA', 'BC', 'CA', 'CB'])
