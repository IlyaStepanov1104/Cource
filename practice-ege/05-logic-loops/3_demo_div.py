# Демо ЕГЭ-2027, №15.
# ДЕЛ(n, m) - «n делится без остатка на m». Отрезок B = [70; 90].
# Для какого наибольшего натурального A выражение
# ДЕЛ(x, A) ∨ ((x ∈ B) → ¬ДЕЛ(x, 22))
# истинно при любом натуральном x?
def ok(a: int) -> bool:
    for x in range(1, 1000):
        if not (x % a == 0 or ((70 <= x <= 90) <= (x % 22 != 0))):
            return False
    return True

# Наибольшее A, при котором выражение истинно при любом x.
def answer() -> int:
    # best = 0
    # for a in range(1, 1000):
    #     if ok(a):
    #         best = a
    # return best
    for a in range(1000, 0, -1):
        if ok(a):
            return a




print(ok(88), True)
print(ok(88 + 1), False)
print(answer(), 88)
