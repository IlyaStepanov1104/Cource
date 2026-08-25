# Задача: Место вставки (бинарный поиск)
# Дан отсортированный массив. Найди индекс, куда нужно вставить target,
# чтобы массив остался отсортированным. Перебор запрещён - только
# бинарный поиск через left/right.
#
# Вход: arr - отсортированный список int, target - int
# Выход: индекс вставки (int)


def insert_position(arr, target):
    left, right = 0, len(arr)
    # TODO: сдвигай left и right, пока не найдёшь место вставки
    pass


print(insert_position([2, 4, 6, 8, 10, 12], 7))   # 3
print(insert_position([2, 4, 6, 8, 10, 12], 2))   # 0
print(insert_position([2, 4, 6, 8, 10, 12], 13))  # 6
print(insert_position([], 5))                     # 0
