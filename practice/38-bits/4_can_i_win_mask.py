# LeetCode 464. Can I Win - то же самое, но позиция хранится одним числом:
# бит номер x - 1 горит, если число x уже взято.
def can_i_win(maxChoosableInteger: int, desiredTotal: int) -> bool:
    if maxChoosableInteger >= desiredTotal: 
        return True
    if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
        return False

    memory = {}

    def win(taken: int, left: int) -> bool:
        if taken in memory:
            return memory[taken]

        result = False

        for x in range(1, maxChoosableInteger + 1):
            if (taken >> (x - 1)) & 1: 
                continue
            if x >= left or not win(taken | (1 << (x-1)), left - x):
                result = True
                break
        memory[taken] = result
        return result

    return win(0, desiredTotal)



print(can_i_win(10, 11), False)
print(can_i_win(10, 0), True)
print(can_i_win(10, 1), True)
print(can_i_win(10, 40), False)
print(can_i_win(3, 4), False)
print(can_i_win(3, 5), True)
print(can_i_win(4, 6), True)
print(can_i_win(5, 50), False)
print(can_i_win(18, 79), True)
print(can_i_win(20, 210), False)
