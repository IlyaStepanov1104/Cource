from pathlib import Path

# ФИПИ FCE3BE: Числа от 1 до 100 000. В соседней паре ровно одно двузначное число; сумма кратна максимальному двузначному числу файла. Найти количество пар и максимальную сумму.
# https://ege.fipi.ru/bank/questions.php?search=1&proj=B9ACA5BBB2E19E434CD6BEC25284C67F&qid=FCE3BE

def solve(a: list[int]) -> tuple[int, int | None]:
    pass




print(solve([12, 100, 24, 120, 8]), (1, 144))
numbers = list(map(int, Path(__file__).with_name('17_FCE3BE.txt').read_text(encoding='utf-8-sig').split()))
print(solve(numbers), (16, 9702))
