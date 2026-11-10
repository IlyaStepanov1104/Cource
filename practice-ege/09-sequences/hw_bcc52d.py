from pathlib import Path

# ФИПИ BCC52D: Числа от 1 до 100 000. В соседней тройке ровно одно двузначное число; сумма не меньше максимума среди чисел файла, оканчивающихся на 13. Найти количество троек и максимальную сумму.
# https://ege.fipi.ru/bank/questions.php?search=1&proj=B9ACA5BBB2E19E434CD6BEC25284C67F&qid=BCC52D

def solve(a: list[int]) -> tuple[int, int | None]:
    pass




print(solve([113, 20, 5, 200, 7]), (2, 225))
numbers = list(map(int, Path(__file__).with_name('17_BCC52D.txt').read_text(encoding='utf-8-sig').split()))
print(solve(numbers))
