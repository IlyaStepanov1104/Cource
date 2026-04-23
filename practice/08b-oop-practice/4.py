# Задача 4: Транспорт
#
# Наследование с расширением через super().
#
# Vehicle: brand, max_speed, метод info() -> "Tesla, до 250 км/ч"
# Car(Vehicle): +seats, info() через super() -> "..., 5 мест"
# ElectricCar(Car): +battery, info() через super() -> "..., батарея 100 кВт"
#
# tesla = ElectricCar("Tesla", 250, 5, 100)
# print(tesla.info())
# Tesla, до 250 км/ч, 5 мест, батарея 100 кВт


class Vehicle:
    pass


# Проверка
# car = Car("Toyota", 200, 5)
# print(car.info())
# tesla = ElectricCar("Tesla", 250, 5, 100)
# print(tesla.info())
