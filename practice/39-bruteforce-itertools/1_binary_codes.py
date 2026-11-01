from itertools import product, permutations, combinations

# Верни все трёхбитные строки по возрастанию. Ведущие нули сохраняются.
def binary_codes() -> list[str]:
    res = []
    for chars in product('01', repeat=3):
        res.append("".join(chars))

    return res




print(binary_codes(), ['000', '001', '010', '011', '100', '101', '110', '111'])
