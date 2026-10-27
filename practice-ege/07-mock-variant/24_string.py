# Решу ЕГЭ 58328, №24. Файл 24.txt - одна строка из цифр (не больше 10^6 символов).
# Определите максимальное количество идущих подряд цифр, среди которых каждые две соседние различны.
def longest(s: str) -> int:
    best = 1
    cur = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            cur += 1
        else:
            cur = 1
        best = max(best, cur)
    return best




print(longest('1122'), 2)
print(longest('5'), 1)
print(longest('12113434'), 5)
print(longest(open('24.txt').readline().strip()), 90)
