from collections import deque


# LeetCode 913. Cat and Mouse.
# Неориентированный граф: graph[v] - соседи вершины v. Мышь стоит в 1, кот в 2, нора - 0.
# Ходят по очереди, первой ходит мышь; стоять на месте нельзя, кот не может зайти в 0.
# Мышь в норе - победа мыши, кот на мыши - победа кота, бесконечная игра - ничья.
# Вернуть 1, если выигрывает мышь, 2 - если кот, 0 - ничья.
def cat_mouse_game(graph: list[list[int]]) -> int:
    n = len(graph)
    MOUSE, CAT = 0, 1
    # res[m][c][t] - кто выигрывает: 0 - неизвестно, 1 - мышь, 2 - кот
    # m - вершина, где стоит мышь, c - кот, t - чей ход
    res = [[[0, 0] for _ in range(n)] for _ in range(n)]
    # cnt[m][c][t] - количество не исследованных путей
    cnt = [[[len(graph[m]), sum(1 for to in graph[c] if to != 0)] for c in range(n)] for m in range(n)]
    
    q = deque()

    for c in range(1, n):
        for t in (MOUSE, CAT):
            res[0][c][t] = 1
            q.append((0, c, t))
            res[c][c][t] = 2
            q.append((c, c, t))

    while q:
        m, c, t = q.popleft()
        winner = res[m][c][t]
        if t == MOUSE:
            prev = [(m, prev_c, CAT) for prev_c in graph[c] if prev_c != 0]
        else:
            prev = [(prev_m, c, MOUSE) for prev_m in graph[m]]

        for pm, pc, pt in prev:
            if res[pm][pc][pt] != 0:
                continue
            mover = 1 if pt == MOUSE else 2
            if winner == mover:
                res[pm][pc][pt] = winner
                q.append((pm, pc, pt))
            else:
                cnt[pm][pc][pt] -= 1
                if cnt[pm][pc][pt] == 0:
                    res[pm][pc][pt] = winner
                    q.append((pm, pc, pt))

    return res[1][2][MOUSE]

print(cat_mouse_game([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]), 0)
print(cat_mouse_game([[1, 3], [0], [3], [0, 2]]), 1)
print(cat_mouse_game([[2, 3], [2], [0, 1], [0]]), 2)
print(cat_mouse_game([[1, 2], [0, 2], [0, 1]]), 1)
print(cat_mouse_game([[2, 3], [3, 4], [0, 4], [0, 1], [1, 2]]), 1)
