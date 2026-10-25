# Задание ФИПИ 2EE07F.
# ДЕЛ(n, m) - «n делится без остатка на m». Отрезок B = [50; 70].
# Для какого наибольшего натурального A выражение
# ДЕЛ(x, A) ∨ ((x ∈ B) → ¬ДЕЛ(x, 15))
# истинно при любом натуральном x?
def ok(a: int) -> bool:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((x + y <= 33) or (y <= x + 9) or (y >= a)):
                return False

    return True


# Наибольшее A, при котором выражение истинно при любом x.
def answer() -> int:
    best = 0
    for a in range(1000):
        if ok(a):
            best = a
    return best



print(ok(0))
print(ok(120000))
print(answer())
