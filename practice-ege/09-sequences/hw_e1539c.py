from pathlib import Path

# ФИПИ E1539C: Числа от 1 до 100 000. В соседней паре хотя бы одно трёхзначное число; сумма кратна минимальному трёхзначному числу файла, оканчивающемуся на 5. Найти количество пар и максимальную сумму.
# https://ege.fipi.ru/bank/questions.php?search=1&proj=B9ACA5BBB2E19E434CD6BEC25284C67F&qid=E1539C

def solve(a: list[int]) -> tuple[int, int | None]:
    pass




print(solve([105, 210, 1050, 5]), (2, 1260))
numbers = list(map(int, Path(__file__).with_name('17_E1539C.txt').read_text(encoding='utf-8-sig').split()))
print(solve(numbers))
