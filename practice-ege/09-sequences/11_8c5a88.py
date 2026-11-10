from pathlib import Path

# ФИПИ 8C5A88: Целые числа от −100 000 до 100 000. Все числа соседней тройки одного знака. Произведение её минимума и максимума больше квадрата минимального трёхзначного числа файла, оканчивающегося на 15. Найти количество троек и минимальное из этих произведений.
# https://ege.fipi.ru/bank/questions.php?search=1&proj=B9ACA5BBB2E19E434CD6BEC25284C67F&qid=8C5A88

def solve(a: list[int]) -> tuple[int, int | None]:
    pass




print(solve([115, 200, 300, 400]), (2, 34500))
numbers = list(map(int, Path(__file__).with_name('17_8C5A88.txt').read_text(encoding='utf-8-sig').split()))
print(solve(numbers), (3507, 863808))
