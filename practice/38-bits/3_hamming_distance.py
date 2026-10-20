# LeetCode 461. Hamming Distance.
# Даны два неотрицательных числа x и y. Вернуть, в скольких разрядах их двоичные записи различаются.
def hamming_distance(x: int, y: int) -> int:
    diff = x ^ y
    count = 0
    while diff > 0:
        count += diff & 1
        diff >>= 1
    return count


print(hamming_distance(1, 4), 2)
print(hamming_distance(3, 1), 1)
print(hamming_distance(13, 24), 3)
print(hamming_distance(7, 7), 0)
print(hamming_distance(0, 255), 8)
