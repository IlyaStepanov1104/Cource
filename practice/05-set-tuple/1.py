player1 = ["меч", "щит", "зелье", "лук", "стрелы"]
player2 = ["щит", "зелье", "броня", "меч", "факел"]

# Напиши функцию common_items(p1, p2)
# Вернуть set с общими предметами

def common_items(p1, p2):
    set1 = set(p1)
    set2 = set(p2)
    return set1 & set2

print(common_items(player1, player1))