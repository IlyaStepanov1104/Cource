from collections import deque


# 2290. Minimum Obstacle Removal to Reach Corner
# Сетка из 0 (свободно) и 1 (препятствие). Идём из левого верхнего угла
# в правый нижний, ходы по четырём направлениям. Препятствие можно убрать.
# Вернуть минимальное число препятствий, которые придётся убрать.


def minimum_obstacles(n: int, connections: list[list[int]]) -> int:
    revert_E = [[] for _ in range(n)]
    E = [[] for _ in range(n)]
    for a, b in connections:
        E[a].append(b)
        revert_E[b].append(a)
    visited = [False for _ in range(n)]
    visited[0] = True
    q = deque([0])
    count = 0
    while q:
        v = q.popleft()
        for to in E[v]:
            if not visited[to]:
                visited[to] = True
                q.append(to)
                count += 1
        for to in revert_E[v]:
            if not visited[to]:
                visited[to] = True
                q.append(to)
    return count


print(minimum_obstacles(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
