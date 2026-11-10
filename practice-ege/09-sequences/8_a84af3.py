from pathlib import Path

# ФИПИ A84AF3: Целые числа от −100 000 до 100 000. Сумма соседней пары меньше минимального положительного числа файла, кратного 21. Найти количество пар и модуль максимальной из подходящих сумм.
# https://ege.fipi.ru/bank/questions.php?search=1&proj=B9ACA5BBB2E19E434CD6BEC25284C67F&qid=A84AF3

def solve(a: list[int]) -> tuple[int, int | None]:
    pass




print(solve([21, -30, 5, -10]), (3, 5))
numbers = list(map(int, Path(__file__).with_name('17_A84AF3.txt').read_text(encoding='utf-8-sig').split()))
print(solve(numbers), (4990, 723))
