from pathlib import Path

# ФИПИ CF2AF3: Целые числа от −100 000 до 100 000. В соседней тройке ровно два трёхзначных числа; сумма не больше максимума среди чисел файла, оканчивающихся на 21. Найти количество троек и максимальную сумму.
# https://ege.fipi.ru/bank/questions.php?search=1&proj=B9ACA5BBB2E19E434CD6BEC25284C67F&qid=CF2AF3

def solve(a: list[int]):
    t = max(x for x in a if abs(x) % 100 == 21)
    count = 0
    best = float('-inf')
    for i in range(len(a) - 2):
        g = a[i:i+3]
        if sum(100 <= abs(x) <= 999 for x in g) == 2 and sum(g) <= t:
            count += 1
            best = max(best, sum(g))
    return count, best


print(solve([121, -100, 5, 200, 21]), (2, 105))
numbers = list(map(int, Path(__file__).with_name('17_CF2AF3.txt').read_text(encoding='utf-8-sig').split()))
print(solve(numbers), (1169, 95216))
