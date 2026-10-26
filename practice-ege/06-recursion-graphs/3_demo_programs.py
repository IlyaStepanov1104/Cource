# Демо ЕГЭ-2027, №13.
# Исполнитель преобразует число на экране. Команды:
# A. Прибавь 1
# B. Поменяй местами - применяется, только если цифра десятков меньше цифры единиц,
#    и меняет местами две младшие цифры (113 -> 131).
# Сколько существует программ, для которых при исходном числе 100 результатом является число 141?
# Сколько программ переводят число a в число b.
def count(current: int, end: int) -> int:
    # Не через 120
    if current == 120: return 0
    if current == end:
        return 1
    if current > end:
        return 0
    res = count(current + 1, end)
    tens = current // 10 % 10
    units = current % 10
    if tens < units:
        res += count(current // 100 * 100 + units * 10 + tens, end)
    return res



print(count(13, 14), 1)
print(count(113, 131), 2)
print(count(100, 141), 16)

# Обязательно через 114
print(count(100, 114) * count(114, 141))
