# Задача 1: Employee с @property
#
# Класс сотрудника с защитой зарплаты.
#
# Атрибуты: name, _salary
# @property salary: только чтение
# @salary.setter: нельзя задать меньше 0
#

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError('Нельзя задать зарплату меньше 0.')
        
        self._salary = value

# Проверка
e = Employee("Иван", 50000)
print(e.salary)
e.salary = 60000
print(e.salary)
e.salary = -100   # должно упасть
