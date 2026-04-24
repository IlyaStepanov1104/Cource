# Задача 3: Температура
#
# Альтернативные конструкторы через @classmethod.
#
# Temperature: хранит celsius
# @classmethod from_fahrenheit(f): строит объект из градусов F
#     формула: c = (f - 32) * 5 / 9
# @classmethod from_kelvin(k): строит из кельвинов
#     формула: c = k - 273.15
#
# t1 = Temperature(25)
# t2 = Temperature.from_fahrenheit(77)   # 25 C
# t3 = Temperature.from_kelvin(300)      # 26.85 C
#
# print(t1.celsius, t2.celsius, t3.celsius)


class Temperature:
    pass


# Проверка
# t1 = Temperature(25)
# t2 = Temperature.from_fahrenheit(77)
# t3 = Temperature.from_kelvin(300)
# print(t1.celsius, t2.celsius, t3.celsius)
