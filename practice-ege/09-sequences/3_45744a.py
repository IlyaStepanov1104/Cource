from pathlib import Path

# ФИПИ 45744A: Числа от 1 до 100 000. В соседней паре сумма двух остатков от деления на 15 равна минимуму файла. Найти количество пар и минимальную сумму их элементов.
# https://ege.fipi.ru/bank/questions.php?search=1&proj=B9ACA5BBB2E19E434CD6BEC25284C67F&qid=45744A

def solve(a: list[int]) -> tuple[int, int | None]:
    pass




print(solve([2, 15, 17, 30, 4]), (3, 17))
numbers = list(map(int, Path(__file__).with_name('17_45744A.txt').read_text(encoding='utf-8-sig').split()))
print(solve(numbers), (365, 5888))
