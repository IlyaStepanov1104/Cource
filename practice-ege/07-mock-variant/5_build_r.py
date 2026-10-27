# Решу ЕГЭ 69909 (ЕГЭ-2024, основная волна, №5).
# По числу N строим R: берём двоичную запись N.
# Если N чётное - слева дописываем 10.
# Если N нечётное - справа дописываем 00, слева 1.
def built(n):
    s = bin(n)[2:]
    if n%2==0:
        s = '10' + s
    else:
        s = '1' + s + '00'
    return int(s, 2)

def answer():
    for n in range(1, 13):
        r = built(n)
        print(r)
print(answer())


print(answer(), 108)
