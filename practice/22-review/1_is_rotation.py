# Задача: Циклический сдвиг строки
# Проверь за один проход, является ли строка s2 циклическим сдвигом строки s1.
# Например: "abcde" и "cdeab" -> True
#
# Вход: s1, s2 - строки одинаковой длины
# Выход: True / False


def is_rotation(s1, s2):
    # TODO: реализуй здесь
    pass


print(is_rotation("abcde", "cdeab"))  # True
print(is_rotation("abcde", "abced"))  # False
print(is_rotation("", ""))            # True
print(is_rotation("a", "a"))          # True
