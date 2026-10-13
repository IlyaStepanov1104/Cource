# Задание ФИПИ, группа 2B23FD (там №19 «при любом ходе Пети»: ответ 14). Здесь №19 - как в демо 2027: «Ваня выиграл первым ходом».
# Куча из s камней, 1 <= s <= 28. Ход: добавить 1 камень или увеличить кучу в 2 раза.
# Игра кончается, когда камней не менее 29. Выиграл тот, кто сделал последний ход. Первым ходит Петя.
FINISH = 29


def moves(s: int) -> list[int]:
    return [s + 1, 2 * s]


# Тот, кто ходит при s камнях, выиграет не больше чем за k своих ходов при любой игре соперника.
def can_win(s: int, k: int) -> bool:
    for t in moves(s):
        if t >= FINISH or (k > 1 and must_lose(t, k - 1)):
            return True
    return False

# Тот, кто ходит при s камнях, проиграет: соперник выиграет не больше чем за k своих ходов.
def must_lose(s: int, k: int) -> bool:
    for t in moves(s):
        if t >= FINISH or not can_win(t, k):
            return False
    return True

# Метка позиции для того, кто ходит: 'W1', 'L1', 'W2', 'L2' или '' (если ни одна из них).
def label(s: int) -> str:
    if can_win(s, 1): return 'W1'
    if must_lose(s, 1): return 'L1'
    if can_win(s, 2): return 'W2'
    if must_lose(s, 2): return 'L2'
    return '-'


# №19 (демо 2027): минимальное s, при котором Ваня выиграл своим первым ходом.
def q19():
    # for s in range(1, FINISH):
    #     if label(s) == 'W1':
    #         continue
    #     for t in moves(s):
    #         if label(t) == 'W1':
    #             return s
    for s in range(1, FINISH):
        if can_win(s, 1):
            continue
        for t in moves(s):
            if can_win(t, 1):
                return s


# №20: все s, при которых Петя не может выиграть за один ход, но выигрывает своим вторым ходом.
def q20():
    res = []
    for s in range(1, FINISH):
        if not can_win(s, 1) and can_win(s, 2):
            res.append(s)
    return res


# №21: минимальное s, при котором Ваня выигрывает первым или вторым ходом, но гарантированно первым не может.
def q21():
    for s in range(1, FINISH):
        if not must_lose(s, 1) and must_lose(s, 2):
            return s


print(q19(), 8)
print(q20(), [7, 13])
print(q21(), 12)



















# 19
for s in range(1, FINISH):
    if not can_win(s, 1) and must_lose(s, 1):
        s

# 20
for s in range(1, FINISH):
    if not can_win(s, 1) and can_win(s, 2):
        s

# 21
for s in range(1, FINISH):
    if not must_lose(s, 1) and must_lose(s, 2):
        s