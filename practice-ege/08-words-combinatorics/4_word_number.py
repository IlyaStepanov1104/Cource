from itertools import product

def first_number() -> int:
    count = 1
    for chars in product('ВЕКНО', repeat=5):
        if chars[0] != 'О':
            count += 1
        else:
            return count




print(first_number(), 2501)
