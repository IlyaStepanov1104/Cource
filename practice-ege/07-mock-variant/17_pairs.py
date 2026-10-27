# Решу ЕГЭ 51986, №17. Файл 17.txt - целые числа, по модулю не больше 10 000, по одному в строке.
# Пара - два идущих подряд элемента. Найдите количество пар, в которых меньший элемент оканчивается на 5,
# а сумма квадратов элементов пары меньше квадрата наименьшего из чисел файла, оканчивающихся на 5.
# Затем - максимальную сумму квадратов таких пар.
def read_numbers(path: str) -> list[int]:
    nums = []
    for line in open(path):
        nums.append(int(line))
    return nums


# Число оканчивается цифрой 5 (у отрицательных тоже).
def ends_with_5(x: int) -> bool:
    return abs(x) % 10 == 5


# Количество пар и максимальная сумма квадратов.
def answer(nums: list[int]) -> tuple[int, int]:
    min5 = float('inf')
    for x in nums:
        if ends_with_5(x) and x < min5:
            min5 = x

    count = 0
    best = 0
    for i in range(len(nums) - 1):
        a, b = nums[i], nums[i + 1]
        s = a**2 + b**2
        if ends_with_5(min(a, b)) and s < min5**2:
            count += 1
            best = max(best, s)
    return count, best



print(answer([-15, 20, 5, 7]), (1, 74))
print(answer(read_numbers('17.txt')), (403, 99805561))
