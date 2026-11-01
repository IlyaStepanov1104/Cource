# Дан список точек на плоскости - [(0, 0), (3, 4), (1, 1)]. Найти ближайшую пару (пару с минимальным расстоянием)
# Повторения - нет
# Порядок - нет
# combination

from itertools import combinations

def dist(p1, p2):
    return sum((p1[i] - p2[i] ) ** 2 for i in range(len(p1)))
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2

def closest_pair(points):
    best_pair = None
    min_dist = float('inf')

    for p1, p2 in combinations(points, 2):
        if dist(p1, p2) < min_dist:
            best_pair = (p1, p2)
            min_dist = dist(p1, p2)
    return best_pair

print(closest_pair([(0, 0, 0, 0, 0), (3, 4, 4, 4, 5), (1, 1, 1, 1, 1), (100, 0, 0, 0, 0), (-5, 2, 1, 0, 0)]))