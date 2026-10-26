# P = [130; 171]
# Q = [150; 185]
# min len(A): (x in P) -> (((X in Q) and not (x in A)) -> not (x in P))
def ok(a_0: int, a_1: int) -> bool:
    for x in range(1, 1000):
        p = 130 <= x <= 171
        q = 150 <= x <= 185
        a = a_0 <= x <= a_1
        if not (p <= ((q and not a) <= (not p))):
            return False

    return True


# Наибольшее A, при котором выражение истинно при любом x.
def answer() -> int:
    best = 10000
    for a_0 in range(100, 201):
        for a_1 in range(a_0, 201):
            if ok(a_0, a_1) and a_1 - a_0 < best:
                best = a_1 - a_0
    return best


print(answer())
