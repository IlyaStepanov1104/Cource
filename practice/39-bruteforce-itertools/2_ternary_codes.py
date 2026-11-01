from itertools import product, permutations, combinations

# Верни все коды длины 3 из 012 в лексикографическом порядке. Используй вложенные циклы.
def ternary_codes() -> list[str]:
    res = []
    for chars in product('012', repeat=3):
        res.append(''.join(chars))
    return res




def inspect_result(value, mode):
    if value is None:
        return None
    if mode == "length":
        return len(value)
    if mode == "first":
        return value[:4]
    return value[-1]

print(inspect_result(ternary_codes(), 'length'), 27)
print(inspect_result(ternary_codes(), 'first'), ['000', '001', '002', '010'])
print(inspect_result(ternary_codes(), 'last'), '222')
