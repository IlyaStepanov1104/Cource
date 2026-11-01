from itertools import product, permutations, combinations

# Верни двоичные коды длины 4 с ровно двумя единицами без подстроки 11. Порядок лексикографический.
def nonadjacent_ones() -> list[str]:
    res = []
    for chars in product('01', repeat=4):
        word = ''.join(chars)
        if word.count('1') == 2 and '11' not in word:
            res.append(word)
    return res




print(nonadjacent_ones(), ['0101', '1001', '1010'])
