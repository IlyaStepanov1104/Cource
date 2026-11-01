from itertools import product, permutations, combinations

# Верни коды длины 3 из 012 с суммой цифр target в лексикографическом порядке.
def digit_sum_codes(target: int) -> list[str]:
    res = []
    for a, b, c in product('012', repeat=3):
        if int(a) + int(b) + int(c) == target:
            res.append(a + b + c)

    return res
            

print(digit_sum_codes(3), ['012', '021', '102', '111', '120', '201', '210'])
print(digit_sum_codes(0), ['000'])
print(digit_sum_codes(7), [])
