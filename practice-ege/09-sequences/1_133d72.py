# ФИПИ 133D72: Числа от 1 до 100 000. В соседней паре хотя бы один остаток от деления на 55 равен минимуму всего файла. Найти количество таких пар и минимальную сумму.
# https://ege.fipi.ru/bank/questions.php?search=1&proj=B9ACA5BBB2E19E434CD6BEC25284C67F&qid=133D72

from pathlib import Path


def solve(a: list[int]):
    t = min(a)
    count = 0
    best = float('inf')

    for i in range(len(a) - 1):
        g = a[i:i+2]
        if any(x % 55 == t for x in g):
            count += 1
            best = min(best, sum(g))

    return count, best

# print(solve([2, 57, 10, 112, 5]), (4, 59))
# чтение чисел из файла - 17_133D72.txt
numbers = list(map(int, Path(__file__).with_name('17_133D72.txt').read_text().split()))
print(solve(numbers), (359, 3716))
