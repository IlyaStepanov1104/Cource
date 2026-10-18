# LeetCode 338. Counting Bits.
# Дано n. Вернуть список ans длины n + 1, где ans[i] - количество единиц в двоичной записи i.
# Попробуйте за один проход: ans[i] связан с ans[i >> 1].
def count_bits(n: int) -> list[int]:
    pass




print(count_bits(2), [0, 1, 1])
print(count_bits(5), [0, 1, 1, 2, 1, 2])
print(count_bits(0), [0])
print(count_bits(8), [0, 1, 1, 2, 1, 2, 2, 3, 1])
