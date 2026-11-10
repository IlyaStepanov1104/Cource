from pathlib import Path

# ФИПИ 8FBD47: Числа от 1 до 100 000. Найти минимум среди кратных 21. В соседней паре хотя бы одно число должно делиться на этот минимум. Вывести количество пар и максимальную сумму.
# https://ege.fipi.ru/bank/questions.php?search=1&proj=B9ACA5BBB2E19E434CD6BEC25284C67F&qid=8FBD47

def solve(a: list[int]) -> tuple[int, int | None]:
    pass




print(solve([21, 42, 5, 63, 8]), (4, 71))
numbers = list(map(int, Path(__file__).with_name('17_8FBD47.txt').read_text(encoding='utf-8-sig').split()))
print(solve(numbers), (126, 171120))
