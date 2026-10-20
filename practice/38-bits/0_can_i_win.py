# LeetCode 464. Can I Win.
# Числа от 1 до max_choosable, каждое можно взять только один раз. Двое по очереди берут число
# и прибавляют к общей сумме. Кто первым довёл сумму до desired_total или больше - выиграл.
# Вернуть True, если первый игрок выигрывает при идеальной игре обоих.
def can_i_win(maxChoosableInteger: int, desiredTotal: int) -> bool:
    if maxChoosableInteger >= desiredTotal: 
        return True
    if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
        return False

    memory = {}

    def win(taken: tuple[int, ...]) -> bool:
        if taken in memory:
            return memory[taken]

        left = desiredTotal - sum(taken)
        result = False

        for x in range(1, maxChoosableInteger + 1):
            if x in taken: continue
            if x >= left or not win(tuple(sorted(taken + (x, )))):
                result = True
                break
        memory[taken] = result
        return result

    return win(())
    


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
