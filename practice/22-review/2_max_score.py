# Задача: Имена с максимальным баллом
# Дан словарь {имя: балл}. Верни список имён с максимальным баллом
# (максимум могут делить несколько человек).
#
# Вход: score - словарь {str: int}
# Выход: список str


def names_with_max_score(score):
    max_score = max(score.values())
    result = []
    for key in score.keys():
        if score[key] == max_score:
            result.append(key)
            
    return result


print(names_with_max_score({"Аня": 90, "Боря": 75, "Вика": 90}))  # ['Аня', 'Вика']
print(names_with_max_score({"Аня": 90}))                          # ['Аня']
print(names_with_max_score({"Аня": 50, "Боря": 50, "Вика": 50}))  # ['Аня', 'Боря', 'Вика']