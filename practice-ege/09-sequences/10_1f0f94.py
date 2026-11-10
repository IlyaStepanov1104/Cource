from pathlib import Path

# ФИПИ 1F0F94: Целые числа от −100 000 до 100 000. В соседней тройке ровно два двузначных числа; квадрат суммы меньше максимума среди чисел файла, оканчивающихся на 33. Найти количество троек и максимальную сумму.
# https://ege.fipi.ru/bank/questions.php?search=1&proj=B9ACA5BBB2E19E434CD6BEC25284C67F&qid=1F0F94

def solve(a: list[int]) -> tuple[int, int | None]:
    pass




print(solve([133, 10, -20, 5, 30]), (1, -5))
numbers = list(map(int, Path(__file__).with_name('17_1F0F94.txt').read_text(encoding='utf-8-sig').split()))
print(solve(numbers), (68, 306))
