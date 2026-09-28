# 5 домов A, B, C, D, E. Пожарные станции - в A и E.
# Дороги: A-B=3, B-C=4, C-D=2, D-E=3, B-D=6.
# Для каждого дома найти время до ближайшей станции.


def nearest_station_time(graph: dict[str, list[tuple[str, int]]], sources: list[str]) -> dict[str, int]:
    pass


graph = {
    "A": [("B", 3)],
    "B": [("A", 3), ("C", 4), ("D", 6)],
    "C": [("B", 4), ("D", 2)],
    "D": [("C", 2), ("B", 6), ("E", 3)],
    "E": [("D", 3)],
}

print(nearest_station_time(graph, ["A", "E"]), {"A": 0, "B": 3, "C": 5, "D": 3, "E": 0})
