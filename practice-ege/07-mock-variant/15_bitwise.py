# Решу ЕГЭ 34513, №15.
# m & n - поразрядная конъюнкция. Для какого наименьшего неотрицательного A формула
# x & 33 = 0 -> (x & 45 != 0 -> x & A != 0)
# истинна при любом неотрицательном x?
def ok(a: int) -> bool:
    for x in range(0, 1000):
        if not ((((x) & (33)) == 0) <= (((x) & (45) !=0) <= ((x) & (a) !=0))):
            return False
    return True

# Наименьшее подходящее A.
def answer():
    for a in range(1000):
        if ok(a):
            return a




print(ok(11), False)
print(ok(12), True)
print(answer(), 12)
