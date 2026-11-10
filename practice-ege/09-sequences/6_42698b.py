from pathlib import Path

# ФИПИ 42698B: Числа от 1 до 100 000. Порог — минимальное трёхзначное число файла с последней цифрой 5. В соседней паре ровно одно трёхзначное число, а сумма кратна порогу. Найти количество пар и минимальную сумму.
# https://ege.fipi.ru/bank/questions.php?search=1&proj=B9ACA5BBB2E19E434CD6BEC25284C67F&qid=42698B

def solve(a: list[int]) -> tuple[int, int | None]:
    pass




print(solve([105, 1050, 210, 5]), (2, 1155))
numbers = list(map(int, Path(__file__).with_name('17_42698B.txt').read_text(encoding='utf-8-sig').split()))
print(solve(numbers), (16, 105))
