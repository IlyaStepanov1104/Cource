from itertools import product, permutations, combinations

# Верни коды длины length из alphabet в порядке product. Символы alphabet различны, length >= 0.
def make_codes(alphabet: str, length: int) -> list[str]:
    # res = []
    # for chars in product(alphabet, repeat=length):
    #     res.append(''.join(chars))
    # return res
    return [''.join(chars) for chars in product(alphabet, repeat=length)]



print(make_codes("01", 2), ['00', '01', '10', '11'])
print(make_codes("ABC", 1), ['A', 'B', 'C'])
print(make_codes("01", 0), [''])
