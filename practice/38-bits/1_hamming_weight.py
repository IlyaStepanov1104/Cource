# LeetCode 191. Number of 1 Bits.
# Дано неотрицательное целое n. Вернуть, сколько единиц в его двоичной записи.
# Без bin() и строк: только операции с битами.
def hamming_weight(n: int) -> int:
    count = 0
    while n > 0:
        count += n & 1
        n = n >> 1
    return count


print(hamming_weight(11), 3)
print(hamming_weight(128), 1)
print(hamming_weight(0), 0)
print(hamming_weight(13), 3)
print(hamming_weight(255), 8)
print(hamming_weight(2147483645), 30)
