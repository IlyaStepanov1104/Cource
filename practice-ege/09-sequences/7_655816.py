from pathlib import Path

# ФИПИ 655816: Целые числа от −100 000 до 100 000. Соседняя пара содержит хотя бы одно отрицательное число; её сумма меньше количества чисел файла, кратных 32. Найти количество пар и максимальную сумму.
# https://ege.fipi.ru/bank/questions.php?search=1&proj=B9ACA5BBB2E19E434CD6BEC25284C67F&qid=655816

def solve(a: list[int]) -> tuple[int, int | None]:
    pass




print(solve([32, -31, 0, -2, 64]), (3, 1))
numbers = list(map(int, Path(__file__).with_name('17_655816.txt').read_text(encoding='utf-8-sig').split()))
print(solve(numbers), (4969, 299))
