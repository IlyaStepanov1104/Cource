# Решу ЕГЭ 59833 (ЕГЭ-2023, основная волна, №9). Файл 9.txt - таблица, сохранённая как текст.
# В каждой строке шесть натуральных чисел. Сколько строк, где выполнены оба условия:
# - в строке есть только два равных числа, остальные 4 различны;
# - среднее арифметическое повторяющихся чисел меньше среднего арифметического остальных чисел строки.
def ok(row: list[int]) -> bool:
    pair = []
    other = []
    for x in row:
        if row.count(x) == 2:
            pair.append(x)
        elif row.count(x) == 1:
            other.append(x)
    if len(pair) != 2 or len(other) != 4:
        return False
    return sum(pair) / 2 < sum(other) / 4

# Сколько строк файла подходит.
def answer(path: str) -> int:
    res = 0
    for line in open(path):
        row = []
        for x in line.split():
            row.append(int(x))
        if ok(row):
            res += 1
    return res




print(ok([5, 5, 10, 20, 30, 40]), True)
print(ok([50, 50, 10, 20, 30, 40]), False)
print(ok([5, 5, 10, 10, 30, 40]), False)
print(answer('9.txt'), 1483)
