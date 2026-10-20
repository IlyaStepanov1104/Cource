# Задание ФИПИ 4D0976.
# По числу N строим R: берём двоичную запись N.
# Если N чётное - слева дописываем 10.
# Если N нечётное - слева дописываем 1, справа 01.
def build_r(n: int) -> int:
    s = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + s
    else:
        r = '1' + s + '01'
    return int(r, 2)


# Минимальное N, при котором R больше 441.
def answer() -> int:
    for n in range(1, 1000):
        r = build_r(n)
        if r > 441:
            return n




print(build_r(4), 20)
print(build_r(5), 53)
print(answer(), 47)
