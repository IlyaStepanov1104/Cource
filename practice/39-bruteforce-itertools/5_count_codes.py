from itertools import product, permutations, combinations

# Посчитай коды длины length из 012, которые не начинаются с 0. length >= 1. Не сохраняй все коды.
def count_codes(length: int) -> int:
    count = 0
    for chars in product('012', repeat=length):
        if chars[0] != '0':
            count += 1
    return count


print(count_codes(5), 162)
print(count_codes(1), 2)
