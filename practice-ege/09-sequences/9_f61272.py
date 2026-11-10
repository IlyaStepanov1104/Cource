from pathlib import Path

# ФИПИ F61272: Целые числа от −100 000 до 100 000. В соседней тройке хотя бы одно двузначное число; сумма меньше максимума среди чисел файла, оканчивающихся на 19. Найти количество троек и максимальную сумму.
# https://ege.fipi.ru/bank/questions.php?search=1&proj=B9ACA5BBB2E19E434CD6BEC25284C67F&qid=F61272

def solve(a: list[int]) -> tuple[int, int | None]:
    pass




print(solve([119, -20, 5, 300]), (1, 104))
numbers = list(map(int, Path(__file__).with_name('17_F61272.txt').read_text(encoding='utf-8-sig').split()))
print(solve(numbers), (3632, 67430))
