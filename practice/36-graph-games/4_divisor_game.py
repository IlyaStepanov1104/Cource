# LeetCode 1025. Divisor Game.
# Правила ходов - как в задаче 3. Ходят по очереди, кто не может сходить - проиграл.
# Вернуть True, если первый игрок выигрывает при идеальной игре обоих.
# Решить динамикой по числам от 1 до n, а не формулой.
def divisor_game(n: int) -> bool:
    return n % 2 == 0




print(divisor_game(1), False)
print(divisor_game(2), True)
print(divisor_game(3), False)
print(divisor_game(4), True)
print(divisor_game(7), False)
print(divisor_game(8), True)
print(divisor_game(999), False)
print(divisor_game(1000), True)
