# Задание ФИПИ, группа 106EB7.
# Две кучи: в первой 5 камней, во второй s камней, 1 <= s <= 53. Позиция - пара (камни в первой, камни во второй).
# Ход: добавить 1 камень в одну из куч или увеличить одну из куч в 2 раза.
# Игра кончается, когда в двух кучах вместе не менее 59 камней. Выиграл тот, кто сделал последний ход. Первым ходит Петя.
FIRST = 5
FINISH = 59


def moves(pos: tuple[int, int]) -> list[tuple[int, int]]:
    a, b = pos
    return [
        (a + 1, b),
        (a, b + 1),
        (2 * a, b),
        (a, b * 2)
    ]


# Игра кончилась: в двух кучах вместе не менее FINISH камней.
def is_finish(pos):
    a, b = pos
    return a + b >= FINISH


# Тот, кто ходит в позиции pos, выиграет не больше чем за k своих ходов при любой игре соперника.
def can_win(pos, k):
    for t in moves(pos):
        if is_finish(t) or (k > 1 and must_lose(t, k - 1)):
            return True
    return False


# Тот, кто ходит в позиции pos, проиграет: соперник выиграет не больше чем за k своих ходов.
def must_lose(pos, k):
    for t in moves(pos):
        if is_finish(t) or not can_win(t, k):
            return False
    return True


# №19: минимальное s, при котором Ваня выиграл своим первым ходом после неудачного хода Пети.
def q19() -> int:
    for s in range(1, 53 + 1):
        pos = (FIRST, s)
        if can_win(pos, 1):
            continue
        for t in moves(pos):
            if can_win(t, 1):
                return s


# №20: два наименьших s, при которых Петя не может выиграть за один ход, но выигрывает своим вторым ходом.
def q20() -> list[int]:
    res = []
    for s in range(1, 53 + 1):
        pos = (FIRST, s)
        if not can_win(pos, 1) and can_win(pos, 2):
            res.append(s)

    return res


# №21: минимальное s, при котором Ваня выигрывает первым или вторым ходом, но гарантированно первым не может.
def q21() -> int:
    for s in range(1, 53 + 1):
        pos = (FIRST, s)
        if not must_lose(pos, 1) and must_lose(pos, 2):
            return s
    




print(moves((20, 30)), [(21, 30), (20, 31), (40, 30), (20, 60)])
print(is_finish((5, 54)), True)
print(can_win((5, 27), 1), True)
print(can_win((5, 26), 1), False)
print(q19(), 14)
print(q20(), [24, 26])
print(q21(), 23)
