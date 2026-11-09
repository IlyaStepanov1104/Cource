def greedy_set_cover(states_needed, stantions):
    remainder = states_needed.copy()
    final_stantions = set()

    while remainder:
        best_stantion = None
        best_covered = set()

        for stantion, states in stantions.items():
            covered = remainder & states
            if len(covered) > len(best_covered):
                best_stantion = stantion
                best_covered = covered

        final_stantions.add(best_stantion)
        remainder -= best_covered

    return final_stantions

states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
stations = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"},
}

selected = greedy_set_cover(states_needed, stations)
covered = set().union(*(stations[name] for name in selected))

print("Станции:", sorted(selected))
print("Количество:", len(selected))
print("Все штаты покрыты:", states_needed <= covered)